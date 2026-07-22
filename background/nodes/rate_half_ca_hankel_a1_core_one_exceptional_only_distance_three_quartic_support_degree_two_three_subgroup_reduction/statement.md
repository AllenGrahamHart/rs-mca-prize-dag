# `A=1` distance-three quartic support degree-two/three subgroup reduction

- **status:** PROVED
- **closure:** proof using a published subgroup-curve bound
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_low_degree_fiber_reduction`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_official_trigonal_subgroup_exclusion`

Retain the official all-deficient support alternative from the first
dependency. Its degree-three common-fiber branch is empty.

Its degree-two branch has the following exact form. There is one fixed
`c in mu_N` such that at least `e-40` of the exceptional pairs are all of
one of the two forms

```text
{x,-x},                                               (Q23-1)
{x,c/x}.                                              (Q23-2)
```

The same form applies to every captured pair; at most `40` exceptional
pairs lie outside it.

Consequently simultaneous deficiency of all support pair-crossing matrices
has only three remaining branches:

1. global smooth antiweight `H(a_k)+H(b_k)=0` for every pair;
2. an antipodal or constant-product matching with at most `40` tail pairs;
3. at least `e-148` fibers of one separable degree-four rational map.

This node does not remove the bounded tail in the degree-two branch and does
not classify the degree-four coincidence divisor.
