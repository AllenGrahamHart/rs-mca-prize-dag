# Pilot campaign ledger — consolidated decisions, obligations, and queues

**Purpose:** single findable index of everything the 2026-08-02 Opus
pilot campaign has left open or pending. Evidence lives in the pilot
directories (`notes/pilots_20260802/*/REPORT.md` verbatim +
`FABLE_AUDIT.md` coordinator verification) and in dated node-local
flags; THIS file is the queue. Update on every bank; entries move to
"resolved" with a commit hash, never deleted.

Banked pilots this campaign (all coordinator-replayed before banking):
`xr_bridge_semantics` (30e40f70) . `f2_slice_coefficients` (639970c8) .
`c1_norm_ladder` + `pb_selector_orders` + mint (56d93816) .
`p_a1_widening_cost` (79316563) . `xr_cascade_payment_audit` (5cc59b52) .
`xr_graded_band_ledger` + `pb_fm3_mechanism` (this commit).
In flight: `f2_parity_boundary`, `c1_imprimitivity`.

---

## A. SURFACED DECISIONS (user / maintainer ratify; Pro adversarial input welcome)

1. **Route W vs Route T** (band repair). State: **RECOMMENDATION =
   ROUTE T**, redesigned as a THIRD generic column from the 13n^3
   headroom (never enlarging B_tan — dead on 5/6 rows even at
   N_d = 1; never splitting 8n^3). Reconciliation: the cascade audit
   killed T-as-B_tan-enlargement (correct); the band-ledger pilot's
   third-column design avoids that objection entirely, and T then
   strictly dominates W (same single open input — the band occupancy
   lemma — bought with ZERO demotions and unchanged prize ranks;
   Group-C nodes become conditional on the band column via an
   explicit req edge instead of permanently re-scoped). Wording
   defects (strip item-3, cascade "paid", 4,662 sentence,
   clean_residual "removes") get fixed under EITHER route. Evidence:
   `xr_graded_band_ledger/` + `xr_cascade_payment_audit/` +
   `p_a1_widening_cost/`. Awaiting user/maintainer ratification +
   Pro adversarial round.
2. **PP4.0 freeze** as the **COMPRESSION-ORDER CLASS** (greedy
   coordinate-sequential minimality: lex/colex under any coordinate
   permutation) — CORRECTED from "support-keyed" by the FM3 pilot:
   the hash null controls ARE support-keyed (they key on the mask)
   and they are RED, so the support-keyed class admits the nulls.
   Exclusions unchanged (polynomial/codeword/procedural; slope-major
   degenerate; error-lex = reverse-lex). Evidence:
   `pb_selector_orders/` + `pb_fm3_mechanism/` section 5.
3. **Strip item-3 scope-narrowing** (`xr_strip_classification_rungs`):
   corrected wording in its `BAND_OVERCLAIM_FLAG_20260802.md`
   (amended: NO core-based charge proved at any threshold).
4. **Cascade scope-narrowing** (`xr_pencil_cascade`): PROVED = forcing
   + cascade only; "paid" and the one-pencil "~n-core" clause need
   scoping. `PAYMENT_UNSOURCED_FLAG_20260802.md`.
5. **P-B EXPOSURE — RESOLVED TO ONE SCOPE CALL (pb_gamma_exposure
   banked, superseding the first framing of this item).** Kill line
   K1 is CLOSED for the entire split-fibre class by the proved
   (SF-SELFCOLLISION) lemma (planted slopes all high-core, ZERO in
   Gamma_lo at every q — structural, selector-free). "Safe by field
   size" refuted (no row has q_max < 8n^3; safety = witness supply).
   The construction-free exposure is confined to **RowC 1/4,
   q in [2^192.29, 2^200.11)** (random supply up to 2.63e9 x 8n^3;
   exact criterion C(n,A) > (8n^3)^h 2^{128(h-1)}, satisfied ONLY
   there, by +156 bits). **THE ADJUDICATION: which q-scope governs
   P-B** — (P1) official_row_primes_pinning (PROVED, family-uniform)
   => the window is LIVE; (P2) the clean-anchor envelope pins
   (q >= 2^250) => all six rows supply-safe (>= 49.9 bits). RowC 1/16
   FRAGILE (2.31 bits, 58.6% of budget). The (PB-SUPPLY) discharge
   skeleton goes to Pro: P-B reduces to (H4) restricted to
   non-split-fibre concentration + the RowC 1/4 scope/floor decision.
   Maintainer item routed: the 2^189 char-0 / 2^55 single-field
   distinct-bad-slope pencil is the matching LOWER bound for the
   row-soundness gap already recorded at
   xr_agreement_raise_quotient_safe_sum_fence.

## B. NAMED PROOF OBLIGATIONS (open)

- **k-packing lemma — WITHDRAWN as a mint** (subtraction check by the
  band-ledger pilot): already banked verbatim at
  `xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`.
  Cite it; do not re-derive.
- **BAND OCCUPANCY LEMMA — REDUCED (xr_band_occupancy banked; round 3
  complete 4/4).** The lever discharged: high-depth injectivity
  (Theorem 2) converts 96.9% of the ledger cost into "**some pencil
  member has <= ~0.7n^2 codewords at agreement k + ceil(h/2)**" — a
  single-word beyond-Johnson RS list-size bound (25-50% of Johnson),
  SAME SPECIES as positive target #1 (L1/#106); min over q+1 pencil
  members; the low band is free at any bound up to n^2 (0.52-0.65 n^3
  of headroom). F1 not fired (best admissible construction — the new
  sunflower family — is exactly LINEAR, formula floor((n-k+1)/(h-d)),
  ~21 orders below requirement); master ledger worst-case TIGHT
  (slope-counting buys <= 2x); no-go proved for every slope-side
  route. **MANDATORY GATE before banking the reduction: check
  BSKR-style superpolynomial-list constructions (additive domains) for
  transfer to the multiplicative prize domain** (vs
  literature_map_20260726 + Pro). Corrections: Route S un-killed
  (re-selection real, 15/76 — key everything on RAYS); tangent gate
  must cover all of P^1 incl. (0:1). Mint queue: occupancy-pilot T1
  supersedes band-ledger T4+T5; mint T1 + T2 (+ T4 bookkeeping) with
  the Route T edit; Deza clique corollary awaits its covering
  argument.
- **Band-ledger mint queue (with the Route T edit):** Theorem 3 (line
  cap under J >= k — the banked `common_code_line_budget` hypothesis
  is out of range at all six rows, see its node note), Theorem 4 (ray
  rigidity), Theorem 5 + corollary (the band interaction strip:
  d_1 + d_2 >= h forces a tangent event — a genuine strip extension),
  Theorem 7 (two-column determinacy). Theorem 6 recorded as a warning
  (per-ray multiplicity = MDS list size; master inequality lossy).
- **Injection-extension one-liner** — recovered-line slopes <= |T| <=
  n-A+1 at forced core >= A-1; scope-widening of
  `xr_true_tangent_coordinate_injection` (proof already
  hypothesis-free). Makes half the cascade charge sourced.
- **A-1 ceiling derivation** — generic-branch cores <= A-1 from
  genericity + strip forcing algebra (one line, verified). Bank inside
  the coordinated edit.
- **xr_band_core_slope_count** — new TARGET (<= 4n^3 from the 13n^3
  headroom; NEVER by splitting 8n^3 — AZC margin 0.5005%). Mint on
  Route W ratification. Candidate statement:
  `p_a1_widening_cost/REPORT.md` section 5.
- **FM3 — RESOLVED AS A RE-TARGET** (`pb_fm3_mechanism` banked): the
  mechanism is greedy-depletion marginal tilt (parameter-free model,
  5/6 frozen predictions PASS); FM3 as a "Gamma_lo small" theorem is
  DEAD at official scale (the collapse inverts); its conditional
  small-scale form's entire content is the equidistribution hypothesis
  (H) (Weil-type, unknown) and it is NOT a lane target. The exchange/
  swap route is closed (third refutation). See surfaced item A.5 for
  what replaces it.
- **b-resolved slice-coefficient theorem (F2)** — boundary pilot
  BANKED: the hypothesis is (H-spread)/(H-flat) — spectral flatness
  of the Delta multiset over ALL odd modes — NOT parity
  (adjacent-pair killer: beta_min = 1/2, eta = 0 exactly, universal,
  proxy-independent; parity is only the k=p frequency). Coordinator
  drafts the theorem with BOTH budget variants displayed; **PP5.0 is
  now load-bearing on the budget choice** (1/3 viable for only ~15%
  of windows and impossible outside beta in [0.206,0.794]; 1/43
  clears at 97%+ under flat >= 0.086). Then Pro adversarial round;
  no node before both. Mutation battery: adjacent-pair, arc-w,
  few-value, coset-trivial added.
  (`f2_parity_boundary/{REPORT,FABLE_AUDIT}.md`.)
- **Imprimitivity conjecture (C1) — REFUTED, retired** (pilot banked):
  exhaustive counterexample at 2N=64 w=11 (primitive argmax, ratio
  1.0259, coordinator-replayed); break weights 3/7/10 at N=8/16/32,
  not N/2. The minted sandwich node is untouched (all four PROVED
  claims re-exercised); dated correction appended to its context
  section. The lane keeps what it needs unconditionally (router
  threshold, saturating family). Mint queue additions (small, proved):
  Lemma C (odd-autocorrelation monotonicity), the rotation identity,
  Norm == w (mod 2), imprimitive => square-norm certificate. Proof
  necrology recorded (majorization dead with certificate, local moves
  dead via the U-shaped two-branch value function).
