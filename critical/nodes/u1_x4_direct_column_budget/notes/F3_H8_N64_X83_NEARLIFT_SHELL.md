# F3 h=8 n=64 x83 near-lift shell

Status: MACHINE-VERIFIED ADVERSARIAL SHELL, NOT A FULL H8 CERTIFICATE.

This packet attacks the nearest non-antipodal neighborhoods of the paid h=8
square-lift branch.  Starting from every paid antipodal 16-support at the
boundary-style primes, remove `r` roots and insert `r` roots outside the
support.  The resulting support is `r` exchanges from a paid lift and is
typically non-antipodal.

## Pre-registration

Question:

```text
Are there any x83 full-zero h=8 supports one or two exchanges away from the
paid antipodal square-lift branch at the n=64 boundary-style primes?
```

Success criterion:

- enumerate the complete one-exchange shell around every paid lifted support at
  `p=4289` and `p=262337`, and the complete two-exchange shell prime-by-prime
  under the light-compute rule;
- compute the h=8 x83 obstruction vector for each shell support;
- find zero full obstruction vectors with nonzero square `lambda`.

Failure criterion:

- any full x83-zero shell support is a concrete primitive/norm-gate candidate
  and should be isolated as the next h=8 obstruction.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=4289 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=262337 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
```

Expected digests:

```text
H8_N64_X83_NEARLIFT_SHELL_PASS
H8_N64_X83_NEARLIFT_RADIUS2_PASS
```

## Result

The replay reports:

```text
p=4289 one-exchange shell: paid=7 supports=5376 full_zero=0 first_obstruction_zero=0
p=262337 one-exchange shell: paid=7 supports=5376 full_zero=0 first_obstruction_zero=0
H8_N64_X83_NEARLIFT_SHELL_PASS
p=4289 two-exchange shell: paid=7 supports=947520 full_zero=0 first_obstruction_zero=1504
H8_N64_X83_NEARLIFT_RADIUS2_PASS
p=262337 two-exchange shell: paid=7 supports=947520 full_zero=0 first_obstruction_zero=1344
H8_N64_X83_NEARLIFT_RADIUS2_PASS
```

The local verifier now treats these four rows as pinned expectations.  A
standalone radius-two replay for one prime remains under the local 60-second
cap, but the two radius-two prime replays are intentionally not part of the
default aggregate `f3_flip_interim_report_replay.py`; running both sequentially
would push that aggregate beyond the laptop-safe budget.

Interpretation:

This is a complete adversarial check of the radius-one and radius-two exchange
shells around the paid square-lift branch at the two boundary-style primes.  It
rules out the closest non-antipodal deformations of the paid h=8 supports.  It
does not rule out farther non-antipodal primitive supports, so the h=8 n64 rows
remain partial.
