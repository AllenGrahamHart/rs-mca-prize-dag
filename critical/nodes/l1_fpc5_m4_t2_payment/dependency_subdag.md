# Dependency sub-DAG

```text
pma_two_full_petal_linear_slice_reduction [PROVED] --------ev----+
l1_fpc5_m4_t2_official_codimension_sieve [PROVED] --------ev----+
l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice [PROVED] ---ev----+
l1_fpc5_ratequarter_m4_t2_payment [PROVED] ---------------req---+
l1_fpc5_ratehalf_m4_t2_payment [TARGET] ------------------req---+
                                                                    v
  l1_fpc5_m4_t2_payment [CONDITIONAL]
    --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
