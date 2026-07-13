# qme_proof — QA.22 M <= t EXTENSION: proofs
# (companion to qme_statement.md; every numbered claim is also a qme_verify.py
# PASS line — proofs first, machine record second)

Throughout: n = 2^s (13 <= s <= 44), rho in {1/2,1/4,1/8,1/16}, k = rho*n,
t = (n-k)/2, M dyadic with 2 <= M <= t (hence M | n), N = n/M,
h_M = ceil((k+1)/M), A_own(M) = M*h_M, Q_M(A) = C(n/M - 1, floor(A/M)).
k is a 2-power >= 2^9, so k is even and k+1 is odd.

## Clause (i) — nondegeneracy

**Lemma i.1: A_own(M) <= k + M.** ceil((k+1)/M) <= floor(k/M) + 1 (since
k+1 <= M*floor(k/M) + M whenever M does not divide... directly: k+1 <=
M(floor(k/M)+1) because k < M(floor(k/M)+1) and both sides integers).
Multiply by M: A_own <= M*floor(k/M) + M <= k + M. (Equality A_own = k+M
iff M | k: then ceil((k+1)/M) = k/M + 1 since M does not divide k+1, k+1
being odd and M even.)

**Lemma i.2: A_own(M) <= n - M for M <= t.** By i.1, A_own <= k+M, and
k + M <= n - M <=> n - k >= 2M <=> M <= t. Hence h_M = A_own/M <= n/M - 1
and Q_M(A_own) = C(N-1, h_M) >= 1. Boundary exact at (rho, M) = (1/2, t):
n = 4t, A_own = 3t = n - M, h = 3 = N - 1, Q = 1. Also A_own >= k+1 by
definition of ceil (band floor: the own cell is never below the k+1 band).
csp cell: h = k/2 + 2 <= n/2 - 1 <=> k + 6 <= n, true in scope. QED
(grid-verified, 3392/3392 cells + 128 csp cells).

## Clause (ii) — the COL landing fits the 719 line

n - A_own >= n - k - M >= n - k - t = t (sigma = 1), so
n/(n - A_own) <= n/t = 2/(1 - rho) <= 4 for rho <= 1/2.
Lemma COL (petal_column_lemma, PROVED): realized classes at (M, A_own) <=
C(N, h_M) = [n/(n - A_own)] * Q_M(A_own) <= 4 * Q_M(A_own) <=
719 * Q_M(A_own). Headroom before any band/petal filtering: 719/4 = 179.75.
Per-rate maxima of n/(n-A_own) over the grid (exact, attained):
rho = 1/2: 4 (only at M = t = n/4, A_own = 3n/4); 1/4: 2 (at M = n/4,
A_own = k + M = n/2); 1/8: 4/3 (at M = k = n/8, A_own = n/4, and again at
M = n/4 where h = 1, A_own = n/4); 1/16: 4/3 (at M = n/4, h = 1,
A_own = n/4). The exact per-rate table {4, 2, 4/3, 4/3} of bsra claim 1
step 5 is reproduced as EQUALITIES (verify.py asserts equality, not <=).
csp cell: n/(n-k-4) <= 4 <=> n - k - 4 >= n/4 <=> 3n/4 - 4 >= k, true for
rho <= 1/2, n >= 16. QED (grid-verified equalities + caps).

## Clause (iii) — dedup unchanged

(a) Vs the M > t composite: the extension's scale range is [2, t], the
composite's is (t, n] — disjoint. The stabilizer partition (PROVED,
petal_g2_support_forcing) makes exact scale c(S) a function of the class,
so each class lands at exactly one cell (c(S), |S|): within the union
ledger no class is charged twice and none is silently uncharged (top-band
full-petal periodic classes have 2 <= c(S), and c(S) <= t or > t
exhaustively). This is bsr_consistency D1 verbatim; nothing changes.

