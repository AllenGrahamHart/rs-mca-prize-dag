# Proof

## 1. The incident continuation of the minimum-word scalar

Fix a zero-excess slope `delta`. The minimum-word circuit supplies

```text
g_delta=c_delta-c^L(delta)
```

and one nonzero scalar `kappa_delta=lambda_delta nu`. For an incidence
`x in I_delta`, the minimum-word formula is

```text
g_delta(x)=lambda_delta Omega_D'(x)/L_W,delta'(x),
v_x=nu/Omega_D'(x).                                (1)
```

The disjoint decomposition of the minimum-word support gives

```text
L_W,delta'(x)
 =(x-s_0)A_delta'(x)L_X,delta(x)B_delta(x),
L_U0'(x)=A_delta'(x)L_X,delta(x).                  (2)
```

Combining `(1)--(2)` proves the incident identity

```text
kappa_delta
 =(x-s_0)v_x g_delta(x)B_delta(x)L_U0'(x).         (3)
```

This is not the nonincidence Forney identity with `omega_x` substituted:
on the support,

```text
b(delta)(x)=e_delta(x)+g_delta(x),
e_delta(x)!=0.                                     (4)
```

## 2. Exact first-jet mismatch

At `x in I_delta`, `(PJT1)` and disjointness of the three fiber factors
give

```text
G_X/Q_X
 =zeta_delta/[chi_delta B_delta(x)]
 =kappa_delta/[Lambda(delta)B_delta(x)],           (5)
```

using the proved scalar relation
`zeta_delta=chi_delta kappa_delta/Lambda(delta)`.

The defining interpolation identity for the split biform is, at every
`x in U_0`,

```text
G(t,x)/L_U0'(x)=omega_x(t)Q(t,x)/Lambda(t).         (6)
```

The locator row has a simple root at the off-line slope `delta`, so
differentiating `(6)` in `t` gives

```text
G_t/Q_t=L_U0'(x)omega_x(delta)/Lambda(delta).       (7)
```

Substitute `omega_x(delta)=(x-s_0)v_x b(delta)(x)`, then use `(3)--(4)`
in `(5)--(7)`. This yields `(PJT4)`. Every factor on its right is nonzero:
`x!=s_0`, the dual multiplier and locator derivative are nonzero, `delta`
is off the center line, and `e_delta(x)` is nonzero by definition of the
actual support. The `t`-derivative of `Q` and both `X`-derivatives in
`(PJT1)` are nonzero, so the curves are smooth and their Jacobian is
nonzero. This proves `(PJT2)`.

## 3. Common factors can use only padding on selected fibers

Let `C` be as in `(PJT5)`. At a transverse common point, no common curve
component can pass through the point: if `Q=CQ_1` and `G=CG_1` there, the
smoothness of both curves makes `Q_1,G_1` nonzero and both gradients
proportional to `dC`, contradicting `(PJT2)`.

Fix a selected zero-excess slope at which the leading `X`-coefficient of
`C` does not vanish. The common roots of the two fibers in `(PJT1)` are
exactly the roots of `A_delta R_delta`. None of the `A_delta` roots can lie
on `C`, by transversality. Therefore every root of `C(delta,X)` is a root
of `R_delta`, and

```text
a<=r_delta.                                        (8)
```

The leading `X`-coefficient of `C` has parameter degree at most `b`, so
its degree can drop on at most `b` selected slopes. If `Z_0` is a selected
zero-excess set, summing `(8)` gives

```text
(|Z_0|-b)a<=sum_(delta in Z_0)r_delta.              (9)
```

There is no nonconstant parameter-only factor of `G`. Indeed, a root of
such a factor would be a root of every classified row of `G`. The row-root
dictionary makes it an off-line supported slope whose actual support
contains all classified rows and the fixed core point. In both profiles
this is more than `rho` support positions, impossible.

For the extremal profile, `|Z_0|=2e`, `b<=e-2`, and the total selected
padding is at most `e-6-d_A`. If `a>=1`, `(9)` would give

```text
e+2<=e-6-d_A,
```

a contradiction. Thus `a=0`, and the parameter-only argument gives
`b=0`. This proves `(PJT6)`.

For the strict profile, take `|Z_0|=p+2`, use `b<=e-1`, and bound the
selected padding by `e-6-r_A`. If `a>=2`, `(9)` gives

```text
e+5=2[p+2-(e-1)]<=e-6-r_A,
```

again impossible. A nonconstant gcd therefore has `a=1`; equation `(9)`
then gives

```text
b>=p+2-(e-6-r_A)=(e+15)/2+r_A.
```

Since also `b<=e-1`, this profile requires `r_A<=(e-17)/2`; above that
range the strict curves are coprime as well. This proves `(PJT7)` and
leaves only the printed `X`-linear profile.

Write this putative factor as

```text
C(t,X)=A(t)X+B(t),       deg_t C=b.                (10)
```

Its leading parameter coefficient is a nonzero polynomial in `X` of degree
at most one. Hence `C(t,x)` has exact parameter degree `b` on all but at
most one classified row. On every such row it divides `G(t,x)`, whose
roots are distinct off-line supported slopes, so it contributes `b`
distinct row-slope incidence pairs. There are `R=2p+r_A` classified rows,
giving at least

```text
b(R-1)                                              (11)
```

pairs. Conversely, for every one of the `3e+1` off-line supported slopes,
`C(delta,X)` is a nonzero polynomial of degree at most one. It is nonzero
because `G(delta,X)` is nonzero and `C|G`. Thus each slope contributes at
most one classified row, proving `(PJT8)`.

But `(PJT7)` and `R-1=3e-2+r_A` give

```text
b(R-1)>3e+1
```

already at the smallest allowed `e`; the official row is vastly beyond
that threshold. This contradiction removes the final common-factor
profile and proves `(PJT9)`. QED.
