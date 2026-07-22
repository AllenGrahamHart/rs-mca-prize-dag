# Proof

The top `z`-coefficient in the pair-Lagrange formula is

```text
q_e=A/I(0)+B sum_k lambda_k A_k/[xi_k I'(xi_k)].      (1)
```

At a root of `D_k`, every term except the `k`th vanishes, proving
`(QLK1)--(QLK2)`.

Now fix `l` and a root `a` of `D_k` with `k!=l`. Evaluate `(QTK3)` at
`z=xi_l`. Every term with `i!=l` vanishes because `L_i(xi_l)=0`, while

```text
W_lk(xi_l)=L_l(xi_l)/(xi_l-xi_k)=1/(xi_l-xi_k).      (2)
```

Consequently

```text
V_a(xi_l)=
 -theta_l q_e(a)D_l(a)^2/(xi_l-xi_k)^2.              (3)
```

The exceptional boundary reconstruction gives

```text
Omega(xi_l;a)=q_e(a)^2V_a(xi_l)/C(a).                (4)
```

Substitute `(QLK2)` and `(3)` into `(4)`:

```text
Omega(xi_l;a)=
 -theta_l lambda_k^3
  r_k(a)^3D_l(a)^2/[C(a)(xi_l-xi_k)^2].              (5)
```

As `a` ranges over the roots of `A^(l)`, equations `(QLK3)` and `(5)` say

```text
Omega(xi_l;X)=-theta_l Y_l(X) mod A^(l).             (6)
```

Both `theta_l` and `C(a)` are nonzero. Also
`deg_X Omega<=4<2e-2=deg A^(l)` because `e>=4`. Hence the canonical
remainder in `(6)` has degree at most four, proving `(QLK5)`. Formula
`(QLK4)` is the subgroup derivative identity already proved in the CRT
dependency.

Every forbidden coefficient of `Y_l` is linear in the values
`lambda_k^3`. Collecting the coefficients of degrees `5` through `2e-3`
gives `(QLK6)--(QLK8)`. The vector `u` has no zero coordinate. Therefore
full rank excludes it; and, since the official field has `q>e`, the same
rank-deletion argument as `(QTK8)` shows that one coloop excludes every
torus vector. At `e=3`, `deg A^(l)=4`, so the strict degree comparison used
in `(6)` fails and there are no forbidden coefficients. QED.
