# Proof of the refutation theorem + consequences, catches, and the honest successors

## 1. Proof of the t = 1 truncated-locator floor (six lines, self-contained)

Let c be any codeword (deg c < k') and W_tau = X^{k'}(X - tau) = X^{k'+1} - tau X^{k'}.
Then W_tau - c is MONIC of degree exactly k'+1, so it has at most k'+1 roots in F_q.

(=>) If the exact agreement support S = {x in D : c(x) = W_tau(x)} has |S| = k'+1,
then W_tau - c is a monic degree-(k'+1) polynomial vanishing on the k'+1 distinct
points of S, hence W_tau - c = L_S := prod_{x in S}(X - x) exactly, and comparing
X^{k'} coefficients: -tau = -e1(S), i.e. e1(S) = tau. Moreover S is then the FULL
root set, so the exact support is S — nothing off S agrees.

(<=) Conversely, for any S ⊆ D with |S| = k'+1 and e1(S) = tau, set
c := W_tau - L_S. The X^{k'+1} coefficients cancel (both monic), and the X^{k'}
coefficient is -tau + e1(S) = 0, so deg c <= k'-1 < k': a codeword. Its exact
agreement support with W_tau is precisely the root set of L_S in D, i.e. S,
of size exactly k'+1.

The two maps are mutually inverse (c determines L_S = W_tau - c determines S), so

    L(W_tau, k'+1) = #{S ⊆ D : |S| = k'+1, e1(S) = tau}    ... (exact, per tau).

Summing over tau in F_q partitions ALL (k'+1)-subsets of D by their element sum:
sum_tau L(W_tau, k'+1) = C(n', k'+1); pigeonhole gives max_tau >= ceil(C(n',k'+1)/q).

Aperiodicity for free: at the P1-OWN cell, |S| = k'+1 with k' = rho n' = 2^{s'-c},
s'-c >= 3 (k' >= 8), so |S| is ODD. The stabilizer of S in Z_{n'} = Z_{2^{s'}} is a
subgroup of a cyclic 2-group; a nontrivial stabilizer has even order and its order
divides |S| (S is a union of its orbits, all of size = stabilizer order). Odd |S|
forces the trivial stabilizer: S is aperiodic. QED.

Remark: no step used q >= n^2, the dyadic structure, or anything about D beyond
|D| = n' (the aperiodicity step uses D = the order-n' cyclic subgroup and k' even).
The bound is tight in-vivo: at (n'=64, q=65537) the measured fibers deviate from
C(n',k'+1)/q by < 0.02% (sjb_n64_fiber_demo.py) — the pigeonhole loses nothing.

## 2. Exhaustive validation of the semantics (mutation control)

sjb_semantics_tiny.py enumerates ALL q^{k'} = 83,521 codewords at (n'=8, k'=4,
q=17) and confirms, for every tau: the brute-force exact-agreement-5 list (exact
support semantics, aperiodicity under the true rotation action) coincides with the
e1-fiber as sets of supports. The averaging identity and the mass identity
sum_{c: A_c >= k'} C(A_c, k') = C(n', k') (a second, independent characterization
of the incidence semantics) hold exactly. Any misreading of "exact agreement
support", "aperiodic", or "codeword" would break these checks.

## 3. Why every step of the board's route was individually verified yet the target is false

The packet audit (qra_findings.md) verified T1/T2/T3 and the ESP arithmetic — all
TRUE, and all confined to n' <= 32, Johnson cells, or M >= k. The consistency
sweeps (514 census cells, 42 in-vivo words) all live at n' <= 32 or tiny rows,
where C(n', a) itself is below the cap (T1's window) — the fiber-rich regime
C(n',k'+1) >> q * cap starts exactly at the first open size n' = 64 (s <= 15) and
is unreachable by exhaustive enumeration (C(64,33) ~ 1.8e18), which is why every
in-vivo probe missed it. The pre-registered falsifier QRL-MODAL-1 enumerates
"complete for the constructed classes ONLY" — structurally blind to the generic
mass (catch #126). The first-moment model the board itself validated campaign-wide
(the window law; supply law fiber = qcore + Poisson background) PREDICTS this
refutation: the witness-hunt cells were fiber-STARVED (q^t > C(n,k+t)); the
quotient rows at minimal official fields are fiber-RICH, and the "Poisson
background" mean C(n',a)/q^{a-k'} is the exponential mass. The red contradicted
the board's own supply law in the regime nobody re-checked.

## 4. Upstream calibration (Paper D is consistent with the refutation — and only the board's red overshot)

- prob:band (v13 line 4624) — the aperiodic band conjecture — starts at
  a > k + 2n/N, DELIBERATELY excluding the near-capacity strip (k, k + 2n/N].
  The minted red claimed polynomiality at a = k'+1, INSIDE the excluded strip.
- prop:list-calibration: "No uniform subexponential L_Q exists in the band; only
  the aperiodic term CAN be uniformly polynomial" — a hope stated only for the
  band above the left edge. The subset-sum family shows the aperiodic mass is
  exponential throughout the strip a - k' <~ n'H(rho)/log2(q), which at razor
  fields sits below Paper D's left edge (n'/256 vs 2n'/N' = n'/128 at rho = 1/2,
  N' = 256 the planted 2^128-crossing): tight within a factor 2, no contradiction
  with any Paper D theorem — it vindicates their left-edge choice.
- The witness words X^{k'}(X - tau) are graded-locator-prefix words (the t=1 case
  of the banked truncated-locator moment map); the count is the t=1 e1-fiber.
  Second-moment/equidistribution technology for e1 over subgroups exists in-repo
  (e1_fullness lane) and empirically the fibers concentrate to 0.02% — the
  refutation is uniform over the family, not just existential.

## 5. Catches (#124-#127)

- **#124 (THE REFUTATION).** quotient_row_subjohnson_bound is FALSE as minted.
  Constructive family, exact instances at all four rates at the P1-OWN cell
  (the only cell the gate consumes), including the first open size n' = 64 at
  s in {13,14,15} at every admissible prime up to ~2^30.8; and at ALL prize
  fields (q < 2^256) for n' >= 512/512/1024/1024 (rho = 1/2,1/4,1/8,1/16), with
  doubling persistence. Machine-verified (3 scripts, ALL PASS).
- **#125 (ESP route dead by truth, strengthens #109/#115).** The true worst list
  at a = k'+1 exceeds the ESP capacity (q-3n')/2 at the minimal official field
  for every open scale of s = 13 (all rates' exhibits verified) — the #115 pin is
  unsatisfiable by ANY true lemma; transport through
  exact_support_interleaving_projection at those (row, scale, q) is impossible
  regardless of future proofs. The census-gate supplier map for n' >= 64 cannot
  be ESP-routed at small official fields.
- **#126 (falsifier mis-aimed).** QRL-MODAL-1 could not have caught the falsity:
  its enumeration is complete only for constructed classes, while the violation
  is carried by the generic e1-fiber mass; at its own grid cell (n=256, M=4,
  q=65537) the true complete aperiodic list at a = k'+1 is ~2.71e13 for EVERY
  word of the t=1 family (exact census) vs its pre-registered "max <= 2n' = 128".
  The node's "conjectural true size O(n'^2)" is false in the same stroke.
- **#127 (provenance/calibration).** The red overshot Paper D's own left edge
  (prob:band starts at k + 2n/N; the strip below it was deliberately excluded
  upstream); and the "load-bearing aperiodicity restriction" is VOID at the
  consumed cell (odd |S| in a cyclic 2-group is automatically aperiodic) — the
  planted/quotient-periodic exclusion aimed at the wrong enemy; the enemy is
  generic, not planted.

## 6. The honest successors (re-pose; reductions NOT proved here, obligations named)

**SUCCESSOR-A (chart-carrying descent — the route that can serve the census gate
at ALL scales).** The gate's object is chart-constrained (top-band full-petal
contributors), and the wave-4 chart-level K4 theorem (retained-zero -> CRT
touched-set injection -> tail collapse, audited "row-agnostic") bounds any
full-petal chart list by m+1 <= n on ANY row. Proposed lemma: for M | k and a
top-band full-petal G1 chart in the fiber-aligned layout (census layout pin:
petals are unions of full fibers), the intrinsic-scale-M subclass of the chart's
contributor list descends to the contributor list of a full-petal chart at the
quotient row with ell' = ell/M (petals -> points when ell = M), m' <= m,
d' <= d/M, and d' >= ell'(m'-2) (the top-band pin divides through by M); the
row-agnostic collapse then gives <= m'+1 <= n' PER CHART, and the atlas census
prices the aggregate — no word-uniform input anywhere. Obligations: (i) chart
K_M-compatibility from the layout pin; (ii) the descended chart word and degree
arithmetic (retained-zero factor behaves as L_R = fiber-locator^{r/M}); (iii) the
ell < M boundary. This is the reduction worth attempting next; it consumes only
PROVED machinery plus one new descent lemma about structured (chart) words.

