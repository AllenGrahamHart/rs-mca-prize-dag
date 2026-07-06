# proof: xr_sameslope_list_crossover

- **status:** PROVED
- **closure:** proof

## Source

Vendored from the working record; primary artifact(s):
- `experimental/notes/roadmaps/qx13_pair_rank_ledger.md`

## Ledger

PROVED (X-3 wave, verifier 39/39): same_slope_branch(u,v;z,A) = ExactList_C(w_z, A) exactly, with automatic far-spread (RS uniqueness + exactness). The list-lane obligation itself lives in the list nodes, as designed. | X-4 CORRECTION: the consumed object is the SPLIT form (staircase terms charged + primitive bound), not the unqualified ExactList. Slope/support distinction limits MCA-side impact: staircase supports share slopes, so R_post's slope count survives; the spread-count support analysis charges staircase supports to the (enlarged, tail-form) quotient strip.
