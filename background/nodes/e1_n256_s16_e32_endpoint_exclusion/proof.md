# Proof

The proved `V=64` profile/parity/diameter reduction enumerates all 18 integer
autocorrelation magnitude profiles and pays every one except

```text
(4,7), (0,8), (3,5,1).                               (1)
```

The three profile exclusions are unconditional and disjoint:

1. `e1_n256_s16_e32_profile_08_light_template_exclusion` proves `(0,8)`
   empty by two complete 119,087,616-vector censuses.
2. `e1_n256_s16_e32_profile_351_light_template_exclusion` proves every
   `(3,5,1)` vector has `M_3<=1392<1517`, using two independent complete
   148-template censuses.
3. `e1_n256_s16_e32_profile_47_exact_norm_exclusion` removes every proper-
   conductor `(4,7)` vector by the conductor theorem and every full-conductor
   vector by two independent exact norm censuses, whose maximum satisfies
   `15*N_max<2^250`.

Thus every case in (1) is impossible, and there is no pair-feasible collision
at `V=64`. The preceding endpoint chain leaves only positive even `V<=64`;
removing 64 sharpens this to `0<V<=62`. QED.
