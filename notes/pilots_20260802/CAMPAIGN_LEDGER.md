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

## 2026-08-06: round-16 pilot 4 BANKED — (ES) SPLIT BY READING; ROUND 16 COMPLETE; the lost-reports recovery

- **es_boundary_adversary (Opus) BANKED** (296/296 + witness script
  exit 0, both coordinator-replayed). **(ES) per-weight is REFUTED**:
  five verified non-periodic sub-balance witnesses at n = 32 (deepest
  Lam -8.284; cleanest in-scope p = 47, delta = 2, exact integer
  sub-balance), each reproduced from scratch-built fields by a
  disjoint code path. **The GLOBAL reading (u2c floor's q^t >= 2^n)
  survives everything measured** — 0/5 witnesses below it — and the
  faithful crossing shape (n=32, r'=w=8, ALL subsets, ALL
  characteristics) is CLEAN: zero accidents. RE-POSE OF RECORD:
  **(ES-G)** = global balance with TRUE |Z_w|, imposed
  stratum-by-stratum (C4-a); per-weight retired to heuristic status
  (thin boundary band [-8.3, +0.1] bits). Mechanism lead: GENERIC
  COPRIMALITY of the window ideals (C4-c), pairing with the AK
  pilot's char-p rigidity frontier. Round-15 "1-2 orders EARLY"
  REPRICED (n=16-only; never cite as scaling). Above-balance witness
  sharpened to p = 665857. Next compute: the n = 64 census +
  ES-G-LANES (re-check all four lanes against (ES-G) with true
  |Z_w|). Exemplary subtraction (norm-floor novelty withdrawn).
- **CATCH-16C (coordinator, systemic) + REPAIR**: all ELEVEN
  round-13-15 pilot dirs were missing REPORT.md — final-message
  reports were audited but never persisted. All 11 recovered VERBATIM
  from the session transcript by task-id (opening sanity lines match
  the ledger bank entries) and persisted with recovery headers; the
  mun "four proved structural constraints" gloss repaired by
  addendum. STANDING RULE HARDENED: REPORT.md persistence is part of
  the bank — check before the bank commit.

ROUND-16 NET (4/4): the t/q pin resolved HARDER than posed (7e10 a
unit error; the 16-rung tower NOT prize-admissible; F2 headline
withdrawn to rungs 1-10/1-9; F2-ADM named); SL-1b split
(proved-literal via LEMMA SL-1b-DIM / refuted-intended, 61 witnesses
— non-load-bearing); Ax-Katz DEAD four ways (THEOREM AK-UNIT closes
the whole congruence family; frontier reframed as char-p
vanishing-sums rigidity; CATCH-16B band seam live); (ES) split by
reading and RE-POSED as (ES-G) with the crossing shape clean.

BOARD AFTER ROUND 16:
- Mystery 2 = {SL-1b' (= Z(L) terminal), F2-ADM (re-derive on an
  admissible <= 2-rung row), the PP5.0 average-vs-sum choice
  (SURFACED; stricter-reading clause suggests sum), the t-naming
  identification (|Lambda| vs A - k)}.
- Mysteries 1+3+4 residual = (ES-G) + ES-G-LANES + the char-p
  rigidity / generic-coprimality frontier + CATCH-16B; plus the W-5
  rollback (still awaiting ratification) and CR-W5-ELL1 behind it.
- Mint-4 queue grows: (ES-G) node, AK-UNIT/AK-WARN, LEMMA SL-1b-DIM,
  the stratum lemma, the recovery-repaired report set, all round-16
  catches.

NEXT-ROUND CANDIDATES: ES-G-LANES (per-lane re-check, true |Z_w|);
the n = 64 boundary census (Modal-scale); F2-ADM; the t-naming
identification; mint-4 (very large).

## 2026-08-06: ROUND 17 LAUNCHED — 4 Opus pilots (2 on (ES-G), 2 on mystery 2)

- **es_g_lanes** ((ES-G) audit lens): true |Z_w| per row for all four
  consuming lanes; global-balance status per admissible (p, delta)
  incl. possible sign flips (C4-d); binding stratum per lane; exact
  per-lane obligation under (ES-G); the u2c pin check. Broken routing
  reported plainly if a lane sits above global balance.
- **es_coprimality** ((ES-G) proof lens, sibling-blind to es_g_lanes):
  formalize the COPRIMALITY CONJECTURE (N(I_S) = 1 outside a
  characterized exceptional class => the (ES-G) crossing instance);
  w = 3 proof attempt via resultants / Galois orbits / Lam-Leung
  pushed to norms; exceptional class must contain all five round-16
  witnesses; exact coprimality-rate measurements; AK-UNIT
  self-checked.
- **f2_adm** (mystery 2): F2-ADM — reconstruct F2 on a <= 2-rung
  admissible row (explicit witness p = 18446735827372343297, q = p^4);
  theorem survival table; margins worst-case over t in
  (2^33, 5.364e10], both window readings; re-based obligation list;
  PP5.0 seam priced both ways. Falsifier: if the descent needed 16
  rungs, the F2 lane is VACUOUS AS POSED.
- **t_naming** (mystery 2, sibling-blind to f2_adm): prove/refute the
  t_F2 = |Lambda| vs t_XR = A - k identification; re-tag every banked
  consumer of "t"; reconcile 8,592,912,739 vs 8,594,128,895; the
  sliver-seam corrected convention (N5); independent re-check that
  the 7e10 exclusion is naming-independent.

Standing rules as round 16 (PREREG appended before compute; verbatim
quotes; ramguard; DRAFT ONLY; coordinator persists reports — NOW WITH
the hardened persistence check at bank time). STILL PENDING USER:
W = 5 rollback (+ CR-W5-ELL1); PP5.0 average-vs-sum choice.
DEFERRED COMPUTE (not launched this round): the n = 64 boundary
census — Modal-scale; needs a distributed adaptation of the round-16
census machinery; candidate for a coordinator-launched run next.

## 2026-08-06: round-17 pilot 1 BANKED — the t-naming collision RESOLVED BY REFUTATION; round-16 headlines repriced

- **t_naming (Opus) BANKED, MAINTAINER-LEVEL** (68/68). The
  identification is REFUTED: one SCHEMA (UFMB: t·L >= log2 N + G),
  two different balances (t_F2: (2^n, 0); t_XR: (C(n,n-k-t), 128));
  divergence 0.0044%/18.4%/45.0%/65.8% by rate; the rate-1/2
  near-miss is the central binomial (0.0044% = 2/(L^2 ln 2), a
  Stirling correction — f2_tq_pin CATCH-4's tightness demoted).
  **CATCH-E (maintainer, definitional)**: t_F2 is the MAX Newton
  index (5 sources), not |Lambda| (f2_tq_pin PROOFS.md:158) — the
  factor 2 leaves rung-16 LEMMA 3, the t_F2 interval, and the 7e10
  exclusion each with TWO LIVE VALUES pending the Lambda parity pin.
  **7e10 DOWNGRADED**: unit-error origin unconditional; excluded
  under count normalization; NOT excluded under degree normalization.
  Band 1-10/1-9 SURVIVES (t = 2^33 endpoint naming-independent);
  "rungs 1-13" stays withdrawn. **N4**: t* = t_XR = the mca_floor
  object (sigma* = t*-1 exactly); the 8,594,128,895 endpoint is
  SUPERSEDED (unsafe band 1..2^34-1) — t* sits at 0.50017 of the
  proved-unsafe reach; conflict-of-use to maintainer;
  xr_radius_arithmetic lacks the cross-reference. **N5 FORCED
  CORRECTIONS APPLIED**: the sliver is RETIRED (empty for all
  L < 256; repair provably impossible); the two balances are NEVER
  cross-audited again. SURFACED CHOICE: re-label L = 255.9 as a
  representative evaluation point publishing dt*/dL = -3.36e7/bit.
  CATCH-G: a THIRD t* (SOL_TARGET_3, unrenamed) to hygiene queue.
  f2_tq_pin FABLE_AUDIT addendum written (P3 downgraded, P5
  caveated, residual 4 corrected, CATCH-2/5 subsumed; CATCH-1
  untouched). Cross-pilot: the running f2_adm registered the
  CATCH-E-correct max-index reading — reconcile at its bank.
  Honest residual of note: the pilot self-reports WEAK PREREG (8/8
  registered post-reading; all surprises post-registration).
- Awaiting: es_g_lanes, es_coprimality, f2_adm.

## 2026-08-06: round-17 pilot 2 BANKED — THE FOUR-LANE UNIFICATION IS BROKEN AS WIRED

- **es_g_lanes (Opus) BANKED, MAINTAINER-LEVEL** (1413/1413; certified
  140-digit comparator, no float decides a boundary; one self-caught
  float defect fixed by its own PREREG clause). THE TERMINAL RE-SCOPE
  OF RECORD: the "unified terminal of four lanes" is WITHDRAWN —
  the four lanes' field regimes are MUTUALLY UNSATISFIABLE (u2c needs
  log2 Q >= 255.9113; band 1/4-1/8 low depth >= 255.99999994; band
  1/16 >= 256 exactly, i.e. NEVER; dli RES needs < 256 strictly by
  its own proved H2). Per lane: **u2c YES** — its pin IS (ES-G)
  verbatim (q^t >= 2^n), witnesses re-excluded independently;
  **crossing** YES at w >= 2^37, NO at w = 2^34 (all 19 admissible
  (p-class, e) pairs fail the binding deep stratum — the requirement
  log2 p >= 256 IS the rules cap; explicit admissible exhibit
  p = 3·2^41+1, e = 6 above balance at a = 0); **band both nodes** NO
  at rate 1/16 anywhere (>= 512-bit deficit at the cap) and on the
  low-depth 22.5% of 1/4-1/8 scope; **dli RES** NO anywhere —
  UNWIRED (above balance by its own H2/A2; round-15's "discharges
  all four consumers" REFUTED for this lane; mun addendum 2 written).
  MECHANISM: THEOREM Q makes extension degree free for the count
  while e divides log2 p — tower rows are the adversary's best
  choice against (ES-G). BANKED: exact |Z_w| closed forms for all 8
  admissible p-classes (CATCH-B: delta(w-1) bracket top never
  attained at delta = 4; CATCH-C: orbit merge at w = 2^38/2^39).
  CATCH-D: the band q >= 2^209 pin computes the RETIRED per-weight
  threshold, 47.5 bits short of (ES-G) — re-derive under the band's
  adopted form. CATCH-E: u2c three-bases wording + "~2%" prose to
  the u2c statement addendum queue. NEW NAMED OBLIGATIONS: the
  crossing deep-stratum instance at w in {2^34..2^36} (n_a = 256,
  one condition — direct attack candidate); the band effective-base
  question (catch #11/#13 analogue — if the base moves to the
  generated field every band verdict WORSENS).
- Awaiting: es_coprimality, f2_adm.

## 2026-08-06: round-17 pilots 3+4 BANKED — ROUND 17 COMPLETE: (O1) false off-generation; THEOREM CS covers 71% of the crossing bracket

- **f2_adm (Opus) BANKED, MAINTAINER-LEVEL** (373/373; clean-state
  replay byte-identical). The falsifier does NOT fire — the F2
  mechanism reconstructs on <= 2 rungs (LEMMA ADM-2: one-step
  direct-sum into prime-field GRS codes; dim L EXACT, sl1b's bracket
  collapses to a point; ADM-3 kills the coefficient-field ambiguity)
  — but the reconstruction is worse than vacuity: THEOREM A
  discharges NO moving rung on ANY admissible row (0.78% of domain
  at prize-max); LEMMA 3 exactly SATURATED (k/e = 1.000, zero
  margin, vs the tower's 7.89x); and **CATCH-1 (maintainer): (O1)
  IS FALSE by 2^{Theta(n)} on every non-generating admissible row
  (k = ord_n(p) < e)** — explicit exhibit p = 3·2^41+1, q = p^6
  (COORDINATOR-VERIFIED independently; the SAME row es_g_lanes
  exhibited above balance — blind cross-pilot convergence on the
  extension-row adversary). F2 HEADLINE OF RECORD (replaces all rung
  bands): "(O1) discharged on order layers <= 2t (<= 4.9% of domain,
  none moving); at every moving rung it equals SL-1b' with LEMMA 3
  exactly saturated; and it is FALSE unless the smooth domain
  generates the field." The generation hypothesis goes to Przemek.
  SL-1b' now EXPLICIT: ternary mass of [2^38, 2^38-R, R+1]_p GRS on
  the half-system of mu_{2^39}, R = 4.295e9, p ~ 2^64, C <= 4.
  **THE SEAM IDENTITY (D5)**: (O1)'s necessary condition = the
  PP5.0 avg-vs-sum seam (log2|K1|_eff >= n/2), equality exactly on
  k = e rows — the pending user decision is sharpened: sum = bits
  already spent; average = (O1) as a zero-slack claim. CATCH-2
  (sl1b constant, addendum written), CATCH-3 (the tower
  inconsistent with its own t: 7e10 is 1.29e5x too large by tower
  arithmetic), CATCH-4 (empty (40,6) class), CATCH-6 (the
  COSET-DOMAIN gap — antipodal law fails off-subgroup; new named
  obligation). ~9 bare-python3 text edits self-reported.
- **es_coprimality (Opus) BANKED** (143,974/0; fail-closure proven
  by permanent injected-failure stage). **THEOREM CS** — the first
  UNCONDITIONAL positive coverage of the (ES) crossing terminal:
  ideal-level Galois multiplicity (p^{|Z_w^odd|} | N(x_1)) squeezed
  against a SHARP AM-GM ceiling proves the instance outright
  wherever ceil((w-1)/2)·log2 p > (n/4)·log2 r' — at 256-bit p,
  71.16% of the bracket (w > 2^37.3131, incl. w = 2^38, 2^39);
  coverage scales with log2 p (39.57% at 128 bits) and the
  obligation quantifies over all admissible rows — NO STATUS FLIP,
  banked as strong partial. LEMMA TWO (r' even => 2 | N; N_odd is
  the invariant — the naive conjecture false at every prize row,
  self-caught); LEMMA STRAT (the round-16 deep witnesses are w' = 2
  PRINCIPAL instances — triangulates with es_g_lanes' one-condition
  binding stratum); all 5 witnesses in the exceptional class with
  exponents matching on the nose; crossing-shape rate EXACTLY
  1.00000 (21,282/21,282 orbits, all characteristics); round-16's
  r' = 7 gap closed. CATCH-17B: "generically coprime" was never
  banked math — CC-sparsity = the SHARPENED form of the repo's own
  named pair-coprimality open lemma (u2c + u1_x4 consumers).
  CATCH-17D: C4-c's gcd-of-norms mechanism corrected (the collapse
  identity makes it blind). CS2 SHARP — the low-w gap cannot close
  archimedeanly. w = 3 NOT closed (CS degenerates to M3).

ROUND-17 NET (4/4): t-naming refuted with CATCH-E (the Lambda parity
pin, maintainer) + the sliver retired + 7e10 downgraded; the
four-lane unification BROKEN AS WIRED (mutually unsatisfiable
regimes; u2c alone correctly pinned; dli RES unwired); (O1) FALSE
off-generation (the F2 lane conditional on a hypothesis the rules
do not supply); THEOREM CS covers the high-w crossing
unconditionally. THREE BLIND PILOTS CONVERGED on one frontier: the
LOW-w CROSSING CORE (w in [2^34, 2^37.31]) — deep strata = w' = 2
principal-ideal instances, n_a = 256 one-condition — plus E_floor
sparsity (= pair-coprimality), the Z_1 ternary mass (SL-1b',
explicit GRS), and the band lanes' re-pose. The universal adversary
everywhere: extension/non-generating rows.

