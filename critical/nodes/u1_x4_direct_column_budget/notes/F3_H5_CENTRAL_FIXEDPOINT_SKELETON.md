# F3 h=5 central chart fixed-point skeleton

Status: SPARSE DEGREE SKELETON / ROUTE WARNING, NOT AN h=5 CLOSURE.

The central chart graph is compact, but applying conjugation back to the graph
and expanding the resulting fixed-point equations is not compact.  This packet
records a lightweight sparse profile so future work attacks the central chart
through the rational graph structure rather than by forming full expanded
fixed-point numerators.

## Setup

The central graph gives

```text
bar_l(10-j) = bar_l5 * P_j / (D_j * l5),    j=1,2,3,4.
```

Conjugating this relation and substituting the graph again gives four
fixed-point compatibility equations.  The compiler does not expand them.  It
tracks:

- the power of `l5` needed to clear graph denominators;
- the pre-cancellation term upper bound;
- top-variable and `bar_l5` degree bounds.

## Replayed Skeleton

```text
F1: l5 denominator power 9, pre-cancel terms <= 1,255,488,415,957, total degree <= 91
F2: l5 denominator power 8, pre-cancel terms <=    57,067,651,704, total degree <= 81
F3: l5 denominator power 7, pre-cancel terms <=     2,593,979,107, total degree <= 71
F4: l5 denominator power 6, pre-cancel terms <=       117,907,944, total degree <= 61
```

The graph itself has only `67` terms.  The fixed-point expansion is therefore
the wrong primitive object to manipulate directly.

## Consequence

The central h=5 chart should be attacked as a structured rational graph with
conjugation/support compatibility, not as four fully expanded cleared
polynomials.  If resultants or Groebner-style eliminations are needed, they
should exploit the graph equations and saturations explicitly.

This packet does not prove that the central chart is empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_fixedpoint_skeleton.py
```

Expected digest:

```text
H5_CENTRAL_FIXEDPOINT_SKELETON_PASS
```
