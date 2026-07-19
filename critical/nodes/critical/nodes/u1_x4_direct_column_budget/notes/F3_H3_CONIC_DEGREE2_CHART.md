# F3 h=3 conic degree-2 chart

Status: PROVED BRIDGE-SIDE PARAMETRIZATION LEMMA, NOT `H3-ACT`.

This packet makes explicit a bridge input that was previously implicit in the
h=3 rich-curve route.  The h=3 same-fiber surface can be covered by degree-2
rational membership maps over the actual row field, without adjoining a cube
root.  This is the local geometric reason the `RC-RED` and `RC-RANK` packets
may work with degree-2 rational maps.

## Pre-registration

Question:

```text
Given a same-fiber conic
  G(u,v)=u^2+uv+v^2+a(u+v)+b=0
and one row-field point (u0,v0) on it, can the remaining same-fiber triples be
parametrized by rational maps U(t),V(t),W(t) of degree at most 2?
```

Success criterion:

- give explicit formulas over the base row field;
- prove `G(U(t),V(t))=0`;
- prove the third coordinate `W(t)=-a-U(t)-V(t)` has the same `e1,e2`;
- show the affine chart misses at most the vertical mate, which is the
  projective `t=infinity` value;
- keep this below the rank theorem and the activation-count theorem.

Failure criterion:

- require adjoining `omega`;
- silently include the degenerate hyperbola-line cell `a^2=3b`;
- claim that parametrizing one conic proves the row activation bound.

## Lemma

Let `K` be a field of characteristic not `3`, and let

```text
G(u,v)=u^2+uv+v^2+a(u+v)+b.
```

Assume `(u0,v0)` lies on `G=0`.  Put

```text
A0 = 2u0 + v0 + a,
B0 = u0 + 2v0 + a,
Q(t) = t^2 + t + 1.
```

For `Q(t) != 0`, define

```text
S(t) = -(A0 + B0 t) / Q(t),
U(t) = u0 + S(t),
V(t) = v0 + t S(t),
W(t) = -a - U(t) - V(t).
```

Then

```text
G(U(t),V(t)) = 0.
```

Moreover, if

```text
F0(T)=T^3+aT^2+bT,
```

then

```text
F0(U(t)) = F0(V(t)) = F0(W(t)).
```

Equivalently, `{U(t),V(t),W(t)}` is a same-`e1,e2` triple with

```text
e1 = -a,        e2 = b.
```

After clearing the denominator `Q(t)`, each of `U,V,W` has numerator degree at
most `2` and denominator degree `2`.  Therefore the three subgroup membership
conditions

```text
U(t), V(t), W(t) in H
```

are exactly of the degree-2 rational-map type consumed by the current
rich-curve compiler.

## Proof

Substitute the line through `(u0,v0)` with slope `t`:

```text
u = u0 + s,
v = v0 + t s.
```

Expanding `G(u,v)` gives

```text
G(u0+s,v0+ts)
  = G(u0,v0)
    + s[(2u0+v0+a) + t(u0+2v0+a)]
    + s^2(t^2+t+1).
```

The first term vanishes by hypothesis.  The second intersection point on this
line is therefore obtained by choosing

```text
s = -[(2u0+v0+a) + t(u0+2v0+a)] / (t^2+t+1),
```

which is the formula above.

For the third coordinate, set `W=-a-U-V`.  Then

```text
U+V+W = -a.
```

Also, using `G(U,V)=0`,

```text
UV + UW + VW
  = -U^2 - UV - V^2 - a(U+V)
  = b.
```

Thus `U,V,W` are the roots of

```text
T^3 + aT^2 + bT - UVW,
```

so they have the same value under `F0(T)=T^3+aT^2+bT`.

Finally, the possible point with `u=u0` and `v != v0` is the projective
`t=infinity` value.  It is

```text
(u0, -a-u0-v0),
```

which is again a row-field point on the conic.  Hence one affine chart plus
this projective value covers the conic points obtained from lines through the
base point.  The degenerate line cell `a^2=3b` remains the separately banked
hyperbola-line exception and should still be paid or excluded before applying
`RC-RANK`.

## Role in h=3

This lemma narrows the bridge statement.  Once an activated h=3 shape supplies
one row-field same-fiber point, the whole same-`e1,e2` conic can be placed in
the exact degree-2 rational-map class used by:

```text
F3_H3_RICH_CURVE_DENOMINATOR_COMPILER.md
F3_H3_RICH_CURVE_LOGJET_REDUCTION.md
F3_H3_RANK_AVOID_INTERFACE.md
```

It does not prove the rank-good minor avoidance theorem, and it does not prove
the geometric batching/rank-capacity bound.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_degree2_chart.py
```

Expected digest:

```text
H3_CONIC_DEGREE2_CHART_PASS
```
