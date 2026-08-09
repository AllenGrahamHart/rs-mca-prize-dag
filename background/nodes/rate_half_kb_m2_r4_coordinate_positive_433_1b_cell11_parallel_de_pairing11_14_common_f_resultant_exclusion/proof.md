# Proof

The pinned cell-4 pairing-11 compiler is evaluated on the exact cell-11
four-basis tower. Its two paired-product equations are quadratic in the same
variable `f`; their division-free resultant is normed to the base field.
External `gcd(P,x^p-x)` reconstruction supplies every base-field root of the
norm and inverse guards.

The 32 rows contain 216 target roots, 360 root-or-exception candidates, and
272 guarded source points. Direct replay routes 64 missing-record
inconsistencies and 64 zero-product rows, then checks the remaining 144
interior cases. Their two quadratic root sets have no common `f` root, so no
quartic lift is reached. The replay also pays 32 `B`-leading and 32
`C`-leading boundary cases. There is no witness or unresolved branch.

The independent root packet reconstructs 53 polynomial profiles, 222 field
roots, and degrees through 1420. A separate Modal replay reconstructs every
candidate union, tower relation, missing record, boundary class, and paired
quadratic directly from those roots.

The generic-label orbit theorem maps `(0,11)` to `(1,11)` and maps `(2,11)`
to `(2,14)`. These bijections preserve every equation and guard, proving all
four labels.
