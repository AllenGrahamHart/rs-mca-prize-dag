# b2_modp_giant_extras

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/u2c_falsifier_scan.md']

## Statement

At official prize-max rows: the count of non-coset-union t-null blocks (and their trade families) is <= n^3 = 2^123. STRUCTURE: (i) THE FROBENIUS GAP — q = 1 mod n makes Frobenius act trivially on frequencies, so B1's Galois forcing has NO mod-p analogue; extras genuinely can exist (the X-8 boundary class is exactly such) — the char-0/finite-field gap is fundamental, not technical. (ii) THE FIRST-MOMENT BALANCE: t log2 q ~ 2.15e12 vs log2(2^n) = 2.2e12 — the prize-max giant regime sits within ~2% of the counting threshold; pure counting can NEVER close it. (iii) THE CUSHION: the budget is 2^123, not 1 — the statement is 'no 2^123-fold concentration above the balanced mean', a FIXED arithmetic quantity per row (no adversarial quantifier). (iv) The boundary/zero-sum class is EXACTLY counted (QA.25: <= 64 per row, fits). Routes for the residue: the divisor frame (L_B = degree-b divisor of X^n - delta with a top-t coefficient gap — divisor-with-prescribed-coefficients counting), the mu_M-fiber descent (128 coupled fiber-DFTs), or a second-moment/pair-correlation bound at giant scale. SCAN VERDICT (39/39 rows, replayed): NOT FALSIFIED — and the shape is the best case: NO spike at the balance crossing; extras die BEFORE nominal balance, decaying faster than the mean; above balance every t-null block is exactly a coset union (the coset floor). Max observed excess 2^4.18 vs the toy cushion 2^15 — concentration exponent ~4 bits against the 123-bit prize cushion. NO SIXTH GUISE: every near-crossing survivor is X-8/QA.25 boundary-class. Coverage exact and honest: exhaustive mu_32 all-t, n=64 window b in [5,10] (amended from [5,16], disclosed), n=256/512 known-class arithmetic + falsifier-only sampling. RESIDUAL for the proof: large weights and prize scales rest on known-class arithmetic — the divisor-frame lemma must close them, now with the calibrated target: smooth sub-mean decay, boundary-class-only survivors, 119 bits of margin.

## Attack surface

the divisor-counting frame is the most promising: monic degree-b divisors of a fully-split X^n - delta with t prescribed top coefficients — a concrete F_q[X] counting question with possible Hayes/Carlitz-style tools; the cushion means even 2^100-lossy bounds close it

## Falsifier

a toy-scale analogue showing concentration ~2^{cushion} above the mean (scaled: count non-coset t-null blocks at n = 256, t = 16, q chosen near the balance point — extend the U2-C scan machinery)
