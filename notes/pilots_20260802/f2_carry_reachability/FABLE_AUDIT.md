# Fable audit of the F2A.2 pilot — 2026-08-02

**Verdict: ACCEPTED.** Opus-5 subagent pilot, directed per the Brief-5
adversarial-audit work packages. Audit trail:

- Re-ran the full validation suite (validate.py) independently under
  ramguard: ALL PASS (V1-V10, including the brute-forced Myhill-Nerode
  quotient V7 and the real-model carry-DFT product identity V9 at
  2e-14).
- Hand-verified the two load-bearing identities: (1) the delta normal
  form — w^p = -w for a non-residue square, so Tr(c y^p) flips the
  N b_c b_y term, giving delta = 4N b_c b_y mod p and the exact
  frequency dichotomy (b_c = 0 vacuous; otherwise no zero deltas and no
  proper subgroup available in Z/p); (2) the trace-zero dead mode —
  s(-) = p - s(+) with p odd gives f(p-s) = f(s) for
  f(s) = s + [2s>p] mod 2, so mode k = p has |M| = a+b exactly.
- The verdict logic is sound: Law B is measured on the REACHABLE
  Myhill-Nerode quotient (the audit's re-typed question), not the
  all-continuations version; the GF(2)-subspace robustness sweep
  addresses the seam-idealisation objection quantitatively.
- Honest-assumptions list is complete and correctly flags the
  tower-transport gap (q = p^k unverified).

Consequences adopted: PP5.4 = NEGATIVE (banked fence); carry-DFT route
mandatory; F2A.4 spec gains the k=p x trace-zero pre-registered owner
and the >= 0.24 bits/pair generic floor; K2 not triggered. Next F2 items
in queue order: F2A.0 seam (planner), F2A.3 carry-DFT node (mintable
after seam), F2A.4 mode compiler (worker).
