# F3 h=3 rich-curve reduced-condition compiler

Status: ARITHMETIC COMPILER WITH RC-RED SUPPLIED, NOT THE T1 THEOREM.

This packet isolates the exact coefficient-count arithmetic that would turn a
repaired h=3 rich-curve Stepanov lemma into a usable incidence bound.  It is
the analogue of the h=2 linear-system and degree steps.  The reduced-condition
gate is now supplied by `F3_H3_RICH_CURVE_LOGJET_REDUCTION.md`; the remaining
mathematical gate is nonvanishing (`RC-NV`).

## Pre-registration

Question:

```text
Using the proved log-jet reduced derivative condition count, what exact
inequalities are needed to force the rich-curve degree contradiction?
```

Success criterion:

- state the compiler using the denominator bound already proved;
- consume the proved reduced-condition constant;
- keep the missing nonvanishing gate explicit;
- verify the integer inequalities in deterministic parameter rows.

Failure criterion:

- the compiler uses a reduced-condition constant not supplied by replayed proof;
- the degree formula disagrees with `F3_H3_RICH_CURVE_DENOMINATOR_COMPILER.md`;
- a sample row marked admissible violates the coefficient or degree inequality.

## Reduced-condition input

Let `Z` be a family of repaired nondegenerate degree-2 rational signature
curves

```text
r_{z,i}(X) = P_{z,i}(X) / Q_{z,i}(X),       i=1,2,3,
```

with all constant-ratio, toral, and hyperbola-line degeneracies removed or
paid.

For integers `A,B,D >= 1`, use the auxiliary polynomial

```text
Phi(X,Y_1,Y_2,Y_3),        deg_X < A,       deg_{Y_i} < B.
```

The denominator compiler gives, for each curve `z`, a cleared substituted
polynomial of degree

```text
L(A,B,h) = (A - 1) + 6 h (B - 1).
```

The log-jet packet proves:

```text
RC-RED(13):
  For each curve z and derivative order j < D, after reducing by the
  three H-membership equations r_{z,i}(X)^h = 1, the j-th multiplicity
  condition is represented by at most 13 (A + D) independent linear
  coefficient conditions.
```

The sharper derivative-order profile is now also recorded:

```text
RC-RED-PROFILE:
  per repaired curve, all j<D reduced conditions are over-imposed by
  DA + 6D(D-1) linear coefficient conditions.
```

The rank audit `F3_H3_RICH_CURVE_NV_RANK_AUDIT.md` clarifies that the
nonvanishing gate should be proved as an image-rank statement, not as full
injectivity of the `A B^3` coefficient box.  The sufficient form is:

```text
RC-RANK:
  The cleared substitution map to the direct sum over Z has rank
  > 13 D (A + D) |Z|.
```

`RC-RANK` implies the required `RC-NV` conclusion because then the solution
space to the log-jet conditions cannot be contained in the substitution
kernel.  It remains false without the degeneracy repairs in the previous
packets.

Using `RC-RED-PROFILE`, the sharper sufficient rank target is:

```text
rank(S_Z) > (DA + 6D(D-1)) |Z|.
```

## Compiler

There are

```text
A B^3
```

coefficients.  Under `RC-RED(13)`, imposing multiplicity `D` on every point
of every curve in `Z` is forced by at most

```text
13 D (A + D) |Z|
```

linear conditions.  Therefore a nonzero auxiliary exists if

```text
13 D (A + D) |Z| < A B^3.                       (LS3)
```

Assuming `RC-RANK`/`RC-NV`, each curve contributes at most

```text
L(A,B,h) / D
```

points, since a nonzero polynomial of degree `L(A,B,h)` cannot have
multiplicity-`D` roots at more than `L(A,B,h)/D` distinct non-pole points.
Thus

```text
sum_{z in Z} T(z) < |Z| * L(A,B,h) / D.          (DEG3)
```

This is only an arithmetic compiler.  The hard T1 content is now exactly:

1. prove `RC-RANK`, hence `RC-NV`, after the degeneracy filters;
2. optimize `(A,B,D)` strongly enough that `(DEG3)` beats the F3 floor at the
   official rows.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py
```

Expected digest:

```text
H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS
```
