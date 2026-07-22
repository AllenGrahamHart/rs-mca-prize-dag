# L1 full-domain pullback intrinsic rigidity

- **status:** PROVED
- **role:** identify every full-domain polynomial pullback with the intrinsic
  cyclic quotient partition
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Theorem

Let `K` be a finite field and let

```text
H=alpha mu_n subset K^*,       |H|=n.                 (IR1)
```

Let `s|n`, `s>1`, and let `P in K[X]` be monic of degree `s`. Suppose `H` is
partitioned into complete level fibers of `P`, each having exactly `s`
points. Then there is a constant `c in K` such that

```text
P(X)=X^s+c.                                            (IR2)
```

Consequently the `P`-fiber partition of `H` is exactly the intrinsic quotient
by the unique order-`s` subgroup `mu_s` of `mu_n`. Any exact agreement support
that is a union of these fibers has multiplicative stabilizer containing
`mu_s` and is already owned by `pma_exact_periodic_owner`.

## L1 consequence

There is no non-intrinsic full-domain pullback branch. Across all degrees, the
only full-domain partitions are the intrinsic dyadic scales already covered
by the intrinsic quotient and exact-periodic ledgers. In particular, the
sub-Johnson remainder left by
`l1_full_pullback_divisibility_johnson_closure` is globally retired whenever
the complete agreement support is fully fiberwise.

The surviving general-pullback residual requires at least one of:

1. the map has incomplete fibers or residual domain points;
2. the contributor agrees only partially on at least one fiber; or
3. the internal map does not carry a whole fixed-source petal.

The exact `F_17^*` affine-quadratic obstruction has the first two features and
is therefore consistent with `(IR2)`.
