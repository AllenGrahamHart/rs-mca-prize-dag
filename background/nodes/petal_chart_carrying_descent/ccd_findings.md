# ccd_findings — falsification runner on petal_chart_carrying_descent (2026-07-13)

Worker: fresh-context FALSIFICATION RUNNER. Repos read-only; all scratch ccd_-prefixed.
Catch ledger continues from #127.

## TURN 1 — reading pass (verbatim)

Read: dag.json node `petal_chart_carrying_descent` (TARGET, key) + neighbors
(census gate, bridge, scale_reserve, G1, K4, descent, refuted sjb); the #124
refutation packet (sjb_refutation_statement/proof, sjb_findings); the
tail-collapse chain (petal_top_band_tail_collapse, petal_full_touched_set_injection,
petal_retained_zero_effective_degree — statement+proof each);
cyclic_fiber_interleaving_descent (statement+proof); the census machinery
(cg_petal_census.py, 372-cell results JSON, QUALITY certificate + layout pin);
G1 statement + conditional.md G4 dictionary + upstream v13
prop:capf-concrete-sunflower (the concrete chart: G_P = P/L_{Y\D0}, deg <= d = |D0|,
a = sigma + d + 1 - |R0|, retained-zero G_P|R0 = 0).

### The two obligations, operationalized

(i) descended member of a fiber-aligned chart member IS a chart member at the
quotient row (petals -> petals under X -> X^M);
(ii) the descended chart satisfies tail-collapse hypotheses: retained-zero
(|R0'| < ell' and G'|R0' = 0), P1 band d' >= ell'(m'-2), petals pairwise disjoint,
disjoint from D0' ∪ R0'; the collapse then gives <= m'+1 distinct classes/chart.

FALSIFIER: (1) a fiber-aligned chart at a scaled row whose scale-M subclass
descends to > m'+1 distinct classes; (2) a descended member escaping every
descended petal.

### Exact hypothesis list obligation (ii) must deliver at the descended chart
(from the proof files, verbatim mapping):

- H1 (retained-zero factorization, petal_retained_zero_effective_degree):
  R' and T' disjoint, |R0'| = r' <= d', every descended member G' vanishes on R0';
  gives G' = L_{R'} Q, deg Q <= d' - r'.
- H2 (touched-set injection, petal_full_touched_set_injection): m' pairwise
  disjoint petals of size ell', petals disjoint from D0' and R0'; full-petal
  membership (agreement all-or-nothing per petal); a' = ell' + d' - r';
  petal locators pairwise coprime (automatic for disjoint petals).
