# Fable audit of the graded-band-ledger pilot (Route T costing) — 2026-08-02

**Verdict: ACCEPTED — and the W/T fork REVERSES again, this time with
proofs.** Route T, redesigned as a THIRD generic column from the 13n^3
headroom (never enlarging B_tan), strictly dominates Route W: both
routes are gated on the same single open input (the band occupancy
lemma), and Route T buys it with zero demotions and unchanged prize
ranks. The cascade audit's tilt-to-W objection is RECONCILED, not
contradicted: it killed Route-T-as-B_tan-enlargement (correctly — the
printed column is dead on 5/6 rows even at N_d = 1), and this pilot's
design simply does not do that. Cascade separability is explicit: the
extension to depth h-1 needs a 27x weaker occupancy bound, so the
ledger's feasibility is independent of the payment audit's outcome.

## Independent verification record

- Replayed `band_arith.py` (ALL CHECKS PASS; banked pins B*, B_quot_ub,
  s_lo reproduced from scratch) and the battery `shared` + `interact`
  groups (the decisive adversarial fixture beats the printed column 14
  vs 8 AND is then killed by the Theorem-5 forced tangent; rigidity and
  cap invariants at 0 violations).
- Hand-proved all five theorem proofs (T2-T5, T7; T1 is banked, T6 is
  a bijection I checked): the T2 disjointness argument, the T3 count,
  the T4 proportionality, the T5 union identity and its corollary
  |Z_1 u Z_2| >= k+d_1+d_2+1 > A when d_1+d_2 >= h (fires P2's
  A0 > A), and the T7 2x2 determinant. All sound.
- Verified BOTH subtraction claims directly in the tree:
  (1) the k-packing is banked verbatim at
  `xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`
  — the p_a1 pilot's "lemma worth banking" is a re-derivation;
  CAMPAIGN_LEDGER corrected. (2) `common_code_line_budget` prints the
  line-cap formula under the hypothesis `a + b - n >= k`, which fails
  at all six rows (J <= A-2 << n-A+k-1) — the banked node does NOT
  cover the band; Theorem 3's four-line proof under `J >= k` is the
  version to bank. Node-local flag written.
- Hand-checked the arithmetic: RowC 1/4 SUM_d L(d) = 191+255+382 = 828
  > 764; L(h-1) = R-h+1 = n-A+1 exactly (matches the payment audit's
  saturation finding from the other side — two pilots, blind to each
  other, converged on the same identity); the harmonic law
  SUM_d L(d) ~ R(H_{h-1}-1) ~ 22.3R at h ~ 2^33 (H ~ ln(2^33)+gamma).
- The self-refuting adversarial fixture (M2 shared-block) is the best
  kind of evidence: the pilot found the strongest attack AND the
  theorem that kills it, and verified both numerically.

## Findings adopted

1. **Fork recommendation UPDATED: Route T** (surfaced — final call
   with user/maintainer, Pro adversarial round invited). The complete
   fork history: bridge adjudication forced the repair; cost pass
   priced W and surfaced the fork; cascade audit killed
   T-as-B_tan-enlargement and re-sourced the ceiling at A-1; this
   pilot redesigned T as a third column and proved the interaction
   strip. Under T: zero demotions, prize ranks unchanged, P-A1 keeps
   exact-k form; the Group-C nodes' "post-strip cap" premise becomes
   CONDITIONAL on the band column (recorded as a req dependency when
   minted) rather than permanently re-scoped. The wording defects
   (strip item-3, cascade "paid", the 4,662 sentence, clean_residual
   "removes") need fixing under EITHER route.
2. **The named heart is now singular**: the BAND OCCUPANCY LEMMA
   (N_d <= ~0.68n^2 at the binding row; aggregate <= 13n^3). The n^2
   vs n^2/2 boundary is the exact target. Theorem 7 (two-column
   determinacy — band occupancy as point-line incidence in A^2) is the
   designated lever. This subsumes the cascade audit's pencil-count
   obligation (the d = h-1 term, 27x weaker requirement).
3. **Mint queue (after ratification):** Theorem 3 (line cap under
   J >= k — supersedes the inapplicable common_code_line_budget
   hypothesis for this use), Theorem 4 (ray rigidity), Theorem 5 +
   corollary (the band interaction strip — a genuine STRIP EXTENSION:
   d_1+d_2 >= h configurations leave the generic branch; also kills
   the overlap-(k-1) class automatically), Theorem 7 (two-column
   determinacy). Theorem 1 NOT minted (banked); Theorem 6 recorded as
   a warning (per-ray multiplicity = MDS list size below Johnson — the
   master inequality is lossy; sharp ledger must count slopes).
4. **Two corrections of my own prior statements**: (a) "a per-depth
   sum growing with h is DEAD" was too crude — the line cap's harmonic
   decay makes the astronomically wide prize band survivable at fixed
   ~n^2 cost per depth; (b) the CAMPAIGN_LEDGER's k-packing mint item
   is withdrawn (already banked).
5. **"Route S" (re-selection dodge) recorded as killed-empirically**
   (0 slopes with >1 exact-A ray across the battery), not proven
   impossible.

## Caveats kept (endorsed)

- The master inequality is lossy (Theorem 6); 0.68n^2 is sufficient,
  not necessary; a sharp ledger counts slopes directly.
- The banked interleaving collapse is TRUE BUT VACUOUS here (L(k+1)
  astronomically above n^2) — do not cite it as progress.
- Toy scale (n <= 27, q <= 101); band population at official A open
  (same caveat as every band-adjacent pilot).
- The occupancy CONJECTURE is the whole remaining content; nothing
  here proves it.

> **[AMENDED same day — xr_band_occupancy pilot, coordinator-replayed.]**
> Three updates. (1) The occupancy heart RE-ROUTES: Theorem 2 there
> (high-depth injectivity) converts 96.9% of this ledger's cost into a
> single-word RS list-size bound at k + ceil(h/2) (25-50% of Johnson)
> — same species as positive target #1; the low band is free at any
> bound up to n^2. F1 did not fire (best construction exactly linear).
> (2) TWO corrections to this audit's adopted items: "Route S has no
> purchase" is REFUTED (re-selection freedom at 15/76 admissible
> fixtures; all rigidity/coset statements must be keyed on RAYS —
> the slope-keyed reading of Theorem 4 is false); and caveat 1's
> "arbitrarily lossy" is corrected — the master inequality is
> worst-case TIGHT (slack exactly 1.0 attained; max family at 2.0).
> (3) The mint queue changes: the occupancy pilot's unified Theorem 1
> SUPERSEDES this pilot's Theorems 4+5 (contains them, extends to
> z in {0, inf}); the tangent gate must be stated over all of
> P^1(F_q) including (0:1) (bandlib's scan omits it; 0/76 fixtures
> retroactively affected). See
> notes/pilots_20260802/xr_band_occupancy/{REPORT,FABLE_AUDIT}.md.
