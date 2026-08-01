# Proof

The negative loop-budget gate starts from the complete-fiber Vieta compiler
and product injectivity.  It proves that a negative packet has at most two
antipodal common-`K` edge orbits.  Solving the two possible degree profiles
under this bound leaves exactly the five rows `(KBNX-1)`; no graph or
algebraic case remains outside this list.

For profile `(4,4,2)`, the one-loop complete exclusion deletes
`(0,1,0;2,2,0)`.  The two-loop H6 complete-product exclusion is the terminal
member of the exact H8/H6 row census and deletes
`(1,1,0;1,1,1)` in full.

For profile `(4,3,3)`, the new zero-loop complete exclusion deletes
`(0,0,0;2,2,1)`.  The one-loop complete exclusion deletes
`(1,0,0;1,1,2)`.  Finally, the constrained two-loop complete-product
exclusion composes with its `M2/M3` parent and deletes the full
`(1,0,1;2,0,1)` skeleton.

Thus each member of the exhaustive five-row partition is empty.  A packet
in their union cannot exist, proving the claim. QED.
