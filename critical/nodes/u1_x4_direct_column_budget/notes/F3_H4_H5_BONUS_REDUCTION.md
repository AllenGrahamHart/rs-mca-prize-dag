# F3 h=4/h=5 bonus reduction status

Status: PROVED REDUCTION + VERIFIED ROW EVIDENCE.  This is the first bonus
queue item after Terminals A, B, and C.  It does not prove the full h=5
no-primitive theorem; it records exactly what is already proved in the DAG and
what remains.

## Pre-registration

Bonus item:

```text
prove the h=4/5 emptiness (the pullback classification + no-primitive theorem
the data supports)
```

Success criterion for this pass:

- identify the already-proved h=4/h-uniform structural theorems in `dag.json`;
- verify the row evidence that h=4/h=5 primitive residue vanishes in the
  q >= n^2 test rows while the positive-control gate still detects trades;
- state the exact remaining h=5 no-primitive certificate without promoting it.

Failure criterion:

- if any required DAG theorem is not `PROVED`, or if the row evidence loses its
  positive control / zero-residue rows, do not use this reduction.

## Already-Proved Structural Inputs

The current DAG already contains the h=4 pullback/no-third-mechanism theorem:

```text
h4_terminal_dichotomy: PROVED
```

For `n=2^s`, odd characteristic, and disjoint 4-subsets `P,Q` with equal
top-three elementary symmetric sums, the proved dichotomy is:

1. `Phi_n` divides the signed 8-sparse exponent word, so the trade is an
   antipodal quotient pullback under `X -> X^2` and descends to an h=2
   collision; this is paid by the quotient ledger.
2. Otherwise the prime divides the resultant `Res(Phi_n,f)`, an explicit
   top-level sparse norm-gate event.

Thus h=4 has no hidden third mechanism.  The remaining "emptiness" part is not
a structural classification problem; it is a per-row norm-gate exclusion or
certificate problem.

The h-uniform square-shift gate is also already proved:

```text
x83_uniform_square_shift_obstruction_gate: PROVED
```

It says every finite-row minimal h-trade is either a char-zero paid trade or a
p-specific norm-gate event detected by explicit low obstruction coefficients.
For h=5 over `n=2^s`, there is no `mu_5` full-fiber char-zero paid family, so
the live h=5 primitive branch is exactly the p-specific norm-gate certificate
branch.

## Verified Row Evidence

The existing boundary/smooth confinement artifacts plus the new compiled h=5
certificate give:

- positive control: `n=16,h=4,p=17` detects `60` nontoral trades;
- h=4 smooth/confined rows at `p=97,113,241,337` detect zero nontoral trades;
- h=5 smooth/confined rows at `p=97,113,241` detect zero nontoral trades;
- the boundary row `n=32,h=5,p=1153` detects zero nontoral trades in the
  original artifact;
- the compiled h=5 replay gives complete zero anchored nontoral certificates
  at `n=32,h=5` for
  `p in {1153,3137,12289,32801,40961,61441,65537}`;
- the compiled n=64 h=5 replay gives complete zero anchored nontoral
  certificates for
  `p in {4289,12289,40961,65537,262337}`;
- M720 separately replays the low-row h=5 gate `full_census(32,5,97)=96`,
  all non-toral, below the q >= n^2 regime.

This matches the intended theorem shape:

```text
q < n^2 can have h=5 norm-gate events;
q >= n^2 tested rows show no h=5 primitive residue.
```

## Remaining h=5 Certificate

The exact remaining no-primitive theorem should be posed as:

```text
For n=2^s and p = 1 mod n with p >= n^2, every h=5 finite-row minimal trade
is absent after paid pullback/char-zero branches; equivalently, every
square-shift obstruction norm-gate key from x83 is nonzero modulo p at the
official q >= n^2 rows.
```

A proof can be either:

- a symbolic norm lower/upper incompatibility showing no p >= n^2 can divide
  the h=5 obstruction norms in the relevant square-shift keys; or
- a replayable per-row certificate family using the x83 certifier keys.

Do not promote h=5 to `PROVED` from the current evidence alone.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
```

Expected digest:

```text
H4_H5_BONUS_REDUCTION_PASS
H5_N32_MULTIROW_CERTIFICATE_PASS
H5_N64_MULTIROW_CERTIFICATE_PASS
```
