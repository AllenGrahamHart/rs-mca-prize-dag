# Q(zeta_128) J_63 Stickelberger relation

- **status:** PROVED
- **closure:** classical Jacobi-sum factorization plus an exact 32-row
  integer relation

Put `K=Q(zeta_128)`, let

```text
q_s=(257,zeta_128-9^s),                 s odd mod 128,
J_63=q_1 q_63,
I=J_63/bar(J_63)=q_1 q_63/(q_127 q_65),
ell=21121.
```

There is an explicit `alpha in K^x`, defined as a product of 32 Jacobi-sum
ratios, such that

```text
(alpha)=I^(2 ell).                                  (SR1)
```

All Jacobi factors and all integer exponents defining `alpha` are printed
in `proof.md` and independently replayed by `verify.py`.

## Falsifier

A prime-ideal valuation of `alpha` different from `(SR1)`.
