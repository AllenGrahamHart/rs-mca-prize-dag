# F3 h=3 rich-curve logarithmic jet reduction

Status: PROVED REDUCED-CONDITION GATE, NOT THE RICH-CURVE THEOREM.

This packet discharges the coefficient-count side of the h=3 rich-curve
Stepanov route.  It proves an explicit reduced derivative condition bound for
degree-2 rational signature curves.  The remaining T1 gate is nonvanishing
(`RC-NV`) after the degeneracy filters.

## Pre-registration

Question:

```text
For r_i(X)=P_i(X)/Q_i(X), deg P_i, deg Q_i <= 2, can every multiplicity
condition for

    Phi(X, r_1(X)^h, r_2(X)^h, r_3(X)^h)

at points where r_i(X)^h=1 be over-imposed by O(A+D) coefficient conditions,
independently of B, h, and the number of incidence points?
```

Success criterion:

- give a symbolic reduction of the j-th derivative to a polynomial numerator
  of degree at most `(A-1)+12j`;
- convert this to an explicit `RC-RED(C_red)` constant;
- replay the jet identity over several finite fields and rational maps.

Failure criterion:

- the numerator degree grows with `hB`;
- poles, zeros, or `X=0` are silently counted as admissible subgroup points;
- a finite-field replay finds a jet identity mismatch.

## Logarithmic reduction

Fix one monomial

```text
m(X) = X^a prod_i r_i(X)^(h b_i),
0 <= a < A,     0 <= b_i < B.
```

Let

```text
S(X) = X prod_i P_i(X) Q_i(X).
```

At admissible points we have `X != 0`, no zero or pole of any `r_i`, and
`r_i(X)^h=1`.  Put

```text
L = m'/m
M = S L.
```

The polynomial `M` is explicit:

```text
M = a S/X
    + h sum_i b_i [S/(P_i Q_i)] (P_i' Q_i - P_i Q_i').
```

Define polynomials `W_j` by

```text
W_0 = 1,
W_{j+1} = S W_j' + (M - j S') W_j.
```

Then, by induction,

```text
S(X)^j m^(j)(X) = m(X) W_j(X)
```

away from zeros and poles.  Since `deg S <= 13` for degree-2 rational maps and
`deg M, deg S' <= deg S - 1`, the recurrence gives

```text
deg W_j <= j (deg S - 1) <= 12j.
```

At an admissible subgroup point, `r_i(X)^h=1`, so `m(X)=X^a`.  Thus the
j-th multiplicity condition is implied by the vanishing of the polynomial

```text
N_{a,b,j}(X) = X^a W_j(X),
```

whose degree is at most

```text
a + 12j <= (A-1) + 12(D-1)       for j < D.
```

For each fixed derivative order `j`, all coefficient conditions are therefore
contained in the coefficient vector of a polynomial of degree `< A + 12D`.
This over-imposes the pointwise vanishing conditions, but that is allowed in
the auxiliary-polynomial construction.

Keeping the derivative order instead of collapsing immediately to a uniform
constant gives the sharper exact profile

```text
sum_{j=0}^{D-1} (A+12j) = DA + 6D(D-1)
```

conditions per repaired curve.  The companion condition-profile packet records
this arithmetic strengthening for future budget optimizers.

## RC-RED constant

The reduction proves the gate

```text
RC-RED(13):
  For each repaired degree-2 signature curve and each derivative order j < D,
  the j-th multiplicity condition is represented by at most
  13 (A + D) linear coefficient conditions.
```

The constant `13` is deliberately conservative; it absorbs the `X` factor and
the six numerator/denominator factors in `S`.  It does not prove nonvanishing
of the resulting auxiliary polynomial.  `RC-NV` remains the h=3 rich-curve wall.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_logjet_reduction.py
```

Expected digest:

```text
H3_RICH_CURVE_LOGJET_REDUCTION_PASS
```
