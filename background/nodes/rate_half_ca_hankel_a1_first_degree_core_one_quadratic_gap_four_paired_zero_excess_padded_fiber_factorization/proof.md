# Proof

Fix a zero-excess slope. In either profile, write

```text
P_delta=S_delta\U,
X_delta=U_0\I_delta,
B_delta(X)=product_(x in P_delta)(X-x).             (1)
```

The actual residual locator and its padded completion are

```text
q_delta=A_delta B_delta,
Q_delta=A_delta B_delta R_delta.                    (2)
```

All padded-heavy roots lie outside the actual support and outside the light
set `U_0`, so `A_delta` and `R_delta` are coprime.

## The minimum-word circuit

At the extremal boundary, the existing Forney-barycentric gate proves

```text
omega_x(delta)Q_delta(x)L_X,delta'(x)
 =kappa_delta R_delta(x),       x in X_delta,       (3)
```

for one `kappa_delta!=0`.

The same identity holds at the strict boundary. Indeed, zero excess gives

```text
|I_delta|=p-2-r_delta,
|P_delta|=p+1,
|X_delta|=2p+1+r_delta.                             (4)
```

The center difference `g_delta` is a nonzero minimum RS word supported on
`W_delta=U union S_delta`. With
`Omega_D(Y)=product_(z in D)(Y-z)`, the standard dual multipliers have one
normalization `v_x=nu/Omega_D'(x)`, and for one nonzero `lambda_delta`,

```text
g_delta(x)=lambda_delta Omega_D'(x)/L_W,delta'(x)
                                      (x in W_delta). (5)
```

For `x in X_delta`, the actual error at `delta` vanishes, so the contracted
source formula and the disjoint decomposition

```text
W_delta={s_0} disjoint_union I_delta
          disjoint_union X_delta disjoint_union P_delta              (6)
```

give

```text
omega_x(delta)
 =lambda_delta nu/(L_X,delta'(x)q_delta(x)).        (7)
```

Multiplying `(7)` by `Q_delta=q_delta R_delta` proves `(3)` in the strict
profile as well, with `kappa_delta=lambda_delta nu`.

## Specializing the biform

Let `Lambda(t)` be the product of the three center-line factors in the
extremal profile and of the two endpoint factors in the strict profile. By
construction of the homogeneous full locator, for one `chi_delta!=0`,

```text
Qbar(delta;X)=chi_delta Q_delta(X).                 (8)
```

The dual-MDS biform satisfies

```text
G(delta,x)/L_U0'(x)
 =omega_x(delta)Qbar(delta;x)/Lambda(delta).        (9)
```

For `x in X_delta`, the identity

```text
L_U0'(x)=A_delta(x)L_X,delta'(x)                   (10)
```

together with `(3)`, `(8)`, and `(9)` yields

```text
G(delta,x)
 =[chi_delta kappa_delta/Lambda(delta)]
   A_delta(x)R_delta(x).                            (11)
```

For `x in I_delta`, both sides of `(11)` vanish. Hence they agree at every
point of `U_0`. In the extremal profile both have degree at most `p-3`; in
the strict profile both have degree at most `p-2`. These bounds are smaller
than `|U_0|`, so polynomial interpolation proves `(PZF2)` with

```text
zeta_delta=chi_delta kappa_delta/Lambda(delta)!=0. (12)
```

The degree identities follow from

```text
extremal: deg A_delta+deg R_delta=p-3,
strict:   deg A_delta+deg R_delta=p-2.              (13)
```

The extremal minimum-word reduction supplies at least `2e` zero-excess
slopes, and the strict reduction supplies at least `p+2`. This proves
`(PZF3)--(PZF5)`. QED.
