#!/usr/bin/env python3
"""C2'' F-round 2 -- FINAL VERDICT (exact-rational F-b path).

Combines: n=32 calibration (8 rows, recomputed via M1 kernels), M1's banked
n=64 rows (45), and the c2r2 NEW n=64 rows. Runs read_Fa over ALL depths,
read_Fc over the extended census, and scores F-b (packet arithmetic x^33 vs
2^21). Reuses M1's read_Fa/read_Fc/decompose_row verbatim (import, no .pyc).
"""
import sys, math, json, importlib.util
from fractions import Fraction
sys.dont_write_bytecode = True

M1 = "/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_tower_census_modal.py"
spec = importlib.util.spec_from_file_location("m1", M1)
m1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m1)
M1JSON = "/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_results.json"
NEW = "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/c2r2_new_rows.json"
RES, JUNC = 21, 33
CAL_ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801), (3, 97), (3, 193), (4, 97), (4, 193)]

# ---- assemble n=32 calibration rows (recompute, cheap) ----
cal = []
for (t, q) in CAL_ROWS:
    cs = m1.mitm_joint_census_dict(q, 32, t)
    cn = m1.even_null_census(q, 32, t); asum = m1.signed_all_census(q, 32, t)
    cal.append(m1.decompose_row(q, 32, t, cn, cs, asum))
m1res = json.load(open(M1JSON))["rows"]
new = json.load(open(NEW))["rows"]

def flt(x):
    try:
        x = float(x)
        return x if x == x else 0.0
    except Exception:
        return 0.0
for r in m1res + new:
    for kk in ("bulk_ratio", "stripped_mean_ratio", "stripped_mass_ratio", "ratio"):
        r[kk] = flt(r[kk])

# positive-control: new t=3 q=193 must match M1 banked exactly
bank = {(r["t"], r["q"]): r for r in m1res}
for r in new:
    if (r["t"], r["q"]) in bank:
        b = bank[(r["t"], r["q"])]
        ok = abs(r["ratio"] - b["ratio"]) < 1e-9 and abs(r["bulk_ratio"] - b["bulk_ratio"]) < 1e-9
        print(f"[PC-modal] new (t={r['t']},q={r['q']}) reproduces M1 banked "
              f"ratio/bulk: {'OK' if ok else 'MISMATCH!'} "
              f"(ratio {r['ratio']:.6f} vs {b['ratio']:.6f})")
        assert ok, "t=3 modal positive control mismatch"

# ---- dedupe n=64 rows (M1 + new), prefer new only if not in M1 ----
n64 = {(r["t"], r["q"]): r for r in m1res}
new_added = []
for r in new:
    if (r["t"], r["q"]) not in n64:
        n64[(r["t"], r["q"])] = r; new_added.append((r["t"], r["q"]))
n64rows = list(n64.values())
print(f"\nn=64 rows: {len(m1res)} banked (M1) + {len(new_added)} new = {len(n64rows)} "
      f"unique; new = {sorted(new_added)}")

# ================= F-a over all depths (M1 read_Fa verbatim) =================
by_depth = {}
for r in n64rows:
    by_depth.setdefault(r["t"], []).append(r)
fa_fired, fa_log = m1.read_Fa(by_depth)
print(fa_log)

# ================= F-c extended census (M1 read_Fc verbatim) =================
CEN_QS = set(m1.FC_CENSUS) | {11777, 17729}
census_rows = [r for r in n64rows if r["t"] == 2 and r["q"] in CEN_QS]
fc_fired, fc_log = m1.read_Fc(census_rows)
print(fc_log)
# theta spot-check (insensitivity): re-decompose census cells at theta in {2,3,4}
print("\n[theta spot-check] k=3 accident count on the census at theta in {2,3,4}:")
for th in (2.0, 3.0, 4.0):
    xx = 0
    for r in sorted(census_rows, key=lambda x: x["q"]):
        tbl = r["table"]
        v = tbl.get("3", tbl.get(3))
        if v:
            cn3, cs3, an3, asum3 = v
            Ec = cs3 / cn3 if cn3 else 0.0; Eu = asum3 / an3 if an3 else 0.0
            if Eu > 0 and cs3 > 0 and Ec / Eu > th:
                xx += 1
    print(f"   theta={th}: {xx} accident cells (of {len(census_rows)})")

