# Sub-k support data alone cannot price G3

- **status:** PROVED
- **role:** no-go theorem for the petal G3 attack

Let `L` be an `n`-point evaluation set over `F_q`, let `U:L->F_q`, and fix
`R subset L` of size `r<k`. Among polynomials of degree less than `k`, exactly

```text
q^(k-r)
```

agree with `U` on every point of `R`. At least

```text
q^(k-r) - (n-r)q^(k-r-1)
```

have agreement set exactly `R`.

Therefore canonicalizing only a sub-`k` agreement support cannot prove the G3
per-word multiplicity bound. A valid G3 datum or charging argument must carry
additional independent petal/cofactor constraints, or couple the remaining
freedom to another paid profile.

