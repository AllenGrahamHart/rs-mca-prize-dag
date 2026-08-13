# Proof

The formal Padé resultant is

```text
Res_X^(d,d-1)(Qbar,P_F)=c_F a^(2d+1)D_1,          (1)
```

where `a=lc_X Qbar`. At the large center, `(PCT1)` makes
`a(gamma_0)=chi_0!=0`. The exact regular factor is

```text
D_1=c_D g_*S_B^2.                                (2)
```

The center-deficit ledger says `gamma_0` is a simple root of the
squarefree form `g_*`, while the unshared collision parameter is not a
center, so `S_B(gamma_0)!=0`. Equations `(1)--(2)` therefore give

```text
ord_(gamma_0) Res_X(Qbar,P_F)=1.                 (3)
```

Equation `(PCT1)` exhibits the common point `(gamma_0,x_*)`. Every local
intersection multiplicity is positive, and their sum over the fiber is
the resultant order in `(3)`. Thus this point is the only common point
over `gamma_0` and its local intersection multiplicity is exactly one.
In particular both specialized roots are simple, so

```text
C_0(x_*)!=0.                                     (4)
```

Specialize the Pade identity

```text
Qbar B_src-Lambda G=L_U0 P_F                    (5)
```

at `gamma_0`, differentiate in `X`, and evaluate at `x_*`. Since
`Lambda(gamma_0)=0` and both `Qbar` and `P_F` vanish there,

```text
Qbar_X(gamma_0,x_*)B_src(gamma_0,x_*)
 =L_U0(x_*)P_(F,X)(gamma_0,x_*).                 (6)
```

All three factors other than `B_src` are nonzero: `x_* notin U_0`,
`Qbar_X=chi_0L_rest,0(x_*)`, and `(4)` gives
`P_(F,X)=chi_0C_0(x_*)`. This proves the second assertion in `(PCT2)`.

At a small center, `D_1` is nonzero because the sole center root of
`g_*` is `gamma_0` and `S_B` has no center root. The leading locator
coefficient is again nonzero. Equation `(1)` therefore makes the
specialized resultant nonzero, proving coprimality. QED.
