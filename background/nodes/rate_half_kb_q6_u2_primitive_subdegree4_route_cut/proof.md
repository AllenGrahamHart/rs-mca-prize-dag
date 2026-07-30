# Proof

The retained source theorem constructs a separable degree-60 rational
endpoint map `f`. An actual outgoing component of bidegree `(u,2u)` maps to
a non-diagonal component of `f(T)=f(W)`. In the residual
birational-quartic branch the deck conjugate is a distinct component; the
quadratic base change therefore has generic degree one on each component.
The map is birational and its image has bidegree `(2u,2u)`. At `u=2` this is
`(4,4)`. The line branch is already excluded, and the conic branch is the
proved dependency, so every residual actual `u=2` component has this form.

Let `G` be the geometric monodromy group of `f` and fix one of its 60
sheets. Irreducible factors of `f(T)-f(W)` over the fixed-sheet function
field are indexed by point-stabilizer orbits; their degrees are the orbit
sizes. Thus a non-diagonal bidegree-`(4,4)` component forces subdegree four.

The complete primitive degree-60 catalogue contains nine groups. Their
point-stabilizer orbit multisets are exactly `(KBP-2)`, with multiplicities
two, three, and four. None contains four. Hence `G` is imprimitive. For a
separable rational map on `P^1`, imprimitive geometric monodromy is
equivalent, by the intermediate-field correspondence and Luroth's theorem,
to a nontrivial geometric functional decomposition

```text
f=F composed h,       deg(F) deg(h)=60.               (1)
```

It remains to enumerate the possible inner degree `m=deg(h)`. Put
`n=deg(F)=60/m`. Every pole of `f` has exact order five. If an outer pole has
order `r`, each point above it satisfies

```text
e_h r=5.
```

Hence `r` is one or five. If `F` has `a` order-five poles and `b` order-one
poles, then

```text
5a+b=n.                                               (2)
```

If `b>0`, then `5|m`; each such pole contributes `4m/5` to the ramification
of `h`, so Riemann-Hurwitz gives

```text
b(4m/5)<=2m-2.                                       (3)
```

Enumerating the proper divisors of 60 under `(2)--(3)` gives

```text
(m,n,a,b)=
(2,30,6,0), (3,20,4,0), (4,15,3,0), (5,12,2,2),
(6,10,2,0), (10,6,1,1), (12,5,1,0), (30,2,0,2).
```

The missing inner degrees 15 and 20 violate `(3)`. This proves `(KBP-3)` and
the route cut. QED.
