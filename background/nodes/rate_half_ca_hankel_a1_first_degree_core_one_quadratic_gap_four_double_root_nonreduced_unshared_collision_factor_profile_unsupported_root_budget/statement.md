# `A=1` nonreduced collision factor-profile unsupported-root budget

- **status:** PROVED
- **closure:** `4+d_A` exceptional heavy-row roots sharpen the factor trichotomy
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal split-biform factorization

```text
G(t,X)=c product_j Q_j(t,X),       bideg Q_j=(m_j,n_j),
M=e-2,       N=p-3,       R=3p-3+d_A,       T=3e,
q=9-2d_A.                                         (URB1)
```

Let `Gamma` be the `T` off-line supported slopes and `X_cls` the `R`
classified rows. For each factor put

```text
sigma_j=Tn_j-Rm_j.                                (URB2)
```

At the heavy row `x_*`, let `s_j` be the number of distinct roots of the
binary form `Q_j(t,x_*)` lying in `Gamma`, and set

```text
u_j=m_j-s_j.                                      (URB3)
```

Then

```text
s_j<=sigma_j,
u_j>=m_j-sigma_j,
sum_j u_j<=4+d_A.                                 (URB4)
```

For a large-odd factor and a huge-even factor respectively, `(URB4)`
sharpens the degree thresholds to

```text
large odd:       (q-2)m_j>=3e-8-2d_A,
huge even:       (q-2)m_j>=6e-8-2d_A.             (URB5)
```

Thus for `d_A=0`,

```text
large odd:       m_j>=least odd >=(3e-8)/7,
huge even:       m_j>=least even >=(6e-8)/7.      (URB6)
```

For `d_A=1`, profiles II and III of the exact factor trichotomy are
impossible. The only remaining profile is

```text
one large odd factor, no small odd, no huge even,  (URB7)
```

plus any number of ordinary-even factors, and its large factor obeys

```text
m_j>=least odd >=(3e-10)/5.                       (URB8)
```

On the official row `e=183251937963`, the center-adjusted thresholds are
unchanged after parity rounding:

```text
d_A=0: large odd >=78536544841,
       huge even >=157073089682;

d_A=1: large odd >=109951162777,
       huge-even threshold 219902325554>M,
       so only profile I survives.                (URB9)
```

## Scope

The theorem does not exclude profile I, nor profiles I--III when `d_A=0`.
Roots are counted projectively; an affine root at infinity is not lost.
