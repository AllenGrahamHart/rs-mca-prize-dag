# Paper D v13.2 discrete subfield-census guard

- **status:** PROVED
- **closure:** proof
- **source:** Paper D v13.2, `prop:capg-census-floor`

Let `C=RS[F,D,K]` with `D subseteq B`, `|D|=n`, and `p=|B|`. Fix
`K<=m` with `2(m-K)<=n-K`, put `w'=m-K`, and take

```text
w'+1 <= d1 <= floor((n-K+1)/2),
m'=K-1+d1,    m'+d1<=n.
```

In the identity-prefix census of Paper D v13.2, put

```text
A_B(d1) = C(n,m') |B|^-(d1-1),    m'=K-1+d1.
```

Under the proposition's support-lift contract, the exact pigeonhole
lower floor and the soft mean-plus-one upper model are

```text
M_B^disc(d1) = C(m',m) ceil(A_B(d1)),
M_B^soft(d1) = C(m',m) (1+A_B(d1)).
```

The ceiling is taken before multiplying by the support count. In
particular, when `0<A_B<1`, the discrete floor is `C(m',m)`, not the
ceiling of the raw product `C(m',m)A_B` and not zero.

At the deployed KoalaBear and Mersenne-31 list rows, offsets zero through
three give the corrected bit floors

```text
KoalaBear:   67.0958  56.0111  43.9348  57.6849
Mersenne-31: 52.1129  41.0169  39.1799  57.6848.
```

This is a finite-ledger guardrail. It does not prove the residual
safe-side balanced-core, quotient-flatness, or shift-pair bounds.
