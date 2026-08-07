# f2_o1_status_split

- **status:** PROVED (the theorems constituting the split; (O1)
  itself is NOT a claim of this node)
- **minted:** 2026-08-06 (mint-4, rounds 17-18), coordinator-audited.
- **provenance:** notes/pilots_20260806/f2_adm/ (THEOREM ADM-B),
  notes/pilots_20260806/z1_ternary_mass/ (THEOREM Z-3),
  notes/pilots_20260806/o1_generating_adversary/ (THEOREM Z2,
  CATCH-A/G/H) — all coordinator-replayed.

## Statement

THE STATUS OF (O1) ON PRIZE-ADMISSIBLE ROWS, split by generation and
by two UNPINNED conventions.

**Non-generating rows (k = ord_n(p) < e): (O1) IS FALSE by
2^{Theta(n)}, twice over.** (i) THEOREM ADM-B: LEMMA 3's exact ratio
k/e < 1 fails the necessary condition for every t in the non-vacuous
regime (t-naming-independent). (ii) THEOREM Z-3 (independent route,
object-level): Z(L) >= 2^{m(1 - (k/e)(tL/n))} = 2^{Theta(n)} — the
K1 first moment itself exceeds its target. Explicit exhibit
p = 3·2^41+1, q = p^6 (k = 1 < 6), excess 2^{5n/12} (nested) /
2^{n/6} (looser reading), exponents matching between the two routes
exactly. Coordinator-verified arithmetic; coset-robust by THEOREM
C1. CONSEQUENCE OF RECORD: the F2 lane requires a hypothesis "the
smooth domain generates F" that the rules freeze does not supply
(official_row_primes_pinning: admissibility and quantifier
conditions only) — MAINTAINER QUESTION, open.

