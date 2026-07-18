# Audit

The anchor slope is charged separately. Pair-list agreement is `n-2r`, not
`n-r`; each rider member is derived from the intersection of two slope
witnesses. The factor `r+1` comes from actual distinct slopes per pair-list
member, not witness multiplicity.

The verifier exhausts all pairs and slopes for two tiny proper linear codes,
checks the rider inequality pair by pair, and verifies that every case with at
least two CA-bad slopes has both components within `2r` of the code.
