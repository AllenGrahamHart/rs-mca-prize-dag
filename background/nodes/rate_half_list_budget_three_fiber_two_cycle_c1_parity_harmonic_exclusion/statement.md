# Budget-three fiber-two c=1 parity harmonic exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic certificate
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_harmonic_field_router`

On the official generic `c=1` two-antipodal-denominator chamber, the
canonical outer ratio is nonharmonic:

```text
q_out!=-1.                                           (CHE1)
```

The field-router dependency reduces every harmonic survivor to one of two
fixed trace terminals over

```text
p=1+k*2^40,       29058991<=k<33554432.              (CHE2)
```

A preregistered 32-shard Modal campaign checked all `4,495,441` integer
moduli in `(CHE2)`, including composites, against

```text
H_P: 41 updates from 8/5,       terminal 2,
H_R: 40 updates from 16,        terminal 2.          (CHE3)
```

`899,088` multiples of five were rejected as composite before division.
All shards completed, exact coverage and rolling digests replay, the longest
shard took 3.121 seconds, and neither trace had a hit.

The launcher, compact result, human-readable result, and independent checker
are

```text
experiments/prize_resolution/
  rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py
  rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.json
  rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.md
  rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_check.py
```

This closes only the harmonic `c=1` parity subbranch. The six nonharmonic
outer-trace tests and the nonparity normalized `c=1` chamber remain open.

