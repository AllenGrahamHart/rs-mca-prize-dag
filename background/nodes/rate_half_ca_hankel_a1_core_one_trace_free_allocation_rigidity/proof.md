# Proof

## 1. The norm residual

At a residual domain row `x`, divide `q_x=Q(U,V;x)` by one copy of every
distinct supported-slope factor. For a nonsaturated row this quotient is
exactly

```text
N_x=Qhat_x/E_Z^epsilon_x,
```

and has degree `delta_x=e_*-v_x`. At a saturated row the corresponding
quotient is a nonzero scalar.

Multiply these factorizations over all rows of `D\S`. Every clean supported
slope occurs in exactly `r` distinct rows. If `D_*=1`, the exceptional slope
occurs in exactly `r-1` distinct rows, and the correction factor `J_*` in the
component norm identity contributes its one missing copy. Therefore

```text
J_* product_(x in D\S)q_x
 =P^r product_(x:B_X(x)=0)N_x                         (1)
```

up to a nonzero scalar. Comparison with the proved exact identity
`J_*R_*=P^rS_*` gives `(TFA2)`.

## 2. A trace-free bad domain row

Assume every defect trace vanishes. The previous theorem gives

```text
K_x=-H_xJ_x=0.                                        (2)
```

If `H_x=0`, its local formulas give `A_x=B_x=0`, so the factor `X-x` divides
both global biforms `A,B`.

Otherwise `J_x=0`. The remaining local relation is

```text
Phat_x E_Z=Qhat_x V_x.                                (3)
```

Since `Phat_x,Qhat_x` are coprime, `Qhat_x` divides `E_Z`. If `D_*=0`, this
contradicts the positive degree `deg Qhat_x=delta_x+epsilon_x>=1`. If
`D_*=1`, divisibility by `E_Z` says that the exceptional supported slope is
a root of `q_x`, so `epsilon_x=1`. It then gives

```text
deg Qhat_x=delta_x+1>=2>deg E_Z,                       (4)
```

again a contradiction. Therefore `J_x=0` is impossible, every bad row has
`H_x=0`, and the full product `B_X` divides both `A,B`. This proves `(TFA3)`.

## 3. The trace-free exceptional slope

Assume `D_*=1`. At `gamma_0`, the previous theorem gives

```text
K_0=-H_0J_0=0.                                        (5)
```

If `H_0=0`, then `V_0=W_0=0`, so `E_Z` divides both `V,W`; this is the `Z_W`
allocation. Otherwise `J_0=0`, so `B_0=0` and `E_Z` divides `B`. The remaining
exceptional relation becomes

```text
Qhat_0 A_0=Phat_0 B_X.                                (6)
```

Coprimality gives `Qhat_0|B_X` and `Phat_0|A_0`. Since `R_0|P_X`, equation
`(6)` makes `q_0=R_0Qhat_0` a divisor of the squarefree polynomial
`G_X=P_XB_X`. It is therefore squarefree and all its roots lie in `D\S`.
The exceptional fiber already has exactly `r-1` distinct such roots, so its
degree is `r-1`. This proves `(TFA5)`.

## 4. The reduced complement square

The divisibilities just proved give `(TFA6)`. Substitute them into the two
original complement identities

```text
QV+P_XW=P_clE_Z,       QA+P_clB=P_XB_X.
```

Cancel `Z_W` in the first and `B_X` in the second to obtain the first two
equations in `(TFA7)`. The trace-descent theorem already gives
`W_1B_1-1=QK_1` after the same allocations, and proves `K_1!=0`. Thus no
other allocation branch remains. QED.
