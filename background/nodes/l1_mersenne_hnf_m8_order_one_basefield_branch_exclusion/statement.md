# L1 Mersenne HNF m=8 order-one base-field branch exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_basefield_conic_router`
- **consumer:** `l1_mixed_petal_amplification`

The complete `t in F_p` branch of the `m=8,h=7` order-one conic is empty on
all four official rows.

The two smaller characteristics are already empty by the dependency. On the
two residual characteristics, coefficientwise Frobenius satisfies

```text
P^[p](W)=-P(1-W).                                     (BBE1)
```

Consequently, if `x` is any root of `P`, both `x` and `1-x` are roots of
unity of order dividing

```text
n=8(p+1)=2^(q+3),       p=2^q-1.                     (BBE2)
```

There are at most six such field elements. Since `P` is squarefree of degree
seven, this is impossible.

Thus no finite packet from the base-field conic router requires computation.
Only `t notin F_p` remains in the `h=7` order-one curve. The `h=15`, lower
value-degree, nonembedded `m=4,h=2`, and inner-lift branches remain open.
