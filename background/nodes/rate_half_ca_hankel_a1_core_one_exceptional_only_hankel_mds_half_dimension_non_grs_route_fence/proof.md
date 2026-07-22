# Proof

Let `G=[I_4|B]` with `B` from `(MHF1)`. Direct multiplication modulo `11`
gives

```text
BB^T=-I_4.                                           (1)
```

Thus `GG^T=0`; since `G` has rank four, its row code is Euclidean self-dual.
All `binom(8,4)=70` maximal minors of `G` are nonzero, so every four columns
are independent and the code is `[8,4,5]` MDS.

Use the quadratic monomial order

```text
x0^2,x0x1,x0x2,x0x3,x1^2,x1x2,x1x3,x2^2,x2x3,x3^2.
```

Evaluation on the eight projective columns of `G` has rank seven. Its
three-dimensional kernel has basis

```text
Q1=6x0x2+10x0x3+x1x2,
Q2=7x0x1+10x0x2+4x0x3+x1x3,
Q3=10x0x1+5x0x2+2x0x3+x2x3.                        (2)
```

The same rank is the Schur-square dimension.

It remains to exclude generalized Reed--Solomon form. A dimension-four GRS
generator has projective columns on a rational normal cubic in `P^3`. The
quadratic ideal of such a cubic has dimension three and has nonzero linear
syzygies; in standard coordinates these are the two Hilbert--Burch syzygies
among its three `2x2` catalecticant minors. Projective coordinate changes
preserve the dimension of the linear-syzygy space.

For the three quadrics in `(2)`, form the degree-three coefficient matrix of

```text
x0Q1,x1Q1,x2Q1,x3Q1,...,x0Q3,x1Q3,x2Q3,x3Q3.
```

It has rank twelve. With degree-three monomials in descending lexicographic
order, zero-based rows

```text
1,2,3,4,5,6,7,8,9,11,12,13
```

give a `12x12` minor of determinant `10 mod 11`. Hence `(2)` has no nonzero
linear syzygy, so the eight columns do not lie on a rational normal cubic.
The code is not GRS. QED.
