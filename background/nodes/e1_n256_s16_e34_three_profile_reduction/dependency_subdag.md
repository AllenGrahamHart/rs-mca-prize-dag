# Dependency sub-DAG

```text
e1_n256_s16_sparse_l1_variance_exclusion --req-->
e1_n256_s16_e36_quotient_schur_exclusion --req-->
e1_n256_s16_e35_quotient_schur_exclusion --req-->
collision_norm_criterion                         --req-->
                     e1_n256_s16_e34_three_profile_reduction

e1_n256_s16_e34_three_profile_reduction --ev-->
                     e1_official_prime_exception_control
e1_n256_s16_e34_three_profile_reduction --ev-->
                     unsafe_crossing_family_instantiation
```

The node is a proved route reduction. It does not discharge either target;
the three printed `L=20` profiles remain live at `V=68`.
