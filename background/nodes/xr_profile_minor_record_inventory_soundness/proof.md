# proof: xr_profile_minor_record_inventory_soundness

Let `P` be the set of budget-meeting unpaid non-boundary light-triangle
profiles. Assume an inventory `I` covers `P`, meaning every profile in `P`
appears with exactly one payload record or with a declared disjoint record
class whose multiplicity is accounted for.

For each profile, the record has one of the accepted forms.

For a triangular record, the proved node
`xr_triangular_minor_certificate_soundness` shows that an admissible
specialized maximal-minor matrix with nonzero diagonal has nonzero
determinant.

For a monomial/noncancellation record, the record includes the named maximal
minor and the certified noncancelling monomial or specialization value, so it
directly supplies a nonzero determinant witness under the payload schema.

For a remote table record, completeness of the table entry means the row names
the profile, the maximal minor, the admissible specialization, and the
nonzero determinant value. Thus it also supplies an accepted nonzero-minor
payload record.

Since every profile in `P` is covered by one accepted record, the inventory
supplies exactly the profile-by-profile payload required by
`xr_profile_minor_certificate_payload`.
