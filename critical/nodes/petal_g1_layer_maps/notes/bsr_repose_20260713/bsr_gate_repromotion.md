# Census gate re-promotion spec — petal_small_scale_staircase_census (DRAFT)

The gate was demoted (second time) at #144 pending the branch-split re-pose.
This spec re-promotes it on TWO independent suppliers, the primary one new.

## LEMMA COL (the primary supplier; word-free, chart-free, ~10 lines)

**Statement.** Let H be the order-n (n = 2^s) evaluation domain, U ANY
received word, M >= 2 dyadic, A a multiple of M with A >= k+1. Then the
number of realized exact-agreement classes of contributors to U at consumed
profile (M, A) — i.e. distinct exact supports S with |S| = A, c(S) = M —
satisfies

```text
   #classes(M, A)  <=  C(n/M, A/M)  =  [n/(n-A)] * Q_M(A)     (A < n),
```

with Q_M(A) = C(n/M - 1, A/M) the planted column. In particular, at the
gate's consumed P1-OWN band (A = A_own(M) = the least multiple of M that is
>= k+1; A_own = k + M when M | k) and consumed scales 2 <= M <= t:

```text
   #classes  <=  [n/(n - A_own)] * Q_M(A_own)  <=  4 * Q_M(A_own)
             <=  719 * Q_M(A_own).
```

**Proof.** (i) c(S) = M makes S invariant under the index-n/M translation,
so S is a union of full M-fibers with empty tail (stabilizer partition
theorem, PROVED `petal_g2_support_forcing`); there are exactly A/M fibers,
so S is one of the C(n/M, A/M) fiber-unions. (ii) |S| >= k+1 > deg, so the
support determines its codeword: classes = supports, each counted once
(also multiplicity 1 — codewords = classes — as banked). (iii) The identity
C(n', h) = C(n'-1, h) * n'/(n'-h) is Pascal at one point; n'/(n'-h) =
n/(n-A). (iv) In scope, A_own <= k + M <= k + t and n - k - t = t (sigma=1),
so n/(n-A_own) <= n/t = 2n/(n-k) <= 4 at rho <= 1/2 — max EXACTLY 4 at
rho = 1/2, M = t (grid-verified s = 13..44, bsr_check P5). (v) M <= t is
precisely the nondegeneracy boundary: h <= n/M - 1 <=> A <= n - M <=> M <= t
at the own band — the gate's scale scope keeps the column nonzero. QED.

