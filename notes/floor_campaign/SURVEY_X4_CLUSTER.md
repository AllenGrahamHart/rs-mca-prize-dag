# Floor-campaign survey: u2c_giant_tnull_dichotomy, u1_x4_direct_column_budget
# (Explore agent, 2026-07-07; verbatim quotes; both edges kind=req into x4)

## u2c_giant_tnull_dichotomy
STATEMENT (dag, re-posed 2026-07-06 after falsification): unscoped dichotomy FALSE (verified witness q=97,
n=32, t=2: T = {zeta^i: i in (0,1,2,8,12,30)} is 2-null non-coset; complement 81% GIANT; 160 accidents at
size 6; accidents = random-model objects of the ABOVE-BALANCE window C(n,b) > q^t). REPAIRED CLAIM: at rows
with q^t >= 2^n (sub-balance; ALL official prize-max rows qualify by ~2%): every t-null block is a union of
mu_M-cosets (M >= t) with zero-sum value patterns at multiples of M <= t. PROVED ASSETS: complementation
lemma (S t-null iff C\S t-null; verified 27762/27762), top-band rigidity (|S| >= n-t forces full coset),
(t+1)-support rigidity. Census: t=3 and large-q/n rows CLEAN. Remaining obligation: entropic suppression —
zero accidents in sub-balance (anti-concentration, same shape as the dli RES count).
CONSUMPTION (x4 REDUCTION_PACKET): "AUDIT BEFORE COMPRESSION surfaced two prose lemmas, now declared as the
wired hypothesis u2c_giant_tnull_dichotomy (U2-C prime; subsumes the divisor-frame residual)." The concrete
budget it feeds (b2_modp_giant_extras): "At official prize-max rows: the count of non-coset-union t-null
blocks (and their trade families) is <= n^3 = 2^123." Prize-max: "t*log2(q) ~ 2.15e12 > n ~ 1.1e12, so
q^t > 2^n: the window is EMPTY AT EVERY b."
MACHINERY: FALSIFICATION_AND_REPOSE.md (only node file); experiments/u2c_tnull_boundary_scan.py + results
(7 cells PASS; boundary transition 192 -> 64 -> 0 extras as p grows past the window at N=64, t=3, b=8;
primitive_boundary_coset_blocks: 0 everywhere).
QUANTIFIERS: re-posed scope = sub-balance rows only (regime hypothesis NECESSARY — witness shows it);
consumer needs only the extras COUNT <= n^3, not zero.

## u1_x4_direct_column_budget
STATEMENT (dag; node folder does not exist): "At the official X4/list corridor rows, after quotient,
dihedral, moment-trade, U2 boundary, and DLI/skew strips have removed their paid columns, the remaining
primitive exact-list active-core residue fits inside the direct row column consumed by
x4_exactlist_staircase_split. A sufficient concrete target is <= n^3 at the official rows. This is strictly
weaker than u1_pullback_dichotomy." FALSIFIER: "a complete or certified row/slice with more than n^3 fully
stripped non-toral primitive active-core trades, or row arithmetic showing the direct n^3 primitive column
no longer fits after quotient/dihedral/moment columns." NOTES: AMBER WEAKENING 2026-07-06 (x4 rewired to
this narrower premise; u1_pullback drops off critical orbit, retained ev/route).
CONSUMPTION: x4 statement.md STALE (still prints n^2 primitive target + names u1_pullback_dichotomy in
conditional.md/REDUCTION_PACKET.md prose); the DAG edge + EMPIRICAL_OBSERVATIONS record the actual
consumption: "consumer sufficiency PROVED exactly at 16n^3. Red sharpened to the 16n^3-compatible
obligation"; "NEW RED u1_x4_direct_column_budget replaces u1_pullback_dichotomy as x4's premise (strictly
weaker: <= n^3 direct-column residue after all strips)".
MACHINERY: experiments/u1_x4_active_core_budget_probe.py + results.json: status PASS,
direct_n3_alarms: [], max_nontoral_to_n3_ratio: 0.0146, positive control detected (60 anchored nontoral
trades vs budget 4096 at the exceptional control row).
QUANTIFIERS: official corridor rows only; post-strip residue; per-row existential falsifier.
