# Cycle 156: rate-half `A=1` separated double-heavy quotient cubic (2026-08-11)

In the double-root arm, assume `S_B` is squarefree and coprime to `g_*`,
and divide the primitive locator at its fixed heavy row:

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*).
```

The first moment is exactly `P_F(t,x_*)`. It vanishes on the supported
factor `g_*`; the contact divisor `R_*+2B`, compared with vertical contact
`R_*+3B`, forces two further correction copies. Hence

```text
P_F(t,x_*)=D_1(t)C_0(t),       deg C_0<=3.
```

The Hankel shift recurrence propagates the same factor through every moment:

```text
M(t)U(t)=D_1(t)C(t),
C_(i+1)=x_*C_i-kappa S_Bh_i,
deg C<=3.
```

Locally, `U` is a primitive new kernel direction at either correction root.
Its image is divisible by the full determinant valuation, so all that
valuation sits in one Smith invariant. Each separated correction has type
`[2]`, not `[1,1]`.

```text
result:                  PROVED separated cubic residual and type-[2] form
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer degree/tamper checks only
new assumptions:         none
```

The separated double-root locus is now reduced from an `e`-degree correction
problem to one cubic parameter-vector recurrence. Nonreduced `S_B` and
roots shared with `g_*` remain separate live cases. The next attack should
combine the cubic with the three-class source partition or prove an explicit
Hankel countermodel satisfying it.
