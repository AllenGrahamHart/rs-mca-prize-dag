# ATTACK - xr_profile_eliminant_nonvanishing

Do not run E32 locally.

This node is now an assembly node. The determinant semantics are closed by
`xr_minor_specialization_certificate_semantics`.

The remaining proof route is exactly
`xr_profile_minor_certificate_coverage`: use the MDS normal-form matrix from
`xr_triangle_eliminant_form` and identify, for every unpaid non-boundary light
profile, a profile-dependent maximal minor with a visibly nonzero monomial
term or a triangular specialization with nonzero determinant.

Remote evidence route: obtain a complete E32-extended `E32_RESULTS` certificate
covering the intended profile range. Toy E32-MERGED data is evidence, not a
uniform proof.
