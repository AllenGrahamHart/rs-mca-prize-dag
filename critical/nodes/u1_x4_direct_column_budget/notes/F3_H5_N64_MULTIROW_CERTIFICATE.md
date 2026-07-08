# F3 h=5 n=64 multirow certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATES.

This is a follow-up to the h=5 n=32 compiled certificate.  It tests the next
power-of-two row at `h=5`, where the anchored search is still small enough for
local compiled replay.

## Pre-registration

Rows:

```text
n = 64, h = 5,
p = every admissible prime 1 mod 64 with 64^2 < p <= 6337,
plus p in {12289, 40961, 65537, 262337}.
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

The full replay completed locally in `52.45s` with peak RSS below 90 MB.  For
every listed prime:

```text
left anchored subsets   = binom(63,4) = 595665
right probe subsets     = binom(63,5) = 7028847
anchored toral trades   = 0
anchored nontoral trades= 0
partial                 = false
direct n^3 alarm        = false
```

Thus the h=5 no-primitive evidence now has `13` complete `n=64` rows in
addition to the expanded `56`-row `n=32` bank.  In particular, every admissible
`n=64` prime through `6337` is certified.  This remains finite-row evidence,
not a uniform h=5 theorem.

## Replay

Single-prime timing gate:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py 4289
```

Full default replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
```

Expected digest after a successful complete replay:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
```

The full replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
```
