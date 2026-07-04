# conj_f conditional proof

## Predicate node

- `f_primitive_case`

## Proved reductions

- `f_gcd_reduction`
- `f_scale_recursion`

## Claim

Conditional on `f_primitive_case`, full Conjecture F holds.

## Proof

Let `P` be a linear flat of locators and consider the points of `P cap D_j`.

First apply `f_gcd_reduction`. If the members of `P cap D_j` share a common
divisor `g` of degree `w`, then division by `g` maps the section injectively
to a lower-degree section with trivial common gcd. The branch with large `w`
is exactly the paid tangent/common-divisor shape required by Conjecture F.
Thus the unpaid content may be reduced to gcd-trivial sections.

Next split the gcd-trivial section by periodicity. The proved
`f_scale_recursion` identifies the multiplicative `M`-pullback branch with a
linear section at quotient scale `n/M` and degree `j/M`. Those points are
therefore paid by the quotient/pullback stratum, or else recursively reduced
to a smaller-scale instance.

After removing the tangent/common-divisor branch and the quotient/pullback
branches, the remaining points are precisely the primitive, gcd-trivial,
aperiodic, unpaid points counted by `f_primitive_case`. That predicate gives a
bound of `n^{B_F}` for this residual set.

The reductions are injective on their branches and the scale recursion
terminates at smaller divisors of `n`, so the accumulated residual remains
polynomial. Therefore every point of `P cap D_j` is covered by a paid tangent
shape, a paid quotient-pullback stratum, or one of polynomially many primitive
exceptions. This is full Conjecture F conditional on `f_primitive_case`.
