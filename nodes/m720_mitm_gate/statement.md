# m720_mitm_gate

- **status:** PROVED
- **closure:** proof

## Statement

The MITM scanner used for the `h in (6,20]` band correctly detects known
h=3,4,5 trade/census facts and distinguishes toral or paid cores from
non-toral active cores.

## Falsifier

A known small-h trade missed by the scanner, or a paid/toral calibration core
misclassified as an unpaid non-toral active core.

## Decomposition

This node is proved from:

- `m720_mitm_enumerator_soundness`;
- `m720_ground_truth_replay`.
