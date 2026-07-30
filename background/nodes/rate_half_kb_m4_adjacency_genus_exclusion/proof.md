# Proof

## 1. The source genus and outer degree

The retained source theorem starts with an actual irreducible component
`Gamma_0` of bidegree `(u,2u)`. On the residual birational-quartic branch,
the quadratic base change has generic degree one on each deck-conjugate
component, so `Gamma_0` maps birationally to a bidegree-`(2u,2u)` component
`Gamma` of the endpoint self-correspondence. Here `u=2`. The normalization
of the `(2,4)` curve `Gamma_0` therefore has

```text
g(Gamma)=g(Gamma_0)<=p_a(Gamma_0)=(2-1)(4-1)=3.       (KBM4-G1)
```

For a terminal inner factor `h` of degree `m`, the transverse compiler puts
`C=(h x h)(Gamma)` and proves

```text
delta*r=4m,                                          (KBM4-G2)
```

where `delta=deg(Gamma->C)` and `C` has bidegree `(r,r)`. The proved
degree-four outer route leaves only `(m,r,delta)=(4,8,2)` and geometric
outer monodromy `A6` or `S6` in the degree-15 two-subset action.

## 2. The adjacency orbital

Fix a two-subset `A` of six letters. Its stabilizer has suborbits of sizes
`1,6,8`: the pair `A`, the six pairs disjoint from `A`, and the eight pairs
meeting `A` in one letter. Thus the `r=8` component is the adjacency
orbital

```text
Omega={(A,B): |A|=|B|=2, |A intersect B|=1}.
```

There are `15*8=120` ordered states. Direct generation by `A6` and by `S6`
shows that each acts transitively on `Omega`, so the associated orbital
cover is connected and is the normalization `C`, viewed over the target
line of the degree-15 map.

For a branch permutation `sigma` on the six letters, its action on `Omega`
is simultaneous transport of both pairs. Exact cycle enumeration gives

```text
letter type       cycles on Omega   index on Omega
6                       20                 100
5.1                     24                  96
4.2                     30                  90
3.2.1                   26                  94
2.1.1.1.1               72                  48
2.2.1.1                 60                  60
2.2.2                   60                  60.       (KBM4-G3)
```

The value depends only on cycle type. Summing `(KBM4-G3)` over the four
exhaustive passports gives total indices `244,250,246,264`. Since the cover
degree is 120, Riemann--Hurwitz

```text
2*g(C)-2=-2*120+sum index(sigma)
```

gives the four genera `3,6,4,13` printed in the statement.

## 3. Contradiction

The challenge characteristic is `p=2130706433`, so `p` does not divide the
degree `delta=2`. Hence `Gamma->C` is separable. Riemann--Hurwitz for this
map gives

```text
2*g(Gamma)-2 = 2*(2*g(C)-2)+deg(R) >= 2*(2*g(C)-2),
```

and therefore

```text
g(Gamma)>=2*g(C)-1.                                  (KBM4-G4)
```

The four lower bounds from `(KBM4-G4)` are `5,11,7,25`, all strictly above
the upper bound three in `(KBM4-G1)`. Every passport is impossible. Since
the passport parent is exhaustive, the `m=4` transverse row is empty. QED.
