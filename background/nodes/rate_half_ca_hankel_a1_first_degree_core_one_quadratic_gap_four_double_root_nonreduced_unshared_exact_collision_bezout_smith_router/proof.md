# Proof

The residue characteristic is odd, so every ramification index two below
is tame.

The exact specialized multiplicity two and the unit leading coefficient
give a Hensel factorization of `Q` into the quadratic factor `(CBS1)` and
a factor which is a unit at `(tau,x_*)`. All Pade intersections over
`tau` lie on the correction divisor `B`, hence on this quadratic factor;
the complementary contact-algebra block is invertible.

Writing `P_F=b+ay+qR` and evaluating at `y=0` gives

```text
F_0=P_F(t,x_*)=b+c_0R(z,0).
```

The normalization/collision theorem gives `ord_z F_0=2`, while the local
quadratic argument below gives `ord_z c_0=6`. Consequently

```text
ord_z b=2.                                         (1)
```

Likewise `c_0`, up to a unit, is `Q(t,x_*)`, whose exact order is six.
The normalized branches have `ord_b(y)=3m_b`. In the two-unramified-branch
case each branch root has base order at least three. In the ramified
degree-two case, tame trace of an element of normalization order six has
base order at least three. Since `-c_1` is that trace, this proves

```text
ord_z c_0=6,       ord_z c_1>=3.                   (2)
```

By the Pade-Bezout contact-module theorem, the regular Hankel Smith
invariants equal those of multiplication by `p=b+ay` on

```text
R[y]/(y^2+c_1y+c_0),       R=F[[z]].               (3)
```

In the basis `(1,y)`, this multiplication has matrix

```text
T_p=[ b       -a c_0 ]
    [ a        b-a c_1].                           (4)
```

Now

```text
det T_p=b^2-a b c_1+a^2c_0.                       (5)
```

The three terms in `(5)` have respective orders `4`, at least `5`, and
at least `6`. Hence `ord_z det T_p=4`, with no possible cancellation.

If `a(0)` is nonzero, `(4)` has one unit invariant and one positive
invariant of exponent four. Its regular specialization has corank one and
positive Smith profile `[4]`. If `ord_z a=1`, the gcd of the entries of
`(4)` has order one. The two
Smith exponents therefore have sum four and minimum one, giving `[1,3]`.
If `ord_z a>=2`, every entry is divisible by `z^2`, while the entry `b`
has exact order two. The exponents are `[2,2]`. In either case `(4)` is
zero modulo `z`, so the regular corank is exactly two. This proves the
complete trichotomy `(CBS3)--(CBS5)`. QED.
