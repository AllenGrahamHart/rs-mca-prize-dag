# Proof

The residual star-graph theorem gives two disjoint complete tripartite
graphs with three deck-pair parts of size two. Fix a source label `k`.
The regular cubic incidence and the cross-edge law say that the two points
of `psi^(-1)(alpha_k)` contribute two opposite edges between two of the
three deck-pair parts in one six-label component. Write `U_k` for their
four endpoints and `P_k` for the omitted deck pair. Thus

```text
component(k)=U_k disjoint_union P_k,       |U_k|=4, |P_k|=2.    (1)
```

This description retains the relative second-endpoint projective twist:
it does not yet identify `P_k` with the first-coordinate pair containing
`k`.

Now apply the common-five outgoing-fiber pin. It supplies a set
`K subset I` of size five. At either point over any `alpha_k`, `k in K`,
the whole outgoing factor has horizontal roots exactly `I^c`. The cubic
component divides that factor, so both of its star pairs lie in `I^c`.
Hence

```text
U_k subset I^c.                                      (2)
```

But `k in K subset I`, so `k notin U_k`. The label `k` and the four
horizontal roots in `U_k` lie over the same pole of the common outer
function, hence belong to the same six-label component of `G`. Equation
`(1)` therefore forces `k in P_k`. Every vertex of one part in
`K_(2,2,2)` has as its neighborhood the four vertices in the other two
parts, so `U_k=N_G(k)`. Together with `(2)` this proves `(KB3F-2)` without
assuming that the relative endpoint twist is the identity.

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
