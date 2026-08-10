# Proof

The product-rank parent makes the five common product rows rank five on the
guarded torus. Their six signed maximal cofactors therefore span the unique
product kernel. Multiplication by `r^4(1-r^4)`, followed by the loop and `AB`
pivot equations, gives the polynomial eight-entry common kernel used in the
replay. The scale is a guard.

For a missing colored record, eliminate its unknown target coordinate from
the two displayed missing equations. Multiplying by `-1` after substituting
`x=-r^4` gives `(CM-1)`. This equation remains necessary even when `am=0`,
so no division or omitted boundary is used in the exclusion.

Exact standard bases first prove all eight common-only cuts are finite.
For each cut, compute the resultant in `r`, enumerate all of its base-field
`u` roots by `gcd(P(U),U^p-U)`, and for every such `u` enumerate all common
`r` roots by the same method on the specialized gcd. Direct evaluation
replays the torus and cut equations at every lift. In each `BE` row all 12
raw lifts make the inherited guard zero. Hence no guarded missing-`BE`
system exists, regardless of its outside sign or residual matching.

The transport parent is an exact bijection of all labels and signs and maps
cell-3 `BE` to cell-6 `CF`. It transfers the 120 exclusions. QED.
