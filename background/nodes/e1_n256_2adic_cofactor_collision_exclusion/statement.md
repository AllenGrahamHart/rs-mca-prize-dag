# E1 N=256 2-adic cofactor exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `zeta` be a primitive `256`-th root and let

```text
alpha=F(zeta)=sum_(i=0)^127 c_i zeta^i
```

have one of the two first-surviving `N=256,s=5` folded profiles. Let
`bar F in F_2[X]` be the coefficientwise reduction and put

```text
mu=ord_(X=1)(bar F).
```

Then any collision at a pair-feasible row prime satisfies

```text
profile (3,4,0):  mu<=5,
profile (4,2,0):  mu<=16.
```

Only singleton coefficients survive modulo two. Consequently:

- in profile `(3,4,0)`, the polynomial formed by the four singleton
  exponents is not divisible by `(X+1)^6`;
- in profile `(4,2,0)`, if the singleton exponents are `r,s`, then
  `mu=2^v_2(r-s)`, so their separation is not divisible by `32`.

The proof uses the exact cofactor windows forced by
`|Norm(alpha)|<=S^64` and `p>2^250`. It is uniform over the live
prime intervals and requires no norm census. It does not exclude candidates
that pass these 2-adic tests.