**SUCCESSOR-B (fiber-starved word-uniform remnant — small scales only).** The
original statement restricted to (row, M, q) with
2 C(n', k'+1) <= q * min((63/64) n'^6, q - 3n')  [pigeonhole-safe regime].
Open, not refuted; candidate tool: e1 (and general t) fiber equidistribution
(second moment / Gauss sums; in-repo e1-fullness technology; the in-vivo
concentration at 0.02% supports it). Coverage ceiling: at q ~ 2^256 this can at
best serve n' <= 256 (rho = 1/2, 1/4) and n' <= 512 (rho = 1/8, 1/16); at
minimal official fields q = n^2 it serves n' = 64 only for s >= 16. NOT
sufficient for the gate alone — pair with SUCCESSOR-A.

**Gate re-surgery required.** petal_small_scale_staircase_census's conditional
close names "the successor falsified" as a re-surgery trigger; it fires now. The
per-scale supplier map's "n' >= 64 -> successor red" edge must be replaced by
SUCCESSOR-A (all scales) and/or SUCCESSOR-B (small scales, if proved). The
PROVED windows T1/T2/T3 and Lemma 0 stand unchanged. The
petal_k4_primitive_bound "one lemma serves both reds" convergence note must be
retracted: the row-level form is strictly stronger than the chart-level theorem
and is FALSE; the chart-level theorem stands.

