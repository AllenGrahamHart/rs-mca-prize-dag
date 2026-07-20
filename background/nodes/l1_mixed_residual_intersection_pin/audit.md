# Audit - L1 mixed-residual intersection pin

## Checked axes

1. The polarized root-pinning payment and B11 payment are combined by union,
   so the residual is the intersection of their complements.
2. The B11 anchor predicate is `G_2<=V_2 or G_R<=V_R`; replacing this by an
   `and` would omit paid `A2` and `AR` words.
3. The bounded defect boundary is inclusive: `d<=ell+E_d` is paid.
4. The rich-fiber theorem is a necessary condition on every residual, not a
   count and not a fixed power-map fiber statement.
5. PR `#977` has the same generic packing endpoint already proved by
   `pma_source_paving_bridge`; its `n/c` normalization cannot be imported as
   a structure theorem for arbitrary petals.
6. The two-parameter corollary is a union escape `p>P or d>ell+E`, the exact
   complement of a paid box; it is not a claim that both coordinates grow.

## Remaining attack

Count or naturally own the exact residual. At aggregate scale the two honest
escape routes are growing cofactor excess or growing polarized support
entropy, always under the more detailed `(I3)` gates and the reserve rich
fiber.
