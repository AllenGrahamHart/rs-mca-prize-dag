# frontier: xr_profile_minor_certificate_coverage

Conditional.

What is now closed: if a proposed certificate names a maximal minor and gives
one admissible specialization with nonzero determinant, then the corresponding
profile eliminant is nonzero. That is the proved node
`xr_minor_specialization_certificate_semantics`.

What is also now closed: a triangular specialized minor with nonzero diagonal
has nonzero determinant. That is the proved node
`xr_triangular_minor_certificate_soundness`.

What remains: `xr_profile_minor_record_inventory_payload`, producing such
certificates uniformly for all budget-meeting unpaid non-boundary
light-triangle profiles.

The smallest next proof step is to inspect the normal-form matrix from
`xr_triangle_eliminant_form` and isolate a profile statistic that selects a
triangular minor for every live profile. A remote complete certificate table
would also discharge the payload node, but should not be generated locally in
this WSL clone.
