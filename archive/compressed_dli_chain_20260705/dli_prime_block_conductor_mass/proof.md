# proof: dli_prime_block_conductor_mass — conditional on large-block support (Pro T3-followup, verified)

REFUTED as an unconditional consequence of the T3 hypotheses; PROVED conditional on
dli_prime_weighted_large_block_support.

## Refutation (VERIFIED, elementary): small blocks kill the ledger
For a FREE/adversarial partition the leaf is false. Singleton blocks (P=X, lambda=1,
prime field, no trace collapse): every singleton has |mu_hat|=1 and is exceptional,
so D_{j,lambda} >= sum_X m = 256 L_j = Omega(L_j), and S_{j,1}=256 L_j too. Fixed
K-blocks: nonexceptional conductor term ~ (256/K) L_j = Omega(L_j); exceptional =>
sum_X m = Omega(L_j). Either way Omega(L_j). Deligne gives per-block saving ~1/|A_r|,
but positive mass on BOUNDED-size blocks keeps the total linear in L_j. Low degree
bounds each atom's size, NOT how much mass sits on many tiny atoms. The missing
estimate is WEIGHTED ANTI-CONCENTRATION of the residue partition.

## Conditional theorem (PROVED given large-block support)
If (i) mass on exceptional + small blocks (|A_{j,r}| < B_j) is o(L_j) and (ii)
Gamma_j/B_j -> 0 (Gamma_j = sup cond^2), then: large blocks (|A|>=B_j) give
sum m cond^2/|A| <= (Gamma_j/B_j) * 256 L_j = o(L_j); plus the o(L_j) small part =>
D_{j,lambda}=o(L_j). VERIFIED.

## Key subtlety (why this is not a real DLI failure)
The refutation uses a FREE partition. The REAL DLI blocks are MAP-DETERMINED
(degree-preimage of the odd-eval map on the square-root section), NOT free. The leaf
is exactly that the ACTUAL map-partition puts o(L_j) mass on small blocks (large-block
support). This is load-bearing and consistent with the calibration eta*/L=3.6e-7
(which flatness requires large blocks); if the real partition had linear small-block
mass, DLI would fail. => new deepest leaf: dli_prime_weighted_large_block_support.

## REPOSE (2026-07-05): sup -> U-weighted average
The claim this node carries is now the U-WEIGHTED form (E_U over central profiles),
matching the re-posed leaf (weighted average / RES count) and the endpoint (b2b
U-weighted average of prod rho_j). The pointwise reduction above is UNCHANGED — it is
applied per-profile inside the average. Why the weighted form is safe where the sup
failed: low-mass profiles (all-singleton blocks, X_j ~ L_j, |mu_hat|=1) falsify the
sup but carry weight fraction <= 2^{-501 L_j} against penalty q^{L_j} = 2^{256 L_j}
— net 2^{-245 L_j} (verified; matches Codex's alpha=256 envelope -0.9639 ~ -245/256
and its exact weighted DPs, rho = 1.000000 flat).
