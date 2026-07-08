# F3 T4 local replay audit

Status: REPLAY AUDIT, NOT A NEW GENERAL-N THEOREM.

This packet records the local verification state for T4 of
`notes/codex_briefs/F3_FLIP_20260708.md`, using only existing JSON
certificates and replay scripts.  No Modal job is launched by this audit.

## Replayed commands

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t4_residual_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_x83_triangular_norm_gate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

## Digests

```text
F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS
H5_X83_TRIANGULAR_NORM_GATE_PASS
H4_H5_BONUS_REDUCTION_PASS
H6_H8_BONUS_SWEEP_PASS
```

## Current T4 interpretation

The h=4 rigidity route is structurally banked:

```text
h4_terminal_dichotomy: PROVED
x83_uniform_square_shift_obstruction_gate: PROVED
```

Thus h=4 has no hidden third mechanism.  Its live residue is not a new
classification theorem; it is the explicit sparse norm-gate/certificate column
identified by the dichotomy.

The h=5 evidence is stronger than the original bonus note and is now compiled
by the residual frontier ledger:

```text
n=32 complete zero certificates: 402 primes, all admissible through p=65537
n=64 complete zero certificates: 179 primes, with 515 admissible primes still
      missing up to p=262337
n=96 boundary zero certificate: p=9601
n=128 complete zero certificates: 7 primes
total complete zero rows: 589
total audited right-side probes: 3,164,030,779
```

This is still row evidence plus proved structural gates, not a uniform h=5
no-primitive theorem.

For h=6 and h=7, the local aggregate replay verifies full anchored certificates
for the banked rows.  The h=6 extra sweep has one real nontoral row at
`p=4993`, but its count is `6`, far below the `n^3` direct-column budget, and
the existing square-lift analysis classifies it as a paid h=3 lift rather than
a primitive h=6 floor threat.

For h=8, six n=32 rows are complete and the n=64 x83 radius-three shell
certificates replay.  The remaining h=8 n=64 rows are still explicitly partial:

```text
boundary_n64_h8_p193
q3_n64_h8
```

## Residual T4 work

The next useful T4 work is therefore not another broad h=4 identity search.
The residuals are:

1. a symbolic h=5 norm-gate incompatibility theorem, or a maintainable
   certificate family replacing row evidence;
2. an h=8 n=64 non-antipodal x83 certifier/signature join that avoids the
   known oversized blind hash table;
3. if neither lands, a T5 dossier must state these exact residuals rather than
   claiming h=4..8 general-n closure.
