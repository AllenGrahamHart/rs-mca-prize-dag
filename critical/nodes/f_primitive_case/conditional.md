# f_primitive_case conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `f_dim1`
- `f_concurrency_equiv`
- `f_dim2_skeleton`
- `f_dim_induction`

Evidence/calibration:

- `perfiber`
- `f_pair_bound_envelope`

## Claim

Conditional on the predicate nodes, every gcd-trivial, aperiodic, non-pullback
linear flat has only polynomially many unpaid points of `D_j`.

## Proof

The proved `f_concurrency_equiv` rewrites the primitive problem as a
`j`-fold-concurrency problem for the evaluation-hyperplane arrangement on the
linear flat `P`.

In dimension one, `f_dim1` proves the voting bound: a gcd-trivial pencil has at
most `n/j` members of `D_j`, far below the polynomial budget.

In dimension two, `f_dim2_skeleton` proves the pair-counting bound for
twin-free planes and charges twin coincidences to the tangent/gcd branch. Thus
the primitive plane base case is already controlled.

For dimensions at least three, `f_dim_induction` supplies the conditional
divisor-depth induction. Its spread branch is bounded by moment counting; its
coincident branch either gains shared-divisor depth via sparse descent or is
paid by the many-sparse structure taxonomy; and its descent tree terminates
polynomially.

Combining the dimension-one base, the dimension-two base, and the conditional
all-dimension induction gives the stated polynomial bound for the primitive
gcd-trivial non-pullback remainder. The calibration nodes `perfiber` and
`f_pair_bound_envelope` remain evidence for the shape; they are not additional
requirements for this conditional assembly.
