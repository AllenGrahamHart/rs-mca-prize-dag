# Fable audit of the pencil-cascade payment audit — 2026-08-02

**Verdict: ACCEPTED.** The "paid" in `xr_pencil_cascade` is UNSOURCED —
a classification into a stratum (rigidity_kernel clause (i), itself
CONJECTURE) whose price was never proved to cover this shape — and its
natural pair-level payment form is REFUTED in-tree
(`xr_nondeep_tangent_supportwise_payment`) under a STRONGER hypothesis,
with the deep-regime condition failing on all six official rows. The
compensating positive: the honest generic-branch core ceiling is `A-1`
and is independently sourced by a one-line derivation from banked
pieces. This audit answers the W/T fork gate: it tilts toward Route W.

## Independent verification record

- Replayed both scripts this session (ramguard tiny): `ceiling_arith.py`
  (deep-condition `3j <= n-k` False on all six rows; collapsed-face
  survival at kappa = A-2 only on RowC 1/16, at kappa = A-1 nowhere;
  B_tan slot saturation exactly 1.0000 on all six rows) and
  `f17_cascade_check.py` (the F_17 refutation witness carries MULTIPLE
  forced pencils, each with |T| = 6 = n-A+1 — the per-pair overflow is
  real and visibly worse than the report's "two": the replay lists a
  dozen distinct pencils at |T| = 6 on this one received pair).
- Confirmed the provenance gap directly: `critical/nodes/
  xr_pencil_cascade/` contains statement.md + proof.md + EMPTY notes/,
  no verify.py. The "W1, PR #10, 70/70" string has no in-repo artifact.
- Hand-verified the honest-ceiling derivation: selected supports are
  exact-A; two distinct-slope selected supports with core = A have
  |S ^ S'| = A = |S| = |S'|, hence S = S'; the strip forcing algebra on
  that common support (core >= k+1) produces a codeword pair agreeing
  on all A points — a joint A-support explanation — so the pair is
  nongeneric by the bridge's own case split. Generic branch cores
  <= A-1 unconditionally. Sound, and genuinely independent of the
  disputed node.
- Hand-verified the T2 non-firing: the cascade upgrade map sends one
  off-core point to one slope at agreement exactly A; exceeding A needs
  two cooperating points per slope, which the map never produces. And
  the T2-firing case (core >= A) is exactly the nongeneric case. Sound.
- Hand-verified the arithmetic: L(A-1)/L(A-2) = (n-A+1)/floor((n-A+2)/2)
  = 2 exactly when n-A is odd... verified numerically on all six rows
  (e.g. RowC 1/4: 764/382); collapsed-face at kappa = A-1 needs
  k+2 > A-1 <=> h < 3: dead 6/6.

## Findings adopted

1. **Fourth false-green wording catch of the day**, and structurally
   the deepest: statement-level "paid" resting on a CONJECTURE-status
   taxonomy, with the node's own cited source explicitly disclaiming
   the netting ("'Unpaid' is not netted against the asymptotic
   ledgers"). The scope-narrowing of `xr_pencil_cascade` (PROVED covers
   forcing + cascade only; "paid" and the one-pencil "~n-core"
   multiplicity clause both need scoping) is SURFACED — node-local flag
   written.
2. **The W/T fork gate is answered.** Route W survives with the ceiling
   moved A-2 -> A-1 (sourced independently; line caps exactly double;
   PSP already priced at A-1; the collapsed-face exclusion, already
   fatal, loses its last row). Route T is now materially harder: it
   must charge up to A-1, its target column is provably saturated by a
   single cascade (1.0000 six/six) with multi-pencil overflow realized,
   forcing B_tan > n-A+1 = re-surgery trigger 4, and its nondeep form
   is REFUTED. My updated recommendation to user/maintainer: Route W,
   pending only the in-flight graded-band-ledger pilot's report (which
   was instructed not to assume the cascade payment — its verdict on a
   >n-A+1 ledger remains informative for the residual-column design).
3. **The A-1 scope hole is recorded**: under current wording the A-1
   tier is counted ZERO times (outside both B_tan and F5-OS's <= A-2
   quantifier). Any Route W edit must move F5-OS and the
   xr_smallcore_spread_count dag statement to A-1 in the same change.
4. **Two named proof obligations queued**: (a) the injection-extension
   one-liner (recovered-line slopes <= |T| <= n-A+1 at forced core
   >= A-1) — small, real, makes half the cascade charge sourced;
   (b) the per-pair forced-pencil-count lemma — the SAME object as the
   k-packing lemma the widening pass proposed and the band-ledger pilot
   is currently attempting. Convergence noted: one lemma serves three
   consumers.
5. **Consumer wording repairs queued** (with the eventual coordinated
   edit): `xr_clean_residual_any_gate/conditional.md` ("removes" ->
   "classifies"; second unproved contribution acknowledged); the
   BAND_OVERCLAIM_FLAG's own repair text (no core-based charge proved
   at any threshold); WP7_WORSTWORD_VERDICT's "two proved bookends";
   the widening pass FABLE_AUDIT (ceiling correction — addendum
   appended).

## Caveats kept (endorsed)

- The F_17 witness is the REFUTED node's toy row; the finding is
  "unsourced + natural form refuted outside the deep regime (= all
  official rows)", NOT "official rows falsified".
- A-1-tier population at official scale established nowhere (same
  scale caveat as the band and the bridge exhibits).
- Every banked cascade-tier measurement lives at rows where the tier
  is a single point or empty — the corpus cannot see this structure
  (third instance of the t=2 blindness genre).
- Provenance items ("W1 PR #10", the #147 .tex) remain unpulled;
  flagged for any re-grade.
