# Audit

## Scope and typing

The color `a^(p+1)` is an `m`th root of unity, but it is not asserted to lie
in the prime field. The official evaluation fields can have extension degree
eight or sixteen. The proof uses all `m` colors and only the injectivity of a
nonconstant linear interpolant.

The missing color is legitimate because `P_s` has `m-1` distinct roots and a
linear `E_s` takes distinct values on them. Formula `(4)` follows by deleting
the unique unused linear factor from `E_s^m-1`; it does not assume that the
roots of `P_s` lie in the base field.

## Algebra audit

Only the first three coefficients are used. Their denominators divide six,
and `h`, `h+1`, and the resultant scalar are nonzero on every official row.
The resultant is checked from the exact linear/quadratic formula in `y`, not
from a numerical Groebner calculation.

The constant case is discharged directly by a separate three-coefficient
comparison. The cases `s=1` and `s=-m` in the linear case are rejected
solely by the already-proved off-prime-field condition. No inference is made
from failed toy searches.

## Nonclaims

The theorem deletes the two lowest degree strata. It gives no bound on color
degrees at least two and does not turn the bounded colored system into a
sufficient cyclotomic or inner certificate.
