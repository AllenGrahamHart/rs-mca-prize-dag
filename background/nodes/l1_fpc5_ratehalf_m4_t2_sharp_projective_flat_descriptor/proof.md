# Proof: sharp rate-half FPC5 projective-flat descriptor

## 1. The locator image is a vector flat

The guarded-slice theorem gives a vector space `V_FW` of dimension `ell-1`
and proves that the linear projection

```text
pi_F: V_FW -> K[X]_<=j
```

is injective. Its image `V_F` therefore has dimension `ell-1`, and `pi_F`
is an isomorphism from `V_FW` onto `V_F`. Projectivizing proves (FD1).

Let `lambda_j` be the coefficient-of-`X^j` functional on `V_F`. If it is
zero, no member of `V_F` has degree `j`, so there is no member of `D_j(C)`.
If it is nonzero, the fiber `lambda_j=1` is a nonempty affine hyperplane in
`V_F`. It has affine dimension `ell-2`. The ambient monic degree-`j` space
has affine dimension `j`; hence its codimension is

```text
j-(ell-2)=(2ell-3)-(ell-2)=ell-1.
```

This proves (FD2)--(FD3).

## 2. Projective split points are exact locator candidates

Every sharp-cell contributor has `F` monic of degree `j` with `j` distinct
roots in the source core `C`. It therefore lies in `A_F intersect D_j(C)`.
Conversely, every projective point in `P(V_F) intersect D_j(C)` has exactly
one monic representative, and that representative belongs to `A_F`. This
proves (FD4).

Because `pi_F` is an isomorphism, the monic representative determines one
and only one guarded numerator `W_F`. The core-defect normal form makes the
missed core exact precisely when `W_F` is nonzero at every root of `F`, which
is `gcd(F,W_F)=1`. Requiring no roots of `W_F-c_uF` on either untouched petal
is exactly the untouched-petal nonagreement guard. An exact `t=2` contributor
has a unique unordered touched pair; source-layout multiplicity is already
handled by the proved first-layout owner. Applying those filters gives (FD5)
and shows that no multiplicity is lost in the descriptor.

## 3. Divide the maximal common gcd

Choose any basis of `V_F` and let `G` be its monic polynomial gcd. A
polynomial is divisible by `G` if and only if every basis coordinate is, so
`G` is the maximal common divisor of the whole vector space and is independent
of the chosen basis.

If the split intersection is nonempty, choose `F_0 in D_j(C)` in it. Since
`G|F_0`, the monic polynomial `G` is squarefree and all its roots lie in `C`.
Division by `G` is a linear isomorphism from `V_F` to

```text
V_F'={F/G:F in V_F}.
```

Maximality of `G` gives `gcd(V_F')=1`, while linear isomorphism preserves the
vector and projective dimensions.

For any `F=GF'` in `V_F`, the polynomial `F` is monic, squarefree, degree
`j`, and split on `C` if and only if `F'` is monic, squarefree, degree `j-w`,
and split on `C\Z(G)`. Multiplication by `G` and division by `G` are inverse,
so they prove the bijection (FD7), not merely an upper-bound injection.

The monic degree-`j-w` ambient space has dimension `j-w`. Subtracting the
unchanged affine dimension `ell-2` gives reduced codimension

```text
(j-w)-(ell-2)=ell-1-w.
```

Nonnegative codimension also gives `w<=ell-1`. The numerator `W` and every
exact guard are reconstructed before a divided point is counted, so division
does not silently pay or discard those conditions. QED.
