# qme_statement — QA.22 M <= t EXTENSION (node qa22_m_le_t_extension)
# Proof packet 2026-07-13 (fresh-context proof worker). Repo read-only;
# packet: qme_statement.md / qme_proof.md / qme_verify.py / qme_claim_contract.md /
# qme_findings.md, all in the session scratchpad.

## Setting (all conventions banked; nothing new is defined here)

- **Official grid.** n = 2^s, s = 13..44; rates rho in {1/2, 1/4, 1/8, 1/16};
  k = rho*n; sigma = 1; t = (n-k)/2 (the petal count — the gate's scale
  bound, per the stabilizer partition c(S) <= t). 128 rows, 3392 own cells.
  This SUPERSETS every narrower "official grid" reading in the bsr packet
  (s = 13..20 exact + maximal rows; "29 rows x 4 rates"): in particular the
  four official maximal rows (n, k = 2^40) = grid rows (41, 1/2), (42, 1/4),
  (43, 1/8), (44, 1/16) are inside.
- **QA.22 column convention** (dyadic_profile_evaluation, PROVED):
  Q_M(A) = C(n/M - 1, floor(A/M)).
- **P1-OWN cell at scale M:** A_own(M) = M * ceil((k+1)/M), so
  h_M := floor(A_own/M) = A_own/M = ceil((k+1)/M) exactly (A_own is a
  multiple of M); k+1 <= A_own <= k+M, with A_own = k+M when M | k.
  At M = 2 (k even): A_own(2) = k+2.
- **Allowance constant:** 719 = floor(n^6 / C(n+6,6)) exactly at the four
  official maximal rows (and FYI at s = 40, 45 — not knife-edge; #154).
- **Extension rows added to the ledger:** { (M, A_own(M)) : M dyadic,
  2 <= M <= t }, each with allowance line 719 * Q_M(A_own(M)); PLUS, if the
  consumer charges the csp band, the cell (2, k+4) with allowance
  719 * Q_2(k+4). The banked M > t_res QA.22 rows (t_res = A_row - k, the
  row reserve) and the M > t composite's cells are NOT touched.

## THEOREM (the extension; every clause machine-verified by qme_verify.py)

For every official-grid row (s, rho):

**(i) Nondegeneracy (the ledger rows exist).** Every extension row has
Q_M(A_own) >= 1: A_own(M) <= k + M <= n - M, equivalently
h_M <= n/M - 1, for every dyadic 2 <= M <= t. (COL's load-bearing
direction, #151; the boundary is exact at (rho, M) = (1/2, t):
h = 3 = n/M - 1, Q = 1.) The csp cell is likewise nondegenerate:
k/2 + 2 <= n/2 - 1.

**(ii) The COL-priced mass fits every row's allowance.** At every extension
row, n/(n - A_own(M)) <= 2/(1 - rho) <= 4, hence by Lemma COL (PROVED,
word-free) the realized class mass at the cell is
<= [n/(n-A_own)] * Q_M(A_own) <= 4 * Q_M(A_own) <= 719 * Q_M(A_own):
the allowance line absorbs the landing with headroom exactly 719/4 = 179.75
before any full-petal/band filtering. Per-rate exact maxima of the cap
ratio over the grid: {1/2: 4, 1/4: 2, 1/8: 4/3, 1/16: 4/3} (equality
attained; the 4 only at rho = 1/2, M = t). The csp cell's ratio
n/(n-k-4) <= 4 in scope.

**(iii) Dedup unchanged.** (a) Extension cells vs the M > t 7-lemma
composite: scale ranges [2, t] and (t, n] are disjoint; under the
stabilizer partition each realized class is charged exactly once at its
exact-scale cell (c(S), |S|) — a partition, no geometric-ledger dedup
device needed (#102 dissolution unchanged). (b) Extension cells vs the
banked QA.22 M > t_res rows: even where the M-ranges overlap (they do:
e.g. prize 1/4 banked rows start at M* = 2^34 < t), the (M, A) cells are
disjoint by PARITY — every A_own is even (a multiple of even M), every
banked QA.22 row A is odd (all seven banked rows: 507, 261, 133, 67,
558345748481, 283467841537, 141733920769). The banked rows' values are
untouched: dyadic_profile_evaluation/verify.py replayed ALL PASS
(2026-07-13, this session).

**(iv) First-scale dominance, extended (corrected constant — catch #155).**
   sum_{M dyadic, 2 <= M <= t} Q_M(A_own(M))  <=  (1 + 2^-690) * Q_2(k+2),
i.e. the whole extension costs the profile clause ONE first-scale column
plus epsilon per band cell. The worst excess over the grid is EXACTLY at
(s, rho) = (13, 1/16), value 2^-690.2765 (exact integer comparisons:
excess * 2^691 > 1, excess * 2^690 <= 1), and is carried by the M = 4
term ((tail - Q_4) <= 2^-300 * Q_4 grid-wide on the exact regime). THE
PRE-COMPUTED CONSTANT 2^-691 IS FALSE at the worst cell (bit-length
rounding, same family as #154a/c); (1 + 2^-690) is the honest uniform
constant. Verification: exact bigint s = 13..20; certified integer-only
entropy bounds s = 21..44 (min certified margin 168245 bits beyond the
691-bit requirement, at (21, 1/16)); certificates cross-checked against
exact values on s = 15..20 (24 rows).

**(v) Absorption (imgfib's reserve arithmetic).** (a) The aggregate new
mass is <= 719 * (1 + 2^-690) * Q_2(k+2) per band cell — one first-scale
column at the SAME uniform 719 allowance the M > t composite already pays;
no new constant, no n^B charge (pin P3 intact). (b) This is the profile
clause's OWN scale of mass, not an inflation: exactly
Q_2(k+2) = Q_2^planted(k) * (n/2 - 1 - k/2)/(k/2 + 1), ratio in
[2047/2049, 15) over the grid (exact rationals), where Q_2^planted(k) =
C(n/2 - 1, k/2) is the PROVED unavoidable planted lower count
(v13_capf_planted_lower_count) carried by a single received word. (c) The
old ledger is negligible in the extended total: banked top terms
2^99.81 / 2^66.15 / 2^82.97 vs the new top term Q_2(k+2) >= 2^L with
certified L >= 1.09e12 bits at every official maximal row.

**Scope remark (catch #156).** The rate-1/2 parity triviality
("B_quot = 0 exact"; dyadic_profile_evaluation §4.1, xr_target_budget_audit)
is a statement about the banked odd-A M > t_res rows ONLY. The EXTENDED
ledger's rate-1/2 own-cell rows are nonzero — indeed Q_2(k+2) =
C(n/2-1, n/4+1) at rho = 1/2 is the grid's largest first-scale column, and
the COL cap attains its maximum 4 exactly there. Any consumer citing
"rate 1/2 carries no dyadic quotient mass" must scope the citation to the
banked M > t_res rows.

## Falsifier (F(G)-3, pre-registered in bsr_falsifiers.md — EXECUTED)

Dominance failing at any official (s, rho, M <= t) cell, or the
719-weighted extended ledger not absorbed. qme_verify.py executes it over
the full grid: PASS everywhere with the corrected constant (and the
2^-691 form FAILS at (13, 1/16) exactly as catch #155 records — kept as a
live regression guard/mutation control MUT2).
