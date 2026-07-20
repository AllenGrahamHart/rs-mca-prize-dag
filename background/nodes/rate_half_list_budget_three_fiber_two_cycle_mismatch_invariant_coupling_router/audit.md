# Audit

## Count audit

For `c=2`, selecting the two denominator roots used by completion pairs gives
`binom(4,2)=6`. For `c=1`, the repeated completion square and residual
exceptional square form an ordered pair of distinct denominator roots;
there are `4*3` choices and two relative signs `u`, hence 24. The sign of
`s` is global source negation and is not counted twice.

## Invariant audit

The formulas were checked independently by substitution into the five
coefficient definition `(MIC3)`. The anharmonic factorization `(5)` is
checked as an integer polynomial identity on an interpolation grid larger
than its degree in either variable. Mutations deleting the second `u` sign
or replacing the selected `c=2` pair fail on explicit integer fixtures.

## Field audit

Every root of `D_*` is a square because it descends from the order-`2^41`
domain to the order-`2^40` quotient. Thus both roots of `u^2=BD` and the
needed source square roots are in the base field. The official
characteristic is greater than three. Distinct roots of `D_*` make every
candidate source quartic separable.

## Scope audit

Invariant equality certifies only the completion-root PGL match. The full
cycle certifier still requires the primary and secondary coefficient gaps,
canonical span identity, exact denominator inventory, and every later
branch-specific gate. No large or remote computation was used.
