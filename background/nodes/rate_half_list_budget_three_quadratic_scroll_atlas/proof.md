# Proof

The degree table gives the four chambers and shows in each that `b_01` is a
nonzero constant and `b_03` is exactly linear. The polynomial Plucker gate
proves

```text
b_01 A=A_0r_0+A_1r_1,
r_0 wedge r_1=b_01 B(X).                              (1)
```

If `b_13` has degree at most one, both rows in `(QSA1)` are already
affine-linear and we take `h=0`. The only remaining case is a pendant chamber
with `deg b_13=2`. Write `ell` for the leading coefficient of `b_03` and `q`
for that of `b_13`. Taking

```text
h=(q/ell)X
```

cancels the quadratic coefficient of `-b_13+h b_03`. The other possibly
changed coordinate is `-b_12+h b_02`. In a pendant chamber `b_02` is
constant and `b_12` is linear, so this coordinate is also affine-linear.
The first two coordinates are `b_01,hb_01`. This proves `(QSA2)` in every
quadratic chamber.

The determinant is invariant under adding a multiple of one row to the
other, so

```text
U wedge V=(r_0+h r_1) wedge r_1=r_0 wedge r_1=b_01B.
```

Rewriting `(1)` with `r_0=U-hV` and dividing by the nonzero constant `b_01`
gives `(QSA3)--(QSA4)`. No rational denominator remains.

At least one edge factor has exact degree two in each of the four chambers.
The quadratic coefficient of `U wedge V=b_01B` is `U_1 wedge V_1`, so it is
nonzero. This proves that `U_1,V_1` are independent and that the Grassmann
map has genuine degree two.

Now form the constant matrix `C`. If its rank is below four, choose a nonzero
row vector `lambda` with `lambda C=0`. Equation `(QSA3)` gives

```text
lambda A=0.
```

For `d>=3`, the four `A_i` are nonzero, pairwise coprime split locators with
nonempty disjoint root blocks. A relation cannot have support one. Support
two would make two locators proportional, which is impossible. Therefore the
relation has support at least three, and no proper subsum on that support can
vanish: a two-term subsum is impossible, while a three-term subsum in a
four-term relation would force the remaining nonzero term to vanish. This is
the stated nondegenerate split-unit subbranch.

If `C` is invertible, expand `(QSA3)` as

```text
A=alpha U_0+X alpha U_1+beta V_0+X beta V_1.
```

Multiplication by `C^(-1)` proves `(QSA6)`.

Finally, the pendant row has four edge points and no singleton or full point,
while `K_4-e` has five edge points and one full point. The normal-form
partition identity gives `(QSA7)` with exceptional degrees four and six.
QED.
