# F3 h=3 repeat loose rank-minor compiler

Status: PROVED ARITHMETIC/ALGEBRAIC REDUCTION, NOT A RANK THEOREM.

This packet turns the three loose nonvanishing gates into explicit
rank-minor avoidance statements.

## Setup

For each loose target, the Stepanov compiler gives a cleared substitution map
from the auxiliary coefficient space to `X`-polynomial coefficients over a
repaired family `Z` of parameter values.  The strong sufficient rank gate is

```text
rank(substitution over Z) > D(C+kD)|Z|.
```

Equivalently, it is enough to find a nonzero minor of size

```text
r = D(C+kD)|Z| + 1.
```

This is stronger than the exact nonvanishing requirement, but it is a concrete
algebraic target.

## Entry Degree

Every entry of the universal cleared substitution matrix is a polynomial in
the loose parameter variables.  For a target with `m` parameter variables,
parameter degree box `P`, subgroup degree box `B`, subgroup order `n`, and
degree-budget sum `S_total`, the entry parameter degree is bounded by

```text
E = m(P-1) + n(B-1)S_total.
```

Thus any `r x r` rank minor has total parameter degree at most

```text
r E.
```

## Sample Box

For the replayed sample box

```text
P=16, C=512, B=4, D=2, |Z|=1, n=32,
```

the compiler prints:

```text
generic:  r=1061, E=1470;
branch A: r=1057, E=2127;
branch B: r=1057, E=2319.
```

Each sample also has positive rank-capacity slack `L_X+1-r`.

## Remaining Theorem

The useful theorem statement is now:

```text
LOOSE-GEN-RANK-AVOID:
  after generic loose repairs, exhibit a rank-good minor that does not vanish
  on the generic two-parameter loose image over the row field.

LOOSE-A-RANK-AVOID and LOOSE-B-RANK-AVOID:
  the analogous one-parameter branch statements.
```

This packet only supplies the degree bounds for those bad-minor hypersurfaces.
It does not prove any such minor is nonzero on the actual parameter images.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_rank_minor_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_RANK_MINOR_COMPILER_PASS
```
