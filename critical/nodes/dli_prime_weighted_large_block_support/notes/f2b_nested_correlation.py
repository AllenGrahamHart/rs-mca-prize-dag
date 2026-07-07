#!/usr/bin/env python3
"""F2b: the C2 verdict measurement — cross-level conditional correlation in
the packet's OWN nested tower, at the eight exact b2b TEST-1 rows.

C2 (nested form) needs E[prod rho] <= 2^22 * prod E[rho] over the schedule.
The per-junction object is the correlation ratio

    R(t, q) = E[ skewcount(G(m1)) | m1 even-null ]
            / E[ skewcount(G(m1)) | m1 unrestricted ],

i.e. does conditioning on level-1 nullity bias the level-2 count?  The
nested factorization is exact iff R = 1; the 22-bit budget over ~34
junctions allows geometric mean R <= 2^0.65 ~ 1.57.

Machinery: the archived verify_level2_tower.py (which reproduced the exact
censuses, TEST 1). Conditional side = its tower_enumerate. Unconditional
side = mask-frequency convolution of the two independent half-config
tables against the same skewcount table.  Small exact runs (t = 2, 3, 4 at
n = 32) — the same rows the archive note published from this machine.
"""
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/home/u2470931/smooth-read-solomin/prize')
VT = ROOT / 'archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/verify_level2_tower.py'
spec = importlib.util.spec_from_file_location("vt", VT)
vt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vt)

ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801), (3, 97), (3, 193), (4, 97), (4, 193)]

results = []
for t, q in ROWS:
    n = 32
    e, o = t // 2, (t + 1) // 2
    zeta = vt.get_zeta(q, n)
    sc = vt.skewcount_table(zeta, q, n, o)
    h = n // 2
    L = vt.build_half_configs(range(0, h // 2), zeta, q, n, e)
    R = vt.build_half_configs(range(h // 2, h), zeta, q, n, e)

    # conditional (even-null m1) side
    dL = defaultdict(list)
    for ev, gm, dm in L:
        dL[ev].append(gm)
    n_null, s_null = 0, 0
    for ev, gmR, dmR in R:
        key = tuple((-x) % q for x in ev)
        for gmL in dL.get(key, ()):
            n_null += 1
            s_null += sc.get(gmL | gmR, 0)

    # unconditional side: independent halves, mask-frequency convolution
    fL = Counter(gm for _, gm, _ in L)
    fR = Counter(gm for _, gm, _ in R)
    n_all, s_all = 0, 0
    for gmL, cL in fL.items():
        for gmR, cR in fR.items():
            n_all += cL * cR
            s_all += cL * cR * sc.get(gmL | gmR, 0)

    Ec = s_null / n_null if n_null else float('nan')
    Eu = s_all / n_all
    ratio = Ec / Eu if Eu > 0 else float('inf')
    results.append({"t": t, "q": q, "null_states": n_null,
                    "E_cond": Ec, "E_uncond": Eu,
                    "ratio": ratio})
    print(f"t={t} q={q}: null states={n_null}  E[sc|null]={Ec:.6f}  "
          f"E[sc|all]={Eu:.6f}  RATIO={ratio:.3f}")

import math
finite = [r["ratio"] for r in results if r["ratio"] not in (float('inf'),) and r["ratio"] > 0]
if finite:
    gm = math.exp(sum(math.log(x) for x in finite) / len(finite))
    print(f"\ngeometric-mean ratio over {len(finite)} rows: {gm:.3f} "
          f"(budget allows <= 1.57/junction)")
Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=1))
