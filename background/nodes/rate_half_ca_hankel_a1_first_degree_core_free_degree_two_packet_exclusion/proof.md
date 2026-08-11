# Proof

The bounded-divisor theorem and the packet ledger give, in both cases,

```text
O=Delta=2e-1,       sum_gamma c_gamma<=Delta.         (1)
```

For one supported fibre write

```text
Qbar_gamma=Q_min R_gamma,       deg R_gamma=c_gamma.
```

If `t_gamma` is the number of distinct new domain roots contributed by
`R_gamma` outside the squarefree roots of `Q_min`, then

```text
o_gamma=c_gamma-t_gamma.                              (2)
```

Summing `(2)` and using `(1)` forces

```text
sum c_gamma=Delta,       t_gamma=0 for every gamma.   (3)
```

Thus every distinguished incidence lies in `Q_min` as well as in the
excess factor.

Choose a distinguished row of deficit one; both packets have one. Its row
form has `e-1` distinct supported parameter roots. At such a root let `r`
be its multiplicity in `R_gamma`. By `(3)`, the horizontal intersection
multiplicity is

```text
m=1+r.                                                (4)
```

The local cancelled cube identity at the distinguished row gives

```text
m+n=0 mod 3,                                          (5)
```

where `n` is the positive vertical intersection multiplicity.

First suppose every incidence on the row has `r=1`. Then `(4),(5)` give
`n=1 mod 3` at all `e-1` supported points. Any unsupported vertical point
has `n=0 mod 3`. The total vertical degree is therefore

```text
e-1 mod 3,                                            (6)
```

but the row form has degree `e`. Since the official `e` is divisible by
three, `(6)` is impossible.

It remains to see whether a larger `r` can repair the congruence. In the
`I_0=1` packet, the factorization

```text
D_reg=P_1P_2L_0^2
```

already spends the full determinant degree, so every distinguished
incidence has `r=1` and the preceding contradiction applies.

In the `I_0=0` packet, only one determinant order remains after `P_1P_2`.
Hence at most one distinguished incidence can have `r=2`, and no larger
value is possible. At that point `(4),(5)` give `m=3` and `n>=3`; all other
`e-2` supported points have `n>=1`. Their minimum total vertical degree is

```text
(e-2)+3=e+1>e,                                        (7)
```

again impossible. If the remaining determinant order occurs elsewhere,
all incidences have `r=1` and `(6)` applies. This excludes both packets and
proves `(CFE1)`. QED.
