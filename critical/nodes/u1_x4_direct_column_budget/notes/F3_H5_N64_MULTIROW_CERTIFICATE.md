# F3 h=5 n=64 multirow certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATES.

This is a follow-up to the h=5 n=32 compiled certificate.  It tests the next
power-of-two row at `h=5`, where the anchored search is still small enough for
local compiled replay.

## Pre-registration

Rows:

```text
n = 64, h = 5,
p = every admissible prime 1 mod 64 with 64^2 < p <= 26177,
plus p in {40961, 65537, 262337}.
```

Object:

```text
anchored same-signature h=5 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_4, unequal e_5, and disjoint supports.
```

Success evidence:

- the compiled replay checks all `binom(63,4)` anchored left subsets and all
  `binom(63,5)` right subsets for every selected prime;
- the positive result sought is zero anchored nontoral trades;
- a nonzero count is banked as a falsifier for h=5 emptiness evidence, while
  still checking whether the direct `n^3` floor is exceeded.

## Result

The default replay covers the base `15`-row bank and completed locally in
`56.08s` with peak RSS below 90 MB.  Seven explicit prefix chunks cover the
remaining admissible primes through `26177`.  The `12289` chunks completed in
`44.94s` and `48.75s`; the `20353` chunks completed in `36.73s`, `36.66s`,
and `25.98s`; the `23873` chunk completed in `47.09s`; the `26177` chunk
completed in `36.51s`.  For every listed prime:

```text
left anchored subsets   = binom(63,4) = 595665
right probe subsets     = binom(63,5) = 7028847
anchored toral trades   = 0
anchored nontoral trades= 0
partial                 = false
direct n^3 alarm        = false
```

Thus the h=5 no-primitive evidence now has `81` complete `n=64` rows in
addition to the expanded `402`-row `n=32` bank.  In particular, every admissible
`n=64` prime through `26177` is certified.  The combined replay processes
`569,336,607` total right-side subsets.  This remains finite-row evidence, not
a uniform h=5 theorem.

## Replay

Single-prime timing gate:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py 4289
```

Full default replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
```

Prefix chunks:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_b.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_b.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_c.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_23873_chunk_a.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_26177_chunk_a.py
```

Expected digest after a successful complete replay:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
H5_N64_PREFIX_12289_CHUNK_A_PASS
H5_N64_PREFIX_12289_CHUNK_B_PASS
H5_N64_PREFIX_20353_CHUNK_A_PASS
H5_N64_PREFIX_20353_CHUNK_B_PASS
H5_N64_PREFIX_20353_CHUNK_C_PASS
H5_N64_PREFIX_23873_CHUNK_A_PASS
H5_N64_PREFIX_26177_CHUNK_A_PASS
```

The replays write:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_12289_chunk_b.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_b.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_20353_chunk_c.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_23873_chunk_a.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_prefix_26177_chunk_a.json
```