(b) Vs the banked QA.22 rows (M > t_res at row agreement A_row = k + t_res):
the M-ranges DO overlap (e.g. prize 1/4: banked M* = 2^34, extension
range reaches 2^39). Disjointness is by parity of the A-coordinate:
A_own(M) = M * h_M is a multiple of the even M, hence EVEN; every banked
QA.22 row has A_row = k + t_res ODD (k even, t_res odd at all seven banked
rows — the corridor's reserves are 2^j + 1 shapes; verified: 507, 261,
133, 67, 558345748481, 283467841537, 141733920769 all odd). So no (M, A)
cell of the extension coincides with a banked row; the banked rows'
VALUES are untouched (the node's own verify.py replayed ALL PASS this
session — §Machine record). SCOPE PIN: parity disjointness is verified at
the banked rows; if a future corridor row with EVEN reserve is banked, the
check must be re-run (one line, in qme_verify.py already as a table).

## Clause (iv) — first-scale dominance at (1 + 2^-690)

**Statement.** For every grid row: T := sum_{M dyadic, 2<=M<=t}
Q_M(A_own(M)) <= (1 + 2^-690) * Q_2(k+2), where Q_2(k+2) is the M = 2 term
(A_own(2) = k+2). Equivalently tail := T - Q_2(k+2) <= 2^-690 * Q_2(k+2).

