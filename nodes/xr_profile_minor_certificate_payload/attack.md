# ATTACK - xr_profile_minor_certificate_payload

This node is now conditional. The live XR coverage leaf is
`xr_profile_minor_record_inventory_payload`.

Do not run E32 locally on the WSL laptop. The soundness of triangular
certificates is proved in `xr_triangular_minor_certificate_soundness`, and the
general nonzero-specialization semantics are proved in
`xr_minor_specialization_certificate_semantics`. The inventory-format
soundness rule is proved in `xr_profile_minor_record_inventory_soundness`.

Needed output:

- for every budget-meeting unpaid non-boundary light profile, give a payload
  record naming a maximal minor and admissible specialization;
- each record must be triangular with nonzero diagonal, monomial-certified
  nonzero, or part of a complete remote certificate table;
- the payload must cover the uniform profile quantifier, not only the toy
  E32-MERGED/E32-COORD samples.
