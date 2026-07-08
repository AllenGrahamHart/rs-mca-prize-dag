# F3 h=6/7/8 bonus sweep status

Status: VERIFIED-AT-ROWS + FULL H6 N64 CERTIFICATE + H6 N64 EXTRA-PRIME
FALSIFIER ROW + SIX FULL H8 N32 CERTIFICATES + HONEST REMAINING H8 PARTIALS.
This is bonus item (ii) after Terminals A/B/C: sweep `h = 6,7,8` with the
ladder machinery.

This pass consolidates the existing Modal artifacts, adds one new complete
Modal-sharded h=6 n=64 certificate, and separates full certificates from
partial slices.

## Pre-registration

Success criterion for this pass:

- verify every existing full h=6/h=7 boundary/smooth row has zero anchored
  nontoral trades and no `n^3` alarm;
- verify the upgraded `n=32,h=8,p in {1153,3137,12289,40961,61441,65537}`
  complete anchored certificates;
- verify remaining h=8 rows are present but marked partial, with no alarm in
  the checked slices;
- state the next h=8 action without promoting partial evidence.

Failure criterion:

- if any full h=6/h=7 row has nonzero primitive residue or an `n^3` alarm, the
  sweep has found a bonus counterexample;
- if any remaining h=8 row is silently treated as full when it is partial, the
  handoff is invalid.

## Verified Rows

From `f3a1_results.json`:

```text
boundary_n32_h6_p1153_FULL  zero, full
boundary_n32_h7_p1153_FULL  zero, full
boundary_n32_h6_p3137       zero, full
boundary_n32_h7_p3137       zero, full
boundary_n32_h6_p12289      zero, full
```

From `f3a2_results.json`:

```text
smooth_n32_h6_p40961        zero, full
smooth_n32_h7_p40961        zero, full
smooth_n32_h6_p61441        zero, full
smooth_n32_h7_p61441        zero, full
smooth_n32_h6_p65537        zero, full
smooth_n32_h7_p65537        zero, full
```

New complete h=6 n=64 boundary row:

```text
boundary_n64_h6_p4289_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
```

The certificate is in `f3_h6_n64_boundary_certificate.json`; it is produced by
`f3_h6_n64_boundary_modal.py` and locally verified by
`f3_h6_n64_boundary_certificate.py`.

Extra complete h=6 n=64 prime sweep:

```text
boundary_n64_h6_p4481_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
boundary_n64_h6_p4673_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
boundary_n64_h6_p4801_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
boundary_n64_h6_p4993_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=6, partial=False,
                                    no n^3 alarm
boundary_n64_h6_p5441_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
boundary_n64_h6_p5569_SHARDED_CPP  complete anchored certificate:
                                    toral=0, nontoral=0, partial=False
```

The certificate is in `f3_h6_n64_extra_primes_certificate.json`; it is produced
by `F3_H6_N64_MODE=extra f3_h6_n64_boundary_modal.py` and locally verified by
`f3_h6_n64_extra_primes_certificate.py`.

Upgraded complete h=8 rows:

```text
boundary_n32_h8_p1153_FULL   complete anchored certificate:
                              toral=3, nontoral=0, partial=False
boundary_n32_h8_p3137_FULL   complete anchored certificate:
                              toral=3, nontoral=0, partial=False
boundary_n32_h8_p12289_FULL  complete anchored certificate:
                              toral=3, nontoral=0, partial=False
smooth_n32_h8_p40961         complete anchored certificate:
                              toral=3, nontoral=0, partial=False
smooth_n32_h8_p61441         complete anchored certificate:
                              toral=3, nontoral=0, partial=False
smooth_n32_h8_p65537         complete anchored certificate:
                              toral=3, nontoral=0, partial=False
```

The certificates are in `f3_h8_n32_full_certificate.json` and
`f3_h8_n32_multirow_certificate.json`; they are produced by
`f3_h8_n32_full_certificate.py` and `f3_h8_n32_multirow_certificate.py`.

Remaining h=8 partial rows:

```text
boundary_n64_h8_p193        zero in checked slice, partial=True
q3_n64_h8                   zero in checked slice, partial=True
```

## Interpretation

The h=6/h=7 rows mostly continue the pattern from the shallow ladder, but the
extra-prime h=6 n=64 sweep finds a real p-selected primitive residue at
`p=4993`.  This falsifies the stronger finite-row emptiness heuristic for h=6.
It does not threaten the direct-column floor: `6 << n^3 = 262144`, and the
correct h=6 target is now a small/budgeted norm-gate accident statement rather
than universal emptiness.  The n=32 h=8 boundary rows meet the same complete
anchored standard at six primes.  The n=64 h=8 rows do not yet meet that
standard because the runs were sliced by the 60-second Modal budget.

Next h=8 action:

```text
replace the remaining n=64 partial W-window runs by shard-complete anchor
certificates, or use the x83 square-shift certifier keys to reduce h=8 to
explicit norm-gate keys.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.py
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
F3_H6_N64_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
```

Expected digest:

```text
H6_H8_BONUS_SWEEP_PASS
H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H6_N64_EXTRA_PRIMES_SWEEP_VERIFY_PASS
H6_N64_BOUNDARY_CERTIFICATE_PASS
H6_N64_EXTRA_PRIMES_SWEEP_DONE
```
