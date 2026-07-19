# H3 low-distance edge–quotient incidence router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_high_excess_low_distance_moment_reduction`,
  `f3_h3_distance_four_cross_overlap_router`

Fix one primitive order-`n` root and use its exponent order to orient every
unordered shifted-root pair and every unordered edge canonically. For
`d in {4,6}`, let `I_d` consist of quadruples

```text
(x,y,u,z) in (H\{1})^4                              (LQI1)
```

for which

```text
t=(1-x)(1-y),
v=(x+y-xy-u)/(1-u),
w=1-t(1-z),                                         (LQI2)
```

satisfy all of the following:

1. `v,w in H\{1}`;
2. `{x,y}` and `{u,v}` obey the canonical pair/edge orientation;
3. both half-basis coefficient vectors have squared norm at most three and
   their squared distance is `d`;
4. `t!=1` and `P(t)>=33`.

Then the correspondence between an edge and an ordered quotient
representation is exact:

```text
|I_d|=sum_(t!=1,P(t)>=33) N_d(t)R(t).               (LQI3)
```

Consequently the selected C36' moment target is

```text
M_33=2|I_4|+|I_6|.                                  (LQI4)
```

The distance-four part has two lower-dimensional covers. Every generic record
injects, after choosing its first canonical cross-overlap certificate, into
triples `(u,y,z) in H^3` satisfying

```text
x=(u^2-y)/(u(1-y)) in H,
t=(1-u)(u+y)/u,
w=1-t(1-z) in H.                                   (LQI5)
```

Every antipodal record injects, after choosing the canonical sign of `x`, into
triples `(x,u,z) in H^3` satisfying

```text
v=(x^2-u)/(1-u) in H,
t=1-x^2,
w=x^2+(1-x^2)z in H.                               (LQI6)
```

All original selection, orientation, `P(t)>=33`, and nonidentity conditions
remain in these covers. Thus distance four is a three-variable/two-membership
incidence, while generic distance six remains the four-variable system
`(LQI2)`. This theorem is an exact router and supplies no incidence estimate.
