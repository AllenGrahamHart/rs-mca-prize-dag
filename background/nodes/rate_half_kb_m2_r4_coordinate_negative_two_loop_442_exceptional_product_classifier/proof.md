# Proof

Changing representatives of the three signed `J` pairs changes two of the
three cross-edge signs at a time.  Hence their product `tau` is the only
sign invariant, and representatives can be chosen as in `(KB4P-1)`.
Scaling all three representatives scales every edge product by one common
square, which is absorbed by postcomposing the Mobius product map.  This
justifies `A=1`.  Distinct nonzero signed pairs give `(KB4P-2)`.

Order the five rows by `A,B,AB,AC,BC` and use

```text
[-p,-pk,1,k].                                     (1)
```

The three label rows are

```text
H6:   (k_A,k_B,k_AB,k_AC,k_BC)=(l,-l^2,1,-l,l^2),
H8-L: (l,-l^2,1,-1,l^2),
H8-M: (-l^2,l,1,l^2,-1).                          (2)
```

Substitute `(KB4P-1)--(2)` into the five maximal minors of `(1)` and reduce
by `l^2-l+1` or `l^4+1`.  A lexicographic elimination in `(c,b,l)` has the
following decisive basis factors after removing the units protected by
`(KB4P-2)`:

```text
H6,-: 4b^2+b+4;
H6,+: 4b^2+7b+4;

H8-L,- and H8-M,-: b^2-b*l^3+b*l-b+1;
H8-L,+ and H8-M,+: b^2-2b*l^3+2b*l-b+1.          (3)
```

The next basis element is linear in `c`.  Reduction modulo `(3)` gives,
in the same row order,

```text
3c+2b-2,
c-2b-2,
c-(b-2)(l^3-l+1),
c+b*l^3-b*l-b-2,
c-(2b-1)(l^3-l+1),
c-2b+l^3-l-1.                                    (4)
```

These are exactly `(KB4P-3)--(KB4P-5)`.  The verifier reconstructs all five
determinants, derives the saturated decisive factors, and independently
reduces every determinant to zero modulo each printed row.  No numerical
root approximation or search is used.

Each equation in `(3)` is quadratic with nonzero constant term over the
geometric closure.  The accompanying linear equation determines `c`.
The exact symbolic guards show nondegenerate roots in characteristic zero,
so every one of the six rows is geometrically nonempty.  Special deployed-
field collisions, descent, q signs, and the seven unused fibers are not
settled by this calculation. QED.
