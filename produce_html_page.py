from census_blocks import RADII


row_template = """
<tr>
    <td style="width: 30%;">
        <span class="text value">$statname:</span>
    </td>
    <td style="width: 20%;">
        <span class="text value">$statval</span>
    </td>
    <td style="width: 30%;">
        <span class="text ordinal">$ordinal of $total $types</span>
    </td>
    <td style="width: 20%;">
        <span class="text ordinal">$percentile</span>
    </td>
</tr>
"""


def create_page(row):
    statistic_names = {
        "population": "Population",
        "sd": "AW Density",
        **{f"ad_{k}": f"PW Density (r={format_radius(k)})" for k in RADII},
    }

    with open("html_templates/named_region_page.html") as f:
        html = f.read()
    html = html.replace("$shortname", row.shortname)
    html = html.replace("$longname", row.longname)
    html = html.replace("$source", row.source)
    table_rows = []
    for stat in statistic_names:
        row_text = row_template
        row_text = row_text.replace("$statname", statistic_names[stat])
        row_text = row_text.replace("$statval", format_statistic(stat, row[stat]))
        row_text = row_text.replace("$types", row["type"] + "s")
        row_text = row_text.replace("$ordinal", f'{row[stat, "ordinal"]:.0f}')
        row_text = row_text.replace("$total", f'{row[stat, "total"]:.0f}')
        row_text = row_text.replace(
            "$percentile",
            render_percentile(100 * (1 - row[stat, "ordinal"] / row[stat, "total"])),
        )
        table_rows.append(row_text)
    html = html.replace("$rows", "\n".join(table_rows))

    name = f"{row.longname}.html"
    with open(f"outputs/webpages/{name}", "w") as f:
        f.write(html)
    return name


def add_ordinals(frame, keys):
    frame = frame.copy()
    for k in keys:
        frame[k, "ordinal"] = frame[k].rank(ascending=False)
        frame[k, "total"] = frame[k].shape[0]
    return frame


def format_population(x):
    if x > 1e6:
        return f"{x / 1e6:.1f}m"
    elif x > 1e3:
        return f"{x / 1e3:.1f}k"
    else:
        return f"{x:.0f}"


def format_density(x):
    if x > 10:
        return f"{x:.0f}/km²"
    elif x > 1:
        return f"{x:.1f}/km²"
    else:
        return f"{x:.2f}/km²"


def format_statistic(name, x):
    if name == "population":
        return format_population(x)
    return format_density(x)


def format_radius(x):
    if x < 1:
        return f"{x * 1000:.0f}m"
    else:
        assert x == int(x)
        return f"{x:.0f}km"


def render_percentile(pct):
    """
    Take a percentile value like 33.2 and return "33rd percentile".
    """
    pct = round(pct)
    if pct % 10 == 1:
        suffix = "st"
    elif pct % 10 == 2:
        suffix = "nd"
    elif pct % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{pct}{suffix} percentile"
