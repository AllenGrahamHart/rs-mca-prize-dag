# Proof

The universal quotient partitions the 75 active labels into 24 disjoint orbits with size profile

`1^1 2^9 4^14`.

The 16 required owner packets exclude exactly the following representatives:

`(0,0),(0,1),(2,0),(2,1),(0,3),(2,3),(0,4),(2,4),(0,5),(2,5),(0,9),(0,11),(0,12),(0,14),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,7),(3,8),(3,11)`.

There are 24 entries in this list: the first owner packet contributes four, seven packets contribute two or one as printed, and the final eight `xi=3` packets contribute nine. The verifier compiles the quotient directly, checks that these representatives are pairwise distinct and equal its complete representative set, and transports each exclusion over its orbit. Their union is exactly

`{0,...,4} x {0,...,14}`.

Therefore all 75 active labels are empty. Endpoint roles remain a separate obligation.
