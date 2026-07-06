# c_xr_content conditional proof

## Predicate nodes

- `xr_e3_to_expansion`
- `xr_kms_import`
- `xr_junta_to_paid`
- `xr_kms_parameter_matching`

## Claim

The post-strip `k = 3` inverse class consists of fixed-core/fixed-hole paid
structures.

## Proof

By `xr_e3_to_expansion`, large `E_3` is the same obstruction as poor expansion
for the restricted one-exchange walk on the relevant Johnson graph.

By `xr_kms_import`, non-expanding small sets in this Johnson graph correlate
with juntas. The predicate `xr_kms_parameter_matching` supplies the needed
quantitative compatibility at FM scale, so this import can be used in the
post-strip regime without consuming the q-power budget.

A Johnson junta is a union of fixed-core/fixed-hole cells. The predicate
`xr_junta_to_paid` identifies those cells with tangent/common-divisor paid
structure after the quotient strata have been stripped.

Therefore the `k = 3` XR content is exactly the fixed-core/fixed-hole paid
class, conditional on the four predicate nodes.

