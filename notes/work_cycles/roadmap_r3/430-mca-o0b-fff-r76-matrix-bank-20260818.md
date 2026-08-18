## MCA O0b `FFF` `R76` rational-matrix bank (2026-08-18)

### Exact bank

The full regular multiplication matrix of

```text
R76 = Res_E(q7,q6)
```

in the certified 16-dimensional `q5` quotient is now retained entry by
entry over `GF(2130706433)(t)`:

```text
matrix size:                 16 x 16
nonzero entries:             256
distinct reduced denominators: 184
numerator-degree range:      1105..1387
denominator-degree range:     975..1256
```

The bank is Modal app `ap-MUI78JcsnhTmx76IIDm0mq`. Matrix-ledger SHA-256:
`24a8cc69a613bae3d367a087b524979de2bb8ec64174f97a2155c5227b7883f4`;
result SHA-256:
`701f4a255f2f573b4f50d7bbf3ea14b80ae8562ae09d93f96a8409cb45babbfb`.

### Determinant decomposition

For each column `j`, let `L_j` be the LCM of its sixteen reduced
denominators and define the polynomial column

```text
P_ij = numerator(M_ij) * L_j / denominator(M_ij).
```

Then

```text
det(P) = det(M_R76) * product_j L_j.
```

Thus, away from the explicit denominator roots, `det(P)` vanishes exactly
where the rational multiplication determinant vanishes. The next node should
bank the sixteen `L_j` and all 256 polynomial entries, verifying this identity
at `t=2`. A following node can take `det(P)` over the univariate polynomial
ring without any rational-function arithmetic.

### Proof boundary

This is an exact reusable algebra bank. It proves no new special fiber empty
by itself; the `FFF` chart remains open pending the polynomial determinant,
root extraction, and specialization replay.
