# F3 h=3 conic-chart ratio guard

Status: PROVED BRIDGE-SIDE DEGENERACY GUARD, NOT `RC-RANK`.

This packet connects the field-rational conic chart to the existing
constant-ratio degeneracy filter.  Once the hyperbola-line cell `a^2=3b` is
excluded, the three chart membership maps `U(t),V(t),W(t)` have no constant
ratios.  Thus the constant-ratio degeneracy handled by
`F3_H3_RICH_CURVE_DEGENERACY_FILTER.md` cannot arise inside a repaired
nondegenerate same-fiber conic chart.

## Pre-registration

Question:

```text
For the conic chart U(t),V(t),W(t) from F3_H3_CONIC_DEGREE2_CHART.md, can
U/V, U/W, or V/W be constant after the hyperbola-line cell is excluded?
```

Success criterion:

- prove that a constant ratio would force the conic to lie in a line;
- use the existing nondegeneracy condition `a^2 != 3b`;
- replay exact polynomial ratio tests on finite fields;
- keep the result below `RC-RANK`.

Failure criterion:

- silently use the `omega`-split coordinates;
- claim all degeneracy cells are gone;
- add another default aggregate replay check while the aggregate is at the
  60 second cap.

## Lemma

Let `K` have characteristic not `2` or `3`, and let

```text
G(u,v)=u^2+uv+v^2+a(u+v)+b.
```

Assume:

```text
a^2 != 3b.
```

Let `(u0,v0)` be a `K`-point on `G=0`, and let `U(t),V(t),W(t)` be the chart
from `F3_H3_CONIC_DEGREE2_CHART.md`, with

```text
W(t)=-a-U(t)-V(t).
```

Then none of

```text
U(t)/V(t),   U(t)/W(t),   V(t)/W(t)
```

is constant in `K(t)`.

## Proof

The chart is the standard line-through-point parametrization of the conic.  Its
image contains a Zariski-dense subset of the projective conic `G=0`; in the
affine chart it misses only the projective `t=infinity` value.

If, for example, `U/V=lambda` in `K(t)`, then every point in the dense chart
image lies on the affine line

```text
u - lambda v = 0.
```

The irreducible conic must then have that line as a component.  Equivalently
the quadratic form is reducible into two lines over an algebraic closure.  But
`F3_H3_HYPERBOLA_LINE_DEGENERACY.md` identifies the reducible cell exactly as

```text
a^2 = 3b.
```

This contradicts the hypothesis.  The same argument applies to `U/W` and
`V/W`, because `W=-a-U-V`; a constant ratio with `W` places the dense conic
image on one affine line in the `(u,v)` plane.

Therefore the only same-fiber conic charts where a chart membership condition
can collapse with another by a constant ratio are contained in the already
excluded or separately paid hyperbola-line cell.

## Role in h=3

This sharpens the repaired h=3 bridge target:

```text
nondegenerate conic chart
  => degree-2 rational membership maps
  => no internal constant-ratio collapse among U,V,W.
```

The remaining h=3 proof debt is unchanged in kind: finite-row rank-good minor
avoidance and global rank-capacity batching still have to be proved.

## Replay

Standalone only, because the aggregate replay is already close to the laptop
60 second cap:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_ratio_guard.py
```

Expected digest:

```text
H3_CONIC_CHART_RATIO_GUARD_PASS
```
