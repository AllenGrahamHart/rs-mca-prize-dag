# Proof

The residual workboard gives `(KBP1BA-1)` and `(KBP1BA-3)`.  A loop costs
one defect unit.  A multiplicity-two cross pair costs zero exactly when its
two records use opposite signed target edges, so `BC` is `bc,-bc`.  A
multiplicity-three cross pair has minimum defect two, attained exactly by a
`2+1` sign split.  Hence `DE` has the displayed split and the total defect
is `1+2=3`; all singleton edges cost zero.

The common degrees after `(KBP1BA-2)` are `(4,3,3)`, so `B,C` each need one
colored incidence.  In `O0a`, both colored incidences meet the outside
degree-two deficit at `F`; outside multiplicities `(3,1,1)` then give
degree four at `D,E,F`.  This proves the twelve-edge degree ledger.

The signs not fixed in opposite pairs are those on
`AB,AC,BF,CF,DE,DF,EF`.  Their graph is connected on six vertices and has
seven edges, so its cycle space has dimension `7-6+1=2`.  Choose

```text
AB,AC,BF,DE,DF
```

as a spanning tree.  Vertex sign gauge makes all five tree signs positive.
The two chord signs are then exactly the products around the cycles
`A-B-F-C-A` and `D-E-F-D`, giving `(KBP1BA-4)` and the canonical records
`(KBP1BA-5)`.

The executable enumerates all `2^7=128` active-sign assignments and all
`2^6` vertex gauges.  It obtains four disjoint orbits of size 32, verifies
both invariants on every member, and replays every target degree, record
count, and defect contribution. QED.
