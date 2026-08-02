# KoalaBear positive 433-1a cell-5 exceptional-fiber router census

- **status:** PROVED
- **scope:** deployed characteristic, cell 5, signs `(-1,-1)`, specialization
  of the registered generic `DE+/DE-/BE` exclusion
- **consumer:** `rate_half_band_closure`

Let `p=2130706433` and remove the source-forbidden values

```text
F_bad={0,1,-1,iota,-iota} subset F_p.
```

Exact norms of the 30 declared guards and two chart denominators on each of
the five primitive residue factors have numerator/denominator root union
whose part outside `F_bad` has size 14.

The registered generic certificate chain contains six denominator
categories: the monic squared-pair basis, primitive polynomial and factors,
primitive coordinate maps, colored Bezout packet, guard norms, and localized
multiplication operator.  Across these categories there are 3,659
denominator occurrences and 1,143 category-unique denominator polynomials.
Their deployed-field root union has size 61, of which 56 lie outside
`F_bad`.

The two exceptional sets overlap in one value.  Their union outside
`F_bad` therefore consists of exactly 69 deployed-field values.  In sorted
decimal serialization its SHA-256 is

```text
bd64dc238bb3dcc4491d7d7b856078871336571cbdd5df3343014f8198cfe1d4.
```

At every admissible `t` outside this 69-value set, every registered
coefficient is regular and every declared guard/chart norm is nonzero.
Consequently the proved generic cell-5 sign-row exclusion specializes at
that fiber.

This theorem is a finite completeness router.  It does not exclude any of
the 69 listed fibers, treat another sign row or matching cell, delete cell 5
or `433-1a -> O0b`, close K3, a Prize row, or either Prize result.

## Falsifier

An unlisted admissible deployed `t` where one registered denominator or
guard norm vanishes, a mismatch in the printed 69-value digest, or an
admissible packet outside the router set that evades the specialized generic
Bezout identity.
