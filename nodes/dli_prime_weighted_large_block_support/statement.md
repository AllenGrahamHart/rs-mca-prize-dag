# dli_prime_weighted_large_block_support

- **status:** TARGET (the dli frontier; single arc into x4_exactlist_staircase_split)

## Statement

The U-weighted / RES counting obligation (re-posed 2026-07-05 after the sup form was
refuted): over the central profile measure, E_U[q^{eta_j}] = q^{o(L_j)} per level --
equivalently the RES resultant-survivor count |R_j(M)| <= q^{kappa_j} U_j/q^{L_j} with
sum kappa_j = o(t) in U-weighted form. Exact reduction (PROVED, Lemma 1):
rho_j(M) = q^{L_j}|Z_j(M)|/U_j, Z_j the bounded-coefficient kernel skews.

Empirical: calibration reproduced on the real object (3 independent computations);
weighted DPs flat (rho = 1.000000); low-mass tail self-kills at 2^{-245 L_j}.
See REDUCTION_PACKET.md on the interface for the composed conditional proof.