BOARD AFTER ROUND 17:
- Mystery 2 (F2): {the generation hypothesis (Przemek), Z_1/SL-1b'
  (explicit prime-field GRS), the coset-domain re-derivation, the
  PP5.0 seam choice (user; = (O1)'s own necessary condition), the
  Lambda parity pin (maintainer)}.
- Mysteries 1+3+4: {the low-w crossing core; E_floor sparsity
  (pair-coprimality); the band re-pose (weight-aware form or
  non-balance route) + the effective-base question + CATCH-16B;
  u2c stands on its own correct pin; dli RES on its own
  instruments}.
- PENDING USER: W = 5 rollback (+ CR-W5-ELL1); the PP5.0 reading.
- PENDING MAINTAINER (Przemek queue): the generation hypothesis;
  the Lambda parity pin; the t*/mca_floor conflict-of-use; CATCH-1
  tower answer to field_cap_check.
- MINT-4 (still growing): (ES-G) re-scope + CS/STRAT/TWO + ADM
  lemmas + |Z_w| closed forms + all round-16/17 catches + the
  recovered reports.

## 2026-08-06: ROUND 18 LAUNCHED — 4 Opus pilots on the four named hard cores (2 generative, 1 adversarial, 1 hybrid)

- **crossing_low_w (GENERATIVE)**: the low-w crossing core — state
  the w = 2 principal question exactly; attack the n_a = 256
  one-condition deep-stratum instance via the LIFT-CONSTRAINT
  conjecture (toy-gated at three shapes); refine the
  covered/uncovered split; if a reduced solution lifts, follow it up
  toward a genuine accident (campaign-critical either way). Balance
  frame forbidden (CS2 sharp; no admissible row clears the stratum).
- **o1_generating_adversary (ADVERSARIAL, blind to z1)**: break (O1)
  on the surviving generating rows (k = e, zero margin): V1
  zero-margin loss hunt; V2 the coset attack (CATCH-6); V3 the Z_1
  lower-bound attack (crosswalk check first — the DLI wt >= 2R+1
  law under char > w may now APPLY since admissible p ~ 2^64 > w);
  V4 the generating-class vacuity sweep FIRST. Failed attacks
  reported as SURVIVED-with-margin; every step under both Lambda
  parity readings.
- **z1_ternary_mass (GENERATIVE, blind to o1)**: SL-1b' on the
  explicit object — crosswalk check FIRST (transport the DLI
  stronger distance law if char > w now holds), then the mass bound
  via norm-sandwich transport / GRS-dual second moments / the
  C <= 4 class structure; calibration grid pre-registered; DLI
  subtraction mandatory; consistency with the 61 witnesses required.
- **efloor_sparsity (HYBRID, blind to crossing_low_w)**: the
  pair-coprimality debt — S1 prove small-prime exclusion (p = 3
  first; union bound over the finite CS3-surviving range = the
  theorem shape); S2 adversarially construct the densest floor
  families (non-vanishing density refutes CC-sparsity); S3 the
  n = 64 asymptotic (close or honestly re-flag); S4 the u2c
  conversion statement.

Brief hardening this round: the COMPUTE LAW clause now explicitly
covers file patching and JSON peeking (the recurring round-17 breach
pattern). Standing rules otherwise as round 17. STILL PENDING USER:
W = 5 rollback (+ CR-W5-ELL1); the PP5.0 reading (= the seam
identity). PENDING PRZEMEK: generation hypothesis; Lambda parity;
t*/mca_floor conflict. Mint-4 queued after this round.

## 2026-08-06: round-18 pilot 1 BANKED — the adversary lands: (O1)'s sign is the 0.0044%

- **o1_generating_adversary (Opus) BANKED, MAINTAINER-LEVEL**
  (187/187). Three attacks FAIL with exact margins: V2 coset costs a
  FACTOR OF 1 (THEOREM C1, disjoint group-ring route; half of f2_adm
  CATCH-6 closes; CATCH-1 coset-robust); V4 the generating scope is
  exactly THREE non-empty classes (THEOREM G1: ord mod 2^41 is
  always a 2-power, so e in {3,5,6} can NEVER generate; THEOREM G2:
  Lucas p-1 CERTIFICATES for all witnesses); V3 no ternary
  construction reaches the floor — and **THEOREM D1: the DLI
  wt >= 2R+1 law APPLIES on every admissible row** (p > m always;
  the first family where char > w holds; the tower verdict reversed
  by the field cap; (M3) still vacuous, 23.9x -> 11.96x). BUT V1
  LANDS CONDITIONALLY — **THEOREM Z2, the ensemble dichotomy**: at
  k = e LEMMA 3's requirement IS the balance t·L >= n, so (O1)
  survives under the full-subset (C) calibration (<= 184 bits
  slack) and is FALSE by 2^{Theta(n)} (>= 2^{4.84e7}) under the
  exact fixed-slice (T*) calibration. **CATCH-A: the 0.0044%
  "agreement" banked twice (f2_tq_pin CATCH-4, t_naming CATCH-C) IS
  the sign of (O1) at zero margin.** CATCH-G: the (O1)=>(O2) fence
  itself demands the slice ensemble (THEOREM B' vacuous at every
  moving rung); CATCH-H: reading A is internally FORCED (proved
  K1/K2/G trichotomy + the lane's own t/2 text) — so the
  internally-forced cell of the 2x2 (parity x ensemble) is exactly
  the FALSE one. STATED OF RECORD: the lane's own internal logic
  points at the false cell; only a maintainer ruling on intent can
  restore (O1) on generating rows. THE MINIMAL SURVIVING FORM
  banked (E[T] = 2^{n/2}·Z_1^e on three classes, two unpinned
  conditions) — this is what the Przemek note carries. CATCH-B:
  f2_adm's "margin 1.000" is reading-A-only (addendum written).
  Addenda: f2_adm (CATCH-6 half-closed, D3 caveat, Z2), t_naming
  (CATCH-E burden shifted). Third consecutive weak-prereg
  self-report — noted as systematic for derivation pilots.
- Awaiting: crossing_low_w, z1_ternary_mass, efloor_sparsity.

## 2026-08-06: round-18 pilot 2 BANKED — THEOREM DSA: (ES)-crossing FALSE at admissible tower rows, witness AT n = 2^41

- **crossing_low_w (Opus) BANKED, CAMPAIGN-CRITICAL** (1,565,906
  checks 0 failures; coordinator replayed the bijection gate 81,005/0
  and the witness verification 2,854/0). MY brief's lift-constraint
  conjecture REFUTED structurally (the pilot pre-registered the
  negation, X1: at the binding stratum there are ZERO lift
  constraints — LEMMA FREE); LEMMA DS (deep-stratum bijection,
  r'_a = L-2 uniformly — ONE one-parameter family); LEMMA OE (the
  odd/even epsilon/sigma split — the recursion for shallower strata);
  LEMMA TC (the primitive object is TERNARY: 3^L, not 2^{n_a} or
  C(n_a,r'_a) — per-weight mis-priced by 48.75 bits); LEMMA ROT
  (2L-orbit over-dispersion). **THEOREM DSA (unconditional
  pigeonhole): accidents EXIST at every admissible row with
  p^{delta_a} < 2^{L-2}** — (ES)-crossing FALSE at 10/19 pairs
  outright at w = 2^34 (3/19 at 2^35), with an explicit witness
  VERIFIED AT n = 2^41 on the triple-refutation row
  (p = 3·2^41+1, e = 6 — the same row as es_g_lanes' balance exhibit
  and f2_adm's (O1) kill). e = 1 prime rows PROVABLY outside the
  regime (B* >= 3 forces log2 p >= 129.6 > 126) and RE-PRICED
  heuristically to a 53-61 bit margin under the ternary functional
  (vs the 0.089-bit global cliff). Consumer consequence SCOPED: the
  refuted statement is |W_w| = structural; the crossing NODE's
  gamma-shell/budget question at tower rows is RE-OPENED, not
  decided. es_g_lanes P4 was detecting a REAL refutation. CATCH-18E
  (self-caught birthday-sizing). SCOPE ESCALATION OF RECORD: the
  Przemek tower/generation question now DECIDES two lanes — the
  maintainer note leads with the DSA witness. Next-round residuals:
  the gamma-shell population; shallower strata via LEMMA OE; the
  prime-row emptiness proof at the ternary margin.

## 2026-08-06: round-18 pilot 3 BANKED — the first sparsity theorems; CC-sparsity re-labelled as (ES)-again

- **efloor_sparsity (Opus) BANKED** (56,542/0 across 10 stages;
  coordinator replayed self 52,510/0; ZERO compute-law breaches —
  the hardened clause worked). **THEOREM SP-COVER + SP-UNIFORM**:
  a = 0 bad primes force p > sqrt(w+1) — p = 3 dead for all w >= 6
  at every n; the bad-prime range is TWO-SIDED (CS-EXCL above).
  THEOREM SP-TERNARY (second mechanism); LEMMA AB (the engine — the
  ternary object again); LEMMA QS + the F1 quarter-shift family
  (49% of floor mass at 116x density, dies at one step of w — the
  adversarial half finds NO refutation of CC-sparsity); the SPD
  union-bound shape proved VACUOUS (the middle of the prime range
  needs a non-character-sum idea); round-16's n = 64 flag CLOSED
  (+ n = 128) via a new exact MITM census over all 2^32 subsets;
  (CONV) stated exactly with the official q provably in neither
  closed end. **CATCH E-1 (round-17 downgrade)**: E_floor is a
  TAUTOLOGY given CS — the (K5) conditional re-labelled (hypothesis
  as hard as conclusion); CS's 71.16% untouched. **CATCH E-2**:
  CC-sparsity IS (ES) at half length over ternary. **CATCH E-3**:
  the official v_2(q-1) >= 41 gate is exactly SP-COVER's blind spot
  (gap 2^4.69 in w between the two proved exclusions).
  **COORDINATOR CONVERGENCE NOTE**: third independent appearance of
  TERNARY-IN-CODE as the primitive this round (crossing LEMMA TC,
  this LEMMA AB, z1's mandate) — the true shared terminal candidate,
  to be tested at the z1 bank and posed for round 19 if it survives.
  Leads: the p = 5, w = 2 zero-ternary anomaly; even-condition
  SP-COVER.
- Awaiting: z1_ternary_mass (the last of round 18).

## 2026-08-06: round-18 pilot 4 BANKED — ROUND 18 COMPLETE: the knife edge, the no-go, and the ternary unification

- **z1_ternary_mass (Opus) BANKED** (81/81; process CLEAN — second
  fully clean pilot). **THEOREM Z-1**: the DLI distance law
  TRANSPORTS (min ternary weight >= 2R+1 = 8,589,934,681) —
  CONVERGENT with the blind adversary's D1 (same constant, disjoint
  derivations); scope: shift-0 only (43 shifted counterexamples;
  legitimate because the official window starts at 1).
  **THEOREM Z-FLOOR**: the first moment is a POINTWISE floor
  (Z >= 2^m/p^{dim L}; one Cauchy-Schwarz from a banked identity
  nobody had drawn; tight within 2x). **THEOREM Z-3**: (O1) FALSE
  at the OBJECT level on every k < e admissible row — f2_adm
  CATCH-1's 2^{5n/12} reproduced EXACTLY by an independent route.
  **THEOREM Z-NOGO**: distance+counting can NEVER close SL-1b'
  (needs p <= 8 vs admissible 2^39). **THEOREM Z-2** (gift to DLI:
  the {±1} restriction unnecessary — l1 weight, same cutoff).
  At k = e the floor misses by 46 BITS of 2.75e11 (one Lambda
  condition = 64 bits; the two t-readings STRADDLE ZERO — under
  exact-balance it FIRES: ternary kernel vectors provably exist,
  the exact-zero form dies, yet Z stays 2^{o(n)}).
  **CATCH-Z1 (brief defect, coordinator's)**: mass form != exact-zero
  form; THE TERMINAL OF RECORD = the MASS form (Z_1 <= 2^{o(m)} at
  k = e), with route (b) (Weil products over the 2^39-subgroup,
  factor-2 headroom) the ONLY live route. Calibration honest: at or
  below random median on all valid miniatures; "better than random"
  NOT claimed. CATCH-Z6 (composite-2N toy contamination — standing
  grid rule adopted).

ROUND-18 NET (4/4): the adversary's ensemble dichotomy (the 0.0044%
IS (O1)'s sign; internally-forced cell FALSE); THEOREM DSA
((ES)-crossing FALSE at tower rows, witness AT n = 2^41, on the
triple-refutation row); the first sparsity theorems (SP-COVER/
SP-UNIFORM two-sided range) with CC-sparsity re-labelled as
(ES)-again; the F2 terminal re-shaped to the MASS knife edge with a
proved NO-GO for the whole distance+counting family. THE ROUND'S
DISCOVERY: all four blind pilots converged on TERNARY VECTORS IN
p-ARY CODES FROM CYCLOTOMIC WINDOWS as the primitive object — the
ROUND-19 UNIFICATION CANDIDATE (one question family, three
instances, the round's theorems as its partial answers).

BOARD AFTER ROUND 18:
- Mystery 2 (F2): terminal = Z_1 MASS at k = e via route (b);
  everything else is the maintainer seam (generation/parity/
  ensemble/PP5.0 — now FOUR faces of one inequality). k < e rows:
  (O1) dead twice over (necessary-condition + object-level).
- Crossing: tower rows REFUTED (DSA; scope = the Przemek question);
  prime rows at a 53-61 bit heuristic ternary margin with proof
  obligation open; low-w core two-sided (SP-COVER below, CS above)
  with the official primes provably in the gap.
- Band: unchanged this round; the ternary functional (LEMMA TC) is
  the transfer candidate for its re-pose.
- C1/C2'': own instruments, unchanged.
- PENDING USER: W = 5 rollback; PP5.0 reading (now the fourth face).
- PENDING PRZEMEK (the note now writes itself): the tower/generation
  scope (DECIDES two lanes, with the DSA witness); Lambda parity
  (internally forced to A); the ensemble calibration; the
  t*/mca_floor conflict.
- NEXT: MINT-4 (massively overdue — three rounds of theorems in
  notes) + the Przemek note + the round-19 ternary unification
  draft + the gamma-shell question + route (b).

## 2026-08-06: MINT-4 CORE EXECUTED + the two parked decisions ruled (user-delegated)

DECISIONS (coordinator rulings under user delegation, 2026-08-06):
- **W = 5 ROLLBACK RATIFIED** (round-16 a1_window_audit verdict
  LOSSY; the +7 was underived): W = 5 is the window of record;
  board 10/8-routeless -> 4/1-closable; recorded as a statement
  addendum on xr_band_high_window_exclusion. CR-W5-ELL1 census
  DEFERRED until the band functional re-pose settles (no compute
  spent calibrating a retired frame).
- **PP5.0 = the SUM reading** as campaign working convention, by the
  rules-freeze stricter-reading clause; flagged for maintainer
  confirmation; both pricings carried in all statements (recorded in
  f2_o1_status_split).

MINT-4 CORE (six new background nodes + six statement addenda;
write-path: shards -> compile_dag --write -> sectioned docs ->
verify chain):
- NEW: f2_admissible_object (ADM lemmas, G1/G2 census, C1 coset
  invariance); f2_o1_status_split (ADM-B + Z-3 + Z2 + the minimal
  surviving form + the FOUR-FACE SEAM); f2_z1_mass_knife_edge
  (Z-FLOOR, Z-1/D1, Z-2, Z-NOGO, the 46-bit knife edge, route (b),
  terminal = the MASS form); crossing_dsa_refutation (DSA + witness
  + DS/FREE/OE/TC/ROT + the prime-row re-pricing);
  es_ternary_suppression_instruments (CS + STRAT + TWO +
  SP-COVER/SP-UNIFORM/SP-TERNARY + the E-1/E-2/E-3 limits);
  esg_lane_rescope (the re-scope of record + |Z_w| closed forms).
  Edges: supplier-owned ev/ref into u2c, crossing, band leaf, dli.
- ADDENDA: u2c (base pin per THEOREM Q, ~2% -> 0.089-bit, witness
  exclusion, the two-closed-ends state); crossing node (DSA scope
  note, gamma-shell re-opened, CS coverage); band leaf (W = 5
  ratification + functional status); xr_radius_arithmetic (t* =
  mca_floor object, sliver retired, never cross-audit);
  dli_wcl_newton_short_window_exclusion (scope reversal + the l1
  strengthening); b1 (CATCH-15B verifier-of-record repair, MC-4 by
  citation).
- Compiled: dag 1817/5070 -> 1823/5081; sectioned docs recompiled;
  verify_prize_dag PASS (no warnings on the six; x81/x83 warnings
  pre-existing); ORBIT_CENSUS_PASS unchanged (246 = 179/41/26,
  submission 261 = 191/43/27) — the six are orbit-external
  satellites.
- DEFERRED to mint-4b: the critical-lane re-wiring of the F2/crossing
  terminals (blocked on the Przemek scope answers by design); the
  naming ledger extension (six t symbols); the SOL_TARGET_3 t*
  rename; the D2/D3 shard addenda; the remaining round-15 mint queue
  (UPB, 3-drop THEOREM D, F2 A/B/C wave, crossing X/Q/Y/MW wave,
  b2b retyping).

## 2026-08-06: ROUND 19 LAUNCHED — the ternary unification, attacked before adoption (4 Opus pilots)

Per the user's directive (speculative unifications have collapsed
before — attack/strengthen before proceeding), the round-18
convergence candidate goes through the fire the (ES) unification
never got:
- **tern_unification_adversary (ADVERSARIAL, blind to the builder)**:
  the (ES)-collapse failure modes as registered falsifiers — the
  shape-pun test (one parametrized statement specializing EXACTLY,
  vs the proved mass/existence split, R-vs-one conditions,
  fibred-vs-native ternary, differing evaluation structures); the
  regime-compatibility audit (mutually satisfiable or provably
  disjoint — with the honest note that a method-unification can
  survive disjoint regimes, unlike (ES)'s discharge claim); the
  instrument transfer matrix (exact hypothesis matching); the
  structural-disanalogy hunt. Deliverable: a GRADED verdict
  (statement / regime / method), each surviving or killed, with
  proofs.
- **tern_master_statement (GENERATIVE, blind to the adversary)**:
  the strongest honest form — T(P, Lambda) with exact dictionaries
  (existence/count/mass as a PARAMETER per CATCH-Z1), the shared
  spine proved with subtraction (char-0 emptiness at 2-power
  orders; CS over Frobenius-stable Lambda; orbits; Z-FLOOR scope),
  the constructive instrument matrix, THE VALUE TEST (>= 1 proved
  cross-instance consequence or the honest zero), the draft master
  node.
- **tern_route_b (GENERATIVE)**: the one route Z-NOGO leaves open,
  made precise or killed — the exact character-sum form of Z_1
  (gate: machine-verified identity), the cancellation ledger (the
  factor-2 headroom to theorem grade or dead-with-gap), the
  round-15 L2-barrier precedent test, toy calibration, and the
  LIVE/DEAD/TRANSFORMED verdict (chasing 2-power-conductor
  Gauss-sum exactness hard).
- **tern_small_scale_laws (ADVERSARIAL-EMPIRICAL, blind to
  route-b)**: matched exact censuses across the three instance
  miniatures; the TRACKING TEST (dictionaries pre-stated; a
  structured deviation = quantitative refutation); the p = 5
  zero-ternary anomaly explained or weaponized (shared anomaly =
  best positive evidence; local = disanalogy datum); the
  cross-instance scaling verdict. One labelled composite-length
  negative-control cell; otherwise 2-power only (CATCH-Z6).

Blind pairs: adversary/builder on the statement; route-b/laws on
the quantitative side. The coordinator reconciles the two
instrument matrices at the bank. Standing rules as round 18
(hardened compute-law clause; REPORT.md persistence at bank).

## 2026-08-06: round-19 pilot 1 BANKED — the unification's exact core SURVIVES; two heuristics refuted; the anomaly closed

- **tern_small_scale_laws (Opus) BANKED** (412/0 staged; coordinator
  replay 122/0; licensing controls reproduce banked numbers
  verbatim). THE DICTIONARIES VERIFY EXACTLY: I3's binding stratum
  IS I2 vector-for-vector (D1); I1 at R = 1 = I2 (D2); the efloor
  S-count and z1 mass are ONE functional (D3: Sct = 2^N(Z-1),
  disjoint code paths) — the unification's exact content at full
  strength. HEURISTICS REFUTED with exact laws: CATCH-19A (the
  LEMMA ROT orbit constant 2N collapses to 2 for I1's mixed-parity
  windows at R >= 2 — negacyclic iff all-odd T); CATCH-19B (shift-0
  = a p-INDEPENDENT INTEGER layer, count T(N)-1 exactly —
  CATCH-Z6's second door; CONTAMINATES a quarter of z1's
  calibration grid [addendum written]; COORDINATOR SCOPE
  CORRECTION: the official window is odd and never contains s = 0 —
  the pilot's "2^44 excess at the official row" line is mis-scoped;
  calibration hazard only). CATCH-19C (the (3/2)^N convention gap —
  name the functional, standing rule). CATCH-19D (DISJOINT PRIME
  STRATA: SELF-ORTH needs |T| >= N/2, I1 forces split primes — the
  instances share the object, sample non-overlapping strata).
  THE ANOMALY CLOSED: **LEMMA TWT** (self-orthogonal + ternary =>
  p | wt; sharp predicate, 83/0) x orbit quantization = the full
  155x; instance-local (the weaker outcome). NEW LEAD: the
  p = 7, w = 4 484x OVER-representation — an opposite-signed
  mechanism TWT does not explain. Scaling: exact structure
  scale-free; TWT dies for I1 at scale; orbit gap grows log2 N.
- Awaiting: tern_unification_adversary (resumed after an API-error
  kill), tern_master_statement, tern_route_b.

## 2026-08-06: round-19 pilot 2 BANKED — the master statement is REAL and PAYS TWICE; a minted-node constant corrected

- **tern_master_statement (Opus) BANKED** (92,263/0 staged;
  coordinator replayed all six stages + failclosed). PROPOSITION HS:
  T(P, Lambda) = the ternary words of a negacyclic F_p-code — the
  master object in one sentence; all three instances specialize
  EXACTLY (I2 mass-reading only, I3 odd-conditions only — both
  partials honestly reported; the recursion named). THE SPINE
  PROVED: CZ-M (CATCH-Z6 -> a rank statement, closed count);
  **CS-M** (CS verbatim for ANY Frobenius-stable unit Lambda — no
  window hypothesis — via **LEMMA BR: r' - a_{n/2}(S) = wt(A-B)**,
  the unification's prettiest fact); ROT-M; Z-FLOOR-M (exact
  boundary). VALUE TEST PAYS TWICE: **THEOREM I3-FORCE** (first
  EXISTENCE instrument on the (ES) object: below |Z_w^odd| log2 p <
  n/2 the odd-condition exclusion mechanism PROVABLY FAILS — on
  named tower rows; CATCH E-3 upgraded from vacuous to false-there)
  and **THEOREM MT** (ONE inequality g log2 p vs h governs I1's
  knife edge, I2's DSA boundary, I3's stratum-0 boundary —
  reproducing -46.0249/+17.9751 to FOUR DECIMALS; COROLLARY MX: norm
  and pigeonhole mechanisms never simultaneously informative —
  route (a)'s death is structural). 19-instrument matrix delivered
  (12 master / 1 subsumed / 4 instance-only / 2 cited). BLIND
  CONVERGENCE with ssl (the one-framework object + the D3 functional
  identity — subtraction caught it, credit given). **CATCH-T3
  (against a minted node): FORCED CORRECTION APPLIED** —
  f2_z1_mass_knife_edge's route-(a) constant 2.0000 -> 4.0000 (the
  banked sharp ceiling is w^{n/4} not w^{n/2}; dead either way; dag
  recompiled, verify PASS). CATCH-T4 citation drift noted. NOTHING
  CLOSED — stated plainly. NODE_DRAFT (tern_master_threshold)
  delivered; THE MINT IS GATED on the adversary sibling's graded
  verdict, per the blind-pair design.
- Awaiting: tern_unification_adversary (resumed), tern_route_b.

## 2026-08-06: round-19 pilot 3 BANKED — ROUTE (b) DEAD AS POSED; the F2 terminal has NO NAMED ROUTE; second forced node correction

- **tern_route_b (Opus) BANKED** (137/137). The minted "factor-2
  headroom" REFUTED — the sizing dropped the DEGREE factor
  (restored: deg·sqrt p = 2^65 vs |H| = 2^39, Weil vacuous by
  exactly 26.000 bits); the executable substitute (LEMMA 5 AM-GM +
  Z-2 moments) yields **THEOREM 7: Z_1 <= 2^{0.8908·S}
  unconditional** (first nontrivial unconditional mass bound,
  3.0e10 bits below trivial) but closes only at p <= 8.30 —
  Z-NOGO's own threshold, structurally (the moment route consumes
  distance+count). **PROPOSITION 3: the object is a sum of p^R
  NON-NEGATIVE terms — cancellation between tuples does not exist
  in principle; the route was mis-conceived, not mis-sized.** The
  true open form: THE TAIL-COUNT CRITERION
  (|{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)} for all c).
  Favourable reductions banked: LEMMA 2 (oddness => COMPLETE
  subgroup sums — no partial-sum loss) + LEMMA 5 (first moment in
  V_1 only — no L2->Linf loss): both round-15 loss modes provably
  do not bite; the fatal one is DEGREE (which my brief did not
  name — CATCH-B4 brief defect accepted; the round-15 "1-2 orders"
  gloss re-labelled: ratios track sqrt p). PROPOSITION 9 (my
  Gauss-chase brief hint was misdirected — quadratic/quartic
  evaluations govern the opposite object; chased and killed
  properly). **PROPOSITION 10 (the lead)**: log2 P(u) exactly as a
  doubling-map/log-sine functional — Dedekind-sum-shaped, strictly
  finer than V_1, no bound known. CATCH-B1 (z1's 1+2cos line = the
  unweighted count; disclaimed in situ, nothing breaks). CATCH-B3:
  **SECOND FORCED CORRECTION to f2_z1_mass_knife_edge this round**
  (route (b) sizing struck; "NO NAMED ROUTE REMAINS" is the node's
  text now; dag recompiled, verify PASS). BOARD CONSEQUENCE: the F2
  knife edge has no route with a named instrument — the open form
  is the tail count; the leads are Prop 10 + whatever the
  adversary/master pair surfaces. Honest limit: implementation-
  death, not a Z-NOGO-strength no-go.
- Awaiting: tern_unification_adversary (the round's gate).

## 2026-08-06: round-19 pilot 4 BANKED — ROUND 19 COMPLETE: THE GRADED VERDICT; tern_master_threshold MINTED

- **tern_unification_adversary (Opus) BANKED — THE GATE** (54/54;
  two self-corrections caught by its own fail-closed gates). THE
  GRADED VERDICT, ADOPTED OF RECORD: **OBJECT survives** (proved —
  one negacyclic code, all-odd shift-0 window; PROPOSITION FIB:
  I1's mass IS a count of binary pairs, my disanalogy (iii) false;
  the real split = constant-weight vs full-cube); **REGIME survives
  as satisfiability** (THEOREM SR: an explicit shared admissible
  256-bit prime row for ALL THREE — the anti-(ES) result; no shared
  discharge); **METHOD survives but INERT** (verbatim transfers,
  every one vacuous at its target's tau); **STATEMENT KILLED** by
  **THEOREM PT — the phase transition**: tau = g log2 p / h puts I1
  AT tau = 1 (forced by saturation; supercritical — only MASS can
  be true; CATCH-Z1's re-pin was FORCED by sign(Tcrit)) vs I2/I3 at
  tau = 2 (subcritical — EMPTINESS the target); the coordinate
  reproduces FOUR banked constants unfitted. **COROLLARY PT-2 (WATCH
  LINE)**: the crossing bracket's proved lower endpoint clears the
  ternary threshold by 0.336 BITS — one step below, prime rows go
  supercritical; re-run on any bracket change. ADJUDICATIONS:
  CATCH-19A RE-SCOPED (the official I1 window is ALL-ODD — the 2N
  orbit constant STANDS for the official object; ssl's collapse is
  miniature-convention-only; addendum written); I4 DEMOTED (three
  instances, not four — the (ES)-style inflation caught); the
  QUARANTINE RULE adopted (blind pilots must not read in-round
  ledger sections — the porosity was disclosed with an honest
  timeline; the -46.0249/+17.9751 is now a THREE-way blind
  convergence); the CRITICALITY-COMPATIBILITY gate adopted as the
  standing third unification test; CATCH E-3 re-labelled a
  shared-row property (es_ternary addendum queued). Elevated
  residual: **the untested cell — constant-weight Z-FLOOR at I2 —
  the one place a genuinely new instrument might live** (round-20
  candidate).
- **tern_master_threshold MINTED** (background, PROVED — the graded
  form ONLY: object + dictionaries + spine + MT/PT/SR + per-tau
  targets + the instrument matrix + PT-2 watch line; explicitly NOT
  a single-theorem target; refs = all four pilot verifiers; ref
  edges to the three instance nodes). dag 1823/5081 -> 1824/5084;
  verify PASS; census UNCHANGED.

ROUND-19 NET (4/4): the unification ATTACKED FIRST per the user's
directive and it SURVIVED IN GRADED FORM — object/regime/method
proved, single-theorem form killed by a proved phase transition;
the master node minted gated on the adversary's verdict; route (b)
died honestly (the F2 terminal has NO named route; open form = the
tail count; leads = Prop 10 + the constant-weight-Z-FLOOR cell);
two forced corrections landed on the knife-edge node; the (ES)
post-mortem toolkit grew a third gate. BOARD: mystery 2's terminal
= the tail-count criterion at tau = 1 (no named route; two leads);
crossing low-w = emptiness at tau = 2 with the official primes in
the SP/CS gap + the PT-2 cliff on the watch line; the maintainer
stack unchanged and still the highest-leverage item (the Przemek
note next).

## 2026-08-06: THE SCOPE AND READING RULINGS (user-prompted; the maintainer stack DISSOLVED)

The user's challenge ("we know what the prize problems are — judge
for ourselves") is CORRECT and is adopted as of record:

1. **SCOPE RULING (spec-derived, no intent needed).** The frozen
   public spec ("for every choice of F, L, and k"; the pinned
   admissibility constraints) contains NO generation restriction —
   and our own stricter-reading clause points the same way.
   **Non-generating and tower rows ARE in the challenge family.**
   Przemek is a fellow researcher, not the prize organizer; the
   spec text governs. THE PRZEMEK NOTE IS SHELVED (draft kept at
   notes/przemek_note_20260806/DRAFT.md as a record of the fork;
   the t*/mca_floor cross-reference survives as a future PR-comment
   hygiene item, no question attached).
2. **CONSEQUENCE, stated honestly**: the tower/non-generating
   counterexamples (DSA; the (O1) kills) refute OUR INTERMEDIATES,
   not the prize conjectures — those are our constructions. Whether
   the prize-level statement survives at tower rows runs through
   the GAMMA-SHELL/BUDGET analysis (left open at the DSA bank),
   which becomes the board's sharpest question with two live
   outcomes: within-budget (our intermediates were lossy — re-pose)
   or budget-break (A REFUTATION PATH FOR THE GRAND CHALLENGE — a
   resolution either way).
3. **READING RULINGS (soundness-forced, internal).** Lambda parity
   = READING A of record (the proved K1/K2/G trichotomy + the
   lane's own min(m_j, t/2) text); the ensemble = THE SLICE (T*)
   of record (forced by the (O1) => (O2) fence — the consumer
   demands it); PP5.0 = SUM (already ruled). CONSEQUENCE ACCEPTED:
   **(O1) AS POSED IS FALSE on generating rows too** — the
   two-live-values bookkeeping collapses; the F2 lane's obligation
   of record is the minimal surviving form (E[T] = 2^{n/2}·Z_1^e)
   with the TAIL-COUNT criterion at tau = 1, which is where the
   mathematics already stands. The rung-band caveats and the
   "internally-forced cell" language are superseded by this ruling.
4. Node addenda written this bank: f2_o1_status_split (the 2x2
   ruled); crossing_dsa_refutation (the scope clause resolved —
   towers in-family; the refutation's scope condition is
   SATISFIED).

BOARD AFTER THE RULINGS: no external blockers. (1) THE GAMMA-SHELL
question (refutation-or-repose); (2) the F2 re-pose + tail-count
criterion (leads: Prop 10; the 484x creation anomaly); (3) the
crossing low-w prime-row emptiness (the SP/CS gap; the
even-condition extension; the PT-2 cliff needs its floor
re-verified); (4) the band re-pose.

## 2026-08-06: ROUND 20 LAUNCHED — the post-rulings frontier (4 Opus pilots)

(Quarantine marker: round-20 pilots must not read ledger entries
below this line until the round completes.)

- **gamma_shell (THE PRIORITY)**: refutation-or-repose — the shell
  map of the DSA accident family (sig-arithmetic of the periodic
  lift, toy-gated), the per-shell budget comparison with the
  concentration danger case FIRST, the verdict under the strict
  refutation protocol (budget-break = CANDIDATE for coordinator
  replay, consumer chain traced to the prize-level statement), the
  PT-2 stability note.
- **f2_repose (blind to tail_count)**: the F2 lane rebuilt from the
  consumer down — the quoted consumer contract; the weakest
  sufficient intermediate at generating rows (median/quantile
  candidates before mass); at least one candidate per route for
  non-generating rows; the lane NODE-DRAFT.
- **tail_count (blind to f2_repose)**: the terminal's open form
  attacked via the two leads — the Prop-10 doubling/log-sine
  functional (orbit telescoping, multiset second moments evading
  the Corollary-8 trap, a large-P structure theorem) + the p=7 w=4
  484x CREATION mechanism identified from its 288 codewords; the
  exact toy tail profile vs the criterion.
- **crossing_gap (blind to gamma_shell)**: the even-condition
  SP-COVER recursion (gated on the p=7 w=7 census cell); the
  constant-weight Z-FLOOR at the crossing instance (the round-19
  untested cell); the ADVERSARIAL PT-2 cliff re-verification
  (RHL-LB's 2^34 re-derived from source; the 0.336-bit clearance
  under all banked readings); the exact remaining gap.

Standing rules as round 19 + the quarantine marker above. All four
mysteries' post-rulings frontier covered: the gamma-shell question
(crossing/prize-level), the F2 re-pose + terminal, the prime-row
gap, with the band re-pose queued behind the ternary-functional
outcome.

## 2026-08-06: WAVE-47 AUDIT LAUNCHED (Codex, from pin 88238fd0 — audit head PINNED at 48fc9efcf)

Codex has been merging canonical continuously (through fed71a06b)
and working the SAME F2 terminal in real time — AND IS LIVE NOW
(a newer commit f8ad8cb5e "Record F2 selector transport handoff" +
uncommitted pilot results appeared during the survey; post-pin work
queues for wave 48 per protocol). Two streams, two Opus auditors
(drafts to WAVE47_{F2,WCL}_DRAFT.md):
- **F2 STREAM**: a NEW CRITICAL NODE f2_conditional_close + eight
  new background nodes (the admissible direct-sum/GRS reductions,
  the weighted prefix L2 identity, the kernel collision floor, the
  max-fiber sandwich, the all-admissible o1 mass bound, and a
  minted CS supplier rate_half_crossing_ideal_galois_multiplicity_
  exclusion) + the route repair + the generated-field descent
  commits. KEY AUDIT QUESTIONS: soundness/replay; consistency with
  our minted rounds-16-19 nodes AND with the 2026-08-06 rulings
  (which POSTDATE Codex's latest commits); collisions with the
  RUNNING f2_repose pilot (reconcile at that pilot's bank).
- **WCL + REMAINDER**: the WCL hard-tail certificate stream (CADO
  runs + self-contained certificates + slot-emptiness proofs +
  batch replays); the crossing/band/l1 critical-node edits
  (BOTH-diff-direction clobber check vs our addenda); roadmap/
  compute-request/work_cycles repricing; Codex's own pilot dirs.

PROCESS NEAR-MISS, disclosed: the coordinator's launch ledger entry
was briefly committed ONTO CODEX'S BRANCH (cwd drift into the
worktree — the third cwd incident; the standing absolute-path rule
was violated by the coordinator). Repaired within minutes: the
stray commit removed (git reset + ledger checkout), Codex's own
newer commit and dirty in-flight state fully preserved, verified
clean. RULE HARDENED: every worktree-inspection command uses
git -C <path>; the coordinator shell never cd's into a worktree.

## 2026-08-06: wave-47 WCL-stream audit BANKED (integration executes after the F2 auditor)

- **WCL + remainder auditor (Opus) BANKED** (all replays exit 0;
  draft at notes/wave24_integration_20260727/WAVE47_WCL_DRAFT.md).
  HEADLINE: the WCL (1,5) SLOT CLOSURE IS REAL AND NOW STRONGER
  THAN CODEX'S OWN PROOF — the census completeness rested on an
  unreplayed Modal-volume artifact (2,296,920 affine-Galois
  classes, SHA-pinned only); the AUDITOR RE-DERIVED IT FROM SCRATCH
  by Burnside over |G| = 131072 (sum 301,061,898,240, remainder 0,
  EXACT MATCH) — corroborating completeness AND irredundancy at
  once. Certificates: tail-191 CADO factorization replayed 20/20
  (self-certifying — the heavy compute is NOT a trust dependency);
  193-hard-tail 17/17 with 400 independent primality proofs (own
  BPSW); node verifier 5/5 tamper controls; the CS supplier node's
  verifiers PASS. VERDICTS: ADOPT (tail-191 + 193 certs, zone
  10->9, the wcl16_delta6 fence, the supplier node, roadmap/CR
  shards, fiber_rigidity pilot); ADOPT-WITH-EDITS (easy census
  with the volume-resident residual stated; the PROVED promotion;
  the document decomposition WITH THE VERBATIM ADDENDUM RESTORED;
  verify.py + 2 constants); HOLD (the weight4 background->critical
  promotion — census-repricing, needs coordinator; the new
  sectioning schema). CATCHES: **W-3** (paraphrase-clobber of our
  ratified DSA addendum — similarity 0.37; surgical restore
  prescribed); **W-5** (PRE-EXISTING CANONICAL RED:
  rate_half_list_adjacent_crossing/verify.py FAILS at canonical
  HEAD — 7 stale edge expectations, Codex fixes 6, 2 remain; repair
  at integration); W-7 (the restored addendum's "MAINTAINER
  question" is stale — answered by ruling 85c9d1536; update text at
  restore); W-1 (opt-in tamper self-test reads as passed when
  skipped); W-4 (two sectioning schemas now competing); W-6
  (missing order fields). Honest residual: the easy census's 6.2M
  primality checks are attested, not re-run — methodologically
  independent + fail-closed, flagged. INTEGRATION DEFERRED to a
  single batch with the F2 stream (one compile, one verify chain).
  NOTE: the F2 auditor also owns a flagged "f2_admissible_object
  PROVED->REFUTED conflict" — awaiting its report.

## 2026-08-06: round-20 pilot 1 BANKED — THEOREM BB: a PROVED 72-BIT BUDGET-BREAK; the consequence is THRESHOLD RELOCATION

- **gamma_shell (Opus) BANKED, CAMPAIGN-CRITICAL, CANDIDATE
  CONFIRMED ON COORDINATOR REPLAY** (245,402 checks 0 failures; the
  coordinator re-ran every load-bearing stage incl. the
  exact-integer comparison AND re-derived the break arithmetic by
  hand). **LEMMA SL + THEOREM SM**: the deep-stratum accidents
  CONCENTRATE into 256 of 2^41 gamma-shells (factor 2^33; the
  registered danger-case prediction was exactly right); structural
  members equidistribute over 128 shells (2^117.149 each, [B4]
  reproduced). **THEOREM AC**: Cauchy-Schwarz accident lower bound
  N_acc >= 2^207.575 at the witness row (103 bits over round 18;
  1.5 bits below the banked heuristic, as required). **THEOREM BB**:
  max-shell X_{2^34} >= 2^199.575 vs B* = 2^127.510 — **a 72.065-bit
  PROVED budget-break; agreement k + 2^34 is UNSAFE;
  a_L(C) >= k + 2^34 + 1** on the break region (e >= 3 fully;
  e = 1 prime rows untouched and provably unreachable). Structural
  control within budget by 10.36 bits — the break is entirely the
  accidents. **THE HONEST TRIAGE (the pilot's finest hour)**: the
  consumer chain (hand-verified, req-only to the root on BOTH grand
  challenges) is existence/determination-shaped — (RHL-ADJ) cannot
  be falsified by a larger list, (RHL-LB) is STRENGTHENED, and the
  joint protocol's own words make relocation a valid resolution
  route. WHAT DIES: the safe-side pin at w = 2^34 on the break
  region (no route can establish safety there). THE RE-POSE: safe
  side moves to w = 2^35 (54-bit deep-stratum margin, stable across
  [2^35, 2^39]); THE NEW CRUX: an accident UPPER bound on shell
  populations (nothing supplies one). PT-2 honesty: the proved
  region is strictly inside the heuristic one; the v = 33 alarm
  stands un-upgraded. CATCH-B (es_g_lanes' usable-w pricing needs
  an accident term). Process: 3 bare-python3 text patches + 1
  subagent quarantine leak (no sibling exposure) — disclosed; RULE:
  pilots pass the quarantine clause to their subagents. Node
  addendum (crossing) composes into the wave-47 integration edit
  pass. Board: mystery 4 RESHAPED — the accident upper bound is the
  crossing lane's sharpest named obligation.

## 2026-08-06: round-20 pilot 2 BANKED — THE FINITE TARGET; the ensemble ruling re-opened; the scope question dissolved

- **f2_repose (Opus) BANKED, MAINTAINER-LEVEL** (60/60; the
  CATCH #11 anchor coordinator-verified; the five-class G1
  refutation independently confirmed by a third route). **CATCH-R1:
  the consumer's tolerance IS the counting-balance surplus — THE
  SEAM'S FIFTH FACE** (banked 2^{1.05e12} reproduced to 0.047%).
  UNDER (C) THE TERMINAL COLLAPSES TO A FINITE TARGET:
  **F2-MASS-N^3: Z(L) <= 1 + N^3 — Z_1 in a 4.77-BIT WINDOW
  [2^{17.98}, 2^{22.75}]** (open; falsifier registered; THEOREM 7
  misses by 9.79e11 bits). UNDER THE RULED (T*): NO CANDIDATE
  (CATCH-R6 — an EXACT-VALUE obligation; upper bounds dead as a
  class). **THE ENSEMBLE RULING IS RE-OPENED** (the consumer's own
  sentence uses both ensembles; existence-vs-death fork; the
  fence/contract reconciliation is a named task; the (C)-side
  finite target is the working obligation meanwhile). **THE SCOPE
  QUESTION DISSOLVES**: u2c CATCH #11 (2026-07-07) is the
  consumer-side k = e rule — extension rows route through f1/ext;
  k = 1 reduces VERBATIM to the PROVED f2_k1_contraction_theorem
  (bypassing (O1), covering the killer exhibit row); the right
  split is k = 1 vs k >= 2; **k in {2,4} is the uncovered residual**
  (+ the minus-branch generating types have the target but no
  object model). CATCH-R2 (consumer-chain arithmetic defect:
  n = 2^40 vs N = 2^41 — the tolerance flips negative by 4.9e10
  bits = BRIEF5's threshold; mint-queued). CATCH-R4 (our
  rounds-17/18 non-generating kill re-derived CATCH #11 —
  subtraction hit accepted). CATCH-R3/R5 ((O1) was UNDER-posed; the
  sum reading makes it a finite certificate). Median/C-S/partial-
  window candidates triaged (refuted / refuted / conditional on a
  nonexistent PP5.0 statement). The pilot's headline prereg REFUTED
  AT ITS OWN FALSIFIER — real risk taken, honestly reported.
  NODE-DRAFT delivered; mint composes with the wave-47 five-class
  correction.
- Awaiting: tail_count, crossing_gap; the wave-47 integration batch
  executes next.

## 2026-08-06: round-20 pilot 3 BANKED — the terminal's exact hard point: c* = 1/ln 2 - 1, zero margin

- **tail_count (Opus) BANKED** (111/111; banked values reproduced by
  disjoint paths). **CATCH-T1: the Prop-10 lead is a MIRAGE** (it
  telescopes to log2 P = S - sum d(c_s); no Dedekind content) —
  THIRD forced correction applied to f2_z1_mass_knife_edge; the
  open form of record is the NORMALIZED criterion
  Pr[P >= 2^{cS}] <= 2^{-cS+o(S)} (the +46.02 WAS the saturation
  constant; the knife edge re-identified as the c = 1 slack — a
  tail-side cross-validation). **THE BINDING LAYER: c* = 1/ln 2 - 1
  = 0.4426950409, ZERO flat-model margin** (measured 0.45 on every
  resolvable row) — no layer can be given away; no per-coordinate
  loss survives. STRUCTURE THEOREM: the tail IS a small-values/box
  count of the MDS value code ("C* is not unusually smooth").
  Endpoint layer PROVED (U_c = {0} for c > 1 - 2^{-124.19} —
  honestly an endpoint). BOTH supplies killed with thresholds (Z-2
  moments recover p <= 8.30 layer-by-layer; interpolation dead at
  EVERY p — position entropy H(1/L) > 1/L). THE NAMED DEFICIT:
  R-LOCALITY, factor log2 p / log2(e log2 p) = 8.60; the Fourier
  escape circular. **LEAD 2 FULLY EXPLAINED**: 288 = 16 + 16 + 16^2
  (decimation rank-collapse 7^4 x TWT x composition; residual = one
  2.6% Poisson orbit); **THEOREM 14: the decimation dichotomy —
  forced by saturation R/S = 1/log2 p — proves the creation
  mechanism CANNOT operate at F2 parameters** (a candidate
  refutation of the terminal removed; CATCH-T2: creation and
  discharge die at the same p <= O(1) shape). Honest misses: P6/H1
  + P7-reason refuted; one grid row mis-specified, declared
  UNREACHED. Board: the terminal = ONE question three ways (the
  finite window / the c* layer / the true rate function), no named
  route, deficit = R-locality; leads = a non-R-local instrument +
  the constant-weight cell + the fence/contract reconciliation.
- Awaiting: crossing_gap (the last of round 20); then the wave-47
  integration batch.

## 2026-08-06: round-20 pilot 4 BANKED — ROUND 20 COMPLETE: the even route dead, CW-FLOOR minted, PT-2 scope-corrected

- **crossing_gap (Opus) BANKED** (7,192/0; coordinator replayed the
  pt2 table and the exhaustive census). **CATCH-20B: the
  even-condition SP-COVER route is STRUCTURALLY DEAD** (even
  exponents are non-units; 0.00% closes; prime-row margin exactly
  2) — round-18 residual 5 closed by proof; the true recursion =
  PROPOSITION HT (the 2-adic Haar tower) + SP-COVER-R (new
  integrality gate) + **THEOREM SP-COUPLE** (exactly reproduces
  every observed census emptiness incl. the p = 7, w = 7 gate; the
  n-UNIFORM FORM is the low-w core's open lever). **THEOREM
  CW-FLOOR** (the constant-weight Z-FLOOR, from the round-19
  untested cell): PROVED, upgrades the heuristic tower-row excess
  to 2^205.7132 (vs DSA's 2^104.267), vacuous at prime rows by
  3.85 bits, unavailable at odd r' (proved), the break located at
  the cross-shell terms. **CATCH-20D (MAJOR, against the minted
  tern_master_threshold): the PT-2 clearance is p-DEPENDENT** —
  0.336 bits is the log2 p = 256 value only; the endpoint is
  first-moment supercritical on 57.98% (ternary) to 100% (GLOBAL)
  of the live prime range; NOT an emptiness refutation (proved
  regimes unreachable at prime rows; the e = 1 dichotomy
  re-verified); FOURTH forced correction applied (+ node.json
  dedup). CATCH-20A (w_cov(11)/(19) = 6, not 8 — REPORT-level,
  minted node unaffected); CATCH-20C (E-3's gap = 2^3.6869 —
  addendum written). C4: the exact residual stated; five dead
  routes named; four live levers (n-uniform SP-COUPLE, p-uniform
  CS, a NEW endpoint construction above 2^34.6467, anything in
  tau in (1, 1.585)). Registration discipline the round's best
  (13/14 held, five numerics to 4 decimals).

ROUND-20 NET (4/4): THEOREM BB (72-bit break = threshold
relocation; safe side w = 2^35; crux = the accident upper bound);
the FINITE TARGET Z <= 1 + N^3 (ensemble ruling re-opened; scope
dissolved; k in {2,4} residual); c* = 1/ln 2 - 1 at zero flat
margin (deficit = R-locality; both supplies dead); the even route
dead + CW-FLOOR + PT-2 corrected. FOUR forced corrections to
minted nodes in one round. NEXT: the wave-47 integration batch
(five-class correction + the WCL/F2 adoptions + the crossing-node
addendum + slot_1_5 census flip), then the round-21 board.

## 2026-08-07: WAVE-47 INTEGRATION EXECUTED — A RED CLOSED (246 -> 247 = 181/41/25)

The full adopted batch landed in one pass, all chains green:
- **dli_wcl_slot_1_5_emptiness TARGET -> PROVED** (Codex's proof;
  the auditor's Burnside closure of the census trust root
  [2,296,920 classes, remainder 0]; coordinator replay
  WCL15_CERTIFICATE_PASS) — **THE FIRST CRITICAL RED CLOSED this
  phase: math orbit 26 -> 25 targets** (247 = 181/41/25; submission
  262 = 193/43/26; pins repriced with provenance).
  dli_wcl_weight4_ambient_exclusion promoted background -> critical
  (FORCED by the adopted slot wiring — the partition law; the
  auditor's HOLD resolved by necessity, refs fixed).
- **13 F2 nodes adopted** (7 clean + 6 with coordinator addenda:
  the banked-identity citation, the truncated-fence widest reading,
  the superseded-upward note, the root-disjointness gap, the
  Hamming-vs-Fourier tail distinction, the retargeted edge) + the
  CS supplier node. THE FIVE-CLASS FORCED CORRECTION applied to
  f2_admissible_object + f2_o1_status_split (statement.md AND
  node.json; the auditor's REJECT-the-in-place-flip prescription
  honoured — G1/G2 narrowed to the plus branch, five signed types
  of record, survivors enumerated).
- **The crossing node**: statement addendum landed (THEOREM BB +
  the resolved maintainer question + the verifier note);
  **verify.py repaired GREEN for the first time** (Codex's wave-47
  version + the post-dating edges incl. the two ref-kind entries —
  the pre-existing W-5 red is dead, 224/224).
- WCL artifacts: wcl15_finish (tail-191 + 193 certs), wcl16_delta6
  fence, zone-coverage 10 -> 9, fiber_rigidity, roadmap shard 15 +
  CR-004, the tail-factor result. HELD (unchanged): the
  f2_conditional_close rewrite (awaits the f2_repose mint
  composition), the selector transport, the sectioning schema +
  decomposition (the verbatim-restore edit goes with it, wave 48).
- Site + orbit republished at the new census. WAVE 48 QUEUE: the
  post-pin Codex commits (selector handoff f8ad8cb5e, the
  aperiodicity corollary, f2_selector_face_primitive_reduction,
  + overnight work) — next audit cycle.

## 2026-08-07: MYSTERIES 5 & 6 PROMOTED (user-ratified) + ROUND 21 LAUNCHED

(Quarantine marker: round-21 pilots must not read ledger entries
below this line until the round completes.)

THE PROMOTION (recorded in the roadmap board section, r4 update):
generator_economy = MYSTERY 5 (the early-cap signal; kernel-lattice
alternative; ternary-bridge candidate); l1_mixed_petal_amplification
= MYSTERY 6 (retracted induction; residue-line growth = the named
obstruction; the un-surveyed ~133-commit Codex v4 PMA campaign).
The 25-red accounting of record: 14 mystery-linked / 9 WCL grind /
2 straddling (hge4 = sparsity in another jersey; dsp8 = pencil
satellite); two of the 14 possibly already closable.

ROUND 21 (4 agents):
- **PMA v4 auditor**: the un-surveyed Codex campaign
  (prize-codex-resolution-v4-20260713), audited against the CURRENT
  mystery-6 node incl. retraction-respect; draft to
  PMA_V4_AUDIT_DRAFT.md; blind to the l1 pilot.
- **gen_economy_diag (MYSTERY 5)**: consumer contract; the early
  cap quantified with an in-principle verdict; the TERNARY BRIDGE
  TEST under the round-19 graded discipline (construction-vs-
  exclusion duality, the tau side); the kernel-lattice route
  priced; the weakest-form re-pose.
- **l1_pma_diag (MYSTERY 6, blind to the auditor)**: the imgfib
  contract; the obstruction formalized; the MANDATORY adversarial
  construction attempt before believing the censuses; the
  cross-lane instrument matrix; the weakest-form re-pose.
- **red_closability_probes**: integer_code_distance_cert vs
  Z-1/Z-2 (the shift-0 scope check IS the probe);
  unsafe_crossing_family_instantiation vs THEOREM BB (the
  universality quantifier decides); certificates written where
  closable, no status flips (coordinator flips on replay).

## 2026-08-07: round-21 agent 1 BANKED — the v4 PMA "un-surveyed campaign" premise was FALSE; two catches against canonical, both applied

- **PMA v4 auditor (Opus) BANKED** (65/65 replays incl. mutation
  controls in 29/32; draft PMA_V4_AUDIT_DRAFT.md, 560 lines). THE
  PREMISE INVERTED: the campaign was ALREADY 100% IMPORTED at waves
  8-9 (2026-07-16/17), byte-identical, canonical ahead in every
  divergent file — zero novelty in the v4 -> canonical direction;
  the survey flag was stale. Retraction compliance PASS (3 tests;
  zero cut-node resurrections; addresses the dim-K obstruction by
  EXACT rank computation, not induction). The campaign
  self-retracted 8 times and caught itself everywhere — including
  un-proving its own previous day's headline. CATCHES (both against
  CANONICAL, both APPLIED as forced corrections):
  **C-V4-1**: the N10 census's reassuring reading is a FIELD-SIZE
  ARTIFACT — the second doubling doubles p, and the banked
  fixed-(n,k) control shows a 98.0%-exact 1/p retention law;
  field-corrected the growth exponent is FLAT at 6.14-6.21, ABOVE
  the separately-disproved n^6 line (the numerics and the proved
  obstruction point the SAME way). attack.md re-read applied;
  DECISIVE CONTROL QUEUED: the census at (64,32,97).
  **C-V4-2**: pma_sigma_one_variable_defect_exact_hit_floor's Scope
  clause cited the sigma >= C n/log n hypothesis STRUCK per #155 —
  replaced by the entropy-reserve justification (2048x margin,
  auditor-verified numerically). Survey flags retired in
  statement.md + attack.md. COMPUTE-LAW NOTE: ramguard unavailable
  in the subagent environment (systemd user bus, environmental) —
  a POSIX-rlimit shim reproducing the exact ceilings was used and
  disclosed; acceptable. MYSTERY-6 IMPACT: the diagnosis pilot's
  evidence base tilts HARDER (the friendly census reading is gone);
  the blind l1_pma_diag pilot reconciles at its bank.

## 2026-08-07: round-21 agent 2 BANKED — MYSTERY 5 DIAGNOSED: the construction refuted, the ceiling structural, the re-pose lands on kernel emptiness

- **gen_economy_diag (Opus) BANKED, MAINTAINER-LEVEL** (all scripts
  replayed; the collision identity coordinator-confirmed as
  arithmetic, not interpretive). **THE COLLISION CATCH (forced,
  applied)**: Pro-Brief-F's padding factor is exact e_1-collision
  multiplicity — the family has N' = 128 centers (the orbit of
  (1+x)), not 2^65.7; the "23.3-bit gap" is an **82.00-BIT
  DEFICIT**; the N' = 256 "pass" is FALSE; conditional.md was
  unsound as written (addendum applied); Pro brief H dead (same
  defect; same class as the REFUTED signed-8-core). **FLOOR-GE (the
  structural ceiling)**: 2-power-norm base sets certify at most
  N' + 1 centers INDEPENDENT of base count (exhaustive N = 8, 16;
  falsifier registered); template compression dead in principle;
  difference-set imports the dual problem (3/3 banked REFUTED).
  **THE CONTRACT DERIVED**: a 2^m family decides exactly
  q < 2^{m+161} — the construction route decides ZERO prize rows.
  **THE RE-POSE OF RECORD (GE-WEAK, coordinator-adopted)**: the
  node's obligation is the kernel-emptiness form (K_p has no
  non-cyclotomic ternary vector of support <= 2l') — the
  lattice-cone line, priced (Modal per pinned row at w <= 16,
  time 95 core-hours, MEMORY the binder at ~2^18x over ceiling;
  no finite row registry — the universal form is the open
  content). **THE BRIDGE VERDICT (the round-19 gates working)**:
  OBJECT partial (5-ary folded box fails the shape-pun test),
  REGIME pass, CRITICALITY pass-in-side (tau = 1.9531, the I2/I3
  subcritical cell; anti-numerology check: the banked 2^-50
  reproduced at 2^-47.1 unfitted) but FAIL-in-interval (the banked
  folded-box norm instrument starts at tau = 1.9957 — a 0.0426
  gap), METHOD partial-asymmetric. NO unification language; a
  genuine instance-family relationship on the exclusion side.
  COMPOSITION NOTE: mystery 5's re-posed obligation shares its
  object with integer_code_distance_cert — the running probes
  pilot's verdict composes directly. Honest self-corrections
  exemplary (R4's registered bar FAILED and says so; R3
  superseded; the wrong-ring PREREG flagged not patched).
- Awaiting: l1_pma_diag, red_closability_probes.

## 2026-08-07: round-21 agent 3 BANKED — BOTH CLOSABILITY PROBES: NO, with permanent named blockers; three banked-material catches

- **red_closability_probes (Opus) BANKED** (137/0 replayed; both
  fail-closed controls verified). **PROBE 1 (integer_code_distance_
  cert vs Z-1/Z-2): NOT CLOSABLE — permanently.** H1-H3 hold and
  the shift-0 scope check PASSES (my brief's "the scope check is
  the whole probe" was wrong — the pilot corrected it); the kill is
  H4: the system supplies ell = 1 condition vs ell = 65 needed, and
  ell = 1 is permanent by the REFUTED multi_multiplier_reduction
  (rank-1 outer product for EVERY k, re-verified at six cells).
  Z-2 at ell = 1 gives only weight >= 3 (attained). Bonus: the
  PROVED high-field branch covers 5.02% of the prime-row window.
  **PROBE 2 (unsafe_crossing_family_instantiation vs BB): CLOSES NO
  PART.** Wrong functional (L_1 vs B_C — the inference refuted by
  an exact finite countermodel L_1 = 6 > B* = 5 >= B_C = 5); BB's
  row coverage DISJOINT from the pair-feasible residual (which
  forces e = 1); form and endpoint mismatched (~1e6). Lead banked:
  BB's METHOD shape matches the M-route's nu(A) need. CATCHES
  (applied): P1 (folded_certificate's "min support 5" is the folded
  Hamming statistic; the node-relevant unfolded support is 7 — the
  wrong statistic in a certificate note); P2 (weight_graded_mitm's
  factor-N' speedup justified by a Frobenius map that is the
  IDENTITY under p = 1 mod N'; the saving survives via cyclic
  shift — mechanism corrected in a certificate node); P3 (the MCA
  node was filed under LIST.md — filing corrected both sides).
  ACCOUNTING UPDATE: "2 of the 14 possibly closable" -> **0** —
  the 14 mystery-linked reds hide no cheap wins; both blockers are
  structural and already-banked. The probes also COMPOSE with
  mystery 5's re-pose: integer_code_distance_cert is confirmed as
  the genuine open content of the kernel-lattice line (ell = 65
  conditions needed = the real problem; the transported laws serve
  the ell-condition system, which the k-multiplier route cannot
  manufacture).
- Awaiting: l1_pma_diag (the last of round 21).

## 2026-08-07: round-21 agent 4 BANKED — MYSTERY 6 WELL-POSED; the N10 census could never have fired its falsifier; ROUND 21 COMPLETE (4/4)

- **l1_pma_diag (Opus) BANKED, MAINTAINER-LEVEL.** All six scripts
  coordinator-replayed clean. (1) THE COUNTING DISSOLUTION: the N10
  candidate box has an EXACT degree-6 closed form (reproduces
  5,096/386,640/27,152,032 to the digit; cap n^6/2304 approached
  from below), so the registered super-polynomial falsifier was
  UNFIREABLE at ell=2 for every received word — the census was
  structurally incapable of testing what it was launched to test.
  Retained counts = the random-word law BOX/q (0.4-2% at n=32,64;
  doubling factor 38.58 predicted vs 38.00/38.01 banked, q-driven).
  C-V4-1 RECONCILED: the field-corrected 6.14-6.21 exponent is the
  exact polynomial's pre-asymptotic slope; "above the disproved n^6
  line" was a finite-size artifact; the queued (64,32,97) decisive
  control is SUPERSEDED by the derivation. (2) THE REAL PARAMETER:
  petal size ell, not n. Bucket EMPTY when sigma > 2*ell+b-2, else
  BOX = Theta(n^{4*ell+2b-4}); consumer regime needs ell =
  Omega(n/log n) (listing inequality), where BOX = n^{Theta(n/log
  n)} — census and consumer separated by Theta(n/log n) in the one
  parameter that matters. Measured danger: 44x for ell 2->4 at
  fixed n=24 vs 2,544x for three doublings of n. (3) THE MANDATORY
  ADVERSARIAL ATTEMPT FAILED, mechanism found: exhaustive over all
  830,490 legal words at n=16 (max 66 = 2.05x mean; banked consec
  word at 95th pct); filter spikes (69x) COLLAPSE under exact
  agreement (22x below mean) — degeneracy promotes codewords into
  higher-agreement strata; the bucket is self-limiting at fixed
  ell. Escape tests silent. (4) ZERO band-lane instruments transfer
  (matrix, all at hypothesis level); the one ambient match is a
  proved route cut. RE-POSE OF RECORD L1-MPA-w applied: clause (a)
  PROVED by counting (0.31 of 720 allowed columns at ell=2); clause
  (b) = growing-ell control carries the entire content; falsifiers
  F-w1/F-w2 registered. COMPUTE SWAP: L1-N10-128 DROPPED,
  L1-N10-ELL (fixed-n ell-sweep) is the decisive request; the
  n=24 row is already done locally at zero cost. Honest ledger:
  P5 falsified as written at one cell, P3 misses 10% at 1/6 cells,
  MAX32 a search lower bound — all labelled. Node addenda:
  statement.md (diagnosis + re-pose), attack.md (RESOLVED bracket);
  roadmap section 07 updated + recompiled.
- **ROUND 21 COMPLETE (4/4 banked).** Both promoted mysteries are
  now WELL-POSED with re-poses of record and registered falsifiers
  (5: GE-WEAK kernel emptiness; 6: L1-MPA-w growing-ell control);
  both closability hopes dead with permanent structural blockers.
  The 25-red accounting final: 14 mystery-linked (no cheap wins) /
  9 WCL-slot grind / 2 straddling.

## ROUND 22 LAUNCHED (2026-08-07) — QUARANTINE MARKER

Four pilots: l1_ell_sweep (mystery 6 F-w1 falsifier attempt),
ge_floor_falsifier (mystery 5 FLOOR-GE falsifier + GE-WEAK first
positive), bb_nu_transport (mystery 4, BB method -> accident upper
bound / nu(A)), f2_rlocality (mystery 2, the 8.60 R-locality
deficit). Pilots MUST NOT read ledger entries below this marker and
MUST pass this quarantine clause to any subagent they dispatch.

## 2026-08-07: WAVE-48 AUDIT COMPLETE (integration STAGED behind round 22)

- Delta audited: v11 cf4699f77..a55acc2fd + v12 to pin f7e850788
  (~2,027 files; 60 nodes added 50P/8T/2C; 6 status changes).
  Full audit: notes/wave24_integration_20260727/WAVE48_AUDIT_DRAFT.md.
- HEADLINE: Codex caught a FALSE GREEN on the Conjecture-F chain —
  conj_f + f_dim_induction + f_many_sparse_structure +
  f_primitive_case demoted PROVED -> CONDITIONAL. I verified all
  three semantic gaps against canonical's own texts (the Face-4
  routing-as-payment at f_many_sparse_structure/conditional.md:29;
  the dimension-dependent binom(n,r)/binom(j,r) at
  f_spread_moment_count/proof.md:34 vs the absolute B_F needed; the
  two-consumer scope). The wave-24 "auto-discharge exposure"
  landing on its largest target. ACCEPTED.
- The LIST Conjecture-F route is RETIRED (subtree -> background);
  imgfib re-routed to two exact L1 leaves; the FPC5 full-petal
  program replaces it on critical (rate-quarter M=4,t=2 PROVED
  with absolute bound 10 — spot-read sound; three payment leaves
  red). Critical reds 25 -> 28 (honest repricing).
- Verifier replays in the Codex tree: 91 PASS / 8 FAIL, all 8
  benign (4 background->critical path staleness in the moved PMA
  chain; 4 same-wave pin staleness). Fixes specified.
- Clobber checks CLEAN: my round-21 addenda relocated intact into
  Codex's landed sectioned-node schema (statement_sections/ +
  statement_addenda/); CATCH-P3 filing annotations intact.
- MERGE HELD until all four round-22 pilots report: the wave
  restructures l1_mixed_petal_amplification (read by l1_ell_sweep)
  and touches f2_z1_mass_knife_edge (read by f2_rlocality).

## 2026-08-07: round-22 agent 1 BANKED — bb_nu_transport: the FIRST accident upper bound of record (p-free, prime-row-reaching) + the M-route anti-transport PROVED

- **bb_nu_transport (Opus) BANKED, MAINTAINER-LEVEL** (1550/0
  replayed; fail-closed exits 1). (1) ANATOMY: BB's nine steps
  graded; registered 6-transport/3-fail split HELD EXACTLY, and the
  three failures (SM(1) concentration, THEOREM AC Cauchy-Schwarz,
  max>=mean pigeonhole) carry ALL of BB's quantitative power —
  concentration is the SOURCE of the accident problem, not a tool
  against it. (2) **PROPOSITION U2** (from the surviving
  scaffolding, BB-1+BB-2 only): Acc_deep <= M(2L,L-2) =
  (C(2L,L-2)+C(L,(L-2)/2))/(2L) — unconditional, p-FREE, exact
  Ramanathan/Lehmer gcd=2 closed form; at the witness row
  2^117.0820 vs B* = 2^127.5098 (+10.4278 bits, exact integers),
  below B* throughout v in [35,39], vacuous at v=34 (consistent
  with BB's proved break). Being p-free it reaches the e=1 PRIME
  rows BB provably cannot: coverage 8.64% (v=35) -> 99.67% (v=39)
  of the live prime window. Novelty honestly LOW (subtraction done:
  gamma_shell's banked gcd=1 structural count is the coprime case);
  value: the repo recorded "no upper bound on the shell population
  anywhere" three times. Consistency: brackets gamma_shell's proved
  floor at +1.436 bits (P6.6 HELD). 17 toy cells, three independent
  counters; measured U2 loss tracks Q=p (exactly the discarded
  relation). (3) **THEOREM AT (anti-transport), threshold exactly
  3**: RHS <= (3/2)N - N^2/(2Y); occupancy concentration kappa >= 3
  forces nu(A) <= 0; BB's deep-stratum kappa is 2^33 — shell
  concentration DESTROYS the M-route functional. The round-21 lead
  REVERSED: the M route needs a proved ANTI-concentration
  certificate (C_t(A) enters with a MINUS sign; E[N(A)] sees only
  |A|). Addendum applied to averaged_slope_conversion (wave-safe).
  (4) CRUX RELOCATED: X_w <= S(v) + Acc_deep + Acc_shallow now has
  two of three terms supplied; crux = Acc_shallow + aperiodic S =
  constant-weight BCH_w population cap in a prescribed sig class
  (LEMMA Y/MW equality at w <= p); the sharp deep route is gated by
  integer_code_distance_cert's min-l1 instrument — the THIRD lane
  converging on that one missing instrument (after GE-WEAK and
  PROBE-1). (5) Catches: T1 (gamma_shell prose ambiguity, artifact
  correct, note filed), T2 (0.067-bit near-collision flag), T3
  (pilot's own float bug, self-caught). The pilot's OWN P6.3
  falsifier prediction was falsified and it refused the upgrade
  (U3 stays heuristic, unused) — exemplary. DEFERRED: the U2
  addendum on rate_half_list_adjacent_crossing lands post-merge in
  the wave-48 sectioned schema.
- Awaiting: l1_ell_sweep, ge_floor_falsifier, f2_rlocality.

## 2026-08-07: round-22 agent 2 BANKED — ge_floor_falsifier: FLOOR-GE survives, its route-block DIES (exhaustive witness), PRICE-GE measured at the prize cell, and GE-WEAK per-row repriced by ~20 ORDERS

- **ge_floor_falsifier (Opus) BANKED, MAINTAINER-LEVEL** (selftest
  PASS; escape curve 9/9/17/17/17/17 exact; threshold tables and
  C-4 anchor replay exact; TIGHTEMPTY boundary witnesses Norm = p).
  (1) FLOOR-GE (k=0) SURVIVES: L_2adic = N'+1 PROVED-exhaustive at
  N'=8,16, independent implementation; its registered falsifier
  exhausted EMPTY. One odd ideal buys NOTHING (L_1 = L_0 — stronger
  than registered; H3 falsified honestly). (2) THE ROUTE-BLOCK
  DIES: L_2(8) = 2N'+1 = 17 > 9, exhaustive in centers AND ideal
  subsets, witness {0} u {+-1}^4 over both primes above 3 —
  FLOOR-GE must never be quoted as a cap once odd-prime bases are
  allowed. (3) PRICE-GE (floor of record, falsifier registered):
  ideal cost quadratic in orbit count; AT N'=128: 257 centers/140
  ideals (1.83/ideal) falling to 385/457 (0.84); the consumer's
  2^89 centers price at 2^88-2^170 ideals vs poly(128) — an
  82-163-bit ceiling, NORM-CLASS-FREE. Mystery 5's (a)-route dead
  without the round-21 caveat. (4) GE-WEAK (b) REPRICED ~20
  ORDERS: the folded kernel lattice is dim h=64 (not 128), det p,
  R/lambda1 = 0.551 at the prize cell — complete Fincke-Pohst
  emptiness certification = 2^27.4 nodes LLL-only (validated vs
  exhaustive brute force at h=4,8, deciding BOTH directions,
  10^3-10^4x); banked 2^188.2/Modal-scale figure corrected (its
  weight-split model valid only below w=28). lambda1>16 honestly
  labelled a REDISCOVERY of PRO_W3 prior art (subtraction done by
  the pilot itself); PRO_W3's "do not attempt" confirmed correct
  for N'=256/dim-128 and DISTINGUISHED from the prize cell.
  (5) UNIVERSAL toy thresholds (fold reduction made exact): every
  p = 1 mod 16 above 463249 (full radius) / 4049 (radius 6) has
  empty non-cyclotomic ternary kernel — the banked C-4 anchor
  generalized from one pinned prime to a congruence class, PLUS
  the scope catch: the SAME anchor prime p=12289 has 6 witnesses
  at FULL radius (consumers must respect the radius scope).
  (6) CATCH-1 forced correction on kernel_lattice_reframing: the
  ~2^-50 expected-hits is multiplicity-inflated 54.3 bits
  (existence 2^-101.4; 5^64 folded classes) — round-21's collision
  defect class, safer direction, applied. (7) Honest ledger: H4,
  H5 falsified (norm base pattern false at h=2, unconfirmed h=16;
  TIGHTEMPTY hugs MAXNORM within 0.41 bits — no norm-family
  threshold reaches prize rows, STRUCTURAL); two runs died on the
  ramguard wall with no verdict, reported; first cost functional
  5x loose, self-caught, superseded with headers. Addenda applied:
  generator_economy, kernel_lattice_reframing,
  lattice_cone_certificate, integer_code_distance_cert (all four
  byte-identical master-vs-v12 — merge-safe), + REPOSE_DRAFT D4
  superseded note. NEXT-MOVE CANDIDATE: execute the dim-64
  enumeration and certify pinned prize rows — mystery 5's first
  executable positive step.
- Awaiting: l1_ell_sweep, f2_rlocality.

## 2026-08-07: round-22 agent 3 BANKED — f2_rlocality: 8.60 retired (wrong layer), the deficit PROVED structural (LP floors), the banked instrument +1.7% from optimal, mystery 2's obligation NAMED — fourth lane onto the constant-weight instrument

- **f2_rlocality (Opus) BANKED, MAINTAINER-LEVEL** (47/0 across
  four verifier logs, coordinator-replayed; the k=2R LP wall death
  reproduced exactly as disclosed). (1) CATCH-RL1 APPLIED: 8.5990
  = DEF_INSTR(1) — correct arithmetic on the WRONG LAYER; at c = 1
  R-locality costs NOTHING (OPT_k(1) = p^{-k} EXACT — the c = 1
  requirement is met on the nose by pure R-locality, the knife-edge
  constant Delta the entire margin); the BINDING-layer deficit is
  6.3130; the node's own sentence mixed four numbers under one
  label (8.60 / 3.81 / 6.31 / 64). Decomposition at c*: THETA 1.000
  x AMGM 2.299 x GAUSS 1.035 x LOCALITY-CAP 2.654 — the cap is the
  lossiest step AND is sharp (N_{R+1} fails at all three toy rows).
  (2) CATCH-RL2 APPLIED: the "position entropy H(1/L) > 1/L / dies
  at every p" diagnosis WITHDRAWN (union-bound artifact; the exact
  R-local binomial moment cancels C(S,R), threshold at every
  log2 p >= 3.06); the route still dies numerically (258.9) — the
  wall is LOCALITY. (3) THE DEFICIT IS STRUCTURAL, now with
  floors: formalized k-LOCAL class, exact G1 full-LP floor 1.5889
  (p=41 row: 2.7651), lifted official-row floors 6.2063 (k=R) /
  3.4848 (k=2R, asymptotic evidence); the banked instrument
  (6.3130) is +1.7% from the k=R floor — essentially OPTIMAL; the
  1.81x headroom provably collapses back onto V_1 at the licensed
  radius (l1-weight accounting: k=2R forces J=1 = LEMMA 5's
  route). No sharpening attempt beats the banked instrument (A1
  deficit 64.0, A2 8.995, A3 258.9; all registered predictions
  hit). (4) MYSTERY 2'S OBLIGATION NAMED: a NON-LOCAL smoothness/
  box count for the GRS value code C* at exponential scale —
  quantifying over Theta(S) coordinates at once — and under the
  finite target's 4.77-bit window it must be essentially EXACT.
  Nearest banked object: the crossing-side constant-weight Z-FLOOR
  cell — the FOURTH lane converging on the constant-weight
  population instrument (after GE-WEAK, PROBE-1/ell-conditions,
  and the round-22 crossing crux). (5) Honest ledger: 14/14
  registered numeric bands hit; P13 UNRESOLVED reported; seven
  self-corrections all caught by the pilot's own controls; scipy
  refused by the wall -> from-scratch simplex (the compute law
  held against tooling friction). Corrections applied to
  f2_z1_mass_knife_edge (merge-safe) + tail_count coordinator
  note. ROUND-23 MATERIAL: price the constant-weight Z-FLOOR cell
  as the SHARED target of mysteries 2 and 4.
- Awaiting: l1_ell_sweep (the last of round 22).

## 2026-08-07: round-22 agent 4 BANKED — l1_ell_sweep: F-w1 EXHAUSTIVELY silent at the proper-band frontier; the falsifier itself sharpened; ROUND 22 COMPLETE (4/4)

- **l1_ell_sweep (Opus) BANKED, MAINTAINER-LEVEL** (gate ALL PASS
  three-path with character-identical histograms; degen_word closed
  form cross-checked against the full engine). (1) THE SWEEP went
  beyond brief: n=32 to ell=5 (the deepest PROPER-band cell,
  BOX = 1.6e9, exhaustive per word at 2e7 cand/s), n=24 to ell=6,
  n=64 added at ell=2,3. F-w1 SILENT everywhere (max ratio 0.091 of
  threshold) and EXHAUSTIVELY silent at FOUR cells (n=24 ell=4,5,6;
  n=32 ell=5): the word-uniform upper bound UB(c) enumerated the
  ENTIRE legal word space; the only flagged class (constant-scalar
  words) adjudicated exactly — RET = 0 PROVED for b <= 1, 0.0096 of
  threshold at b = 2. No received word of the chart family can fire
  F-w1 at those cells. (2) THE LAW IN ELL holds to 0.1% at the
  three largest cells; no amplification signal at any ell <= 6, any
  n <= 64. (3) FALSIFIER SHARPENED (to apply post-merge): the
  10*BOX/q normaliser LOOSENS with ell (2.9x at n=32 ell=5 — in the
  content-bearing regime); the re-pose of record moves to
  10*N_{k+1}(ell)/q, against which the law is flat (RET =
  (1-1/q)^{n-k-1} N_{k+1}/q to ~1%, NO ell dependence). (4) BUG
  CAUGHT in round-21's d3_ell_sweep.py (b<=1-only filter; two
  failure modes; unquoted n=16 ell=3 zero is wrong, true 100); NO
  banked number affected; warning note filed. (5) P0 brief
  correction: n=24 ell=5,6 are t=2/band-VACUOUS (my brief plotted
  them on the floor-band curve in error — pilot corrected before
  computing). (6) Off-family band test: with the band OFF, exact-
  agreement still enforces sigma <= Lambda (measured max k+3 vs
  formal k+11) — clause (a) robust beyond its definition; the band
  is a real 48.6x restriction. (7) The round-21 ~16% mindeg excess
  is a coset-layout ell=2 (mu_2 antipodal) phenomenon — 0.20% at
  ell=4; does not grow. (8) Extrapolation honestly labelled:
  census/consumer regimes separated ~10^12 in log2 mass by
  q^{-sigma}; says nothing about adversarial words (the open
  content); t-direction caveat stated. Modal lines filed in the
  audit (48-4 best value 23 CPU-h; 64-5 DO-NOT-LAUNCH).
- **ROUND 22 COMPLETE (4/4).** Aggregate: PROPOSITION U2 (first
  accident cap of record, p-free) + THEOREM AT (anti-transport) +
  FLOOR-GE two-sided resolution with the ~20-order (b)-route
  repricing + the 8.60 retirement with proved LP floors (+1.7%
  optimality) + F-w1 exhaustive silence with a sharpened
  normaliser. FOUR lanes now converge on the constant-weight /
  ternary-min-distance instrument cluster. NEXT: the wave-48 merge
  (staged, audit complete) + post-merge obligations.

## 2026-08-07: WAVE-48 INTEGRATED — the Conjecture-F false-green repair lands; census 231 = 167/36/28 (reds 25 -> 28); the sectioned-node schema adopted

- MERGE executed at pin f7e850788 after round-22 completion (clean;
  no conflicts). The four demotions (conj_f chain PROVED ->
  CONDITIONAL) verified against canonical texts BEFORE the merge
  (audit f2ac06dd6); the LIST Conjecture-F route retired to
  background; the FPC5 program is on critical with 3 payment reds
  (rate-quarter PROVED, absolute bound 10). Census of record:
  math 231 = 167/36/28, submission 246 = 179/38/29 — recomputed on
  my side, pins updated with provenance.
- POST-MERGE FIXES (all verified): 8 stale verifiers repaired (4
  background->critical path repoints in the moved PMA chain; 4 pin
  refreshes preserving semantic intent, incl. the FPC5
  TARGET->CONDITIONAL router repin + the u2c born-red edge rewire
  pin); 22 untracked ghost folders deleted (both-side move
  leftovers, every one verified a pure duplicate of its tracked
  home before deletion); zero partition-law warnings; full chain
  GREEN (dag 1905/5291, sectioned-node docs PASS).
- DEFERRED ADDENDA APPLIED into the sectioned schema (registry
  extended in tools/refactor_critical_node_documents.py):
  statement_addenda/14-round22-u2-accident-cap.md on the crossing
  node (PROPOSITION U2 + crux relocation);
  statement_addenda/07-round22-ell-sweep.md on
  l1_mixed_petal_amplification (F-w1 exhaustive silence + THE
  NORMALISER AMENDMENT: F-w1 of record is now retained >
  10*N_{k+1}(ell)/q). L1-N10-128 marked DROPPED in the compute
  queue; L1-N10-ELL-48-4/64-4 filed PARKED, 64-5 DO-NOT-LAUNCH.
- RED ACCOUNTING on the 28-board: 14 mystery-linked + 9 WCL-slot
  grind + 2 straddling + 3 NEW FPC5 exact official-cell
  obligations (UNCLASSIFIED until a diagnosis round — do not force
  them into a bucket). Round-23 candidates: the FPC5 diagnosis;
  the constant-weight Z-FLOOR cell priced as the SHARED target of
  mysteries 2 and 4; the dim-64 lattice certification run
  (mystery 5's first executable positive step).

## 2026-08-07: WAVE-49 INTEGRATED + FULL PR SWEEP (1144-1151) + upstream check — census UNCHANGED 231 = 167/36/28

- **WAVE 49 (Codex v12 through eef69b37f) ADOPTED.** 9 nodes, all
  kb_m2_r4 112-lane + LS6 + crossing fence; 8/9 verifiers PASS
  (9th is a statement-only TARGET). The import discipline is
  exemplary and REPLAYED: Scott's PR #1144 ten moving cells PROVED
  via independent Sage 10.9 replays (7 direct + M01->M02 literal
  transport + operational M00-R11; fail-closed verifier, payload
  hash + 29 mutations); the two unreplayable cells (M01-R11 +
  companion) held at a PROVABLE REVIEW GATE — the external
  Singular slimgb basis fails to convert in THREE environments;
  NOT promoted. PR #1149's quadratic frontier imported as the
  orbit-compression node (pinned at 55ac3e07). HONEST
  SELF-DEMOTION verified: source_line_complete_exclusion PROVED ->
  CONDITIONAL (combinatorial orbits are not automatically
  covariance orbits) with the explicit literal-assignment-coverage
  TARGET born (36 cells, 22 PROVED, residual = M01-R11, M02-R11,
  twelve F04-F07). l1_fpc5_ratehalf_ls6_canonical_owner_packing
  PROVED (FPC5-lane progress on the rate-half red).
- **PR SWEEP 1144-1151:** #1144/#1141/#1149 (scottdhughes) =
  imported by wave 49 behind gates (the M2 EXPORT COLLISION is
  RESOLVED: Scott pushed his side 08-01; our LS6 ladder went up as
  #1151 today; clean division, no clobber). #1145-#1148 (maelcar
  = Manuel E. Rey-Alvarez Zafiria) = already fully audited
  2026-08-03 (notes/pilots_20260803/maelcar_audit/AUDIT.md:
  VERIFIED at certificate level with per-flag ledger F1-F11; its
  F10 became task #36 SOL_TARGET_4 repricing, completed);
  RE-REPLAYED today: 1146 parity-uniform S6 audit PASS, 1145 both
  audits PASS, 1147 both verifies PASS (currencies reproduce),
  1148 synthesis + Cauchy route cut + bidegree barrier PASS. No
  change upstream since (updatedAt 08-03/08-04); the C++ sieve
  loads remain UNREPLAYED as labelled. #1150 (ours, F2 census)
  awaiting triage upstream. **Upstream main UNMOVED since
  93fba1be** — nothing new in Przemek's repo.
- **PROCESS DISCLOSURE + RULE:** the wave-48 merge used FETCH_HEAD
  at fetch time, which had drifted a few commits past the audit
  pin f7e850788 (Codex commits continuously) — the drifted commits
  are exactly the wave-49 set, all replayed and key-read TODAY, so
  nothing unaudited is on canonical; but the RULE OF RECORD is now:
  merge the EXACT audited pin SHA, never FETCH_HEAD.
- Census unchanged (background satellites): site/artifact current
  by invariance. Codex has one uncommitted node in progress in the
  v12 worktree (fixed_balanced_quadratic_branch_reduction) — left
  untouched; it belongs to wave 50.

## ROUND 23 LAUNCHED (2026-08-07) — QUARANTINE MARKER

Four pilots: cw_shared_target (the constant-weight instrument priced
as the SHARED target of mysteries 2 and 4 — the four-lane
convergence play), fpc5_diag (the three new FPC5 reds: standard
grind or mystery-hard), ge_lattice_cert (the dim-64 per-row
emptiness certification EXECUTED — mystery 5's first positive step),
c2pp_diag (mystery 3 C1'/C2'' — the full diagnosis pipeline it never
had). Pilots MUST NOT read ledger entries below this marker and MUST
pass this quarantine clause to any subagent they dispatch.

## 2026-08-07: round-23 agent 1 BANKED — c2pp_diag: the twice-survived C2'' margin is an ARTIFACT (theta-fragile + selection-biased); the evidence ledger reset symmetrically; C2''-r3 is the pose of record

- **c2pp_diag (Opus) BANKED, MAINTAINER-LEVEL** (all four scripts
  coordinator-replayed; positive controls bit-exact against the
  banked packet). (1) BRIEF CORRECTED by the pilot before
  computing: C2'' had survived TWO F-rounds (M1 + c2r2); my brief
  conflated that with the 2026-07-07 kill of the predecessors —
  this round is F-ROUND 3, and it properly minted a NEW falsifier
  family instead of replaying. (2) THE THETA KILL (no new
  transport needed): the pose's "insensitive for theta in [2,4]"
  claim REFUTED on its own 8 rows — F-b's own kill rule FIRES at
  every theta in {2.5, 3, 4} (x_max 1.0662 -> 2.2387; 14.53% ->
  182.71% of reserve; 35.3-bit spread across the declared-
  immaterial range). The 85% margin was manufactured by the
  theta=2 accident cut (two classes clearing it by 0.24/0.14).
  (3) SELECTION BIAS: all three original falsifiers excluded the
  high-loss cells by three different mechanisms (F-b's b>0 filter;
  F-c's window cap; F-a's stripped object). (4) THE STATEMENT GAP:
  the `_reduced` qualifier separating the defended clause from the
  wired claim lives in ONE line of ONE script and is dropped by
  the very next use; clause (i) conflates internal-correlation-
  freedom (true) with contribution-freedom (false — conditioning
  shifts weight INTO the coset class up to 21.8x); clause (iii)
  "counted once" non-conservative at 2/8 rows. (5) THE HONEST
  PEAK: the pilot's own F-d overflow (482%) RETIRED TOGETHER with
  the survivals under the now-binding SYMMETRIC not-evidence
  clause — uniform 33x stacking is evidence in NEITHER direction
  (Pro's 2026-08-01 demotion + the 32-wise trap now recorded on
  the node). (6) RE-POSE OF RECORD ADOPTED: C2''-r3 — the
  unreduced junction-sum form the consumer actually needs;
  falsifiers G-a/G-b demand >= 8 CONSECUTIVE junctions of a
  SINGLE tower. STANDING: C2'' is UNMEASURED AT ITS OWN QUANTIFIER
  DEPTH; the decisive instrument does not exist in the repo
  (Modal-scale, M1-shaped) — round-24 candidate: spec + price it.
  (7) Catches C-1..C-8 ALL APPLIED (statement addendum; node.json
  path/rounds/notes fixes; the roadmap FD-schema gate adjudicated
  UNSUPPORTED — H2 has no live instance). No status flip (TARGET
  stays); census unchanged; chain green. The risk register had
  anticipated exactly this outcome.
- Awaiting: cw_shared_target, fpc5_diag, ge_lattice_cert.

## 2026-08-07: round-23 agent 2 BANKED — cw_shared_target: ONE OBJECT, TWO TARGETS; CONJECTURE Z-CEILING minted as mystery 2's candidate closure; the first official-row datum on the shared functional

- **cw_shared_target (Opus) BANKED, MAINTAINER-LEVEL** (130/29
  replayed exactly; every FAIL an itemized registered miss; G1/G4
  licensing controls bit-exact from a fresh code path). (1) THE
  VERDICT: the four-lane convergence is real on the OBJECT
  (mystery 4's deep-stratum population IS mystery 2's ternary
  theta TMASS via the LEMMA TC bijection — 20/20 fold-vs-brute +
  12/12 vs banked N_acc; weight distortion GDEV exactly computed,
  max = Theta(sqrt L)) and on the DIRECTION (both need the upper
  companion of proved floors), but NOT on the bottleneck: mystery
  2 pays a 0-bit bridge; mystery 4's live crux (Acc_shallow +
  aperiodic S) sits off the periodic strata and its only bridge
  (collision/C-S) loses 0.31-0.50 of kappa*log2 p = >= 4.565e11
  bits at the official row vs a 54.45-bit tolerance (ratio
  8.4e9). TWO SEPARATE TARGETS; no unification language; round-19
  gates graded. (2) **CONJECTURE Z-CEILING** (the upper companion
  of THEOREM Z-FLOOR): sharp EXCESS form FALSIFIED by the pilot's
  own registered adversarial search at (16,2,3137) (EXCESS 2.3463,
  growing along SIGMA -> -inf) BEFORE proposal; ratio form
  survives 7,000+ exhaustive 2-power cells at C <= 1.2610; iff
  C < 2^4.77 it closes mystery 2's finite target with 4.44 bits
  headroom (and the terminal is open ONLY under the exact-balance
  reading); load-bearing hypothesis = the 2-power grid (composite
  2L: EXCESS 178.51, linear in p). Recorded on
  f2_z1_mass_knife_edge with the NORMALIZATION PIN (the banked
  factor-2 calibration covers RATIO only; EXCESS exceeds 2 in
  f2's own family — the pilot's catch). (3) THE FIRST
  OFFICIAL-ROW DATUM on the shared functional: THEOREM BB's
  2^199.575 floor composed with the TC identity => the official
  ternary theta sits 11.84 bits BELOW its volume heuristic —
  consistent with the ceiling. (4) The crossing ledger updated
  (statement_addenda/15): deep stratum settled at v >= 35 by the
  TRIVIAL bound; the ceiling would de-vacuum only v=34 e=1 prime
  rows (+2.09 bits, conditional); Acc_shallow NOT bridged — the
  crux stays PRIMAL and unshared. (5) SC-1: the pilot's kappa = e
  defect caught because it CONTRADICTED BANKED BB by 73.575 bits
  — the tripwire mechanism working as designed; four registered
  predictions falsified and reported; subtraction disclosed up
  front. DEFERRED: the integer_code_distance_cert qualification
  waits for ge_lattice_cert (reading that node now). ROUND-24
  CANDIDATES: a Z-CEILING proof attempt; the primal BCH
  population cap as its own brief.
- Awaiting: fpc5_diag, ge_lattice_cert.

## 2026-08-07: round-23 agent 3 BANKED — fpc5_diag: ALL THREE FPC5 reds are MYSTERY-HARD against ONE wall (MF), with the first quantitative handles; a mystery-7 promotion question SURFACED

- **fpc5_diag (Opus) BANKED, MAINTAINER-LEVEL** (identity table +
  official constants + A1 gate + the cap-4 adversary all
  coordinator-replayed exactly). (1) THE STRUCTURE: the
  CODIMENSION-RESERVE IDENTITY codim(F-flat) = sigma holds
  identically (verified ell = 4..39 both families, matching the
  nodes' printed codims) => every FPC5 first moment is
  <= 2^{-7.948e12} at the official row — NONE of the three reds is
  a counting problem; all are max-to-mean on a Theta(n)-dim flat.
  The single statement (MF) specializes exactly to all three AND
  to upstream prob:capfr1-master-flatness: shape-pun test PASSES —
  ONE WALL. The mystery-6-style counting rescue is dead in advance
  (box = binom(N, 0.4N), exponential). (2) RED 1: the pilot
  invented a STRONGER adversary than the node's own attack surface
  (the guarded flat is C-independent => core-choosable set
  packing, exhaustive sound BB) and it stops DEAD at 4 —
  q-INVARIANT (8x more split members at q=193, still 4), flat in
  ell, 0 hits on the official domain; ~1200x adversarial gain over
  the mean, then a wall. Scope pin: the banked nonemptiness census
  is label-free (factor ~q = 85x measured); sharpened overlap cap
  |D cap D'| <= 2s-b derived and witness-checked. (3) RED 2: the
  live LS6 tail is PROVABLY UNREACHABLE by any census ever
  (minimal cell binom(42,17) = 2.5e11); at the off-tail cell the
  atom is generic to 2%, the measured packing cap EQUALS the
  proved Bonferroni cap (instrument tight), and 52.4% of the atom
  sits at the TRIVIAL owner G=1 where the fixed-owner theorem is
  worthless — the binding problem is OWNER-QUALITY, not the
  owner-count the attack list targets. (4) RED 3: least defended;
  the registered exposure FIRED as an exposure (408 unsieved
  residual rows, e up to n/3; no t>=4 overlap theorem; no
  background guard; t <= M always; touched-subset multiplicity is
  FREE — the attack note aims at a non-obstruction). THE NAMED
  GATE: the t-petal overlap-cap lemma (proved at t=2,3) legalizes
  the whole precomputed J-sieve at a stroke. (5) Honest ledger:
  one disclosed compute-law slip (errored, zero contamination),
  the unsound prune self-caught (answer unchanged), two
  registered-not-run cells, the free-domain relaxation disclosed.
  Addenda applied to all three red nodes. **SURFACED (user's
  call): promote the (MF) master split-locator flatness wall to
  MYSTERY 7?** Accounting if ratified: 28 = 14 + 9 + 2 + 3(MF).
  Round-24 candidates: the ell=4 finite decision; the base-cover
  number; the t-petal overlap-cap lemma (highest single-lemma
  leverage on the board).
- Awaiting: ge_lattice_cert (the last of round 23).

## USER RULING + ROUND 23B LAUNCHED (2026-08-07) — QUARANTINE MARKER

RULING (user): mystery 7 is created ONLY on proof or strong
evidence via UNSUCCESSFUL FALSIFICATION that the three FPC5 reds
share one wall. The round-23 shape-pun identification is
statement-level and does NOT meet the bar by itself. Launched:
mf_wall_adversary — attack the classification; registered
separation attempts + a mandatory falsifier-power control.
Pilots MUST NOT read ledger entries below this marker; the live
ge_lattice_cert dir is off-limits; banked round-23 dirs
(fpc5_diag, cw_shared_target, c2pp_diag) are READABLE sources.

## 2026-08-07: round-23 agent 4 BANKED — ge_lattice_cert: E1-128 CERTIFIED EMPTY (complete transcript, STATUS FLIP TARGET->PROVED) + CATCH-23A (the round-22 enumerator was not fail-closed); ROUND 23 PROPER COMPLETE (4/4; 23b out)

- **ge_lattice_cert (Opus) BANKED, MAINTAINER-LEVEL.**
  (1) **E1-128 CERTIFIED EMPTY** at the literal pinned Pocklington
  field/root: complete Fincke-Pohst enumeration, 2,061,127,954
  nodes, 12/12 shards byte-identical basis, deterministic
  standalone checker (independent Bareiss det = p => L(B) =
  Lambda_p), planted fail-closed control AT full dimension found
  by the same code path (seed-reproducible, zero imports). The
  first complete transcript for the cell the repo ruled
  "explicitly inconclusive" under BKZ. **STATUS FLIP APPLIED on
  replay: e1_folded_no_vector_certificate_128_payload TARGET ->
  PROVED**, certificate banked into the node; census unchanged
  (background satellite); chain green. The status ruling's
  literal-exhibit half is SUPPLIED; family-uniform + consumer
  narrowing remain (no other flip). (2) **CATCH-23A**: round-22's
  d4_cone.py floors a rational FP window — NOT fail-closed;
  witness counts superseded at 3/6 rows (2->8, 6->16, 2->16) with
  a structural proof (witness sets are full <sigma,-1>-orbits of
  size 2h; the partial sets were not sigma-closed); ALL verdicts
  survive (brute-force re-confirmed); corrections applied to
  lattice_cone_certificate + warning note in the round-22 dir;
  TIGHTEMPTY/D3 unaffected. (3) **PRICE-CLIFF**: the round-22
  laptop-scale reclassification holds only above ~242 bits
  (measured 2^30.94 at 249 bits); at the four DEPLOYED Proth rows
  (167-171 bits) the full-radius cell costs 2^60-63 LLL / 2^38-40
  BKZ-90 — those rows now carry radius-graded COMPLETE
  certificates to support <= 24 (12 swaps = the node's own named
  MITM radius; archimedean-free radius is only 6), full radius
  UNRESOLVED + priced. (4) **GS-FLOOR OBSTRUCTION (proved)**: a
  lambda_1-floor certificate needs p > (4h)^{h/2} = the AM-GM
  ceiling = 2^256 at h=64 = the spec's field cap — NO admissible
  N'=128 row escapes enumeration; only its price moves; the
  253^32 branch's 0.544-bit sliver is the entire free region.
  (5) Six deployed clean-anchor rows priced: rate-1/8 FLIPS to
  expected-EMPTY; 1/4 and 1/16 expected-NONEMPTY => the
  e1_folded_certificate_manifest_payload cannot close its N'=256
  entry as written (addendum applied; re-pose needed). (6) Honest
  ledger: G1 re-gated on brute force under disclosed amendment
  when the gold standard proved broken; Q2 falsified (+3.5 bits,
  cause identified); the sharding race caught BY the fail-closed
  merge refusing a verdict; prior art subtracted (lambda_1>16 and
  the 2^48 figure are PRO_W3's). Deferred cw qualification
  applied to integer_code_distance_cert alongside.
- **ROUND 23 PROPER COMPLETE (4/4).** Aggregate: mystery 3
  adjudicated (evidence reset, C2''-r3, unmeasured-at-depth);
  mysteries 2/4 split at the bottleneck with Z-CEILING minted and
  an official-row consistency datum; the three FPC5 reds
  classified one-wall-candidate (promotion gated on 23b's
  falsification attempt per the user's ruling); mystery 5's
  per-row line EXECUTED with a red closed. Round-24 queue: the
  full-radius Proth Modal request; the family-uniform brief; the
  Z-CEILING proof attempt; the t-petal overlap-cap lemma; the
  >= 8-junction C2'' instrument spec.
- Awaiting: mf_wall_adversary (round 23b).

## 2026-08-07: round-23b BANKED — mf_wall_adversary: the round-23 evidence BROKEN and REBUILT stronger; the user's bar MET for a SCOPED mystery-7 core; ROUND 23 FULLY COMPLETE

- **mf_wall_adversary (Opus) BANKED, MAINTAINER-LEVEL** (s4_power /
  ledger / red3_split / rh_bucket coordinator-replayed exactly).
  (1) THE BREAK: the round-23 shape-pun test FAILED the hard power
  control — the PROVED rate-quarter sibling satisfies EVERY (MF)
  clause with strictly better margins (the separating clause,
  over-determination t*ell > N, is not part of (MF)); both
  round-23 quantitative handles WITHDRAWN as classification
  evidence (cap-4 is structure-specific — a random flat with
  identical parameters reaches 5; owner concentration is 92x its
  parametric reference). Handles remain valid node-level findings.
  (2) THE REBUILD: the repaired round-19 METHOD test passed ALL
  THREE power controls; then ALL separation attempts FAILED for
  reds 1+2 — SAME WALL: the dimension-uniform split-locator
  max-to-mean theorem (the anticode exponent grows with flat
  dimension; both nodes say it in their own words). The wall is
  BIGGER than FPC5: METHOD-identical at the PROVED rootfree
  packing cell's open d = Theta(n) regime AND at
  f_global_packing_step (the conj_f packing leaf — identical
  formula, identically named n^r failure). (3) RED 3 UNDECIDED:
  65.2% of its residual (266/408 rows) is not posable as a flat
  without the t-petal overlap-cap lemma. (4) STRENGTHENED: cap-4
  exact at ell=4,5,6 (329 configs, 3 primes, exhaustive BB);
  sharpened cap ell-3 tight at every ell; budget elasticity
  (+1..+4, stiffens with ell); mechanism at ell>=5 UNIDENTIFIED.
  Upstream master-flatness has ZERO discriminating power (PROVED
  nodes are instances; round-23's "one statement" over-reach
  corrected; |B|^{-s} vs q^{-sigma} mismatch flagged). (5) Honest
  ledger: the pilot's own separation candidate dissolved, its own
  mechanism prediction falsified, a mid-run false witness (16)
  self-caught and withdrawn with cause, the strict ell=4 decision
  scoped out in advance (5.6e10 configs). Addenda applied to the
  three red nodes + f_global_packing_step. **SURFACED: the user's
  bar (strong evidence via unsuccessful falsification) is MET for
  mystery 7 SCOPED to red1 + red2 + f_global_packing_step + the
  rootfree d=Theta(n) regime — "the dimension-uniform
  split-locator max-to-mean wall"; red 3 joins on the t-petal
  lemma; upstream master-flatness NOT claimed as the same wall.**
- **ROUND 23 FULLY COMPLETE (5/5).** The single
  highest-leverage item, doubly confirmed: the t-petal
  overlap-cap lemma.

## 2026-08-07: round-23b POSTSCRIPT — the pilot's second final message banked; CATCH-23B (coordinator process defect, rule hardened)

- The mf_wall_adversary pilot emitted a SECOND corrected final
  message (its first was premature — two runs in flight). VERDICT
  UNCHANGED; three refinements recorded (the W1 ell=5
  filter-mismatch caveat — falsification rests on the clean
  matched ell=4 arms + the ell=5 random arm at 5; the
  necessity-vs-sufficiency asymmetry of the one-wall claim;
  two unreached cells named). Appendix persisted to REPORT.md;
  audit postscript written.
- **CATCH-23B (mine):** banking artifacts were written into the
  LIVE pilot dir because banking began on the first notification
  without confirming quiescence; the pilot correctly flagged and
  did not rely on them. RULE HARDENED: confirm pilot quiescence
  (no in-flight runs / fresh checkpoints) before persisting
  REPORT.md or writing FABLE_AUDIT.md into a pilot dir.

## 2026-08-07: round-23b THIRD message — W1 falsification now on TWO matched cells; verdict unchanged; 23b closed

- The mf_wall_adversary pilot closed its own last gap: the ell=5
  W1 arm completed fully matched (guarded 4 vs random 5, overlaps
  ell-3 vs ell-3+1) — the cap-4's structure-specificity now rests
  on two independent matched cells; the withdrawn MAXPACK-16
  anomaly corroborated seed-specific. Nothing else changes. The
  provenance flag = CATCH-23B (resolved, rule standing). 23b is
  CLOSED.

## 2026-08-07: MYSTERY 7 RATIFIED (user) — the dimension-uniform split-locator max-to-mean wall; board r5

- Membership: the two FPC5 rate-half reds + f_global_packing_step
  + the d = Theta(n) open regime of the PROVED rootfree packing
  cell. NOT members: the large-source red (UNDECIDED pending the
  t-petal lemma) and upstream master-flatness (no discriminating
  power). Red accounting: 28 = 16 mystery-linked / 9 WCL-grind /
  2 straddling / 1 undecided. Board of record updated (roadmap
  section 12 r5, recompiled); membership lines on the three member
  nodes. Basis: 23b unsuccessful falsification against a
  power-validated test (the user's bar).

## 2026-08-07: round-23b final quiescence — writer identity CONFIRMED; 23b closed for good

- The mf_wall_adversary pilot's final state check: all processes
  exited cleanly, the killed watcher was a no-op (no measurement
  lost), no writes outside its dir. Its request for "one human
  glance to confirm the writer" is ANSWERED ON THE RECORD: the
  coordinator (Fable) authored REPORT.md (verbatim transcript
  persistence, per standing practice) and FABLE_AUDIT.md, at the
  timestamps the pilot inferred — no stray process, no other
  pilot. CATCH-23B (banking before quiescence) stands as the
  process lesson; the quiescence rule is in force. The 23b verdict
  is final as banked and MYSTERY 7 is ratified on it (7ad7f5ec2).

## 2026-08-07: WAVE-50 INTEGRATED (exact pin 3fa2922e3) — 13 PROVED K3 nodes, 13/13 verifiers replayed; coverage registry 26/36; census unchanged

- Delta eef69b37f..3fa2922e3: 13 new PROVED nodes, ALL on the
  kb_m2_r4 diagonal C2 112 fixed-residual lane (degree-12 branch
  closures across R02/R20/F04: rank-drop, s-zero, degree-six
  leading curves, the K8 branch cover + B0 K8-nonzero exclusion,
  the F04-R02 and four-R02 branch exclusions; plus two portable
  instruments: the parity-reduced quadratic evaluation identity
  (+ its expanded-route fence) and the quadratic pseudo-remainder
  determinant reduction). The only status change in the delta is
  our own E1-128 flip arriving via branch convergence. 13/13
  verifiers coordinator-replayed AT THE PIN. Board effect: the
  literal-assignment coverage TARGET's registry moves 22 -> 26 of
  36 PROVED; residual = the review-gated M01-R11/M02-R11 pair +
  eight F04-F07 cells over R02/R20. Merge = EXACT PIN (the wave-49
  rule followed); Codex's in-flight work (log-derivative probes +
  two new node dirs) left untouched for wave 51. Census unchanged
  231 = 167/36/28 (background satellites); full chain green.
- PROCESS NEAR-MISS disclosed: replaying at the pin used checkout
  + stash in Codex's LIVE worktree (detached HEAD, stashed its
  dirty state); fully restored (branch re-attached, stash popped,
  state byte-identical). RULE HARDENED: never checkout/stash in
  Codex's live worktree — replay at the current HEAD when it
  equals the pin, or extract files via git -C show into the
  scratchpad.

## 2026-08-08: WAVE-51 INTEGRATED (exact pin ac7d90f26) — THE LITERAL COVERAGE CAMPAIGN CLOSES: 41 new PROVED + 4 flips, 44/44 verifiers replayed at the pin; census unchanged

- Delta 3fa2922e3..ac7d90f26 (31 commits): the kb_m2_r4 112
  source-line campaign COMPLETES. FOUR STATUS FLIPS, all verified:
  (1) source_line_literal_assignment_coverage TARGET -> PROVED —
  the wave-49-born coverage obligation closed at 36/36 aligned-
  positive cells (disjoint seven-packet census) + the near-positive
  branch (108 cells -> 42 orbits via two exact restricted q-slice
  transports, direct exclusions + finite survivors rejected by
  first-quotient replay) + aligned-negative + negative source-line
  + 48 literal projective boundary cells; (2) source_line_complete_
  exclusion CONDITIONAL -> PROVED (its wave-49 conditional
  obligation was exactly this coverage theorem — the honest
  demotion repaid in full); (3) the M01-R11 REVIEW GATE PROVABLE ->
  PROVED — discharged the RIGHT way: a direct exact Singular replay
  at the pinned PR #1144 commit (fresh augmented slimgb basis size
  168 dim 2; all 148 deterministic blocks of the 151,178-term I
  polynomial reduced; the serial parity replay routes fenced) —
  the independent replay the gate demanded in wave 49, not a
  gate surrender; (4) e1_folded_certificate_cell_128_payload
  CONDITIONAL -> PROVED by propagation from OUR round-23 E1-128
  certificate flip (no verifier; conditional discharged). Plus 41
  new PROVED nodes (the seven census packets, the branch-closure
  chain, the 433-1b cell4 campaign opening). 44/44 verifiers
  coordinator-replayed AT the pin (worktree HEAD == pin; no
  checkout — the wave-50 rule held). Census UNCHANGED at
  231 = 167/36/28 / submission 246 (background satellites);
  full chain green incl. sectioned-node docs.
- BOARD EFFECT: the K3/kb_m2_r4 lane's source-line branch is now
  FULLY PROVED end-to-end (the wave-49 self-demotion + coverage
  TARGET arc closed in two days); the m2-export-collision material
  (Scott's PRs 1141/1144/1149) is completely absorbed with every
  cell independently replayed. Codex's in-flight (wave 52): the
  positive 433-1b cell4 ledger continues (one untracked experiment
  file left untouched).

## 2026-08-08: WAVE-51 REPAIR — CATCH-W51: Codex broke the sectioned-archive invariant; repaired by extraction, chain restored GREEN

- POST-MERGE the sectioned-node verify FAILED: three wave-51
  commits appended 53 lines of live 433-1b campaign progress
  IN-PLACE to the ARCHIVED attack_sections/12 packet of
  rate_half_band_closure, breaking the lossless-decomposition sha
  pin. Codex's OWN tree fails its OWN verifier (it does not run it
  in its loop). REPAIR per the schema's semantics: the section
  restored to its archived bytes; the 53 lines extracted VERBATIM
  to attack_addenda/13-wave51-positive-433-cell4-campaign.md with
  a provenance header stating the rule; registered in
  document.json + the tool (addenda tuple AND index text) + the
  attack.md index. Full chain GREEN (sectioned PASS, dag PASS,
  census unchanged). STANDING RULE FOR THE WORKER (to propagate
  via merge): campaign progress on sectioned nodes goes in
  attack_addenda/, NEVER in attack_sections/; wave audits now
  include running verify_sectioned in the Codex tree at the pin
  BEFORE merging.

## ROUND 24 LAUNCHED (2026-08-08) — QUARANTINE MARKER

The high-impact conjecture falsification fleet (user directive:
select the conjectures whose truth gives the biggest gains; try to
falsify/sharpen them): z_ceiling_assault (mystery 2's candidate
closure attacked in its worst directions + tractable-subfamily
proof attempts), kernel_window_hunt (the family-uniform emptiness
falsifier — the norm-cofactor prime hunt in the admissible window,
with the N'=256 positive control), t_petal_lemma (prove-or-refute
the overlap cap at t>=4 — the board's highest single-lemma
leverage), c2pp_gb_probe (C2''-r3's registered G-b falsifier
executed at toy scale — the first evidence-bearing C2''
measurement). Pilots MUST NOT read ledger entries below this
marker and MUST pass this quarantine clause to any subagent.

## 2026-08-08: round-24 agents 1+2 BANKED — the t-petal lemma WAS ALREADY OURS (sieve legalized; red 3 posable; CATCH-24A minted); Z-CEILING SURVIVES repriced to C >= 1.7681 with THEOREM RC

- **t_petal_lemma BANKED**: (JB3) at h = t*ell IS the lemma —
  proved all along in l1_fixed_support_defect_johnson_bound; six
  names hid it from three rounds (CATCH-24A: hard law 5's own-repo
  grep now GATES every named-gate pricing). General-t proof
  written + coordinator-verified (degree counting, no syzygy);
  refutation search 0 violations at MIN_SLACK 0 with power
  control firing; payoff executed (J-sieve legal at every t; 156
  rows' payment legalized; residual 408 verbatim-identical). NEW:
  the slice-dimension theorem dim V = e+1 at every t (391 cells +
  proof draft) — RED 3'S MYSTERY-7 MEMBERSHIP NOW DECIDABLE; the
  disjointness hypothesis free for primitive members. Next: audit
  CJ2/CJ3 at M >= 5 (71 rows); the 23b membership test on red 3.
- **z_ceiling_assault BANKED**: SURVIVES 59,203 cells; constant
  repriced 1.2610 -> >= 1.7681 (headroom 3.95 bits); sigma -> -inf
  proved safe; THEOREM RC proved (kernel dead above N^{N/2}; each
  N-line a finite max); scope pinned (general subspaces FALSE at
  25.23; the 2-power gate sharp with the composite closed form);
  S2 EQUIVALENCE: Z-CEILING = the non-local smoothness-mass input
  restated faithfully. CATCH-Z24-A applied (CZ-M count formula
  false at two-odd-prime n; spine re-confirmed). Named next: the
  N = 32 sigma~0 band (new algorithm/Modal).
- Awaiting: kernel_window_hunt, c2pp_gb_probe.

## 2026-08-08: round-24 agent 3 BANKED — FAMILY-UNIFORM EMPTINESS IS FALSE (proven-prime witness at N'=128; the N'=256 falsifiers were banked-and-missed since July); the narrowing decision SURFACED

- kernel_window_hunt BANKED: REPRO PASS replayed (Norm(w) = P
  exactly at the BLS-proven 247-bit P = 1 mod 128 < 2^256; support
  127 <= 2l'; non-cyclotomic). 20,636 W_TOP hits. CATCH-24C: the
  e1_n256 audit dismissed a 248-bit witness as "harmless" via the
  wrong bar (prize-interval vs admissibility) — eight N'=256
  falsifiers banked since July, conclusion never drawn. DEPLOYED
  ROWS PROTECTED: v_2(p-1) = 7 generic vs 92-200 pinned. The
  pilot self-amended its novelty claims when its sweep returned
  (two retractions; headline free). Addenda applied
  (integer_code_distance_cert board event; generator_economy
  universal reading refuted; CATCH-24C). CATCH-24B disclosed
  (my broad git add swept this live pilot's dir; explicit-path
  rule restated). USER DECISION SURFACED: exhibit-scoped /
  o(1)-sparsity / large-v_2 narrowing.
- Awaiting: c2pp_gb_probe (the last of round 24).

## 2026-08-08: round-24 agent 4 BANKED — BOTH C2'' falsifiers are dead as tests (G-b vacuous by theorem; G-a unreachable at 2^203 states); the freeze law + the first non-stacked r3 datapoint (4.5x); ROUND 24 COMPLETE (4/4)

- c2pp_gb_probe BANKED (verify_law ALL CHECKS PASS replayed;
  criterion scoring replayed; positive control 8/8 bit-exact).
  G-b WITHDRAWN (omega_j's denominator is q-free => the junction
  sum is schedule-bounded — firing impossible, silence
  uninformative); G-a needs redesign (census squaring law: J=8
  costs 2^203). Keepers: THE FREEZE LAW (census freezes at
  log2 q = n/t; the official row lives entirely pre-saturation);
  the middle-peaked shape; GB-5: R3_W = 11.34 bits over 4
  junctions vs 2.545 window-scaled (4.5x, no transport claimed) —
  the escalation target. Addendum applied; falsifier redesign =
  round-25 item.
- **ROUND 24 COMPLETE (4/4): the falsification fleet's ledger —
  one conjecture KILLED before we chased it (family-uniform
  emptiness, with the narrowing decision surfaced), one conjecture
  SURVIVED and repriced (Z-CEILING at C >= 1.7681 + THEOREM RC +
  the equivalence finding), one "missing lemma" FOUND ALREADY
  PROVED in-repo (the sieve legalized, red 3 posable, CATCH-24A),
  and one falsifier pair RETIRED by theorem with the first honest
  datapoint on mystery 3's object. Four catches (24A own-repo
  gate; 24B explicit-path adds; 24C filter bars; Z24-A count
  formula). Round-25 queue: the narrowing decision execution; the
  C2'' falsifier redesign + GB-5 escalation; the N=32 sigma~0
  Z-CEILING band; the CJ2/CJ3 chart audit; red 3's membership
  test on the newly posable rows; wave-52.**
## 2026-08-08: CODEX WAVE-52 READY (pin 25cf3aedf) — cell-4 pairing-3/6 exact close; honest quotient composition

- The deployed positive `433-1b -> O0a` cell-4 pairing-3 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The direct exceptional-root ledger has 312 candidate roots, 272
  guarded source points, 96 nonzero colored terminals, 16 `f=0` boundaries,
  zero witnesses, and zero unresolved branches. Final Modal app
  `ap-VnOKofCGaEWi6SM8IN26qj`; independent finite replay PASS.
- Exact quotient audit first added only `(xi,pairing)=(2,6)`, producing a
  64-case four-label/two-orbit block. A proposed six-label count was rejected
  because the parallel-DE involution exchanges `xi=0,1` at fixed matching.
- A separate direct pairing-6 campaign then closed both positive omissions:
  16 computed + 16 transported raw cases, 160 candidate roots, 176 guarded
  source points, 48 missing-sum survivors, 96 nonzero colored terminals, and
  zero boundaries/witnesses/unresolved. Final app
  `ap-xIKZhX3GDN2uknjpfoFBMn`. The complete pairing-3/6 block is 96 raw
  cases; cell 4 is now 15/105 paid labels, with 90 labels in 51 quotient
  orbits live.
- Four new background PROVED nodes; critical census unchanged at
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and negative-control checks pass at the pin. Fable canonical remained at
  `5c98633e1`; upstream main remained at `93fba1be`.

## 2026-08-08: CODEX WAVE-53 READY (pin 1faf2902a) — cell-4 pairing-4 exact close; positive pairing-9 correctly retained

- The deployed positive `433-1b -> O0a` cell-4 matching-4 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The degree-eight, division-free exceptional-root ledger has 352
  candidate roots, 384 guarded source points, 1,088 nonzero missing-relation
  terminals, 64 nonzero colored terminals, 16 `f=0` boundaries, zero
  witnesses, and zero unresolved branches. Final Modal app
  `ap-d0Snabe8KIXbHW06cTgXe1`; independent finite replay PASS.
- Exact quotient composition adds only `(xi,pairing)=(2,9)`. The involution
  exchanges `xi=0,1` at fixed matching, so `(0,9),(1,9)` remain open. The
  new payment is four labels in two orbits and 64 raw cases.
- Two new background PROVED nodes; cell 4 is now 19/105 paid labels with 86
  labels in 49 quotient orbits live. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and negative-control checks pass. Fable canonical remains `5c98633e1`;
  upstream main remains `93fba1be`.

## 2026-08-08: CODEX WAVE-54 READY (pin 114db05ae) — positive pairing-9 closed; complete pairing-4/9 block

- The retained positive matching-9 omissions are PROVED empty: 16 computed
  `xi=0` rows plus 16 identical-copy transports. The exact ledger has 288
  candidate roots, 544 guarded source points, 1,280 nonzero missing-relation
  terminals, 192 nonzero colored terminals, and zero boundaries, witnesses,
  or unresolved branches. Final Modal app `ap-LHmTRosR90JHKDnuGjh8oI`;
  independent finite replay PASS.
- Composing with Wave 53 closes all six labels in `{0,1,2} x {4,9}`: three
  quotient orbits and 96 raw cases. Cell 4 is now 21/105 paid labels, with 84
  labels in 48 quotient orbits live. The next orbit is `{5,12}`.
- Two new background PROVED nodes; critical census remains `231=167/36/28`.
  Sectioned-document, DAG, crosswalk, orbit, focused replay, and negative-
  control checks pass. Fable canonical remains `5c98633e1`; upstream main
  remains `93fba1be`.

## 2026-08-08: CODEX WAVE-55 READY (pin 99e0e55ff) — cell-4 pairing-5 exact close; positive pairing-12 retained

- The deployed positive `433-1b -> O0a` cell-4 matching-5 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The division-free degree-eight ledger has 320 candidate roots,
  288 guarded source points, 960 nonzero missing-relation terminals, 64
  nonzero colored terminals, 16 `f=0` boundaries, zero witnesses, and zero
  unresolved branches. Final Modal app `ap-MuHmcgibJfx736RiVWp2vE`;
  independent finite replay PASS.
- Exact quotient composition adds only `(xi,pairing)=(2,12)`. The involution
  exchanges `xi=0,1` at fixed matching, so `(0,12),(1,12)` remain open. The
  new payment is four labels in two orbits and 64 raw cases.
- Two new background PROVED nodes; cell 4 is now 25/105 paid labels with 80
  labels in 46 quotient orbits live. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and negative-control checks pass. Fable canonical remains `5c98633e1`;
  upstream main remains `93fba1be`.

## 2026-08-08: CODEX WAVE-56 READY (pin a5f911ca5) — positive pairing-12 closed; complete pairing-5/12 block

- The retained positive matching-12 omissions are PROVED empty: 16 computed
  `xi=0` rows plus 16 identical-copy transports. The exact ledger has 224
  candidate roots, 320 guarded source points, 960 nonzero missing-relation
  terminals, 128 nonzero colored terminals, and zero boundaries, witnesses,
  or unresolved branches. Final Modal app `ap-3ssYWiGc9bn3vctPUZcPAj`;
  independent finite replay PASS.
- Composing with Wave 55 closes all six labels in `{0,1,2} x {5,12}`: three
  quotient orbits and 96 raw cases. Cell 4 is now 27/105 paid labels, with 78
  labels in 45 quotient orbits live. The next orbit is `{7,10}`.
- Two new background PROVED nodes; critical census remains `231=167/36/28`.
  Sectioned-document, DAG, crosswalk, orbit, focused replay, and negative-
  control checks pass. Fable canonical remains `5c98633e1`; upstream main
  remains `93fba1be`.

## 2026-08-08: CODEX WAVE-57 READY (pin 08fec0333) — cell-4 pairing-7 exact close; positive pairing-10 retained

- The deployed positive `433-1b -> O0a` cell-4 matching-7 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The division-free degree-eight ledger has 352 candidate roots,
  384 guarded source points, 1,088 nonzero missing-relation terminals, 64
  nonzero colored terminals, 16 `f=0` boundaries, zero witnesses, and zero
  unresolved branches. Final Modal app `ap-tl4qnwUTevKIzsxlTPRLyT`;
  independent finite replay PASS.
- Exact quotient composition adds only `(xi,pairing)=(2,10)`. The involution
  exchanges `xi=0,1` at fixed matching, so `(0,10),(1,10)` remain open. The
  new payment is four labels in two orbits and 64 raw cases.
- Two new background PROVED nodes; cell 4 is now 31/105 paid labels with 74
  labels in 43 quotient orbits live. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and negative-control checks pass. Fable canonical remains `5c98633e1`;
  upstream main remains `93fba1be`. The next exact target is positive
  matching 10.

## 2026-08-08: CODEX WAVE-58 READY (pin d158091e2) — positive pairing-10 closed; complete pairing-7/10 block

- The retained positive matching-10 omissions are PROVED empty: 16 computed
  `xi=0` rows plus 16 identical-copy transports. The exact degree-eight
  ledger has 288 candidate roots, 544 guarded source points, 1,280 nonzero
  missing-relation terminals, 192 nonzero colored terminals, and zero
  boundaries, witnesses, or unresolved branches. Final Modal app
  `ap-vg9F2A5OL2rHsqLlmEu0ao`; independent finite replay PASS.
- Composing with Wave 57 closes all six labels in
  `{0,1,2} x {7,10}`: three quotient orbits and 96 raw cases. Cell 4 is now
  33/105 paid labels, with 72 labels in 42 quotient orbits live. The next
  parallel-`DE` orbit is `{8,13}`.
- Two new background PROVED nodes; critical census remains `231=167/36/28`.
  Sectioned-document, DAG, crosswalk, orbit, focused replay, and negative-
  control checks pass. Fable canonical remains `5c98633e1`; upstream main
  remains `93fba1be`.

## 2026-08-08: CODEX WAVE-59 READY (pin e5bca6df3) — cell-4 pairing-8 exact close; positive pairing-13 retained

- The deployed positive `433-1b -> O0a` cell-4 matching-8 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The division-free degree-eight ledger has 320 candidate roots,
  288 target roots, 288 guarded source points, 960 nonzero missing-relation
  terminals, 64 nonzero colored terminals, 16 `f=0` boundaries, zero
  witnesses, and zero unresolved branches. Final Modal app
  `ap-rpCUgXeECUEAWWOjI2Ma2S`; independent finite replay PASS.
- Exact quotient composition adds only `(xi,pairing)=(2,13)`. The involution
  exchanges `xi=0,1` at fixed matching, so `(0,13),(1,13)` remain open. The
  new payment is four labels in two orbits and 64 raw cases.
- Two new background PROVED nodes; cell 4 is now 37/105 paid labels with 68
  labels in 40 quotient orbits live. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and negative-control checks pass. Fable canonical is `860e22c47`;
  upstream main remains `93fba1be`. The next exact target is positive
  matching 13.

## 2026-08-08: CODEX WAVE-60 READY (pin 30cd1dada) — positive pairing-13 closed; complete pairing-8/13 block

- The retained positive matching-13 omissions are PROVED empty: 16 computed
  `xi=0` rows plus 16 identical-copy transports. The exact degree-eight
  ledger has 224 candidate roots, 208 target roots, 320 guarded source
  points, 960 nonzero missing-relation terminals, 128 nonzero colored
  terminals, and zero boundaries, witnesses, or unresolved branches. Final
  Modal app `ap-Dxy9l3OPbvPHbjXD6Fb1ul`; independent finite replay PASS.
- The independent verifier caught a stale matching-8 scalar replay in the
  first draft even though its symbolic matching-13 eliminant was correct.
  Both the pilot and census were rerun after repair; the invalid preliminary
  payload is not evidence for this theorem.
- Composing with Wave 59 closes all six labels in
  `{0,1,2} x {8,13}`: three quotient orbits and 96 raw cases. Cell 4 is now
  39/105 paid labels, with 66 labels in 39 quotient orbits live. The final
  small-missing orbit is `{11,14}`.
- Two new background PROVED nodes; critical census remains `231=167/36/28`.
  Sectioned-document, DAG, crosswalk, orbit, focused replay, and negative-
  control checks pass. Fable canonical is `110aa4e73`; upstream main remains
  `93fba1be`.

## 2026-08-08: CODEX WAVE-61 READY (pin 0aa6c7c41) — cell-4 pairing-11 exact close; positive pairing-14 retained

- The deployed positive `433-1b -> O0a` cell-4 matching-11 block is PROVED:
  32 exact computed rows plus 16 identical-positive-copy transports close 48
  raw cases. The common-`f` resultant ledger has 304 candidate roots, 240
  target roots, 192 guarded source points, 64 nonboundary quartic candidates,
  64 nonzero colored terminals, 16 `f=0` boundaries, zero witnesses, and
  zero unresolved branches. Final Modal app `ap-kFJQZFlwV86ixm21ONfYJR`;
  independent quadratic-intersection and quartic-root replay PASS.
- Exact quotient composition adds only `(xi,pairing)=(2,14)`. The involution
  exchanges `xi=0,1` at fixed matching, so `(0,14),(1,14)` remain open. The
  new payment is four labels in two orbits and 64 raw cases.
- Two new background PROVED nodes; cell 4 is now 43/105 paid labels with 62
  labels in 37 quotient orbits live. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, focused replay,
  and scope checks pass. Fable canonical is `00e28e1ba`; upstream main is
  `999b8f3a1`. The next exact target is positive matching 14.

## 2026-08-08: CODEX WAVE-62 READY (pin 599b7afb2) — positive pairing-14 closed; parallel-DE layer complete

- The retained positive matching-14 omissions are PROVED empty: 16 computed
  `xi=0` rows plus 16 identical-copy transports. The exact common-`f` ledger
  has 152 candidate roots, 120 target roots, 80 guarded source points, 128
  nonboundary quartic candidates, 128 nonzero colored terminals, and zero
  boundaries, witnesses, or unresolved branches. Final Modal app
  `ap-pw5ZlqWXn640JjkVYlv221`; independent root and final-cut replay PASS.
- Composing with Wave 61 closes all six labels in
  `{0,1,2} x {11,14}`: three quotient orbits and 96 raw cases. All
  `3*15=45` parallel-`DE` labels are now closed.
- Two new background PROVED nodes; cell 4 is now 45/105 paid labels with 60
  labels in 36 quotient orbits live. The live set is exactly the nonparallel
  missing roles `xi in {3,4,5,6}`. Critical census remains
  `231=167/36/28`. Sectioned-document, DAG, crosswalk, orbit, independent
  replay, and scope checks pass. Fable canonical is `00e28e1ba`; upstream
  main is `999b8f3a1`.

## 2026-08-08: CODEX WAVE-63 READY (pin e404201d6) — both cell-4 endpoint roles closed

- Missing `bf` and missing `sigma_c cf` obey the same source-only necessary
  identity `(x^2+m)^2-s*x^2=0`, with `x=b` or `x=c`. It precedes every
  matching and target-sign equation.
- Eight exact four-basis norm rows have 40 compatibility roots and 56 total
  norm/inverse candidates. The terminal ledger is 40 `r` guards, 8 `t`
  guards, 8 nonsquare `b` discriminants, and zero guarded source points,
  compatible sources, or unresolved branches. Final Modal app
  `ap-e2M3bp83ckyLVeO9wqmAtd`; independent root and lift replay PASS.
- One new background PROVED node pays 30 labels, 18 quotient orbits, and 480
  raw cases. Cell 4 is now 75/105 paid with exactly `xi in {3,4}` live: 30
  labels in 18 quotient orbits. Critical census remains `231=167/36/28`.
  Sectioned-document, DAG, crosswalk, orbit, and protocol checks pass.
  Fable canonical is `00e28e1ba`; upstream main is `999b8f3a1`.

## 2026-08-08: CODEX WAVE-64 READY (pin 7327fd5f9) — universal xi4/xi3 transport proved

- The signed outside-role involution transposes exactly the `df` and
  `sigma_o ef` atlas rows and fixes compact residual order, matching index,
  guards, signs, lanes, and every one of the 15 common role cells.
- The primary sparse-polynomial certificate checks 3,600 exact system
  bijections. An independent integer implementation checks 31,104 rows.
- One new background PROVED node pays no label by itself but halves the live
  independent cell-4 obligation: the 30 labels in 18 `xi in {3,4}` quotient
  orbits reduce to 15 `xi=3` labels in nine matching-exchange orbits.
  Critical census remains `231=167/36/28`; all structural gates pass.
  Fable canonical is `00e28e1ba`; upstream reference main is `999b8f3a1`.

## 2026-08-08: CODEX WAVE-65 READY (pin 38c0f89a1) — cell-4 xi3/xi4 pairing 0 closed

- Missing `df` at matching 0 is PROVED empty. The three exhaustive
  `paired(q,q)` coefficient-ratio branches reduce to two quadratics in
  `y=1/d^2`; their division-free resultant is normed through the exact
  four-basis source tower.
- Across 24 internal branch rows, the complete ledger has 200 candidate
  `r` roots, 72 guarded source points, 24 empty denominator branches, 64
  reciprocal-square candidates, 128 nonzero final-pair checks, and zero
  target boundaries, witnesses, free branches, or unresolved strata. Final
  Modal app `ap-ymGV72om2LOXCwxR8zKKlr`; independent root, source-lift, and
  target replay PASS.
- The universal outside-role transport pays the matching-0 `xi=4` partner
  with no duplicate computation. Two new background PROVED nodes pay 32 raw
  cases, two labels, and two quotient orbits. Cell 4 is now 77/105 paid;
  28 labels in 16 quotient orbits remain, requiring 14 independent `xi=3`
  proofs in eight matching-exchange orbits.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, and refactor checks pass.
  Fable canonical is `00e28e1ba`; upstream reference pin is `93fba1be`.

## 2026-08-08: CODEX WAVE-66 READY (pin d2cdb61c0) — cell-4 xi3/xi4 pairings 1-2 closed

- Missing `df` at matchings 1 and 2 is PROVED empty. Three exhaustive
  coefficient-ratio branches reduce each row to an even missing-sum quartic
  and a matching-specific paired quadratic in `z=1/d`. Their exact linear
  remainder gives a division-free common-root cut in the four-basis tower.
- Across 36 branch rows, the complete ledger has 360 candidate `r` roots,
  216 guarded source points, 32 common `z` lifts, 64 nonzero final-lane
  checks, and zero target boundaries, witnesses, free branches, or
  unresolved strata. Final Modal app `ap-FvpQcJ8FuxEK0TRI6DiZet`;
  independent root-union and finite-lift replay PASS.
- Universal outside-role transport supplies both `xi=4` partners. Two new
  background PROVED nodes pay 64 raw cases, four labels, and four quotient
  orbits. Cell 4 is now 81/105 paid; 24 labels in 12 quotient orbits remain,
  represented by 12 `xi=3` labels in six matching-exchange pairs.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, and refactor checks pass.
  Fable canonical is `00e28e1ba`; upstream reference pin is `93fba1be`.

## 2026-08-08: CODEX WAVE-67 READY (pin 817b1dcb0) — cell-4 xi3/xi4 pairing-3/6 orbit closed

- Missing `df` at matching 3 is PROVED empty. The colored-pair quartic is
  split into its even/odd `z` parts, sign-eliminated in `y=z^2`, and reduced
  modulo the missing-sum quadratic to a linear-remainder common-root cut.
- Across eight rows, the exact ledger has 60 candidate `r` roots, 16 guarded
  source points, eight common `z` lifts, and zero common roots between the
  antipodal and outside-pair q quartics. There are no target boundaries,
  witnesses, free branches, or unresolved strata. Final Modal app
  `ap-6XSVCn7sZu2uToXIzZ9J3E`; independent degree-1112 root-union and finite
  replay PASS.
- Parallel-`DE` matching exchange supplies pairing 6, and universal
  outside-role transport supplies both `xi=4` partners. Two new background
  PROVED nodes pay 64 raw cases, four labels, and two quotient orbits. Cell
  4 is now 85/105 paid; 20 labels in 10 quotient orbits remain, represented
  by ten `xi=3` labels in five matching-exchange pairs.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, and refactor checks pass.
  Fable canonical is `00e28e1ba`; upstream reference pin is `93fba1be`.

## 2026-08-08: CODEX WAVE-68 READY (pin 7eec52b69) — cell-4 xi3/xi4 pairing-4/9 orbit closed

- Missing `df` at matching 4 is PROVED empty. Nested sign elimination in
  `q` and `z` reduces the first two paired equations and the missing-sum
  equation to a linear-remainder common-root cut in the exact four-basis
  source tower.
- Across four source-sign rows, the exact ledger has four degree-5108 norms,
  56 candidate `r` roots, 56 guarded source points, 32 compatible `z`
  values, 32 compatible `q` values, and 128 nonzero third-pair lane
  evaluations. There are no target boundaries, witnesses, free branches, or
  unresolved strata. Final Modal app `ap-wroUJycnzyUOJqETrQHZt4`;
  independent root-union and finite replay PASS in 253 seconds under the
  1 GB RAMguard ceiling.
- Parallel-`DE` matching exchange supplies pairing 9, and universal
  outside-role transport supplies both `xi=4` partners. Two new background
  PROVED nodes pay 64 raw cases, four labels, and two quotient orbits. Cell
  4 is now 89/105 paid; 16 labels in eight quotient orbits remain,
  represented by eight `xi=3` labels in four matching-exchange pairs.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, manifest, and refactor checks
  pass. Fable canonical is `00e28e1ba`; upstream reference pin is
  `93fba1be`. The next exact target is representative matching 5.

## 2026-08-08: CODEX WAVE-69 READY (pin bca792862) — cell-4 xi3/xi4 pairing-5/12 orbit closed

- Missing `df` at matching 5 is PROVED empty. Nested sign elimination in
  `q` and `z` reduces the antipodal and colored second-pair equations plus
  the missing-sum equation to a linear-remainder common-root cut in the
  exact four-basis source tower.
- Across eight source-sign/`sigma_c` rows, the exact ledger has eight degree-
  5058 norms, 104 candidate `r` roots, 128 guarded source points, 32
  compatible `z` values, 32 compatible `q` values, and 64 nonzero third-
  pair lane evaluations. There are no target boundaries, witnesses, free
  branches, or unresolved strata. Final Modal app
  `ap-U8FZQRqn5ocilCEg0xtzQY`; independent root-union and finite replay PASS
  in 256 seconds under the 1 GB RAMguard ceiling.
- Parallel-`DE` matching exchange supplies pairing 12, and universal
  outside-role transport supplies both `xi=4` partners. Two new background
  PROVED nodes pay 64 raw cases, four labels, and two quotient orbits. Cell
  4 is now 93/105 paid; 12 labels in six quotient orbits remain, represented
  by six `xi=3` labels in three matching-exchange pairs.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, manifest, and refactor checks
  pass. Fable canonical is `00e28e1ba`; upstream reference pin is
  `93fba1be`. The next exact target is representative matching 7.

## 2026-08-08: CODEX WAVE-70 READY (pin a5c7b864a) — cell-4 xi3/xi4 pairing-7/10 orbit closed

- Missing `df` at matching 7 is PROVED empty. The exact quadratic
  Sylvester resultant of the two non-lane paired equations, followed by
  `z -> -z` elimination, reduces the system and missing-sum equation to a
  linear-remainder common-root cut in the exact four-basis source tower.
- Across eight source-sign/`sigma_c` rows, the exact ledger has eight degree-
  4068 norms, 48 target roots, 64 candidate `r` roots, 32 guarded source
  points, 16 compatible `z` values, 16 compatible `q` values, and 32
  nonzero remaining-pair lane evaluations. There are no target boundaries,
  witnesses, free branches, or unresolved strata. Final Modal app
  `ap-CeL2YMFG6ppa6aHpWDhM3T`; independent resultant, root-union, source-
  lift, and finite replay PASS under the 1 GB RAMguard ceiling.
- Parallel-`DE` matching exchange supplies pairing 10, and universal
  outside-role transport supplies both `xi=4` partners. Two new background
  PROVED nodes pay 64 raw cases, four labels, and two quotient orbits. Cell
  4 is now 97/105 paid; eight labels in four quotient orbits remain,
  represented by four `xi=3` labels in two matching-exchange pairs.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, focused replay, manifest, and refactor checks
  pass. Fable canonical `87ad3be1a` was merged cleanly; upstream reference
  pin remains `93fba1be`. The next exact target is representative matching 8.

## 2026-08-08: CODEX WAVE-71 READY (pin 4aeee3a2d) — cell-4 xi3/xi4 pairing-8/13 orbit closed

- Missing `df` at matching 8 is PROVED empty. Exchanging the `bf` and
  `sigma_c cf` partners in the two non-lane quadratic equations preserves
  the exact Sylvester-resultant and `z -> -z` architecture used at matching
  7, with a fresh direct finite replay of the matching-8 signs.
- Across eight source-sign/`sigma_c` rows, the exact ledger has eight degree-
  4068 norms, 48 target roots, 64 candidate `r` roots, 32 guarded source
  points, 16 compatible `z` values, 16 compatible `q` values, and 32
  nonzero remaining-pair lane evaluations. There are no target boundaries,
  witnesses, free branches, or unresolved strata. Final Modal app
  `ap-M2MiquWgaRzmJgiqN1Cumc`; independent resultant, root-union, source-
  lift, and finite replay PASS under the 1 GB RAMguard ceiling.
- Parallel-`DE` matching exchange supplies pairing 13, and universal
  outside-role transport supplies both `xi=4` partners. Two new background
  PROVED nodes pay 64 raw cases, four labels, and two quotient orbits. Cell
  4 is now 101/105 paid; four labels in two quotient orbits remain,
  represented by the single `xi=3` pair `{11,14}`.
- Critical census remains `231=167/36/28`. Sectioned-document, DAG,
  crosswalk, orbit, protocol, manifest, and refactor checks pass. Fable
  canonical remains `87ad3be1a`; upstream reference pin remains
  `93fba1be`. The next exact target is representative matching 11.

## 2026-08-08: WAVE-52 INTEGRATED (exact pin cfe023690) — 36 PROVED cell-4 nodes, 36/36 replayed; the campaign at 93/105; census unchanged

- Delta ac7d90f26..cfe023690 (40 commits): the positive 433-1b
  cell-4 orbit campaign, closed pairing by pairing (0-5, 11, 13,
  14 + endpoint roles + the universal xi4/xi3 transport) — 36 new
  PROVED background nodes, ZERO status changes, 36/36 verifiers
  coordinator-replayed at the pin (background batch, exit 0).
  Codex's own cycle records (its internal waves 62-69) document
  per-orbit exact ledgers with Modal replays under the RAMguard
  ceiling; verify_sectioned PASSES AT THE PIN (the CATCH-W51 rule
  held — Codex now files campaign records as REGISTERED addenda
  14-23 on rate_half_band_closure, adopting the repair pattern).
  Cell-4 state: 93/105 slices paid; 12 labels in six quotient
  orbits remain (six xi=3 representatives in three matching-
  exchange pairs; next target matching 7). Merge = exact pin;
  three conflicts resolved (the tool + document.json + attack.md:
  empty-HEAD vs Codex's addenda 14-23 registrations — took theirs
  after verifying my addendum-13 survives in all three; the
  ledger union-merged). Census unchanged 231 = 167/36/28; full
  chain green.

## 2026-08-09: WAVE-53 INTEGRATED (exact pin 0e30537c8) — CELL-4 AND CELLS 12-13 COMPLETE; 48/48 replayed; census unchanged

- Delta cfe023690..0e30537c8 (65 commits): 48 new PROVED nodes,
  ZERO status changes. MILESTONES: cell4_complete_exclusion and
  cell12_complete_exclusion PROVED — the [4,7] and [12,13]
  common-role orbits of the 433-1b workboard are CLOSED end to
  end; the universal positive label quotient proved; cell-9's
  global structure banked (common curve, common kernel, endpoint
  roles, signed-pair guard factorization) with its pairing ledger
  underway (16 representatives / 56 labels open). 48/48 verifiers
  coordinator-replayed at the pin — two heavy degree-4068 norm
  ledgers exceeded the 5-minute wall and PASSED under
  RAMGUARD_TIMEOUT=2400 (the profile's documented extension, not
  a dodge). verify_sectioned PASSES AT THE PIN (Codex continues
  the registered-addenda pattern). Merge = exact pin, clean.
  Census unchanged 231 = 167/36/28; chain green. Remaining
  workboard: cell 9 (in flight), the [5,8] and [11] orbits, and a
  residual cell-3 xi4 ledger to be re-pinned.
- NEXT (user-ratified): the LIVING K3 EXPORT PR — package the
  completed units (source-line coverage 36/36 + M01-R11 gate;
  cell-4; cells 12-13; the universal transports) in the #1143
  certificate format on a fork branch; open the PR; push
  incremental commits as later cells close.

## 2026-08-09: THE LIVING K3 EXPORT PR OPENED — upstream #1152

- The crashed packaging pilot was replaced by a bounded coordinator
  script (RAM-conscious: file-at-a-time sha256 walks, no bulk
  loads). Package: FOUR unit certificates in the #1144
  whole-cell-closure convention (README + JSON with K3_closed:
  false / row_closed: false up front, dependency pins, nonclaims):
  c112 source-line coverage COMPLETE (86 nodes incl. the M01/M02
  Singular-replay discharge), 433-1b cell-4 CLOSED (50 nodes,
  105/105 slices), cells 12-13 CLOSED (24 nodes), universal
  structure (44 nodes) — 204 theorem nodes pinned by path +
  verifier sha256 at canonical 594aaa985; one notes-only dir
  skipped and manifest-logged. Branch k3-433-progress-export cut
  from upstream main 93fba1be in a SCRATCH worktree (the live
  fork checkout untouched); agents-log entry appended per
  convention; pushed; **PR #1152 OPENED** (przchojecki/rs-mca).
  STANDING CADENCE (user-ratified): each wave audit ends with an
  incremental push of newly completed cells to this branch —
  cell 9 will be the first.

## 2026-08-09: round-25a BANKED — the PR re-harvest: exact complementarity with #1146; the mystery-7 mechanism sharpened from #1148's fixture; three addenda applied

- pr_harvest BANKED (their auditors replayed PASS; all arithmetic
  exact). HEADLINES: (1) #1146 x the legalized sieve = EXACT
  COMPLEMENTARITY — our NEW corollary (d < g => |Z| <= 1, ours,
  one line, previously unwritten) + their S_6 <= 20 compose to
  per-pattern uniqueness on the whole tau=6 family (chart mapping
  CANDIDATE); Theorem J proper misses their family entirely
  (extended to tau=5). (2) MYSTERY 7's mechanism SHARPENED: both
  exhibited M31 flats sit at the anticode instrument's r -> j
  counterexample end (0.931/0.9998; 2^836-vacuous) — the wall is
  ROOT-SHARING flats, not dimension growth; in symmetric-
  difference coordinates the same instrument is 2^7.75-loose /
  EXACT — a coordinate-change lead (CANDIDATE; upstream truth
  rests on unreplayed C++ sieves; vertex-vs-hull caveat). (3) The
  #1148 bridge: PROVED NEGATIVE (cap-3 unreachable even with the
  map); pricing stays closed. (4) Queue scan 0 new; false friends
  disarmed; #1133/#1134 records gap + #1135-#1137 import-pending
  surfaced. Addenda: the JB crosswalk + corollary; the rootfree
  instrument calibration + complement lead; the program-frontier
  citation. OUTSTANDING: SOL_TARGET_4 reprice wording (surfaced
  decision); ask-maelcar (F4 7-normal discrepancy; max C_r
  witness). ROUND-25 CANDIDATE (new, high): the complement-
  coordinate re-pose of the mystery-7 instrument.

## ROUND 25 LAUNCHED (2026-08-09) — QUARANTINE MARKER

Four pilots: m7_complement_repose (the symmetric-difference
coordinate re-pose of the mystery-7 instrument + the vertex-vs-hull
adversarial test + the FPC5 application + the CJ2/CJ3 chart audit),
large_v2_hunt (narrowing decision support: targeted witness hunt on
v_2(p-1) >= 41 admissible rows + the toy v_2 profile ground truth),
c2pp_falsifier_redesign (a REACHABLE C2''-r3 falsifier + the GB-5
pre-saturation escalation), z_n32_band (an algorithm for the N=32
sigma~0 Z-CEILING band under the 1G wall + the constant's
N-dependence). Pilots MUST NOT read ledger entries below this
marker and MUST pass this clause to any subagent. RAM DISCIPLINE
binding in all four (file-at-a-time reads; no bulk loads).

## ROUND 25 BANK 1/4 — m7_complement_repose (2026-08-09, coordinator)

**BANKED, verdict holds on replay: the symmetric-difference re-pose is
REAL, ALREADY-PROVED in-repo, and DEAD as a mystery-7 route.** Exact
threshold: the complement orientation beats the direct one iff
sigma < 2a; every FPC5 rate-half cell has sigma/a -> 2.5 permanently
(kappa=0 + PENCIL_MAX=1 measured in 63/63 exact-chart configs); the
root-sharing stratum that would help is deleted by our own guards
(the config-18 sunflower, 94->18 under primitivity+nonagreement).
Hard law 5: the instrument was PROVED three times over
(xr_lowcore NK4 with a prize-row table, band_complement CP2,
max_split_value MSC4) — my round-25a subtraction line was FALSE,
corrected in place; 723 of the "2^836-vacuous" bits were a
ground-set error. BONUS DECIDED: (CJ2)/(CJ3) hypotheses TRANSFER at
M >= 5 — large-source claim (ii) FALSE (round-24 mechanism again);
71/408 rows partially rescued, 1.97% of d-mass, rate-1/16 nothing.
Flagged: the m4_t3 owner-quality cell (4,1,1) is out of the node's
parameter family (all three admissibility conditions fail).
Replays byte-identical: d3_pricing, d4_cj3_audit; exact-match:
arm_a (4,97,seed 20260809, full), arm_b t=9 (pure sunflower, zero
hull escape). Registered falsifier to reopen the route: a guarded
admissible cell with common core or |U| < 2d — cheapest hunt = the
M>=5 charts D4 just legalized. Corrections applied to 3 nodes
(l1_rootfree + large_source + m4_t3); no status flips; census
unchanged 231 = 167/36/28. Pilot self-corrections: 7, all
unprompted, incl. one bare-python3 patch (isolated). Files:
notes/pilots_20260809/m7_complement_repose/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 25 BANK 2/4 — z_n32_band (2026-08-09, coordinator)

**BANKED: the round-24 named decisive computation EXECUTED. The N=32
wall is BROKEN (BBM, bucket-bisect MITM: 117.5s / ~50MB per cell vs
the "out of reach at 1G" blocker — the wall was memory layout, not
arithmetic). The record C >= 1.7681 STANDS (max N=32 CRATIO
1.4210954721 at p=4683696257), but Z-CEILING is repriced WEAKER:**
sigma/M-matched decay NOT significant (quantile 0.2278); sd decay IS
significant (quantile 0.0000) — the body shrinks, the tail does not;
round-24's SD-based growth law missed the N=32 max by 10x, and its
P4d "C = 1 + o(1) with grotesque room" is NOT SUPPORTED; heuristic
band extrapolation lands at ~1.88 ABOVE the record (warning, not
measurement). Mechanism found: low-weight mu_64-orbit spikes
(UMIN 9 at records vs 11 typical; AU[U] always divisible by 64; the
orbit-corrected threshold C(32,U)2^U >= 64p lands exactly at 11).
Verification: ez 15/15 (P-Z9 record exact), 33/72 two-way incl. all
top-12, record cell THREE-WAY (my reversed/101 driver AGREE 47.3s),
seeded analysis fully replayed. Honest tail: 39/72 single-algorithm.
Named follow-on: UMIN-targeted spike search + the declared post-hoc
exhaustive kappa=2 band (266 cells, never run). Addendum applied to
f2_z1_mass_knife_edge; no status flips. Pilot predictions: 9 HIT /
6 MISS incl. its own headline, all reported plainly; final report
issued twice (identical substance), both in the session record.
Files: notes/pilots_20260809/z_n32_band/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 25 BANK 3/4 — large_v2_hunt (2026-08-09, coordinator)

**BANKED: mystery-5 narrowing OPTION (c) IS DEAD three ways** —
(1) by exhibition to v_2 = 26 (209-bit witness, standalone
repro_v2_r25.py OVERALL PASS on my replay, fail-closed controls);
(2) heuristically at the registered threshold 41 (~2^98 predicted
counterexamples; the rung-41 silence pre-calibrated uninformative,
expected count 0.005); (3) mechanism PROVED ABSENT (NORMLAW three-
liner + the repo's own e1_n256 local-norm EQUALITY = surjectivity —
nothing stronger than v_2 >= 7 is forced). NOT REPAIRABLE: VSTAR ~
136-139 while the deployed Proth rows sit at v_2 = 92-97; the toy
law verified exactly at h=8 (MAXV2BAD8 = 12 = the Kyber prime
12289; VSTAR law 12.74). **OPTION (b) POSITIVELY SUPPORTED**
(W_TOP bad density ~2^-112; suppression is exactly prime-density,
K=1 after the LAW-2 cofactor split). NEW PROVED LAW banked: LAW 2,
Norm(1+2v) = 1 + 2h*v_{h/2} mod 4h (Newton identities; general w a
named gap; identity suite 0 violations h=2..64 on my replay).
Replays: repro PASS, d3_thm 0 violations, d1_h8 exhaustive census
EXACT (554/536/12289, round-22 densities to the digit). Addendum
applied to integer_code_distance_cert; coordinator recommendation
UPDATED to (b) primary + (a) fallback, (c) withdrawn; THE DECISION
REMAINS SURFACED TO THE USER. No status flips; census unchanged
231 = 167/36/28. Files:
notes/pilots_20260809/large_v2_hunt/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 25 BANK 4/4 — c2pp_falsifier_redesign (2026-08-09, coordinator) — ROUND COMPLETE

**BANKED: mystery 3 moves from "unmeasurable at depth" to "measured,
with a powered falsifier that stayed SILENT."** C25-1 TELESCOPING
LEMMA: N_{>j-1} = E_j AND N_{>j}, so R3_W = two level censuses +
per-level block censuses — round 24's junction-squaring wall applies
to the WINDOW, not the LEVELS (PR-A brute-force PASS on my replay).
G-c (level-decay exponent): power-controlled on synthetic worlds
BEFORE proposal (kappa_det=1/32, delta_det=0.10; powered for official
log2 q <= 247/232, blind at the knife edge — declared in advance);
VERDICT SILENT (alpha/T = 0.995-1.067 at the well-determined cells);
power_results.json IDENTICAL on my fresh replay. C25-4: GB-5's 4.5x
is a SATURATION ARTEFACT — the official shape is deep pre-saturation
where measured R3_W ~ 0 (-0.003, +0.0004 at n/t = 16, 8); round-24's
datapoint stands as measurement, weight moved. C25-2: the e-periodic
frozen stratum closed form (98/98; 86/98 re-verified by me, 0
mismatches) IS the official ledger's coset stratum — rebuild 5/5,
and 107 = e - 21 = 128 - 21 exactly (C25-6). First-ever [law]
estimate of the official junction sum: ~ -0.0066 bits for log2 q <=
255.9, crossing 21 at exactly 256 - 107/2^33 (replayed break scale
255.999999987544); licensed <= 232, undecidable (232, 256], broken
within 107/2^33 of 256 — where the packet's two 256-bit rows sit.
New laws: S_inf = 1/ln2 (R3inf ~ 0.4427n); freeze law PER-LEVEL
(round 24's form = lev 0; strengthens GB-3). Named obstruction: the
freeze-tail cutoff law. C25-5: official_scale.json:83 decimal 10^3
too large — sidecar correction filed, JSON verbatim. Symmetric
not-evidence clause respected: G-c silence = survived powered test
on toys, NOT official-row evidence. Addendum on
dli_c2pp_joint_reserve; no status flips; census unchanged 231 =
167/36/28. Pilot self-corrections: 7, all disclosed. Files:
notes/pilots_20260809/c2pp_falsifier_redesign/{REPORT.md,FABLE_AUDIT.md}.

**ROUND 25 COMPLETE: 4/4 banked (m7_complement_repose,
z_n32_band, large_v2_hunt, c2pp_falsifier_redesign). Two kills
(the mystery-7 re-pose; narrowing option (c)), one wall broken +
one conjecture repriced weaker (Z-CEILING at N=32), one conjecture
measurably testable for the first time with its powered falsifier
silent (C2''-r3). Zero status flips — the round moved evidence and
instruments, not statuses. PENDING USER DECISION: mystery-5
narrowing, coordinator now recommends (b) primary + (a) fallback.**

## NARROWING RATIFIED (2026-08-09, user): mystery 5 = (b) primary + (a) fallback

The user ratified the round-25 recommendation verbatim: (b)
o(1)-sparsity primary, (a) exhibit-scoped fallback, (c) large-v_2
withdrawn. Recorded on integer_code_distance_cert + board r5
(roadmap section 12). The b_sparsity_pose pilot (round 26) executes
the pose.

## ROUND 26 LAUNCHED (2026-08-09) — QUARANTINE MARKER

Four Opus pilots: b_sparsity_pose (pose the ratified (b) conjecture
+ LAW-2 general-w + box-depth gap), umin_spike_hunt (Z-CEILING
kill-or-confirm: weight-enumerator triage of the N=32 band for
UMIN<=10 spike cells, exact CRATIO at the top candidates),
freeze_tail_law (the C2'' named obstruction: fit-and-prove the
level-census cutoff law + the S_inf = 1/ln2 proof + extend G-c's
licensed range), m7_falsifier_hunt (the registered mystery-7
falsifier's cheapest ground: overlap structure of the M>=5
large-source charts legalized by round-25 D4). Pilots MUST NOT
read ledger entries below this marker and MUST pass this clause to
any subagent. RAM DISCIPLINE binding in all four (file-at-a-time
reads; no bulk loads; checkpointed background batches for >10-min
runs). Draft-only; no status flips; REPORT.md persisted by the
coordinator from the transcript.

## ROUND 26 BANK 1/4 — b_sparsity_pose (2026-08-09, coordinator)

**BANKED: the ratified (b) is a THEOREM at the prize cell — THEOREM
B1: bad-prime density in W_ADM <= 2^-93.93 elementary / 2^-106.93
with the exact Burnside orbit count (2^135.6034 over the 8192-element
group), v_2-uniform to VSPARSE(128) = 113.93.** Four banked
ingredients (fold reduction + the DLI lane's LN4 energy ceiling +
zero-margin pigeonhole + PNT-in-AP at fixed modulus) — the
union-bound route honestly subtracted as in-repo prior art (the e1
retired proof; the pilot's script also restores catch-#61's missing
script). THREE TEETH: (i) no valid asymptotic parameter (N'=256
VACUOUS +42.7 bits and heuristically every prime bad — SURFACED:
re-scope (b) to a numeric per-cell bound); (ii) (a)/(b) are
COMPLEMENTARY (the deployed Proth stratum is vacuous by ~62 bits for
the theorem — (b) = row selection, (a) = assigned rows); (iii)
status_ruling has NO density slot — SURFACED: ruling amendment
needed before (b) can move the node. Falsifiers: F1 exhaustive not
falsified (toy bound non-vacuous, 43.6x over truth); F2 trend
Z=-0.47/-1.34 not falsified (round-25's p=0.07 resolved as omnibus
noise); F4 standing (Proth collision = 2^27 surprise). BONUS BOTH
NAMED GAPS DISCHARGED: LAW-2 GENERAL-w CLOSED (P2 proved:
Norm(w) = 1+2h[sigma(u)+(u^{-1}z)_{h/2}] mod 4h; sigma linear in
(zeta-1)-adic digits, tables computed, 0/200 everywhere); box depth
2^17 -> 2^40 NO structure (full realization exhibited to 2^23).
Replays: burnside/prize/toy/law2/digits/d3-analyse/d4 ALL exact;
pigeonhole + P1/P2 logic hand-verified. Pilot misses disclosed:
registered margin wrong (0.0000 exact), first Burnside bound wrong
(exact count instead), GUESS-G refuted, one benign out-of-dir write
(byte-identical, git-clean verified). Addendum on
integer_code_distance_cert; no status flips; census unchanged
231 = 167/36/28. Files:
notes/pilots_20260809/b_sparsity_pose/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 26 BANK 2/4 — freeze_tail_law (2026-08-09, coordinator)

**BANKED: the round-25 named obstruction CLOSED AS A THEOREM.** The
freeze tail is a short-vector census of a rank-e lattice terminating
at an exact integer cutoff (non-frozen state => q^{g_v} divides a
nonzero Hadamard-bounded resultant); 419/419 rows, five exact
cutoffs certified predictively (8,279 primes, 0 violations). My
replays: P2 419/419 from scratch; Q*(32,2,1) = 273857 re-derived by
INDEPENDENT full-box Bareiss sweep (ties to the round-25 large_v2
census: 1450 norms, MAXNORM 614656); proof logic hand-verified.
C26-2 L3 negacyclic reduction (T=1 level census = skew census on e
coords, 181/181 bit-exact, 7.0e9 -> 1.19e6 states); C26-4 sharp
max-norm law (e-1)^{e/2} u^e exact at all five cells. FORCED
CORRECTION C26-5: round-25's "measured freeze scales 14.5..67" were
NOT cutoffs (excess non-monotone in q; 6.2-bit understatement at
(64,4,2)). C26-6: S_inf = 1/ln 2 PROVED (factorial telescoping,
identity + algebra coordinator-verified) => mint
R3inf_full(n,n/2) = 0.4427n - (1/2)log2(pi n) + 1/2 + O(1/n).
C26-8: G-c licensed range 232.7 -> 251.1 [law] (~80% of the
undecidable band closed; CAVEAT of record: power re-calibration at
the new tolerance not run — the named next job). C26-7: the
ledger's linear coset model understates true depth exactly in the
break-constant window (flag, no transport). (232, 256] by census:
unreachable (2^2176 even under L3). Pilot misses first: PR-6
(0.736 vs [0,0.05] — became finding C26-9), PR-6b slope refuted,
PR-5 5/7. Addendum on dli_c2pp_joint_reserve; no status flips.
Files: notes/pilots_20260809/freeze_tail_law/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 26 BANK 3/4 — m7_falsifier_hunt (2026-08-09, coordinator)

**BANKED: THE REGISTERED FALSIFIER FIRED — and the kill survives on
its honest leg.** C8 (rate 1/2, M=5, t=3, ell=2, b=u=1, d=5, N=9,
q=23; admissibility hand-verified) fires sigma < 2a in 67.2% of
m>=3 configs, kappa >= 1 in 44.3% (vs round-25's 0/63); mechanism =
exact arithmetic N + kappa < 2d (hand-verified); matched control C9
(2d-N = -5): 0/64 — the switch is exactly at 2d = N; 156/408 real
residual rows pass the threshold in the CJ-admissible window.
FORCED CORRECTION on l1_rootfree: the round-25 "wrong side by
construction" line is m4-family-only. THE KILL STANDS ON PRICING:
0/156 rows polynomial (mean 7.3e11 bits vs a 123-129-bit target);
b->ell intuition REFUTED (overlap up, kappa DOWN). NEW: the sharp
overlap cap r_J - |R1 cap R2| (= d-ell at u=b) — (CJ2) un-summed,
0/8336 configs, attained, DELETES the pencil stratum (round-25's
sunflower deletion now systematic + explained). BONUS (largest
number, REPLAYED byte-identical, NOT YET ADOPTED): charging the
node's own list threshold empties **71.380% of the residual d-mass**
(+0.679% singleton by PROVED (BO2); pilot's own derivation caught
by its CATCH-24A grep as a (BO2) re-derivation) vs round-25's 1.97%
— third instance of the claims-(i)/(ii) mechanism; adoption gated
on the full-grid distinct-d computation (named highest-value
follow-up). Red 3 membership UNDECIDED of record (honest refusal:
t>=4 priced 2.3h not spent; the 23b functional FAILS its power
control at accessible cells). Replays: bo_sieve + d1_cells
byte-identical, C8 config-identical, EMPTY logic + C8 arithmetic
hand-verified. Corrections on l1_rootfree + large_source; no
status flips; census unchanged 231 = 167/36/28. Files:
notes/pilots_20260809/m7_falsifier_hunt/{REPORT.md,FABLE_AUDIT.md}.

## ROUND 26 BANK 4/4 — umin_spike_hunt (2026-08-09, coordinator) — ROUND COMPLETE

**BANKED: CONJECTURE Z-CEILING's RATIO FORM IS FALSIFIED on its own
pinned family — the campaign phase's falsification event.** Record:
CRATIO = 5.8131644651 exact at N=32 kappa=1 p=4337074369
(sigma=-0.0141), FOUR-WAY derived (pilot x3 + coordinator stride-5/113)
and the weight-5 kernel witness (support {0,1,3,12,25}) verified
DIRECTLY by coordinator code; 119/124 exact cells > 2; the N=16
record 1.7681 beaten 3.3x. THEOREM RS (new; converse of RC, an IFF)
=> recall 1.000 by proof; the sweep runs over ternary f not primes —
a complete CENSUS of all 2.12e7 admissible kappa=1 primes (UMIN
strata 0/0/90/2,395/25,105; 0.130% of the band; 4.4 microsec/prime =
4e7 speedup). MECHANISM: the kernel is the ternary part of an IDEAL
=> mass multiplies, TMASS >= ~(1+2^{1-U})^N with U pinned at 5 by RC
=> NO absolute constant (ladder 0.944/1.7681/5.81+, factor >= 3.3
per doubling). Round-24's "C >= 1.7681, 3.95 bits headroom" and
round-25's "matched decay not significant" SUPERSEDED — the tail is
arithmetic, not statistical (a 47-cell sample had expectation 2e-4
of hitting the U=5 stratum). SURVIVES: Z-FLOOR (0/292), RC, RS.
SURFACED: the F2 terminal's non-local smoothness input has NO NAMED
ROUTE again (round-19 verdict strengthened). kappa=2 exhaustive band
COMPLETED BY COORDINATOR (pilot's sweep died at 186/266; resume
batch; 266/266, 77 double-computed with 0 conflicts): max 1.3887 at
p=63361, ZFLOOR clean — no spikes at kappa=2, the round-25 post-hoc
sweep closed. Pilot record: 7 HIT / 5 MISS misses-first (own
headline missed 1.9x — the additive predictor was structurally
wrong; the ideal mechanism found in data, declared unregistered);
checkpoint-resume escape circularity caught by the pilot itself.
Addendum on f2_z1_mass_knife_edge; no status flips; census unchanged
231 = 167/36/28. Files:
notes/pilots_20260809/umin_spike_hunt/{REPORT.md,FABLE_AUDIT.md}.

**ROUND 26 COMPLETE: 4/4 banked (b_sparsity_pose, freeze_tail_law,
m7_falsifier_hunt, umin_spike_hunt). Two theorems where conjectures
were expected (B1 density; the freeze-tail cutoff), one falsification
of a minted conjecture (Z-CEILING ratio form — mystery 2's candidate
closure), one registered falsifier fired-and-survived-on-pricing
(mystery 7), S_inf = 1/ln2 and LAW-2 general-w proved, G-c's
undecidable band 80% closed. Zero status flips. PENDING USER:
(1) numeric per-cell re-scope of (b); (2) integer_code_distance_cert
status-ruling amendment (density slot); (3) the mystery-2 board
event — Z-CEILING dead, the F2 smoothness input route-less again.**

## WAVE 54 INTEGRATED (2026-08-09, coordinator) — CELL 9 CLOSED; Codex self-pushed the export

**Merged exact audited pin 91e580f19 (merge 4755268be; 24 commits,
27 NEW background PROVED nodes, zero edits to existing nodes, no
critical/sectioned touches).** Headline: **positive 433-1b CELL 9
CLOSED** (rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_
complete_exclusion — composition: 105 = 30 endpoint + 75 labels in
24 proved orbit-owner packets; verifier checks the partition, size
profile 1:1/2:9/4:14, owner disjointness, and all 19 dependency
statuses). Also: cell-3 xi4 residual RE-PINNED for export (the
long-open workboard item); cell-5 campaign underway (9 pairing
exclusions banked, 6 active orbits / 28 labels remaining at the
pin). REPLAYS: verify_sectioned + verify_prize_dag PASS AT THE PIN;
**54/54 verifier runs PASS** (verify.py + verify_audit.py on all 27
nodes, background batch, RAMGUARD_TIMEOUT=2400). Census unchanged
231 = 167/36/28 (background-only additions); post-merge verify
chain green.

**PROCESS EVENT, SURFACED: Codex pushed the export itself.** Two
commits on fork/k3-433-progress-export (1b866634 cell-9 cert,
e1e7d263 cell-3 cert) minutes after banking the closures — PR
#1152 now titled "cells 3, 4, 9, and 12-13 closed". COORDINATOR
AUDIT OF THE PUSHED CERTS: convention-compliant (#1144 shape,
K3_closed false, honest nonclaims incl. "fresh independent proof
review required", provenance pins the exact worktree commits,
per-node verify sha256 — spot-checked EXACT). The pinned commits
became publicly reachable with THIS wave's master push (the certs'
replay instructions were dangling until then — the one real gap in
self-pushing). PENDING USER: ratify Codex push-on-close for this
living PR (coordinator recommends YES, scoped to PR #1152 only,
with same-day coordinator audit + fix-forward), or re-assert
coordinator-only pushes.

## RULING RATIFIED (2026-08-09, user): Codex push-on-close for PR #1152

Scoped to the living K3 export PR only; exact-commit provenance
required; coordinator same-day audit with fix-forward. Ruling of
record: notes/codex_briefs/RULING_PUSH_ON_CLOSE_20260809.md.

## ROUND 27 LAUNCHED (2026-08-09) — QUARANTINE MARKER — THE ANALYTIC-HALF ROUND

Four Opus pilots on the band-closure analytic half (user-directed
after the K3-lane review): pincer_formalization (re-audit the
consumed safe-side machinery FIRST, then formalize the worst-word
per-row FM crossing and state BAND-AC as a sharp conjecture),
nonpoly_flank_census (the named residual hunt space: planted-hybrid
non-polynomial received words outside the fiber reduction),
staircase_extension (close the {2^39, 2^39+1} residual budgets;
diagnose the 2^167 boundary; price the razor-scale analogue),
cancellation_recon (can THEOREM Z-FLOOR's proved pointwise-floor
mechanism transport to band counts — the first in-repo attack on
the cancellation barrier). Pilots MUST NOT read ledger entries
below this marker and MUST pass this clause to any subagent. RAM
discipline binding; banked scripts run from SCRATCH COPIES only
(the round-26 b_sparsity lesson); draft-only; no status flips;
REPORT.md persisted by the coordinator.
