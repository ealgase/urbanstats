import pandas as pd
from shapefiles import shapefiles
from output_geometry import produce_all_geometry_json
from stats_for_shapefile import compute_statistics_for_shapefile
from produce_html_page import add_ordinals, get_statistic_names


folder = "/home/kavi/temp/webpages"


def full_shapefile():
    full = [compute_statistics_for_shapefile(shapefiles[k]) for k in shapefiles]
    full = pd.concat(full)
    full = full[full.population > 0].copy()
    full = pd.concat(
        [add_ordinals(full[full.type == x]) for x in sorted(set(full.type))]
    )
    full = full.sort_values("population")[::-1]
    return full


def next_prev(full):
    statistic_names = get_statistic_names()
    by_statistic = {k: {} for k in statistic_names}
    for statistic in statistic_names:
        s_full = full.sort_values(statistic)[::-1]
        names = list(s_full.longname)
        for prev, current, next in zip([None, *names[:-1]], names, [*names[1:], None]):
            by_statistic[statistic][current] = prev, next

    return by_statistic


def next_prev_within_type(full):
    statistic_names = get_statistic_names()
    by_statistic = {k: {} for k in statistic_names}
    for type in sorted(set(full.type)):
        result = next_prev(full[full.type == type])
        for statistic in statistic_names:
            by_statistic[statistic].update(result[statistic])

    return by_statistic


def main():
    full = full_shapefile()
    long_to_short = dict(zip(full.longname, full.shortname))

    produce_all_geometry_json(folder, set(long_to_short))


if __name__ == "__main__":
    main()
