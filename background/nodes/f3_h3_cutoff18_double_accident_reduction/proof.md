# Proof

For every nonnegative integer `r`,

```text
r = 1_(r>0)+max(r-1,0).                  (1)
```

Multiplying `(1)` by `Q_18(t)` and summing over `t!=1` proves `(DA1)`.

Since `Q_18(t)<=P(t)`,

```text
A_18
 <= sum_(t!=1,R(t)>0) P(t)
 <= sum_t P(t)
 = |A|^2
 = (n-1)^2,
```

which is `(DA2)`. Therefore

```text
17X_18 <= 17(n-1)^2+17Y_18.              (2)
```

The exact remaining allowance after paying the first term is

```text
300n^2-17(n-1)^2
 =283n^2+34n-17.
```

Substituting `(DA3)` into `(2)` proves `(DA5)`. If `(DA4)` holds, then

```text
17X_18
 <=17(n-1)^2+272n^2
 =289n^2-34n+17
 <=300n^2
```

for every `n>=1`, so `(DA4)` also suffices.

Finally, the proved dyadic shifted-product Sidon theorem says that a
nonidentity quotient has at most one representation in characteristic zero.
Hence `max(R(t)-1,0)>0` records an additional finite-characteristic quotient
collision. The condition `Q_18(t)>0` forces a product fiber far beyond its
characteristic-zero multiplicity at most two. Every positive summand of
`Y_18` is therefore a simultaneous, or double, accident. QED.
