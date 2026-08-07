#!/usr/bin/env python3
"""C2'' F-round 3, part D -- F-d-D: THETA-FRAGILITY OF THE F-b SURVIVAL.

Unplanned follow-up: the theta spot-check registered in PREREG P4 ("I will
spot-check theta in {2,3,4} and report insensitivity or its failure")
returned a NON-insensitive reading, so it is scored here in full.

The pose declares the convention immaterial:
  "theta = 2 is a pose-time convention (results insensitive for theta in
   [2,4] at the 8 rows)"
  -- critical/nodes/dli_prime_weighted_large_block_support/notes/
     C2PP_POSED_20260710.md:93-95

F-b (the falsifier of record) scores `bulk_ratio`, which is defined
relative to theta.  This re-runs F-b's OWN kill rule at each theta in
{2, 2.5, 3, 4} over F-b's OWN search set, changing nothing else.

  F-b kill rule (c2r2_falsifiers.md:87-91):
      33*log2(x_max) + a > 21,   x_max = max bulk_ratio > 0

NEW named functional (CATCH-19C): `fb_score_at_theta` := 33*log2(x_max(theta))
  + a(theta), in bits, with x_max taken over F-b's search set exactly as
  c2r2_local.py:93 takes it (`if b > 0`).

Run: tools/ramguard local -- python3 \
       notes/pilots_20260807/c2pp_diag/fdd_theta_fragility.py
"""
import sys, math, json, importlib.util
from fractions import Fraction

sys.dont_write_bytecode = True
ROOT = "/home/u2470931/smooth-read-solomin/prize"
M1PATH = (ROOT + "/critical/nodes/dli_prime_weighted_large_block_support"
                 "/notes/m1_dli_m1_tower_census_modal.py")
M1JSON = (ROOT + "/critical/nodes/dli_prime_weighted_large_block_support"
                 "/notes/m1_dli_m1_results.json")
OUT = ROOT + "/notes/pilots_20260807/c2pp_diag/fdd_results.json"
spec = importlib.util.spec_from_file_location("m1", M1PATH)
m1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m1)

CAL_ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801),
            (3, 97), (3, 193), (4, 97), (4, 193)]
N, JUNC, RES = 32, 33, 21
ALLOW = 2.0 ** (21.0 / 33.0)
THETAS = [2.0, 2.5, 3.0, 4.0]

# censuses are theta-independent; compute once
base = {}
for (t, q) in CAL_ROWS:
    base[(t, q)] = (m1.even_null_census(q, N, t),
                    m1.mitm_joint_census_dict(q, N, t),
                    m1.signed_all_census(q, N, t))

print("=" * 78)
print("[F-d-D] THETA-FRAGILITY -- F-b's own kill rule, re-run at each theta")
print("=" * 78)
print(f"  pose: 'results insensitive for theta in [2,4] at the 8 rows'")
print(f"  F-b kill line: 33*log2(x_max) + a > 21 bits    "
      f"(allowance/junction {ALLOW:.6f})")

# the n=64 rows F-b also searched are banked at theta=2 only; note and use
m1res = json.load(open(M1JSON))
n64 = []
for r in m1res["rows"]:
    b = r["bulk_ratio"]
    if isinstance(b, (int, float)) and b == b and b > 0:
        n64.append((b, "n64", r["t"], r["q"]))
n64_max = max(n64)[0] if n64 else 0.0
print(f"  (n=64 rows are banked at theta=2 only; their max bulk = "
      f"{n64_max:.6f} is carried unchanged across theta)")

table = {}
out = []
for th in THETAS:
    per = {}
    for (t, q) in CAL_ROWS:
        cn, cs, asum = base[(t, q)]
        d = m1.decompose_row(q, N, t, cn, cs, asum, theta=th)
        b = d["bulk_ratio"]
        b = 0.0 if (b != b) else b
        accmass = sum(a["mass"] for a in d["accidents"])
        s_all = sum(asum)
        per[(t, q)] = (b, len(d["accidents"]), accmass / s_all if s_all else 0.0)
    table[th] = per

    cands = [(b, "n32", t, q) for (t, q), (b, na, af) in per.items() if b > 0]
    cands += n64
    xmax, lab, bt, bq = max(cands)
    amax = max(math.log2(1.0 + af) for (_, _, af) in per.values())
    score = JUNC * math.log2(xmax) + amax
    fires = score > RES
    exact = Fraction(xmax).limit_denominator(10 ** 12) ** JUNC > Fraction(2) ** RES
    out.append(dict(theta=th, x_max=xmax, x_max_at=[lab, bt, bq],
                    accident_bits=amax, fb_score_at_theta=score,
                    usage_pct=score / RES * 100, fires=fires,
                    exact_bulk_stack_exceeds=exact))
    print(f"\n  theta = {th}")
    print(f"    per-row bulk_ratio: " + "  ".join(
        f"({t},{q})={per[(t,q)][0]:.4f}" for (t, q) in CAL_ROWS))
    print(f"    n_accidents:        " + "  ".join(
        f"({t},{q})={per[(t,q)][1]}" for (t, q) in CAL_ROWS))
    print(f"    x_max = {xmax:.6f} at {lab}(t={bt},q={bq}) ; a = {amax:.5f} bits")
    print(f"    F-b score = 33*log2(x_max) + a = {score:.4f} bits"
          f"  = {score/RES*100:.2f}% of the 21-bit reserve")
    print(f"    exact Fraction: x_max^33 {'>' if exact else '<='} 2^21")
    print(f"    ==> F-b at theta={th}: "
          f"{'*** FIRES ***' if fires else 'does not fire'}")

print("\n" + "=" * 78)
print("  INSENSITIVITY CLAIM, SCORED")
print("=" * 78)
scores = [o["fb_score_at_theta"] for o in out]
print(f"    F-b score across theta in [2,4]: "
      f"{[round(s,3) for s in scores]} bits")
print(f"    spread = {max(scores)-min(scores):.3f} bits"
      f"  ({min(scores)/RES*100:.2f}% -> {max(scores)/RES*100:.2f}% of reserve)")
firing = [o["theta"] for o in out if o["fires"]]
print(f"    thetas in the pose's declared-immaterial range where F-b FIRES:"
      f" {firing}")
print(f"    ==> pose insensitivity claim: "
      f"{'REFUTED' if firing or max(scores)-min(scores) > 1.0 else 'holds'}")

# where does the swing come from?
print("\n  source of the swing (rows whose bulk_ratio moves with theta):")
for (t, q) in CAL_ROWS:
    vals = [table[th][(t, q)][0] for th in THETAS]
    if max(vals) - min(vals) > 1e-6:
        print(f"    (t={t},q={q:>5}): " + " -> ".join(
            f"theta={th}:{table[th][(t,q)][0]:.4f}"
            f"(nacc={table[th][(t,q)][1]})" for th in THETAS))

json.dump(dict(thetas=THETAS, allowance=ALLOW, results=out,
               per_row={str(k): {str(th): table[th][k] for th in THETAS}
                        for k in CAL_ROWS}), open(OUT, "w"), indent=1)
print(f"\n  artifact -> {OUT}")
