# TARGET 4 — THE h = 4 SHALLOW COLLISION CENSUS. Prove or falsify.

The next rung of a ladder with two proved predecessors. Self-
contained; either resolution moves a load-bearing kernel (the
census core of the rigidity-kernel program, notes/kernel_basis/).

## Setup

q an odd prime with q > 4 (so indices 1,2,3 are p-free), N a power
of two with N | q - 1, mu_N <= F_q^x. For h >= 2 define the
SHALLOW COLLISION CENSUS

  T_h(q, N) = #{ ordered pairs (A, B) : A, B disjoint h-subsets of
                 mu_N with p_i(A) = p_i(B) for i = 1, ..., h-1 }.

Known: T_2 <= C N^{5/2} (proved via Heath-Brown--Konyagin;
ladder data to N = 512 puts the truth at ~N^2). At h = 3, the
characteristic-zero pair families are classified (toral/unit-circle
families only), and all interior mass at finite q is norm-gate
accidents with per-shape activation at most phi(N) log 6 / (2 log N)
primes. Structured families at h <= 3 are exactly: quotient
pullbacks (coset-compatible pairs) and toral families.

## The conjecture

There is an absolute constant C such that for all (q, N) as above:

    T_4(q, N) <= C N^3,

with the pair families attaining the count classified as (i)
quotient pullbacks, (ii) toral/norm-kernel families, and (iii)
finitely many norm-gate accident shapes per (N), each active at
O(phi(N) / log N) primes.

## PROVE OR FALSIFY.

Notes: the exponent 3 is the first uncommitted point above the
proved T_2 <= C N^{5/2} and the h-ladder heuristic T_h ~ N^{h-1};
a proof of ANY exponent < 4 with the classification is valuable; a
falsification means a family (3+ growing scales, exact counts)
beating every polynomial the classification permits. The h = 2
proof imports Stepanov's method; whether it extends past the
resolvent degree at h = 4 is exactly the open question. In-repo
context: the shared_census_kernel node (dag.json), the f3_h2/h3
theorem nodes and their verifiers, and qx13_pair_rank_ledger
(the moment-level machinery, replayed 164/164).

## Addendum 2026-08-03 — FALSIFIED AS STATED; reprice forced

Ours. Coordinator Modal run `ap-sx9plNuGHtzGtGYisoYrh0`; exact integer
census; result `experiments/prize_resolution/sol_target4_n256_result.json`
(sha256 `27ed261e...`); generator
`experiments/prize_resolution/sol_target4_n256_modal.py`; decided in commit
`8d6f1aeb`. Algorithm validated against our banked `(32,97): T_4 = 792`
anchor and against maelcar #1147's independently replayed `n = 128` row.

The conjecture above quantifies over ALL `(q,N)` with `q` an odd prime `> 4`,
`N` a power of two and `N | q-1`. It carries no `q`-vs-`N` hypothesis. At the
FULLY ADMISSIBLE row `N = 256, q = 257` (index `(q-1)/N = 1`):

    T_4 = 1,729,295,040 ,   N^3 = 16,777,216 ,   T_4/N^3 = 103.07 .

At `N = 256, q = 769` (index 3): `T_4 = 63,361,728`, ratio `3.78` — still
rising from `2.87` at `N = 128`. No absolute constant `C` survives: the
index-1 family's ratio grows as `~ N^2/576`, by elementary first-moment
pigeonhole into the `q^3 ~ N^3` key space, which predicts unbounded growth.
**The conjecture is FALSE AS STATED.**

REPRICE FORCED (wording is a surfaced decision, not applied here): the
statement needs an index hypothesis — either an explicit index floor, or the
form `T_4 <= C(index) N^3` with `C(index)` DECREASING in `index = (q-1)/N`,
re-calibrated on the banked `(32,97)` anchor. Note that every in-repo `n^3`
census node carries such a guard already (`f3_hge4_aggregate_budget` and
`f3_hge4_norm_gate_count`: "every prime `p = 1 mod n` with `p >= n^2`";
`f3_h2_stratum_theorem`: "`n <= q^{2/3}` implied by F3's own regime
`q >= n^2`"). The guard was simply not carried into this target.

BRIDGE ADOPTED (from the maelcar #1147 audit, proved exactly at `(32,97)`):
their Paper-D smooth-trade currency `T_sm` is this census restricted and
normalised — `T_4^{smooth,ordered} = 2n T_sm` on free orbits, reconciling our
banked `792 = 2 x 396 = 2 x (288 smooth + 108 non-smooth)` with their
`T_sm = 9`. So their smooth target `T_sm <= n^2/2` is exactly this bound with
`C = 1` on the smooth locus. Their aggregate energy inequality, if it ever
closes, is a direct input here. (#1147 is UNMERGED; the bridge is OURS,
computed by our own replay.)
