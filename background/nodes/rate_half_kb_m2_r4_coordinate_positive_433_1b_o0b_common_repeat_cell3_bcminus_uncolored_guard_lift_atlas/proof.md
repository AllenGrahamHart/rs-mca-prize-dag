# Proof

For each of the 47 printed guard polynomials, compute
`gcd(G(q),q^p-q)` and factor the squarefree result. All factors are linear;
their union has 48 values and 73 incidences.

For each union value, evaluate `N(q)` and `D(q)`. If `D(q)=0`, the exact
projection equation has no guarded point in this chart. Otherwise factor the
quadratic `Y^2-N/D` over the deployed field, reconstruct `b,c` by the guarded
Mobius formulas, and replay `F(b,c)=0`.

For each surviving `(q,y)` and each root-sign pair, factor the certified
quadratic for `r`. Every retained root is replayed in its exact `r` relation
and checked against the complete common label and target guard. This gives
the displayed disjoint census and 368 guarded points. QED.
