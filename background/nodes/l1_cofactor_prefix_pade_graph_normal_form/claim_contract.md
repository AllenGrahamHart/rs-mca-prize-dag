# Claim contract - L1 cofactor-prefix Pade graph

## Inputs

- normalized received word `U` with `h=deg U`;
- shell parameters `w=a-k`, `e=h-a`, and `0<=e<k`;
- monic split agreement locators.

## Outputs

- reversed-series equation `Qhat Lhat=Uhat mod T^(w+e+1)`;
- a `q^e`-point codimension-`w` polynomial graph in locator-prefix space;
- bijective recovery of the cofactor from the first `e` locator coefficients;
- exact-shell equality with the graph/divisor intersection plus the complement
  gcd guard;
- ambient graph density exactly `q^(-w)`.

## Consumer rule

Count split locators meeting `G_(U,a)` directly.  Preserve the received-word
series `Uhat`, the graph equations, quotient/primitive owner, and gcd guard.
Do not enumerate independent `(Q,prefix)` pairs and do not apply a generic
maximum-fiber union when a graph-intersection theorem is available.

## Nonclaims

No divisor/graph transversality or max-fiber theorem is proved.  The graph may
align strongly with the attained split-divisor image.  No quotient payment,
or uniform finite-row constant is supplied. The `e>=k` representation is
provided only by the follow-on full-locator section node.

## Falsifier

Two distinct cofactors producing the same depth-`w+e` prefix, failure of the
inverse `(PG4)`, a graph divisor whose reconstructed difference has degree at
least `k`, or disagreement between the complement gcd guard and exact
agreement.
