#!/usr/bin/env python3
"""Wrap the derived radial SVG into a standalone, shareable image: same map,
with a title, live stat counts, and the three-colour legend baked in -- so the
file explains itself with no surrounding HTML. Reads critical_dag.json for the
counts and prize_dag_critical_radial.svg for the graph; writes
prize_map_shareable.svg next to them. Content is tight-cropped to the map's
bounding box. Idempotent; safe to call from the build."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def _find(base):
    for cand in (
        os.path.join(base, "..", "orbit"),
        os.path.join(base, "..", "data", "prize-dag"),
    ):
        svg = os.path.join(cand, "prize_dag_critical_radial.svg")
        cd = os.path.join(cand, "critical_dag.json")
        if os.path.exists(svg) and os.path.exists(cd):
            return cand, svg, cd
    raise SystemExit("shareable-svg: source svg / critical_dag.json not found")


def build(base=HERE):
    outdir, svg_path, cd_path = _find(base)
    svg = open(svg_path).read()
    cd = json.load(open(cd_path))
    c = {"PROVED": 0, "CONDITIONAL": 0, "UNPROVED": 0}
    for n in cd["nodes"]:
        c[n["label"]] = c.get(n["label"], 0) + 1
    total = len(cd["nodes"])

    body = svg[svg.index("</defs>") + len("</defs>"):svg.rindex("</svg>")]
    # strip the embedded full-canvas background rect (it would paint over the
    # header once the crop translation is applied)
    body = re.sub(r'<rect width="\d+" height="\d+" fill="#0b1220"/>', "", body, count=1)
    defs = svg[svg.index("<defs>"):svg.index("</defs>") + len("</defs>")]

    # tight content bounding box from node positions (circles carry cx/cy)
    pts = [(float(x), float(y)) for x, y in
           re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)"', body)]
    PAD = 170.0
    minx = min(p[0] for p in pts) - PAD
    maxx = max(p[0] for p in pts) + PAD
    miny = min(p[1] for p in pts) - PAD
    maxy = max(p[1] for p in pts) + PAD
    W = maxx - minx
    TOP, BOT = 360.0, 300.0
    NEW_H = (maxy - miny) + TOP + BOT

    ink, muted = "#dbe4f0", "#7e8ba3"
    pal = [("PROVED", "#15803d", f'{c["PROVED"]} proved'),
           ("CONDITIONAL", "#f59e0b", f'{c["CONDITIONAL"]} conditional'),
           ("UNPROVED", "#f87171", f'{c["UNPROVED"]} unproved')]

    # header: title + subtitle + stat row
    hdr = [
        f'<text x="{W/2:.0f}" y="150" fill="{ink}" font-size="104" '
        f'font-weight="600" text-anchor="middle">rs-mca &#183; proximity prize '
        f'&#183; critical orbit</text>',
        f'<text x="{W/2:.0f}" y="238" fill="{muted}" font-size="52" '
        f'text-anchor="middle">The prize at the centre &#8212; implication flows '
        f'inward. {total} critical nodes.</text>',
    ]
    seg = W / len(pal)
    for i, (_k, col, txt) in enumerate(pal):
        cx = seg * (i + 0.5)
        hdr.append(f'<text x="{cx:.0f}" y="330" fill="{col}" font-size="64" '
                   f'font-weight="700" text-anchor="middle">{txt}</text>')

    # footer: two lines (fits the cropped width)
    fy = TOP + (maxy - miny) + 110
    leg = [f'<text x="{W/2:.0f}" y="{fy:.0f}" fill="{muted}" '
           f'font-size="44" text-anchor="middle">Every arc is a requirement, '
           f'drawn in its source&#8217;s colour; rings are implication depth.</text>',
           f'<text x="{W/2:.0f}" y="{fy+72:.0f}" fill="{ink}" font-size="46" '
           f'font-weight="600" text-anchor="middle">Prove the {c["UNPROVED"]} '
           f'red leaves and the prize follows.</text>']

    out = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {NEW_H:.0f}" '
        f'font-family="Helvetica,Arial,sans-serif">\n{defs}\n'
        f'<rect width="{W:.0f}" height="{NEW_H:.0f}" fill="#0b1220"/>\n'
        + "\n".join(hdr) + "\n"
        + f'<g transform="translate({-minx:.0f},{TOP - miny:.0f})">' + body + "</g>\n"
        + "\n".join(leg) + "\n</svg>\n"
    )
    dest = os.path.join(outdir, "prize_map_shareable.svg")
    open(dest, "w").write(out)
    print(f"shareable svg: {dest}  ({total} nodes, {os.path.getsize(dest)//1024} KB)")
    return dest


if __name__ == "__main__":
    build()
