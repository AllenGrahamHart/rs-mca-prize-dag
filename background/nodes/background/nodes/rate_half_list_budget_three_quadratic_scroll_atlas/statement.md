# Budget-three quadratic scroll atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

The four quadratic chambers left by the linear Grassmann atlas are the three
pendant chambers and the quadratic `K_4-e` chamber. In every one, `b_01` is a
nonzero constant and `b_03` is exactly linear. Define

```text
r_0=(b_01,0,-b_12,-b_13),
r_1=(0,b_01,b_02,b_03).                               (QSA1)
```

There is a polynomial `h` of degree at most one such that

```text
U=r_0+h r_1=U_0+XU_1,
V=r_1      =V_0+XV_1                                 (QSA2)
```

have only affine-linear coordinates. If `deg b_13<=1`, take `h=0`. If
`deg b_13=2` (which occurs only in a pendant chamber), choose the linear
coefficient of `h` to cancel the quadratic term of `-b_13+h b_03`.

The edge bivector and block-locator vector then satisfy

```text
U wedge V=b_01 B(X),
A=alpha U+beta V,                                    (QSA3)

alpha=A_0/b_01,
beta=(A_1-hA_0)/b_01 in F[X].                        (QSA4)
```

Moreover `U_1 wedge V_1!=0`; hence every one of the four chambers is a
genuine balanced quadratic scroll in `Gr(2,4)`.

Put

```text
C=(U_0,U_1,V_0,V_1) in Mat_(4x4)(F).                 (QSA5)
```

There are exactly two algebraic subbranches:

1. If `rank C<4`, a nonzero base-field functional annihilates the four
   coefficient vectors and gives a nondegenerate constant relation among at
   least three of `A_0,A_1,A_2,A_3`.
2. If `rank C=4`, then

   ```text
   C^(-1)A=(alpha,X alpha,beta,X beta)^T.             (QSA6)
   ```

   Thus the full-rank chamber is the standard balanced-scroll module after
   one constant base-field change of locator coordinates.

The domain factorization is

```text
Lambda_D=E A_0A_1A_2A_3,                             (QSA7)
```

with exact `deg E=4` in every pendant chamber and `deg E=6` in the quadratic
`K_4-e` chamber.

Together with the linear Grassmann atlas, this classifies the bounded edge
geometry of all thirteen B*=3 chambers: nine split-unit lines and four
balanced scrolls, with the rank-deficient scrolls returning to the split-unit
class. It does not exclude the full-rank scroll or any split-unit equation.
