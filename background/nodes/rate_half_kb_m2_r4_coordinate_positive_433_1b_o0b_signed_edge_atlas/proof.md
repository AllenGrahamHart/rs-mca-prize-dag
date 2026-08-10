# Proof

The residual workboard fixes the displayed common and outside multigraphs.
A loop costs one collision-defect unit. A multiplicity-two target pair has
cost zero when its two records have opposite signs and cost two when their
signs agree. Thus at most one of `BC,DE,DF` can repeat, proving the four-stratum
partition.

In `S0`, the active singleton signs form the five-cycle
`A-B-E-F-C-A`, hence have one cycle invariant and two gauge orbits. In `SBC`,
the repeated `BC` edge adds the independent triangle `A-B-C-A`, hence two
cycle invariants and four orbits. In `SDE` and `SDF`, the repeated edge merely
attaches vertex `D` to the five-cycle, so each again has one invariant and two
orbits. The exact image ranks give orbit sizes `16,16,32,32` by stratum.

The executable atlas enumerates every active-sign assignment and every one of
the 64 vertex gauges. It checks invariant constancy, canonical representatives,
orbit coverage, all twelve records, the degree-four equations, and the defect
ledger. The orbit cardinalities sum to `32+64+64+64=224`. QED.
