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

SCOPE SEAM (round-28 quantifier audit, 2026-08-10 — the sentence above is
NOT yet supported by the premise as decomposed). After the 2026-08-09 band
decomposition the rate-half premise delivers: the crossing LOCATED at
admissible `q < 2^167` (banked, unconditional); the two residual budgets
`{2^39, 2^39+1}` at `q` in `[2^167, 2^167 + 2^129)`; and the located crossing
at the RAZOR rows only (`rate_half_band_crossing_location`'s pose is
`q` prime in `(2^255.9, 2^256)`). The other decomposition child is scoped to
`n = 2^21` deployed rows and states in terms that it is not razor-row
coverage. The premise's own statement records "beyond 2^167, brackets only".
Rate-`1/2` rows at the official `n = 2^41, k = 2^40` with `q` in
`[2^167, 2^255.9]` are therefore inside this node's quantifier and located by
nothing: the only proved bracket tops there are `n` (full agreement, every
admissible `q`) and `3n/4` (`q >= 2^169`), and a bracket top is not an
adjacent certificate. Either the premise's razor-row pose must be widened to
the full admissible `q`-range, or this node's quantifier must be restricted
with the restriction printed. Flagged, not silently resolved.

With the finite candidate interval localized, the knife-edge and aperiodic
point decisions made, the corridor slack eaten, and the rate-1/2 band closed,
the proved safe agreement `a` and proved unsafe agreement `a - 1` are adjacent
for every admissible row. This proves `adjacency_closing` conditional on its
predicate nodes.

RESOLUTION (2026-08-10, same day, coordinator): the SCOPE SEAM above is
RESOLVED by the first exit — rate_half_band_crossing_location's pose is
WIDENED to all admissible 2^167 < q < 2^256 (statement + shard, dated
widening note in place). With the sub-2^167 range proved by the wave-10
staircase and the widened child owning the rest, the premise as
decomposed again supports the no-remaining-exception sentence.
