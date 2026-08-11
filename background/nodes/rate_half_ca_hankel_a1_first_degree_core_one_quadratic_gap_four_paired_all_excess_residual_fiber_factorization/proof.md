# Proof

Fix an off-line supported slope and write

```text
g_delta=c_delta-c^L(delta),
W_delta=U union S_delta.                            (1)
```

The codeword `g_delta` is nonzero because the only assigned centers on the
line `c^L` are the two endpoints in the strict profile and the three named
centers in the extremal profile. Its support is contained in `W_delta`,
whose size is

```text
|W_delta|=d_min+a_delta.                           (2)
```

Let `Omega_D(X)=product_(y in D)(X-y)`. The polynomial representing
`g_delta` vanishes on `D\W_delta`, a set of size `k-1-a_delta`. Therefore
there is a nonzero polynomial `H_delta` of degree at most `a_delta` such
that, for `x in W_delta`,

```text
g_delta(x)
 =Omega_D'(x)H_delta(x)/L_W,delta'(x).             (3)
```

This proves `(AEF3)`.

For `x in X_delta`, the actual error `e_delta=f-c_delta` vanishes, so

```text
b(delta)(x)=f(x)-c^L(delta)(x)=g_delta(x).          (4)
```

Write the standard dual multiplier as

```text
v_x=nu/Omega_D'(x),       nu!=0.                   (5)
```

The disjoint decomposition

```text
W_delta={s_0} disjoint_union I_delta
          disjoint_union X_delta disjoint_union P_delta             (6)
```

gives, at `x in X_delta`,

```text
L_W,delta'(x)
 =(x-s_0)L_X,delta'(x)A_delta(x)B_delta(x).         (7)
```

Since the actual residual locator is `q_delta=A_delta B_delta`, equations
`(3)--(7)` and the contracted source definition give

```text
omega_x(delta)Q_delta(x)L_X,delta'(x)
 =nu H_delta(x)R_delta(x).                         (8)
```

Specialize the homogeneous locator by

```text
Qbar(delta,X)=chi_delta Q_delta(X),       chi_delta!=0.             (9)
```

The split-biform interpolation identity and
`L_U0'(x)=A_delta(x)L_X,delta'(x)` now turn `(8)` into

```text
G(delta,x)
 =[chi_delta nu/Lambda(delta)]
   A_delta(x)H_delta(x)R_delta(x)                  (10)
```

for every `x in X_delta`. Both sides vanish on `I_delta`. The union-size
identity gives `(AEF2)`, so the right side of `(10)` has degree at most

```text
(n-a_delta-r_delta)+a_delta+r_delta=n.             (11)
```

The left side also has degree at most `n`, and `n<|U_0|`. Agreement on all
of `U_0` proves the second identity in `(AEF4)` with

```text
zeta_delta=chi_delta nu/Lambda(delta)!=0.          (12)
```

Degree additivity among nonzero polynomial factors proves `(AEF5)`.

Fix `x in P_delta=S_delta\U`. Since `x` lies outside both endpoint error
supports,

```text
c_alpha(x)=c_beta(x)=f(x).
```

The codeword line through the endpoints is therefore constant with value
`f(x)` at this coordinate, and

```text
g_delta(x)=c_delta(x)-c^L(delta)(x)
          =c_delta(x)-f(x)=-e_delta(x)!=0.         (12a)
```

Equation `(3)` then gives `H_delta(x)!=0`. Thus `H_delta` has no root in
the root set of `B_delta`, proving `gcd(B_delta,H_delta)=1`. The full
locator factors in the first line of `(AEF4)`; its actual-support and
padded root sets are pairwise disjoint. Taking the polynomial gcd now
proves `(AEF6)`.

It remains to compute the first jet. Fix `x in I_delta`. Equations `(3)`
and `(6)` at an incidence give

```text
nu H_delta(x)
 =(x-s_0)v_x g_delta(x)B_delta(x)L_U0'(x).         (13)
```

The vertical factorizations `(AEF4)` imply

```text
G_X/Q_X
 =nu H_delta(x)/[Lambda(delta)B_delta(x)].         (14)
```

Differentiating the row interpolation identity at the simple locator root
gives

```text
G_t/Q_t=L_U0'(x)omega_x(delta)/Lambda(delta).       (15)
```

Finally

```text
omega_x(delta)=(x-s_0)v_x[e_delta(x)+g_delta(x)].  (16)
```

Substitution of `(13)--(16)` proves `(AEF7)`. Its right side is nonzero,
so the Jacobian determinant is nonzero and both curves meet transversely.
QED.
