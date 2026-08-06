# FABLE_AUDIT — f2_tq_pin (round 16, pilot 3 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED, MAINTAINER-LEVEL —
the t catch resolves harder than posed: t = 7e10 is a unit error
excluded by the rules under both field readings; t* is right in kind
(t pinned to the interval (2^33, 5.364e10]); and CATCH-1 finds the
16-rung KoalaBear tower is NOT PRIZE-ADMISSIBLE (field cap broken from
rung 4; admissible region v_2(e) <= 2, e <= 6, log2 p >= 39, depth
<= 2). The F2 discharge headline "rungs 1-13" is WITHDRAWN of record:
on the tower-as-written the band is rungs 1-10 (1-9 under the stricter
window reading the rules clause mandates), and every F2 statement at
rungs >= 4 carries a scope defect pending re-derivation on an
admissible row.**

Replay: verify.py 64/64 PASS exit 0, digest F2_TQ_PIN_VERIFY_ALL_PASS
(coordinator re-run under ramguard tiny). Anchor spot-checks verbatim-
exact: rules_freeze/statement.md:9 (including the "plans against the
stricter reading" clause CATCH-3 turns on); field_cap_check/statement.md:9
(the standing tower-admissibility question, now ANSWERED) and :13;
background/nodes/official_row_primes_pinning/proof.md:25-33;
background/nodes/xr_radius_arithmetic/proof.md:33 ("Prize convention",
self-labelled) and :41-43 ((T*) verbatim). Minor report defect: two
citations carried a critical/ prefix for nodes that live under
background/ — paths corrected here, content exact.

ADOPTED:
- (P1) the negative pin: rules pin an admissibility region + quantifier,
  no rules-level p, k, q, t; the forced facts (R1) n | q-1 hence q > n,
  (R2) L < 256, (R3) stricter-reading clause. The explicit admissible
  prize-max row (p = 18446735827372343297, q = p^4, v_2(q-1) = 41)
  as the non-vacuity witness.
- (P2)-(P3) the adjudication of record: t = n/L to 0.0044%;
  t in (2^33, 5.364e10]; 7e10 back-implies log2 q = 31.4, impossible
  for any field containing a 2^41-subgroup — WRONG IN KIND. t* right
  in kind, right to 3 significant figures.
- (P4) m_16 = 2^38 new-part vs 2^39 nested — a reading conflict, both
  correct counts of different windows; the stricter (2^39) governs
  published margins per CATCH-3.
- (P5) the band of record (tower-as-written): rungs 1-10 new-part,
  1-9 nested; LEMMA 3 violated at rung 16 under EVERY admissible t.
  Round-15's CATCH-4 sign flip is CONFIRMED AND STRENGTHENED (was
  t*-specific, now rules-forced). SL-1 immunity reproduced.
- (P6) the |K1|/PP5.0 seam PRICED, not frozen: average-vs-sum = exactly
  2^{n/2} (a structural identity, (t*/2)L = n/2); Theta(n) under both
  readings, never absorbable in o(n). The PP5.0 composition choice is
  a genuine open decision — SURFACED to the user, not resolved.

CROSS-PILOT ADJUDICATION (with f2_sl1b, same round): SL-1b's
INTERACTION-1 (k = 2 vs k = 3 vs tower-k_16 at rung 16) is settled by
CATCH-1 — the tower reading describes a rules-excluded row, so the
k_16-vacuity branch is moot; on the deployed tower-as-written the
violation stands under every admissible t. The two pilots' PROVED
cells are k-free and unaffected in both directions.

CATCHES ACCEPTED: CATCH-1 (maintainer-level, answers
field_cap_check:9); CATCH-2 (L = 255.9 convention vs sliver left
endpoint 255.911275 — 0.011-bit inconsistency; xr_radius_arithmetic
addendum queued); CATCH-3 (stricter-reading clause never invoked —
standing process rule adopted: quote margins under both windows);
CATCH-4 (b2_modp_giant_extras "~2%" is 0.0044% — strengthens its own
conclusion; addendum queued); CATCH-5 (sliver generator is t*L >= n,
not (T*)).

HONEST RESIDUALS accepted, two elevated: (1) the t-NAMING COLLISION
(LEMMA 3's t = |Lambda| vs xr_radius_arithmetic's t = A - k; three
lanes agree on 2^33 but no proof identifies them) — candidate
next-round derivation; (2) F2-ADM, the successor task: re-derive the
F2 obligations on an admissible <= 2-rung tower — what mystery 2
becomes there is open. Also: t* conditional on xr_ledger_qpower; the
rate_half_cyclic_simple_pole_mca_floor near-collision (8,592,912,739
vs 8,594,128,895 — different objects) queued for maintainer
reconciliation.

Process defect self-reported (one bare python3, read-only, re-run
under ramguard, no result used) — accepted with disclosure; the
violation-and-disclosure pattern is exactly what the law is for.
DRAFT-ONLY confirmed via git status.
