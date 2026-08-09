# Proof

There are seven direct roles and 15 pairing labels, hence 105 raw labels.
The proved endpoint-role theorem excludes the 30 labels with `xi in {5,6}`.

For `xi in {0,1,2,3,4}`, the proved universal router partitions the other
75 labels into 24 disjoint orbits. The owner packets pay the following
representatives:

| owner family | representatives | orbits | labels |
|---|---|---:|---:|
| parallel-DE first pair | `(0,0),(0,1),(2,0),(2,1)` | 4 | 9 |
| parallel-DE pairing 11 | `(0,11),(2,11)` | 2 | 4 |
| parallel-DE pairing 3 | `(0,3),(2,3)` | 2 | 8 |
| parallel-DE pairing 4 | `(0,4),(2,4)` | 2 | 8 |
| parallel-DE pairing 5 | `(0,5),(2,5)` | 2 | 8 |
| positive-DE pairing 9 | `(0,9)` | 1 | 4 |
| positive-DE pairing 12 | `(0,12)` | 1 | 4 |
| positive-DE pairing 14 | `(0,14)` | 1 | 2 |
| xi3 pairings 0,1,2 | `(3,0),(3,1),(3,2)` | 3 | 6 |
| xi3 pairings 3,4,5 | `(3,3),(3,4),(3,5)` | 3 | 12 |
| xi3 pairings 7,8,11 | `(3,7),(3,8),(3,11)` | 3 | 12 |
| total | 24 representatives | 24 | 75 |

Every owner packet is `PROVED` and transports exclusion across its printed
orbit. The executable verifier imports the authoritative router, checks the
24-orbit partition and size profile `1:1,2:9,4:14`, checks that the owner
sets are disjoint and equal the router representatives, and verifies all 19
dependency statuses. Thus all 75 non-endpoint labels are excluded. Together
with the 30 endpoint labels, all `30+75=105` cell-9 labels are excluded. QED.
