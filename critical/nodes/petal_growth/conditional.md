# petal_growth — CONDITIONAL packet (r2, 2026-07-12 cluster import;
# r1 2026-07-10 amber surgery retained below where unchanged)

- **status:** CONDITIONAL (amber)
- **predicates (open, req-wired):** `petal_g1_layer_maps` (the first-match
  ATLAS form, re-posed 2026-07-12), `petal_k4_primitive_bound`,
  `petal_small_scale_staircase_census` (the gate minted at the G2 flip —
  catch #80).
- **compiler (amber, req-wired):** `petal_g3_pricing_multiplicity`,
  CONDITIONAL on G1 — clause (b) proved in general
  (petal_g3_profile_conversion_identity), clause (a) via full-support
  codeword injectivity + first-match charge-once; census carve-out
  explicit.
- **proved this import:** G2 (stabilizer partition — flip banked WITH the
  census gate), the conversion identity, injectivity, the exact 719
  allowance (= floor(n^6/C(n+6,6)) at all four official maximal rows; the
  integer sharpening of the banked 9.4919-bit slack).
- **route of record (r2):** G1-atlas -> first-match charge-once ->
  {per-class: injectivity + conversion identity -> 719 x column, scales
  M > t via the replayed composite | scales 2 <= c(S) <= t: the census
  gate} | primitive: K4 -> floor.
- **catch #79 (2026-07-10 r1 correction):** r1's clause (iii) + K4 did NOT
  imply the primitive n^{b1+b4} line ('machine-verified assembly' covered
  the budget arithmetic only); the atlas total-census clause |A_U| <=
  n^{b1} is the repaired sufficient form.
- **stale r1 lines corrected (catch #82):** P1's 'all four predicates'
  reads 'all wired predicates'; the fifth-branch 'fastest close of G3'
  line is superseded (clause (b) is now PROVED; the branch remains
  ev-only/replay-annotated); the r1 route-of-record routed ALL staircase
  pricing through the M > t composite — the small-scale class is now
  explicitly owned by the census gate.

## Re-surgery criteria (r2)

1. Any wired predicate falsified as stated.
2. The G4 dictionary check fails on a sweep cell, or the escalation rule
   fires.
3. The conversion identity contradicted at any cell (mutation-controlled
   verifier banked).
4. Pin P1 resolved to a different band constant (maintainer line owed).
5. imgfib's quotient clause re-scoped so the P3 emission no longer lands.
6. The census gate falsified (the banked engineered family exceeding the
   budgeted column at scaled rows) or its landing re-scoped.

---

## r1 packet (2026-07-10) — retained for pins P1/G4/G5/P3 and history


- **status:** CONDITIONAL (amber)
- **route of record:** G1 -> pma -> [G4 pin] -> cofactor packets -> G2 ->
  {staircase: tail-coset + 7-lemma composite -> G3 -> quotient budget |
  primitive: K4} -> floor
- **audit:** fresh-context amber audit 2026-07-10 (sequel to WP6_PETAL_VERDICT),
  verdict AMBER-READY; all packet verifiers replayed exit-0 a second time,
  budget arithmetic machine-checked exactly (record in KB_LOG #20).
- **supersedes:** the 2026-07-05 archived predicate route below (retained for
  history; see RETRACTION_MANIFEST.md).

## The implication (machine-verified assembly)

IF the four wired predicates hold —

1. `petal_g1_layer_maps` (layer-map supply for arbitrary U, with the
   load-bearing joint chart-control clause (iii)),
2. `petal_g2_support_forcing` (support-forcing dichotomy, CLOSURE form over
   all dyadic scales M >= 2 — not SOL_TARGET_2's fixed-M form, which leaks
   scales M <= sigma+1; audit Finding C),
3. `petal_g3_pricing_multiplicity` (per-support codeword multiplicity <=
   n^{b3} + exactness of the declared inclusion-exclusion weight W),
4. `petal_k4_primitive_bound` (stabilizer-primitive auxiliary lists <=
   n^{b4}, band-restricted chart form; the kernel K4),

— THEN at every official row (n = 2^41..2^44, k = 2^40) and every received
word U, the top-band full-petal contribution to #ImgFib_U(k+sigma) splits as

- **primitive part** <= n^{b1+b4}, charged to the n^B budget;
- **staircase part** <= n^{b1+b3} x (planted binomial column), charged to
  imgfib's quotient-profile budget (pin P3) — a charge proved NECESSARY by
  `v13_capf_planted_lower_count` (exact column match: 507 / 32760 bits
  super-budget vs n^10 at official-like shape; no n^B absorbs it).

Every non-predicate link is PROVED and on the critical surface (req-wired
green skeleton): prop:capf-pma injection; the four E22 packets
(`e22_agreement_cofactor_equations`, `e22_cofactor_petal_divisibility`,
`e22_tail_coset_locator_algebra`, `e22_lower_scale_filter_inclusion_exclusion`
with its req-chain and `e22_fiber_locator_saturation` — the replayed 7-lemma
staircase composite); `v13_capf_planted_lower_count`; and the exact budget
arithmetic (saturated column exponent <= 5.785 at all four official maximal
rows, slack exactly log2(6!) = 9.4919 bits).

**Slack warning (audit, adversarial):** the 9.5 bits IS the binomial
denominator log2(6!), not structural headroom — it vanishes against any
720x constant inflation of the paid family. Do not spend it inside the
predicate exponents b1/b3/b4; it is consistency margin only.

## Pins (definitional; part of the amber statement)

**P1 (band constant — audit Catch B).** The floor's band is d >= M(t-2)
(M = petal/fiber size, t = petal count). The operational scan band
(`experiments/petal_excess_local_scan.py`, summarize()) is top_defect =
(t-1)*M — narrower by one petal. The floor claims the WIDER band (safe
direction); all four predicates are quantified over the floor's band.
Maintainer decision owed: one line confirming which band was intended;
if the narrower, re-pin (re-surgery criterion 4).

**G4 (E22 dictionary pin).** Auxiliary layers are the Z∩C = ∅
specialization of the E22 challenger normal form. Dictionary: E22 receiver
(0 on C∪B0, a_i·L_C on petal P_i) ↔ auxiliary word U_{D0} (0 on D0∪R0,
c_i·L_{D0} on T_i); challenger f ↔ G = Psi(P); E22 core C ↔ missed core D0;
background B0 ↔ retained residual R0; labels a_i ↔ c_i; E22
degree/threshold instantiated at (<= d, >= a). Layers forbid D0-agreements,
hence force Z∩C = ∅; E22 allows Z∩C nonempty — the packets are consumed in
the SPECIALIZATION direction only (weakening of hypotheses, no new math).
Falsifier (machine-checkable): an auxiliary-layer member from any sweep
cell whose petal-agreement system violates the transported cofactor
equation. ESCALATION RULE: if any E22-side hypothesis turns out NOT weaker
(e.g. exactness of agreement sets), G4 escalates to a fifth predicate and
the amber re-opens (re-surgery criterion 2).

**G5 (primitive-notion pin, absorbed into `petal_k4_primitive_bound`).**
"Stabilizer-primitive" = aperiodic (c(S)=1, def:periodicity-scale) in the
chart's fiber lattice — the SAME notion G2 charges, which is what makes G5
vacuous-by-definition. Honesty cost, declared in the node: the band-restricted
chart-level K4 neither implies nor follows from upstream's row-level
prob:capf-primitive-image-fiber; upstream K4 is its provenance and natural
attack route, and consuming a future row-level proof needs a band-restriction
bridge as a then-new proof obligation.

**P3 (emission pin).** The staircase/quotient-periodic branch (including
G3's multiplicity factor) is charged to imgfib's quotient-profile clause,
quantified by the PROVED `dyadic_profile_evaluation` node (QA.22 exact) —
never to n^B; no double-charge, no silent no-charge.

## NOT consumed (audit Catch A)

`e22_cross_scale_pricing_multiplicity` and the minimal-scale (fifth E22)
branch are NOT wired, despite dag status PROVED: WP6 explicitly did not
replay that branch, and its key node `e22_minimal_scale_pricing_compatibility`
has no verifier. (WP6's verdict line "exists nowhere" was WRONG — the node
exists locally since Jul 5; corrected in the node statement and
WP6_PETAL_VERDICT.md.) The branch carries REPLAY-PENDING annotations in
dag.json; a fresh-context replay of it is the fastest close of G3.

## Re-surgery criteria (demote to TARGET if any fires)

1. Any predicate falsified as stated.
2. The G4 dictionary check fails on a sweep cell, or the escalation rule
   fires.
3. The fifth-branch replay contradicts the declared W semantics.
4. Pin P1 resolved to a different band constant.
5. imgfib's quotient clause re-scoped so the P3 emission no longer lands.

## Scope

Top band only. Mixed-petal and below-top contributions are separate
obligations, untouched by this packet (below-top is Lemma-13-clean on the
76-row scan; see the node statement's survival ledger).

---

## Archived predicate route (2026-07-05 retraction; historical)

- `petal_fixed_excess`, `petal_excess_induction` (+ alternate
  `petal_mixed_amplification`): cut by the 2026-07-05 retraction after
  repeated falsifications-as-stated (Gate N, PRK, chargeability); see
  RETRACTION_MANIFEST.md and archive/retraction_petal_20260705/. These
  remain evidence/attack structure only.

## Stress evidence 2026-07-06 (retained)

`experiments/petal_excess_local_scan.py` ran a local coset-chart
residue scan (16 configurations, 76 rows): no below-top Lemma-13 violations;
ambient `dim K` grows with `c` (flat-kernel induction not revivable); exact
realizable counts max `1` below top, max `5005` at/beyond top — the shape
that motivated the top-band paid-family focus this packet now formalizes.
NOTE: this scan's band is the (t-1)*M operational band — see pin P1.
