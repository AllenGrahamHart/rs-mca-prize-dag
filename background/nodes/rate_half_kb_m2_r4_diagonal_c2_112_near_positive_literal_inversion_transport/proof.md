# Proof

Let `v0=2`, `v1=1/2`, `v2=b`, and `v3=1/b`, and use the twelve source-edge
pairs printed in the exact literal registry. For a selected pair, its common
vertex and two remaining vertices determine the internal-star target. The
positive reciprocal source space is then reconstructed by the five linear
conditions supplied by the two `q`-membership rows at `w=1/c` and the three
internal-star rows. The internal-star reconstruction theorem makes this
solution unique.

The independent audit forms this `5 x 5` matrix over `QQ(b,c,d)` and invokes
`solve_right`; it does not import the upstream explicit inverse. It then
divides `U(T,r)^2-WV(T,r)^2` by `(W-w)^2` at `r=c,d`, obtaining the two
quadratic residuals. For every one of the twelve assignments it verifies
directly that applying either substitution in `(KBNI-1)` gives a projective
multiple of the residuals for the assignment in `(KBNI-2)`.

There are four oriented target roots and three allocations. Direct
coefficient comparison verifies the target action

```text
B:  A->A, TA->TA, OB<->OI,
TW: A<->TA, OB->OB, OI->OI.
```

For each reconstructed system the audit factors every numerator and
denominator contributing to the radical reconstruction/q-slice named open.
After removing powers of the invertible coordinates `b,c,d`, the transformed
factor set equals the destination factor set. Thus neither substitution
silently crosses an omitted affine component.

This gives `2*12*12=288` exact transport checks. A second implementation
patches only the entrypoint of the exact PR #1140 source compiler and obtains
the same assignment maps, target maps, localizer maps, and empty failure
lists. The independent reconstruction and the imported-formula replay both
terminate `PASS`.

It remains to count the quotient. Identifying `OB/OI` leaves three semantic
root classes per assignment and allocation, hence 108 cells. On assignments,
`(KBNI-2)` has five two-cycles and two fixed points, or seven orbits. The
composition of the two transports exchanges `A` and `TA` while fixing the
semantic `other` class, giving two root orbits. Allocations are fixed. Hence
there are `7*2*3=42` orbits.

The canonical leaves use assignment orbits `F00/F01` and `M00`. They account
for `2*2*3=12` orbit representatives. The other five assignment orbits give
`5*2*3=30`, exactly the displayed residual frontier. QED.
