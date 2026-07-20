# Proof

For an unordered pair `{A,B}` put

```text
z=(A+B)^2/(AB).
```

The `c=2` source invariants from the dependency simplify to

```text
I_2=AB(z+12),
J_2^2=4(AB)^3z(z-36)^2.                             (1)
```

Indeed `A^2+B^2=AB(z-2)`, giving the first identity, while
`(A+B)^2=ABz` gives the second. The old invariant condition is therefore

```text
I^3J_2^2-I_2^3J^2=(AB)^3K_O(z)=0.                  (2)
```

All roots are nonzero, so the factor `(AB)^3` may be cancelled. Moreover,

```text
R_D(Z)=e_4^3 product_({A,B} subset Omega)(Z-z_(A,B)). (3)
```

Direct multiplication of the six factors in `(MTR2)`, followed by writing
the resulting symmetric polynomials in the elementary symmetric functions
of `Omega`, gives exactly `(MTR3)`. This also proves `(3)` without choosing
an ordering of the roots.

Equations `(2)--(3)` show that one of the six old candidates passes exactly
when `R_D` and `K_O` have a common root. This is equivalent to the resultant
condition `(MTR5)`. The binary-quartic discriminant is a nonzero scalar
multiple of `4I^3-J^2`; separability of `O` therefore proves that `K_O` has
degree three. The gcd and reconstruction assertions follow from `(3)` and
the reconstruction theorem in the dependency.

For `c=1`, retain one of the twelve choices in `(MTR6)` and choose `u` with
`u^2=P=BD`. The two source invariants are

```text
I_1=X-8Au,
J_1=2(A-u)(Y+16Au).                                  (4)
```

Reduce their required powers in the quadratic algebra `F[u]/(u^2-P)`.
First,

```text
(A-u)(Y+16Au)=E_0+uF_0,
J_1^2=J_even+uJ_odd.                                 (5)
```

Likewise direct expansion gives

```text
I_1^3=I_even+uI_odd.                                 (6)
```

The definitions in `(MTR6)` are precisely the even and odd coefficients in
`(5)--(6)`. Hence the old invariant test for this sign is

```text
I^3J_1^2-J^2I_1^3=K_0+uK_1.                         (7)
```

Its conjugate sign has value `K_0-uK_1`. Their quadratic norm is

```text
(K_0+uK_1)(K_0-uK_1)=K_0^2-PK_1^2=N_(A;B,D).       (8)
```

The roots of `D_*` are base-field squares, so both values of `u` lie in the
base field. Since a field has no zero divisors, `(8)` vanishes exactly when
one of the two old sign candidates passes. Choosing `A` and the unordered
pair `{B,D}` gives twelve choices and determines the unused root `C`, so
`(MTR7)` is equivalent to all 24 old tests. The dependency then reconstructs
the corresponding base-field PGL map. QED.

