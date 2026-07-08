# F3 h=3 conic base-point equivalence

Status: PROVED BRIDGE-SIDE IMAGE LEMMA, NOT `RC-RANK` AND NOT `H3-ACT`.

This packet prevents a bridge bookkeeping error.  A same-`(e1,e2)` fiber can
contain many ordered triples, and each ordered triple can be used as a base
point for the degree-2 chart from `F3_H3_CONIC_DEGREE2_CHART.md`.  These are
not new geometric curve images.  They are different parametrizations of the
same nondegenerate conic.

## Pre-registration

Question:

```text
If two row-field base points lie on the same repaired h=3 same-fiber conic, do
their degree-2 charts recover the same conic image and the same ordered
H-triple fiber?
```

Success criterion:

- prove the projective chart image is independent of base point;
- prove the ordered `H`-triple ledger `R(s1,s2)` is independent of base point;
- state that finite affine chart counts can differ only by which point is the
  vertical/projective mate;
- avoid claiming Mobius reparametrization invariance for the rank theorem.

Failure criterion:

- charge one curve image per ordered triple rather than per same-fiber conic;
- treat this as a proof of the global bridge or of `RC-RANK`;
- ignore the hyperbola-line cell `a^2=3b`.

## Lemma

Let `K` be a field of characteristic not `2` or `3`, and let

```text
G(u,v)=u^2+uv+v^2+a(u+v)+b
```

be nondegenerate.  If `P0=(u0,v0)` and `P1=(u1,v1)` are two `K`-points on
`G=0`, then the two line-through-point charts from
`F3_H3_CONIC_DEGREE2_CHART.md` have the same projective image:

```text
image(chart from P0) union {vertical mate of P0}
 =
image(chart from P1) union {vertical mate of P1}
 =
{ (u,v) in K^2 : G(u,v)=0 }.
```

Consequently, for any finite subgroup `H <= K^*`, both charts recover the same
ordered same-fiber triple set

```text
R(s1,s2) =
  { (u,v,w) in H^3 :
      u,v,w pairwise distinct,
      u+v+w=s1,
      uv+uw+vw=s2 }.
```

Only the split between finite chart points and the one projective/vertical
point can depend on the selected base point.

## Proof

The conic-chart coverage lemma proves the displayed image identity for any
single `K`-point on the nondegenerate conic: every affine point not vertical
over the chosen base point is obtained from a finite slope, and the only
remaining affine point is the vertical mate.  Applying that lemma to `P0` and
to `P1` gives the same middle set `{G=0}`.  Adding `w=-a-u-v` then gives the
same ordered triple set after restricting to `H^3` and to pairwise-distinct
triples.

Thus an h=3 bridge may choose one deterministic base point for each nonempty
same-`(e1,e2)` conic fiber when doing incidence bookkeeping.  It should not pay
one geometric curve image per ordered triple in that fiber.

This lemma is not a rank theorem.  If a future `RC-RANK` proof is sensitive to
the exact rational parametrization rather than to the conic image, it must
either fix a deterministic base-point rule or separately prove the relevant
Mobius-reparametrization invariance.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_basepoint_equivalence.py
```

Expected digest:

```text
H3_CONIC_BASEPOINT_EQUIVALENCE_PASS
```
