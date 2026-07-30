# Proof

Fix a generic pole `p` of `G`. On a regular orbit of `D_n=<u,v>`, the
fibers of the two reflection quotients are the two-element orbits of `u`
and `v`. Alternating these two matchings traverses one orbit of `uv`, of
length `n`. Their incidence graph is consequently the bipartite cycle
`C_(2n)`. In particular, when `n>=3`, the `n` neighborhoods of the `Z`
vertices are distinct unordered pairs of `Y` vertices.

Fix one `Z` value `z`, write its adjacent `Y` values as `y_0,y_1`, and let
`w,tau(w)` be the two endpoint labels above `z`. Choose one point `x` of
the reduced divisor `D_w=psi^*[w]`. The source cross-edge lemma writes

```text
star(x)={t,s},       star(bx)={tau(t),tau(s)},       (1)
```

where `t` lies over `y_0` and `s` lies over `y_1`.

Let `P,eta(P)` be the two points of the source normalization above `x`,
with `T`-coordinates `t,s`, and put `Q=c(P)`. The second endpoint lift
fixes `T`, sends `w` to `tau(w)`, commutes with `a`, and satisfies

```text
c eta c^(-1)=eta*a.                                (2)
```

Thus `Q` and `eta(Q)` have `T`-coordinates `t,tau(s)`: indeed
`eta(Q)=c eta a(P)`. Their `a`-translates have coordinates
`tau(t),s`. These are the two source-parameter fibers over
`D_(tau(w))`, so its stars are

```text
{t,tau(s)},       {tau(t),s}.                       (3)
```

Equations `(1)` and `(3)` are the four distinct edges between the two
endpoint pairs over `y_0,y_1`. Therefore every `Z` value contributes one
copy of `K_(2,2)`, with no repeated star.

For `n=3`, the three distinct `Z` neighborhoods are the three edges of a
triangle on the three `Y` values. There are two generic poles of `G`, so
the source-star graph is two disjoint copies of the two-point blow-up of a
triangle, namely `K_(2,2,2)`. For `n=6`, the six neighborhoods are the
edges of one six-cycle, giving the two-point blow-up of `C_6`.

The generic quotient fibers over all poles of `G` are disjoint and contain
all six poles of `F`. Their twelve endpoint preimages are all source labels.
The complete-source identity

```text
div(B)=psi^*(sum_i [alpha_i])
```

therefore says that the preceding divisors account for all 24 source
units. Every divisor is reduced, and the cycle neighborhoods are distinct,
so the 24 star vertices all have weight one. Each `Y` vertex has two cycle
neighbors; after replacing each base edge by `K_(2,2)`, each of its two
source labels has degree `2+2=4`, as required by the quartic rows
`q_i=H(alpha_i,X)`. The defect is

```text
sum_v binomial(1,2)=0.
```

This proves the asserted rigidity and also proves that the defect budget
alone has no remaining leverage. QED.
