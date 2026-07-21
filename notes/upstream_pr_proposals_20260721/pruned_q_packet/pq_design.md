# pq_design: pre-registered design for the pruned-Q toy packet

Written BEFORE the main computation (only the raw anchors of pq_definitions.md §3,
which are his committed numbers, and hand-derivable closed-form cell counts appear
below). Answers agents.md Good-first-PR #1: "Write a small exact Q toy packet that
tests `prob:row-sharp-q` on a row where the full fiber distribution can be
enumerated."

## 1. Toy rows

All rows are HIS census rows (qsp_fiber_census.py FIBER_DEFAULT), for direct
comparability; the first two are the rows whose ratios are printed in
rem:capff1-collision-gap (cs25_cap_v13_2.tex L6334).

- R1 = (p,N,m) = (17,16,8), depths w = 1,2,3 — direct enumeration, C(16,8) = 12870.
- R2 = (41,20,10), w = 1,2,3 — direct enumeration, C(20,10) = 184756. Contains his
  mode-at-null datum row (w=2).
- R3 = (101,50,25), w = 2 — exact big-int DP over p^2 = 10201 cells (raw), plus an
  exact coset-DP for the cell members.
- R4 = (257,64,34), w = 1 — exact big-int DP over p = 257 cells (raw) plus coset-DP.

(257,64,34,2) is EXCLUDED: the pure-python exact DP over 257^2 cells with
C(64,34)-scale big ints is a >2-minute job; per the compute law the row is shrunk
(R4 keeps the same row at depth 1, still a committed exact anchor) rather than
raising limits.

## 2. Enumeration method (exact integers only)

- D = order-N subgroup of F_p^* built exactly as his script builds it
  (qsp_fiber_census.py L46-51): D = <g^((p-1)/N)>, g = smallest primitive root;
  elements listed as d[i] = h^i so that multiplication by h^s is index rotation
  by s.
- R1/R2: enumerate all C(N,m) m-subsets as index combinations; maintain the
  depth-3 power-sum prefix by summing precomputed (x, x^2, x^3) mod p; represent
  the subset as an N-bit mask for O(1) rotation tests.
- R3/R4: his DP recurrence (dp[c+1] += roll(dp[c], (x, x^2, ...))) reimplemented
  stdlib-only with python big ints (no numpy, no int64 caps) over flat lists with
  precomputed index permutations.
- Everything asserted is an exact integer or exact Fraction; floats appear only in
  display strings.

## 3. The pruning ledger (explicitly labeled as our first-match application of HIS
      in-tree toy classifiers)

Cells, in his script's order (qsp_modeatnull_structure.py L20-23) — first match:
a subset charged to C1 is not charged to C2:

- C1 "coset-union" (quotient-pullback, mu_2): S = -S, i.e. S is a union of
  antipodal mu_2-pairs. Membership test: mask invariant under index rotation by
  N/2 (the element h^(N/2) = -1).
- C2 "dilation-stable" (quotient-pullback, general): gS = S for some g in D,
  g != 1. Membership test: mask invariant under rotation by N/q for some prime
  q | N (a nontrivial stabilizer subgroup of a cyclic group contains a
  prime-order element; the order-q subgroup is <h^(N/q)>).

Residual P_Q(z) := members of Fib_w(z) in neither cell = subsets with trivial
multiplicative stabilizer in D ("primitive" in the natural toy sense, matching
grande_finale.tex L1846's "quotient ... certificates ... applied"). Since
C1 subset-of C2 whenever -1 in D (all four rows have N even), the residual is
independent of the cell order; order affects only the printed per-cell
attribution (consistent with L1283-1284 "order these cells arbitrarily").

FLAGGED SCOPE LIMIT: the deployed-row ledger's other cells (tangent,
common-support, planted, field-drop, extension, rank — grande_finale.tex L3561)
have no in-tree toy-scale instantiation and are NOT modeled; the packet says so
rather than silently treating them as empty.

