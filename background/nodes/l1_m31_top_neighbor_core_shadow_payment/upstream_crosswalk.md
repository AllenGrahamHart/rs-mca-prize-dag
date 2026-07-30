# Upstream crosswalk - M31 top-neighbor core-shadow payment

```yaml
workboard_item: M1/L/T
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Every fixed degree-4979 core supports at most 240 actual top neighbors; a forbidden dense-top anchor realizes at least 4477705 such cores.
architecture: M31_RANK7_PROPER_G_ZERO_EXCESS_INCIDENCE_ROUTE_CUT_V1
atom_or_cell: primitive top-shift core-shadow aggregation
quantifier: every actual top-neighbor family around one fixed listed anchor
projection_and_unit: distinct LIST codewords per received word
claimed_bound: fixed-core neighbor cap 240 and codimension-one core-shadow floor 4477705
status: PROVED LOCAL
impact: ROUTE REDUCTION
falsifier: failure of the affine-flat inclusion, affine-span cap, or core-incidence double count
replay: symbolic proof and two exact verifier sources; local arithmetic unrun
```

This extends upstream draft PR `#1124` after its geometry-only route cut. It
uses upstream `thm:affine-span-list` as the actual-list payment and leaves the
cross-core aggregate open. Export custody is head commit
`36721bfb8538bef480048db627d0ea726f8a69f0`.
