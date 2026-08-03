# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and kernel [PROVED]
        |
        v
(KBP1B3-QUOT-1): global quadratic quotient [PROVED]
        |
        v
(KBP1B3-DE-P7-1): pairing-7 DE block [PROVED]
        |
        v
rate_half_band_closure [TARGET]
```

Repository IDs:

```text
rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_global_quadratic_quotient
  -> rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_de_pairing7_complete_exclusion
  -> rate_half_band_closure
```

The quotient-to-pairing-7 edge is `req`. The edge to
`rate_half_band_closure` is evidence only.
