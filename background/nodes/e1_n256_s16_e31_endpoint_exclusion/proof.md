# Proof

By `e1_n256_s16_e31_profile_parity_light_reduction`, every pair-feasible
folded-profile `(3,4,0)` vector at `V=62` has magnitude profile

```text
(3,7), (2,5,1), or (1,3,2).
```

By `e1_n256_s16_e31_three_profile_joint_exclusion`, none of those profiles
can collide. They exhaust the exact reduction, so `V=62` is impossible.

The preceding endpoint theorem left only positive even `V<=62`. Removing
`V=62` advances the live frontier to positive even `V<=60`. QED.
