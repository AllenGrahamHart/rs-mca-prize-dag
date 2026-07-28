# Proof - L1 Mersenne HNF order-one full-trace cancellation

The Frobenius gate gives `d_star=zeta/d`, `zeta^m=1`, and the two known roots
in (FTC2). Every official `m` is even. Hence, for `j>=1`,

```text
(x_0^star)^(mj)
  =(-d/zeta)^(mj)
  =d^(mj) zeta^(-mj)
  =d^(mj),                                             (1)

x_0^(-mj)=(-d)^(mj)=d^(mj).                           (2)
```

This proves (FTC3). No choice of an `m`th root is involved: `x_0` and
`x_0^star` are the printed roots themselves.

Write the reduced traces from (NRR1) as `P_j^star` and `P_j^-`. Equations
(FTC3)--(FTC4) give

```text
T_j^star-T_j^-=P_j^star-P_j^-                         (3)
```

for every `j>=1`. Thus equality of the two full traces is equivalent to
equality of the corresponding reduced traces.

Newton's identities are triangular. Since every integer `1,...,H` is
invertible on the official rows, the first `r` equalities of elementary
symmetric functions are equivalent to equality of the first `r` power sums:
at step `j`, all lower terms already agree and the coefficient of the new
power sum is `(-1)^(j-1)`. The Newton reciprocal reduction identifies those
elementary-symmetric equalities with the first `r` reduced reciprocal
coefficient equations. Combining that identification with (3) proves
(FTC5).

The roots contributing to `T_j^star` are all roots of the original monic
polynomial `P_(rho_star,c_star)`. The roots contributing to `T_j^-` are the
roots of the monic reciprocal of `P_(rho,c)`. Ordinary Newton recurrence
therefore constructs both sides directly, through the powers in (FTC6),
without dividing by `W-x_0` or forming an `m`th-power resultant. QED.
