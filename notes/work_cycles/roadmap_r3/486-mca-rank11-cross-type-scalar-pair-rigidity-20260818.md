# Cycle 486: cross-type scalar-pair rigidity

## Result: PROVED independent-normalization exclusion

Consider two distinct pole-simple atom certificates sharing a sharp
28-record deck, with 14 supports from each of two distinct pair types. If
their scalar coefficient pairs are independent, the common coefficient-zero
set `H` consists of roots of both denominators. Pole-simplicity therefore
bounds every `H` point by one deck incidence.

Writing `z=|G\H|`, the complete support-incidence count becomes

```text
28m' <= n' + 27z,
z >= 1079711-c.
```

Every point of `G\H` belongs to at least 27 supports, hence to at least 13
from each pair type and therefore to both exact pair cores. Distinct-pair
Reed--Solomon uniqueness caps that intersection at `1048575-c`. The
shortening-invariant contradiction margin is 31,136.

Thus every surviving cross-type collision has proportional scalar pairs. In
degree two, the scalar pair records the leading coefficients of the two
locator generators, so proportionality is exactly equality of the
projective quotient-map value at infinity.

## Audit

The primary verifier recomputes the incidence floor and checks shortening
invariance at representative boundary values. The independent audit checks
132 shortening values, the 14+14 multiplicity implication, proof language,
and parent statuses. Ten hostile contract mutations are rejected. No Modal
computation was used.

## Burn-down

```text
starting local pin:       201d26821
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
upstream frontier pin:    PR #1173 at 2788d5ec3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +1 PROVED route node, +4 edges
critical status delta:    none
closed branch:            independent scalar-pair cross-type collision
compute spend:            none
next action:              proportional-scalar compatibility or deck supply
```

## Nonclaims

- no proof that arbitrary quotient types admit a shared 14+14 deck;
- no equality or count of proportional-scalar quotient maps;
- no quotient-population or chronology payment;
- no shifted/nonquadratic/high-complexity payment, rank-eleven closure, or
  MCA closure.
