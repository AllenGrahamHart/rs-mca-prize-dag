# Cycle 264: rate-half Shape-A all-excess degree-ledger rank fence (2026-08-13)

The all-partition scan suggested full rank, but it sampled incidence tables.
An algebraically structured table gives an exact counterexample to the
broader degree-ledger-only rank route.

Over `F_211`, take four common fifth/seventh-power values and the biform

```text
G(t,X)=t^5-X^7.
```

Its grid has `28` domain rows, `21` slopes, five roots in every row, seven
roots in twenty fibers, and no root in the zero fiber. Hence its excess
profile is `(7,0,...,0)`. The induced all-excess residual blocks are all
nonzero, yet the exact `120 x 28` matrix has rank `27`.

```text
result:                  PROVED degree-ledger rank route fence
matrix:                  rank 27/28 over F_211
kernel support:          21/21 polynomial blocks
hostile mutations:       2/2 rejected
independent audit:       exact rank and parity replay
compute:                 subsecond guarded local exact arithmetic
critical status effect:  none
```

This is not an official Shape-A survivor. It does not impose spread,
source/Hankel, collision, or positive-padding constraints. It proves that a
closing theorem must use at least one of those constraints; more random
degree-preserving incidence scans cannot establish universal full rank.