## 7. Questions 1 and 2 (the task's two live routes) — answered

**Q1 (does the tail-collapse chain apply at the quotient row without an atlas
supply?): NO — and provably nothing can.** The chain's conclusion for general
words is false at n' >= 128 (minimal fields) resp. n' >= 512 (all prize fields),
so no hypothesis-check can rescue a general-word application. Concretely, the
chain degenerates without the chart: with no pinned retained set the factorization
gives d_eff = k'-1; with no petal partition, petals = points (ell = 1, m = n'),
and the CRT injection collapses to exactly T1's subset bound C(n', a) — while the
top-band pin d >= ell(m-2) reads k'-1 >= n'-2, false by the maximal margin at
every rate. The load-bearing chart hypotheses are the top-band pin and the
retained-zero constraint; the oversized field CANNOT substitute — the collapse is
field-free combinatorics, and the refutation shows the field would need
q >~ C(n',k'+1)/n'^6, exponential in n', far beyond the prize envelope for
n' >= 512.

**Q2 (does the moment-map fiber framing prove the single cell at the oversized
field?): It settles it — NEGATIVELY.** At a = k'+1 the framing is the t=1
truncated-locator map S -> e1(S); the complete list at degree-(k'+1) words IS the
fiber, exactly. The task-sketch's premise "first-moment counting says the
expected fiber is << 1 at q >= (Mn')^2" is arithmetically false in the claim's
regime: the expected fiber is C(n',k'+1)/q, which at q ~ n^2 = (Mn')^2 is
exponentially LARGE for n' >= 128 (fiber-rich; the starved/rich boundary is
q^{a-k'} ~ C(n',a), i.e. n' ~ 2s/H(rho) at minimal fields). Second-moment /
Cauchy-Schwarz can only prove fibers CONCENTRATE at that exponential mean
(observed: 0.02%), i.e. they upgrade the existential refutation to a uniform one.
The oversized field is genuine leverage only in the starved regime — that is
SUCCESSOR-B, and its ceiling (n' <= ~512 at prize fields) is now exactly priced.
