# Upstream crosswalk - p-free Wronskian distance packing

This is an arbitrary-target `(Q)` statement, unlike the zero-prefix F2
summit. It converts equality in the p-free power-sum map into a signed
logarithmic-derivative relation and then into constant-weight packing. In
Przemek's terminology it is a collision-gap rung: every nontrivial collision
has disjoint-tail width at least `ceil((d+2)/2)`.

The theorem can be vendored without a Myerson hypothesis. It does not supply
the final quotient/prefix flatness constant because the packing quotient can
remain exponential at linear density. The natural successor is a primitive
shift-pair or exchange-compression estimate on families that approach this
packing cap.

Scope pin: this is a collision-gap rung for the coarse p-free `(Q)` map, not
an improvement to the exact elementary-prefix SPI ledger. Full-prefix pairs
already have tail width at least `d+1`; after checkpoints are forgotten only
the sharp half-depth bound survives. Under `q<2^256`, the coarse packing cap
is itself too large to pay any cell with `a+k>=n` and `n-a>=128`.
