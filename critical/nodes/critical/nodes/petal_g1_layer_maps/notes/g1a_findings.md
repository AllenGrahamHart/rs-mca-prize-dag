# g1a_findings — G1 coverage hypothesis (petal_chart_carrying_descent conditional) — 2026-07-13
# Catch ledger continues from #137.

Mission: prove the COVERAGE hypothesis as wired in
critical/nodes/petal_chart_carrying_descent/conditional.md (reading-A band
charts covering all contributor classes S' of u1 with y_nf in S',
k'+1 <= |S'| <= k'+2, within sum(m_chi+1) <= (121/128) n^6).

## TURN 1 — sources read (verbatim)

- critical/nodes/petal_chart_carrying_descent/conditional.md (the consumed form)
- csp_statement.md (Claims 1/2/3: S1-S6, U0-U2, L0+C; scope; #133-#135 pins)
- csp_proof.md (Lemma L1 classes<->codewords; S3 lift form)
- csp_findings.md (#131 measured censuses; #135 band = |S'| in {k'+1,k'+2})
- background/nodes/quotient_row_subjohnson_bound/sjb_refutation_proof.md
  (#124-#127; e1-fiber bijection; supply law; SUCCESSOR-A/B)
- critical/nodes/petal_g1_layer_maps/{statement,claim_contract,attack,frontier}.md
  (budget (121/128)n^6; pre-registered falsifier: "a family whose necessary
  weighted chart census exceeds (121/128)n^6")
- ccd_findings.md catches #128-#132 + honest-scope section
- critical/nodes/e22_agreement_cofactor_equations/statement.md (cofactor form)
- dag.json: f3_shiftpair_weld, f3_h2_stratum_theorem,
  v13_second_moment_shift_pair_identity (what the F3 lane actually proves:
  h=2 stratum T_2 <= (2/3) n^{5/2}; weld at top stratum; NOT width-a censuses)

## TURN 1 — the structural findings (algebra first; verification scripts follow)

### F1. Coverage is free; the hypothesis IS a weighted class census (exactly)

For each realized band class S' (y_nf in S', |S'| = k'+j, j in {1,2}), its
minimal chart (W = S' n core'', P = S' \ core'') is a legal reading-A band
chart: z >= 1 (y_nf in W); z <= k'-1 because z = k' forces g = 0 on core''
(deg g <= k'-1, k' zeros) which has only k' agreements (csp U2: d' = 0 charts
empty); m' = |S'| - z <= k'+2-z = d'+2 (band). It covers S' tautologically.
CONVERSELY (the P3-CURSE): by csp U1, every band chart holds AT MOST ONE
member, and a chart (W,P) covering a class S' makes that class's codeword a
member of (W,P); hence EVERY covering atlas satisfies |A'| >= #classes and,
since a covering chart needs m_chi >= |I'| >= d'+1 >= 2, weighted census
>= 3 * #classes. Therefore

  coverage-within-budget  <=>  weighted realized band-class census fits:
     3 * B(u1) <= sum(m_chi+1)_necessary, and the minimal-chart atlas
     achieves sum <= (k'+2) * B(u1)   (weight m'+1 <= |S'|+1-z+... <= k'+3).

So the open content is EXACTLY: B(u1) (weighted) <= (121/128) n^6. No atlas
creativity can beat the class count; none is needed above it.

### F2. The cofactor equation for u1 (E22 form) and the pinning count

g (deg <= k'-1) interpolates u1 on S' = W u I' (|S'| = k'+j) iff the Newton
divided differences of orders k'..k'+j-1 vanish: EXACTLY j equations.
For j = 1, u1 = 0 on W and u1(y) = c_{i(y)} L_{Z'}(y) on petal points:

  (DIAMOND)  sum_{y in I'} c_{i(y)} * [L_{D0'}(y)/(y - y_nf)] / L'_{I'}(y) = 0

using L_{Z'}(y)/L_W(y) = L_{D0'}(y)/(y - y_nf) (catch #133's algebra),
L'_{S'}(y) = L_W(y) L'_{I'}(y). All coefficients of the c-variables are
NONZERO (petal points avoid core''; distinct points). For j = 2 the second
equation is the order-(k'+1) divided difference on the full S' — again
affine-linear in the labels with nonzero coefficient on each new petal point.

PINNING IMPOSSIBILITY (answer to mission item 2's hope): the number of
independent constraints is EXACTLY j = |S'| - k' in {1,2} — the codimension
of "some deg <= k'-1 interpolant exists" among all words on S' is j, period
(Newton triangular system; core-first ordering makes each successive
condition introduce a fresh petal label with nonzero Cauchy coefficient).
There is NO e2/e3/...-style extra pinning for chart words: first moment is
C(n'-1,k')/q + C(n'-1,k'+1)/q^2 and the exponential binomial prefactor is
per-word untouchable. The W_tau case is the j=1 instance whose single
equation happens to be e1(S) = tau; for u1 the single equation is (DIAMOND).

### F3. W_tau-form exclusion (mission item 3, answered exactly)

W_tau = X^{k'}(X - tau) restricted to the row vanishes at <= 1 row point
(only y = tau, if tau in H^2). u1 vanishes on ALL k' points of core''
(S2's word data; k' >= 2). The ZERO-SET CLAUSE of the sunflower word — not
the cofactor system — excludes W_tau-form from arising as a u1. However
(F4) the refutation's MASS transports into the chart class anyway.

### F4. THE FALSIFIER THEOREM (label-averaged lower bound; rigorous)

Setting: quotient row (n', k'), 2n' | q-1, q odd, u1 = chart word with label
vector c in (F_q^*)^t, t = n'-k'. Let B(c) := #band classes of u1 with
y_nf in S' (the consumed set). Define
  N1(c) := #{(k'+1)-supports S' with y_nf in S', DD-consistent}
         = sum_{g contributor, y_nf in A_g} C(|A_g|-1, k'),
  V(c)  := sum_{g: y_nf in A_g, |A_g| >= k'+3} C(|A_g|-1, k').
Then N1 <= (k'+1) B + V pointwise, so B >= (N1 - V)/(k'+1).

Averaging over the label torus:
 (i) For each support with m' >= 2 petal points, (DIAMOND) is one nonzero
     linear form in >= 2 torus variables: Pr_c = ((q-1)^{m'} +
     (-1)^{m'}(q-1)) / (q (q-1)^{m'}) >= (1 - 2/(q-1))/q.
     Supports with m' <= 1 (i.e. S' = core'' + one petal): never consistent
     (single nonzero term). Hence E[N1] >= (C(n'-1,k') - t) (1-2/(q-1))/q
     >= C(n'-1,k')/(2q).
 (ii) For each oversized support (size a = k'+j, j >= 3, y_nf in S), the j
     conditions are triangular in fresh petal labels => rank j =>
     Pr_c[A_g superset S] <= q^{t-j}/(q-1)^t <= 2 q^{-j} (q >= 2t). Hence
     E[V] <= sum_{j>=3} 2 C(k'+j-1,k') C(n'-1,k'+j-1) q^{-j}
           <= E[N1] * O((n'/q)^2)  — negligible for q >= 2(n')^2 (all
     official/prize fields qualify: q >= n^2 = 4 n'^2).
Therefore EXISTS c*: B(c*) >= E[N1 - 2V]/(k'+1) >= C(n'-1, k')/(4 q (k'+1)).

COROLLARY (falsification criterion): whenever
    C(n'-1, k') > 12 (k'+1) q * (121/128) n^6      [n = budget row length]
NO band-chart atlas covers the consumed band within budget for the chart
word with labels c* — i.e. the coverage hypothesis AS WIRED IS FALSE at that
cell. This is EXACTLY attack.md's pre-registered falsifier ("a family whose
necessary weighted chart census exceeds (121/128)n^6") and conditional.md's
re-surgery trigger.

Instances (exact arithmetic in g1a_check3):
- s=8, rate 1/2, minimal field (n0=256, q=65537, primary cell n'=128,k'=64):
  B(c*) >= C(127,64)/(4*65537*65) ~ 1.4e27 >> (121/128)*256^6 = 2.7e14.
- s=13, rate 1/2, q~2^26, primary cell n'=4096: B(c*) >= 2^{4039} vs budget
  2^{78} — violated by ~3960 bits (both budget readings).
- q = 2^128 (prize-typical): violated for n' >= 256 at rate 1/2 (s >= 9).
- q = 2^256 (prize cap): violated for n' >= 512 (rate 1/2) — matches the
  refutation's coverage table for W_tau, now INSIDE the chart class.

### F5. The honest positive windows

(a) PROVED unconditional window (trivial count; atlas = minimal charts of
    all DD-consistent band supports — explicitly defined from u1 by algebra,
    no list dependence): coverage-within-budget holds whenever
      (k'+3) [C(n'-1,k') + C(n'-1,k'+1)] <= (121/128) n^6.
    Rate 1/2 & 1/4: n' <= 32 under own-row budget; under top-row budget
    n' <= 64 for s >= 12; n' <= 128 needs s >= 22.
(b) CONDITIONAL middle window — the missing lemma at its sharpest:
    "per-word band-class first-moment upper bound": for EVERY label vector,
      B(u1) <= K * C(n'-1,k')/q + poly(n').
    (Cofactor-value equidistribution for sunflower words; e1_fullness-lane
    technology; open. CS/shift-pair route cannot supply it: the proved F3
    instruments are h=2/h=3 strata only, and even perfect equidistribution
    gives the TRUTH ~ C/q, which still violates the budget in the rich
    regime — so (b) can only serve the starved window
    n' H(rho) <~ log2 q + 6 log2 n.)
(c) Between (a)'s ceiling and F4's floor the hypothesis is exactly "class
    count fits" and the truth is first-moment: the boundary cell-by-cell is
    C(n'-1,k') ~ q n^6.

### F6. Weight-arithmetic catch

m' = d' + j with d' = #missed core (up to k'-1), j = |S'|-k' <= 2. The
mission brief's "m' <= d'+2 <= 4" conflates d' with the excess j. Typical
weight m'+1 ~ (1-rho)k' + 3 — polynomially large, not O(1). Affects only
constants here (weights <= k'+3), but any budget bookkeeping that assumed
O(1) weights must be corrected.

## TURN 2 — the falsifier theorem, proof-grade statement (packet-ready)

**THEOREM (label-averaged band-class floor for descended chart words).**
Let n' >= 8, 2 <= k' <= n'-2, t = n'-k', q odd with 2n' | q-1 and
q >= 2(n')^2. For a label vector c in (F_q^*)^t let u1(c) be the descended
concrete sunflower chart word of csp S2 (u1 = 0 on core'', u1(y_i) =
c_i L_{Z'}(y_i) on the t petal points), and let B(c) be the number of exact
agreement classes S' of u1(c) with y_nf in S' and |S'| in {k'+1, k'+2}
(the consumed band). Then there exists c* with

    B(c*) >= C(n'-1, k') / (4 q (k'+1)).

*Proof.* For g of degree <= k'-1 write A_g = agr(g, u1). Define
N1(c) = #{(k'+1)-subsets S' of the row, y_nf in S', admitting a deg<=k'-1
interpolant of u1}, and V(c) = sum over g with y_nf in A_g, |A_g| >= k'+3 of
C(|A_g|-1, k'). Every consistent S' lies in A_g for exactly one g (L1), so
N1 = sum_{g: y_nf in A_g, |A_g| >= k'+1} C(|A_g|-1, k') <= (k'+1) B + V
(band terms contribute C(k',k') = 1 or C(k'+1,k') = k'+1), giving
B >= (N1 - V)/(k'+1) pointwise.
(i) For a support with m' petal points, consistency is the vanishing of the
order-k' divided difference — one linear form in (c_y)_{y in I'} with all
coefficients L_{Z'}(y)/L'_{S'}(y) nonzero. For m' >= 2 the torus solution
count is ((q-1)^{m'} + (-1)^{m'}(q-1))/q, so Pr_c >= (1 - 2/(q-1))/q; m'<=1
supports are never consistent. Hence E[N1] >= (C(n'-1,k') - t)(1-2/(q-1))/q
>= 0.9 C(n'-1,k')/q.
(ii) For an oversized support (|S| = k'+j, j >= 3, y_nf in S), consistency
is j divided-difference conditions; ordering core points first, each
successive condition introduces a fresh petal label with nonzero
coefficient, so the system on the label torus has rank exactly j and
Pr_c <= q^{-j}(1+1/(q-1))^t <= 2 q^{-j} (q >= 2t). Hence
E[V] <= sum_{j>=3} 2 C(k'+j-1,k') C(n'-1,k'+j-1) q^{-j}
     <= (C(n'-1,k')/q) * sum_{j>=3} 2 base^{j-1}/(j-1)!,  base :=
     n'(n'-k')/(k'q) <= (n')^2/(k'q) <= 1/4  (q >= 2(n')^2, k' >= 2),
so E[V] <= 0.07 C(n'-1,k')/q. Then E[N1 - 2V] >= 0.76 C(n'-1,k')/q, and any
c* maximizing N1 - 2V has B(c*) >= (N1-2V)(c*)/(k'+1) >= that /(k'+1). QED
(constant stated as 1/4 for slack; the derivation gives 0.76).

**COROLLARY 1 (falsification of the consumed coverage hypothesis).** By csp
U0/U1 (PROVED), every reading-A band chart holds at most one member, and a
chart covering class S' makes S''s codeword a member; a covering chart has
m_chi >= d'+1 >= 2. Hence ANY atlas covering the consumed band satisfies
|A'| >= B and sum(m_chi+1) >= 3 B. Whenever

    3 C(n'-1,k') / (4 q (k'+1)) > (121/128) n_b^6      (n_b = budget row)

no atlas exists within budget: the coverage hypothesis of
petal_chart_carrying_descent/conditional.md is FALSE at that cell (for the
chart word with labels c*). This is exactly the pre-registered falsifier
(attack.md: "a family whose necessary weighted chart census exceeds
(121/128)n^6"; conditional.md re-surgery clause).

**COROLLARY 2 (official G1 falls at the same cells).** The official chart
word U* with labels c* is a legitimate received word; by S4 its scale->=2
band classes biject with the B(c*) descended classes and are top-band
full-petal official contributors. Official charts hold <= m_chi+1 classes
each (K4 / G1's own claim contract line), so any official atlas has
sum(m_chi+1) >= #classes = B(c*). At (n=256, k=128, q=65537) — an OFFICIAL
cell, q = n^2+1, 256 | q-1 — B(c*) >= C(127,64)/(4*65537*65) = 7.0e29
vs budget (121/128)*256^6 = 2.7e14: G1 as posed is FALSE by 15 orders.

**COROLLARY 3 (the demand itself is unsatisfiable, not just the route).**
The official scale->=2 top-band class census for U* EQUALS B (S4 bijection),
so no alternative mechanism can price it within n^6 either: at fiber-rich
cells the TARGET NUMBER is exponential. Re-surgery must re-pose the
downstream demand (q-weighted allowance or band/regime restriction), not
swap mechanisms.

## TURN 2 — exact windows (g1a_check3, all bigint)

Falsified-below threshold q* = 3C(n'-1,k')/(4(k'+1)(121/128)n_b^6),
first-moment-fit-above threshold q** = C(n'-1,k')((1-rho)k'+3)(128/121)/n_b^6,
trivial PROVED window (q-free): (k'+2)(C(n'-1,k')+C(n'-1,k'+1)) <= (121/128)n_b^6.

- Rate 1/2, own-row budget: n'=32 trivially PROVED; n'=64: q* = 2^12.3 <
  2(n')^2 (F4 needs q >= 2(n')^2, so NO rigorous falsification there), but
  q** = 2^22 — minimal official fields q ~ 2^14 sit in the first-moment-
  violated gap; n' >= 128: q* = 2^68.8 and beyond — all minimal official
  fields falsified.
- s=13 tower, rate 1/2, q ~ 2^26, top-row budget 8192^6: n'=64 trivially
  PROVED; EVERY n' in {128,...,4096} RIGOROUSLY FALSIFIED (primary cell
  n'=4096: B(c*) >= 2^4049 vs budget 2^77.9).
- Minimal official fields, rate 1/2, primary cell n' = n0/2: falsified for
  ALL s >= 8; s <= 7 in the gap/trivial zones.
- Prize fields: smallest rigorously falsified n' (rate 1/2) = 128 at
  q = 2^26..2^64, 256 at q = 2^128, 512 at q = 2^256 — matching the #124
  refutation's coverage table, now INSIDE the chart-word class.
- Rate 1/4 thresholds analogous (q* = 2^46.4 at n'=128, 2^142.8 at n'=256).

## TURN 2 — verification (all ramguard tiny, ALL PASS)

1. g1a_check1.py — tiny cell (n=16,k=8,q=17), EXACT, 43 label vectors incl.
   constant/degenerate: dual census (83521 brute codewords vs DD-consistent
   supports) N1 identity exact; band class sets identical; P3-curse in vivo
   (every band chart <= 1 member, exhaustive over all charts; minimal charts
   distinct); B >= (N1-V)/(k'+1); torus-count formula exact on real DIAMOND
   coefficients (m=2..4); oversized j=3 supports: rank/torus-count bound
   verified for ALL such supports; mutation control TRIPS (corrupted petal
   value breaks the dual census). ALL PASS.
2. g1a_check2.py — Monte Carlo at the consumed shape (n'=64, k'=32; official
   n=128 layout), q in {257, 641}, geom5 + random labels, 3e5-6e5 samples:
   DD-hit density * q = 0.978/0.970/1.032/0.982 (predict 1); exactness sieve:
   band fraction of hits 0.995-1.000 (oversized attrition negligible, as the
   E[V] estimate predicts); weight m'+1 mean 17.2-17.4 (poly, not O(1));
   implied #band classes ~ 3.5e15 at q=257 vs own-row budget 4.2e12 — the
   GENERIC label vector already violates at this toy field. ALL PASS.
3. g1a_check3.py — exact bigint window table (above). PASS.

## CATCHES #138-#144

- **#138 (THE FALSIFIER — coverage hypothesis as wired is FALSE).** The
  label-averaged floor B(c*) >= C(n'-1,k')/(4q(k'+1)) (theorem above; needs
  only q >= 2(n')^2, 2n' | q-1) makes the necessary weighted census of ANY
  covering band-chart atlas >= 3B, exceeding (121/128)n_b^6 at every
  fiber-rich cell: all minimal-official primary cells s >= 8 (rate 1/2),
  every n' >= 128 in the s=13 tower, n' >= 256 at q=2^128, n' >= 512 at
  q=2^256 — under BOTH budget readings. Official G1 (petal_g1_layer_maps)
  falls with it at official cells (Corollary 2; exact instance (256, 128,
  65537), 15 orders over budget). The pre-registered falsifier clause fires;
  conditional.md's re-surgery clause fires.
- **#139 (P3-CURSE).** The same PROVED uniqueness (csp U0/U1) that makes the
  m'+1 safety line safe makes band coverage maximally expensive: <= 1 class
  per band chart => |A'| >= #classes, weight >= 3 each. At ell' = 1 no
  amortization is possible INSIDE the band; any repair must leave the band
  (m' > d'+2) or leave ell' = 1 — both exit the consumed hypothesis's form.
- **#140 (PINNING IMPOSSIBILITY).** The number of independent constraints
  pinning a band support is EXACTLY j = |S'| - k' in {1,2} (Newton
  triangular system; core-first ordering). No e2/e3/...-style extra pinning
  exists for chart words: the fiber division is q^j with j <= 2, full stop;
  the exponential prefactor C(n'-1,k') is per-word untouchable. (W_tau's
  e1(S) = tau is the j=1 instance; u1's j=1 instance is the DIAMOND cofactor
  equation sum_{y in I'} c_{i(y)} [L_{D0'}(y)/(y-y_nf)]/L'_{I'}(y) = 0.)
- **#141 (WEIGHT ARITHMETIC).** m' = d' + j with d' = #missed core up to
  k'-1; typical minimal-chart weight is (1-rho)k'+3 (measured mean 17.3 at
  n'=64) — NOT "m' <= d'+2 <= 4"; that reading conflates d' with the excess
  j <= 2. Any budget bookkeeping assuming O(1) weights is off by ~k'.
- **#142 (W_tau EXCLUSION AND MASS TRANSPORT).** W_tau-form cannot arise as
  a u1: the excluding clause is the ZERO-SET clause (u1 vanishes on all k'
  core'' points; W_tau vanishes at <= 1 row point), not the cofactor system.
  But the refutation's mass transports into the chart class by label
  averaging: the enemy is the generic torus point c*, not a planted word
  (echo of #127 — the enemy is generic, not planted).
- **#143 (HONEST POSITIVE WINDOWS + instrument audit).** (a) Unconditional
  PROVED window: (k'+2)(C(n'-1,k')+C(n'-1,k'+1)) <= (121/128)n_b^6 — the
  minimal-chart atlas of all DD-consistent band supports (explicitly defined
  from u1, no list dependence) covers within budget; e.g. n' <= 32 all
  readings; n' = 64 under top-row budget for s >= 12. (b) Conditional middle
  window — missing lemma at its sharpest: PER-WORD BAND-CLASS FIRST-MOMENT
  UPPER BOUND (for every label vector, B(u1) <= K C(n'-1,k')/q + poly(n');
  cofactor-value equidistribution for sunflower words; e1_fullness-lane
  technology; open). (c) CS/shift-pair route CANNOT supply it: proved F3
  instruments are the h=2 stratum (T_2 <= (2/3)n^{5/2}) and h=3 char-0 only;
  width-(k'+1) censuses need all strata h <= k'+1; and even PERFECT
  equidistribution yields the truth ~C/q, which itself violates the budget
  in the rich regime — the sqrt(C) ceiling fits (n')^6 only for n' <= 64-128
  where (a)/(b) already operate. No route through this hypothesis reaches
  the prize envelope.
- **#144 (DEMAND, NOT MECHANISM).** Via the S4 bijection the official
  scale->=2 top-band census for U* EQUALS B(c*): the number the downstream
  gate wants priced is itself exponential at fiber-rich cells. Re-surgery
  must re-pose the demand (q-weighted allowance, e.g. the supply-law form
  qcore + C(n',a)/q^{a-k'}, or an explicit fiber-starved scope
  C(n'-1,k') <= q * poly), not swap coverage mechanisms.

## STATUS (deliverable 1)

- PROVED: the free-coverage reduction (coverage-within-budget <=> weighted
  realized band-class census fits; F1), the falsifier theorem + corollaries
  (packet-grade proof above, engine machine-verified at the tiny cell), the
  unconditional positive window of #143(a) with its exact per-cell criterion.
- FALSIFIED (not blocked — FALSE): the coverage hypothesis at the consumed
  generality, and official G1 as posed, at every cell with
  C(n'-1,k') > (16/3)(121/128)(k'+1) q n_b^6 and q >= 2(n')^2. Exact
  instances named; both pre-registered falsifier clauses fire.
- CONDITIONAL remainder: the middle window q in [q*, q**) is first-moment
  violated but not rigorously (gap factor ~ (k')^2); q >= q** needs the
  named equidistribution lemma. Neither affects the falsification above.

## ARTIFACTS (this scratchpad, g1a_-prefixed)

- g1a_findings.md (this file)
- g1a_check1.py (tiny-cell exact engine verifier; ALL PASS)
- g1a_check2.py (n'=64 Monte Carlo density; ALL PASS)
- g1a_check3.py (exact bigint window table; PASS)
