# Dependency sub-DAG

```text
polynomial algebra + round-35 (L2) pencil model
                 |
                 v
rate_half_l2_stratum_rational_parametrization [PROVED; (RES) split]
   |
   +-- supersedes as instrument: the (D-F) inversion inside
   |   rate_half_l2_stratum_nonempty_at_m_two [PROVED] (witness theorem
   |   unaffected)
   |
   : evidence / construction instrument
   v
rate_half_band_crossing_location [TARGET]
```

No requirement edge in. The outgoing edge supplies the construction
instrument of the (SAT3)-on-(L2) lane; the first-moment gate it feeds is
recorded in `rate_half_sat3_realizability_ledger_record`.
