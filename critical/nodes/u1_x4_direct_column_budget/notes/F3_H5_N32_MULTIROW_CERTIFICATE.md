# F3 h=5 n=32 multirow certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATES.

This note strengthens the h=5 side of the h=4/h=5 bonus item.  The existing
artifact had one full `n=32,h=5,p=1153` zero row.  This replay checks seven
complete `n=32,h=5` rows at boundary/smooth primes in the `p >= n^2` regime.

## Scope

Rows:

```text
n = 32, h = 5,
p in {1153, 3137, 12289, 32801, 40961, 61441, 65537}.
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

Thus the h=5 no-primitive evidence at `n=32` now covers seven complete
`p >= n^2` rows, including both boundary and smooth primes.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
```

Expected digest:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
```

The replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
```

