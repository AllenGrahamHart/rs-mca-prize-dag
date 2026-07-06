# conditional: e1_fullness

## Predicate nodes

- `e1_exceptional_set_reduction`
- `e1_official_prime_exception_control`

## Claim

Conditional on official-prime exceptional-set control, non-quotient `e_1`
collisions are `o(1)`-sparse for the admissible prize primes.

## Proof

The proved predicate `e1_exceptional_set_reduction` reduces every
non-quotient `e_1` collision outside the paid antipodal quotient class to
incidence between the row prime and an explicit bounded norm-divisor
exceptional set. It also records the equivalent folded sparse-kernel
certificate form and the proved small-radius exclusions.

The remaining predicate `e1_official_prime_exception_control` says that the
admissible prize-scale row primes in the open E1 cells have negligible
incidence with that exceptional set, or are certified directly by the folded
lattice procedure.

Combining the reduction with that official-prime control leaves only the paid
signed-core quotient collisions at leading order. Hence the non-quotient
collisions are `o(1)`-sparse relative to the signed-core quotient, which is the
statement of `e1_fullness`.
