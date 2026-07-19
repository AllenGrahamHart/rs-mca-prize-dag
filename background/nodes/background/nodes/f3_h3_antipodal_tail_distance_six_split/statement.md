# H3 antipodal-tail distance-six split

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_high_excess_distance_six_moment_reduction`,
  `f3_h3_distance_four_fiber_degree_cap`,
  `f3_h3_low_distance_quotient_incidence_router`

Partition the selected targets `t!=1`, `P(t)>=33` according to whether their
squared-norm-at-most-three representation fiber contains its unique possible
antipodal pair. Put

```text
M_6,33^0=sum_(t antipodal-free) N_6(t)R(t),
M_6,33^A=sum_(t antipodal)      N_6(t)R(t).              (A6S1)
```

Every antipodal-free target satisfies the stronger pointwise estimate

```text
P(t)-18 <=(16/53)N_6(t).                                (A6S2)
```

The antipodal targets retain the proved uniform estimate
`P(t)-18<=(8/21)N_6(t)`. Consequently, writing

```text
B_n=300n^2-238(n-1)(n-2),
```

the weighted moment bound

```text
136(42M_6,33^0+53M_6,33^A)<=1113B_n                    (A6S3)
```

implies C36'. A conservative sufficient form is

```text
M_6,33^0+(53/42)M_6,33^A <=(1643/136)n^2 <12.081n^2.  (A6S4)
```

The expensive antipodal part has an additional exact membership equation.
Fix the canonical sign `x` of its unique antipodal representation `{x,-x}`.
Let `J_6^A` consist of quadruples

```text
(x,u,a,z) in (H\{1})^4                                  (A6S5)
```

for which, with

```text
t=1-x^2,
v=(x^2-u)/(1-u),
b=(x^2-a)/(1-a),
w=x^2+(1-x^2)z,                                         (A6S6)
```

the three derived values `v,b,w` lie in `H\{1}`, the pairs `{u,v}` and
`{a,b}` satisfy the canonical pair/edge orientations and have squared
distance six, and all original small-vector, nonidentity, and `P(t)>=33`
conditions hold. Then

```text
|J_6^A|=M_6,33^A.                                       (A6S7)
```

Thus the selected endpoint is a weighted sum of a four-variable/two-
membership antipodal-free incidence and a four-variable/three-membership
antipodal incidence. This theorem supplies no incidence estimate.

There are also two exact lower-cutoff analytic alternatives. For
`E in {6,10}`, put

```text
B_(n,E)=300n^2-17E(n-1)(n-2),
M_6,q^0=sum_(t antipodal-free,P(t)>=q)N_6(t)R(t),
M_6,q^A=sum_(t antipodal,P(t)>=q)     N_6(t)R(t).
```

Either one of

```text
4(10M_6,25^0+17M_6,25^A)<=5B_(n,6),                (A6S8)
17(8M_6,29^0+11M_6,29^A)<=22B_(n,10)               (A6S9)
```

also implies C36'. Conservative sufficient forms are

```text
M_6,25^0+(17/10)M_6,25^A <=(99/4)n^2,              (A6S10)
M_6,29^0+(11/8)M_6,29^A <=(715/34)n^2.             (A6S11)
```

These are Pareto alternatives: they have larger moment allowances but weaker
richness filters and lower multistar degree. They do not supersede the
selected `E=14` interface for fixed-order candidate generation.
