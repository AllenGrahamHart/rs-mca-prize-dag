# PMA sigma-one diffuse defect-three hyperplane reduction

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **dependencies:** `pma_source_paving_bridge`,
  `pma_sigma_one_d3_full_petal_payment`

## Statement

Work in the finite `sigma=1`, `(d,r)=(3,0)` diffuse class isolated by
`pma_sigma_one_d3_full_petal_payment`. Let

```text
S={x_1,...,x_5}
```

be the first five agreement points. They lie in distinct petals, whose
distinct scalars are `c_1,...,c_5`. Put

```text
lambda_j = product_(m!=j)(x_j-x_m)^(-1),
A_t(S) = sum_(j=1)^5 lambda_j c_j x_j^t,    0<=t<=3.
```

Then `(A_0,A_1,A_2,A_3)` is nonzero. If the missed-core locator is

```text
L_D(X)=X^3-e_1(D)X^2+e_2(D)X-e_3(D),
```

it satisfies the explicit affine hyperplane equation

```text
A_3-A_2 e_1(D)+A_1 e_2(D)-A_0 e_3(D)=0.       (DH)
```

The first four values determine the residual cubic `W`. Thus a diffuse source
object injects into its canonical pair `(S,D)`.

If the core has size `K=k-1`, every fixed nonzero hyperplane `(DH)` contains
strictly fewer than `K^2/2` split monic cubic locators with three distinct
roots in the core. Consequently the complete diffuse class is bounded by

```text
#DIFF_30 < 16 K^2 binom(M,5),    M=(n-k)/2.          (DHB)
```

## Consequence

The diffuse defect-three problem is an aggregate incidence problem between
canonical five-point hyperplanes and split cubic core locators. A direct sum
of `(DHB)` has order `n^7`. The subsequent proved
`pma_sigma_one_d3_reciprocal_quadratic_obstruction` constructs actual
primitive source objects attaining this exponent, so a universal one-power
saving is false. The proved `pma_sigma_one_index_two_core_owner` now pays that
family globally. The finite route requires a complementary aggregate estimate
only after both global owners are removed.

## Scope

This theorem is field-independent and exact. It is a structural reduction,
not a finite PMA payment and not a counterexample to `imgfib`.
