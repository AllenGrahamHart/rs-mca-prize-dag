# DLI full-spectrum primitive polymer majorant

- **status:** PROVED
- **closure:** proof

Let `v_1,...,v_N` lie in an abelian group and let

```text
K = {c in {-1,0,1}^N : sum_i c_i v_i = 0}.
```

Give `c` weight `z(c)=2^(-|supp(c)|)`. Call a nonzero member of `K`
primitive if no nonzero proper support restriction also lies in `K`. Put

```text
Z = sum_(c in K) z(c),
P = sum_(primitive c in K) z(c).
```

Then

```text
Z <= exp(P).
```

For a DLI level, the fused four-state zero-fiber normalization satisfies

```text
E_j = r_j Z_j,             r_j=q^(ell_j)/2^(256 ell_j).
```

If `W_full,j` is the raw full-spectrum primitive signed-shift ledger, charging
each primitive orbit of weight `w` by `2N_j 2^-w`, then `P_j<=W_full,j` and

```text
E_j <= r_j exp(W_full,j).
```

On the official schedule `sum_j ell_j=t`. Consequently

```text
product_j E_j <= 2^100
```

follows from the single aggregate primitive-excess budget

```text
sum_j W_full,j <= 100 log(2) + t log(2^256/q).
```

This is an exact replacement interface for the refuted truncated C1' route.
It does not assert the displayed aggregate budget, C2'', B-WEAK, or the prize.
