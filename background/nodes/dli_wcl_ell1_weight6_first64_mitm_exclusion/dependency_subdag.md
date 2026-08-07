# Dependency sub-DAG

```text
dli_wcl_weight5_first64_mitm_exclusion [PROVED]
  --> dli_wcl_ell1_weight6_first64_mitm_exclusion [PROVED]
       --ev--> dli_wcl_slot_1_6_emptiness [TARGET]
                --> dli_wcl_zone_coverage [CONDITIONAL]
```

The requirement imports only the certified identity and order of the first 64
split-prime rows. The new exact search is independent of the weight-five
exclusion. Its outgoing edge is evidence: finite survival cannot discharge
the universal target.
