# DSP8 smooth-trace substar router

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_dsp8_joint_star_depth_pareto_compiler`,
  `f3_h3_dsp8_unit_trace_elliptic_curve_router`

Fix a retained target `t`. A generic unordered product representation
`{x,y}` has the injective vertex parameter

```text
r=xy,       x+y=1+r-t.
```

For two vertices with parameters `r,s`, the associated decorated cubic pair
has common unnormalized trace

```text
sigma_0=1+r+s-t
```

and common product `rs`. Its unit-product trace curve is nodal exactly when

```text
(1+r+s-t)^3=27rs.                                  (SSR1)
```

Consequently the graph of nodal edges on any fixed product fiber has maximum
degree at most three. Every product star of degree `d` therefore contains a
same-center smooth-trace substar of degree at least `max(d-3,0)`.

Applying this to the joint-star/depth Pareto packets gives:

```text
E       (P,R) corner       smooth leaves off A    smooth leaves on A
10,11   (29,8),(30,7)               2                      0
12,13   (31,6),(32,5)               3                      1
14,15   (33,4),(34,3)               4                      2
16      (35,2)                       5                      3.       (SSR2)
```

In particular, the preferred coordinate-minimal `(P,R)>=(35,2)` packet has
the original degree-eight/degree-six product stars and, at the same centers,
degree-five/degree-three substars whose trace cubics are smooth elliptic
curves.

Let `beta_E` be the lifted shifted product at a chosen star center and let
`r,s_i` be the distinguished root products for one of its smooth leaves. Put

```text
Delta_i=(1+r+s_i-beta_E)^3-27rs_i.                 (SSR3)
```

At the actual official row prime every `Delta_i` is nonzero. Hence the
product-star candidate ideal may be saturated by the product of the selected
`Delta_i` without losing an actual `(35,2)` survivor. This is a structural
candidate compression. It does not bound the number of smooth templates,
their prime divisors, or the quotient-weighted DSP8 moment.