# ================= F-b scoring (exact) =================
print("\n" + "=" * 72 + "\nF-b READ -- packet transport x^33 vs 2^21 (exact Fraction)\n" + "=" * 72)
def F(x):
    return Fraction(x).limit_denominator(10 ** 12)
allrows = [("n32", r) for r in cal] + [("n64", r) for r in n64rows]
bulk_pos = [(r["bulk_ratio"], lab, r["t"], r["q"]) for lab, r in allrows if r["bulk_ratio"] > 0]
bmax, blab, bt, bq = max(bulk_pos)
bulk_bits = JUNC * math.log2(bmax)
fired_bulk = F(bmax) ** JUNC > F(2) ** RES
# accident absolute charge (clause iii, counted once)
def accmass_frac(r):
    am = sum(a["mass"] for a in r["accidents"]) if r["accidents"] else 0
    tbl = r["table"] if isinstance(r["table"], dict) else {}
    asum_all = sum(v[3] for v in tbl.values()) if tbl else 0
    return (am, am / asum_all if asum_all else 0.0)
acc = [(math.log2(1 + accmass_frac(r)[1]) if accmass_frac(r)[1] > 0 else 0.0, lab, r["t"], r["q"], accmass_frac(r))
       for lab, r in allrows]
amax_bits, alab, at, aq, (amass, afrac) = max(acc)
total_bits = bulk_bits + amax_bits
fb_fired = (total_bits > RES)
print(f"  worst BULK ratio (clause ii): {bmax:.6f} at {blab} (t={bt},q={bq})")
print(f"    bulk^33 = 2^{bulk_bits:.4f}  -> exact bulk^33 {'>' if fired_bulk else '<='} 2^21")
print(f"  worst ABSOLUTE accident charge (clause iii, once): 2^{amax_bits:.4f} "
      f"at {alab}(t={at},q={aq}) mass={amass} frac={afrac:.2e}")
print(f"  TOTAL replayable-tower charge = 2^{total_bits:.4f}  -> RESERVE USAGE "
      f"= {total_bits/RES*100:.3f}% of 21 bits")
print(f"  F-b: {'*** FIRED ***' if fb_fired else 'NOT fired (reserve intact)'}")
strip_pos = [(r["stripped_mean_ratio"], lab, r["t"], r["q"]) for lab, r in allrows if r["stripped_mean_ratio"] > 0]
smax, slab, st, sq = max(strip_pos)
print(f"  [NOT-falsifier] stripped-stacked {smax:.4f}^33 = 2^{JUNC*math.log2(smax):.2f} "
      f"at {slab}(t={st},q={sq}) -- per-junction-uniform proxy, NOT scored")

# ================= verdict summary =================
print("\n" + "=" * 72)
print("C2R2 SUMMARY:")
print(f"  F-a fired: {fa_fired}   (depths tested: {sorted(by_depth)}; "
      f"t=2 octaves {sorted(set(int(math.log2(r['q'])) for r in by_depth.get(2,[])))}, "
      f"t=3 octaves {sorted(set(int(math.log2(r['q'])) for r in by_depth.get(3,[])))})")
print(f"  F-b fired: {fb_fired}   (worst bulk {bmax:.4f}, reserve usage {total_bits/RES*100:.2f}%)")
print(f"  F-c fired: {fc_fired}   (census rows: {len(census_rows)})")
print("=" * 72)
out = {"Fa": fa_fired, "Fb": fb_fired, "Fc": fc_fired,
       "worst_bulk": [bmax, blab, bt, bq], "reserve_usage_pct": total_bits / RES * 100,
       "census_rows": len(census_rows), "new_rows": sorted(new_added),
       "worst_stripped": [smax, slab, st, sq]}
json.dump(out, open("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/c2r2_verdict.json", "w"), indent=1)
print("verdict json written.")
