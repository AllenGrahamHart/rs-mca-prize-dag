# Dependency sub-DAG

```text
f3_h2_stepanov_inhouse [PROVED]
  --req-->
f3_h3_identity_deficit_energy_close [PROVED implication]
  --ev--> f3_h3_three_to_one_c36 [CONDITIONAL]
  --ev--> f3_h3_mobius_excess_half [TARGET route ledger]

f3_h3_quotient_block_identity [PROVED normalization]
  --req--> f3_h3_identity_deficit_energy_close
```

The equal-energy and correlation identities are proved directly in this
node. The quotient-block dependency pins the quotient convention used by the
critical consumer; the only non-elementary quantitative input is the proved
one-shift Stepanov estimate.
