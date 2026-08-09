# Proof

The pinned cell-4 pairing-11 compiler is evaluated on the exact cell-5
four-basis tower. Its two paired-product equations are quadratic in the same
variable `f`; their division-free resultant is normed to the base field.
External `gcd(P,x^p-x)` reconstruction supplies every base-field root of the
norm and inverse guards.

The 32 rows contain 264 target roots, 464 root-or-exception candidates, and
576 guarded source points. Direct replay routes 64 missing-record
inconsistencies and 64 zero-product rows, then checks the remaining 448 source
points. Their two quadratic root sets have no common `f` root, so no quartic
lift is reached. There is no witness, unresolved branch, or leading-boundary
remainder.

The independent root packet reconstructs 49 polynomial profiles, 236 field
roots, and degrees through 992. A separate Modal replay reconstructs every
candidate union, tower relation, missing record, boundary class, and paired
quadratic directly from those roots.

The generic-label orbit theorem maps `(0,11)` to `(1,11)` and maps `(2,11)`
to `(2,14)`. These bijections preserve every equation and guard, proving all
four labels.
