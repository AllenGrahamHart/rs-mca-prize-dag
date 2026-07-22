# Proof - L1 m=4, h=3, nu=2 prime-field Belyi normal form

The tangent-radical theorem gives

```text
deg rad(T)=3,       T/rad(T) proportional to V,
T'=2aX V.                                               (1)
```

Factor the monic tangent fiber as

```text
R-y_0=product_(i=1)^3 (X-r_i)^(e_i).                   (2)
```

The exponents are positive and sum to `p`. The derivative is nonzero, so no
single exponent can equal `p`; this proves `(PBN2)`.

The radical is proportional to

```text
P=X^2H-kappa.
```

Because `H` is linear, `P` has no `X` coefficient. Its nonzero roots
therefore satisfy

```text
1/r_1+1/r_2+1/r_3=0.                                  (3)
```

Also `R=X^2U`, so `R'(0)=0`, while `R(0)-y_0=-y_0!=0`. Taking the logarithmic
derivative of (2) at zero gives

```text
e_1/r_1+e_2/r_2+e_3/r_3=0.                            (4)
```

The rows `(1,1,1)` and `(e_1,e_2,e_3)` are independent over `F_p`. If the
three multiplicities were equal in `F_p`, their integer representatives in
`{1,...,p-1}` would be equal, while their sum `p` would give `3e_1=0` in
`F_p`, impossible because `p!=3` and `e_1!=0`.

Thus the common nullspace of (3)--(4) is one-dimensional. A cross product
shows

```text
(1/r_1,1/r_2,1/r_3)
 proportional to (e_2-e_3,e_3-e_1,e_1-e_2).            (5)
```

Every left coordinate is nonzero, so every difference on the right is
nonzero. The multiplicities are pairwise distinct, and (5) proves
`(PBN3)--(PBN4)`.

Now (2) becomes

```text
R(X)-y_0=lambda^p S_e(X/lambda).                       (6)
```

Evaluation at zero and `R(0)=0` give `(PBN6)--(PBN7)`. All coefficients of
`S_e` lie in `F_p` because its roots `t_i` and its integer exponents do.

Finally, (1) says that the only critical points are zero and the three
tangent roots, with orders one and `e_i-1`. Scaling (1) by `lambda` gives
`(PBN8)`. Both sides have degree `p-2`; the scalar `c_e` is nonzero because
the derivative is nonzero. This proves the stated critical-value passport.
