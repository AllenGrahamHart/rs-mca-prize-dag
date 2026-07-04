# xr_heavy_triangle_charge conditional proof

## Predicate nodes

- `deep_link_staircase`

## Claim

Heavy triangles are charged by the rung-2b/deep-link machinery.

## Proof

Write the three pairwise overlaps as `r_12`, `r_13`, `r_23`, and the triple
intersection as `g`. The heavy condition is

`r_12 + r_13 + r_23 - g > 2k`.

Since `g >= 0`, at least one pairwise overlap is greater than `2k/3`, hence in
particular lies in the near-`k` deep-link range `(k/2, k)`.

There are then two cases. If the derived codewords for the triangle are
pencil-degenerate, the two-slope interpolation collapses to the already proved
rung-2b partial-forcing map: one line has the required tangent-pencil
agreement and is charged by the graded tangent ledger. If the triangle is
generic, the near-`k` pair found above is precisely a partner counted by
`deep_link_staircase`. That predicate supplies the linear/staircase cap for
such partners after the paid strip.

Thus every heavy triangle is either rung-2b-degenerate or counted by the
deep-link staircase, proving the local charge conditional on
`deep_link_staircase`.