- **Crossing lane — round-3 pilot BANKED + contract DRAFTED.** PK1
  (the one-packet theorem) PROVED at the smallest instance: exact
  q-free packet C(n,r)/n, ceiling, fence, closed-form template,
  automatic guard, exhaustive inverse maximality (all three verifier
  suites coordinator-replayed: 1002 + 46 + 17 checks). PK2 scope
  theorem: q-freeness is a w=1 phenomenon (w=2 certified q-dependent
  across 20 fields); the official regime is the q-dependent regime.
  Mutation suite M1-M9 adopted as the lane's standing battery.
  Subtraction done: lower half dominated by the rotated-prefix floor
  (upstream #1101); new content = the upper half + PK2 + inverse
  maximality. Frontier movement ZERO (recorded). MINT CANDIDATE (next
  boundary): PK1 as background node with the fast verifier. The
  succinct contract is DRAFTED for Pro's round:
  `notes/pro_briefs_20260801/responses/CROSSING_SUCCINCT_CONTRACT_DRAFT.md`
  (primitives incl. symbolic counted-objects, forbidden moves,
  q-independence via index-family replay, B*=0 pin discharge, M1-M9
  compliance). Lane question for Pro: per-field certification at
  w>=2, or hunt q-free word classes (Lam-Leung candidates)?
- **C2'' lane — round-3 pilot BANKED; the lane is RE-POSED.** The
  exact structural law (junction matrices are scaled Vandermondes;
  delta = sum (L_j - |S_j|)^+, field-independent) KILLS the
  rank-defect currency by the adversarial audit's own kill line:
  {delta = t} IS the archived coset class (already routed + priced by
  the marginal account); the joint excess R lives at delta = 0 where
  the invariant is blind (0/65,535 states correct); R = E[q^delta]
  and its dominating form die with exact counterexamples; the two
  canonical seams differ by q^{255t} (PP2.0 upgraded from Gate-0 to
  DECISIVE). NUL0-NUL4 RETIRED as posed. Delivered: PP2.1 (the exact
  multi-junction compiler, validated 42/42 + 23/23,
  coordinator-replayed), the DERIVED schedule ell_j, the coset-atom
  tail law, and the RE-TARGET: the residual is an arithmetic
  norm-divisibility event in Z[zeta_n] (exact certificate; 1/phi(n)
  splitting) — C2'' routes into the lane's own norm-gate/resultant
  machinery. Third lane this campaign whose heart is arithmetic.
  Pro ask: attack the norm-gate residual framing; adjudicate PP2.0.

## C. THE COORDINATED EDIT (Route W, IF ratified — one commit)

Base: the three-part change in `p_a1_widening_cost/REPORT.md` section 5
(widen P-A1 to core >= k; demote invalidated PAID entries incl. the
"4,662 forced pairs" sentence; re-scope Group-C background nodes with
an explicit kappa = k hypothesis; open the band TARGET). Additions from
the cascade audit: kappa lands at **A-1** not A-2 (line caps exactly
x2; PSP unchanged); move `F5_SKELETON.md:363` and
`xr_smallcore_spread_count`'s dag statement quantifiers to A-1;
`xr_clean_residual_any_gate/conditional.md` "removes" -> "classifies"
(+ second unproved contribution); `notes/kernel_basis/
WP7_WORSTWORD_VERDICT.md` "two proved bookends" correction; bridge R2
statement edit; strip item-3 rewording; cascade scope-narrowing; pin
ONE symbol for K/k; re-run pinned verifiers of PSP/CRB/FN at kappa in
{k, A-1}; retire `xr_smallcore_spread_count` re-surgery criterion 3
(moot under the widening). Consumer wording repairs from
`p_a1_widening_cost/REPORT.md` section 4 (WAVE5/WAVE20 findings,
BRIEF_3 lines, target_mappings.json:145).

## D. CODEX WORKER QUEUE (fold into OPUS5_WORKER_GOAL.md at next wave boundary, AFTER m2 positive composition)

- F2A.2 reachability audit re-run on the difference subgroup
  D = <Delta_i - Delta_j> (Sharp Law A does not survive b-resolution).
- Duplicate-node-id validator assert (gap found wave 38).
- PSP/CRB/FN pinned-verifier re-runs at kappa = A-1 (if Route W).
- Case work from lane charters as they freeze.

## E. FLEET / BIG-BOX ITEMS (outside the 1G law)

- Native/bit-packed enumerator at n = 44 / 48 — **RE-SCOPED by the
  FM3 pilot**: the target is Pi (the population partner count), not
  the budget clause. Frozen pre-registered prediction: at n = 44,
  rate 1/2, q = 1.33e6, Pi = 2^-4.4 < 1 and Gamma_lo = Gamma for
  EVERY order including lex. One measurement that confirms or
  destroys the official-scale extrapolation.
  (`pb_fm3_mechanism/REPORT.md` caveat 6.)
- 2N=64 w=8 exhaustive ladder point if the imprimitivity pilot's
  branch-and-bound does not finish it.

## F. PRO RELAY PACKAGE (user relays)

- **NEW — the F2 theorem draft is READY for the adversarial round:**
  `notes/pro_briefs_20260801/responses/F2_SLICE_THEOREM_DRAFT.md` —
  (H-spread)/(H-flat) hypothesis, both budget variants, the killer
  list, the three explicit gaps, and the three-part ask (attack the
  clause; freeze PP5.0's budget; the window-selection question = the
  lane's new heart).

- Pilot REPORTs: all six banked directories (+ the four in flight as
  they land).
- Amended summaries: `BRIEF5_ADVERSARIAL_AUDIT_SUMMARY.md` (Delta
  inversion addendum); `pb_split_fibre_selector/FABLE_AUDIT.md` (FM3
  withdrawal addendum).
- Decision asks for Pro's adversarial eye: the W/T fork (section A.1),
  the PP4.0 class freeze (A.2), and — when drafted — the
  slice-coefficient theorem hypothesis clause and each lane charter.
- Per-brief next asks: recorded at the end of each
  `notes/pro_briefs_20260801/responses/BRIEF*_DOSSIER_AUDIT.md`.

## G. NEXT PILOT ROUND (planned anchors)

- **C2'' structure pilot** — the one lane untouched by this campaign
  (weighted cross-junction nullity tail; exact fixtures exist in its
  adversarial audit materials).
- Crossing packet pilot — AFTER the succinct contract (B) is drafted.
- Cascade-tier population probe at scaled rows (open question 3 of the
  payment audit), if the fork lands on W.

## H. PROVENANCE FOLLOW-UPS

- Pull the "W1, PR #10, 70/70" replay artifact for `xr_pencil_cascade`
  (no in-repo copy) and the upstream #147 tangent-staircase .tex;
  needed for any re-grade of the cascade node.
- Sandwich node: add a dated remark that Lemma A is the norm-tower
  formula (standard ANT) — honesty pointer, low priority.

## Resolved this campaign

- Bridge flag adjudicated: genuine gap, R2 forced (30e40f70).
- FM3 prefix wording withdrawn (56d93816).
- c_w^(N/4)-as-stated falsified; sandwich theorem minted (56d93816).
- Widening priced; fork surfaced (79316563).
- Cascade payment audited; ceiling re-sourced at A-1; fork tilted W
  (5cc59b52).
- Route T redesigned as a third column; 4 new theorems (line cap,
  ray rigidity, interaction strip, two-column determinacy); occupancy
  lemma named as the single heart; fork recommendation -> T (this
  commit).
- FM3 mechanism identified (greedy depletion); FM3-as-theorem retired;
  P-B re-targeted to bounding |Gamma|; PP4.0 class corrected to
  compression orders; n=44/48 re-scoped to Pi (this commit).
- k-packing mint withdrawn — already banked (subtraction check, this
  commit).

---

## ROUND 4 CLOSE-OUT (4/4 banked, dbc7cdb7) — supersessions and the new top adjudication

- **C1 + C2'' MERGED at junction 0** (dli_norm_gate): censuses
  byte-identical; splitting = exact identity + bounded correction
  (S1-S3); official support-forcing theorem (|S_0| >= 4 at
  q > 3^128); WCL fence q > w^128 (4^128 = 2^256 exactly);
  DECISIVE NEGATIVE: no open WCL slot via max-norm — count bounds
  only. **Most mint-ready package of the campaign** (LN1/LN2/LN4/LN7
  + the support-forcing theorem). New consumer for the C1 doubling
  conjecture at w=4 (the (1,4) slot two-liner).
- **F2**: the ANTIPODAL LAW (deployed windows parity-homogeneous by
  construction; window selection impossible; frequency-space case
  split required; theorem draft AMENDED IN RELAY). NEW OBLIGATION:
  fixed sector mu_{2^24} absorbing the parity-pure class.
- **Band reduction SUPERSEDED (V1)**: the beyond-Johnson list
  statement is FALSE (first moment + the certified MC construction);
  the occupancy LEMMA stands; new splits must keep the two-live-slope
  structure. KEY LEMMA + pencil mass identity proved (mint queue).
- **NEW TOP ADJUDICATION (coordinator, then Pro): is depth d = h-1
  band or cascade tier?** MC produces 2^130-2^197 pairwise
  non-interacting cascade-depth pairs on a gate-admissible received
  pair. If band: the occupancy lemma is REFUTED and the band repair
  needs re-posing. If cascade tier: the (unpaid, per the payment
  audit) tier is astronomically populated and BOTH repair routes'
  extension terms need re-pricing. Intersects the payment audit, the
  ledger, and task #27. Also queued: "strip-free" needs a written
  definition; the below-cascade reading must be pinned.
- **P-B**: (H4) hunt — design space exhausted (affine lines of
  AG(h,q)); richest admissible line always split-fibre, Gamma_lo = 0;
  DESIGN CEILING proved (counterexamples >= 1-2^-23 forced); block
  dichotomy derives SF-SELFCOLLISION; SELECTOR CATCH (Gamma_lo = 0 is
  identity + support-keyed selector; K1 re-couples to PP4.0);
  gauge-invariance scope correction for all P-B gates ((alpha,beta)
  mod RS_K). (H4) refined to (H4') with the equidistribution gap
  named; the FRAGILE row's slack is not consumed by the constant.
- Mint queue additions: norm-gate package; MC family + ceiling;
  KEY LEMMA + pencil mass identity; L1 + design ceiling + block
  dichotomy; antipodal lemma + parity-defect certificate.

---

## WORKFLOW CHANGE 2026-08-02 (maintainer directive): Pro PAUSED

The loop is now Fable (coordinator/auditor) + Opus pilots + the Codex
worker; the user ratifies surfaced decisions. Consequences:
- Section F ("Pro relay package") is RE-PURPOSED as the INTERNAL
  ADVERSARIAL REVIEW QUEUE: every item that awaited a Pro adversarial
  round (the F2 slice-theorem draft with its amendment; the crossing
  succinct contract; the Route T fork memo; the (PB-SUPPLY) skeleton
  with the selector clause; the q-scope call briefing) now gets its
  adversarial round from a dedicated Opus pilot with pre-registered
  kill lines — same falsifier-first discipline, in-house.
- Decision sequencing simplifies to: pilot evidence -> coordinator
  adjudication -> user ratification (for genuine choices) -> execute
  -> upstream visibility via PRs (the export discipline is unchanged
  and remains the only external loop).
- "PP-gate freezes" (PP2.0, PP4.0, PP5.0) are now coordinator drafts
  + internal adversarial pilots, then user sign-off.

---

## RATIFICATION 2026-08-02 (maintainer/user): ALL FOUR ITEMS APPROVED

1. **Band repair RATIFIED**: Route T (third generic column from the
   13n^3 headroom; B_tan untouched; 8n^3 never split) + the fold-in
   of d = h-1 as a NAMED cascade tier in the band column [1, h-1].
   The coordinated-edit bundle is UNBLOCKED (task #27): bridge R2,
   strip item-3 + cascade scope-narrowings, the four wording repairs
   (4,662 sentence; clean_residual "removes"; WP7 bookends; F5-OS +
   xr_smallcore quantifiers to A-1), the 10-item definitions glossary,
   the band TARGET node, and the mint wave (band-ledger T3/T4/T5/T7,
   occupancy T1/T2/T4 + Theorem G + Theorem 5/BP merge, KEY LEMMA +
   pencil mass identity, MC family, L1 + design ceiling + block
   dichotomy, the four norm-gate packages after line-audit, antipodal
   lemma + parity-defect certificate).
2. **PP4.0 RATIFIED**: compression-order class (lex canonical);
   polynomial/codeword/procedural readings excluded; slope-major
   degenerate + error-lex = reverse-lex recorded as closed forks.
3. **q-scope RATIFIED**: (P1) family-uniform governs the ultimate
   claim (per official_row_primes_pinning's own demand); the RowC 1/4
   window q in [2^192.29, 2^200.11) is a RECORDED LIVE OBLIGATION;
   envelope-scoped intermediate results permitted, explicitly labeled.
4. **PP5.0 working budget RATIFIED**: 1/43 (freeze to follow the
   composition-law draft + internal adversarial round; the K1 mass
   obligation O1-O3 shapes the seam).

Execution order (coordinator): (a) two adversarial pilots launched
(Gamma-in--H; the sublinear-rank class); (b) norm-gate mint line-audit
per AUDIT_CHECKLIST; (c) the coordinated-edit bundle in ONE commit
against the ratified decisions; (d) roadmap r3.

---

## ROUND 6 CLOSE-OUT (4/4 banked: adv_gamma_minus_h, adv_sublinear_rank,
## wcl_count_bounds + exact_k_heart + rowc_window, support4_relation — f93cdc03)

Campaign totals: 32 pilots, 32 verified-then-banked, 0 accepted without
replay. The six original mysteries now stand as the 7-heart inventory
(reported to the user 2026-08-02); the band heart is PURELY COMBINATORIAL
(escape form), P-A1's is |K|, P-B's is adversarial planting, F2's is the
K1 mass obligation (O1)-(O3), C1/C2'' is sparse certificates, crossing is
the w >= 2 boundary. NEXT-ROUND ANCHOR: unify |K| with the escape residual.

## NORM-GATE MINT LINE-AUDIT (execution item (b)) — COMPLETE, ALL FOUR ACCEPTED

Per drafts/AUDIT_CHECKLIST.md; every hand-verify item done, all 12
uncertainty flags adjudicated:

- **F1.a/F1.b KEPT** (parenthetical bracketed as non-load-bearing;
  ramification caveat framing is wanted — both hypotheses named).
- **F2.a: `ref` RATIFIED** — the energy-ceiling proof is self-contained
  (Steps 1-4 spelled out with E throughout), so the sandwich edge is
  attribution, not dependency; hand-checked the exact-integer Parseval
  form (constant coefficient of alpha*alpha~ = E) and the n=4 conjugate
  pairing boundary.
- **F2.b KEPT OUT**: the WCL fence stays a candidate FIFTH node
  (checklist item 5); mint deferred, recorded in section B.
- **F3.a stays flagged**: Stab(U_j)={1} at official j <= 25 is an open
  side condition (verified pattern m <= 11); nothing minted depends on it.
- **F3.b/F4.b RESOLVED**: both corrections of record already appended to
  the provenance REPORT (1960/63; 2453) — the persisted artifacts are
  authoritative and the proofs cite them.
- **F4.a DISCHARGED**: junctions.py's rho definition matches Claim 4's
  citation verbatim (incl. the exact Z[zeta_q] 24/24 certification).
- **F4.c CONFIRMED**: official_scale.json pins 33 junctions / ratio 256;
  the 34th-block reading stays recorded-unused.
- **F4.d/F4.e KEPT** (closure string exists in vocabulary; exhibit
  framed as non-certificate illustration).
- **ONE FORCED CORRECTION (applied)**: the max(U)^2 < n stabilizer
  condition requires `1 in U` (proof uses b = b.1 in U); proviso added to
  the splitting-law statement.md + dag statement. Official blocks all
  contain 1, so scope unaffected.

WIRED: 4 background nodes (all PROVED), 5 internal req + 1 ref
(sandwich attribution) + 4 ev into the two red TARGETs
(dli_c2pp_joint_reserve x3, dli_c1r3_gated_envelope_bound x1) — all
three C2''-side ev edges kept (distinct evidence contributions).
DAG: 1746 nodes / 4838 edges; manifest refreshed
(scripts=2347, proof_assets=2475); all four verifiers PASS in place.
No status flips; the math-orbit census is unchanged.

Execution queue: (b) DONE -> (c) the coordinated-edit bundle -> (d)
roadmap r3. Sequencing note (coordinator authority): the norm-gate mint
ships as its own commit — it is DLI-lane, independent of Route T; the
Route T coordinated edit stays atomic in its own commit.

---

## COORDINATED-EDIT BUNDLE EXECUTED (execution item (c)) — ONE COMMIT

Against the four ratified decisions. Contents: (1) bridge R2 + Route T
THREE-WAY partition of record (Gamma_band | Gamma_hi exact-k | Gamma_lo;
definition-based, no core-cap premise; P-A1 keeps exact-k with ZERO
demotions — Route T's promise, now sourced); (2) strip item-3 correction
(forcing only; ceiling A-1 sourced; band CLASSIFIED) + (3') consumption
addendum 20n^3 <= 29n^3; (3) cascade scope correction ("~n-core" and
"paid" WITHDRAWN from proved scope; forcing + cascade only); (4) P-A1
4,662-sentence correction (replay verified FORCING; the 4,662 are
core>=k+1 CROSS pairs — evidence cores exceed k) + group-C kappa = k
scoping line; (5) smallcore route-of-record + criterion-3 re-scope;
(6) quotient-router R2 addendum (sub-core, >= k routing); (7) P-B scope
addendum (field hypothesis NECESSARY; consumption gate IS a q-floor;
RowC 1/4 window VACUOUS V1 — the ratified recorded obligation
DISCHARGED; residual = adversarial planting); (8) clean_residual
"removes" -> "classifies" + second unproved contribution; (9) WP7
bookends, F5-OS quantifier, WAVE5/WAVE20/BRIEF3_DOSSIER dated
corrections (BRIEF_3 + target_mappings.json left as-is — their wordings
remain TRUE under Route T since P-A1 is unchanged; adjudication
recorded); (10) THEOREM Y coordinator amendment appended to
band_adjudication REPORT (caveats 1-2 closed at j=1; j>=2 inherits the
gate inequality; set/cardinality claims separated); (11)
notes/BAND_LANE_DEFINITIONS.md — the 10 ratified definitions + per-ray
accounting + the occupancy heart (items 11-12); (12) NEW TARGET
xr_graded_tangent_band_charge (third generic column <= 4n^3, cascade
tier named, occupancy lemma = single open input, escape-form heart)
with 3 ev in + req out to xr_smallcore_spread_count.

CENSUS: +1 critical red — math orbit 242 = 179/38/25 (was 241 =
179/38/24); dag-wide 1747 nodes / 4842 edges, TARGET 76. Manifest
refreshed; lane verifiers PASS. Remaining mint wave (band-ledger
T3/T4/T5/T7, occupancy T1/T2/T4, Theorem G, Theorem 5/BP merge, KEY
LEMMA + pencil mass identity, MC family, L1 + design ceiling + block
dichotomy, S4 pack, antipodal lemma + parity-defect certificate) ->
delegated to a band-mint-prep Opus pilot for coordinator line-audit
(same pattern as the norm-gate mint). Next: (d) roadmap r3.

---

## EXPORT FALLBACK EXECUTED (user-authorized 2026-08-02)

PR #1143 (przchojecki/rs-mca) updated at 02d2788f: the complete positive
433-1a route exclusion exported as aggregation note + self-contained
fail-closed verifier + canonical certificate; workboard addendum; 433-1b
recorded majority-closed AT THE AUDIT PIN 454159b0 only (cell-14 unit
chart open; the post-pin d5671b339 denominator-boundary work NOT claimed
— wave-42 audit first). Clean-checkout verification: the aggregate
node's verifier replayed PASS in our canonical public checkout
(rs-mca-prize-dag @ 2f7604fc) before packaging; the exported verifier
passes locally under ramguard. Maintainer comment posted
(#issuecomment-5159932119). The kb_m2_r4 export directive (m2 collision
memory, package-by-2026-08-02) is thereby SATISFIED. Diagonal-node
export still HELD (collision surface with Scott's #1139, no response —
unchanged watch). PR #174 unchanged, awaiting triage.

---

## BAND-LANE MINT LINE-AUDIT + WIRE — COMPLETE (6 nodes)

Pilot drafts (99/99 checks) line-audited per AUDIT_CHECKLIST; all flags
adjudicated:

- **F0.j HAND-VERIFIED** (the wave's only pilot-plus-inference): g | j,
  j >= 1 gives j >= g = h-d against j <= M-1 = d-1, so 2d >= h+1 — the
  live shift class sits inside T2(b)'s reach; the dichotomy ->
  quantization req edge is sound. Claims 1-3 of package 3 checked line
  by line (coset-intersection bound; M | k two-power argument + unique
  2-power window; the zeta_P(i) = -x_i^j fibre/parity exclusion).
- **F0.f HAND-VERIFIED**: the capped escape floor — rank = Vh - dim Rel
  with Rel embedded in (+)C_{S_a^inf}; h - (|S_a^inf|-k)^+ =
  |S_a \ S_a^inf| when |S_a^inf| >= k, caps at h below; the K_V
  falsification of the uncapped form is the verifier's witness.
- **Package 4's reconstructed MC-1/MC-2 derivation LINE-AUDITED**: all
  three coefficient extractions traced index-by-index (ceiling c = 0;
  product condition e_{r'}(T) = gamma; s-window e_s = 0) — correct;
  converse rides the exhaustive three-field census.
- **Package 6 hand-checks**: S4-1 pointwise 0-or->=3; S4-3 inversion +
  (T); S4-4 Segre/(1,1)/cross-ratio; S4-14 MDS sum induction with the
  finite-slope pi_1 caveat present; Claim 7 explicitly
  MEASURED-NOT-PROVED.
- **Cross-cutting greps clean**: no "cascade event" survivors; the two
  sunflower variants named distinctly; per-ray/per-datum/free
  denominators straight; slope-keyed reading marked FALSE; no
  "arbitrarily lossy" survivors.
- **Adjudications**: F0.a CONFIRMED (true source = list_bound_transfer;
  brief mis-cited); F0.b Lemma 0 stays INLINE in the cost theorem;
  F0.c seventh node (unified fibre strip T1/T2/T4) NOT commissioned —
  stays flagged + QUEUED; F0.e/F0.i readings accepted (machine-checked,
  statements pin the distinctions); F0.g consistency-check status
  recorded in the node itself. Optional ev edge KEPT; the
  common_code_line_budget differentiation ref KEPT.
- **Pilot compute-law lapse recorded** (~8 bare-python3 read-only JSON
  inspections during triage; no computation of record affected — every
  pin re-derived inside ramguarded verifiers). Standing reminder goes
  into future pilot briefs.

WIRED: 6 PROVED background nodes; 5 internal req + 5 banked req + 2 ref
+ 6 ev into xr_graded_tangent_band_charge (red-leaf law verified in
script). DAG: 1753 nodes / 4860 edges; manifest scripts=2353,
proof_assets=2487; 6/6 verifiers PASS in place. No status flips; the
TARGET's reduction-of-record sentences now each have a PROVED evidence
node behind them. Mint queue remainder: F2 antipodal lemma +
parity-defect certificate, P-B L1 + design ceiling + block dichotomy
(second mint-prep pilot when scheduled); the seventh-node candidate.

## 2026-08-03: cell-14 closure export + round-7 pilot launch

- **EXPORT EXECUTED (#1143, commit b1489664):** wave-42 kernel-boundary +
  wave-43 CELL-14 COMPLETE CLOSURE packaged as one packet
  (`kb_mca_v4_m2_r4_coordinate_positive_433_1b_cell14_complete_closure_v1`:
  note + canonical certificate + self-contained fail-closed verifier
  replayed PASS in the export checkout + atlas status addendum +
  agents-log entry). Claims scoped to audited pins 7cbedd5d/db970533,
  deployed-prime exact, explicit nonclaims. Maintainer comment posted
  (issuecomment-5164524383). User authorization: "lets package it, and
  push if ready" (2026-08-03).
- **ROUND-7 PILOTS LAUNCHED (3 Opus, background):**
  (1) k_escape_unification — the recorded round-6 anchor: unify |K|
  (P-A1 un-peelable residual) with the band escape residual;
  (2) mint2_prep — the recorded MINT REMAINDER: F2 antipodal +
  parity-defect cert, P-B L1 + design ceiling + block dichotomy
  (drafts only, honesty-gated);
  (3) zero_escape_collapse — the band heart's open sub-items: prove
  rank = 2m for zero-escape cliques (duality route pre-briefed) +
  V <= m/2. All three write only under notes/pilots_20260803/;
  coordinator line-audit gates any wiring.

## 2026-08-03: round-7 pilot 1/3 BANKED — |K|-escape unification

- **k_escape_unification (Opus) AUDITED + BANKED** (FABLE_AUDIT.md in
  the pilot dir; coordinator replay 18/18, all 7 pre-registered
  falsifiers survived; U1-U5 hand-verified). Verdict: UNIFIED as one
  operator — both residuals are the (3, k+1)-core of the ray/point
  incidence; the band escape residual is its FIRST ITERATE (U1: the
  no-death peel is one-pass), P-A1's |K| its greatest fixed point (U2)
  — SEPARATED as sets (explicit (T)-clean fixture: heart hypothesis
  fails, conclusion holds via the core; escape floor 8 < kernel floor
  10 = rank). KERNEL FLOOR (U3) dominates the escape floor (U4);
  heart relaxed to the strictly weaker U5 core form. Node-local
  addenda applied (support4 statement, definitions item 12', TARGET
  factual pointer). Conditional first ceiling on |K| recorded
  (Gamma_0 <= (2R-1)/2 — conditional, not banked). NEW OPEN: escape-1
  gate-clean realizability (flag 5). SURFACED: re-pose the heart in U5
  form; commission escape-1 as an anchor. Pilots 2/3 (mint2_prep,
  zero_escape_collapse) still running.

## 2026-08-03: round-7 pilot 2/3 BANKED — zero-escape collapse REFUTED

- **zero_escape_collapse (Opus) AUDITED + BANKED** (FABLE_AUDIT.md;
  coordinator replay 26/26; PREREG confirmed — X1 and its exact rank
  predicted BEFORE computation, falsifiers P1-P7 all as registered).
  BOTH named open sub-items REFUTED: the collapse (gate-clean X1/X2/X3
  from four pencil fibres + one cross-ratio equation, deficits 1/1/2)
  and V <= m/2 (X1, X3). Measurement reconciled, not contradicted:
  slope sweeps at fixed supports are blind to the support-locus
  obstruction; measured fixtures' collapses UPGRADED to theorems
  (MDS-chain + triple-cover criteria; band-mint (3,5,3,5) by Cor 3c).
  HEART SURVIVES: Prop 6 proves charge >= 2 through escape-0 at V=4.
  Remaining channels: V >= 5 zero-escape below Cor-3b threshold;
  escape-1. New proved tools: duality criterion, V=4 cross-ratio
  classification (dual of S4-4), floor rank >= m + dim Sum C_{I_ab}.
  RowC toy-row kill re-opened (Theorem 3 misses by 3). Addenda applied
  (support4 addendum 2, definitions addendum 2, TARGET note); REPORT.md
  persisted by coordinator (pilot's write harness-blocked). SURFACED:
  commission V >= 5 occupancy + escape-1 realizability as the next two
  anchors; RowC re-derivation queued. Pilot 3/3 (mint2_prep) running.

## 2026-08-03: round-7 pilot 3/3 BANKED — mint-2 wired (4 nodes)

- **mint2_prep (Opus) AUDITED + WIRED** (FABLE_AUDIT.md; 37/37 replayed;
  both reconstructed proofs hand-verified line by line). Wired:
  f2_antipodal_descent_lemma, f2_parity_defect_certificate (standalone
  pair + campaign ref to u2c), pb_design_ceiling, pb_block_dichotomy
  (ev x2 into xr_lowcore_spread_heart; req from the banked cost
  theorem). pb_l1_lemma REFUSED as banked duplicate (accepted).
  Three corrections adopted: parity-defect scope a_c b_c != 0 (record
  too broad by 2(p-1) frequencies); spread<=>transverse one-directional
  (gap = core-K = Gamma_hi); design ceiling NOT unconditional (mu_20
  witness) -> dated addendum applied to xr_two_slope_cost_theorem.
  Free-slope ceiling demoted to non-claim; block-dichotomy hypothesis
  corrected to b >= a+2; e-coordinate reading adopted. DAG 1768/4906.
  ROUND 7 COMPLETE: 3/3 pilots banked (unification, refutation, mint).
  Round-8 pilots (v5_occupancy + escape1_realizability) RUNNING.

## 2026-08-03: round-8 pilot 1/2 BANKED — channel (i) DECIDED (2V <= 3h)

- **v5_occupancy (Opus) AUDITED + BANKED** (FABLE_AUDIT.md; replay
  67/67; PREREG Q1-Q12 all as registered; class arithmetic + LEMMA 1 +
  THEOREM B embedding + trichotomy + Y1 + RowC identification
  hand-verified). Channel (i) DECIDED: charge >= 2 iff 2V <= 3h
  (proved tight floor rank >= 3h, V-independent ceiling 2m = 2(t+h));
  collapse dead at EVERY V >= 4 (pencil fibres + Mobius,
  dim Ann = 2t-h); CLOSED at the prize rows (~1e8 margin, proved
  floor); RowC toy rows provably fail the channel — task #33 RESOLVED:
  kill unrestorable shape-only (Y5 rank 15 vs Y6 rank 18, same
  recorded invariants). BONUS CATCH: banked k <= 2h^2 criterion
  REFUTED (ceiling-as-lower-bound error; Y1 witness) — replaced by
  2V <= 3h; no prize-row number moves. Addenda: support-4 addendum 3,
  definitions addendum 4, TARGET note. Sole remaining heart channel:
  escape-1 (pilot 2/2 running).

## 2026-08-03: round-8 pilot 2/2 BANKED — channel (ii) resolved; ROUND 8 COMPLETE

- **escape1_realizability (Opus) AUDITED + BANKED** (FABLE_AUDIT.md;
  replay 113/113, 0/12 falsifiers fired, PREREG pre-dated). Channel
  (ii): escape-1 core rays EXIST gate-clean (flag 5 affirmative; E1
  all-escape-1 family, V >= 3h forced by LEMMA ALL-1); ONE escape-1
  ray never defeats charge 2 (3-DROP FLOOR, tight on U-mechanism,
  predicts its deficit); defeat needs n_1 >= 3h-2; every constructed
  counterexample band-INADMISSIBLE (LEMMA R: rank <= 2m-1 necessary).
  CROSS-CHANNEL CATCH: Zfib11 (zero-escape pencil at V=11) passes the
  FULL gate, realises with exact-A agreements, charge 0.818 — fires
  the TARGET's own channel-(i) + V>m/2 falsifiers; the charge-2 route
  is FALSE as a universal for admissible systems; survives at prize
  rows (2V <= 3h by ~1e8). Reconciled: Zfib11 IS the v5 pencil family
  (identity Mobius), consistent with the trichotomy and with U5.
  Occupancy conclusion + column bound untouched (N_d = 0.11 n^2).
  New floors of record: THEOREM D (3-drop), LEMMA R, LEMMA A (h>=3),
  LEMMA B (|K| = 0 or >= 4). Addenda: definitions #5, TARGET note.
  NEXT ANCHORS (surfaced): consolidate the general-V admissible case
  at prize rows under the four floors; the sharp E1-family deficit
  question; the m >= 9 full-gate oracle (COMPUTE REQUEST).

## 2026-08-03: CONSOLIDATION (task #34) — the heart's open surface is now three named lemmas

- Coordinator derivation, ratified; note + machine-checked arithmetic
  at notes/band_heart_consolidation_20260803/. NEW: CORE-DISJOINTNESS
  LEMMA (depth-d cores pairwise <= k-1 under (T); each core >= k+1
  forces the KEY-LEMMA joint-explanation event). NEGATIVE FINDING
  (machine-checked): even granting L-A (pencil rigidity e >= 2) and
  L-B (escape-1 over-agreement), the ray/pair lens gives 0.78-2.12 n^2
  > 0.68 n^2 at every row — the charge route is retired as primary.
  ROUTE OF RECORD -> count CORES: L-D = "depth-d joint-explanation
  cores with L_P >= 2 number <= 0.68 n^2" (subsumes L-A/L-B; consumes
  only banked machinery; calibration U-mechanism N_1 ~ n/2, >1000x
  headroom). Open surface after consolidation: exactly {L-D primary;
  L-A, L-B fallbacks}. Next pilot anchor: L-D dimension count.

## 2026-08-03: round-9 pilot 1/3 BANKED — L-D refuted-as-worded; route already banked; consolidation CORRECTED

- **ld_core_count (Opus) AUDITED + BANKED.** L-D as worded REFUTED
  (raw-subset explosion; fixture 334 > 272; prize rows 2^6.4e10 vs
  2^81.4); L filter powerless (monotone under subsets); intended
  maximal reading = the ledger's N_d, whose route was banked and
  TERMINATED 2026-08-02 in xr_band_occupancy (THM 2/4 + PROP 5
  slope-side no-go). COORDINATOR ERROR acknowledged: the consolidation
  mis-worded L-D, misapplied core-disjointness, and failed to subtract
  against xr_band_occupancy — CORRECTION block applied. RowC rows
  vacuous for 0.68n^2 (prize rows only bind). Open surface of record:
  RS list-size at tau = k+ceil(h/2) (positive target #1 species);
  L-A/L-B supporting but provably insufficient (PROP 5; V* = 1.166n
  vs 1.25n granted). Pilots 2/3 (L-A, L-B) still running.

## 2026-08-03: round-9 pilot 2/3 BANKED — L-B partial; L-A => L-B adopted

- **lb_escape1_overagreement (Opus) AUDITED + BANKED** (237/237;
  LB-F2 fired as pre-registered). V_1 = 0 PROVED on the
  group-fibre/block class (THEOREM F: 3 fibre rays pin Ann, quadratic
  in c_a; E1P 520-sample phenomenon -> THEOREM, extra point = the
  removed point 12/12); mechanism REFUTED (mult-2 escaped points sit
  at exactly A; only private points force over-agreement); DICHOTOMY
  = exact pointwise criterion; L-A => L-B ADOPTED, L-B dropped as
  independent target. Flag-6 explained (4-wise < k+2 forbids
  support-4 deficits; support >= 5 = named attack surface). Open
  surface: RS list-size terminus + L-A. Pilot 3/3 (L-A) running.

## 2026-08-03: round-9 pilot 3/3 BANKED — ROUND 9 COMPLETE; the heart = list-size + one sliver

- **la_pencil_rigidity (Opus) AUDITED + BANKED** (30/30; FA fired as
  pre-registered). L-A REFUTED as stated (W1/W2: V=4 non-pencil
  zero-escape non-collapsing, the Z-escape and dim-G escape both
  real); L-A' adopted (V >= 5 pencil up to one block, residual
  named); CONSUMER PROVED WITHOUT THE PENCIL (D1: V=4 disjointness
  forced; D2/D3: e <= 2 and t = 2 closed). ROUND-9 NET SURFACE:
  (1) RS list-size at tau = k+ceil(h/2) (primary, positive target #1
  species); (2) the overlap sliver (e >= 3, V >= 5 overlapping
  zero-escape; carries L-B residual). Consolidation UPDATE 3 = final.
  Candidate next anchors: the sliver (toy-attackable); support >= 5
  all-escape-1 deficits (L-B flag); the list-size problem itself
  (Pro-brief-scale, or Codex lane).

## 2026-08-03: ROUND 10 LAUNCHED — 4 Opus pilots, non-overlapping

- (1) maelcar_audit: literature-map audit of upstream #1145-#1148
  (gates our L1 + LIST/M31 moves; read-only gh access; subtraction
  both ways). (2) overlap_sliver: the last ray-side configuration
  (overlapping zero-escape, e >= 3, V >= 5; admissibility-kill route
  first; carries L-B residual). (3) support5_deficit: all-escape-1
  dim Ann >= 1 existence (support-5 relation classification; decisive
  smallest-shape sweep). (4) listsize_program: the PRIMARY terminus —
  structured attack on RS list size at tau = k+ceil(h/2) (min-over-z
  averaging via THEOREM I; obstruction map; ranked sub-lemmas).
  Explicit-path commits while running.

## 2026-08-03: round-10 pilot 1/4 BANKED — stale terminus caught; surface corrected

- **listsize_program (Opus) AUDITED + BANKED** (3/3 verifiers PASS).
  ADJUDICATION: the assigned RS list-size terminus was refuted
  2026-08-02 and stale-propagated by CONSOLIDATION UPDATE 3 + the L-D
  audit (second fifth-surface failure — rule sharpened: same-day grep
  before handing anchors to pilots). Pilot re-derived the refutation
  independently (margins match banked verbatim), proved the SHADOW
  LEMMA (min-over-members worth 256 bits vs ~1e12 deficit; refutation
  structural + selection-insensitive), localised the occupancy
  lemma's survival to ONE depth (h-1, BP parity, h odd), and priced
  the averaging ledger dead. CORRECTED SURFACE: un-reduced two-slope
  band occupancy at band-proper high depths; SL-1 windowed projection
  (unifies with L-B; next anchor), SL-2 Pro-brief, SL-3 diagnostic.
  UPDATE 4 applied. Pilots 2-4 running.

## 2026-08-03: round-10 pilot 2/4 BANKED — maelcar audit: no collisions; SOL_TARGET_4 at risk

- **maelcar_audit (Opus) BANKED.** #1145/#1146 L1: verified/plausible-
  unreplayed, cite-with-scope (S6 <= 20 only on 2/252 supports);
  #1147 Paper-D: VERIFIED strongest (counterexample replayed
  independently, T_sm = 22476 / max K = 26 exact); #1148 M31 hull:
  route cuts verified, DOMINATED in applicability by our chamber
  fence. Zero collisions/exposure both ways. T4 <-> T_sm bridge
  proved at (32,97) and adopted. HIGH: SOL_TARGET_4 as stated lacks a
  q-vs-N hypothesis and their admissible n=128 row gives T4/N^3 =
  2.87, exponent ~N^5.6 at bounded index — reprice-or-expect-
  falsification SURFACED; decisive N=256 q=769 run = COMPUTE REQUEST.

## 2026-08-03: round-10 pilot 3/4 BANKED — all-escape-1 deficits EXIST; prize rows still protected

- **support5_deficit (Opus) BANKED** (168/168 --full; 0/17 falsifiers;
  PREREG amendment A1 honest). EXISTS: E1-PENCIL construction
  (dim Ann = 2s-h+1, whole gate window; exhaustive 680,400-case
  classification at smallest shape, deficit iff pencil+Mobius); PF3 =
  the record's E1 pin (charge 1.75); PF1 FULL-GATE with escape-1 rays
  live at exactly A; PROP 0 (private points give deficits free).
  THEOREM D now TIGHT. Five upstream corrections adopted (escape-1
  implication 4; flag-6 dissolved -> support-4; LEMMA R mult>=2
  hypothesis explicit; support-4 addendum 4). RECONCILIATION: every
  charge defeat obeys n_1 >= 3h-2 (PF2 exactly at threshold) — PRIZE
  ROWS REMAIN PROTECTED arithmetically; the structural-exclusion hope
  is dead at toy scale. PF2/PF3 full gate = standing COMPUTE REQUEST.
  Pilot 4/4 (overlap_sliver) running.

## 2026-08-03: round-10 pilot 4/4 BANKED — sliver CLOSED; ROUND 10 COMPLETE; ray side FINISHED

- **overlap_sliver (Opus) BANKED** (33/33; OS2 fired as predicted).
  V <= |U| <= n PROVED (Fisher, self-contained, sharp at PG(2,3));
  literal n/2 phrasing refuted (third coordinator wording defect —
  anchor rule extended: bounds stated AT THE ROWS); |U|/n <= 0.2588
  at all six rows serves the consumer everywhere, L-B residual
  covered; O1 subsumes D2+D3; CONJECTURE OV open (exhaustive toy
  support, up to 2.96e12 tuples). RAY SIDE FINISHED. Open surface:
  SL-1, SL-2, OV. DECISION STACK: SOL_TARGET_4 reprice (#36); SL-2
  Pro brief; SL-1 pilot; PF2/PF3 + N=256 compute requests.

## 2026-08-03: Modal run 1 DECIDED — PF2 full-gate PASS (charge 1.9), PF3 gate-killed

- Coordinator Modal run (ap-OtZPijv1jV2rWFhllPZUn2, < $1): PF2 is the
  first FULL-GATE admissible charge-defeating all-escape-1 fixture
  (all 30 slopes capped at A; n_1 = 3h-2 exactly); PF3 (E1 pin) fails
  the gate through its own designed slope 10 (forced over-agreement).
  Channel (ii) realised with charge < 2 under every gate at toy
  scale; prize-row protection (n_1 >= 3h-2) certified sufficient and
  sole. Result JSON + sha pinned. SOL_TARGET_4 N=256 run in flight.

## 2026-08-03: Modal run 2 DECIDED — SOL_TARGET_4 FALSIFIED as stated

- Coordinator Modal run (ap-sx9plNuGHtzGtGYisoYrh0, ~$1): T_4/N^3 =
  103.07 at the fully admissible (N,q) = (256,257) index-1 row
  (mechanism: pigeonhole into q^3 keys, ratio ~ N^2/576, unbounded);
  index-3 row still rising (3.78 at N=256 vs 2.87 at N=128). The
  maelcar-audit HIGH flag is CONFIRMED at the strongest level; task
  #36 closed as FALSIFIED; index-hypothesis reprice surfaced (C as a
  decreasing function of index = (q-1)/N). Result JSON + sha pinned.

## 2026-08-03: ROUND 11 LAUNCHED — the unification round (3 Opus + gamma close in flight)

- (1) unified_pencil_bound: the anchor — full-gate admissible pairs
  admit <= Cn live pencil-structured slopes (THEOREM F pinning across
  pencils; PF2/Zfib11 calibration; multi-pencil compatibility).
  (2) sl1_windowed_projection: band-proper pairs project at <= A-2
  (the THEOREM 2 windowed upgrade; Psi_y machinery adapted to pairs;
  MC saved-by-cascade check). (3) crosslane_cashout: best
  unconditional |K| bound at the rows from the new floors + the
  realised-family replacement ceiling for P-B + the selector/
  dichotomy identification. Plus gamma_j2_close (heart 7) still
  running from earlier. Explicit-path commits while pilots run.

## 2026-08-03: round-11 pilot 1 BANKED — SL-1 decided; the windowed route reopens

- **sl1_windowed_projection (Opus, retry honoring killed-run PREREG)
  BANKED** (297 + 34 replayed, 0 failures). "Every member" FALSE
  (forced at d = h-2, unconditional — the ONE exposed depth); "some
  member" TRUE gate-free (>= q+1-(n-k-d) clean members); WINDOWED
  THEOREM 2 survives (min over clean members; 127.7-bit margin at the
  prize rows; loss < 2^-73 worst case). THEOREM F: MC spectrally
  excluded from the window — three exhaustive cases, middle = the
  2-adic gap (band proper strictly between consecutive 2-powers at
  h = 2^m + 1). THEOREM U: SL-1 = L-B functionals via pencil
  pullback — the selection leg of the unification is now a THEOREM.
  Occupancy surface reduces to SL-2 alone (+ OV cleanup). h-even
  fragility recorded. Remaining round-11 pilots in flight.

## 2026-08-03: round-11 pilot 2 BANKED — cash-out: |K| residual = OV; P-B monomial forcing

- **crosslane_cashout (Opus, retry) BANKED** (152/152, 3 falsifiers
  fired-and-reported). NEW: |K_+| <= 2t-h+2 (tight, U-mech); Jensen
  K_0 window bound = banked sunflower values (130/66/66 at prize vs
  targets 383/447/959); THE |K| RESIDUAL IS ONE OBJECT = the band
  lane's CONJECTURE OV (U2's prediction confirmed — OV now pays BOTH
  lanes); THEOREM X monomial forcing (exhaustive) + THEOREM Y sharp
  orbit ceiling M = n (free orbits at all six rows); selector vs L-B
  = different-but-complementary, K1/PP4.0 de-coupling route SURFACED.
  Addenda applied to both P-B nodes. In flight: anchor, gamma close.

## 2026-08-03: round-11 pilot 3 BANKED — anchor: C = 1/2 at e = 1; residual = F9

- **unified_pencil_bound (Opus, retry; killed-run PREREG honored)
  BANKED** (42/42 + both replay halves, 0/10 falsifiers; one in-run
  proxy retraction). PROVED: s >= 2 forced by the gates; C = 1/2 at
  e = 1 UNCONDITIONALLY for ALL live slopes (k-packing disjointness;
  tight at Zfib11 + a new local FULL-GATE q=11 witness); C = 1/2 per
  pencil at every e; M <= 1 pencils at e = 1 via Ann-monotone 3+3
  pinning (combinatorial M <= 1 is FALSE — 170 multi-pencil matchings
  — realisability is what kills them: 0/720 vs control 200/200).
  Residual = EXACTLY v5 flag F9. Unified mystery kernel: {SL-2, OV,
  F9}. Awaiting: gamma_j2_close (the last gate for the 7->4 board).

## 2026-08-03: round-11 pilot 4 BANKED — ROUND 11 COMPLETE; BOARD REVISED 7 -> 4 (task #37 executed)

- **gamma_j2_close (Opus, retry) BANKED** (9,415 checks 0 fail, 0/9
  falsifiers; e2/e3 coordinator-replayed). PARTIAL: THEOREM D
  unconditional reduction |Gamma_j| <= n.E_j (Y = E_1 = 1 case;
  mintable); scope theorem (all 18 counterexamples w = 2 < M, j >= w;
  prize rows j <= w-1, no gate-intact excess to X = 4.44); banked "X
  governs" corrected to necessary-not-sufficient; one-parameter
  averaging gap named as THE obstruction. Heart 7 NOT retired —
  residual = E_j, attached to the unified kernel. Amendment 2 applied
  to band_adjudication; advlib docstring fixed.
- **BOARD REVISION EXECUTED (r3.2)**: four mysteries — UNIFIED
  (kernel {SL-2, OV, F9, E_j} + P-B appendix), F2, C1/C2'', CROSSING.
  Task #37 complete. Next levers: OV pilot, F9 pilot, SL-2 Pro brief,
  E_j identification.

## 2026-08-03: ROUND 12 LAUNCHED — the kernel round (4 Opus on the r3.2 unified kernel)

- (1) ov_conjecture: overlap => collapse (shared-point forcing route
  first; PG(2,3) as extremal lemma; pays band cleanup + P-A1's |K|).
  (2) f9_pencil_forcing: ADJUDICATE-then-attack (W1/W2 may answer the
  literal F9 at V=4 — the anchor needs V >= 5 forcing = L-A residual;
  graceful-degradation fallback for C). (3) ej_coset_spread: bound
  E_j via window rigidity + THEOREM F's newly non-empty prize-shape
  range (w >> 2j); empirical law + falsifiers. (4) sl2_unstructured:
  the occupancy question in-house — non-coset window-system solution
  count + core-disjointness correlation cap; construction as the
  falsifier branch. Explicit-path commits while running.

## 2026-08-03: round-12 pilot 1/4 BANKED — SL-2: scope gap found AND closed; residual = SL-2-RES

- **sl2_unstructured (Opus) BANKED** (677 checks; 1 deliberately
  recorded PREREG mis-specification, corrected forms pass). CATCH:
  BP(1) scoped to M >= d only — sub-depth coset scales live in the
  band proper at the prize rows; CLOSED by THEOREM L (M <= cap_d
  from h-odd parity; M = 2^21..2^31 unconditional) + first-moment
  margins on small M. NEW: LEMMA W (cores = divisors of X^n - 1 on a
  codim-2d affine subspace), THEOREM D (descent bijection; settles
  "syndromes descend"), THEOREM R (full Toeplitz rank via B-M).
  RESIDUAL = SL-2-RES: the aperiodic divisor-count statement (h odd +
  q >= 2^209 load-bearing). Addendum applied to
  xr_mc_depth_quantization; xr_window_system_descent mint QUEUED;
  SL-2-RES = the Pro brief when Pro resumes. Pilots OV/F9/E_j running.

### Codex correction to SL-2-RES currency (2026-08-03)

The phrase "monic degree-r' divisors on a codimension-2d affine
subspace" is not the exact occupancy endpoint. W counts raw
interpolation subsets; a maximal depth-e pair contributes
`C(k+e,k+d)` raw depth-d locators. R proves each single-word rank is d,
not that the stacked rank is 2d. The corrected target is the maximal,
selected, post-strip locator count in
`xr_band_maximal_window_divisor_count`; it retains small-scale
mixed-class systems. The W/D/R/L theorems remain banked unchanged.

## 2026-08-03: WAVE 45 (v11 math half) INTEGRATED — CELL 3 + CELL 6 CLOSED; round-12 pilot 2/4 (E_j) BANKED

- WAVE 45: 23 nodes + 85 edges (dag 1793/4995); cell 3 closed
  1680/1680 (DE 6-14 + xi3 x6 + xi4 transport + xi5 + xi6); cell 6 =
  duplicate-role transport, closed; cell 4 opens (four-basis tower).
  Atlas: 1a complete; 1b cells 0, 1/2, 3, 6, 14 closed. Refactor
  commit held for stage-2 review. Self-catch: roadmap adoption
  clobbered r3.2 — restored same-turn; both-directions rule adopted.
- **ej_coset_spread (Opus) BANKED** (4,744,495 checks, 2 failures =
  the pre-registered falsifier killing the pilot's own post-hoc
  hypothesis — flagged honest). E_j <= 29.6n NOT proved; REPRICING:
  THEOREM G (mu_g action; at prize rows E_j = |Gamma_j|/n within 9
  bits — THEOREM D is a re-coordinatisation, NOT a shrink; heart 7's
  residual pricing corrected in r3.2); THEOREM H (rigidity sharpened
  to d <= (j-1)+gcd(j,n); d <= 1 vs structured at gcd(j,n)=1 = the
  prize regime; 25.9M-candidate exhaustive d-ball verification);
  empirical law E_j = 1 on ALL 152 gate-intact j<w rows (every
  E_j >= 2 at j<w is gate-broken — 46 bits better than needed,
  unproved); species identification UPGRADED to an explicit
  Fourier-prescription reduction; named next-fixture for the live
  excess test (n=35,k=10,w=M=5,q=71, C(n,A)=4.06e9 — COMPUTE
  REQUEST scale). OV + F9 pilots still running.

## 2026-08-03: round-12 pilot 3/4 BANKED — F9 adjudicated + T0 PROVED; C = 1/2 stands

- **f9_pencil_forcing (Opus) BANKED** (39/39; PREREG incl. the full
  construction pre-dated; honest in-run check correction). Literal F9
  CLOSED-YES at V=4 (W1/W2); T2/T1 REFUTED (18 fixtures — la's FB
  fired at Delta = 0, its V >= 5 evidence void, its theorems intact);
  T0 (the anchor-exact statement) PROVED via LEMMAS 2-5 + P-SHARE
  (distinct pencils share <= 1 fibre — NEW, sharpens Q5, keeps the
  pinning out of V=4); residual = the t <= 2e-3 band (includes prize
  shapes; 54+12 complete sweeps find zero there; dim G = 1 in all 134
  non-collapsing systems). C = 1/2 UNCHANGED. Addenda applied to la +
  unified audits. KERNEL NOW: {SL-2-RES, OV, T0-residual, E_j}.
  OV pilot still running.

## 2026-08-03: round-12 pilot 4/4 BANKED — ROUND 12 COMPLETE; the kernel in sharpest form

- **ov_conjecture (Opus) BANKED** (22/22; OV1-OV8 pre-registered,
  none fired). OV OPEN but REDUCED slope-free: Jperp = 0 (THEOREM 2;
  the sliver's slope evidence re-labeled wrong-space); THEOREM 1
  dictionary explains the sibling wall (gates = always-independent
  pairs + always-dependent triples); THEOREM 5 proves the r = d
  branch incl. PG(2,3) (shared-point forcing); residual = r > d
  (s=1 telescoping cocycle = named next attack); consumers correctly
  still blocked. ROUND-12 NET: kernel = {SL-2-RES, Jperp = 0 (r > d),
  T0-residual (t <= 2e-3), E_j/Fourier} — every item sharpest-form
  with named next attacks. MINT QUEUE (5 packages):
  xr_window_system_descent, gamma THEOREM D, T0+P-SHARE, OV THEOREM
  2/5, E_j THEOREM G/H.

## 2026-08-03: MINT-3 line-audited — 2 wired, 1 held; mint-4 queue set

- mint3_prep: 3 drafts (42/42, three checks STRONGER than sources);
  gamma/E_j package refused (banked wording + unaudited G/H —
  endorsed; the missing ej FABLE_AUDIT debt paid); LEMMA W downgraded
  to counting_frame attribution. WIRED: xr_pencil_forcing_t0 +
  xr_ov_slope_free_reduction (dag 1795/4998; census unchanged; all
  verifiers green; OV REPORT persisted pre-wiring). HELD:
  xr_window_system_descent (THEOREM L reconstructed-with-gaps; W/D/L/R
  need fresh coordinator line-audit). MINT-4 QUEUE: window-descent
  line-audit + THEOREM D (3-drop) + UPB. Then: stage-2 refactor
  review; export batch (cells 3/6/14); next Codex wave.

## 2026-08-04: STAGE-2 DAG REFACTOR ADOPTED (task #38 complete)

- All three gates PASSED and the design is INVERTED-but-sound: the
  node-local manifests (node.json per node dir) are the SOURCE; dag.json
  is the COMPILED compatibility artifact; verify_prize_dag now fails
  closed on any mismatch; compile_dag.py is deterministic (byte-for-byte
  for migrated records, deterministic append for new). Edge-ownership
  rule (one writer per edge: consumer owns req/alt, supplier owns
  ev/ref-as-refutes) adopted — ends three-agent dag merge conflicts.
- ADOPTION MECHANICS: merged codex-v11w with -X ours; caught the compile
  overwriting our dag with THEIR shard set (missing our 2 mint-3 nodes +
  3 edges) — restored, reconciled shards to OUR truth (no stale shards;
  their generation already carried the re-pose), recompiled:
  CONTENT-EQUAL assert passed (1795/4998). Roadmap + compute-requests are
  now SECTIONED documents (sections = source, monolith compiled); our
  r3.2 board revision migrated to notes/roadmap/sections/12-*.md.
  Full chain green: DAG_MANIFEST / prize_dag / census / sharded-result /
  sectioned-documents / manifest (refreshed).
- NEW WRITE-PATH OF RECORD: coordinator edits write node.json shards
  (+ sections for the two sectioned docs), then compile_dag.py --write +
  compile_sectioned_documents.py --write, then the verify chain. dag.json
  and the monolithic docs are NEVER hand-edited again. Wire scripts to be
  ported next mint; wave protocol: shards regenerate locally, never
  bulk-checked-out.

## 2026-08-04: WAVE 46 INTEGRATED — THE BAND FLIP (TARGET -> CONDITIONAL on SL-2 alone)

- 22 nodes + 72 edges (dag 1817/5070); census 246 = 179/41/26. Codex
  minted our rounds-7-12 structure (SL-1 reduction PROVED; their own
  sound window-descent proof supersedes our held draft; SL-2 as the
  single conditional leaf; SL-2-RES split into two sharper reds; 13
  deficient-window payments). H_band exact-budget correction accepted.
  First worker-initiated critical status flip — audited SOUND. Site +
  artifact refresh (census changed). See WAVE46_AUDIT.md.

## 2026-08-04: AUDIT FREEZE (user-ratified)

Integration freeze pending the upstream-sync wiring and stocktake:
- FROZEN PINS: Codex = 88238fd0 (wave 46, the band flip; worker
  continues in parallel — its new waves QUEUE, not integrate);
  upstream = the 2026-08-04 PR state (#1149 head; new PRs queue);
  ours = b2acdc98+ lineage.
- IN FLIGHT: upstream_sync pilot (SYNC_PROPOSAL.md) — on return:
  coordinator line-audit, wire trust-labeled addenda via the shard
  write-path, push.
- THEN: full stocktake + next-move plan (surfaced to the user before
  unfreezing).

## 2026-08-04: MOVE 1 SHIPPED — the diagonal six-cell export (1646bbba); THE DIAGONAL HOLD IS LIFTED

- Third #1143 batch pushed + maintainer comment
  (issuecomment-5203979880): the aligned-positive-unramified six-cell
  block closed 6/6, correspondence with Scott's in-flight atlas
  labeled PROBABLE NOT ESTABLISHED (mapping row offered as a
  request); replay honesty verbatim (11/15 exact FLINT PASS, 4
  per-stage-cap timeouts recorded). The 2026-08-01 diagonal-node
  export HOLD is formally LIFTED (its premise died at #1149).
  Remaining export queue: cells 3+6, band-flip narrative.

## 2026-08-04: round-13 pilot 1/2 BANKED — syzygy leaf NARROWED to (FR)

- **commonroot_syzygy (Opus) BANKED** (41,077 exact checks; P6 refuted
  as posed — the ladder is CAPPED, not open; brief-staleness
  adjudicated correctly against the coordinator). (WTB) proved; block
  budget X = 118/136 exact; NO-GO: s <= 11/11/10 for the entire
  incidence-counting family (X = 0 one dimension up, collapse = N/w);
  near-packed extension + the ell-size tail exception; residual
  boundary exhibited (~1e18 x X). THE LEAF'S OBLIGATION OF RECORD IS
  NOW **(FR)** (fiber rigidity: blocks = full phi-fibers + at most
  one point => beta <= 6t < X closes everything in range). Next
  anchors: (FR) pilot; the s >= 12 mechanism via the signed
  support-moment interface. Awaiting: fullrank_divisor_count pilot.

## 2026-08-04: round-13 pilot 2/2 BANKED — ROUND 13 COMPLETE; the two-leaf landscape mapped

- **fullrank_divisor_count (Opus) BANKED** (213 checks; 6 honest
  prediction corrections; P3 refuted — THEOREM SHIFT routes the
  recorded adversary to the sibling leaf). Dual Gr(2, n-k) form;
  route cut (full rank => no anti-concentration, witnessed in-scope);
  LEMMA X0 transversality; exact M = 2..2^20 survival region owned by
  this leaf; M^2-slack self-reduction (transfer gap flagged);
  aperiodic obstruction = sub-Johnson list size, all lenses
  equivalent. BAND PROMOTION now = (FR) + {transfer-gap + quotient
  count | aperiodic anti-concentration}. NEXT-ROUND CANDIDATES: (FR)
  pilot; transfer-gap check; approximate-shift boundary; s >= 12
  mechanism.

## 2026-08-04: ROUND 14 LAUNCHED — one pilot per mystery (the full-board round)

- (1) fr_fiber_rigidity: (FR) — mystery 1's highest-leverage
  conjecture (B-M forcing / selection-exchange / toy-decisive
  liveness routes; the ell-size tail exception carried as a
  constraint). (2) f2_opening: first dedicated F2 round — K1 mass
  obligations (O1)-(O3) obstruction map + exact small-rung
  E[exp S_c] + the T3 character-sum scoping verdict
  (internal/Burgess/beyond). (3) c1_sharpest_leaf: junction-0 lane
  map (norm-gate + wcl slots + C1-ZERO/SWIF-4) + attack the sharpest
  leaf + compute request if needed. (4) crossing_w2_opening: the
  FIRST crossing opening — the w >= 2 obligation verbatim, the
  q-dependence obstruction map, one proved partial, and the
  MERGE CHECK (is the crossing count a divisor-window count in
  disguise? LEMMA W is the same window system — a potential FIFTH
  dependency reduction, flagged prominently either way).
  Explicit-path commits while running.

## 2026-08-04: round-14 pilot 1/4 BANKED — crossing OPENED: 3 theorems + the shared terminal

- **crossing_w2_opening (Opus) BANKED** (152 checks; 3 honest
  recorded resolutions). LEMMA X (general-T equidistribution — all
  5.3e11 bracket w values vs MC-3's 6; PK2 reconciled); THEOREM Q
  (q-dependence = characteristic only, tower-invariant); LEMMA Y/MW
  (window LINEAR at every official razor row: w < p proved; crossing
  heart = constant-weight count in a length-2^41 cyclic code; MC
  window = coordinate subspace -> band route cut theorem-grade);
  q-free floor (12x over MC-3, no bite at 2-power n). MERGE: same
  counting problem, four blockers, ONE SHARED TERMINAL (mu_n
  anti-concentration = mysteries 1+4's common deepest question).
  Anchors A1-A8 (A5/A6 external-shaped; A7/A8 -> Codex). Awaiting:
  fr_fiber_rigidity, f2_opening, c1_sharpest_leaf.

## 2026-08-04: round-14 pilot 2/4 BANKED — C1/C2'' lane mapped; Delta route dead; A1 = the window-extension audit

- **c1_sharpest_leaf (Opus) BANKED.** Ten slot leaves, minimal set =
  all ten (zero-event forced); Delta certificate route DEAD at the
  smallest slot hence all (premise PROVED 61/61, size extrapolated
  4.4e8 bits vs 1e7 threshold — 44x margin); 8/10 leaves now
  routeless; census re-priced FEASIBLE at (1,5) (65-130 CPU-h,
  CR-W5-ELL1 filed, gated on A1); the +5 -> +7 window extension
  identified as the fault line — A1 (audit it) = the lane's next
  obligation. v_2-blindness banked as the structural law. Hygiene
  flags queued. Awaiting: fr_fiber_rigidity, f2_opening.

## 2026-08-04: round-14 pilot 3/4 BANKED — F2 OPENED AND MOSTLY DISCHARGED

- **f2_opening (Opus) BANKED** (V1-V12, 66 PASS; P1-P10 confirmed;
  two self-catches corrected openly). (O1)+(O2) discharged EXACTLY at
  rungs 1-13 (THEOREM A surjectivity: E[exp S_c] = 2^{n/2}, o(n)=0;
  brute-forced at p=5 over all frequencies); (O2) implied by (O1);
  (O3) exact (pullback as a POWER); LEMMA 3 necessary condition
  (7.89x margin — pin t, CATCH-4); T3-UNIFORM REFUTED (constructive;
  the lane's analytic-NT dependency REMOVED; T3 re-posed in measure =
  internal); the banked annealed drift closed exactly. REMAINING for
  mystery 2: SL-1 (rungs 14-16 power-sum relations) + SL-2 (the
  |K1| sum-vs-average seam, settle with PP5.0). Theorems queued
  mint-shaped for mint-4. Awaiting: fr_fiber_rigidity (4/4).

## 2026-08-04: round-14 pilot 4/4 BANKED — (FR) REFUTED -> (BC); ROUND 14 COMPLETE

- **fr_fiber_rigidity (Opus) BANKED** (47,111+ checks, 0 fail; FR-F1
  fired as pre-registered). (FR) refuted inside its intended domain
  (audited witness, gate exhausted-tight, exception not invoked;
  1,710/1,716 partitions violate; the 6 survivors = the packed case).
  SURVIVES: the counting consequence (|Bset| = 2 <= 6t empirically).
  NEW: the two-ray syzygy, self-fiber avoidance, the selection lens
  (census = punctured-RS list count), GATE-r — mint-shaped.
  OBLIGATION RE-POSED: **(BC)** block census (reuse = the unmeasured
  crux; Johnson-regime caveat = falsifier axis 1). Brief-staleness
  catch against the coordinator recorded (quote theorems verbatim).
  ROUND 14 COMPLETE — all four mysteries moved. Next-round board:
  (BC), A1, F2-SL-1, the shared mu_n terminal, mint-4.

## 2026-08-04: ROUND 15 LAUNCHED — the convergence round

- (1) bc_block_census: mystery 1's (BC) — the reuse law (the
  unmeasured crux), the half-agreement list count via the selection
  lens, the Johnson-regime split axis. (2) a1_window_audit: mystery
  3's +5 -> +7 derivation audit (TIGHT/LOSSY/CONDITIONAL verdict +
  minimal-W arithmetic + the A2 overkill gap). (3) f2_sl1_powersums:
  mystery 2's rungs 14-16 — the ternary odd-power-sum minimum-weight
  law, with the CROSS-LANE BCH identification against the crossing
  pilot's LEMMA Y flagged (potential sixth reduction); pin t first
  (CATCH-4). (4) mun_anticoncentration: the SHARED TERMINAL of
  mysteries 1+4 — the unified constant-weight cyclic-code statement,
  the transfer inventory (sparse-zero-set weight distributions /
  Carlitz-Uchiyama at w-1 << p), the w = 2 exact case, and the
  internal/transfer/open verdict BEFORE paying for outside help.
  Standing rules: verbatim theorem quotes in briefs; explicit-path
  commits while running.

## 2026-08-04: round-15 pilot 1/4 BANKED — A1 verdict LOSSY; the W = 5 rollback SURFACED

- **a1_window_audit (Opus) BANKED** (7/7 controls). The +7 window is
  a +2 overshoot with NO derivation (ceiling-not-floor; numeral
  semantics collision; the only pro-argument used a retired
  instrument); W_min = 5 EXACT (the q = 918552577 w6-orbit binding
  inequality); the margin/slot curve plotted for the first time
  (+7 -> +8 buys zero); A2 gap 21.4x but STERILE. ROLLBACK SURFACED
  with coordinator recommendation RATIFY: board 10/8-routeless ->
  4/1-closable, consumer arithmetic bit-identical, costs are
  watch-line (margin 2.85x -> 2.30x). Awaiting: bc_block_census,
  f2_sl1_powersums, mun_anticoncentration.

## 2026-08-04: round-15 pilot 2/4 BANKED — (BC) refuted; THREE-WAY convergence on the mu_n terminal

- **bc_block_census (Opus) BANKED** (34,332 checks 0 fail; BC-F1a +
  BC-F6 fired as registered). (BC) refuted uniform (|Bset| = 2|Tau|
  admissible, exhaustive gates, both Johnson regimes); round-14
  |Bset| = 2 WITHDRAWN (pigeonhole margin exactly -(t-1)); route 2
  dead at rows (K/e = 55-112x); the ordered-pair form CIRCULAR
  (coordinator statement-defect #4). Honest residual = the OFF-D
  agreement count = THE mu_n TERMINAL — now consumed by band
  fullrank + crossing + syzygy alike. Mint-shaped: the bucketed
  slope-free gate (2,618x) + four lemmas. Awaiting:
  f2_sl1_powersums, mun_anticoncentration (now the campaign's
  single most important open thread).

## 2026-08-04: round-15 pilot 3/4 BANKED — THE TERMINAL UNIFIED AS (ES); the coding-theory label refuted by theorem

- **mun_anticoncentration (Opus) BANKED** (50/50; 4 own-PREREG
  withdrawals; 2 own predictions refuted openly). (ES) entropic
  suppression = the unified terminal of FOUR lanes (band, crossing,
  syzygy, u2c/dli). ROUTE CUT PROVED: identical-enumerator code pairs
  with different 0/1 counts — MacWilliams/Delsarte/Krawtchouk/
  Sidelnikov/BCH-family CANNOT decide it in principle; Weil vacuous
  13.5-107 bits; L2 loses exactly 2^128. MDS/RS identification;
  prime-power scope (n = 2^41 good); suppression measured 1-2 orders
  EARLY (for (ES)); above-balance accident witness pins the boundary.
  CATCH-15A: MC-4 = PROVED b1 node — dischargeable by citation
  (mint-4, with the b1 repair). NEXT: Ax-Katz transfer = the one
  untested classical route; Pro brief targets p-adic/Deligne-Katz
  people. Awaiting: f2_sl1_powersums (4/4).

## 2026-08-04: round-15 pilot 4/4 BANKED — SL-1 PROVED; ROUND 15 COMPLETE; the t-pin crisis surfaced

- **f2_sl1_powersums (Opus) BANKED** (85/85). SL-1 PROVED
  characteristic-free (weight >= ceil(t/2)+1, subsumes THEOREM A;
  true law min(2R+1, max(p, R+1)) sharp); sixth reduction refuted
  (shared lens, three blockers) BUT the DLI/WCL lane had a stronger
  uncited version (char > w necessary — 6 counterexamples gifted
  back); Z(L) mass bounds + SL-1b named. **MAINTAINER CATCH: t
  UNPINNED** — t* flips LEMMA 3 at rung 16 (0.969x violation) and
  shortens the band to rungs 1-10; m_16 contradiction; F2 discharge
  headlines carry a dated caveat until q = p^k and t are pinned from
  the rules freeze. ROUND 15 COMPLETE. Next-round board: Ax-Katz on
  (ES); the t/q pin; the W-5 rollback (awaiting ratification);
  mint-4.

## 2026-08-06: ROUND 16 LAUNCHED — 4 Opus pilots (2 on mystery 2, 2 on the (ES) terminal)

- **f2_tq_pin** (mystery 2, DEDICATED): derive q = p^k and t from
  rules-level sources; adjudicate t ~ 7e10 vs t* = 8,592,912,739;
  resolve the m_16 = 2^38-vs-2^39 contradiction; recompute LEMMA 3
  at all 16 rungs; state the true surjectivity band. Secondary: the
  |K1|/PP5.0 seam. Derivation task.
- **f2_sl1b** (mystery 2): prove/refute SL-1b (dim L >= m log_p 3);
  counterexample search first; sharpness; discharge-chain consequence.
  t-pin interactions flagged, not resolved (sibling owns it).
- **es_axkatz_transfer** ((ES) lead): algebraize the 0/1
  constant-weight count; exact Ax-Katz exponent at the four rows;
  verdict LIVE / DEAD-VACUOUS / DEAD-INSENSITIVE, adversarially
  self-checked; toy-row calibration against the round-15 verifiers.
- **es_boundary_adversary** ((ES) adversarial lens, sibling-blind):
  hunt a sub-balance accident at scaled admissible families; fit the
  suppression curve; sharpen the above-balance witness; constraint
  feedback. A sub-balance accident = campaign-critical catch.

Composition per user direction ("at least 1 dedicated to 2"); the two
(ES) pilots are mutually blind (proof lens vs falsification lens).
Standing rules: PREREG appended before compute; verbatim quotes;
ramguard law; DRAFT ONLY; coordinator persists reports verbatim;
explicit-path commits while running. STILL PENDING USER RATIFICATION:
the W = 5 rollback (+ CR-W5-ELL1 census gated on it); CATCH-15A edit
queued for mint-4.

- 2026-08-06 CRASH + RECOVERY: a harness crash killed all four round-16
  pilots mid-run (after PREREG appendices and partial state reached
  disk). All four RESUMED from their own transcripts with context
  intact, with instructions to re-verify on-disk state (half-written
  files) before continuing. No work lost; no relaunch.

## 2026-08-06: round-16 pilots 1-3 BANKED — SL-1b non-load-bearing; Ax-Katz DEAD (AK-UNIT); the t/q pin resolves HARDER than posed

- **f2_sl1b (Opus) BANKED** (37/37). SL-1b PROVED as literally stated
  (new k-free LEMMA SL-1b-DIM, sharp both ends, 131/131 floor rows)
  but REFUTED in its intended reading (61 deployed-family witnesses,
  disjoint-code-path confirmed) — NON-LOAD-BEARING, mystery 2 shortens
  in name only; real residual = SL-1b' = the Z(L) terminal. Real gain:
  LEMMA 3's necessary condition verified from below at rung 16
  (large-t readings). CATCH-A: round-15 S4 measurement retracted as
  support (floor(log2 p) bug, 61/61 false negatives). CATCH-B
  (coordinator re-derived): v2(p^2-1) = 25, f2_opening's setting is
  rung-1-only. CATCH-C: uncited DLI "no rank defect" precedent.
- **es_axkatz_transfer (Opus) BANKED** (32/32 + injected-failure
  fail-closed check). TRANSFER DEAD four ways; the structural kill is
  THEOREM AK-UNIT (unconditional): the (ES) crossing target is a
  p-adic unit, so ANY p-divisibility conclusion has the wrong shape —
  non-vacuous congruence theorems would prove accident EXISTENCE
  (refute (ES)), never prove it. AK-WARN: no exact algebraization can
  ever have positive exponent. The classical-transfer ledger on (ES)
  is now COMPLETE (enumerator/Weil/L2/congruence all cut). Frontier
  REFRAMED: char-p vanishing-sums-of-roots-of-unity rigidity
  (Lam-Leung/Conway-Jones analogue), invariant = the divisor profile
  D(Z). CATCH-16A (ALG-I inexact for p <= n; ALG-L load-bearing).
  CATCH-16B kept on the board: at BAND rows mu >= 1 alone would close
  via the 0.68n^2 budget — the one live p-divisibility seam.
- **f2_tq_pin (Opus) BANKED, MAINTAINER-LEVEL** (64/64). t = 7e10 is
  a UNIT ERROR excluded by the rules (back-implies log2 q = 31.4 vs
  n | q-1 forcing > 41); t* right in kind; t pinned to
  (2^33, 5.364e10]. **CATCH-1: the 16-rung KoalaBear tower is NOT
  prize-admissible** (cap broken from rung 4; admissible region
  v_2(e) <= 2, e <= 6, log2 p >= 39, depth <= 2; answers
  field_cap_check:9). **The "rungs 1-13" F2 discharge headline is
  WITHDRAWN of record** -> rungs 1-10 (1-9 stricter window), on a
  tower whose rungs >= 4 are rules-excluded; F2-ADM (re-derive on an
  admissible row) is the named successor task. m_16 split resolved
  (new-part 2^38 vs nested 2^39; stricter governs). |K1|/PP5.0 seam
  PRICED: average-vs-sum = exactly 2^{n/2}, Theta(n) both readings —
  the composition choice is a genuine open decision, SURFACED. Q5
  self-falsified openly; one bare-python3 process defect self-reported.
  Residual elevated: the t-NAMING COLLISION (|Lambda| vs A - k,
  unproved identification).
- CROSS-PILOT: SL-1b's INTERACTION-1 adjudicated via CATCH-1 (tower
  branch moot; round-15 CATCH-4 sign flip CONFIRMED AND STRENGTHENED
  — now rules-forced, not t*-specific).
- Awaiting: es_boundary_adversary (main hunt running).
