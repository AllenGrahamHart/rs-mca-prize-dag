# Dependency sub-DAG

```text
rate_half_ca_hankel_split_pencil_equivalence [PROVED]
  --req--> rate_half_ca_hankel_exceptional_root_charge [PROVED]

rate_half_ca_hankel_minimal_index_budget [PROVED]
  --req--> rate_half_ca_hankel_exceptional_root_charge [PROVED]

rate_half_ca_hankel_exceptional_root_charge [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The new node strengthens the terminal profile census but does not promote the
critical target.  The remaining strict `A=3` profile is core-free with
`e>=2^37`; the half-distance endpoint also retains `A=1`.
