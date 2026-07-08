# F3 h=3 repeat-boundary support compiler

Status: PROVED ARITHMETIC COMPILER, SUPPORT THEOREM OPEN.

This packet combines the repeat-boundary line compiler, the q0 payment, the
fixed-fiber cap, and the `S_3` support quotient into one theorem interface.
It states exactly what remains to pay the repeat-entry residue in the moment
route.

## Dependency DAG

```text
moment identity
  -> repeat-residue boundary compiler
  -> repeat-boundary line compiler
      -> q0 cell payment
      -> fixed-fiber cap
      -> S3 support quotient
          -> support compiler
```

The open leaf is now a support theorem for quotient line parameters.

## Inputs

The repeat-residue boundary compiler proves

```text
repeat_residue <= 12 n B_line + 18 n^2.
```

The q0 packet pays the triple-repeat cell:

```text
B_q0 <= 132 n^(2/3).
```

The fixed-fiber packet proves that every nondegenerate line parameter has

```text
T_r <= 66 n^(2/3).
```

The support symmetry packet proves that the genuine non-q0 support is a union
of six-element `S_3` Mobius orbits:

```text
R_genuine = 6 R_orb.
```

## Compiler

Combining the inputs,

```text
B_line <= 132 n^(2/3) + 66 n^(2/3) R_genuine
       = 132 n^(2/3) + 396 n^(2/3) R_orb.
```

Therefore

```text
repeat_residue
  <= 1584 n^(5/3) + 4752 R_orb n^(5/3) + 18 n^2.
```

Consequently, any quotient-support theorem

```text
R_orb <= C n^beta
```

with

```text
beta < 4/3
```

pays the repeat residue subcubically:

```text
repeat_residue <= 4752 C n^(5/3+beta) + 1584 n^(5/3) + 18 n^2.
```

In particular, a linear quotient-support theorem `R_orb <= Cn` gives an
`O_C(n^(8/3))` repeat-residue bound.

## Role in h=3

This does not close the h=3 moment route.  It removes the bookkeeping ambiguity
from the repeat residue and identifies a concrete theorem target:

```text
H3-REPEAT-SUPPORT(beta,C):
  R_orb <= C n^beta for the genuine non-q0 repeat-boundary line support.
```

A proof of `H3-REPEAT-SUPPORT(beta,C)` with `beta < 4/3` can be inserted
directly into the moment compiler.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_support_compiler.py
```

Expected digest:

```text
H3_REPEAT_BOUNDARY_SUPPORT_COMPILER_PASS
```
