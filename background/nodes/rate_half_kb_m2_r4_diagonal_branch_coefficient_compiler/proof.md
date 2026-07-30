# Proof

## 1. Even-odd source decomposition

In the source-line branch, the preceding dichotomy gives

```text
b(X)=-X,       W=X^2,
T^2X^4H(1/T,1/X)=epsilon H(T,X).                   (1)
```

Every polynomial of degree at most four in `X` has a unique even-odd
decomposition

```text
H(T,X)=U(T,X^2)+X V(T,X^2),                         (2)
```

where `U` has bidegree at most `(2,2)` and `V` has bidegree at most
`(2,1)`. Applying the source deck involution gives

```text
H(T,-X)=U(T,X^2)-X V(T,X^2).                        (3)
```

The parent fiber-resultant identity says that the endpoint pullback is,
up to a nonzero scalar, `H(T,X)H(T,-X)`. Equations `(2)--(3)` therefore
give `(KBDC-1)` after scaling the endpoint equation.

Substitute `(2)` into `(1)` and compare its even and odd parts. Since
`X^4=W^2` and `X^3=XW`, the two identities are exactly
`(KBDC-2)`.

The coefficient involution on `U` sends `(i,j)` to `(2-i,2-j)`. Its nine
positions have four two-element orbits and one fixed center, so its
positive and negative eigenspaces have dimensions five and four. The
involution on the six positions of `V` sends `(i,j)` to `(2-i,1-j)` and
has three two-element orbits, so both eigenspaces have dimension three.
Using the same sign in `(KBDC-2)` gives total dimensions

```text
5+3=8,       4+3=7.                                 (4)
```

Finally `(KBDC-2)` gives

```text
U(1/T,1/W)=epsilon T^(-2)W^(-2)U(T,W),
V(1/T,1/W)=epsilon T^(-2)W^(-1)V(T,W).
```

Substitution in `(KBDC-1)` proves `(KBDC-3)`; the sign disappears after
squaring. This also shows why the endpoint eigenvalue is positive in both
source eigenspaces.

## 2. The biquadratic resolvent

In the non-lifting branch, the preceding dichotomy proves that the degree-
four extension `E/F`, `F=K(W)`, is Galois with group `V4`. Let the four
roots of the monic separable endpoint quartic in a splitting field be
`z_1,z_2,z_3,z_4`. The three roots of the resolvent convention `(KBDC-4)`
are

```text
z_1z_2+z_3z_4,
z_1z_3+z_2z_4,
z_1z_4+z_2z_3.                                     (5)
```

The regular `V4` action on four letters fixes each of the three pair
partitions. Hence all three values in `(5)` belong to `F`, proving complete
splitting. They are distinct because equality of two values in `(5)`
would be a product of two root differences, contrary to separability.
Also `V4` is contained in `A4`, so the Vandermonde product is Galois-fixed
and `Disc(g)` is its square in `F`.

Conversely, suppose `g` is irreducible and separable and `(KBDC-4)` splits
over `F`. The Galois group fixes all three partitions of the four roots.
The kernel of the natural action `S4 -> S3` on these partitions is `V4`.
Thus the Galois group is a subgroup of `V4`. Irreducibility makes its action
transitive; the only transitive subgroup of this regular `V4` is `V4`
itself. This proves the equivalence.

All coefficients in `(KBDC-4)` lie in `K(W)`. Multiplying the three proposed
linear factors and clearing their common denominators converts the test to
polynomial identities in `K[W]`, with nonzero-denominator side conditions.
No numerical approximation or field enumeration is involved. QED.