**Regime A (s = 13..20): exact.** All terms computed as exact big
integers; excess = tail/Q_2 as an exact Fraction. Result: max excess over
the 32 rows = 2^-690.2765, at (13, 1/16); exact comparisons
excess * 2^690 <= 1 (PASS grid-wide) and worst * 2^691 > 1 (the 2^-691
claim is FALSE — catch #155). The tail is the M = 4 term up to 2^-300
relative error at every row ((tail - Q_4) * 2^300 <= Q_4, exact; the
successive scales drop as ~Q^(1/2), the PROVED node's §2 mechanism).

**Regime B (s = 21..44): certified, integer arithmetic only.** Two
classical inequalities, proofs one line each:

- (B1) C(a,h) <= 2^{a*H(h/a)} for 0 < h < a, H binary entropy:
  1 = (h/a + (a-h)/a)^a >= C(a,h) (h/a)^h ((a-h)/a)^{a-h}.
- (B2) C(a,b) >= 2^{a*H(b/a)} / (a+1): the term at index b is the largest
  of the a+1 terms of 1 = sum_j C(a,j) p^j (1-p)^{a-j} at p = b/a
  (maximality of the mode at j = b when p = b/a... standard: the ratio of
  consecutive terms crosses 1 at j = b; hence the b-th term >= 1/(a+1)).

a*H(h/a) = h*log2(a/h) + (a-h)*log2(a/(a-h)) is sandwiched by dyadic
rationals: for rational x > 1 and precision denominator 128, the integer c
with 2^c <= x^128 < 2^{c+1} (decided by EXACT integer power-and-shift
comparisons, asserted in code) gives c/128 <= log2(x) <= (c+1)/128. So
every needed log2 is bounded above/below with gap 1/128, and

- LOWER: log2 Q_2(k+2) >= L := b2*lb(a2/b2) + (a2-b2)*lb(a2/(a2-b2)) -
  bitlen(a2+1), a2 = n/2-1, b2 = k/2+1 [by B2];
- UPPER, per tail cell with N > 2^16: log2 Q_M <= u_M := h*ub(a/h) +
  (a-h)*ub(a/(a-h)) [by B1]; cells with N <= 2^16 are computed EXACTLY
  (they are tiny) and accumulated into T_small.

Certification: T_small < 2^{L-691} (by bit length) and
cnt_big * 2^{max u_M} <= 2^{L-691} (exponent comparison, Fractions), hence
tail <= 2^{L-691} + 2^{L-691} = 2^{L-690} <= 2^-690 * Q_2(k+2). PASS at
all 96 rows s = 21..44; minimum certified margin beyond the requirement:
168245 bits, at (21, 1/16); at the four official maximal rows the margin
is >= 1.3e11 bits (table in verify output). VALIDATION: on s = 15..20 the
same certificates are computed alongside the exact values and bracket them
(L <= log2 Q_2 exact, u_M >= log2 Q_M exact) at all 24 rows — the
machinery is exercised against ground truth inside the exact regime.

**Why the constant is 2^-690 and not the pre-computed 2^-691 (catch #155).**
The exact worst excess is 2^-690.2765 > 2^-691. The banked "2^-691" came
from lg_frac(x) = x.numerator.bit_length() - x.denominator.bit_length(),
which for this mantissa pair rounds -690.28 to -691 (same rounding family
as catches #154a/#154c). The corrected constant is carried through
statement, verifier, and claim contract; MUT2 keeps the false form as a
mutation control that must trip.

## Clause (v) — absorption into imgfib's reserve arithmetic

(a) Per cell, the landing (<= 4 * Q_M by COL) fits the 719 * Q_M allowance
line (clause ii). Aggregating over the extension's scales via (iv), the
whole extension charges <= 719 * (1 + 2^-690) * Q_2(k+2) per band cell —
ONE first-scale column at the SAME uniform 719 allowance the M > t
composite pays (bsr_consistency D2: one constant, all consumers; the 9.49
bits of floor slack are NOT spent — 719 stays outside predicate exponents).

(b) The first-scale column is the profile clause's own scale of mass:
Q_2(k+2)/Q_2^planted(k) = C(a2, b2)/C(a2, k/2) = (a2 - k/2)/(k/2 + 1)
(one Pascal step; exact rational at every row, even s = 44), and
Q_2^planted(k) = C(n/2 - 1, k/2) is the PROVED planted lower count
(v13_capf_planted_lower_count: a single received word carries that many
codewords — no budget smaller than the column scale can be sound). Grid
range of the ratio: [2047/2049, 15), attained minimum at (13, 1/2),
supremum ~15 toward (44, 1/16). So the extended top line sits within the
fixed constant 719 * 15 of PROVED-unavoidable mass, and is never below
~0.999 * 719 * (planted): the profile hypothesis is charged at exactly its
own scale, uniformly on the grid.

(c) The old rows are unchanged (replay ALL PASS) and negligible: banked
deciding-scale terms are 2^99.81, 2^66.15, 2^82.97 (n-uniform, RowC =
prize), while the extended ledger's top term satisfies log2 Q_2(k+2) >= L
with certified L >= 1.09e12 at every official maximal row — the old
ledger perturbs the extended total by a relative 2^(100 - 1.09e12).

## Machine record (all runs 2026-07-13, tools/ramguard tiny)

1. qme_probe1.py — exact worst-cell discovery; minted catch #155.
2. qme_probe2.py — certificate machinery validation (24 overlap rows
   bracket; 96 large rows certified; 2.5 s).
3. qme_verify.py — the packet verifier: full grid, all five clauses, the
   #155 sharpness pin, five mutation controls (all TRIP). Output appended
   to qme_findings.md. RESULT: ALL CHECKS PASS.
4. critical/nodes/dyadic_profile_evaluation/verify.py — replayed ALL PASS
   (clause iii/v: banked rows unchanged).

## What this packet does NOT claim (scope honesty)

- No census counting claim: the count side is Lemma COL's (PROVED) and the
  gate's; this packet is the LEDGER side only (the D3 landing).
- The csp cell (2, k+4) is priced only IF consumed (SUCCESSOR-A x G1'(D)
  band scope, #152); its allowance line and nondegeneracy are verified
  here regardless.
- Parity disjointness (iii.b) is verified at the seven banked QA.22 rows;
  an even-reserve future row would need the one-line re-check.
- Nothing here supplies G1 coverage, clause (P), or any red predicate; the
  gate's conditionality on those is untouched. This packet closes exactly
  the single input named in the dag: qa22_m_le_t_extension.
