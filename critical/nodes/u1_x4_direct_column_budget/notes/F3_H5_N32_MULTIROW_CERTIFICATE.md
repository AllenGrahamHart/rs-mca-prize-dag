# F3 h=5 n=32 multirow certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATES.

This note strengthens the h=5 side of the h=4/h=5 bonus item.  The existing
artifact had one full `n=32,h=5,p=1153` zero row, then seven selected rows.
This replay now checks a contiguous low-prime prefix plus the original high
selected rows in the `p >= n^2` regime.

## Scope

Rows:

```text
n = 32, h = 5,
p = every admissible prime 1 mod 32 with 32^2 < p <= 8161,
plus p in {12289, 32801, 40961, 61441, 65537}.
```

Object:

```text
anchored same-signature h=5 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_4, unequal e_5, and disjoint supports.
```

This matches the anchored probe convention in
`experiments/u1_x4_active_core_budget_probe.py`.

## Result

For every listed prime:

```text
left anchored subsets   = binom(31,4) = 31465
right probe subsets     = binom(31,5) = 169911
anchored toral trades   = 0
anchored nontoral trades= 0
partial                 = false
```

Thus the h=5 no-primitive evidence at `n=32` now covers `56` complete
`p >= n^2` rows.  In particular, it is no longer only selected-row evidence at
the beginning of the row: every admissible prime through `8161` is certified.
The replay processes `9,515,016` total right-side subsets and completed locally
in `33.05s` in the banked run.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
```

Single-prime timing gate:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py 1153
```

Expected digest:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
```

The replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
```

## Catch

The companion h=8 verifier caught a signature-key packing issue: a fixed
11-bit shift is unsafe for primes larger than `2048`.  This h=5 verifier uses
the corrected generated-C++ rule

```text
BITS = ceil(log2 p).
```

The JSON certificate was generated after the fix.
