# Proof

The residual star-graph theorem gives two disjoint complete tripartite
graphs with three deck-pair parts of size two. Its universal dihedral
normalization is the non-diagonal cubic correspondence

```text
D_3(y)-D_3(z)=(y-z)(y^2+yz+z^2-3).
```

Fix a source label `k`. Its value `z=h(alpha_k)` is one root of the
cubic quotient fiber. The non-diagonal quadratic factor has the other two
cubic roots. Each has two source-deck lifts. The cross-edge law in the
star-graph theorem therefore says that the two points of
`psi^(-1)(alpha_k)` contribute the two opposite star edges between the
other two deck-pair parts. Their four endpoints are exactly `N_G(k)`.

Now apply the common-five outgoing-fiber pin. It supplies a set
`K subset I` of size five. At either point over any `alpha_k`, `k in K`,
the whole outgoing factor has horizontal roots exactly `I^c`. The cubic
component divides that factor, so both of its star pairs lie in `I^c`.
Taking their union gives `(KB3F-2)`.

If `k,k'` were adjacent vertices of `G` and both belonged to `K`, then
`k' in N_G(k) subset I^c`, contradicting `K subset I`. Hence `K` is
independent.

An independent set in a complete tripartite graph is contained in one part,
so has size at most two. Independent sets add across disjoint components,
and consequently

```text
alpha(K_(2,2,2) disjoint_union K_(2,2,2))=2+2=4.
```

This contradicts `|K|=5` and proves that no actual residual cubic component
exists. QED.