**Generating rows (k = e, exactly three classes): (O1)'s truth is
decided by two unpinned conventions — THEOREM Z2 (the ensemble
dichotomy).** At k = e, LEMMA 3's requirement IS the counting
balance t·L >= n with zero slack; therefore under the full-subset
calibration (C) (ensemble 2^n) (O1) SURVIVES with <= 184 bits of
slack (integrality only, O(L)); under the exact fixed-slice
calibration (T*) (ensemble log2 C(n, n-k-t) + 128) (O1) is FALSE by
2^{n/(L^2 ln 2)} >= 2^{4.84e7}. The gap between the calibrations is
2n/(L^2 ln 2) — relative size 0.0044%, the same number banked twice
as "agreement" (f2_tq_pin CATCH-4, t_naming CATCH-C): AT ZERO
MARGIN IT IS THE SIGN OF (O1). Reading dependence: the kill is
Lambda-parity-reading-A-only (under B the margin is 2 and the
recalibration is swamped). CATCH-H: reading A is INTERNALLY FORCED
(the proved K1/K2/G trichotomy forces |Lambda_K1| = ceil(t/2); the
lane's own frequency-space text says min(m_j, t/2)) — an
internal-consistency argument, not proof of maintainer intent.
CATCH-G: the (O1) => (O2) fence itself demands the slice ensemble
(THEOREM B' is vacuous at every moving rung), so THE LANE'S OWN
INTERNAL LOGIC POINTS AT THE FALSE CELL of the 2x2.

**The minimal surviving form (banked verbatim):**
E_{c in K1(Lambda)}[T_W(c)] = 2^{n/2}·Z_1^e EXACTLY, on
(e_p, e) in {(>=41,1), (40,2), (39,4)} with e·log2 p < 256, coset
droppable by C1, Z_1 the ternary mass of the negacyclic prime-field
GRS code [S, S-R, R+1]_p on the half-system of mu_{2^{e_p}}
(S = 2^40/e, R/S = 1/log2 p, min ternary weight >= 2R+1). (O1)
holds iff Z_1 <= 2^{o(n)/e} — subject to the parity reading and the
ensemble calibration, both maintainer-decidable, neither decided
here. Under (reading A + slice) the statement is FALSE and no Z_1
bound can save it.

**THE FOUR-FACE MAINTAINER SEAM (one inequality):** the counting
balance t·L >= n, LEMMA 3's requirement, the vacuity boundary of the
Z-FLOOR mass bound, and the PP5.0 average-vs-sum seam
(log2|K1|_eff >= n/2) coincide on k = e rows (f2_adm D5 + z1
CATCH-Z3). CAMPAIGN WORKING CONVENTION (coordinator ruling
2026-08-06 under the rules-freeze stricter-reading clause, flagged
for maintainer confirmation): the SUM reading of PP5.0; both
pricings carried in all statements.

## Falsifier

A generating admissible row where LEMMA 3 carries margin under
reading A + (C); a proof that the intended ensemble is (C) (restores
(O1) at k = e); a Theta(n) loss under (C) beyond integrality.

## NOT claimed

(O1) itself, in either direction, on generating rows; the parity or
ensemble pins (maintainer); any Z_1 upper bound.

## Addendum (2026-08-06, the reading rulings — the 2x2 is RULED)

Coordinator rulings (user-prompted, soundness-forced, of record):
Lambda parity = READING A (forced by the proved trichotomy + the
lane's own text); ensemble = THE SLICE (T*) (forced by the
(O1) => (O2) fence — the consumer demands it); PP5.0 = SUM.
CONSEQUENCE: **(O1) AS POSED IS FALSE on generating rows as well as
non-generating ones** — the "two live values" language above is
superseded. The F2 lane's obligation of record is the minimal
surviving form with the MASS target and the tail-count criterion
(see f2_z1_mass_knife_edge). The former "maintainer seam" is
dissolved: these were conventions inside OUR chain, decided by what
makes the chain sound, and the spec-level scope question is decided
by the spec text itself (non-generating rows in-family; see the
2026-08-06 rulings entry in CAMPAIGN_LEDGER).

## Addendum 2 (2026-08-06, from round-20 f2_repose — the ensemble ruling RE-OPENED; the scope question DISSOLVED)

1. The ensemble ruling above (= the slice (T*)) is DOWNGRADED to
   PROVISIONAL: the consumer's own text is mixed (its mean is
   slice-calibrated, its window-empty test is the 2^n balance — one
   sentence, both ensembles; f2_repose A1), and the readings differ
   by EXISTENCE of a candidate, not margin (under (C): the FINITE
   target Z(L) <= 1 + N^3, a 4.77-bit Z_1 window; under (T*): an
   exact-value obligation no upper bound can meet, CATCH-R6). The
   fence/contract reconciliation is a named open task.
2. The maintainer-question line above is RESOLVED INTERNALLY: u2c
   CATCH #11 (banked 2026-07-07) is the consumer-side k = e rule —
   extension rows route through the f1/ext descent; the F2 lane
   never owed them. The right split is k = 1 (reduces verbatim to
   the PROVED f2_k1_contraction_theorem, bypassing (O1)) vs
   k >= 2 (open: k in {2,4}). Our rounds-17/18 non-generating kill
   was a re-derivation of CATCH #11 (subtraction, CATCH-R4).
3. The five-face seam: the consumer's own tolerance = the
   counting-balance surplus (CATCH-R1), reproducing the banked
   2^{1.05e12} to 0.047% — with the A2 arithmetic defect (n = 2^40
   vs N = 2^41) flagged for the extras-contraction node.

## Addendum 3 (2026-08-07, wave-47 — five classes, not three)

"Exactly three generating classes" is corrected to FIVE SIGNED
TYPES per the five-class census (see f2_admissible_object Addendum 2
+ f2_admissible_generating_branch_classification). The
non-generating kill and THEOREM Z2 are unaffected (both are
class-independent); the minimal surviving form's domain is the five
generating types, with the two minus-branch types lacking an object
model (the named round-20 residual).
