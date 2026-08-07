# Exact locator-prefix consumer and null-fiber scope

- **status:** PROVED
- **closure:** proof

Let `D` be a finite evaluation domain, let `A=K+t`, and for each
`A`-subset `S` write

```text
Q_S(X)=prod_(x in S)(X-x)
      =X^A+c_1(S)X^(A-1)+...+c_A(S).
```

Define the depth-`t` locator-prefix map

```text
Phi_(A,t)(S)=(c_1(S),...,c_t(S)).
```

For every prefix `z`, the polynomial word

```text
U_z(X)=X^A+z_1 X^(A-1)+...+z_t X^(A-t)
```

has exactly `|Phi_(A,t)^-1(z)|` codewords of degree `<K` agreeing on
`A` points. Hence a worst-word exact-list ledger must control the heaviest
relevant prefix fiber after its declared first-match payments.

The historical `t`-null object is not that maximum:

1. in characteristic `p`, `t`-nullity fixes only the prefix coordinates
   whose indices are not divisible by `p`; and
2. even below characteristic, the raw null fiber need not be heaviest. For
   `D=F_17^*`, `A=9`, and `t=1`, its size is `672`, whereas every nonzero
   prefix fiber has size `673`.

Therefore a null-fiber census can supply the exact-list consumer only after a
separate strip-aware max-to-null or exchange-compression theorem is proved.
