# F3 h=5 n=96 boundary certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATE.

This extends the h=5 finite-row evidence one scale beyond the `n=64` replay,
using only the first boundary prime.  It is intentionally a single-row probe:
the purpose is to test whether the anchored certificate remains local-light at
the next scale before launching wider prime ladders.

## Pre-registration

Row:

```text
n = 96, h = 5, p = 9601.
```

Object:

```text
anchored same-signature h=5 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_4, unequal e_5, and disjoint supports.
```

Success evidence:

- the compiled replay checks all `binom(95,4)` anchored left subsets and all
  `binom(95,5)` right subsets;
- the positive result sought is zero anchored nontoral trades;
- a nonzero count is banked as a falsifier for h=5 emptiness evidence, while
  still checking whether the direct `n^3` floor is exceeded.

## Result

The replay completed locally in 49 seconds with peak RSS about 152 MB.  It
checked the full anchored row:

```text
left anchored subsets   = binom(95,4) = 3183545
right probe subsets     = binom(95,5) = 57940519
anchored toral trades   = 0
anchored nontoral trades= 0
partial                 = false
direct n^3 alarm        = false
```

This extends the h=5 finite-row zero evidence to `n=96` at the first boundary
prime.  It is still finite evidence, not a uniform h=5 no-primitive theorem.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n96_boundary_certificate.py
```

Expected digest after a successful complete replay:

```text
H5_N96_BOUNDARY_CERTIFICATE_PASS
```

The replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n96_boundary_certificate.json
```
