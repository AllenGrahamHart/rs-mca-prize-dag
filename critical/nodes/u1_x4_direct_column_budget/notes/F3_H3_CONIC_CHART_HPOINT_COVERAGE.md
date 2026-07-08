# F3 h=3 conic-chart H-point coverage

Status: PROVED BRIDGE-SIDE COVERAGE LEMMA, NOT `H3-ACT`.

This packet pins the relation between a same-`(e1,e2)` conic's ordered
`H`-triples and the affine rich-curve chart count.  The chart from
`F3_H3_CONIC_DEGREE2_CHART.md` covers every affine conic point except possibly
one vertical/projective point.  Therefore the rich-curve count for a chart
controls the local ordered triple count up to an additive `1`.

## Pre-registration

Question:

```text
If T_chart counts t with U(t),V(t),W(t) in H, how far can it be from the
ordered same-fiber triple count R(s1,s2)?
```

Success criterion:

- prove the chart covers all finite conic points except the vertical/projective
  mate;
- state the exact additive `<= 1` loss for ordered `H`-triples;
- replay the identity on finite subgroup rows;
- avoid folding this into a global `H3-ACT` proof.

Failure criterion:

- ignore poles of `Q(t)=t^2+t+1`;
- assume the base point is always represented at finite `t`;
- claim the additive point loss proves the rank-capacity batching theorem.

## Lemma

Let `K` be a field of characteristic not `2` or `3`, and let

```text
G(u,v)=u^2+uv+v^2+a(u+v)+b
```

be nondegenerate.  Let `(u0,v0)` be a `K`-point on `G=0`, and let
`U(t),V(t),W(t)` be the conic chart from
`F3_H3_CONIC_DEGREE2_CHART.md`.

For a finite subgroup `H <= K^*`, define

```text
T_chart =
  #{ t in K : Q(t) != 0, U(t),V(t),W(t) in H pairwise distinct },
Q(t)=t^2+t+1.
```

Let

```text
R =
  #{ (u,v,w) in H^3 :
       u,v,w pairwise distinct,
       u+v+w=-a,
       uv+uw+vw=b }.
```

Then

```text
R = T_chart + epsilon,       epsilon in {0,1}.
```

The possible missing point is the vertical/projective value

```text
(u0, v_inf, w_inf),
v_inf = -a-u0-v0,
w_inf = v0.
```

It contributes exactly when this ordered triple lies in `H^3`, is
pairwise-distinct, and is not already represented by a finite chart parameter.

## Proof

Let `(u,v)` be an affine point on `G=0`.

If `u != u0`, the line through `(u0,v0)` and `(u,v)` has finite slope

```text
t = (v-v0)/(u-u0).
```

Solving the line-conic intersection as in
`F3_H3_CONIC_DEGREE2_CHART.md` gives `Q(t) != 0` and recovers `(u,v)` as
`(U(t),V(t))`.  Thus every nonvertical affine point is represented by the
finite chart.

If `u=u0`, the equation `G(u0,v)=0` is a quadratic in `v` with one root `v0`.
The other root is

```text
v_inf = -a-u0-v0.
```

This is the projective `t=infinity` value of the line-through-point chart.  It
may coincide with the base point when the tangent is vertical.  In all cases it
accounts for at most one ordered triple.  Adding
`w=-a-u-v` gives the displayed `(u0,v_inf,w_inf)`.

Restricting to `H^3` and pairwise-distinct triples preserves this coverage
statement and gives the formula for `R`.

## Role in h=3

Together with the local fiber-count bridge, this identifies the exact local
loss between the chart incidence count and the ordered same-fiber triples:

```text
ordered triples R <= T_chart + 1.
```

This additive `1` per conic is small bridge bookkeeping.  It does not prove a
global bound on the number of conics or on total rank-capacity consumption.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_hpoint_coverage.py
```

Expected digest:

```text
H3_CONIC_CHART_HPOINT_COVERAGE_PASS
```
