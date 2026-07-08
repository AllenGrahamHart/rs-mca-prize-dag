# F3 h=5 certificate coverage audit

Status: AUDIT / MACHINE-CHECKED COVERAGE TABLE, NOT A UNIFORM h=5 THEOREM.

This packet records exactly what the existing h=5 finite certificates cover for
T4 of `notes/codex_briefs/F3_FLIP_20260708.md`.  It launches no new search.
The replay treats the banked JSON certificates as pinned data and checks their
internal consistency.

## Pre-registration

Question:

```text
Which h=5 rows are currently backed by complete zero certificates, and how much
prime coverage do those certificates actually give?
```

Success criterion:

- every listed certificate is internally complete;
- every top-level row has zero anchored toral and nontoral trades;
- every sharded n=128 row has all 32 shards, matching probe totals, and zero
  shard-level trades;
- every certified prime is actually prime, satisfies `p = 1 mod n`, and lies
  above `n^2`;
- the output distinguishes selected-row evidence from contiguous prime
  coverage or a uniform theorem.

Failure criterion:

- a JSON row marked complete has missing shards or nonzero trades;
- a certified prime is not in the `p = 1 mod n`, `p > n^2` row class;
- the audit silently upgrades selected finite evidence into a general h=5
  no-primitive theorem.

## Certified rows

The existing evidence consists of 530 complete zero rows:

```text
n=32:  all admissible primes p = 1 mod 32 with 32^2 < p <= 65537
n=64:  all admissible primes p = 1 mod 64 with 64^2 < p <= 38977,
       plus p in {40961, 65537, 262337}
n=96:  p = 9601
n=128: p in {17921, 18049, 18433, 19073, 19457, 19841, 20353}
```

Each row checks anchored same-signature h=5 trades with one side containing
exponent `0`, disjoint supports, equal `e_1..e_4`, and unequal `e_5`.  All 530
rows have

```text
anchored_toral_trades = 0
anchored_nontoral_trades = 0
direct_n3_exceeded = false
```

The n=128 rows are full 32-shard certificates with

```text
right probe subsets total = binom(127, 5) = 254231775
```

for each certified prime.

## Coverage interpretation

This is strong finite-row evidence for h=5 rigidity past the already-banked
structural gates.  It is not full contiguous prime coverage for every n and not
a uniform h=5 theorem.  The audit prints, for each n, the number of admissible primes
`p = 1 mod n` between `n^2` and the largest certified prime, and the number not
covered by the current selected certificates.

The current replay output is:

```text
 n  cert  first_p  max_p   admiss<=max  missing<=max  right_probes
 32   402     1153   65537          402            0      68304222
 64   120     4289  262337          694          574     843461640
 96     1     9601    9601            1            0      57940519
128     7    17921   20353            7            0    1779622425
```

Therefore the T4 h=5 residual remains exactly:

```text
prove a symbolic norm-gate/no-primitive theorem, or replace the selected rows
with a scalable certificate family covering the official row set.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Expected digests:

```text
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
H4_H5_BONUS_REDUCTION_PASS
```
