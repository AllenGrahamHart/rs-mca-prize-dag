# u1_alpha_active_core_incidence conditional proof

## Predicate nodes

- `anchored_nontoral_pte_bound`

## Claim

For each base support `S0`, the post-strip active-core incidence mass
`sum_Q K_Q^sp` is at most `n^2`.

## Proof

The active core `Q` contributes only when the corresponding anchored pair
survives the full strip. X-10's orbit transport identifies these surviving
active-core contributions with the anchored non-toral PTE pairs counted by
`anchored_nontoral_pte_bound`; no additional incidence family remains after the
strip.

The predicate `anchored_nontoral_pte_bound` gives
`A_h^nt <= h n`. The proved orbit argument converts anchored pairs to
unanchored split pairs with factor `n/h`, so the total post-strip contribution
is at most

`(n/h) A_h^nt <= (n/h) h n = n^2`.

Thus the active-core incidence theorem follows from the anchored non-toral PTE
bound.
