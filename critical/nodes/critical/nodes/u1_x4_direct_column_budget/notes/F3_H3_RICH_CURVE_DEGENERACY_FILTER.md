# F3 h=3 rich-curve constant-ratio degeneracy filter

Status: PROVED ARITHMETIC FILTER, NOT A COMPLETE SIGNATURE-CURVE ENUMERATION.

This packet operationalizes the first exclusion surfaced by
`F3_H3_RICH_CURVE_DEGENERACY_AUDIT.md`.  It gives an exact finite-field test
for degree-2 rational maps whose `H`-membership conditions collapse or are
mutually incompatible because a ratio `r_i/r_j` is constant.

## Pre-registration

Question:

```text
Given rational maps r_i=P_i/Q_i, can we cheaply detect the constant-ratio
degeneracies that make the broad T1 rich-curve statement false?
```

Success criterion:

- implement an exact test for whether `r_i/r_j = lambda` in `F_p(X)`;
- classify `lambda in H` as a collapsed repeated condition;
- classify `lambda notin H` as an incompatible pair of conditions;
- verify the detector on polynomial and Mobius examples.

Failure criterion:

- a known collapsed example is missed;
- a shifted nonconstant-ratio example is incorrectly marked collapsed;
- an incompatible constant ratio still reports a positive incidence count.

## Filter

Represent `r_i=P_i/Q_i` with nonzero polynomials over `F_p`.  For a pair
`(i,j)`, compute whether

```text
P_i Q_j = lambda P_j Q_i
```

for some `lambda in F_p^*`.

Then:

- if `lambda in H`, the two membership conditions `r_i(X) in H` and
  `r_j(X) in H` are the same condition away from poles;
- if `lambda notin H`, the two membership conditions are incompatible away from
  poles, because `r_i/r_j` cannot equal a non-`H` constant when both values lie
  in `H`;
- if no such `lambda` exists, this filter is silent and the curve must be
  handled by the later hyperbola/Stepanov machinery.

This is only the first degeneracy guard.  It does not classify the toral
`mu_3` coset cell or the `3 | q-1` hyperbola line degenerations; those still
need the F3 signature-curve geometry.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py
```

Expected digest:

```text
H3_RICH_CURVE_DEGENERACY_FILTER_PASS
```
