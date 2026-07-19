# F3 h=6/7/8 bonus sweep status

Status: VERIFIED-AT-ROWS + FULL H6 N64 CERTIFICATE + H6 N64 EXTRA-PRIME
FALSIFIER ROW + FULL H7 N64 CERTIFICATE + SIX FULL H8 N32 CERTIFICATES +
H8 N64 X83 RADIUS-THREE SHELL + HONEST REMAINING H8 PARTIALS.  This is bonus
item (ii) after Terminals A/B/C: sweep `h = 6,7,8` with the ladder machinery.

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

New complete h=7 n=64 boundary row:

```text
boundary_n64_h7_p4289_RANK_SHARDED_CPP  complete anchored certificate:
                                         toral=0, nontoral=0, partial=False
```

The certificate is in `f3_h7_n64_boundary_certificate.json`; it is produced by
`F3_H7_N64_MODE=full f3_h7_n64_timing_gate_modal.py` and locally verified by
`f3_h7_n64_boundary_certificate.py`.

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

Square-lift h=8 n=64 structural probe:

```text
p=193     h4 quotient branch: total=15, toral=7, nontoral=8
p=262337  h4 quotient branch: total=7,  toral=7, nontoral=0
```

The probe is in `f3_h8_n64_square_lift_probe.py`.  It does not certify the
non-antipodal h=8 branch, but it shows that the `q3_n64_h8` antipodal
square-lift branch is clean after the h=4 quotient ledger.

X83 h=8 n=64 obstruction interface:

```text
p=193     lifted h8 branch: total=15, toral=7, x83_zero=15
p=4289    lifted h8 branch: total=7,  toral=7, x83_zero=7
p=262337  lifted h8 branch: total=7,  toral=7, x83_zero=7
p=4289    non-antipodal sample: 4096 supports, full_zero=0
p=262337  non-antipodal sample: 4096 supports, full_zero=0
```

The interface check is in `f3_h8_n64_x83_obstruction_interface.py`.  It aligns
the paid antipodal branch with the x83 forced-root obstruction vector and gives
the exact key format for a later non-antipodal sharded certifier.  It is a
sampled structural interface check, not a full certificate.

X83 one-exchange shell around paid h=8 n=64 lifts:

```text
p=4289    paid supports=7, shell supports=5376, full_zero=0
p=262337  paid supports=7, shell supports=5376, full_zero=0
p=4289    radius-2 shell supports=947520, full_zero=0
p=262337  radius-2 shell supports=947520, full_zero=0
p=4289    radius-3 shell preimages=67800320, first_obstruction_zero=16048,
          full_zero=0, max_shard_elapsed=24.970s
p=262337  radius-3 shell preimages=67800320, first_obstruction_zero=320,
          full_zero=0, max_shard_elapsed=28.446s
p=262337  radius-3 suffix profile=[67800000,320,0,0,0,0,0,0]
```

The radius-one and radius-two shell check is in
`f3_h8_n64_x83_nearlift_shell.py`.  The radius-three shell certificate is in
`f3_h8_n64_x83_radius3_shell_certificate.json`; it is produced by
`f3_h8_n64_x83_radius3_modal.py` and locally verified by
`f3_h8_n64_x83_radius3_certificate.py`; the boundary-style replay at `p=4289`
is stored separately as `f3_h8_n64_x83_radius3_shell_certificate_p4289.json`.
The q3 suffix profile is stored in `f3_h8_n64_x83_radius3_profile_q3.json` and
verified by `f3_h8_n64_x83_radius3_profile.py`.
These are adversarial local falsification attempts; they do not rule out farther
non-antipodal primitive supports.

## Interpretation

The h=6/h=7 rows mostly continue the pattern from the shallow ladder, but the
extra-prime h=6 n=64 sweep finds a real p-selected anchored-nontoral residue at
`p=4993` under the coarse toral-only classifier.  The follow-up
`f3_h6_p4993_square_lift_analysis.py` verifier classifies all six witnesses as
antipodal square-lifts of the complete h=3 anchored trade set on `mu_32` at the
same prime.  Thus the row falsifies crude h=6 toral-only emptiness, but not the
fully stripped primitive h=6 column.  It also does not threaten the
direct-column floor: `6 << n^3 = 262144`.  The h=7 n=64 boundary row now meets
the complete anchored standard as well.  The n=32 h=8 boundary rows meet the
same complete anchored standard at six primes.  The n=64 h=8 rows do not yet
meet that standard because the runs were sliced by the 60-second Modal budget.
The x83 interface now proves that the already-paid antipodal square-lift branch
is seen by the obstruction keys; any remaining h=8 n=64 obstruction must be a
non-antipodal primitive support or a p-specific norm-gate event isolated by the
same forced-root key.  The first non-antipodal exchange shell around the paid
lifts, the radius-two shell around them, and the radius-three shell at both
`p=4289` and the actual `q3_n64_h8` prime have also been exhausted with zero
x83 full-zero supports.

Next h=8 action:

```text
do not launch a blind all-left-hash h=8 n=64 certificate; the left table alone
is about 16.5 GiB at 32 bytes/record.  Use the x83 square-shift certifier keys,
starting from the obstruction vector replayed here, or design a true
external/sharded signature join.  h=7 n=64 is already complete at the boundary
prime.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_p4993_square_lift_analysis.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h7_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_square_lift_probe.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_obstruction_interface.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=4289 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
F3_H8_X83_SHELL_RADIUS=2 F3_H8_X83_SHELL_PRIMES=262337 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_certificate.py
F3_H8_RADIUS3_CERT=f3_h8_n64_x83_radius3_shell_certificate_p4289.json \
  F3_H8_RADIUS3_EXPECTED_PRIMES=4289 \
  python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_profile.py
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
F3_H6_N64_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
F3_H7_N64_MODE=full ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h7_n64_timing_gate_modal.py
F3_H8_RADIUS3_MODE=full F3_H8_RADIUS3_PRIMES=262337 \
  ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_modal.py
F3_H8_RADIUS3_MODE=full F3_H8_RADIUS3_PRIMES=4289 \
  F3_H8_RADIUS3_OUT=f3_h8_n64_x83_radius3_shell_certificate_p4289.json \
  ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_modal.py
F3_H8_RADIUS3_MODE=full F3_H8_RADIUS3_PRIMES=262337 \
  F3_H8_RADIUS3_PROFILE=1 \
  F3_H8_RADIUS3_OUT=f3_h8_n64_x83_radius3_profile_q3.json \
  ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_modal.py
```

Expected digest:

```text
H6_H8_BONUS_SWEEP_PASS
H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H6_N64_EXTRA_PRIMES_SWEEP_VERIFY_PASS
H6_P4993_SQUARE_LIFT_ANALYSIS_PASS
H7_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H8_N64_SQUARE_LIFT_PROBE_PASS
H8_N64_X83_INTERFACE_PASS
H8_N64_X83_NEARLIFT_SHELL_PASS
H8_N64_X83_NEARLIFT_RADIUS2_PASS
H8_N64_X83_RADIUS3_CERTIFICATE_PASS
H8_N64_X83_RADIUS3_PROFILE_PASS
H6_N64_BOUNDARY_CERTIFICATE_PASS
H6_N64_EXTRA_PRIMES_SWEEP_DONE
H7_N64_BOUNDARY_CERTIFICATE_PASS
H8_N64_X83_RADIUS3_SHELL_PASS
```
