#!/usr/bin/env python3
"""Floor-budget slack scan (Codex retarget tactic applied to F4/F5/F7).

Question per floor: is the floor's printed constant BINDING at the
official rows, i.e. would a weaker target still serve the consumer?
(Precedent: the F3 official-row retarget H3-ACT(16) -> H3-ACT(4096)
bought a 256x weaker target because the internal compiler had slack.)

Exact arithmetic here; banked verifier outputs cited where the column
formulas live in the working-record emissions (poly-forcing 52/52,
QA.22 27/27, Pro floor-window 4). Any assertion failure refutes the
scan's reading of the banked numbers.
"""
from math import comb, log2

print("== F5 xr_smallcore 16n^3 vs s_lo (poly-forcing compiler, banked) ==")
# Banked: 16 n^3 <= s_lo at all six clean-rate candidates; prize rows
# tight at 29 n^3; prize-max allowance ~2^127.9.  Consistency check:
n_max = 2 ** 41
tight_c = 29
assert abs(log2(tight_c * n_max**3) - 127.9) < 0.1, log2(tight_c * n_max**3)
slack_bits = log2(29 / 16)
print(f"  prize-max row n=2^41: allowance = 29*n^3 = 2^{log2(29*n_max**3):.2f}")
print(f"  consumed budget 16*n^3 = 2^{log2(16*n_max**3):.2f}")
print(f"  max uniform constant retune: 16 -> 29  ({slack_bits:.2f} bits)")
print("  VERDICT: RETARGET-DEAD at the binding row (<1 bit of room);")
print("  lower candidates have s_lo ~ 2^122 vs much smaller n^3, but the")
print("  uniform-in-row form is pinned by prize-max.")

print("\n== F4 petal n^B vs the saturated binomial column (banked window-4) ==")
# Banked: the paid family saturates to C(n+6, 6) (c-sweep: C(core, 6)
# with core = n + c at excess c; adversarial sweep reached c = 14).
# Pro window-4 replay: C(n+6,6) <= n^6 at all four official maximal
# rows, exponent <= 5.785.  Recompute exactly, incl. the c=14 column.
for s in (41, 42, 43, 44):
    n = 2 ** s
    col6 = comb(n + 6, 6)
    col14 = comb(n + 20, 6)   # c=14 => core n+20, still degree 6
    e6 = log2(col6) / s
    e14 = log2(col14) / s
    assert col6 <= n ** 6 and col14 <= n ** 6
    print(f"  n=2^{s}: log_n C(n+6,6) = {e6:.4f}  (room to B=6: "
          f"{(6 - e6) * s:.1f} bits); c=14 column exponent {e14:.4f}")
print("  VERDICT: NOT binding — the saturated column sits ~9 bits under")
print("  n^6 at every official maximal row and the growth in the excess c")
print("  is degree-6 binomial (absorbed by any c-uniform n^6 budget).")
print("  B_max beyond 6 is gated by the codegree-conversion emission")
print("  (imgfib -> list_safe), not by the paid family: NAMED OPEN CELL.")

print("\n== F7 worst_word envelope room (QA.22 gate, banked) ==")
# Banked QA.22 (27/27 exact big integers): four-column split fits under
# B* at ALL SIX candidates; prize rows have 27.0/60.6+ bits of
# staircase-column room after the 16n^3 + B_tan reserve; the aggregate
# prize-row line is 0.9 bits under QA.22's CONSERVATIVE convention.
print("  within-column room at prize rows: 27.0 / 60.6+ bits (staircase")
print("  column); aggregate-vs-B* line: 0.9 bits (conservative convention).")
print("  VERDICT: NO free uniform slack for the challenger envelope —")
print("  spending the within-column room requires a re-attribution under")
print("  the QA.22 conventions note (decision, not arithmetic): FLAGGED.")

print("\nFLOOR_BUDGET_SLACK_SCAN_PASS")
