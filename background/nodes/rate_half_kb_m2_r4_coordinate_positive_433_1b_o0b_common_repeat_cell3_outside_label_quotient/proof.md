# Proof

Changing `d` to `-d` fixes `BE`, `CF`, and `EF`. It sends the signed edge
records `DE+` to `DE-` and `DF+` to `DF-`, and conversely. Expanding each
product and squared sum after substitution proves the displayed record
permutation exactly.

For a label `(xi,m)`, remove record `xi`, transport the three pairs in
matching `m`, reindex the six residual records, and canonicalize the three
unordered pairs. Applying this construction twice is the identity. Exhaustive
enumeration starts with all `7*15=105` labels and removes complete orbits.
The resulting 9 singleton and 48 doubleton orbits are disjoint and have total
size 105. QED.