- H3 (tail collapse, petal_top_band_tail_collapse): ell' >= 1, m' >= 2,
  0 <= r' < ell'  [STRICT: r' < ell' is load-bearing — "strict retained-remainder
  bound" gives ell' + d' - r' >= ell'(m'-2) + 1], and the band d' >= ell'(m'-2).
  Then tail <= C(m',m'-1) + C(m',m') = m'+1.
- H4 (per-chart fixed data): D0', R0', petal list fixed per chart; members agree
  on ALL of (core'\D0') ∪ R0' and have NO agreements outside
  (core'\D0') ∪ R0' ∪ (chart petals). The m'+1 bound is per fixed chart.

NOTE r' < ell': at ell' = 1 (petal size ell = 2, M = 2: petals -> points) this
forces r' = 0 — the descended reading must absorb the retained point into the
descended CORE (core'' = Z' ∪ {y_nf}, size k') or the hypotheses fail verbatim.
Both readings will be tabulated.

## TURN 1 — structure derivation (to be machine-verified in stage 1)

Fiber-aligned layout at (n, k), k EVEN (required by M | k), sigma = 1, ell = 2:
core Z = nf = k/2 - 1 full antipodal fibers {j, j+n/2}, j = 0..nf-1, PLUS point
x_nf (exponent nf); background = {-x_nf} (exponent nf + n/2); petals = full
fibers j = nf+1 .. n/2-1? NO — census code: petal_fibers = range(nf+1, n/2) when
k-1 odd... CORRECTION from code read: petal_fibers = [nf + 1, ..., n/2 - 1]
wait: `petal_fibers = [j for j in range(nf + (1 if (k-1)%2 else 0), half)]` =
range(nf+1, n/2) for k even. So petals = fibers nf+1..n/2-1, count t = n/2 - nf - 1
= (n - k)/2. Hmm: split fiber = fiber nf. t = n/2 - (k/2-1) - 1 = (n-k)/2.
Word: U = 0 on Z ∪ background, U = c_i L_Z on petal fiber i.

KEY IDENTITY (derived): L_Z(X) = L_{Z'}(X^2) · (X - x_nf), where
Z' = {x_j^2 : core fibers} (k/2 - 1 = k'-1 points at the quotient row, k' = k/2).
Hence with U's M=2 Fourier components (u_0, u_1) [f(x) = f_0(x^2) + x f_1(x^2)]:
  u_1 = the quotient chart word: 0 on Z' ∪ {y_nf}, c_i L_{Z'}(y_i) on descended
        petal points y_i = x_i^2  (scalars descend UNCHANGED),
  u_0 = -x_nf · u_1     (components PROPORTIONAL),
  U(x) = (x - x_nf) · u_1(x^2) for ALL x in H  (the chart word itself factors).

CONSEQUENCES (each to be machine-checked):
- C1: any codeword f with 2-invariant agreement set S, |S| >= k+2, satisfies
  f_0 = -x_nf f_1, i.e., f = (X - x_nf) g(X^2), g = f_1 (common-support pair
  argument: distinct deg<k' polys agree <= k'-1 < k'+1 <= |S'| points).
- C2: for lifts f = (X - x_nf) g(X^2): agreement with U is fiberwise
  all-or-nothing EXCEPT the split fiber: x_nf ALWAYS agrees; -x_nf agrees iff
  g(y_nf) = 0. So c(S) >= 2 <=> g(y_nf) = 0 (retained-zero at the quotient row
  is EQUIVALENT to membership in the scale-2 subclass).
- C3: scale-2 subclass <-> {g : deg g < k', |agr(g, u_1)| >= k'+1, g(y_nf) = 0},
  S = union of fibers over S' = agr(g, u_1); distinct descended classes =
  distinct realized supports S' — the SAME chart-list object one row down.
- C4: chart data descends exactly: d = 2(k' - z) where z = |S' ∩ (Z' ∪ {y_nf})|
  (x_nf in S always), d' = k' - z = d/2; r = 1 (background -x_nf in S), r' = 0
  under the core''-absorbing reading; a = 2 + d - 1 = d+1, member needs
  p# >= ceil(a/2)... = d/2 + 1 = d' + 1 = a' = ell' + d' - r' = 1 + d' - 0 ✓;
  band d >= 2(m-2) <=> d' >= 1·(m-2) = ell'(m'-2) when m' = m ✓ (M = 2:
  distinct petal fibers -> distinct quotient points, NO merging).

W_tau-INSIDE-THE-CHART structural note (task 4, to be probed): the descended
word u_1 vanishes on k' points (Z' ∪ {y_nf}); W_tau = X^{k'}(X - tau) vanishes
nowhere on H^M except possibly tau. The refuting bijection needs (k'+1)-subsets
of the domain where the word is W_tau-shaped; only the n' - k' petal points are
scalar-adjustable. At rate 1/2: n' - k' = k' < k'+1 — the e1-fiber mass CANNOT
fit inside the adjustable region; every member must take >= z >= 1 roots on the
zero-core, coupling it to the CRT/chart structure. This is the structural
escape hatch — the numeric attack will try to defeat it with engineered scalars.

## PRE-REGISTERED EXPECTATIONS (before any run)

- E1: stage-1 structure identities (u_0 = -x_nf u_1; u_1 = quotient chart word;
  U = (X - x_nf) u_1(X^2)) PASS at all cells (derived above; failure = my
  derivation or a layout-convention misread — would NOT itself be a node kill).
- E2: obligation (i) at M=2: ZERO escapes; every scale->=2 member is full-petal
  and fiberwise all-or-nothing at the official row; f_0 = -x_nf f_1 exactly.
- E3: per-descended-chart distinct classes <= m'+1 at every top-band chart;
  saturation (= m'+1) possible at engineered scalars; NO excess. If an excess
  appears: independently re-verify with a second minimal script before any
  falsifier claim.
- E4: retained-zero descends automatically (g(y_nf) = 0 by C2); band descends
  exactly (C4); violations occur only OUTSIDE the top band (z >= 3 at rate 1/2),
  which is outside the node's scope but will be tabulated honestly.
- E5 (task 4): W_tau-matched scalars inflate the CROSS-chart total (many charts,
  each within budget) but NO single chart above m'+1. DEFERRED RISKY PART: none
  (all enumerations bounded; heaviest complete run pre-sized < C(16,9) ~ 1.1e4
  interpolations locally, (64,*) via structured per-chart census, Modal for the
  fiber-subset completeness cross-checks).
- E6 (M=4, ell < M boundary): scale-4 members rare; at rate 1/2 the M=4
  descended images of core-fibers and petal-fibers OVERLAP (4-fibers mix core
  and petal 2-fibers) — the "petals -> petals" clause is expected to DEGENERATE
  here. This is SUCCESSOR-A's own named obligation (iii); a clean numeric
  exhibit of the degeneration is a finding (obstruction), not automatically a
  falsifier — the node's falsifier clauses will be applied verbatim.

## TURN 2 — stage 1 + stage 2 EXECUTED (all local ramguard tiny, < 8 s each)

STAGE 1 (ccd_struct_check.py): 55 cells [(16,8)x4 primes, (32,12)x4, (32,16)x3;
5 scalar modes each] — ALL PASS. The M=2 structure theorem is now in-vivo
verified: I1 L_Z(X) = L_{Z'}(X^2)(X - x_nf); I2 u_0 = -x_nf u_1;
I3 u_1 = the quotient chart word (0 on Z' u {y_nf}, c_i L_{Z'} on petal images,
scalars UNCHANGED); I4 U(x) = (x - x_nf) u_1(x^2) on ALL of H; I5 fiberwise
descent semantics; I6 lift semantics (x_nf always agrees; -x_nf agrees iff
g(y_nf) = 0).

STAGE 2 (ccd_stage2.py): 66 cells [(16,8) 28 cells incl. FULL BRUTE cross-check
C(16,9) per cell; (32,16) 15; (32,12) 15; (32,8) 8; modes incl. adversarial
wtau0/wtauy = scalars matched to W_tau on the petal region at the quotient row].
COMPLETE periodic enumeration (census-proved fiber-subset method).
Totals: 1221 scale-2 members, 0 scale-4, 0 scale-8. ZERO violations on every
counter: escapes (falsifier clause 2) = 0; CRT (W,I') collisions = 0; per-chart
cap violations = 0; C1 (f_0 = -x_nf f_1) fails = 0; C2 (retained-zero <->
scale-2 membership) fails = 0; full-petal fails = 0; petals->petals pattern
fails = 0; d/r arithmetic (d = 2(k'-z), r = 1, a = d+1) fails = 0; official/
quotient band-equivalence fails = 0; brute mismatches = 0.

### PROVED EN ROUTE (clean arguments, machine-confirmed on all members)

- P1 (lift form): every contributor with 2-invariant S, |S| >= k+2 satisfies
  f = (X - x_nf) g(X^2), g = f_1: on S' (|S'| >= k'+1), f_0 + x_nf f_1 agrees
  with u_0 + x_nf u_1 = 0, i.e. vanishes at > k'-1 points, hence f_0 = -x_nf f_1.
  With I6 this gives: scale->=2 subclass <-> {g : deg g < k',
  |agr(g,u_1)| >= k'+1, g(y_nf) = 0}; S = fibers over S' = agr(g,u_1);
  agreement automatically fiberwise all-or-nothing; distinct descended classes
  = distinct realized S' — the SAME chart-list object one row down.
- P2 (image-descent/retained factor): the official chart image
  G_P = f/L_{Z cap S} descends as G_P(X) = Q(X^2) with Q = g/L_{W\{y_nf}} =
  (Y - y_nf)·G', G' = g/L_W the descended chart image — the retained-zero
  factor behaves exactly as SUCCESSOR-A's obligation (ii) wording predicts
  (fiber-locator^{r/M} = the single linear factor (Y - y_nf)).
- P3 (UNIQUENESS — the m'+1 line is slack at ell' = 1): in ANY band chart at
  the descended row (fixed W, petal-list P, |P| = m' <= d'+2), two distinct
  members g_1 != g_2 (g_i = L_W h_i, deg h_i <= d'-1) have
  |I'_1 cap I'_2| >= 2(m'-1) - m' = m'-2 and m'-2 >= d'-... at m' = d'+2:
  intersection >= d' > d'-1 = deg h => h_1 = h_2; at m' = d'+1 the only config
  is I' = P; at m' <= d' no member fits (a' = d'+1 > m'). Hence AT MOST ONE
  member per band chart — m'+1 is an overcount by a factor m'+1. The stage-2
  tables confirm: advmax_in_band_chart = 1 in EVERY chart of EVERY cell (the
  W_tau-matched adversarial scalars included). CATCH #128 (positive-direction):
  SUCCESSOR-A's per-chart line can be strengthened from m'+1 to 1 at ell' = 1
  band charts; the m'+1 form is safe with maximal slack.

### The r' < ell' pin (obligation (ii) exact bookkeeping)

At ell' = 1 the tail-collapse strict hypothesis r' < ell' forces r' = 0: the
descended chart MUST be posed with core'' = Z' u {y_nf} (|core''| = k', one
larger than the (n',k')-canonical E22 core k'-1; legal verbatim under
def:capf-sunflower-layer with sigma' = 0: a' = sigma' + d' + 1 - r' = d'+1,
exactly matching the member threshold |I'| >= k'+1-z = d'+1). Under the
alternative reading (y_nf retained, r' = 1 = ell') the strict hypothesis FAILS
verbatim — the successor proof must fix reading A. The retained-zero constraint
itself descends AUTOMATICALLY: g(y_nf) = 0 is EQUIVALENT to scale-2 membership
(C2/I6) — at the descended chart it is absorbed as the core'' point y_nf.

### wtau adversarial note (task 4 first pass)

At rate 1/2 the W_tau mass cannot enter any chart at all (petal region
n'-k' = k' < k'+1 points; every member needs z >= 1 core roots, and the e1
bijection breaks on the zero set). At rate < 1/2 ((32,12): 10 petals >= 7)
wtauy-matched scalars DO realize W_tau-type members (g = W_tau - L_S,
S ni y_nf, tau = y_nf) — visibly boosting members-per-W (up to 4 per W at
p=97) — but every band chart still holds exactly 1 member (P3); the mass
spreads across charts, each paid separately by the atlas. The chart-carried
route genuinely escapes the #124 mechanism AT M = 2 = ell.

## TURN 3 — stage 3: n = 64, two independent methods, W_tau-inside attack, M=4 plant

- MUTATION CONTROL (cfg census): the config-census (complete enumeration of the
  scale->=2 subclass via the PROVED lift reduction P1, looping (z, W, defining
  petal subsets)) reproduces the stage-2 fiber-subset census EXACTLY at
  (32,16,97,geom5): 63 = 63, same members. At (64,8): fiber-complete vs
  cfg-complete MATCH EXACTLY at p=193 (140/147/140 members, 3 modes) and p=257
  (109/123/119). Two structurally independent complete enumerations agree.
- BATTERY MUTATION CONTROL (ccd_mutation_control.py): three deliberate
  mutations (corrupted u1 petal value; wrong split point in the lift; injected
  fake member) each TRIP the battery (38/67/1 violations). The zero-violation
  production runs are live measurements, not vacuous.
- unique2: 50/50 deliberate attempts to place TWO distinct members in one
  max-band descended chart are forced h2 == h1 (P3 numerically confirmed).

### VOLUMES (complete censuses; ALL obligation counters zero everywhere)

| cell | members (scale>=2 subclass) | charts (W-groups) | max members per band chart | scale-4 |
|---|---|---|---|---|
| (16,8) x 4 primes x 7 modes | 13 total | - | 1 | 0 |
| (32,8/12/16) x primes x modes (38 cells) | 1208 total | - | 1 | 0 |
| (64,8,193/257) x 3 modes | 109..147 per cell | 5-7 | 1 | 0 |
| (64,16,193,geom5) COMPLETE z<=7 | 36,646 | 124 | 1 | 1 (natural) |
| (64,16,193,wtauy) COMPLETE z<=7 | 37,125 | 126 | 1 | 0 |
| (64,16,449,geom5) z=1 seeds | 6,731 | 25 | 1 | 0 |
| (64,32,193) z<=3, 4 modes | 1300-1361 per cell | 482-506 | 1 | 0 |
| (64,32,449) z<=3, 2 modes | 531/600 | 346/367 | 1 | 0 |

- First-moment law CONFIRMED in the chart-carried setting: (64,16) z-stratum
  counts match C(15..,z-1) C(24,17-z-...)/q predictions (z=1: 3426 obs vs 3810
  pred at p=193; (64,32) z=4: 1254 obs vs 1320 pred). The fiber-rich mass of
  the #124 refutation IS present inside chart words (36k+ members per U at
  n=64, rho=1/4) — but it is carried ENTIRELY by chart multiplicity (many
  charts, ONE member each), never by per-chart lists. The chart-carried route
  escapes the #124 mechanism exactly as SUCCESSOR-A hoped, and the escape is
  now measured, not just argued.
- W_tau-INSIDE-THE-CHART attack (task 4): at rate 1/2 blocked structurally
  (petal region k' < k'+1; wtau modes give NO gain: 1300 vs 1324 members). At
  rate 1/4 the attack "succeeds" at inflating the per-U total by only ~1.3%
  (37,125 vs 36,646) because the generic fiber-rich mass already dominates;
  per-chart max stays 1. FALSIFIER CLAUSE 1: NEVER FIRED (any reading:
  per-(W,T) chart <= 1 <= m'+1; per-U totals are large but that is chart
  multiplicity, priced by |A_U|, and the profile budget 719 x Q_2(A) has >=
  five orders of magnitude headroom at every measured cell: e.g. 36,646 vs
  719 x C(31,9) ~ 1.45e10 at the (M,A) = (2,18) cell).

### M = 4 (ell < M) BOUNDARY — the plant (E6 executed)

Engineered scale-4 members (c(S) = 4 exactly, top-band eligible) planted via
quotient-row 2-invariant supports at (32,16,97), (32,16,193), (64,32,193):
- Descent SEMANTICS at M=4: perfect (S'' = S mod n/4, |S''| = |S|/4,
  componentwise agreement exact).
- FALSIFIER CLAUSE 2 (descended member escaping every descended petal): does
  NOT fire — S'' always meets descended petal images (at rate 1/2 the petal
  images cover ALL of Z_{n/4}).
- BUT the "chart structure descends" mechanism is DEAD at M=4, rate 1/2: the
  descended petal-point images COINCIDE with descended core images (overlap =
  16/16 at (64,32); every 4-fiber mixes one core 2-fiber with one petal
  2-fiber); the M=4 vector word has NO joint zero set (joint_zero_pts = 0,
  chart form would need ~k/4) and components are NOT proportional. At rate 1/4
  ((64,16)): 8 petal-petal merges (merged petal groups), consistency FORCED by
  periodicity (0 inconsistent), core/petal overlap 8 of 16.
- Route out (reduction, not new proof): scale-M subclasses for ALL dyadic
  M >= 2 are K_2-invariant, hence contained in the M = 2 descent's domain; the
  M = 2 descended charts price them (the planted scale-4 member appears in the
  M=2 census within caps, S' 2-invariant). Counting classes at M = 2 descent
  upper-bounds every scale-2^j subclass simultaneously (S <-> S' bijective).
  The node's per-M clause for M > 2 is MOOT for the gate's arithmetic if
  re-posed through the M = 2 descent; as literally stated ("petals -> petals
  under X -> X^M" for all 2 <= M <= t) it is REFUTED-AS-MECHANISM at M > ell
  by the planted exhibits (obstruction documented; pre-registered falsifier
  clauses themselves do NOT fire).

## TURN 4 — final Modal shard + verdict

(64,32,193) z=4 stratum complete (Modal, 828k candidates/cell): geom5 13,224
members / wtauy 13,469, across ~1930 charts, max 1 member per band chart,
0 cap violations, 0 obligation violations. z=5-stratum first-moment check:
observed 11,830 vs predicted C(15,4)C(16,12)/193 = 12,872 (within 8%).

# ================= VERDICT =================

## OUTCOME, OBLIGATION (i): HOLDS at M = 2 (= ell) — proof-grade + exhaustive.

Machine-verified on ~100k members across 80+ cells (n = 16/32/64, all four row
rates, 2-4 primes per row, 7 scalar modes incl. W_tau-matched adversarial and
planted words): the descended object of EVERY scale->=2 fiber-aligned chart
member IS a chart member at the quotient row. Zero escapes (falsifier clause
2: never fired). The mechanism is now explicit and general (proof-ready):
U = (X - x_nf) u_1(X^2), members = lifts (X - x_nf)g(X^2), petals -> petal
points, scalars unchanged, full-petal pattern preserved (P1/I1-I6/C1-C4).
At M > ell (M = 4): the claimed mechanism "petals -> petals under X -> X^M"
is REFUTED-AS-MECHANISM by planted top-band scale-4 exhibits (core/petal
images coincide; no joint zero set; components non-proportional) — but
NEITHER pre-registered falsifier clause fires (escapes are impossible because
petal images cover Z_{n/M}; class counts tiny). Fix available by reduction:
scale-M supports are K_2-invariant, so the M=2 descent prices ALL dyadic
scales simultaneously; the node should be re-posed accordingly.

## OUTCOME, OBLIGATION (ii): HOLDS at M = 2 under the forced bookkeeping.

The descended chart satisfies every tail-collapse hypothesis PROVIDED the
descended core is taken as core'' = Z' u {y_nf} (size k', sigma' = 0, r' = 0);
then a' = d'+1 exactly matches the member threshold, the retained-zero
constraint descends AUTOMATICALLY (g(y_nf) = 0 is equivalent to scale->=2
membership), the retained factor behaves as (Y - y_nf) (P2), and the top-band
pin descends exactly (d = 2d', official band <=> quotient band, same m).
Under the naive reading (y_nf retained, r' = 1 = ell') the STRICT r' < ell'
hypothesis of petal_top_band_tail_collapse FAILS verbatim — the successor
proof must fix reading A. Exact per-chart tables for all 66 small cells in
ccd_out_n16/n32a/n32b/n32c.txt; per-cell summaries for n = 64 in turn-3/4 logs.

## OUTCOME, COLLAPSE COUNT (falsifier clause 1): NEVER FIRED, with room to spare.

Per descended band chart the distinct-class count is <= m'+1 in every one of
the ~5,000 realized charts measured — in fact it is <= 1 (P3 uniqueness,
proved generally: two distinct members of one band chart share >= d' petal
agreements > deg h = d'-1, forcing equality; confirmed by unique2 50/50 and by
max_members_per_band_chart = 1 universally, including under attack scalars).
The per-U totals ARE huge in the fiber-rich regime (36,646 members per word at
(64,16,193) — first-moment law confirmed inside chart words) but the mass is
100% chart multiplicity, priced by |A_U|, never per-chart lists.

## CATCHES #128-#132

- #128 (P3 uniqueness — positive slack): at ell' = 1, every band chart at the
  quotient row holds AT MOST ONE member; the node's m'+1 per-chart line is
  safe by a factor m'+1. General proof, two lines, consumes only the band pin
  and the degree count.
- #129 (r' < ell' landmine): the tail-collapse strict remainder hypothesis
  forces the descended chart to absorb y_nf into the CORE (core'' size k', not
  the (n',k')-canonical k'-1; sigma' = 0, r' = 0). Reading B (y_nf retained)
  violates the proved theorem's hypothesis verbatim. Any successor draft that
  copies the official-row bookkeeping (r = 1) will consume a false premise.
- #130 (M > ell mechanism dead): direct X -> X^M descent at M = 4 destroys
  chart structure for fiber-aligned charts (planted top-band scale-4 exhibits
  at (32,16) x 2 primes and (64,32,193), machine-verified end-to-end); the
  pre-registered falsifier clauses are structurally unable to fire there
  (petal images cover everything) — the clauses are too weak to see this
  degeneration, which is why it must be recorded as an obstruction, not a
  kill. Re-pose M > 2 through the M = 2 descent (scale-M classes are
  K_2-invariant; S <-> S' bijective).
- #131 (fiber-rich mass inside charts, harmless per-chart): complete censuses
  at (64,16): 36,646/37,125 members per received word; z-strata match the
  supply-law first moment within 10%; W_tau-matched scalars gain only ~1-2%
  (rate 1/4) and NOTHING at rate 1/2 (petal region k' < k'+1 blocks the e1
  bijection). Every member occupies its own chart (P3). Honest cost transfer:
  G1's atlas exhaustiveness must supply ~4e4 charts per word at n = 64
  rho = 1/4 (|A_U| >= member count; the (121/128)n^6 weighted budget still has
  ~6 orders of headroom there, and the census-gate profile line 719 x Q_M(A)
  has >= 5 orders at every measured cell).
- #132 (the enabling structure theorem): fiber-aligned chart words factor
  U(X) = (X - x_nf) u_1(X^2) with L_Z(X) = L_{Z'}(X^2)(X - x_nf) and u_1 the
  quotient chart word with UNCHANGED scalars; scale->=2 contributors = lifts
  (X - x_nf)g(X^2) with g(y_nf) = 0 <=> membership; chart data descends d =
  2d', a = d+1 -> a' = d'+1, band <=> band. This is obligations (i)+(ii) at
  M = 2 in proof-ready form (verified at 55 + 66 + all n=64 cells).

## HONEST SCOPE — what the small-row evidence does and does not cover

COVERED (and proof-general): the structure theorem, lift form, retained-zero
equivalence, band/threshold arithmetic, and P3 per-chart uniqueness are
parameter-free arguments (any n, even k, fiber-aligned layout, M = 2, any
prime q with n | q-1); the enumerations verify their in-vivo semantics at
n <= 64 with two independent complete methods + brute + mutation controls.
NOT covered:
1. G1 itself (atlas existence/exhaustiveness/weighted budget) — everything
   here is conditional on charts being supplied; the volumes quantify how big
   the atlas must be.
2. n >= 128 rows — no enumeration (but no cap depends on n; only realized
   VOLUMES were measured, and those are first-moment predictable).
3. (64,32): complete only for the z <= 3 and z = 4 strata (P3 still caps all
   unenumerated strata; clause 1 cannot fire anywhere by proof).
4. M > ell = 2: the node as literally stated is wrong-in-mechanism (see #130);
   the M=2-routing re-pose is sketched, not yet a proved node.
5. sigma > 1 charts (petal size > 2): untested (census machinery is sigma=1;
   the structure theorem's proof shape extends but was not verified).
6. k odd: excluded by M | k — no gap (descent undefined there).

## ARTIFACTS (all ccd_-prefixed, scratchpad)

- ccd_struct_check.py (stage 1, 55 cells, ALL PASS)
- ccd_stage2.py + ccd_out_n16/n32a/n32b/n32c.txt (66 cells, complete
  enumerations, per-chart tables, 0 violations)
- ccd_stage3.py (config census via proved lift reduction; fib64k8 dual-method
  match; plant4; unique2; cfg shards) + Modal logs (tasks/bhxhipk6p,
  bvyz3dti6, bvbzytu27)
- ccd_mutation_control.py (battery liveness: 3/3 mutations trip)
- ccd_findings.md (this file)
