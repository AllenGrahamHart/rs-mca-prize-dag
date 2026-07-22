# Proof

The ambient coefficient space represents polynomials of degree at most
`r=2e+1`. A polynomial in that box vanishes on all `2e` roots of the
squarefree degree-`2e` locator `A` exactly when it is a scalar multiple of
`A` or `XA`. Therefore

```text
ker ev_(R_A)=span{q_0,v}.                             (1)
```

The rank-one flag theorem gives

```text
W_q intersect ker ev=span{q_0},
H_q intersect ker ev=span{q_0,v}.                    (2)
```

Together with `dim W_q=e+1` and `dim H_q=e+2`, this proves both equalities
in `(HSD2)` and `dim C_q=e`.

The finite source representation `(HSD1)` turns the `M_0` Hankel pairing
into the weighted evaluation pairing:

```text
x^TM_0y=sum_(a in R_A)beta_a X(a)Y(a).               (3)
```

The coefficient plane is `M_0`-isotropic, so `(3)` makes `C_q`
`beta`-isotropic. Every `beta_a` is nonzero, hence `(HSD4)` is nondegenerate
on a space of dimension `2e`. An isotropic subspace of dimension `e` equals
its orthogonal complement, proving `(HSD3)`.

For `(HSD5)`, suppose first that `Delta_I!=0`. Left-normalize the rows of
`G` and order the columns as `(I,J)`, obtaining

```text
G=[I_e | B].                                         (4)
```

With `D_I,D_J` the diagonal weight matrices, self-orthogonality says

```text
D_I+B D_J B^T=0.                                    (5)
```

Take determinants:

```text
det(B)^2 det(D_J)=(-1)^e det(D_I).                  (6)
```

Since row normalization divides both complementary minors by the same
nonzero factor, `(6)` is exactly `(HSD5)`. It also makes `Delta_J` nonzero.
The same argument with `I,J` exchanged covers the case starting from
`Delta_J!=0`; if both vanish, `(HSD5)` is immediate. QED.
