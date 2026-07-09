# F3 h=3 repeat support crossover

Status: PROVED CONSTANT COMPILER, NOT A SUPPORT THEOREM.

This packet gives the exact official-row crossover table for linear quotient
support theorems of the form

```text
R_orb <= C n.
```

It uses the integer caps from the q0 and fixed-fiber packets:

```text
B_line <= ceil(132 n^(2/3)) + 6 floor(Cn) ceil(66 n^(2/3)).
```

Then it checks

```text
12 n B_line + 18 n^2 < n^3
```

on the official rows `n=2^13..2^41`.

## Crossover Table

```text
C=1/4: covers 2^31..2^41,
C=1/2: covers 2^34..2^41,
C=1:   covers 2^37..2^41,
C=2:   covers 2^40..2^41,
C=4:   covers no official tail.
```

These are exact for the replayed integer cap model and improve the older
conservative prose thresholds.

## Role in h=3

This packet does not prove a support theorem.  It gives a replayed constants
target for any future theorem bounding the quotient line support.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
```
