# KoalaBear positive 433-1a cell-5 raw-basis fiber exclusion

- **status:** PROVED
- **scope:** the final eight basis-specialization hazards in the cell-5
  exceptional router, with signs `(-1,-1)`
- **consumer:** the complete cell-5 sign-row exclusion

At each of the eight fibers, construct the guarded squared signed-pair
quotient directly over `F_2130706433` from

```text
P, g3, h, u*D0*D1-1.
```

Exact certified Groebner bases give quotient dimension 24 at seven fibers
and dimension 23 at `t=1332924776`.  Multiplication by `x1,x0,b` satisfies
the defining relations and the matrix for `D0*D1` is invertible.  The form
`x1+2*x0+b` is primitive at every fiber.  Its squarefree minimal-polynomial
factors account for the full fiber dimensions.

Fresh `DE+/DE-/BE` replay gives 115 irreducible rows: 35 have common gcd
`1` and 80 have common gcd `e^2-1`.  Hence all eight fibers are empty for
cell 5 and sign row `(-1,-1)`.

This does not treat another sign or cell, delete cell 5 or route
`433-1a -> O0b`, close K3, a Prize row, LIST, or MCA.

## Falsifier

An incorrect raw quotient dimension, failed defining relation or
localization, missing factor, outside colored gcd, or admissible packet at
one of the eight listed fibers.
