# cspa_findings — fresh-context PACKET AUDITOR for csp_* (petal_chart_carrying_descent)
# 2026-07-13. Catch ledger continues from #135.

## TURN 1 — reading pass

Read (verbatim): csp_statement.md, csp_proof.md, csp_verify.py, csp_claim_contract.md,
csp_findings.md, csp_verify_out.txt, ccd_findings.md (search ledger);
dag.json nodes petal_chart_carrying_descent (SUCCESSOR-A, pins #128-#135 present),
petal_small_scale_staircase_census, quotient_row_subjohnson_bound (#124 REFUTED);
critical/nodes/{petal_top_band_tail_collapse, petal_full_touched_set_injection,
petal_retained_zero_effective_degree}/statement.md (+ tail-collapse proof.md).

Key upstream hypothesis texts (for verbatim-consumption check):
- petal_top_band_tail_collapse: ell>=1, m>=2, 0<=r<ell (STRICT), d>=ell(m-2)
  => tail sum_{t=ceil((ell+d-r)/ell)}^m C(m,t) <= m+1. Proof uses r<=ell-1.
- petal_full_touched_set_injection: a=ell+d-r; G|R=0; full-petal all-or-nothing;
  m pairwise disjoint petals size ell; injection to touched sets; bound sum_{t>=ceil(a/ell)} C(m,t).
- petal_retained_zero_effective_degree: R,T disjoint, |R|=r<=d, G|R=0 =>
  bijection to deg<=d-r list vs W/L_R; supports+stabilizers unchanged.

## Audit plan
1. Hand re-derive S1-S6, U0-U2, L0, C (independent algebra).
2. Hunt list: (a) #133 scalar normalization use-sites; (b) U0-U2 degree bookkeeping
   under reading A + margin-1 + M3 genuineness; (c) S5 no-merging m'=m; (d) #135 band
   arithmetic {k+2,k+4}; (e) replay csp_verify.py + fresh cell + >=2 own mutations;
   (f) composition C consumption audit vs #124 word-uniform ghost.
3. All runs via tools/ramguard tiny (or modal). Expectations pre-registered before runs.

## TURN 2 — hand re-derivation (every step of csp_proof.md independently re-derived)

L1 ✓ (root count). L2 ✓: k even forces deg f_0, f_1 <= k'-1 (2i <= k-2, 2i+1 <= k-1);
fiber matrix [[1,x],[1,-x]] det -2x != 0 needs q odd (2|n|q-1 ✓) and x != 0 ✓.

S1 ✓: (X-x_j)(X+x_j) = X^2 - y_j; product over j<nf x (X - x_nf); degrees 2nf+1 = k-1 ✓.
S2 ✓: pointwise check re-done on all four point types (core fiber / x_nf / -x_nf /
petal ±x_i, noting (±x_i)^2 = y_i both). Vector word: unique fiberwise solution is
u_0 = -x_nf·u1, u_1 = u1 ✓. Word-presentation reading of u1 against
def:capf-concrete-sunflower (v13 tex 6282-6300 read verbatim): |Y'| = |Z'| = k'-1 ✓
(def requires |Y| = k-1 at row k'), R0' = {y_nf}, T'_i = {y_i} size 1 = sigma'+1,
P'_star = 0, labels c_i vs L_{Y'} = L_{Z'} ✓ EXACT.
#133 pin algebra re-derived: L_{core''} = L_{Z'}(Y-y_nf) = L_W L_{D0'} =>
L_{Z'}(y_i)/L_W(y_i) = L_{D0'}(y_i)/(y_i - y_nf); aux labels c_i/(y_i - y_nf) ✓.
USE-SITE AUDIT (hunt a): the packet USES "same scalars" only in the WORD presentation:
(i) S2 itself; (ii) residual R1 ("u1 is a concrete sunflower chart word" => G1's
quotient-closed clause) — a word-presentation fact ✓; (iii) U1's word on P is
pointwise v = u1|_P — normalization-free ✓; (iv) the tail-collapse chain consumes
label VALUES nowhere (injection needs only pairwise-coprime locators + any labels) ✓;
(v) verifier M3 builds v = u1/L_W — consistent with the aux normalization for that W ✓.
No site consumes word-form scalars in aux normalization. #133 honored everywhere.

S4 ✓: f(x)-U(x) = (x-x_nf)[g(x^2)-u1(x^2)]; factor nonzero off x_nf; -2x_nf != 0;
all-or-nothing off split fiber; formula ✓. Parity: aperiodic lifts (g(y_nf) != 0)
have |S| = 2|agr|+1 ODD; periodic lifts |S| = 2|S'| EVEN (K_2-invariant sets have
no fixed points: x = -x impossible for x != 0, q odd) — the #135 parity engine ✓.
c(S)>=2 <=> g(y_nf)=0 needs L0 for the reverse direction — supplied ✓.
Threshold: |S| >= k+1 & even & k even => |S| >= k+2 <=> |S'| >= k'+1 — no off-by-one ✓.
Bijection ✓ (f -> g well-defined injective by L2 uniqueness; surjectivity: lift of any
qualifying g has |S| = 2|S'| >= k+2; supports mutually inverse via L1).

S3 ✓: K_2-invariance (L0) => both fiber points agree for y in S_0 => f_0(y) = u_0(y),
f_1(y) = u1(y) (L2) => (f_0 + x_nf f_1) vanishes on |S_0| >= k'+1 > k'-1 = deg => 0.
Slack is one root (|S_0| = k'+1 vs deg k'-1: 2 spare) — argument survives the minimum ✓.

S5 ✓ all seven bullets re-derived:
- y_nf in W always; |S n Z| = 2z-1; D0 = pi^{-1}(D0'), D0' <= Z', d = 2d' ✓.
- r = 1 -> r' = 0 (reading A) ✓.
- a = sigma+d+1-r = d+1 (sigma=1, r=1); a' = d'+1; ceil((2d'+1)/2) = d'+1 ✓ exact.
- NO-MERGING (hunt c): at M = 2, fiber index j -> point y_j = g^{2j}, i.e. the
  IDENTITY on indices 0..n'-1 (2j mod n distinct <=> j mod n' distinct). Petal
  indices nf+1..n'-1 and core'' indices 0..nf are disjoint subsets of [0, n'-1]:
  petal points pairwise distinct AND never land in core''. m' = m holds for ANY
  chart petal count, not just full t. SOUND. (Contrast M = 4 where 4-fibers mix
  core and petal 2-fibers — exactly the #130 refuted mechanism, scoped out.)
- band d >= 2(m-2) <=> d' >= m'-2 exact at m' = m ✓; per-member reading:
  d' >= m'-2 <=> |S'| <= k'+2 <=> |S| <= k+4 ✓ (m = |I'| = |S'|-z).
- #135 (hunt d): |S| even + |S| >= k+2 + top band <=> |S| <= k+4 => allowed sizes
  EXACTLY {k+2, k+4}, both even since k even ✓. Odd-|S| supports automatically
  aperiodic ✓ (parity engine above).
- image: L_{ZnS} = L_{W\{y_nf}}(X^2)(X-x_nf) (S1 computation on the subset,
  x_nf in S always) ✓; g vanishes on W (core fibers in S + u1 = 0 there; g(y_nf)=0)
  => L_W | g; Q = (Y-y_nf)G', deg G' <= (k'-1) - z = d'-1 ✓ — #134's one degree,
  bought by reading A (core'' size k' vs generic k'-1), spent by U0/U1.

S6 ✓ hypothesis-by-hypothesis against the three PROVED upstream statements
(read verbatim from critical/nodes/*/statement.md + proof.md):
- H1 retained-zero (petal_retained_zero_effective_degree): needs R,T disjoint,
  r <= d, G|R = 0. r' = 0, R' = empty: vacuous, bijection = identity ✓.
- H2 injection (petal_full_touched_set_injection): a = ell+d-r -> a' = 1+d'-0 = d'+1 ✓
  matches member threshold |I'| >= d'+1; m' singleton petals pairwise disjoint,
  disjoint from core'' >= D0' ✓; full-petal trivial at singletons ✓; locators
  (Y-y_i) distinct monic linear pairwise coprime ✓; CRT degree |I'| >= d'+1 >
  d' = d_eff >= deg G' ✓ (images deg <= d'-1 <= d' inject as a sublist — safe).
- H3 tail collapse (petal_top_band_tail_collapse): ell' = 1 >= 1 ✓; m' >= 2 by
  chart hypothesis ✓; 0 <= r' = 0 < 1 = ell' STRICT ✓ VERBATIM (upstream text:
  "canonical retained remainder size 0<=r<ell"); band d' >= ell'(m'-2) ✓.
  Reading B (r' = 1 = ell') violates the strict inequality verbatim — packet's
  refusal of reading B is correct, not cosmetic.
- H4 per-chart fixed data ✓ (chart membership = exact W + I' <= P).
- The "m+1 <= n" clause of the upstream statement (needs official core k-1) is
  NOT consumed — packet stops at <= m'+1 and Claim 2 sharpens to 1 ✓.

U0 ✓ re-derived incl. the D < |W| degenerate branch (g = 0 forced, unique trivially)
and the nonemptiness of I_1 n I_2 (>= 2A - |P| > D - |W| >= 0). Inclusion-exclusion ✓.
U1 ✓ (hunt b): D = k'-1 (codeword — the code supplies it, NOT the chart), |W| = z,
A = d'+1 from |agr| >= k'+1 & agr n core'' = W exactly & agr\core'' <= P;
2A - m' >= 2(d'+1)-(d'+2) = d' > d'-1 = D - |W|. Margin = 1 exactly at m' = d'+2;
larger below. Relaxations each admit 2 members: D = k' (deg-d' images) => d' > d'
FALSE; A = d' (reading B loses one agreement) => d'-2 > d'-1 FALSE; m' = d'+3 =>
d'-1 > d'-1 FALSE. M3's construction (interpolate through J u {q1} / J u {q2},
|J| = d') is genuine: h_i deg exactly d' (checked), g_i = L_W h_i deg exactly k'
(NOT a codeword — pseudo-member at the relaxed degree), both >= d'+1 agreements ✓.
U2 ✓: z = k' => g = 0 forced, agr(0,u1) = Z' u {y_nf} size k' < k'+1 (u1 != 0 at
petal points: c_i != 0, L_{Z'}(y_i) != 0 since y_i notin Z') => empty ✓;
m' <= d' empty ✓; m' = d'+1 forces I' = P ✓.

L0 ✓: Stab_H(S) <= H cyclic of order 2^s; nontrivial subgroup is cyclic of order
2^j, j >= 1, contains an element of order 2; unique such in F_q^* is -1 = g^{n/2},
lies in H ✓. So K_2 <= Stab, S K_2-invariant ✓.

C ✓ step-by-step; CONSUMPTION LIST (hunt f), exhaustive:
1. L0 (K_2-invariance) — proved in-packet.
2. S3/S4 bijection incl. |S| <= k+4 <=> |S'| <= k'+2 (Claim 1; itself consumes
   L1, L2, S1, S2 only).
3. The coverage hypothesis (A' = per-word band-chart atlas at the quotient row,
   G1's open content) — the ONLY unproved input.
4. U1 (Claim 2) + L1 for classes<->members and injectivity of S' -> chart.
NOT consumed by C: the tail-collapse chain (only S6's m'+1 safety line consumes
it — C uses Claim 2's <= 1 instead); sigma > 1; odd k; any word-uniform list
bound; any aperiodic-class bound. Nothing silently needed beyond Section 0's
fiber-aligned chart-word form (which IS the hypothesis of Claims 1-2).
Coverage is satisfiable in principle: for any top-band S', the minimal chart
(W = S' n core'', P = I') IS a band chart (m' = |S'|-z <= k'+2-z = d'+2 ✓);
existence-within-G1's-budget is the honest residual ✓.
#124 GHOST CHECK: the refuted node bounds APERIODIC exact-agreement lists per
word by a word-UNIFORM cap (63/128)n'^6; the packet (i) counts only c(S) >= 2
classes at the OFFICIAL row, (ii) bounds them by |A'| — a per-word atlas
cardinality, not a uniform cap, (iii) makes no claim about aperiodic classes
(residual R4 sends them to K4). The descended S' are generically aperiodic at
the quotient row, and the packet's U1 handles them by pure degree algebra with
no periodicity or word-uniform input — exactly the chart-carried escape that
#124 left open. NO secret implication of the refuted form. Note (recorded, not
a flaw): Claims 1+2 alone DO imply a word-uniform bound on the PERIODIC
top-band subclass (each class is the unique member of its minimal chart, so
count <= #{(W,I') pairs}) — this is fine: #124's refutation concerns aperiodic
lists; the planted W_tau family is 100% aperiodic (odd |S'|) and invisible to
the periodic count.

Scope edge cases checked: k = 2 (nf = 0, Z = {1}, Z' = empty, L_{Z'} = 1 — all
claims degenerate correctly); k = n-2 (t = 1: S6 vacuous at m' >= 2, U0/U1 still
cover m' = 1, C unaffected) ✓. Prime powers: all arguments are F_q polynomial
algebra, no primality consumed (verifier exercises primes only — contract says so
honestly) ✓.

VERDICT AFTER HAND AUDIT: no algebraic, quantifier, or normalization drift found
in any of L0/L1/L2/S1-S6/U0-U2/C. Statement <-> proof <-> contract quantifiers
agree. Upstream hypotheses consumed verbatim (strict r' < ell' honored via
reading A; reading B correctly refused).

## TURN 3 — verifier code review (csp_verify.py, line-by-line)

- order_n_domain: order-exactness test g0^{n/2} != 1 is valid BECAUSE n = 2^s
  (ord | n and ord does not divide n/2 => ord = n). In-scope correct.
- official_census completeness ✓: K_2-invariant S, |S| >= k+2 => contains
  >= k'+1 full fibers; interpolation through k of the 2(k'+1) points recovers
  the member; dedupe by poly. Independent method 1.
- quotient_census completeness ✓: any |S'| >= k'+1 support contains a
  (k'+1)-subset; y_nf in Sq filter = g(y_nf) = 0 (u1(y_nf) = 0). Method 2.
- battery: BIJECTION compares dicts (codeword -> support) of method 1 vs
  lifted method 2 — checks BOTH directions of S3/S4 ✓. D_ARITH/YNF/A_THRESH/
  FULL_PETAL/PATTERN/LW_DIVIDES/DEG_H/IMAGE_FACTOR = exactly S5's bullets ✓.
  P3 operationalization: two same-W members with |I1 u I2| <= d'+2 <=> exists
  a common band chart => fail — correct falsifier-(c) encoding ✓.
  (Minor: BAND_EQUIV is mathematically tautological given D_ARITH — harmless.)
  stab_order: checks generator shift n/M per dyadic M — subgroup nesting makes
  this exact ✓.
- M1/M2/M4 reviewed ✓ live. M3 reviewed: constructs h1 != h2 of degree EXACTLY
  d' (skips accidental true members), g_i = L_W h_i of degree exactly k'
  (pseudo-members outside the code), both >= d'+1 agreements in a |P| = d'+2
  chart — genuine sharpness exhibit for #134 ✓. (Minor: the final
  len(I1|I2) <= dq+2 condition is trivially true since I_i <= P; the load is
  carried by h1 != h2 + agreement counts — still a genuine construct.)

## TURN 4 — PRE-REGISTERED EXPECTATIONS before any run

- R0 (replay): csp_verify.py exits 0, ALL PASS, member counts identical to
  csp_verify_out.txt (332 total; 4/4 mutations trip).
- R1 (fresh cells, never touched by packet or search: row shapes (16,12),
  (16,4), (32,24) + fresh primes 241, 113, 641, and (32,16,577,rand2) fresh
  prime+mode): structure PASS, dual censuses MATCH, battery 0 violations,
  max 1 member per band chart, every scale->=2 member has EVEN |S|, and
  band <=> |S| in {k+2, k+4}. Member counts themselves are unpinned
  (recorded as new measurements).
- R2 (mutation MA, my design — normalization drift #133): building u1 with
  the AUXILIARY labels c_i/(y_i - y_nf) instead of c_i must (i) break the S2
  pointwise factorization U = (X - x_nf)u1_aux(X^2) at petal points, and
  (ii) break the official<->quotient census bijection. MUST TRIP at every
  tested cell; a non-trip would falsify the #133 pin's materiality.
- R3 (mutation MB, my design — aperiodic complement): quotient contributors
  with y_nf NOT in agr (the S4 else-branch, never enumerated by the packet's
  verifier) must lift to official contributors with ODD |S| = 2|agr|+1,
  c(S) = 1, x_nf in S, -x_nf notin S — zero exceptions. This live-tests the
  aperiodic branch of S4 + the #135 parity engine on real censuses.
- R4 (mutation MC, my design — bijection liveness): deleting one member from
  the official census dict must make battery report BIJECTION. MUST TRIP.
- Any deviation: STOP, re-verify with a second minimal script before any
  claim against the packet (could be my harness).
- Cost pre-size: all cells <= C(16,13)=560 or C(16,9)=11440 interpolations —
  ramguard tiny sufficient; no Modal needed.

## TURN 5 — RUN RESULTS (all under tools/ramguard tiny; scripts cspa_*)

R0 REPLAY: csp_verify.py exit 0; output IDENTICAL to banked csp_verify_out.txt
(15 A-cells, 13 B-cells, 332 members, all 9 pins match, 4/4 mutations trip).

R1 FRESH CELLS (cspa_fresh_check.py; two row shapes + three primes + one mode
never touched by packet or search):
- (16,12,241,consec): struct PASS, battery 0 fails, 1 member (|S| = 14 = k+2),
  1 chart, max 1/chart. POPULATED fresh shape+prime.
- (16, 4,113,geom3):  struct PASS, battery 0 fails, 0 members (vacuous census).
- (32,24,641,geom5):  struct PASS, battery 0 fails, 0 members (vacuous census).
- (32,16,577,rand2):  struct PASS, battery 0 fails, 10 members (all |S| = 18 =
  k+2), 10 charts, max 1/chart. POPULATED fresh prime+mode.
- Parity/band tabulation: every member even |S|, in {k+2, k+4} <=> band ✓ (#135).

R2 MUTATION MA (normalization drift, #133): TRIPPED at both cells. Building u1
with auxiliary labels c_i/(y_i - y_nf): S2 factorization breaks AND the census
bijection breaks. NOTE (see catch #137): |quo_aux| = 0 at both cells — the
wrong-normalized word has NO periodic-lift contributors at all; the failure
mode is an EMPTY census (vacuity trap), not a perturbed one.

R3+R3b MUTATION MB (aperiodic complement, S4 else-branch — a branch the
packet's verifier never enumerates): 5 cells, 123 complement members total
((16,8,97): 2; (32,16,97,geom5): 45; (32,12,193,consec): 76; two cells empty).
ALL lift to official contributors with ODD |S| = 2|agr|+1, c(S) = 1, x_nf in S,
-x_nf notin S — zero exceptions. BONUS cross-check: the with-y_nf counts (63,
43) equal the pinned official scale->=2 counts exactly — the full quotient
contributor list partitions cleanly into {periodic lifts} + {aperiodic odd
lifts}, live-confirming S4's dichotomy on complete censuses.

R4 MUTATION MC (bijection liveness): deleting one official member -> battery
reports BIJECTION. TRIPPED as required.

ALL PRE-REGISTERED EXPECTATIONS MET. No deviations.

## CATCHES #136-#137

- #136 (COMPOSITION CONSUMPTION MAP — wire the req edges right): Claim 3-C
  consumes ONLY {L0, S3/S4 (thence L1/L2/S1/S2), U1 (thence U0) + L1, the G1
  coverage hypothesis}. It does NOT consume the tail-collapse chain: the chain
  (petal_retained_zero_effective_degree -> petal_full_touched_set_injection ->
  petal_top_band_tail_collapse) is consumed ONLY by S6's m'+1 safety line,
  i.e. by SUCCESSOR-A's literally-stated obligation (ii). Surgery consequence:
  the CONDITIONAL's load-bearing req edges are {packet Claims 1+2+L0,
  G1-coverage}; the three chain edges support the obligation-(ii) wording and
  the m'+1 fallback only. A future weakening of the chain would NOT touch the
  composition's classes-per-U <= |A'| line.
- #137 (NORMALIZATION DRIFT IS ANNIHILATING — #133 sharpened): mixing the
  normalizations does not merely perturb the descended census, it EMPTIES it
  (0 contributors against the aux-labeled word at both tested cells, vs 1/3
  true members). A consumer that builds u1 with layer-normalized labels and
  then "verifies no violations" passes VACUOUSLY — the bug presents as an
  empty list, not as a mismatch. Downstream checkers should assert census
  NONEMPTINESS (or pin expected counts) alongside the bijection.

## LINK-BY-LINK VERDICT TABLE — see final report (all links SOUND)

## FINAL VERDICT: PACKET-SOUND

Claims 1, 2, 3-L0: PROVED (audit passed: hand re-derivation + verbatim
upstream-hypothesis check + replay + 4 packet mutations + 3 auditor mutations
+ 4 fresh cells + 123-member aperiodic-branch live test).
Claim 3-C: PROVED-CONDITIONAL on exactly one hypothesis (G1 coverage).
Two cosmetic verifier notes (BAND_EQUIV tautological given D_ARITH; M3's
union condition trivially true) — no repairs required, no check weakened.
Surgery spec in final report: SUCCESSOR-A -> CONDITIONAL on G1 coverage.
