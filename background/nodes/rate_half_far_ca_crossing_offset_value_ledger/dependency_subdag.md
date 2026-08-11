# Dependency sub-DAG

```text
Round-37 U-rand + Round-38 URATE/genericity addenda (proofs on A1)
                 |
                 v
rate_half_far_ca_crossing_offset_value_ledger [TARGET; ledger]
   |         |                |
   |         |                +-- (FIB) floor case: rate_half_far_ca_hr_dictionary_common_support [PROVED]
   |         +-- T_sym mechanism: rate_half_far_ca_negation_closure_excess_fence [PROVED]
   +-- cap independence: rate_half_type2_ledger_vacuous_by_sign_fence [PROVED]
                 |
                 : evidence / residual map
                 v
rate_half_band_crossing_location [TARGET]
```

The three sibling fences are textual cross-dependencies (each also carries
its own evidence edge to the crossing node); no requirement edge is
created. The ledger's open items — the two floor residues and the
normal-form conditionality — are the far-CA entries on the round-39
anchor list.
