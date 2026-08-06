# FABLE_AUDIT — es_axkatz_transfer (round 16, pilot 2 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED — the Ax-Katz /
Chevalley-Warning transfer on (ES) is DEAD by four mechanisms, and the
strongest kill is structural: THEOREM AK-UNIT shows the (ES) target is
a p-adic unit, so ANY p-divisibility theorem has the wrong conclusion
shape — a non-vacuous one would prove accident EXISTENCE, i.e. refute
(ES), never prove it. The last named classical transfer is closed.**

Replay: verify_axkatz.py 32 checks 0 failures exit 0 (coordinator
re-run under ramguard local); the pilot additionally verified
fail-closed by injected failure. Cross-checks against banked results
exact: log2 C(128,63) = 124.1491 vs verify_rows.py [B3] 2^124.15;
delta=1 crossover w* = 2^33.0005 reproduced.

ADOPTED:
- **THEOREM AK-UNIT + COROLLARY AK-ACCIDENT (unconditional)** — the
  conclusion-shape cut over the whole congruence family (CW, Ax, Katz,
  Ax-Katz, Moreno-Moreno, Adolphson-Sperber, Wan, McEliece), exponent-
  independent. **THEOREM AK-WARN** (conditional on (ES) at crossing
  rows): no exact algebraization can have positive Ax-Katz exponent —
  the vacuity is forced, not an encoding artefact. PROPOSITION McE-VAC.
- The exact exponent table: mu ~ -1.1e12 at every row/reading,
  shortfall 2^41.0-2^41.3 degree-units; formula validated on 144
  brute-forced systems all with mu >= 1, 0 violations.
- DEAD-INSENSITIVE on the round-15 separating witness: counts separate
  {0,...,276} while mu, |Z_w|, McEliece ell are all constant — and
  every nonzero count is coprime to p.
- **The (ES) frontier REFRAMED**: the surviving invariant is the
  defining set's divisor profile D(Z); the named open problem is a
  characteristic-p analogue of vanishing-sums-of-roots-of-unity
  rigidity (Lam-Leung / Conway-Jones) in the sub-balance regime —
  a rigidity/equidistribution question, not divisibility. The Pro
  brief (when Pro resumes) must state AK-UNIT up front.

CATCHES ACCEPTED:
- **CATCH-16A**: ALG-I is inexact when p <= n (weight pinned only
  mod p; explicit n=8, p=7, delta=2 witness); ALG-L is the exact,
  load-bearing encoding. Any future (ES) algebraization must use the
  locator reading or re-prove exactness.
- **CATCH-16B (kept on the board)**: at the BAND rows — where the
  structural families are empty and the target is genuine vanishing —
  mu >= 1 alone would close the route via the 0.68n^2 budget
  (2^81.4 < q). The entire gap is the exponent. This is the single
  live p-divisibility seam in the terminal; it survives AK-UNIT
  because there the structural count is 0.

Honest residuals accepted as stated (AK-WARN's (ES)-conditionality;
band rows closed by vacuity only; |Z_w| unpinned but nothing turns on
it; prod T = gamma clause shifts mu by <= 1; Adolphson-Sperber/Wan
excluded by shape, not computed — correctly labelled). Sibling
independence honoured (es_boundary_adversary contents unread; names
seen only as git-status metadata — acceptable). DRAFT-ONLY confirmed.

Coordinator note: with this bank, (ES)'s classical-transfer ledger is
COMPLETE — enumerator methods (refuted by theorem, round 15), Weil/C-U
(vacuous), L2 (loses 2^128), and now the entire congruence family
(wrong conclusion shape). What remains is rigidity (the reframed open
problem), CATCH-16B's band seam, and the empirical boundary (sibling
pilot, still running).
