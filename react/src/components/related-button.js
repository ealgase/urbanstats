
import React from 'react';

export { Related, relationship_key };
import { article_link } from "../navigation/links.js";
import { is_historical_cd } from '../utils/is_historical.js';
import { CheckboxSetting } from "./sidebar.js";

import "./related.css";

function relationship_key(article_type, other_type) {
    return "related__" + article_type + "__" + other_type;
}
function to_name(name) {
    return name.toLowerCase().replaceAll(" ", "_");
}

class RelatedButton extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const classes = `button b_${to_name(this.props.row_type)}`
        return (
            <li className="linklistel">
                <a
                    className={classes}
                    href={article_link(this.props.longname)}>{this.props.shortname}
                </a>
            </li>
        );
    }
}

class RelatedList extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let by_type_key = [];
        for (let i = 0; i < this.props.regions.length; i++) {
            let row = this.props.regions[i];
            if (by_type_key.length == 0 || by_type_key[by_type_key.length - 1].type != row.row_type) {
                by_type_key.push({ type: row.row_type, regions: [] });
            }
            by_type_key[by_type_key.length - 1].regions.push(row);
        }
        return (
            <ul className="list_of_lists">
                <li className="linklistelfirst">{this.display_name()}</li>
                {by_type_key.map((row, i) =>
                    <CheckableRelatedList
                        key={i}
                        {...row}
                        article_type={this.props.article_type}
                        settings={this.props.settings}
                        set_setting={this.props.set_setting}
                    />)}
            </ul>
        );
    }

    display_name() {
        let name = this.props.name;
        name = name.replace("_", " ");
        // title case
        name = name.replace(/\w\S*/g, function (txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        });
        return name;
    }
}

class CheckableRelatedList extends React.Component {
    render() {
        let key = this.key_for_setting();
        return (
            <li className="list_of_lists">
                <div style={{ display: "flex" }}>
                    <div className="linkbox">
                        <CheckboxSetting
                            name=""
                            setting_key={key}
                            settings={this.props.settings}
                            set_setting={this.props.set_setting} />
                    </div>
                    <ul className="linklist">
                        {this.props.regions.map((row, i) => <RelatedButton key={i} {...row} />)}
                    </ul>
                </div>
            </li>
        )
    }

    key_for_setting() {
        return relationship_key(this.props.article_type, this.props.type);
    }
}

class Related extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {

        let elements = [];
        for (var [key, value] of Object.entries(this.props.related)) {
            if (!this.props.settings.show_historical_cds) {
                value = value.filter((row) => !is_historical_cd(row.longname));
            }
            if (value.length > 0) {
                elements.push(
                    <RelatedList
                        key={key}
                        name={key}
                        regions={value}
                        article_type={this.props.article_type}
                        settings={this.props.settings}
                        set_setting={this.props.set_setting}
                    />
                );
            }
        }

        return (
            <div className="related_areas">
                {elements}
            </div>
        );
    }
}