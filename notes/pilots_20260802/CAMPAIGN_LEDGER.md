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
5. **P-B LANE RE-TARGET (top strategic item, from the FM3 pilot):**
   at official scale the compression collapse inverts (block deficit
   K - L* grows linearly in n; Pi = 2^-73.5 at RowC 1/4: >=K pairs
   absent from the POPULATION), so Gamma_hi is empty, the R2
   partition never compresses, and the binding obligation is
   **bounding |Gamma| <= 8n^3**, not partitioning Gamma. Required
   adjudication: row-by-row, does the pinned q exceed 8n^3 (rows with
   q < 8n^3 are safe by field size alone — |Gamma| <= q), and can the
   split-fibre construction realize a super-budget live-slope family
   in one field at any exposed row (the adversarial audit's
   M = 1.3e11 vs 16n^3 = 1.7e10 at RowC, on the new footing)?
   Coordinator pass, then Pro. Node-local note:
   `xr_lowcore_spread_heart/notes/OFFICIAL_SCALE_REFRAME_20260802.md`.
   CAVEAT: 5-doubling model extrapolation, (H) assumed — exactly what
   Pro should attack.

## B. NAMED PROOF OBLIGATIONS (open)

- **k-packing lemma — WITHDRAWN as a mint** (subtraction check by the
  band-ledger pilot): already banked verbatim at
  `xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`.
  Cite it; do not re-derive.
- **BAND OCCUPANCY LEMMA (the named heart of the band repair):**
  N_d <= ~0.68n^2 at the binding row (aggregate SUM N_d L(d) <=
  13n^3); the n^2-vs-n^2/2 boundary is the exact target; Theorem 7
  (two-column determinacy — occupancy as point-line incidence in A^2)
  is the designated lever; the d = h-1 term (27x weaker) subsumes the
  cascade pencil-count question. `xr_graded_band_ledger/REPORT.md`
  section 3.
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
- **Crossing lane succinct contract** — coordinator's to draft (from
  the Brief-6 adversarial round); gates any crossing pilot.

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
