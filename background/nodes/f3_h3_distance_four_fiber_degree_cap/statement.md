# H3 distance-four fiber-degree cap

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_distance_four_cross_overlap_router`

Fix one nonzero product target in an odd-characteristic dyadic row and consider
all its unordered representations whose half-basis coefficient vectors have
squared norm at most three. Call a representation **antipodal** when its roots
are `{x,-x}` and **generic** otherwise. Then:

1. every small antipodal representation has squared norm one, while every
   small generic representation has squared norm three;
2. the fiber has at most one antipodal representation;
3. every generic representation has at most three generic distance-four
   neighbors;
4. including the possible antipodal neighbor, every generic representation
   has distance-four degree at most four.
5. the generic distance-four graph admits an orientation of indegree at most
   one, and hence has at most `g` edges.

If the fiber has `g` generic representations and `a in {0,1}` antipodal
representations, its complete distance-four edge count satisfies

```text
N_4(t) <= g+ag.                                     (D4C1)
```

In particular, for nonempty total small-fiber size `m=g+a>=1`,

```text
N_4(t) <= 2(m-1).                                   (D4C2)
```

This is a fiberwise pseudoforest bound, stronger than applying the global
`(3n^2+n)/2` ledger or the maximum-degree-three envelope to one target. It
does not bound the quotient weight `R(t)`.
