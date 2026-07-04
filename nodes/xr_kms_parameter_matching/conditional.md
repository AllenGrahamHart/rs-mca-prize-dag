# xr_kms_parameter_matching conditional proof

## Predicate nodes

- `xr_globalness_from_ledger`
- `xr_small_set_engine`

## Claim

The KLLM small-set engine composes with the XR ledger at FM-scale densities
with only polynomial loss.

## Proof

The predicate `xr_globalness_from_ledger` gives a post-strip link-density
bound independent of the FM density: every relevant link has density bounded
by a polynomial-scale tangent-ledger parameter. Thus the set entering the
small-set theorem is global in the uniform-slice sense with parameter
`n^{O(1)}` rather than `1/FM`.

The predicate `xr_small_set_engine` supplies the required Johnson-graph
hypercontractive input: for global sets, the expansion/inverse loss is
polynomial in the globalness/link parameters and not polynomial in `1/FM`.

Composing these two statements gives an overall `n^B` loss multiplying the FM
baseline. Hence the XR inverse route is quantitatively compatible with the
FM-scale pair ledger, conditional on the two predicate nodes.

