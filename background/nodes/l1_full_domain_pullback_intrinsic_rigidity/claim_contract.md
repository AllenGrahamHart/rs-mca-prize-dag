# Claim contract - L1 full-domain pullback intrinsic rigidity

## Inputs

- a finite field containing the coset `H=alpha mu_n`;
- a divisor `s|n`, `s>1`;
- a monic degree-`s` polynomial whose complete `s`-point fibers partition
  all of `H`.

## Output

`P=X^s+c`. Its fibers are intrinsic `mu_s`-cosets, and every fully fiberwise
exact agreement support belongs to the exact-periodic owner.

## Falsifier

A monic non-binomial degree-`s` polynomial giving a complete equal-fiber
partition of a multiplicative coset, or a union of its fibers with trivial
multiplicative stabilizer.

## Nonclaims

No rigidity is asserted when the map has incomplete fibers on the domain or
when the contributor has partial agreement inside a fiber.
