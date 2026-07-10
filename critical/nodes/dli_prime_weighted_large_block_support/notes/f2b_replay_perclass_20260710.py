#!/usr/bin/env python3
"""AMBER-AUDIT replay (read-only, scratchpad): the F2b nested-tower measurement
that killed C2-as-frozen, replayed independently from the archived machinery,
PLUS the per-profile-class decomposition (the record cited but not banked as a
table) that motivates the C2'' three-part shape:
  coset class (k=0) routed exactly | noncoset bulk at mean-field | counted accidents.

Outputs, per row (t, q):
  - E[sc | level-1 even-null], E[sc | unrestricted], ratio  (must match banked json)
  - per-class (k = #singletons) conditional/unconditional means + ratios
  - the COSET-STRIPPED ratio (k >= 1 only)  == the C2'' calibration object
"""
import importlib.util, json, math
from collections import Counter, defaultdict
from pathlib import Path

VT = Path('/home/u2470931/smooth-read-solomin/prize/archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/verify_level2_tower.py')
spec = importlib.util.spec_from_file_location("vt", VT)
vt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vt)

BANKED = json.loads(Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/f2b_nested_correlation.json').read_text())
banked = {(r["t"], r["q"]): r for r in BANKED}

ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801), (3, 97), (3, 193), (4, 97), (4, 193)]

def popcount(x): return bin(x).count("1")

results = []
for t, q in ROWS:
    n = 32
    e, o = t // 2, (t + 1) // 2
    zeta = vt.get_zeta(q, n)
    sc = vt.skewcount_table(zeta, q, n, o)
    h = n // 2
    L = vt.build_half_configs(range(0, h // 2), zeta, q, n, e)
    R = vt.build_half_configs(range(h // 2, h), zeta, q, n, e)

    # conditional (even-null m1)
    dL = defaultdict(list)
    for ev, gm, dm in L:
        dL[ev].append(gm)
    n_null = s_null = 0
    cls_n_null = Counter(); cls_s_null = Counter()
    for ev, gmR, dmR in R:
        key = tuple((-x) % q for x in ev)
        for gmL in dL.get(key, ()):
            G = gmL | gmR; k = popcount(G); s = sc.get(G, 0)
            n_null += 1; s_null += s
            cls_n_null[k] += 1; cls_s_null[k] += s

    # unconditional
    fL = Counter(gm for _, gm, _ in L)
    fR = Counter(gm for _, gm, _ in R)
    n_all = s_all = 0
    cls_n_all = Counter(); cls_s_all = Counter()
    for gmL, cL in fL.items():
        for gmR, cR in fR.items():
            G = gmL | gmR; k = popcount(G); w = cL * cR
            s = sc.get(G, 0)
            n_all += w; s_all += w * s
            cls_n_all[k] += w; cls_s_all[k] += w * s

    Ec = s_null / n_null
    Eu = s_all / n_all
    ratio = Ec / Eu
    b = banked[(t, q)]
    ok = (abs(Ec - b["E_cond"]) < 1e-12 and abs(Eu - b["E_uncond"]) < 1e-12
          and n_null == b["null_states"])
    print(f"t={t} q={q}: E[sc|null]={Ec:.6f} E[sc|all]={Eu:.6f} RATIO={ratio:.3f} "
          f"nulls={n_null}  REPLAY {'PASS' if ok else 'FAIL'} (banked "
          f"{b['E_cond']:.6f}/{b['E_uncond']:.6f}/{b['ratio']:.3f})")

    # per-class table + coset-stripped (k>=1) ratio
    print("   k : n_null  E[sc|null,k]   n_all-frac  E[sc|all,k]   class-ratio")
    ks = sorted(set(cls_n_null) | set(cls_n_all))
    for k in ks:
        En_k = cls_s_null[k] / cls_n_null[k] if cls_n_null[k] else float('nan')
        Eu_k = cls_s_all[k] / cls_n_all[k] if cls_n_all[k] else float('nan')
        cr = (En_k / Eu_k) if (Eu_k and Eu_k > 0 and not math.isnan(En_k)) else float('nan')
        print(f"   {k:2d}: {cls_n_null[k]:7d}  {En_k:12.6f}  {cls_n_all[k]/n_all:10.6f}  "
              f"{Eu_k:12.6f}  {cr:8.3f}")
    # stripped: remove k=0 mass from numerator sums AND state counts on both sides
    sn1 = s_null - cls_s_null[0]; nn1 = n_null - cls_n_null[0]
    sa1 = s_all - cls_s_all[0]; na1 = n_all - cls_n_all[0]
    Ec1 = sn1 / nn1 if nn1 else float('nan')
    Eu1 = sa1 / na1 if na1 else float('nan')
    r1 = Ec1 / Eu1 if (Eu1 and Eu1 > 0) else float('nan')
    # also: coset-stripped SUM ratio with original state normalization
    # (charges the coset column to the packet, keeps the measure): ratio of
    # noncoset per-state mass under null vs unconditional.
    r2 = (sn1 / n_null) / (sa1 / n_all) if sa1 else float('nan')
    print(f"   COSET-STRIPPED (k>=1): cond-mean ratio = {r1:.3f} ; "
          f"noncoset-mass ratio (orig normalization) = {r2:.3f}")
    results.append({"t": t, "q": q, "ratio": ratio, "stripped_mean_ratio": r1,
                    "stripped_mass_ratio": r2, "replay_ok": ok})

fin = [r["ratio"] for r in results]
gm = math.exp(sum(math.log(x) for x in fin) / len(fin))
fin1 = [r["stripped_mean_ratio"] for r in results if r["stripped_mean_ratio"] > 0]
gm1 = math.exp(sum(math.log(x) for x in fin1) / len(fin1))
fin2 = [r["stripped_mass_ratio"] for r in results if r["stripped_mass_ratio"] > 0]
gm2 = math.exp(sum(math.log(x) for x in fin2) / len(fin2))
print(f"\nGEOMETRIC MEANS over {len(fin)} rows:")
print(f"  raw ratio            : {gm:.3f}   (banked 2.139; allowance/junction 2^(22/34) = {2**(22/34):.3f})")
print(f"  coset-stripped mean  : {gm1:.3f}")
print(f"  coset-stripped mass  : {gm2:.3f}")
print("replays:", "ALL PASS" if all(r["replay_ok"] for r in results) else "SOME FAIL")
Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=1))
