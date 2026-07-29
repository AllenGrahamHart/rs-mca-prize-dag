# Upstream crosswalk - M31 adjacent quotient-rotation product spectrum

```yaml
workboard_item: M0/M1
row: Mersenne-31 list stress row
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: exact product-class spectrum for the zero-remainder cyclic quotient-rotation construction
architecture: DIRECT
partition_digest: N/A
atom_or_cell: structured quotient-rotation lower family
quantifier: every order-2^21 multiplicative coset in F_(p^4), p=2^31-1
projection_and_unit: distinct codewords in one received-word Hamming ball
claimed_bound: lower floor 8287155; construction maximum 8287155
status: PROVED
impact: ROUTE_CUT / LOCAL_ONLY
falsifier: a subset-product class count differing from the printed spectrum
replay: two independent exact integer verifiers
upstream_pr: https://github.com/przchojecki/rs-mca/pull/1123
upstream_branch: agent/m31-quotient-rotation-spectrum
upstream_head: b6619f20f55beb9183bb0e9d591d0630c8e3f306
upstream_state_at_pin: OPEN / READY FOR REVIEW
```

Portable destination: `experimental/experiments.tex`, immediately after the
general cyclic quotient-rotation theorem, with the explicit nonclaim that the
floor is below budget and supplies no deployed `U_Q`.
