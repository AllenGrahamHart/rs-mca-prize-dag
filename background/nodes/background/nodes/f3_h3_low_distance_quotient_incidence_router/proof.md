# Proof

Take one edge counted by `N_d(t)`, with canonically ordered endpoint pairs

```text
E={x,y},       F={u,v},       E<F,
```

and one ordered quotient representation

```text
(1-w)/(1-z)=t.
```

All roots differ from one because the shifted factors and the target are
nonzero. The common-product identity

```text
(1-x)(1-y)=(1-u)(1-v)
```

is linear in `v`. Solving it gives

```text
v=1-(1-x)(1-y)/(1-u)=(x+y-xy-u)/(1-u).
```

The quotient identity similarly gives `w=1-t(1-z)`. Hence the edge and
quotient representation determine one quadruple `(LQI1)` satisfying
`(LQI2)` and all four listed predicates.

Conversely, a quadruple satisfying those predicates reconstructs `v,w`, the
two canonically oriented endpoint pairs, their distance-`d` edge, and the
ordered quotient representation. The orientation conditions prevent exchange
duplication. These maps are inverse, proving `(LQI3)`. Summing the definition
`W(t)=2N_4(t)+N_6(t)` against `R(t)` proves `(LQI4)`.

For a generic distance-four edge, the proved cross-overlap router permits
exchanging endpoints and roots so that

```text
uv=-y,
x=(u^2-y)/(u(1-y)).                                 (1)
```

Choose the lexicographically first valid orientation `(1)` as the certificate
of the canonically oriented edge. Then `(u,y)` determines `x` and
`v=-y/u`. Its product target is

```text
t=(1-u)(1+y/u)=(1-u)(u+y)/u.
```

The quotient root `z` determines `w=1-t(1-z)`. Thus each generic record maps
injectively to `(LQI5)`; retaining the certificate choice and all original
predicates makes the map unambiguous.

For an antipodal edge, choose the canonical root `x` of its endpoint
`{x,-x}`. The distance-four router gives

```text
x^2=u+v-uv.
```

Solving for `v` yields the first equation in `(LQI6)`, and the common product
is `t=1-x^2`. Substitution into `w=1-t(1-z)` gives the final equation in
`(LQI6)`. Canonical choices again make the map injective. The antipodal and
generic lanes are disjoint, completing the router. QED.
