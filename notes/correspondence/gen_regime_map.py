#!/usr/bin/env python3
"""Emit prize/notes/correspondence/regime_map.svg — balance-coordinate map (v2 layout)."""
import math

W, H = 1060, 660
X0, X1 = 100, 1015
Y0, Y1 = 100, 556
TMIN, TMAX = -11.2, 7.2
LMIN, LMAX = 3, 44

def tx(delta):
    t = math.copysign(math.log10(1 + abs(delta)), delta) if delta else 0.0
    return X0 + (t - TMIN) / (TMAX - TMIN) * (X1 - X0)

def ty(log2n):
    return Y1 - (log2n - LMIN) / (LMAX - LMIN) * (Y1 - Y0)

svg = []
svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="system-ui, -apple-system, 'Segoe UI', sans-serif">
<style>
  :root {{ --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
          --grid:#e1e0d9; --axis:#c3c2b7;
          --s1:#2a78d6; --s2:#1baf7a; --s3:#eda100; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781;
            --grid:#2c2c2a; --axis:#383835;
            --s1:#3987e5; --s2:#199e70; --s3:#c98500; }}
  }}
  text {{ fill: var(--ink2); font-size: 12px; }}
  .title {{ fill: var(--ink); font-size: 17px; font-weight: 650; }}
  .sub   {{ fill: var(--ink2); font-size: 12.5px; }}
  .tick  {{ fill: var(--muted); font-size: 11px; font-variant-numeric: tabular-nums; }}
  .axlab {{ fill: var(--muted); font-size: 12px; }}
  .lab   {{ font-size: 11.5px; }}
  .lab1  {{ fill: var(--ink); font-weight: 600; }}
  .lab2  {{ fill: var(--ink); font-weight: 600; }}
  .lab3  {{ fill: var(--ink); font-weight: 600; }}
  .leg   {{ fill: var(--ink2); font-size: 12px; }}
