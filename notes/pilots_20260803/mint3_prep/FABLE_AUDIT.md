# Coordinator audit — mint-3 (round-12 harvest)

**Auditor:** Fable, 2026-08-03. **Verdict: 2 of 3 packages WIRED;
1 HELD; the refusal and both downgrades ENDORSED.**

Replay: all three draft verifiers PASS (42 checks; three are strictly
STRONGER than their sources — two hard-coded-True checks now computed,
one one-directional check now bidirectional: exemplary); toeplitz.py
replayed by the coordinator (closing my own replay gap the pilot
flagged). OV REPORT.md persisted before wiring (the pilot's
recommendation, executed). The owed ej_coset_spread FABLE_AUDIT
written (the pilot's flag was correct — my banking had been
ledger-level only).

WIRED (dag 1795/4998, all green):
- **xr_pencil_forcing_t0** (T0 + P-SHARE + LEMMAS 2-5; residual
  t <= 2e-3 = h >= 3d+3 explicitly not-claimed, with the pilot's
  sharpening that the band is EMPTY for t <= 4). ev -> band TARGET;
  ref from xr_support4_structure. My hand-verified steps: LEMMA 5,
  case-(b) cross-multiplication, the T0 => M <= 1 => C = 1/2 chain.
- **xr_ov_slope_free_reduction** (THEOREM 1 dictionary + THEOREM 2
  Jperp reduction + THEOREM 5, PG(2,3); THEOREMS 3/4 labeled
  not-hand-verified IN the statement; OV explicitly OPEN). ref ->
  xr_support4_structure (the pilot's flagged alternative ADOPTED —
  the ev into the TARGET was too loose absent an OV node).

HELD: **xr_window_system_descent** — THEOREM L's proof is
RECONSTRUCTED with two named gaps and none of W/D/L/R has coordinator
hand-verification (sl2's audit predates the mint flags). A PROVED
node cannot carry a reconstructed-with-gaps theorem. Queued for a
dedicated line-audit (the draft + its 16-check verifier stand ready;
the LEMMA W attribution downgrade to counting_frame is CORRECT and
kept).

ENDORSED: the xr_gamma_coset_reduction REFUSAL (three claims = banked
wording of record; THEOREM G/H unaudited — now explicit in the ej
audit); the sl1-THEOREM-F duplicate refusal; the E1-PENCIL refusal.
ADOPTED recommendation: escape-1's THEOREM D (3-drop) + UPB join the
window-descent node in the MINT-4 QUEUE (D and UPB were both
coordinator-hand-verified at banking, so mint-4 is drafting work
only). The pilot's bare-python probe self-report recorded.
