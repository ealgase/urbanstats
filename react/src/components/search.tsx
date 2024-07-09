import React from 'react';

import { loadProtobuf } from '../load_json';
import { is_historical_cd } from '../utils/is_historical';
import "../common.css";
import { SearchIndex } from '../utils/protos';

export const SearchBox = (props: {
    on_change: (inp: string) => void, autoFocus: boolean, placeholder: string, style: any, settings: any
}) => {

    const [matches, setMatches] = React.useState<string[]>([]);
    const [matchesStale, setMatchesStale] = React.useState(false);
    const [indexCache, setIndexCache] = React.useState<SearchIndex | undefined>(undefined);
    const [indexCacheUninitialized, setIndexCacheUninitialized] = React.useState(true);
    const [firstCharacter, setFirstCharacter] = React.useState<string | undefined>(undefined);
    const [focused, setFocused] = React.useState(0);

    const form = React.useRef<HTMLFormElement>(null);
    const textbox = React.useRef<HTMLInputElement>(null);
    const dropdown = React.useRef<HTMLDivElement>(null);


    const searchbox_dropdown_item_style = (idx: number) => {
        return {
            padding: "0.5em",
            cursor: "pointer",
            backgroundColor: (focused === idx) ? "#ffe0e0" : undefined
        };
    }

    const onFormSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        let terms = matches;
        if (terms.length > 0) {
            props.on_change(terms[focused])
        }
        return false;
    }

    const get_input = () => {
        var input = textbox.current!.value;
        input = normalize(input);
        return input;
    }

    const reload_cache = () => {
        const input = get_input();
        if (input == '') {
            setIndexCacheUninitialized(false);
            setMatchesStale(false);
            setMatches([]);
            return;
        }
        const currentFirstCharacter = input[0];
        if (firstCharacter != currentFirstCharacter) {
            setFirstCharacter(currentFirstCharacter);
            (async () => {
                setFirstCharacter(currentFirstCharacter);
                setIndexCache(await loadProtobuf(`/index/pages_${currentFirstCharacter}.gz`, "SearchIndex"));
                setIndexCacheUninitialized(false);
                setMatchesStale(true);
            })();
            return;
        }
        if (indexCacheUninitialized) {
            return;
        }
    }

    const onTextBoxKeyUp = (event: React.KeyboardEvent<HTMLInputElement>) => {

        reload_cache();
        // this.setState({ matches_stale: true });
        setMatchesStale(true);

        // if down arrow, then go to the next one
        let dropdowns = document.getElementsByClassName("searchbox-dropdown-item");
        if (dropdowns.length > 0) {
            if (event.key == "ArrowDown") {
                setFocused((focused + 1) % dropdowns.length)
            }
            if (event.key == "ArrowUp") {
                setFocused((focused - 1) % dropdowns.length)
            }
        }
    }

    const update_matches = async () => {
        const input = get_input();
        if (input == '') {
            if (matches.length > 0) {
                setMatches([]);
            }
            return;
        }
        const values = indexCache!.elements;
        const priorities = indexCache!.priorities;
        let matches_new = [];
        for (let i = 0; i < values.length; i++) {
            let match_count = is_a_match(input, normalize(values[i]));
            if (match_count == 0) {
                continue;
            }
            if (!props.settings.show_historical_cds) {
                if (is_historical_cd(values[i])) {
                    continue;
                }
            }
            if (is_international_duplicate(values[i])) {
                continue;
            }
            matches_new.push([match_count, i, match_count - priorities[i] / 10]);
        }
        matches_new = top_10(matches_new);
        matches_new = matches_new.map(idx => values[idx]);
        setMatches(matches_new);
        setMatchesStale(false);
    }

    if (matchesStale && !indexCacheUninitialized) {
        update_matches();
    }

    return (
        <form
            autoComplete="off" ref={form}
            style={{ marginBlockEnd: "0em", position: "relative", width: "100%" }
            }
            onSubmit={onFormSubmit}
        >
            <input
                autoFocus={props.autoFocus}
                ref={textbox}
                id="searchbox"
                type="text"
                className="serif"
                style={{ backgroundColor: "#fff8f0", borderWidth: "0.1em", ...props.style }}
                placeholder={props.placeholder}
                onKeyUp={onTextBoxKeyUp}
            />

            <div ref={dropdown} style={
                {
                    position: "absolute",
                    width: "100%",
                    maxHeight: "20em",
                    overflowY: "auto",
                    backgroundColor: "#f7f1e8",
                    borderRadius: "0.25em",
                    zIndex: "1"
                }
            }>
                {
                    matches.map((location, idx) =>
                    (
                        <div
                            key={location}
                            className="serif searchbox-dropdown-item"
                            style={searchbox_dropdown_item_style(idx)}
                            onClick={() => props.on_change(matches[idx])}
                            onMouseOver={() =>
                                setFocused(idx)
                            }
                        > {location} </div>
                    )
                    )
                }
            </div>
        </form>
    );
}

function top_10(matches: number[][]) {
    const num_prioritized = 3;
    const sort_key = (idx: number) => {
        return (a: number[], b: number[]) => {
            if (a[idx] != b[idx]) {
                return b[idx] - a[idx];
            }
            return a[1] - b[1];
        }
    };
    matches.sort(sort_key(2));
    let overall_matches = [];
    for (let i = 0; i < Math.min(num_prioritized, matches.length); i++) {
        overall_matches.push(matches[i][1]);
        matches[i][0] = -100;
    }
    matches.sort(sort_key(0));
    for (let i = 0; i < Math.min(10 - num_prioritized, matches.length); i++) {
        if (matches[i][0] == -100) {
            break;
        }
        overall_matches.push(matches[i][1]);
    }
    return overall_matches;
}


/*
    Check whether a is a substring of b (does not have to be contiguous)
 
*/
function is_a_match(a: string, b: string) {
    let i = 0;
    let match_count = 0;
    let prev_match = true;
    for (let j = 0; j < b.length; j++) {
        if (a[i] == b[j]) {
            i++;
            if (prev_match) {
                match_count++;
            }
            prev_match = true;
        } else {
            prev_match = false;
        }
        if (i == a.length) {
            return match_count + 1;
        }
    }
    return 0;
}

function normalize(a: string) {
    return a.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function is_international_duplicate(x: string) {
    // ends with [SN], USA
    return x.endsWith(" [SN], USA");
}