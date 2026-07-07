# OVERNIGHT LOG 2026-07-08

## 2026-07-08 initial entry

Stage: Terminal A, h=3 char-zero classification.

Banked pose: `critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_CLASSIFICATION.md`.

Current route: direct unit-circle proof using `e2 = product * conjugate(e1)`,
which should classify all distinct char-zero h=3 trades as toral `mu_3`
coset pairs. Exact checker written but not yet replayed.

Next step: run `f3_h3_char0_classification.py`, fix any exact-check failures,
then commit the banked theorem/checker.

## 2026-07-08 Terminal A core replay

Stage: A1--A4.

Banked claim: direct unit-circle proof classifies all char-zero h=3 trades as
toral `mu_3` coset pairs. Exact checker replays in about two seconds and verifies
rows through `n=96`; the `n=96` row gives exactly `496 = binom(32,2)` char-zero
trades, all toral. The three banked finite-field norm-gate shapes at primes
`9601`, `13249`, and `18433` have both obstructions nonzero in `Q(zeta_96)` and
both obstructions zero modulo their activating prime.

Catch: the first checker implementation did repeated Sympy reductions inside
the pair loop and had to be interrupted after 60 seconds. The replay was repaired
by caching `X^e mod Phi_n` residues and grouping triples by exact `(e1,e2)`
signature before pairing.

Next step: add the requested node-candidate statement/proof files and commit the
stage.

