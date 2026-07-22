# Claim contract - L1 Pade-remainder Jacobian dichotomy

## Inputs

- the all-cofactor full-locator Pade section;
- monic Euclidean division `U=LQ+P`;
- squarefreeness of the domain locator for the exact-shell split.

## Outputs

- differential `D -> -(QD mod L)`;
- full Jacobian rank `a` for the remainder map when `gcd(L,Q)=1`;
- rank `w=a-k` and smooth local codimension `w` for the Pade section there;
- containment of every rank-collapse point in `Res(L,Q)=0`;
- canonical primitive-transverse/tangent partition of every exact shell;
- an exact tangent witness with genuine projected rank loss.

## Consumer rule

Remove or pay `gcd(L,Q)!=1` as a tangent first-match owner before invoking
smooth-section arguments.  On the remaining primitive branch, rank collapse
is unavailable as an explanation for excess split mass; the proof must
control global component/split-point concentration on a smooth codimension-
`w` section.

## Nonclaims

Smoothness does not imply the desired finite-field split-point count.  No
irreducibility, component bound, Lang--Weil estimate, quotient payment, or
tangent census is proved.  A tangent point is not claimed singular after the
high-coordinate projection unless its rank is checked.

## Falsifier

Failure of `(JT3)`, a coprime `(L,Q)` with Pade Jacobian rank below `w`, a
rank-deficient point off the resultant, a noncanonical exact-shell split, or
an alleged tangent witness with a complement root or full projected rank.
