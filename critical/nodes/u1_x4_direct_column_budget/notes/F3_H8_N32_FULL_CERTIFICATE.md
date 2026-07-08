# F3 h=8 n=32 full anchored certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATES.

This note upgrades the smallest h=8 partial row from
`F3_H6_H8_BONUS_SWEEP.md`:

```text
boundary_n32_h8_p1153_FULL
```

The old Modal artifact had `partial=True`; the new replay is a complete
anchored MITM certificate for the same row.  A multirow replay extends the same
certificate to boundary primes `p=3137` and `p=12289`.

## Scope

Base row:

```text
n = 32, h = 8, p = 1153, W = 32.
```

Extended rows:

```text
n = 32, h = 8, p in {1153, 3137, 12289}, W = 32.
```

Object:

```text
anchored same-signature h=8 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_7, unequal e_8, and disjoint supports.
```

This matches the anchored probe convention in
`experiments/u1_x4_active_core_budget_probe.py`.

## Result

Complete enumeration:

```text
left anchored subsets   = binom(31,7) = 2629575
right probe subsets     = binom(31,8) = 7888725
anchored toral trades   = 3
anchored nontoral trades= 0
partial                 = false
```

Thus the previous h=8 `n=32,p=1153` partial zero slice is upgraded to a full
zero anchored nontoral certificate.  The three toral anchored trades are paid
`mu_8` coset trades.

The multirow replay gives the same result at `p=3137` and `p=12289`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_full_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_multirow_certificate.py
```

Expected digest:

```text
H8_N32_FULL_CERTIFICATE_PASS
H8_N32_MULTIROW_CERTIFICATE_PASS
```

The replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_full_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_multirow_certificate.json
```
