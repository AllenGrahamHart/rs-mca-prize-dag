# F3 h=5 central chart graph

Status: SYMBOLIC COMPILER / CENTRAL-CHART REDUCTION, NOT AN h=5 CLOSURE.

This packet records the explicit graph form of the smallest h=5 reciprocal
chart.

## Central Chart

On the central chart

```text
bar_l5 != 0,
```

official conjugation also gives `l5 != 0`.  The four incident central minors
have the form

```text
Cj5 = bar_l5 * P_j(l5,l6,l7,l8,l9)
      - D_j * l5 * bar_l(10-j).
```

Thus each central equation is linear in exactly one noncentral conjugate
variable.  After saturating by `l5*bar_l5`, the central chart is the graph

```text
bar_l(10-j) = bar_l5 * P_j / (D_j * l5),    j=1,2,3,4.
```

## Replayed Rows

The compiler verifies:

```text
C15 solves bar_l9: D=16384, high terms=22, graph terms=23, graph degree=10
C25 solves bar_l8: D=16384, high terms=18, graph terms=19, graph degree=9
C35 solves bar_l7: D=256,   high terms=13, graph terms=14, graph degree=8
C45 solves bar_l6: D=512,   high terms=10, graph terms=11, graph degree=7
```

So the central chart residual is not a generic four-equation system in all
conjugate variables.  It is an explicit rational graph over
`l5,l6,l7,l8,l9,bar_l5`.

## Consequence

The smallest h=5 symbolic target is now:

```text
central chart graph
+ official support/locator constraints
+ conjugation compatibility
=> no official h=5 x83 survivor on bar_l5 != 0.
```

The graph form does not prove emptiness.  It identifies the next algebraic
object to attack: the fixed-point compatibility of this rational central
chart graph with conjugation and support in `mu_{2^s}`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_chart_graph.py
```

Expected digest:

```text
H5_CENTRAL_CHART_GRAPH_PASS
```
