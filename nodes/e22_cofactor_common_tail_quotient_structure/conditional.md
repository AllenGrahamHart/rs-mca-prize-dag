# conditional: e22_cofactor_common_tail_quotient_structure

## Predicate nodes

- `e22_kernel_invariance_full_fiber_criterion`
- `e22_cofactor_common_tail_kernel_invariance`

## Claim

Conditional on the E22-specific common-tail kernel-invariance theorem, the
cofactor divisors supply a common bounded tail and local dyadic full-fiber
structure.

## Proof

The remaining predicate `e22_cofactor_common_tail_kernel_invariance` supplies
one common tail `B`, dyadic local moduli `M_i>t`, the bound

```text
|B| < min_i M_i,
```

and invariance of each `T_i\B` under the `M_i`-th-root kernel.

The proved node `e22_kernel_invariance_full_fiber_criterion` says that a
subset invariant under that kernel is exactly a union of full fibers of
`x -> x^{M_i}`. Therefore every non-tail set `T_i\B` is a union of full local
quotient fibers, with the advertised common tail and tail bound.
