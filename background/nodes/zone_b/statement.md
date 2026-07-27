# zone_b

- **status:** CONDITIONAL

On an admissible clean-anchor row in the pair-feasible direct-E1 candidate
class `|F_p(Q)|>=b_pair_min(K,B*)`, determine the exact ambient-field image

```text
|{e_1(B): B an antipodal-rearrangement class}|
```

at the required quotient order and compare it with `B*`. For the current clean
candidate predecessors the actual quotient orders are `N=256` at rates `1/4`
and `1/8`, and `N=512` at rate `1/16`; their folded dimensions are `128,128,256`.

Conditional on `e1_fullness`, every row in this candidate class has
image size greater than `B*` and supplies a direct-value unsafe payload. This
route-local determination is evidence for
`unsafe_crossing_family_instantiation`, not universal unsafe coverage.

The pair-feasible class is automatically ambient-generating by
`e1_pair_feasible_ambient_generation`; no proper-subfield transfer remains in
this branch. It is also prime-field with `p=1 mod N` by
`e1_pair_feasible_prime_field_reduction`.

Historical experiments at quotient orders `16,32,64,128,256` remain evidence
about collision behavior. In particular, an `N=128` result does not by itself
pay any of the present clean anchors.
