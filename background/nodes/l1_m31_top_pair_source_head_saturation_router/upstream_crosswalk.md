# Upstream crosswalk - M31 top-pair source-head saturation router

```yaml
workboard_item: M1/L/T
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Every maximal-overlap proper-G pair saturates the reduced determinant with scalar equal to its source-head difference; each head fiber has at most 458812 members.
architecture: M31_RANK7_PROPER_G_ZERO_EXCESS_INCIDENCE_ROUTE_CUT_V1
atom_or_cell: source-head colored primitive top-shift aggregate
quantifier: every actual top pair and every head fiber in the violating proper zero-excess class
projection_and_unit: distinct LIST codewords per received word
claimed_bound: at least five head values, at least 1699117 full-head members, and one full-head anchor with 107897 top neighbors
status: PROVED LOCAL
impact: ROUTE REDUCTION
falsifier: failure of determinant saturation, head coloring, constant-weight cap, or colored-core incidence
replay: symbolic proof and two exact verifier sources; local arithmetic unrun
```

This is a direct extension candidate for draft PR `#1124`. It uses the source
notation and reduced determinant of upstream PR `#1113` rather than replacing
them with a support-only model.