Notes. (a) Full-petal and band filters only SHRINK the left side; COL needs
neither, so it covers every band reading the gate might consume at the own
cell, every layout, ODD k included (the M-not-dividing-k scales' own cells
A_own = M*ceil((k+1)/M) included — closing the old #111-type caveats at the
gate). (b) COL sharpens catch #101's "classes <= C(N,h) caps the ratio at
n/M": the sharp cap at the consumed band is n/(n-A) <= 4, uniformly in n —
so the 719 line holds at ALL row sizes, not just n < 2^11; the #101
"reachable at n >= 2^11" excess lives only in widest-ALL cells (h -> n'-1)
that the gate does NOT consume (catch #113 pin, unchanged).

**In-vivo record (bsr_check P1):** all 372 banked cells, all 6 band tags,
514 profile cells: classes <= C(n/M, A/M) everywhere (max saturation 2/3 of
the support cap, at the (8,3,17) cell); rational identity exact everywhere;
multiplicity 1 everywhere; max classes/Q = 4/3 (allowance genuinely needed,
as banked).

## The re-promotion

- **status:** re-promote TARGET -> CONDITIONAL, and to PROVED-pending-audit
  once the single named consumer item lands (below). The COUNT side of the
  gate is closed by Lemma COL; nothing about the count is conditional.
- **statement served (the gate's ORIGINAL column form, band-pinned):** at
  official rows, per received word U, realized top-band full-petal classes
  with 2 <= c(S) <= t, per consumed profile cell (M, A_own(M)) [P1-OWN
  consumption pin, unchanged], number <= 719 * Q_M(A_own) — by COL(iv),
  with 719/4 ~ 180x headroom before any full-petal/band filtering.
- **supplier map (r2):**
  - scales 2 <= M <= t, P1-OWN cells: **Lemma COL** (primary; word-free);
  - same cells, chart words: **SUCCESSOR-A x G1'(D)** (secondary,
    chart-carrying — kept wired because the G3 charge-once compiler consumes
    per-chart structure, and as the audit cross-check: two independent
    mechanisms, one truth);
  - the {k+2, k+4} band cells (csp band, if consumed instead of OWN):
    Lemma COL again — ratio n/(n-k-4) <= 4 in scope (bsr_check P5);
  - scales M > t: the replayed 7-lemma composite via
    dyadic_profile_evaluation (unchanged);
  - aperiodic bucket: clause (P) + PROVED chart-level K4 (unchanged
    ownership; NOTE #145 — the aperiodic bucket's band pin is now known
    load-bearing, see bsr_g1prime_statement.md).
- **the single owed consumer item (gate mint route (a), now the ONLY open
  line):** extend `dyadic_profile_evaluation`'s budgeted profile ledger from
  M > t to 2 <= M <= t and re-verify imgfib's quotient-profile absorption
  with the uniform 719 allowance. The arithmetic is pre-computed
  (bsr_check P5): the added mass is sum_{M <= t} Q_M(A_own) <=
  (1 + 2^-691) * Q_2(k+2) at s = 13..20 (first-scale dominance, exact
  bigint; log2(Q_4/Q_2) < -5e11 at the maximal rows), i.e. the extension
  costs the profile clause ONE first-scale column + epsilon per band cell,
  at the same 719 allowance the M > t composite already pays. See
  bsr_consistency.md.
- **retired:** the descent/ESP/geometric-ledger route to a C(n/M)^6 bound
  (the successor red was #124-refuted; the ledger's petal-lane hypothesis is
  g1a-unsatisfiable). QRL T1/T2/T3 remain true and banked but are no longer
  load-bearing for the gate; the intrinsic_scale_geometric_ledger edge is
  retired (bsr_consistency.md D5). The #102 dedup concern dissolves: the
  exact-scale partition charges each class once at its own (c(S), |S|) cell.

## Falsifier status (re-posed honestly, #101/#126 discipline)

The literal falsifier ("banked engineered family exceeding the budgeted
column, sustained") is UNSATISFIABLE at the consumed cells once COL is
minted — classes <= 4 x column < 719 x column is a theorem there. Per house
law a dead falsifier must be re-posed, not kept as decoration:

1. **live falsifier (audit tripwire):** any banked or future census cell at
   a consumed profile with classes > C(n/M, A/M) — this would break the
   stabilizer partition theorem or interpolation itself, i.e. it guards the
   PROOF's premises. Executable at every census run (it is P1 of
   bsr_check.py; mutation MC1/MC2 confirm the tripwire is live).
2. **consumption-seam falsifier:** a consumer found charging a NON-OWN cell
   (A > A_own, in particular widest-ALL cells with h > k'+1) against this
   gate — there COL's cap degrades to n/(n-A) which is unbounded as
   h -> n'-1, and the gate does NOT price it (the #113 seam, now with the
   exact boundary formula). Executable by grep/audit of consumer wiring.
3. **landing falsifier:** the dyadic_profile_evaluation M <= t extension
   failing first-scale dominance at any official shape — exact bigint,
   executable NOW (bsr_check P5 covers s = 13..20 + lgamma at 41..44; the
   extension worker must run the full s-grid).

## Re-surgery criteria

1. Falsifier 1 fires anywhere (premise breach — escalate to
   petal_g2_support_forcing, not just this gate).
2. The P1-OWN consumption pin is changed (then re-run COL(iv) at the new
   band; the {k+2,k+4} and EDGE bands are pre-verified; widest-ALL is NOT
   covered and must not be consumed).
3. The imgfib landing re-verification finds the 719 allowance not absorbed
   (then C_col renegotiates DOWN toward 4 — COL gives 180x room — or the
   profile clause re-scopes; criterion 5 of petal_growth r2 fires).
