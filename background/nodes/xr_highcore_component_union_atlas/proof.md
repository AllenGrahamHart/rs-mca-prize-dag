# Proof

Fix total orders on the slopes and on the live rays at each slope. Form the
finite graph `G` whose vertices are live slopes and whose cross-slope edges
are precisely the pairs admitting error sets `E,E'` with
`|E union E'|=R`. Its nonisolated vertices are `Z_high`.

For each nontrivial connected component `C`, root the lexicographic
breadth-first spanning tree at the least slope. For every tree edge, choose
the least witnessing ray pair. On the first tree edge retain both endpoint
rays. On every later parent-child edge retain only the child's witnessing
ray. This selects exactly one live ray at every slope of `C`: the root and
first child are covered by the first edge, and every other vertex occurs
once as a child. These deterministic choices define `U_C` as the union of
the selected error sets.

The two error sets retained from the first edge have union of size `R`, so
`|U_C|>=R`; write `|U_C|=R+d_C`. Every selected error set has size at most
`r` and lies in `U_C`. Connected components partition the nonisolated
vertices, giving the exact identity

```text
|Z_high|=sum_C |Z_C|.                                  (1)
```

Let `H_D` be an RS parity check and let `y_0+gamma y_1` be the syndrome line
of the received pair. Restricting `H_D` to `U_C` gives an MDS map

```text
H_(U_C): F^(U_C) -> F^R
```

with kernel dimension `|U_C|-R=d_C`. The selected error vector at each
`gamma in Z_C` is a lift of `y_0+gamma y_1`, supported on at most `r`
coordinates of `U_C`.

The global generic-branch condition says that there is no set `E subset D`
of size at most `r` on which both endpoint syndromes have lifts. Any such
set inside `U_C` would also be one inside `D`, so genericity is inherited by
the restriction. The proved generic MDS residual-kernel ray bound therefore
gives

```text
|Z_C| C(d_C+h,d_C) <= C(R+d_C,d_C) R.            (2)
```

Summing the integer floors from `(2)` over the disjoint partition `(1)`
proves `(CA-GRK)`.

For completeness, the same charts also accept the proved
direction-distance ray bound. Every component has at least two slopes, so
subtracting two selected lifts puts `y_1` in `im(H_(U_C))`. Hence a component
whose direction satisfies the DDR inequality may replace its GRK summand by
the smaller DDR bound; failure supplies the certified sparse-direction
normal form. This refinement does not by itself bound the sum over
components.

Finally, if two exact agreement supports share a `k`-set after the strip
rungs, their intersection has size exactly `k`. Taking complements in the
length-`n` domain gives

```text
|E union E'| = n-k = R.
```

Thus the graph's nonisolated slopes are exactly the target's high-core
slopes, completing the application. The proof does not bound either the
number of components or their excesses `d_C`; those quantities remain
load-bearing in the target.
