# proof: petal_primitive_residue_kernel_rank — 3-gate descent decomposition (Pro T7)
Conditional theorem PROVED: Gates N(petal_newton_window) + D(petal_quotient_descent_step)
+ L(petal_low_defect_quotient_charge) => PRK_pet with B_pet=kappa_N+theta+b_N+1. Descent:
Gate N gives window m>=c-kappa_N; descend via D while m>=theta*Q (charges coarser quotient,
terminates); terminal short window => L charges a low-defect sheet. Uncharged survives only
if c<theta+kappa_N (bounded) => dim Pi_prim<=B_pet => q^{B_pet} points, c-independent.
GUARDRAIL (verified necessary): naive PRK omitting low-defect sheets is REFUTED (L1 dyadic
toy Z_1,Z_2,Z_3 are large terminal sheets, must be charged). Remaining: prove N,D,L.
