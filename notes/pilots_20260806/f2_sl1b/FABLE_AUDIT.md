# FABLE_AUDIT — f2_sl1b (round 16, pilot 1 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED — SL-1b PROVED as
literally stated (new k-free LEMMA SL-1b-DIM, sharp both sides) and
REFUTED in its intended reading (61 deployed-family witnesses), so the
obligation was NON-LOAD-BEARING: mystery 2's list shortens in name
only, and the real residual is SL-1b′ = the Z(L) terminal already
named.**

Replay: verify.py 37/37 PASS, exit 0, digest F2_SL1B_ALL_PASS
(coordinator re-run under ramguard local). Anchor spot-checks all
verbatim-exact: the SL-1b statement (f2_sl1_powersums/PROOFS.md:316-319),
the floor(log2 p) line (verify.py:454), the two-conclusions block
(PROOFS.md:296-299), the n | p^2-1 setting (f2_opening/PROOFS.md:10),
the DLI precedent (dli_prime_weighted_large_block_support/proof.md:18-21).

ADOPTED:
- The (R-A)/(R-B) split (DEFECT-1) — PROOFS.md governs; the audit gloss
  DEFECT-2 is MY round-15 wording, accepted as my defect.
- **LEMMA SL-1b-DIM**: min(m,R) <= dim_{F_p} L <= min(m, k|Lambda|),
  lower bound k-free via SL-1's own diagonal x Vandermonde minor;
  sharp at both ends (131/131 k=1 rows attain the floor); the factor-2
  no-go (t >= 2m log_p 3 cannot relax without importing k).
- (R-B) REFUTED: the "iff" at PROOFS.md:298 was a random-subspace
  statement, not a deployed-L property; 61 witnesses + the official-
  prime abstract witness; disjoint-code-path (cyclotomic) confirmation.
- The one real gain: LEMMA 3's necessary condition now VERIFIED from
  below at rung 16 under the large-t readings.

CATCHES ACCEPTED:
- **CATCH-A**: the round-15 S4 "never under-predicts" measurement is
  RETRACTED AS SUPPORT — its code used floor(log2 p); 61/61 false
  negatives under the predicate as written. Correction note queued for
  mint-4 (f2_sl1_powersums S4 addendum).
- **CATCH-B**: coordinator RE-DERIVED independently — v2(p^2-1) = 25
  for the KoalaBear prime, so n_j | p^2-1 holds ONLY at rung 1;
  f2_opening's stated setting is rung-1-only. Queued for mint-4.
- **CATCH-C**: the DLI lane's "no rank defect" refutation is the
  uncited precedent; joins the F2<->DLI/WCL crosswalk mint item.

INTERACTION-1 — ADJUDICATED BY THE COORDINATOR against the sibling
f2_tq_pin report (same round): the tower reading is MOOT because the
16-rung tower is not prize-admissible (f2_tq_pin CATCH-1, rungs >= 4
break the field cap); on the deployed tower-as-written, LEMMA 3 at
rung 16 is violated under EVERY rules-admissible t (f2_tq_pin P5), so
round-15's CATCH-4 sign flip SURVIVES and is strengthened, while this
pilot's k_16-vacuity caveat applies only to a row the rules exclude.
The joint statement of record lives in the round-16 bank entry.

Honest residuals accepted as stated (witness box scope; (R-A) open
cells; SL-1b′ untouched; the Frobenius-closure lead recorded not
evaluated). Minor report defect (harmless): none found beyond MY
DEFECT-2 gloss. DRAFT-ONLY compliance confirmed via git status.
