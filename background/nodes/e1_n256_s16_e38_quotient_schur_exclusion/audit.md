# Audit

- Confirmed the mod-16 formula is an upper bound residue by residue and takes
  the minimum over all target-layer choices.
- Confirmed that the zero-pair subtraction uses both nesting and symmetry.
- Confirmed the order-128 and divided order-64 orbit capacities directly from
  their positive representatives.
- Recounted all 43,153,083 allocations by an independent dynamic program.
- Re-evaluated every shard maximum in Python independently of the C++ census.
- Exhaustively checked the quotient inequality on every nested symmetric
  layer assignment in `Z/16 Z`, using quotient `Z/4 Z`.
- Confirmed hostile mutations deleting a shard, marking a shard incomplete,
  or corrupting an allocation shape are rejected.
- Checked that only three of the 32 magnitude profiles exceed 2806 under the
  abstract cap.
- Checked `R({c,-c},{c,-c},{c,-c})=0` in a 2-group.
- Replayed the parent's exact rational cubic margin at 2806.
- No numerical approximation or solver incompleteness enters the claim.
