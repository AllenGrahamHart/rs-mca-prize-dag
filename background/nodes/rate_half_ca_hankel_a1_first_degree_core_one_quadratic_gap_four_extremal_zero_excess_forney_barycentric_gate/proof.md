# Proof

The Cycle-127 excess formula gives

```text
sum_(delta notin A)a_delta=e                         (1)
```

over `3e` off-line slopes. Since the excesses are nonnegative integers, at
least `2e` of them vanish.

Fix one zero-excess slope. The proof of the minimum-word reduction gives

```text
|S_delta intersect U_0|=p-3-r_delta.                (2)
```

Since `|S_delta|=rho-r_delta=2p-r_delta` and `s_0` belongs to both
`S_delta` and `U`, equations `(2)` and `(FBG1)` give

```text
|P_delta|
 =(2p-r_delta)-1-(p-3-r_delta)=p+2,                 (3)

|X_delta|
 =(3p-2)-(p-3-r_delta)=2p+1+r_delta.                (4)
```

This proves `(FBG2)`.

Let `c^L` be the endpoint codeword line and put

```text
g_delta=c_delta-c^L(delta).                         (5)
```

Cycle 127 says that `g_delta` is a nonzero minimum-weight RS codeword with
support

```text
W_delta=U union S_delta.                            (6)
```

For `x in X_delta`, the actual error at `delta` vanishes, while
`b(delta)=f_delta-c^L(delta)`. Hence

```text
b(delta)(x)=g_delta(x)!=0.                          (7)
```

Let `Omega_D(T)=product_(y in D)(T-y)`. The standard dual multipliers have
one common normalization `nu in F^x` such that

```text
v_x=nu/Omega_D'(x).                                 (8)
```

A minimum RS word supported on `W_delta` is a scalar multiple of the
locator of `D\W_delta`. Therefore, for one `lambda_delta!=0`,

```text
g_delta(x)
 =lambda_delta Omega_D'(x)/L_W,delta'(x)
                                      (x in W_delta). (9)
```

Using `(7)--(9)` in the contracted source formula gives, for `x in X_delta`,

```text
omega_x(delta)
 =(x-s_0)v_x b(delta)(x)
 =lambda_delta nu (x-s_0)/L_W,delta'(x).            (10)
```

The disjoint decomposition

```text
W_delta={s_0} disjoint_union I_delta
          disjoint_union X_delta disjoint_union P_delta              (11)
```

and `(FBG3)` imply

```text
L_W,delta'(x)
 =(x-s_0)L_X,delta'(x)q_delta(x).                   (12)
```

Substitute `(12)` into `(10)` and multiply by
`Q_delta=q_delta R_delta`. With
`kappa_delta=lambda_delta nu`, this is exactly `(FBG5)`.

Write `A_delta(T)=product_(x in I_delta)(T-x)`. Then

```text
q_delta=A_delta B_delta,
L_U0=A_delta L_X,delta.                             (13)
```

At a root `x` of `L_X,delta`, equation `(13)` gives

```text
L_U0'(x)=A_delta(x)L_X,delta'(x).                   (14)
```

All roots of `R_delta` are padded heavy rows outside the actual support and
outside `U`; hence `R_delta(x)!=0` on `X_delta`. Substitute `(13)--(14)`
into `(FBG5)` and cancel `A_delta(x)R_delta(x)` to obtain `(FBG6)`.
Equation `(FBG7)` is now immediate from `(ESP7)`; `delta notin A` ensures
`ell_gamma(delta)!=0`.

There is an independent Hankel check on the degree in `(FBG5)`. The full
locator equation `M(delta)Q_delta=0`, expressed through the fixed source on
`U_0`, says

```text
sum_(x in X_delta)
 omega_x(delta)Q_delta(x)x^j=0,       0<=j<=d.      (15)
```

The evaluation matrix in `(15)` has `d+1` rows and
`d+2+r_delta` columns. Its nullspace consists exactly of vectors

```text
(H(x)/L_X,delta'(x))_(x in X_delta),
deg H<=r_delta.                                     (16)
```

Thus the circuit calculation has precisely the allowed nullity and
identifies its numerator as the padded factor `R_delta`, up to the common
scalar. In particular, at `r_delta=0` the Hankel nullspace alone is
one-dimensional and forces the barycentric vector.

Finally, the total off-line deficit is

```text
sum_(delta notin A)r_delta=e-6-d_A.                 (17)
```

At most that many off-line slopes can have positive deficit. Removing them
from the at least `2e` zero-excess slopes leaves at least

```text
2e-(e-6-d_A)=e+6+d_A                               (18)
```

with `r_delta=0`. This proves `(FBG8)--(FBG10)`. QED.
