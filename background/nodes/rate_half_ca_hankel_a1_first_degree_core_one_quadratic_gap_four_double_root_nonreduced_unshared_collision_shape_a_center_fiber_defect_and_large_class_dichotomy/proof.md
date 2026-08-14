# Proof

Write

```text
a=ell_alpha,       b=ell_beta,       c=ell_theta,
q_alpha=bc,        q_beta=ac,        q_theta=ab.  (1)
```

If `(f_alpha,f_beta,f_theta)` lies in `ker Phi`, evaluation at `alpha`
gives

```text
q_alpha(alpha)f_alpha(alpha)=0.                   (2)
```

The first factor is nonzero, so `f_alpha(alpha)=0`. The same argument at
the other centers proves

```text
im pi_gamma subset V_gamma.                      (3)
```

We also identify the coordinate kernel. For example, a syzygy with zero
`theta` coordinate has

```text
bc f_alpha+ac f_beta=0,
f_alpha=ah,       f_beta=-bh                     (4)
```

for one `h`. Since the distinct forms `a,b` span `S_1`, the third form
`c` is their linear combination. Hence `ah,bh in V` implies `ch in V`,
so `h` lies in the common inverse prolongation `J`. Conversely every
`h in J` gives `(4)`. Thus

```text
ker pi_gamma isomorphic to J                     (5)
```

for every center. The live syzygy theorem gives

```text
dim ker Phi=3r-(e+1),       dim J=2r-e.           (6)
```

Therefore every coordinate projection has rank `r-1`. The split-row root
description shows that evaluation at any center is nonzero on `V`: for
a classified row `x`, all roots of `G(-,x)` are off the center line.
Consequently `dim V_gamma=r-1`, and `(3)--(6)` prove `(CFD3)`.

For a small class, the locator-interpolation theorem gives
`rank T_gamma=r-1`, while the interpolation syzygy puts its image inside
`im pi_gamma`. Equation `(CFD3)` proves `(CFD4)`.

Minimality in `(CFD1)` makes `(CFD5)` an isomorphism. The transpose kernel
of `T_gamma` consists of the functionals on `V` annihilating its image.
By `(CFD4)` this annihilator is spanned by `ev_gamma`. Applying `iota`
gives `(CFD6)`.

At a small center the primitive locator has degree `d=3e-2`, and its
`U_0` roots are precisely the complement of `M_gamma`, also of size `d`.
This proves the first identity in `(CFD7)`. On `M_gamma`, the split-row
identity is

```text
Qbar(t,x)=eta_x^(-1)q_gamma(t)G(t,x)/L_U0'(x).   (7)
```

Evaluate `(7)` at `gamma` and use

```text
L_U0'(x)=L_Mgamma'(x)L_rest,gamma(x)             (8)
```

to obtain the second identity in `(CFD7)`.

For the large center, the complement has size `d-1` and the proved
center-deficit ledger identifies `x_*` as the unique padded locator root.
This gives `(CFD8)`. Repeating `(7)--(8)` gives

```text
G(gamma_0,x)=kappa_0 eta_x L_M0'(x)
                 L_rest,0(x)^2(x-x_*).           (9)
```

The matrix of `T_(gamma_0)` is

```text
E_B^T D E_n,
D_x=eta_x^(-1)/L_U0'(x)^2,                       (10)
```

on `n+3` points. Sylvester gives rank at least `r-2`; `(CFD3)` gives rank
at most `r-1`. Its defect space therefore has dimension one or two. The
center row is always in that defect space and, by `(9)--(10)`, corresponds
in the two-dimensional dual RS code to

```text
(x-x_*)/L_M0'(x).                                (11)
```

If the rank is `r-1`, this nonzero defect spans the kernel. If the rank is
`r-2`, evaluation on `M_(gamma_0)` identifies the two-dimensional defect
space with the complete dual RS code. Hence there is a nonzero `B_0 in
W_X` corresponding to

```text
1/L_M0'(x).                                      (12)
```

After scaling, `(11)--(12)` say

```text
G(gamma_0,x)=(x-x_*)B_0(x)       (x in M_(gamma_0)). (13)
```

The two sides have degree at most `n+1` and agree at `n+3` distinct
points. They agree as polynomials. Since the left side has degree at most
`n`, this also forces `deg B_0<=n-1`, proving `(CFD9)`.

Finally evaluate this identity at `X=x_*`. In the rank-`r-2` branch,
`G(gamma_0,x_*)=0`. The center-adjusted heavy-row theorem gives `(CFD10)`;
both `g_off` and `S_B` are nonzero at `gamma_0`, because the unique center
factor was removed from `g_off` and the collision parameter is not a
center. Hence `ell_(gamma_0)|T_3`. The residual has exact degree three,
so its quotient has exact degree two. This proves `(CFD11)`. QED.
