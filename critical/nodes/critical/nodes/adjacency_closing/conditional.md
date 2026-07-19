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

At the clean rates, the safe-side aperiodic contribution at the crossing
candidates is supplied by `aperiodic_zero_at_crossing`. The three priced
corridor eaters are assembled by `corridor_ledger`. The rate-`1/2` aperiodic
thin point and residual band are not supplied by the clean-rate aperiodic node;
they are part of the separate `rate_half_band_closure` premise.  Thus, if that
strong rate-half premise holds, the for-each-admissible-row quantifier has no
remaining exception.

With the finite candidate interval localized, the knife-edge and aperiodic
point decisions made, the corridor slack eaten, and the rate-1/2 band closed,
the proved safe agreement `a` and proved unsafe agreement `a - 1` are adjacent
for every admissible row. This proves `adjacency_closing` conditional on its
predicate nodes.

---

## WAVE-9 PREDICATE-ROLE ADDENDUM (2026-07-17, pin body)


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

At the clean rates, the safe-side aperiodic contribution at the crossing
candidates is supplied by `aperiodic_zero_at_crossing`. The three priced
corridor eaters are assembled by `corridor_ledger`. The rate-`1/2` aperiodic
thin point is not supplied by the clean-rate aperiodic node.
`rate_half_band_closure` supplies the complete field-dependent adjacent
certificate for that row. Its proved simple-pole dependency gives only a
lower bracket: it refutes the former fixed candidate rather than certifying an
adjacent crossing there. Thus, if the re-posed rate-half premise holds, the
for-each-admissible-row quantifier has no remaining exception.

With the finite candidate interval localized, the knife-edge and aperiodic
point decisions made, the corridor slack eaten, and the rate-1/2 band closed,
the proved safe agreement `a` and proved unsafe agreement `a - 1` are adjacent
for every admissible row. This proves `adjacency_closing` conditional on its
predicate nodes.
