# Claim contract

## Proved

- Primitive side-swap unions occur only at odd widths.
- Subject to antipodal-freeness and trivial common scaling stabilizer, they
  are exactly the side choices satisfying all odd elementary-symmetric,
  equivalently odd power-sum, equations below `h`.
- The centered polynomial is odd.
- The anchored odd-width candidate count is at most
  `binom(n/2-1,h-1)` before the signed-moment and primitive tests.

## Consumer

`f3_hge4_norm_gate_count`, through the primitive near-square union route.

## Falsifier

One primitive even-width swap union, or one odd-width swap union violating an
odd moment below `h`, falsifies the theorem.

## Nonclaims

- No bound on free unions is proved.
- No nontrivial bound on the odd Vandermonde sign fiber is proved.
- The binomial candidate cap does not imply the quadratic HGE4 aggregate.
