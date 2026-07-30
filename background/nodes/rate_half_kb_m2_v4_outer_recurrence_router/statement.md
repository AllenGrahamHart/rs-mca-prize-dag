# KoalaBear m2 V4 outer-recurrence router

- **status:** PROVED
- **scope:** the three residual actual KoalaBear `Q=6,s=6,u=2`, inner-degree-two transverse types
- **dependencies:** `rate_half_kb_source_pencil_rank_transverse_compiler`,
  `rate_half_kb_q6_u2_primitive_subdegree4_route_cut`, and the proved
  lower-degree routers
- **consumer:** `rate_half_band_closure`

Let `h` be a terminal separable degree-two right component, with deck
involution `tau`, and let

```text
Gamma -> C=(h x h)(Gamma)
```

be the actual bidegree-`(4,4)` component and its transverse outer image.
The map `h x h` is the quotient by

```text
V4=<tau x 1, 1 x tau>.
```

If `S` is the setwise stabilizer of `Gamma` in `V4`, then

```text
delta=deg(Gamma -> C)=|S|.
```

Consequently the three rows have the exact stabilizer forms

```text
(r,delta)=(2,4): S=V4;
(r,delta)=(4,2): S is one of the three order-two subgroups;
(r,delta)=(8,1): S=1.
```

The complete primitive degree-30 catalogue consists of
`PSL(2,29),PGL(2,29),A30,S30`, all with subdegrees `1,29`. Hence no outer
degree-30 map carrying any of `r=2,4,8` is indecomposable. A proper right
factor of outer degree `d in {2,3,5,6,10,15}` produces an endpoint inner
degree `2d in {4,6,10,12,20,30}`. The proved profile exclusions and routers
make every destination impossible or return it to inner degree two. Thus
the complete residual is a recurrent decomposable `m=2` tower; there is no
unclassified primitive outer case.

There is also an exact source-star refinement. If `tau x 1` stabilizes
`Gamma` (in particular, throughout `(r,delta)=(2,4)`), its lift to the
actual bidegree-`(2,4)` source component is

```text
(T,X) -> (tau(T),b(X)),
```

where `b` is the source deck involution. The lift with `X` fixed would put
the coefficient image in a line and is already excluded. If source labels
are paired by `i -> bar(i)`, then

```text
div(q_i) <= div(B/(z_i z_bar(i))),
star(bx)=tau(star(x)).
```

Every occupied fixed matching vertex has weight two. The weight-three
source-defect type is impossible, so only zero through three weight-two
vertices remain; the number of fixed matching vertices has the same parity
as the number of weight-two vertices.

This router does not delete any of the three `m=2` types. It proves no
parameter-to-carrier bridge, owner, charge, `u=2` close, adjacent
certificate, or prize row. The next leaf must break the recurrent tower
using the equivariant actual source/component equations or construct a
chronology-valid same-record owner.

## Falsifier

A component for which `delta` differs from its V4 stabilizer order, a
primitive degree-30 group with subdegree `2`, `4`, or `8`, a missing proper
factor destination, or a coordinate-stabilized source component violating
the printed lift or star-defect parity.
