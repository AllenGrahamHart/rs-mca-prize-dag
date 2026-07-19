# F7 β-check: the count law at base-domain extension rows (node-local, 2026-07-07)

Part of the correspondence β-round (MB_VS_F1_LEDGER.md §7 follow-ups).
Script: `f7_beta_check_modal.py` (Modal, exact enumeration, <60s).

## The proved core (one line)

At a base-domain extension row (D ⊆ F_p ⊆ F_q) with a BASE-VALUED word,
every challenger (non-planted deg<k codeword with ≥ s = k+σ agreements)
interpolates through k base points with base values, so its coefficients
lie in F_p: the challenger set over F_q EQUALS the base-row challenger
set. Hence the count law for such words is ~ K_cell/p^σ, not K_cell/q^σ.
F7's WORST-WORD quantifier makes this bite (the adversary chooses
base-valued layouts/scalars); an average-form statement would have
diluted it by (p/q)^n.

## Census verification (E15/E22 conventions preserved exactly)

q = p² rows, σ = 1, exhaustive interpolant enumeration, 6 layouts/cell:

    cell (p,k)   base-valued challengers      generic challengers    coeffs base?
    (17,4) q=289 148,141,150,126,149,132      13,12,17,12,15,19      True (all)
    (17,2) q=289 13,12,14,14,10,12            2,2,4,2,1,2            True (all)
    (13,4) q=169 38,47,37,36,33,36            5,3,7,9,8,3            True (all)
    (13,2) q=169 4,7,8,6,8,2                  0,1,0,3,1,0            True (all)

Quantitative consistency: SAME K_cell, two denominators — e.g. (17,4):
K_cell ≈ 148·17 ≈ 2516; generic prediction K_cell/q ≈ 8.7 vs measured
12–19 (Poisson range); base/generic ratio ≈ q/p at both p. The q-law is
CORRECT for generic words and off by (q/p)^σ for base-valued words.

## Consequence for the floor (wording fix, catch #12)

The frozen quantifier "at every official-convention row" must read the
count law at the GENERATED field of the cell data:
challenger law ~ K_cell/|F_p(D, word)|^σ. All banked evidence (E22
census 135/135, envelope stress q = 97..1153, adversarial layouts) ran
at prime rows where the readings coincide — untouched. At base-domain
extension rows the f1/ext descent prices the base-valued stratum at the
base row (where the p-law IS the q-law); the envelope's residual claim
applies to the genuinely-F stratum. Same correction class as F2's
catch #11; here the exposure is CENSUS-VERIFIED, not just window
arithmetic.
