# Proof

The saturated defect classifier gives exactly 96 labeled source-line packets
in 12 matching-preserving orbits. The colored quotient compiler applies to
every such orbit and gives exactly one of two cases:

```text
aligned:      Omega=J_1,
near-aligned: Omega={xi,ell}.
```

There is no unclassified source-line orbit.

## Aligned case

Internal-star reconstruction divides candidates into positive and negative
signs. The universal aligned-negative q-slice theorem excludes the negative
sign.

For the positive sign, the forced source fiber is either ramified or
unramified. The repaired ramified theorem excludes `w=0` for both internal
templates and all three residual allocations. In the unramified locus there
are exactly two internal templates, fixed-moving and moving-moving, and
exactly three UFD allocations, same, swap, and mixed. The six corresponding
PROVED leaves exclude all six cells. Four leaves are q-slice exclusions; the
moving-mixed and three fixed-moving leaves use the stronger full quotient
identities at their exact q-slice survivors. Hence no aligned candidate
exists.

## Near-aligned case

The near-negative theorem excludes the complete negative locus, including
`w=0`. For the positive sign, the affine classification has exactly 18
charts: nine fixed-moving and nine moving-moving. The 15 chart theorems in
the dependency set exclude all 18, because one reciprocal fixed theorem
covers two square allocations and one reciprocal moving theorem covers a
three-chart orbit.

The only non-affine locus is the homogeneous endpoint boundary. Its PROVED
theorem exhausts seven shards: three fixed-moving, two moving trace, and two
moving constant-ratio shards. Thus no near-aligned candidate exists.

The aligned and near-aligned cases exhaust the 12 source-line orbits, so no
admissible saturated diagonal `c2(1,1,2)` source-line packet exists.
