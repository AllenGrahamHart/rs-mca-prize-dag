#!/usr/bin/env python3
"""C2'' CALIBRATION (amber audit): three-part decomposition of the F2b junction
ratios at the 8 exact rows — coset class (k=0) routed exactly; accident classes
(class-ratio > theta, orbit-quantized spikes) counted separately at exact mass;
BULK = everything else. C2''-clause-(ii) concerns the bulk ratio only.
theta = 2 (any class-conditional mean > 2x its unconditional mean = accident)."""
import importlib.util, math
from collections import Counter, defaultdict
from pathlib import Path

VT = Path('/home/u2470931/smooth-read-solomin/prize/archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/verify_level2_tower.py')
spec = importlib.util.spec_from_file_location("vt", VT)
vt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vt)

ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801), (3, 97), (3, 193), (4, 97), (4, 193)]
THETA = 2.0

print(f"{'row':>12} | bulk-ratio | accident classes (k: ratio, exact cond mass, orbits-of-32)")
gm_logs = []
for t, q in ROWS:
    n = 32
    e, o = t // 2, (t + 1) // 2
    zeta = vt.get_zeta(q, n)
    sc = vt.skewcount_table(zeta, q, n, o)
    h = n // 2
    L = vt.build_half_configs(range(0, h // 2), zeta, q, n, e)
    R = vt.build_half_configs(range(h // 2, h), zeta, q, n, e)
    dL = defaultdict(list)
    for ev, gm, dm in L:
        dL[ev].append(gm)
    cn = Counter(); cs = Counter()
    for ev, gmR, dmR in R:
        key = tuple((-x) % q for x in ev)
        for gmL in dL.get(key, ()):
            G = gmL | gmR; k = bin(G).count("1")
            cn[k] += 1; cs[k] += sc.get(G, 0)
    fL = Counter(g for _, g, _ in L); fR = Counter(g for _, g, _ in R)
    an = Counter(); asum = Counter()
    for gmL, cL in fL.items():
        for gmR, cR in fR.items():
            G = gmL | gmR; k = bin(G).count("1"); w = cL * cR
            an[k] += w; asum[k] += w * sc.get(G, 0)
    # classify classes
    accid = []
    for k in sorted(set(cn) | set(an)):
        if k == 0: continue
        Ec = cs[k] / cn[k] if cn[k] else 0.0
        Eu = asum[k] / an[k] if an[k] else 0.0
        if Eu > 0 and Ec / Eu > THETA and cs[k] > 0:
            accid.append((k, Ec / Eu, cs[k]))
        elif Eu == 0 and cs[k] > 0:
            accid.append((k, float('inf'), cs[k]))
    acc_ks = {k for k, _, _ in accid}
    # bulk = k>=1, not accident
    bn = sum(cn[k] for k in cn if k >= 1 and k not in acc_ks)
    bs = sum(cs[k] for k in cn if k >= 1 and k not in acc_ks)
    un = sum(an[k] for k in an if k >= 1 and k not in acc_ks)
    us = sum(asum[k] for k in an if k >= 1 and k not in acc_ks)
    Ecb = bs / bn if bn else float('nan')
    Eub = us / un if un else float('nan')
    ratio = Ecb / Eub if (Eub and Eub > 0) else (0.0 if Ecb == 0 else float('nan'))
    tag = ", ".join(f"k={k}: {r if r!=float('inf') else 'inf'}x mass={m} ({m//(2*h)} orb32)"
                    for k, r, m in accid) or "-"
    print(f"t={t} q={q:>6} |   {ratio:6.3f}   | {tag}")
    if ratio > 0:
        gm_logs.append(math.log(ratio))
gm = math.exp(sum(gm_logs) / len(gm_logs)) if gm_logs else float('nan')
print(f"\nBULK-ONLY geometric mean (positive rows): {gm:.3f}")
print(f"allowances/junction: 2^(22/34)={2**(22/34):.3f} (pre catch-30), "
      f"2^(21/34)={2**(21/34):.3f} (corrected)")
