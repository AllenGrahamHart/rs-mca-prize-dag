# xr_syzygy_support_lemma

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/qx13_pair_rank_ledger.md']

## Statement

Alignment functionals of support T are exactly the dual codewords supported in T (Lambda_T, dim t; C-perp is MDS with min weight k+1); condition rows have tensor form (lambda, z lambda). Rank stagnation at a new support forces a SYZYGY: dual codewords lambda_i in Lambda_{T_i} with sum (z_i - z_m) phi_i = 0 (the twist is invertible since slopes are distinct). Support cancellation + the MDS dual weight then force: for some member i0, supp(lambda_i0) lies inside the union of its pairwise intersections, hence sum over partners |T_i0 cap T_i'| >= k+1. QUANTITATIVE CONSEQUENCE: in the far-spread regime (each overlap < k), every stagnation event needs >= 2 partners; the minimal configuration is a TRIPLE; and stagnation events are rationed by the family's total overlap mass.

## Attack surface

the derivation is complete as sketched (subtract z_m x first component; support cancellation; MDS dual weight); write the packet with the twist bookkeeping and the necessity/sufficiency gap stated (the twisted-psi membership in Lambda_{T_m} is an ADDITIONAL constraint beyond the syzygy)

## Falsifier

a toy stagnation with overlap budget < k+1 (mechanical check in any stacked-rank scan)

## Ledger (migrated notes)

PROVED (23,480 checks): the k+1 overlap budget, in the rank-linear-algebra model of qx13 (the ledger's own model — scoping consistent across the whole chain).
