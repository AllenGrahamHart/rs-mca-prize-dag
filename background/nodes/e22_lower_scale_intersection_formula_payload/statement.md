# e22_lower_scale_intersection_formula_payload

- **status:** PROVED
- **closure:** proof

## Statement

For every dyadic pair `M_i<M_j` and every subset `S` of smaller dyadic scales
`M'<M_i`, the dyadic-tree tail polynomial gives exact coefficient formulas
and bijection/weight checks for the residual profiles that:

- are raw-admissible at `M_j`;
- are admissible at every scale in `S`; and
- carry the `dyadic_profile_evaluation` multiplicity.

For a constrained scale set

```text
C = {M_i, M_j} union S,
```

the formula is the finite coefficient extraction from the recursively defined
dyadic occupancy polynomial:

```text
P_1 = 1 + X,

P_L = tau_L(P_{L/2}^2),

tau_L(X^s m) =
    X^s Y_L^s m       if L in C and s < L,
    X^s m             otherwise.
```

Here `X` records support size inside the current dyadic block and `Y_L`
records the recovered tail contribution at scale `L`. The required weighted
intersection count is the sum of `dyadic_profile_evaluation` weights over the
atoms whose `Y_M` exponents satisfy

```text
b_{M_i}<M_i,  b_{M_j}<M_j,  and  b_M<M for every M in S.
```

## Falsifier

A missing subset `S`, an incorrect coefficient formula, or a multiplicity
mismatch with `dyadic_profile_evaluation`.
