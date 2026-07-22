# Claim contract - L1 fixed-source quotient-partition anchor census

## Inputs

- one fixed maximal sunflower source with `M_src` petals of size `ell`;
- a genuine degree-`ell` quotient rechart carrying at least one whole source
  petal;
- optionally, the proved per-key bipolar fixed-polarity payment.

## Outputs

- one full petal determines the quotient partition up to additive shift;
- at most `M_src` anchored partition classes;
- at most `M_src 3^(n/ell)` complete-fiber structural keys;
- polynomial aggregation at the L1 cutoff.

## Consumer rule

Use this theorem after fixing the first maximal source. It removes
non-intrinsic quotient-polynomial multiplicity only when the rechart carries
one source petal as a complete degree-`ell` fiber.

## Nonclaims

No Forney coefficient-key payment, growing-polarity count, arbitrary-locator
count, smaller-fiber refinement, or theorem forcing an arbitrary internal
quotient map to carry a whole source petal is proved.

## Falsifier

Two inequivalent monic degree-`ell` level-fiber partitions carrying the same
`ell`-point source petal, or more than `M_src` anchored partition classes.
