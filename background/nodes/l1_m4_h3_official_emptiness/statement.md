# L1 official m=4, h=3 split-pencil emptiness

- **status:** PROVED
- **dependencies:** `l1_m4_h3_cartier_resonance_reduction`,
  `l1_m4_h3_positive_tangent_multiplicity_exclusion`,
  `l1_m4_h3_nu0_zero_b_euler_exclusion`,
  `l1_m4_h3_nu0_nonzero_b_tangent_exclusion`,
  `l1_m4_h3_nu0_h0_auxiliary_fiber_exclusion`,
  `l1_m4_h3_nu0_h3_tangent_multiplicity_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

For every official row

```text
(n,p)=(32768,8191), (524288,131071),
      (2097152,524287), (8589934592,2147483647),
n=4(p+1),
```

there is no first-checkpoint split pencil with exactly three complete
degree-`p` fibers. Equivalently, the complete official `m=4,h=3` stratum is
empty.

This closes one exact branch of the characteristic-width endpoint. It does
not classify nonembedded `m=4,h=2`, treat `m=8,16`, treat width above `p`,
or close L1.
