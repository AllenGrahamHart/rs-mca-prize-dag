# Fable audit of the band adjudication pilot — 2026-08-02

**Verdict: ACCEPTED — the program's top adjudication is RESOLVED with
a priced recommendation, and the band proper is PROVED protected from
the MC/coset class (THEOREM BP).** Replayed exp_band_proper (135),
rows (66), exp_quotient_periodicity (104) — 0 fails; 574 checks total
in the record. Hand-verified: the depth dictionary (definitional),
MC-6's folding proof (coefficient matching against the coset-locator
gap — sound; the joint-family step is genuinely new and closes a gap
in MY OWN round-4 framing, which asserted the pair count without
proof), THEOREM BP's 2-adic exclusion + parity argument (h odd makes
h-d odd for even d, forcing g = 1 hence d = h-1 — elegant and
correct), and the exclusivity via k-packing (one line).

Adopted (RATIFICATION ITEM for the user, recommendation ready):
1. **d = h-1 is the cascade tier definitionally; RECOMMENDED
   RESOLUTION = fold it into the band column [1, h-1] in the third
   generic column, naming the tier explicitly.** Cost 4.26-4.39% at
   the prize rows; closes the A-1 zero-count scope hole; B_tan stays
   printed (trigger 4 never fires; the 0.858 retune bits survive);
   the extension term is EXACT by exclusivity (|Gamma_casc| = Sum L_P,
   the ledger is TIGHT at the tier). The B_tan re-baseline
   alternative is strictly dominated (same 13n^3, zero headroom).
2. **MC does not refute the occupancy lemma under the banked selected
   semantics** (N_{h-1} <= n/2, -46 bits); the "any exact-A ray"
   reading would flip it (+44..+111 bits) — the L_P/N_d definitions
   (list item 8) are load-bearing and go into the coordinated edit
   verbatim. The full 10-item definitions list is ADOPTED as the
   glossary section of the Route T edit.
3. **MC is quotient-paid (P3)** — subject to the one unverified step
   (the quotient convention's "syndromes descend"), queued for the
   quotient-convention audit; the occupancy verdict does NOT depend
   on it.
4. **The B_tan overflow witness at official parameters**
   (x1.34/1.15/1.07) upgrades the payment-audit exposure from toy to
   the six rows — recorded for the cascade-tier accounting in the
   coordinated edit.
5. **Internal adversarial review queue**: the Gamma subset -H claim
   (toy-verified only — the sharpest falsifier direction against the
   occupancy verdict) is the first item for a dedicated adversarial
   pilot next round.

Caveats endorsed: toy scale; BP protects against coset-type attacks
(char-p non-coset accidents observed OUTSIDE the six-row shape); BP(2)
covers the shift class only; the bare-python3 patch was text-only.
