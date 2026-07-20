# Upstream complete-fiber crosswalk

## Packet read

Przemek PR `#977`, based on `rs-mca@999b8f3a`, proves the generic fixed-size
subset-packing compiler and its equation-(2) wrapper for canonical complete
fibers of one fixed power map. Its source objects are

```text
ground = powerImage H c,
block(P) = completeFiberSet H c (canonicalSupport H m U P),
h = floor((K-1)/c).
```

The PR deliberately retains `|powerImage H c|` and does not formalize the
separate `n/c` normalization or the Johnson-ball equation (3).

## Local subsumption

The proved local `pma_source_paving_bridge` already applies the same generic
packing argument to the full PMA auxiliary agreement blocks. For degree
`<kappa` polynomials, two distinct blocks intersect in at most `kappa-1`
points, so fixed block size `a` gives

```text
#objects <= binom(L,kappa)/binom(a,kappa).
```

Summing the interpolation ownership charge directly gives the local aggregate

```text
sum_Q binom(a(Q),kappa) <= binom(L,kappa).
```

Thus importing PR `#977` would duplicate, not strengthen, the current L1
packing input.

## Why power-fiber normalization does not close the gap

The surviving L1 condition is a large value fiber of the codeword-dependent
rational map `W/L_D` inside one arbitrary source petal. It is not a union of
fibers of one fixed map `x |-> x^c`. Size alone cannot supply that property:
from a partition into `n/c` blocks of size `c`, one may choose `c-1` points
from every block, obtaining `n-n/c` points with no complete block.

At the L1 lower cutoff the forced `Omega(n/log^2 n)` set is far below this
avoidance threshold. The separate theorem
`pma_arbitrary_petal_source_realizability` also prevents inferring fixed
power-map structure from maximal-source geometry alone. A complete-fiber
route would therefore need a new contributor-dependent normalization or
inverse theorem; the elementary rewrite `|powerImage H c|=n/c` is not that
bridge.
