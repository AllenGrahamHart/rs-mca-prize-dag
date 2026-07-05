# REDUCTION PACKET: petal chain (frontier -> interface), compressed 2026-07-05

Frontier: petal_cofactor_chargeability (band pricing). Interface: this node (band-split sparsity).
Verified structural line: top coefficient alive iff d >= M(t-2) (band width ell).

## Compressed steps (archive/compressed_petal_chain_20260705/)

### [CONDITIONAL] petal_squarefree_classification_ledger_payload
CONDITIONAL on P5-CL (Pro P5): every squarefree full-petal kernel point injects into the cofactor space V_c (deg A_i<=c, dim K<=c+1 by Lemma 13), so all c-growth is in the cofactor coordinate. CLOSES given P5-CL: every cofactor family of dim > absolute B_pet is QUOTIENT/coset/signed/cyclotomic chargeable (sparse coeff support signature); then uncharged count is c-independent, total <= 2^M poly(M)
NOTES: CENSUS RAN, INCONCLUSIVE (Modal): measures RAW extras (0->462 threshold jump, = charged coset mass) not the UNCHARGED residual the claim bounds; raw dim_K exceeds Lemma 13 c+1 (scope flag for audit). Needs a REFINED census separating charged/uncharge

### [CONDITIONAL] petal_squarefree_kernel_classification_payload
Classify the squarefree locator points inside the residue-line kernels across the coset-chart corridor into charged families and uncharged families with polynomial bounds whose exponents are independent of the excess c. This is reduced to the proved classification-ledger soundness rule plus the remaining actual squarefree classification ledger payload.


## Reattached side-inputs
- petal_squarefree_classification_ledger_soundness [PROVED]
- q_cofactor_normal_form [PROVED]