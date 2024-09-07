import { TableCheckboxSettings } from '../page_template/settings'
import { universe_is_american } from '../universe'
import { Article, IExtraStatistic } from '../utils/protos'

export interface ExtraStat {
    stat: IExtraStatistic
    universe_total: number
}

export interface ArticleRow {
    statval: number
    ordinal: number
    overallOrdinal: number
    percentile_by_population: number
    statistic_category: string
    statcol: string
    statname: string
    statpath: string
    explanation_page: string
    article_type: string
    total_count_in_class: number
    total_count_overall: number
    _index: number
    rendered_statname: string
    extra_stat?: ExtraStat
}

const index_list_info = require('../data/index_lists.json') as {
    index_lists: {
        universal: number[]
        gpw: number[]
        usa: number[]
    }
    type_to_has_gpw: Record<string, boolean>
}

function lookup_in_compressed_sequence(seq: [number, number][], idx: number): number {
    // translation of produce_html_page.py::lookup_in_compressed_sequence
    for (const [value, length] of seq) {
        if (idx < length) {
            return value
        }
        idx -= length
    }
    throw new Error('Index out of bounds')
}

export function for_type(universe: string, statcol: string, typ: string): number {
    const statnames = require('../data/statistic_list.json') as string[]
    const idx = statnames.indexOf(statcol)
    const counts_by_universe = require('../data/counts_by_article_type.json') as Record<string, Record<string, [number, number][]>>
    const counts_by_type = counts_by_universe[universe][typ]

    return lookup_in_compressed_sequence(counts_by_type, idx)
}

function compute_indices(longname: string, typ: string): number[] {
    // translation of produce_html_page.py::indices

    const lists = index_list_info.index_lists
    let result: number[] = []
    result = result.concat(lists.universal)
    if (index_list_info.type_to_has_gpw[typ]) {
        result = result.concat(lists.gpw)
    }
    // else {
    if (longname.includes('USA')) {
        result = result.concat(lists.usa)
    }
    // sort result by numeric value
    return result.sort((a, b) => a - b)
}

export function load_article(universe: string, data: Article, settings: TableCheckboxSettings, exclusively_american: boolean): readonly [ArticleRow[], number[]] {
    // index of universe in data.universes
    const universe_index = data.universes.indexOf(universe)
    const article_type = data.articleType

    const categories = require('../data/statistic_category_list.json') as string[]
    const names = require('../data/statistic_name_list.json') as string[]
    const paths = require('../data/statistic_path_list.json') as string[]
    const stats = require('../data/statistic_list.json') as string[]
    const explanation_page = require('../data/explanation_page.json') as string[]

    const extra_stats = require('../data/extra_stats.json') as [number, number][]
    const extra_stat_idx_to_col = extra_stats.map(xy => xy[0])

    const indices = compute_indices(data.longname, article_type)

    const modified_rows: ArticleRow[] = data.rows.map((row_original, row_index) => {
        const i = indices[row_index]
        // fresh row object
        let extra_stat: ExtraStat | undefined = undefined
        if (extra_stat_idx_to_col.includes(i)) {
            const extra_stat_idx = extra_stat_idx_to_col.indexOf(i)
            const [, universe_total_idx] = extra_stats[extra_stat_idx]
            extra_stat = {
                stat: data.extraStats[extra_stat_idx],
                universe_total: data.rows.find((_, universe_row_index) => indices[universe_row_index] === universe_total_idx)!.statval!,
            }
        }
        return {
            statval: row_original.statval!,
            ordinal: row_original.ordinalByUniverse![universe_index],
            overallOrdinal: row_original.overallOrdinalByUniverse![universe_index],
            percentile_by_population: row_original.percentileByPopulationByUniverse![universe_index],
            statistic_category: categories[i],
            statcol: stats[i],
            statname: names[i],
            statpath: paths[i],
            explanation_page: explanation_page[i],
            article_type,
            total_count_in_class: for_type(universe, stats[i], article_type),
            total_count_overall: for_type(universe, stats[i], 'overall'),
            _index: i,
            rendered_statname: render_statname(i, names[i], exclusively_american),
            extra_stat,
        } satisfies ArticleRow
    })
    const filtered_rows = modified_rows.filter((row) => {
        if (universe_is_american(universe)) {
            if (index_list_info.index_lists.gpw.includes(indices[row._index])) {
                return false
            }
        }
        else {
            if (index_list_info.index_lists.usa.includes(indices[row._index])) {
                return false
            }
        }
        return settings[`show_statistic_${row.statistic_category}`]
    })

    const filtered_indices = filtered_rows.map(x => x._index)

    return [filtered_rows, filtered_indices] as const
}

export function render_statname(statindex: number, statname: string, exclusively_american: boolean): string {
    const usa_stat = index_list_info.index_lists.usa.includes(statindex)
    if (!exclusively_american && usa_stat) {
        return `${statname} (USA only)`
    }
    return statname
}
