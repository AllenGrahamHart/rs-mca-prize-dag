# Audit

- The proof works with the scalar syndrome Hankel pencil, not an arbitrary
  matrix pencil.  The common right/left generator comes from the binary
  divided-power apolar complete intersection.
- The parameter degree is paid on **both** nullspaces.  Omitting the left
  minimal indices weakens the result enough to lose the official corollary.
- Fixed domain roots are not silently discarded.  Applying their fixed
  differential operator gives the residual inequality `(A+s)e<=rho-s`.
- Rank-drop slopes are not added with a loose `rho` bound.  Their exact KCF
  allowance `delta=rho-Ae` is coupled to the moving degree used by incidence.
- Root incidence is applied only at generic-rank slopes, where every split
  locator is divisible by the specialized apolar generator.  All exceptional
  slopes are charged to `delta`.
- The `A=5,e=1` floor is load-bearing: the exact value is `6`, giving
  `rho+1`.  Replacing it by the real upper bound `7` would not prove the last
  included budget.
- The result deliberately leaves `A=3` and `A=1` open.  Moving kernels exist:
  at `R=8,r=rho=3`, the moment pencil `e_5+Z e_2` has moving kernel
  `1-ZX^3`.  Thus no common-kernel classification is consumed.
