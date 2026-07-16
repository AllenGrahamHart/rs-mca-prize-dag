# PMA sigma-one reciprocal-quadratic defect-three obstruction

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **role:** route cut for a universal per-sunflower `n^6` diffuse payment

## Statement

Let `H` be cyclic of order `n=2^s` in an odd finite field, put

```text
k=N=n/2,    M=n/4,
```

and assume `M>15`. There is a rate-half maximal sunflower word with distinct
nonzero petal scalars for which the finite `sigma=1`, `(d,r)=(3,0)` cell
contains at least

```text
L_RQ(n)
 = floor((M-15)(N-6)(N-3) binom(M,5)/(6M))             (RQ-LB)
```

distinct actual non-planted codewords. Every counted codeword has no full
petal and has trivial agreement stabilizer. In particular, on the official
rate-half row `n=2^41`,

```text
L_RQ(n)>n^6.
```

The family is field-independent once `H` exists; it is not a small-field or
ambient-list artifact.

## Construction

Let `G<H` be the index-two subgroup and `A=H\G`. Choose `r in A` and put

```text
Q(X)=X^(-1)+rX.
```

Take an antipodal transversal `X` of `A`, so `|X|=M`, and let `Y=-X`.
For a suitable background `b in G` and a suitable bijection `pi:X->Y`, use

```text
core C=G\{b},
petals T_x={x,pi(x)},
scalar c_x=Q(x).
```

For every selected five-set `S subset X`, every core triple `D` with

```text
product(D)=r product(S)
```

gives the residual cubic

```text
W=( (1+rX^2)L_D-rL_S )/X
```

and the actual source codeword `f=L_(C\D)W`. Averaging chooses `b` and `pi`
so that the lower bound `(RQ-LB)` survives the exact-background, diffuse, and
primitive filters.

## Consequence

The one-power saving requested after the fixed-hyperplane reduction is false
for the complete diffuse source class. The proved successor
`pma_sigma_one_index_two_core_owner` first-matches and prices this family
globally through its four-miss index-two core. The post-owner PMA theorem must
bound only the complementary incidence; it still cannot assert a uniform
`n^6` bound for the complete per-sunflower class.

This does not by itself refute `imgfib`: the final ledger may own this family
before the primitive mixed-petal column is charged.
