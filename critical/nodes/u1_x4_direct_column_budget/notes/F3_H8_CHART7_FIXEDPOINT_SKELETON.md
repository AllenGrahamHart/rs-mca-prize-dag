# F3 h=8 chart-7 fixed-point skeleton

Status: SPARSE DEGREE SKELETON / ROUTE WARNING, NOT AN h=8 CLOSURE.

The chart-7 graph is compact, but applying conjugation back to the graph and
expanding the resulting fixed-point equations is not compact.  This packet
records sparse upper bounds without forming expanded fixed-point numerators.

## Setup

`F3_H8_CHART7_GRAPH_REDUCTION.md` gives the rational graph

```text
bar_c(16-j) = D7*bar_c9*P_j / (D_j*P7),   j=1,...,6
bar_c8      = D7*bar_c9*c8  / P7.
```

Conjugating these relations and substituting the same graph gives seven
fixed-point compatibility equations.  The compiler tracks:

- the power of `P7` needed to clear graph denominators;
- a pre-cancellation term upper bound;
- a total-degree upper bound.

It does not expand the fixed-point numerators.

## Replayed Skeleton

The conjugated high-part profiles are:

```text
Q1: P7 denominator power 15, pre-cancel terms <= 193739819866454614432080308483638
Q2: P7 denominator power 14, pre-cancel terms <=   1383854668464947616708824390613
Q3: P7 denominator power 13, pre-cancel terms <=      9884628736752300408065281673
Q4: P7 denominator power 12, pre-cancel terms <=        70604136603528584030836299
Q5: P7 denominator power 11, pre-cancel terms <=          504301112158780208566858
Q6: P7 denominator power 10, pre-cancel terms <=            3602046985214881055420
Q7: P7 denominator power 9,  pre-cancel terms <=              25724765024868437269
Q8: P7 denominator power 1,  pre-cancel terms <=                                 1
```

The seven fixed-point rows have:

```text
F1: common P7 power 15, pre-cancel terms <= 193755121556618651323524735233987, total degree <= 241
F2: common P7 power 14, pre-cancel terms <=   1384382312953362681931046002694, total degree <= 225
F3: common P7 power 13, pre-cancel terms <=      9902823374283854381245337262, total degree <= 209
F4: common P7 power 12, pre-cancel terms <=        71231537897720100347389940, total degree <= 193
F5: common P7 power 11, pre-cancel terms <=          525935639544694564310087, total degree <= 177
F6: common P7 power 10, pre-cancel terms <=            4348065170936065736221, total degree <= 161
F8: common P7 power 9,  pre-cancel terms <=              25724765525114850230, total degree <= 145
```

The chart graph itself has only `710` terms, so fully expanded fixed-point
compatibility is the wrong primitive.

## Consequence

The chart-7 h=8 target should be attacked as a structured rational graph with
conjugation/support compatibility and saturations, not by forming the cleared
fixed-point polynomials.  Any elimination or resultant route should preserve
the `P7`-denominator structure.

This packet does not prove the chart empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_chart7_fixedpoint_skeleton.py
```

Expected digest:

```text
H8_CHART7_FIXEDPOINT_SKELETON_PASS
```
