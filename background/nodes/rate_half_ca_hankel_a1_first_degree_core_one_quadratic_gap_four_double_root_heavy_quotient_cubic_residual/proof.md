# Proof

The definition of `P_F` and `(HQC2)` give directly

```text
P_F(t,x_*)
 =sum_x omega_x(t)[Q(t,x_*)-Q(t,x)]/(x_*-x)
 =sum_x omega_x(t)U(t,x)
 =F_0(t).                                           (1)
```

We first prove `D_1|F_0`. At a root `gamma` of the squarefree supported
factor `g_*`, the specialized factorization is

```text
Q_gamma=(X-x_*)U_gamma,                             (2)
```

where `U_gamma` is the minimal locator of the contracted actual source.
Thus `U_gamma in ker M_gamma`, and every `F_i(gamma)` vanishes. In
particular `g_*|F_0`.

Now work at either point of the correction divisor `B`. Condition `(HQC0)`
makes these two points project to distinct simple parameter values, disjoint
from `R_*`. The proved divisor
identities on the normalized curve are

```text
div_C(X-x_*)=R_*+3B,
div_C(s_F)=R_*+2B.                                  (3)
```

The restriction of `P_F` differs from `s_F` only by the fixed domain-
infinity contact, which is a unit at the finite heavy row. Along `B`, it
therefore vanishes to order two, while replacing the moving curve point by
the fixed value `x_*` changes `P_F` only by a multiple of `X-x_*`, of order
three. Hence the first two correction jets are unchanged and

```text
S_B^2|P_F(t,x_*)=F_0(t).                            (4)
```

Thus `S_B^2|F_0`. Since `(HQC0)` also gives
`gcd(g_*,S_B)=1`, combining `(1)--(4)` with `(HQC1)` proves

```text
F_0=D_1C_0                                           (5)
```

for a parameter form `C_0`. Since the source weights are parameter-linear
and `U` has parameter degree at most `e`, `deg F_0<=e+1`. As
`deg D_1=e-2`, one has `deg C_0<=3`. This proves `(HQC6)`.

Apply the kernel recurrence to `(HQC2)`. For `0<=i<d`,

```text
0=Phi_t(X^iQ)
 =Q(t,x_*)h_i+F_(i+1)-x_*F_i.                      (6)
```

Insert `(HQC1)` and `(5)` into `(6)`. Because
`Q(t,x_*)/D_1=kappa S_B`, induction gives

```text
F_i=D_1C_i,
C_(i+1)=x_*C_i-kappa S_Bh_i.                       (7)
```

Every term on the right of the second identity has parameter degree at
most three, proving `(HQC4),(HQC5)`. The entries of `M(t)u(t)` are exactly
the `F_i`, so `(HQC7)` follows.

Evaluate the Pade syzygy

```text
QB-Lambda G=L_U0P_F                                (8)
```

at `X=x_*`, substitute `(HQC1),(HQC6)`, and rearrange. This is `(HQC8)`.

It remains to identify the local Smith type. Let `z` be a uniformizer at
either simple root `tau` of `S_B`. Condition `(HQC0)` and `(HQC1)` give

```text
ord_tau(D_1)=2.                                     (9)
```

At `tau`, `Q(tau,x_*)=0` and

```text
Q_tau=(X-x_*)U_tau.                                (10)
```

The two coefficient vectors in `(10)` are nonzero and independent.
Therefore the class of `u` in the regular quotient by the primitive kernel
is nonzero modulo `z`. Equation `(HQC7)` says that the regular block sends
this primitive class into `z^2` times the local lattice. At least one Smith
exponent is therefore at least two. Their sum is the determinant valuation
two from `(9)`, so there is exactly one positive exponent and it equals two.
This proves `(HQC9)`. QED.
