# Proof

The identities in `(KBPS-1)` are direct rational simplifications. They give
the vertex permutation `0->2, 1->3, 2->0, 3->1`, hence the assignment map
`(KBPS-2)`. Because `phi_b(1/x)=1/phi_b(x)`, the near relation `w=1/c` is
carried to `w'=1/c'`. Clearing the inverse-map denominator transforms a
quadratic `P(W)=sum_i p_i W^i` to

```text
sum_i p_i (uW-1)^i (u-W)^(2-i).                  (1)
```

The independent generic `5 x 5 solve_right` reconstruction supplies the two
residual quadratics for every literal assignment. Applying `(1)` to each
target and comparing with the destination target after
`(b,c,d)->(b',phi_b(c),phi_b(d))` proves all target identities in
`(KBPS-3)` exactly over `QQ(b,c,d)`.

Apply the same comparison to the reconstructed residuals. Twelve independent
Modal shards each process one source assignment. Every shard completes with
zero target failures and exactly two residual failures, one at each endpoint.
Thus the natural induced destination map fails in all twelve assignments.

To exclude the possibility that source reconstruction induces a different
registry permutation, evaluate the rational residual systems at the three
exact parameter triples

```text
(b,c,d)=(3,5,7), (5/2,3,7), (-2,3,5).            (2)
```

All pullbacks in `(2)` are defined. For each source assignment, compare its
transformed residual pair with every one of the twelve destination pairs,
both preserving and swapping the root order. The resulting 288 destination
tests per sample have no candidate surviving all three samples; the recorded
match list is empty for every source assignment.

If a generic rational covariance identity existed for this prescribed
pair-swap map, it would specialize wherever both sides are defined. The exact
mismatches in `(2)` therefore refute every registry destination and establish
the route cut. QED.
