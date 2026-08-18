# Quadratic quotient-survivor identification

- **status:** PROVED
- **scope:** the antipodal and constant-product outputs of the quadratic
  survivor router

Let `H=mu_N` with `N=2^21`.

1. The antipodal involution `x -> -x` has exactly `N/2=1048576`
   nonfixed two-cycles. Their locators are the cyclic quotient pencil

   ```text
   X^2-y,       y in H^2.
   ```

2. For every `kappa in H`, the constant-product involution
   `x -> kappa/x` has

   ```text
   N/2       fibers if kappa is not in H^2,
   (N-2)/2   fibers if kappa is in H^2,
   ```

   after repeated-root fixed points are omitted. Their locators are the
   dihedral quotient pencil

   ```text
   X^2-sX+kappa,       s=x+kappa/x.
   ```

Thus every quadratic quotient survivor has at least `1048575` pairwise
disjoint split squarefree fibers, exceeding the synchronized demand `4370`
by at least `1044205`. These branches are genuine and cannot be removed by a
uniform small-fiber theorem. They must be paid through retained factor-owner,
denominator, recursive quotient, or chronology semantics.

The only quadratic branch that remains eligible for pointwise elimination is
shifted inversion with `tau,kappa!=0` and `lambda=kappa/tau^2!=1`.

## Falsifier

An antipodal pair outside the cyclic power pencil; a constant-product pair
outside the dihedral pencil; a wrong fixed-point count; duplicate slopes from
different nonfixed orbits; or any claim that quotient identification itself
pays these records.