Normalization for the pruned comparison stays at the FULL slice, per
grande_finale.tex L1837-1838 ("The normalization is taken from the full profile
slice, not from the possibly much smaller residual mass"): mean := C(N,m)/p^w.

Hand-derived expected cell totals (to be confirmed two ways at runtime):
- R1: |C1| = C(8,4) = 70, |C2 \ C1| = 0 (N=16 has only prime 2).
- R2: |C1| = C(10,5) = 252, |C2 \ C1| = C(4,2) - C(2,1) = 4 (mu_5-unions minus
  mu_10-unions), |C1 u C2| = 256.
- R3: |C1| = 0 (m = 25 odd), |C2| = C(10,5) = 252 (mu_5-coset unions; all lie in
  the null fiber at depths 1,2 because power sums of a mu_5-coset vanish at
  depths not divisible by 5).
- R4: |C1| = |C2| = C(32,17) = 565722720 (mu_2-pair unions; all in the null fiber
  at depth 1).

## 4. Independent cross-checks (every one is a named PASS/FAIL check)

Raw side (the cross-implementation anchor):
- checksum sum_z N_w(z) = C(N,m) (his L86 standard) on every row/depth;
- digit-exact match of max, null, and sum_z N_w(z)^2 against his committed JSON
  values (pq_definitions.md §3 table) on all 8 row-depth combos;
- second-moment identity consistency: sum N^2 - C(N,m) = SP mass >= 0;
- his printed four-decimal ratios: round(max/mean, 4) = 1.0012 / 1.2126 / 2.6722
  (R1 depths 1-3) and 1.0022 / 1.2101 / 4.1034 (R2 depths 1-3);
- mode-at-null datum replay at (41,20,10,2): null = 66, max = 133 attained at
  z = (11,0), dilation-orbit fibers all equal 133, argmax-fiber classifier counts
  = (0 coset-union, 0 dilation-stable).

Pruned side:
- per-fiber monotonicity pruned(z) <= raw(z) (grande_finale.tex L1895);
- mass identity sum_z pruned(z) = C(N,m) - |C1 u C2| with |C1 u C2| computed TWO
  ways: per-member classification (R1/R2) or generic coset-DP (R3/R4), vs the
  subgroup-lattice inclusion-exclusion of coset-DPs (R1/R2/R3/R4:
  |C2|(z) = sum over nonempty subsets Q of primes(N) of (-1)^(|Q|+1) A_prod(Q)(z),
  A_d(z) = number of unions of m/d distinct mu_d-cosets in fiber z, 0 unless d|m);
  the inclusion-exclusion is per-fiber, so the whole pruned DISTRIBUTION is
  double-computed, not just its total;
- hand-derived cell totals of §3 reproduced exactly.

## 5. Pre-registered comparison and falsifiable expectation

Quantities (exact Fractions): R_max^raw = p^w max_z N_w(z) / C(N,m),
R_max^pruned = p^w max_z |P_Q(z)| / C(N,m) (def:q-row-atom normalization), and
tau = sum_z |P_Q(z)| / C(N,m) (the "actual residual mass" that
prob:row-sharp-q / prop:q-moment-order-floor require a moment proof to use).

Gates (MUST PASS for the packet to print PASS):
- G1 structural: monotonicity + both mass identities + anchor reproductions above.
- G2 row-sharp-Q support: on EVERY tested row-depth, R_max^pruned <= R_max^raw and
  R_max^pruned < 8.4152, the binding deployed full-budget allowance
  (prop:q-exact-target; sec:finite-q-barrier L3546). Pre-registered expectation:
  YES on all 8 combos — supporting evidence for prob:row-sharp-q, since even the
  RAW ratios (1.0012 ... 4.1034, and ~1+eps at R3/R4) sit below 8.4152 and pruning
  can only decrease them. FALSIFIER SHAPE: a pruned (hence also raw) max fiber
  above 8.4152x the full-slice average at a tested row would be a negative
  calibration datum for the row-sharp form at toy scale. Caveat pre-registered:
  depth-3 rows are at the Poisson boundary (mean < 3) where his text pre-explains
  ratio growth (cs25_cap_v13_2.tex L6334); they are still gated at 8.4152 and
  expected to pass, but a failure there would indict the toy regime, not the
  dense-bulk deployed regime.
- G3 pruning strictness: at every row-depth where the null fiber contains cell
  members (per §3: R1 all depths, R2 all depths, R3, R4), pruned null < raw null.
  Expected: YES.

Also printed (informational, not gated): whether the pruned max stays at the raw
argmax or moves, per-cell removed counts, tau as exact fraction and decimal.

## 6. Output table

Per row-depth, in his print standard extended by one "pruned" line:

    fiber (p,N,m,w) EXACT: max/mean-1 = ..., null/mean-1 = ..., max = M, null = U
    pruned(p,N,m,w) [C1 coset-union: c1, C2 dilation-stable: c2]: max = M', null = U',
        tau = t, R_raw = r, R_pruned = r'

then a summary verdict table and the final line
    RESULT: PASS (X/X checks; 4/4 mutation controls caught)
(exit 0) or RESULT: FAIL (exit 1). Fail-closed: any check failure, any anchor
mismatch, or any uncaught mutation => FAIL.

## 7. Mutation controls (each must be CAUGHT, i.e. flip at least one named check)

- M1 wrong pruning-cell membership: pair test uses (p - x + 1) mod p instead of
  (p - x) mod p (and the classifier no longer matches the coset-DP
  inclusion-exclusion) — must be caught by the two-way mass/distribution identity
  or the mode-at-null classifier-count check.
- M2 off-by-one depth: power sums computed to depth w-1, labeled w — must be
  caught by the raw anchors (e.g. (17,16,8,2) max 758 != 54).
- M3 wrong bound constant: allowance 8.4152 -> 1.0 — must flip gate G2 (proves the
  bound comparison is live, not vacuous: (17,16,8,3) ratio 2.6722 > 1).
- M4 wrong domain: D replaced by the first N elements of F_p^* (not a subgroup) —
  checksum still C(N,m), but must be caught by the anchor values.

## 8. Budget

Single zero-argument stdlib-only script pq_verify.py; target < 60 s under
`tools/ramguard tiny -- python3` (256 MB / 60 s); estimated ~15-30 s (R2
enumeration ~6.5M ops; R3 DP ~1.3e7 index ops). If tiny is exceeded the fallback
is `ramguard local` with the reason recorded — not expected.
