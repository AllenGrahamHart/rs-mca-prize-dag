# XR split-pencil dual-trade core

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_split_pencil_maxwell_core_extraction`

Let `G` be a Maxwell core from the preceding extraction, with blocks
`A_i`, distinct slopes `gamma_i`, and parity stack

```text
M_G=stack_i [H_i|-gamma_i H_i].
```

Every nonzero vector in the left kernel of `M_G` determines block words
`lambda_i`, not all zero, with

```text
supp(lambda_i) subset A_i,
sum_i lambda_i=0,
sum_i gamma_i lambda_i=0,                         (DT1)
```

and each nonzero `lambda_i` lies in the dual of cubic evaluation on `A_i`.
If `m_i=|A_i|=4+c_i`, then there is a polynomial `P_i` of degree `<c_i`
such that

```text
lambda_i(x)=P_i(x)/Lambda'_(A_i)(x),       x in A_i. (DT2)
```

Consequently every active block word has Hamming weight at least five.

For a coordinate `x`, put

```text
I_x={i:lambda_i(x)!=0}.
```

Every active coordinate has `|I_x|>=3`. More precisely, for
`t_x=|I_x|` there is a polynomial `Q_x` of degree `<t_x-2` such that

```text
lambda_i(x)=Q_x(gamma_i)
            / product_(j in I_x, j!=i)(gamma_i-gamma_j).   (DT3)
```

Thus every XR split-pencil counterexample contains a nonzero finite
dual-product-code trade whose active block degrees are at least five and
whose active coordinate degrees are at least three. It uses no more blocks
than the Maxwell bounds `308/359/640` in P-A or `256/299/480` in the P-B
one-loop branch.

This is an exact trade normal form. It does not bound or classify the trades
and does not promote either consumer.
