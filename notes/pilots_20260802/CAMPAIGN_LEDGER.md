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
