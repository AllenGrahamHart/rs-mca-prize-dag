#!/usr/bin/env python3
"""C2'' F-round 3, part B -- F-d-B: the ACCIDENT-MULTIPLICITY convention.

Pre-registration: notes/pilots_20260807/c2pp_diag/PREREG.md (H1; functional
names extended here and named at first use per CATCH-19C).

F-b's transport (c2r2_falsifiers.md:78-85) stacks the clause-(ii) BULK ratio
33 times but charges clause-(iii) ACCIDENT mass ONCE, q-independently:
    kill iff  33*log2(x_max) + a > 21,  a = log2(1 + sum mass_k / total).
"Counted once" is sound only if the whole 33-junction tower owns O(1)
accidents.  The pose's own words are "unique FIRST ownership"
(statement.md:15-16) -- which says each accident has ONE owner, not that the
tower has ONE accident.  This measures the gap.

NEW named functionals (CATCH-19C, first use here):
  A1 `accident_charge_once` a1   := log2(1 + sum_acc mass / s_all)  [F-b's]
  A2 `accident_charge_owned` a33 := 33 * a1  [one fresh accident per junction]
  A3 `accident_column_factor` f  := stripped_mean_ratio / bulk_ratio
  A4 `accident_column_bits`      := 33 * log2(f)  [f transported like bulk]
  A5 `window_lam_total`          := sum over populated accident classes of
     the proved q-independent window law lam_window(h,k,q,o)

Reads only the artifact written by fd_coset_routing_attack.py.  Stdlib only.
Run: tools/ramguard tiny -- python3 \
       notes/pilots_20260807/c2pp_diag/fdb_accident_multiplicity.py
"""
import sys, math, json

sys.dont_write_bytecode = True
ROOT = "/home/u2470931/smooth-read-solomin/prize"
IN = ROOT + "/notes/pilots_20260807/c2pp_diag/fd_results.json"
OUT = ROOT + "/notes/pilots_20260807/c2pp_diag/fdb_results.json"
JUNC, RES = 33, 21
ALLOW = 2.0 ** (21.0 / 33.0)

res = json.load(open(IN))
rows = res["rows"]
assert len(rows) == 8, "nonemptiness: expected the 8 banked calibration rows"

print("=" * 78)
print("[F-d-B] ACCIDENT MULTIPLICITY -- 'counted once' vs 'one owner each'")
print("=" * 78)
print(f"  {'row':>14} {'a1(once)':>9} {'a33(owned)':>11} {'accfac':>8}"
      f" {'33*log2':>9} {'lam_tot':>9} {'nacc':>5}")
out = []
for r in rows:
    accs = r["accidents"] or []
    s_all = float(r["s_all"])
    massum = sum(float(a["mass"]) for a in accs)
    a1 = math.log2(1.0 + massum / s_all) if s_all > 0 else 0.0
    a33 = JUNC * a1
    sm, bk = r["stripped_mean_ratio"], r["bulk_ratio"]
    sm = None if sm in (None, "None") else float(sm)
    bk = None if bk in (None, "None") else float(bk)
    if sm and bk and bk > 0:
        f = sm / bk
        fb = JUNC * math.log2(f)
    else:
        f, fb = None, None
    lam_tot = sum(float(a["lam"]) for a in accs)
    out.append(dict(t=r["t"], q=r["q"], n_accidents=len(accs),
                    accident_charge_once=a1, accident_charge_owned=a33,
                    accident_column_factor=f, accident_column_bits=fb,
                    window_lam_total=lam_tot, accident_mass=massum,
                    s_all=s_all))
    print(f"  (t={r['t']},q={r['q']:>5}) {a1:9.5f} {a33:11.4f}"
          f" {('     n/a' if f is None else f'{f:8.4f}')}"
          f" {('      n/a' if fb is None else f'{fb:9.3f}')}"
          f" {lam_tot:9.5f} {len(accs):5d}")

a1max = max(o["accident_charge_once"] for o in out)
a33max = max(o["accident_charge_owned"] for o in out)
fbmax = max([o["accident_column_bits"] for o in out
             if o["accident_column_bits"] is not None] or [0.0])
print(f"\n  worst a1 (F-b's scored accident term)      = {a1max:.5f} bits"
      f"  -> {a1max/RES*100:.3f}% of the 21-bit reserve")
print(f"  worst a33 (one fresh accident per junction) = {a33max:.4f} bits"
      f"  -> {a33max/RES*100:.3f}% of the reserve"
      f"  {'OVERFLOWS' if a33max > RES else 'inside'}")
print(f"  worst accident-column factor transported 33x = {fbmax:.3f} bits"
      f"  -> {fbmax/RES*100:.1f}% of the reserve"
      f"  {'OVERFLOWS' if fbmax > RES else 'inside'}")

# expected accidents across a 33-junction tower under the proved window law
lam_rows = [o for o in out if o["window_lam_total"] > 0]
print(f"\n  window-law expectation over a 33-junction tower "
      f"(clause (iii)'s own frequency model):")
for o in lam_rows:
    print(f"    (t={o['t']},q={o['q']:>5})  lam_per_junction={o['window_lam_total']:.5f}"
          f"  E[#accidents over 33 junctions]={33*o['window_lam_total']:.4f}")
if not lam_rows:
    print("    (no populated accident class carries a positive window lam)")

multi = [o for o in out if 33 * o["window_lam_total"] > 1.0]
print(f"\n  rows where the tower expects MORE THAN ONE accident: "
      f"{[(o['t'], o['q']) for o in multi]}")
print(f"  ==> 'counted once' is {'NOT' if multi else ''} conservative "
      f"at {len(multi)}/{len(out)} banked rows")

json.dump(dict(worst_a1=a1max, worst_a33=a33max,
               worst_accident_column_bits=fbmax,
               rows_expecting_multiple_accidents=[(o['t'], o['q'])
                                                  for o in multi],
               allowance=ALLOW, rows=out), open(OUT, "w"), indent=1)
print(f"\n  artifact -> {OUT}")
