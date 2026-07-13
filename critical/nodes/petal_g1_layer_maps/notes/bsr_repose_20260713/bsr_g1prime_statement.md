# G1' — the branch-split re-pose of petal_g1_layer_maps (DRAFT for surgery)

- **replaces:** the falsified weighted-atlas G1 (FALSIFIER FIRED 2026-07-13,
  catches #138-#144) — the single n^6-capped budget clause is SPLIT BY BRANCH.
- **consumers:** clause (P): `petal_k4_primitive_bound` package -> `petal_growth`
  (primitive line). Clause (D): `petal_chart_carrying_descent` 3-C ->
  `petal_small_scale_staircase_census` -> imgfib quotient-profile clause (pin P3).
- **verifier:** bsr_check.py (ramguard tiny; ALL CHECKS PASS 2026-07-13) — banked
  372-cell replay, g1a-instance fit, fresh censuses at 3 cells, mutations 4/4.
- **provenance:** #144 (the demand, not the mechanism, was wrong: the exponential
  mass is ~1/(4q(k'+1)) of the planted column — column-relative tiny); #139
  (P3-curse: no amortization inside the band); #143 (DD-atlas is the honest
  mechanism); #145 (NEW, this packet: the primitive clause's band pin is
  load-bearing).

## Setting (pinned, inherited)

Official rows n = 2^s, k = rho n, rho in {1/2, 1/4, 1/8, 1/16}; sigma = 1
fiber-aligned chart layout where charts are consumed (petal size ell = 2);
E22 canonical remainder |R0| < ell; retained-zero constraint Psi(P)|_R0 = 0
(catch #107); layer dictionary a = ell + d - |R0| unchanged. For k even and a
chart word U, the descended word u1 at the quotient row (n' = n/2, k' = k/2)
is as in csp S2 (WORD normalization — labels c_i against L_{Z'}; the
layer-normalized labels are c_i/(y_i - y_nf), catch #133; checkers must
assert census nonemptiness, catch #137). Reading A (core'' = Z' u {y_nf},
sigma' = 0, r' = 0) is pinned (catch #129). Q_M(A) := C(n/M - 1, A/M), the
planted column at consumed profile (M, A) (cg_petal_census convention;
petal_g3_profile_conversion_identity's Q_M).

---

## CLAUSE (P) — PRIMITIVE branch (n^6-priced; remains TARGET/red)

At every official row and every received word U, the APERIODIC (c(S) = 1)
top-band full-petal contributors are covered by an explicitly defined finite
first-match atlas A_U^prim of fixed (D0,R0) sunflower auxiliary layers (the
printed dictionary, coset petals, |R0| < ell, retained-zero), with the paid
WEIGHTED census

```text
    sum_(chart chi in A_U^prim) (m_chi + 1)  <=  (121/128) n^6.
```

K4 (PROVED, chart level, b4 = 1) bounds each chart's complete image by
m_chi + 1, so this weighted census is exactly the aggregate primitive
payment; with no descended-primitive rider the package coefficient is
(121/128) < 1 outright (the 64/63 ledger factor is RETIRED — see
bsr_consistency.md D5).

**BAND PIN (load-bearing; catch #145).** Clause (P)'s "top band" is the
FLOOR band d >= ell(t_ch - 2) (t_ch = the chart's petal count — pin P1's
deep reading). This pin is NOT a convenience: under the per-member/wide band
d >= ell(m - 2) (m = touched petals) the clause is ALREADY FALSE by pure
counting, for EVERY field q — the split-point odd-lift family
f = (X - x_nf) g(X^2), g the exact-k'-agreement interpolants of u1, supplies
~C(n'-1, k') aperiodic top-band full-petal classes (|S| = k+1: the free
agreement at x_nf plus fiber-paired interpolation kills the q-suppression;
machine-verified: 6012 realized of 6435 supply at (32,16,97), each verified
aperiodic + full-petal + wide-band end-to-end), and
C(63,32) = 2^59.7 > (121/128) 128^6 = 2^41.3 already at (128, 64).
Under the floor band the same family is capped by
sum_{z <= z0} C(k'-1,z) C(t_ch, k'-z), z0 = (k'-1) - (t_ch-2): poly at rate
1/2 (993 at (128,64); measured 53 <= 57 at (32,16,97)) and EMPTY at rates
<= 1/4 (z0 < 0; measured 0 at (32,12,97)). If pin P1 is ever resolved to the
wide reading, clause (P) must simultaneously acquire an odd-lift carve-out
(the split-point sub-band priced by its own column, C(n'-1,k')-shaped, to
the profile clause) — pre-registered as re-surgery criterion (P)-3 below.

**SCOPE PIN (quotient closure REMOVED).** Clause (P) quantifies over
OFFICIAL rows only. The old quotient-descendant quantifier existed to feed
the geometric ledger's descended-primitive route; that route is dead (g1a:
no n'^6-capped atlas exists at descended chart words) and no surviving
consumer needs quotient-row aperiodic atlases for arbitrary received words
(such a demand is #124-refuted anyway below the Johnson radius). K4's
chart-level theorem remains row-agnostic; only the ATLAS demand retreats.

**Status: TARGET (red).** This is the petal family's one remaining supply
red. Open content: atlas existence/coverage for arbitrary U at the floor
band within the weighted budget.

## CLAUSE (D) — PERIODIC branch (column-priced; proposed PROVED)

For every official row with k even, every fiber-aligned sigma = 1 chart word
U (all labels c in (F_q^*)^t), the DD-CONSISTENT MINIMAL-CHART ATLAS at the
quotient row,

```text
  A'(u1) := { (W, P) = (S' n core'', S' \ core'') :
              S' a DD-consistent support, y_nf in S',
              |S'| in {k'+1, k'+2} },
```

(DD-consistent = some deg <= k'-1 interpolant of u1 exists on S'; an
explicit, list-independent, algebraic definition — #143(a)) satisfies:

1. **(coverage)** every contributor class S' of u1 with y_nf in S' and
   |S'| in {k'+1, k'+2} (the consumed band, = official scale->=2 top band
   |S| in {k+2, k+4} via the S4 bijection, #135) is covered by its own
   minimal chart: realized classes are DD-consistent (their interpolant is
   the member itself), (W, P) is a legal reading-A band chart (z >= 1 since
   y_nf in W; z <= k'-1 by csp U2; m' = |S'| - z <= d'+2), and
   S' n core'' = W, S' \ core'' <= P hold by construction;
2. **(column-priced cardinality census)** per consumed profile
   a' in {k'+1, k'+2} (official (M, A) = (2, 2a')):

   ```text
   |A'_{a'}(u1)|  <=  C(n'-1, a'-1)  <=  C_col * Q_2(2a'),      C_col = 719.
   ```

   Proof of the second inequality: C(n'-1, a'-1) / C(n'-1, a') = a'/(n'-a'),
   which over the official grid (s = 13..44, all four rates) is at most
   1.00196 (max at s = 13, rho = 1/2, a' = k'+2) — verified exactly in
   bsr_check P5. Even C_col = 2 would close in scope; 719 is chosen for
   allowance-line uniformity with the M > t composite and the floor
   (719 = floor(n^6 / C(n+6,6)) at the four official maximal rows) and
   gives ~350x margin against the trivial bound, ~2^33..2^275 against the
   measured/proved truth (bsr_check P2);
3. **(chart injectivity)** distinct covered classes have distinct minimal
   charts (S' = W u P is recoverable), so with csp Claim 2 (U0/U1: at most
   one member per band chart) the count consumed downstream is
   #classes <= |A'| — CARDINALITY, not weight;
4. **(L0 rider)** the single M = 2 census prices every dyadic scale
   2 <= M <= t simultaneously (scale-M supports are K_2-invariant, csp L0).

**Weighted-census NON-demand (catch #141 honored).** No consumer of clause
(D) consumes sum(m'+1): the periodic branch pays 1 class per chart by
uniqueness, so cardinality suffices. A weighted corollary holds with the
extra factor (k'+3) (minimal-chart weights m'+1 <= a'-z+1 <= k'+3) but is
NOT part of the clause; any future consumer wanting weights must take the
poly factor explicitly — a constant C_col cannot absorb it.

**Truth calibration (#144).** The g1a floor puts the realized band-class
count at >= C(n'-1,k')/(4q(k'+1)) for worst-case labels — a fraction
~1/(4q(k'+1)) of the column: the clause's budget sits above the proved floor
by ~ 4 * 719 * q * (k'-1)-ish and above every banked measurement (all 372
cells, the #131 fiber-rich census 36,646 @ (64,16,193) vs 719*C(31,9) =
1.45e10, the fresh censuses here: 63 <= 719*C(31,9)-cell analogs, ratios in
bsr_check P4).

**Status: proposed PROVED** (proof = the four numbered lines above, each
either banked-PROVED (csp U0-U2, L0, S4, #135), a one-line binomial
identity, or the grid computation in bsr_check P5; in-vivo verification at
(16,8,97), (32,16,97), (32,12,97): B <= N_DD <= C(n'-1,a'-1) <= 719 Q at
every profile, banked member pins 3/63/47 reproduced). Owed before
consumption: the house fresh-context audit replay.

**Scope (inherited csp scope-outs, verbatim):** k even; sigma = 1
fiber-aligned charts; M > 2 via L0 only; sigma > 1 and odd k NOT claimed
(for the census gate those cases are covered word-free by Lemma COL — see
bsr_gate_repromotion.md — so no consumer is starved by this scope).

---

## Falsifiers (pre-registered; see bsr_falsifiers.md for executability)

- **(P)-1:** an aperiodic floor-band full-petal contributor family at scaled
  official-like rows whose necessary weighted chart census exceeds
  (121/128) n^6, sustained across scales. Executable at n = 32..128, any
  prime q = 1 mod n (complete enumeration to n = 32; odd-lift/engineered
  plants at n = 64..128).
- **(P)-2:** a floor-band aperiodic contributor covered by no legal chart.
- **(P)-3 (band tripwire):** pin P1 resolved to the wide/per-member band
  WITHOUT the odd-lift carve-out — clause (P) is then pre-falsified by the
  #145 arithmetic (C(63,32) > (121/128)128^6; pure bigint, no run needed).
- **(D)-1:** a chart word u1 with a realized consumed-band class covered by
  no chart of A'(u1) — by construction requires a realized class that is
  DD-INconsistent: unsatisfiable (its member is an interpolant), kept as an
  audit tripwire; executable as stated at n' <= 32 by complete enumeration.
- **(D)-2:** |A'_{a'}(u1)| > 719 Q_2(2a') at any official-shaped cell —
  needs a'/(n'-a') > 719: unsatisfiable in scope (max 1.002); satisfiable
  and REQUIRED-TO-TRIP on the mutation ladder (shifted column, C_col = 1) —
  bsr_check P6 confirms both trips.
- **(D)-3 (#137 vacuity tripwire):** any clause-(D) checker whose census is
  EMPTY at a cell where the banked pins (3/63/47) are nonzero.

## Consistency record (bsr_check, ALL PASS)

Banked 372 cells x 6 band tags = 514 profile cells: zero violations of the
column line, of the COL support cap, of multiplicity-1; max ratio 4/3.
g1a instances (256,128,65537), (8192,4096,q=33710081), (512,256,2^128),
(1024,512,2^256): old form violated by 54..4000+ bits (falsification
reproduced), column form fits with 33..275-bit margins. Fresh censuses:
pins 3/63/47; clause-(D) chain B <= N_DD <= trivial <= 719Q at all six
profiles; minimal-chart injectivity; S2 identity; mutations 4/4 trip.
