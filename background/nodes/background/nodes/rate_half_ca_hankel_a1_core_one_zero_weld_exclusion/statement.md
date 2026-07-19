# `A=1` core-one zero-weld exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary`

Work on the official core-one maximal-degree sharp cap and retain the notation
of the dependency. Thus

```text
e=2^38-1,       C_*=e-5b-1+D_*,                       (ZWE1)
```

where `C_*` is the total parameter-root deficit of the dominant component
over `D\S`.

The two-sided complement weld cannot have `K=0`. Indeed, the only profile
left by the dependency would have

```text
b=0,       D_*=1,       C_*=e,                         (ZWE2)
F(U,V)-G_0(X)=Q_*(U,V;X)V_0(U,V;X),                   (ZWE3)
```

where `F` is the squarefree product of the `4e` clean supported-slope
factors, while `G_0` is the squarefree product of all but exactly three
factors from `D\S`.

Every root `x` of `G_0` makes `Q_*(U,V;x)` a degree-`e` divisor of `F`, so
that domain row is saturated for `Q_*`. At each of the three omitted domain
points, `Q_*(gamma;x)` is nonzero at all `4e` clean supported slopes. It can
therefore have at most the one exceptional supported-slope root, and each
such row contributes at least `e-1` to `C_*`. Consequently

```text
C_* >= 3(e-1) > e=C_*,                                (ZWE4)
```

a contradiction. Hence

```text
K!=0                                                   (ZWE5)
```

for every profile on the official `A=1,s=1,e=2^38-1,ell=0` face.

This theorem closes the zero-weld branch only. It does not exclude the
remaining nonzero-weld (`K!=0`) coupled matrix factorization and does not close
`rate_half_band_closure`.
