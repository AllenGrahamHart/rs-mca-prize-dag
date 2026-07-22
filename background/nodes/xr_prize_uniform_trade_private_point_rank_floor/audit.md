# Audit

- The proof counts points private within the active trade-block set `J`, not
  private coordinates of the trade rows.
- Higher block multiplicities are allowed: `m-2C(m,2)<=1_(m=1)` is valid for
  every `m>=1`.
- A host block covers at most `a` private points from each active block by the
  pairwise selected-block intersection cap; the `ta` charge is not a block-
  size assumption.
- `J` may be the whole core or a proper subset. The algebra cancels `t` and
  yields the same floor in both cases.
- The core caps `384,448,960` and the resulting theorem are prize-only.
- Selector rank is `s=a+1`, so exclusion for `a<A_unif` pays selector ranks
  through `A_unif` exactly.
- No existence at the boundary and no nonuniform-cell statement is claimed.
- No Modal or large local computation is used.
