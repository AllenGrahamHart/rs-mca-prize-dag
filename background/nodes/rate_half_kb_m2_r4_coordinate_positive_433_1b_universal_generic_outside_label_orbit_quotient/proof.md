# Proof

On the `433-1b -> O0a` route, the outside atlas is

```text
DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF.
```

The first two records have identical products and squared sums, so `P`
exchanges them in every O0a complete system.  The proved O0a `D/E`
transport induces `Q`, fixes every O0a common role cell and target lane,
and preserves all guards and equations.

For label `(xi,j)`, delete `xi`, transport each edge of matching `j`, restore
the canonical six-record order, and look up the resulting matching.  Exact
enumeration closes all 105 labels under `P,Q`.  It gives 36 disjoint orbits
with profile `1:3,2:15,4:18` and canonical digest
`b5ec5e8418af3385dc83aeeb9aca9c8b851eae9e23794e6637f1b42a37576cb6`.

Both generators fix the set of endpoint indices `{5,6}` pointwise.  The 30
endpoint labels therefore form 12 whole orbits with profile `1:2,2:6,4:4`.
The complement has 75 labels in 24 whole orbits with profile
`1:1,2:9,4:14` and digest
`c5c6f6b2e4af85cf2efd05fe106fa63a09bde9e6fa6ee07ed29a7f292f3b7353`.
QED.

Neither generator gives the displayed action on all O0b lanes: the O0b
`S0` repeated-BC pair is signed rather than identical, and `D/E` exchange
does not preserve O0b's `BE,CF` colored incidences.  Thus the proof has no
O0b conclusion.