</style>
<rect width="{W}" height="{H}" fill="var(--surface)"/>
<text x="{X0}" y="34" class="title">Regime map — both programs on the balance coordinate</text>
<text x="{X0}" y="54" class="sub">&#916; = log&#8322;(#configurations) &#8722; log&#8322;(#values in the true value field), symlog</text>
<text x="{X0}" y="70" class="sub">exact numbers in REGIME_MAP.md</text>''')

# legend — top right block, clear of subtitle
lx = 700
for i,(cls, name) in enumerate([("--s1","upstream program"),("--s2","our floors' evidence"),("--s3","catch #11 (one row, two readings)")]):
    yy = 26 + i*17
    svg.append(f'<circle cx="{lx}" cy="{yy}" r="5" fill="var({cls})"/><text x="{lx+12}" y="{yy+4}" class="leg">{name}</text>')

# gridlines + x ticks
for delta, label in [(-1e10,"&#8722;10&#185;&#8304;"), (-1e6,"&#8722;10&#8310;"), (-1e3,"&#8722;10&#179;"), (-1e2,"&#8722;10&#178;"), (0,"0"), (1e2,"+10&#178;"), (1e3,"+10&#179;"), (1e6,"+10&#8310;")]:
    x = tx(delta)
    if delta == 0:
        svg.append(f'<line x1="{x:.1f}" y1="{Y0}" x2="{x:.1f}" y2="{Y1}" stroke="var(--axis)" stroke-width="2"/>')
        svg.append(f'<text x="{x:.1f}" y="{Y0-8}" text-anchor="middle" class="axlab">BALANCE</text>')
    else:
        svg.append(f'<line x1="{x:.1f}" y1="{Y0}" x2="{x:.1f}" y2="{Y1}" stroke="var(--grid)" stroke-width="1"/>')
    svg.append(f'<text x="{x:.1f}" y="{Y1+18}" text-anchor="middle" class="tick">{label}</text>')
svg.append(f'<text x="{(X0+X1)/2}" y="{Y1+42}" text-anchor="middle" class="axlab">&#916; bits above balance &#8594; collisions forced (window populations live to the right)</text>')

# y ticks
for l2n, label in [(5,"n = 32"),(7,"n = 128"),(21,"n = 2&#178;&#185;"),(41,"n = 2&#8308;&#185;")]:
    y = ty(l2n)
    svg.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X1}" y2="{y:.1f}" stroke="var(--grid)" stroke-width="1"/>')
    svg.append(f'<text x="{X0-8}" y="{y+4:.1f}" text-anchor="end" class="tick">{label}</text>')
svg.append(f'<text x="30" y="{(Y0+Y1)/2}" transform="rotate(-90 30 {(Y0+Y1)/2})" text-anchor="middle" class="axlab">row size (log&#8322; n)</text>')

# --- OUR band: F2 sub-balance censuses ---
bx0, bx1 = tx(-14.5), tx(5.6)
by0, by1 = ty(7.6), ty(4.4)
svg.append(f'<rect x="{bx0:.1f}" y="{by0:.1f}" width="{bx1-bx0:.1f}" height="{by1-by0:.1f}" fill="var(--s2)" opacity="0.16" rx="4"/>')
bmid = (by0+by1)/2
svg.append(f'<text x="{bx0-8:.1f}" y="{bmid-4:.1f}" text-anchor="end" class="lab lab2">F2 sub-balance censuses (n = 32&#8211;128)</text>')
svg.append(f'<text x="{bx0-8:.1f}" y="{bmid+11:.1f}" text-anchor="end" class="lab">extras = 0 throughout</text>')

def dot(delta, l2n, cls, r=5.5, ring=False):
    x, y = tx(delta), ty(l2n)
    if ring:
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+2}" fill="var(--surface)"/>')
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="var({cls})"/>')
    return x, y

Y21 = ty(21)

# --- catch #11 pair: labels ABOVE their dots, arrow + its label BELOW the row ---
xq, yq = dot(-162, 21, "--s3")
svg.append(f'<text x="{xq:.1f}" y="{yq-32:.1f}" text-anchor="middle" class="lab lab3">KoalaBear row, q-scale reading</text>')
svg.append(f'<text x="{xq:.1f}" y="{yq-18:.1f}" text-anchor="middle" class="lab">window &#8220;admits&#8221; (&#8722;162 bits)</text>')

# --- upstream crossings (4 pairs cluster): labels BELOW the row ---
for d in (67.10, 52.11, 35.92, 20.93):
    dot(d, 21, "--s1", ring=True)
xc = tx(38)
svg.append(f'<text x="{xc:.1f}" y="{Y21+26:.1f}" text-anchor="middle" class="lab lab1">4 deployed adjacent pairs (a&#8320;&#8722;1 &#8594; a&#8320;)</text>')
svg.append(f'<text x="{xc:.1f}" y="{Y21+40:.1f}" text-anchor="middle" class="lab">&#916; = +21&#8230;+67 &#183; gates +24.0 / +57.9 &#183; margins exact</text>')

# upstream proved head-depth strata: labels ABOVE; catch-11 p-truth: below-left
xh, yh = dot(2.09e6, 21, "--s1")
svg.append(f'<text x="{xh-2:.1f}" y="{yh-32:.1f}" text-anchor="end" class="lab lab1">proved head-depth theorems (w &#8804; 21 / 10)</text>')
svg.append(f'<text x="{xh-2:.1f}" y="{yh-18:.1f}" text-anchor="end" class="lab">&#916; &#8776; +2.09M bits</text>')
xp, yp = dot(1740627, 21, "--s3", ring=True)

# dashed beta-jump arrow, well below the row labels
ya = Y21 + 62
svg.append(f'<defs><marker id="arr" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="var(--s3)"/></marker></defs>')
svg.append(f'<line x1="{xq:.1f}" y1="{ya:.1f}" x2="{xp:.1f}" y2="{ya:.1f}" stroke="var(--s3)" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>')
svg.append(f'<line x1="{xq:.1f}" y1="{yq+8:.1f}" x2="{xq:.1f}" y2="{ya:.1f}" stroke="var(--s3)" stroke-width="1" stroke-dasharray="2 4"/>')
svg.append(f'<line x1="{xp:.1f}" y1="{yp+8:.1f}" x2="{xp:.1f}" y2="{ya:.1f}" stroke="var(--s3)" stroke-width="1" stroke-dasharray="2 4"/>')
svg.append(f'<text x="{(xq+xp)/2:.1f}" y="{ya+18:.1f}" text-anchor="middle" class="lab lab3">the &#946;-jump (catch #11): the same row read at the true p-scale lands at +1.74M bits</text>')
svg.append(f'<text x="{(xq+xp)/2:.1f}" y="{ya+33:.1f}" text-anchor="middle" class="lab">t-null values never leave the base field &#8212; the window must be read at the generated field</text>')

# --- ours, small rows ---
x,y = dot(6.6, 5, "--s2")
svg.append(f'<text x="{x+10:.1f}" y="{y+4:.1f}" class="lab lab2">p=97 giant-block witnesses (+6.6)</text>')
x,y = dot(0.42, 5, "--s2", ring=True)
svg.append(f'<text x="{x-10:.1f}" y="{y+20:.1f}" text-anchor="end" class="lab lab2">p=21313 window relatives (+0.4)</text>')
x,y = dot(0.0, 6, "--s2", ring=True)
svg.append(f'<text x="{x+12:.1f}" y="{y-10:.1f}" class="lab lab2">F6 determination flips (q 241&#8211;337)</text>')
x,y = dot(-4.4e10, 41, "--s2")
svg.append(f'<text x="{x+12:.1f}" y="{y-6:.1f}" class="lab lab2">official prize-max F2 window (generating rows)</text>')
svg.append(f'<text x="{x+12:.1f}" y="{y+9:.1f}" class="lab">sub-balance by 2% of n = 4.4&#183;10&#185;&#8304; bits of slack</text>')

svg.append('</svg>')
out = "/home/u2470931/smooth-read-solomin/prize/notes/correspondence/regime_map.svg"
open(out, "w").write("\n".join(svg))
print("wrote", out)
