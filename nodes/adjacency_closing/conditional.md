# adjacency_closing conditional proof

## Predicate nodes

- `crossing_localization`
- `staircase_steepness`
- `aperiodic_zero_at_crossing`
- `knife_edge_census`
- `corridor_ledger`
- `rate_half_band_closure`

The arithmetic inputs below are not separate logical predicates of this node
after the weakening audit: they feed `corridor_ledger`, whose proved packet is
the single corridor-eater predicate consumed here.

- `acl_second_order`
- `corridor_window_cleanup`
- `corridor_ext_crossing`

## Claim

Conditional on the predicate nodes above, the safe and unsafe MCA bounds meet
at adjacent grid points for every admissible row.

## Proof

By `crossing_localization`, the relevant count function is an integer
staircase. Hence each admissible row has a finite candidate interval for the
first crossing, with only the listed corridor points requiring pointwise
decisions.

By `staircase_steepness`, adjacent grid levels are separated by a q-sized
step except on the explicitly recorded knife-edge set. Thus coarse corridor
estimates decide every non-knife-edge candidate, while `knife_edge_census`
handles the remaining exact Diophantine windows.

The safe-side aperiodic contribution at the crossing candidates is supplied by
`aperiodic_zero_at_crossing`. The three priced corridor eaters are assembled by
`corridor_ledger`. Finally, `rate_half_band_closure` supplies the
otherwise-uncovered rate-1/2 band, so the for-each-admissible-row quantifier has
no remaining exception.

With the finite candidate interval localized, the knife-edge and aperiodic
point decisions made, the corridor slack eaten, and the rate-1/2 band closed,
the proved safe agreement `a` and proved unsafe agreement `a - 1` are adjacent
for every admissible row. This proves `adjacency_closing` conditional on its
predicate nodes.
