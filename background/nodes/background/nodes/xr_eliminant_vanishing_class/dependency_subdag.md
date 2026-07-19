# dependency sub-DAG: xr_eliminant_vanishing_class

Promoted subclaims.

```text
xr_triangle_eliminant_form [PROVED]
    -> xr_profile_minor_certificate_payload
    -> xr_profile_minor_certificate_coverage
    -> xr_profile_eliminant_nonvanishing
    -> xr_eliminant_vanishing_class
    -> xr_light_triangle_eliminant

xr_triangle_eliminant_form [PROVED]
    -> xr_minor_specialization_certificate_semantics [PROVED]
    -> xr_profile_eliminant_nonvanishing
    -> xr_eliminant_vanishing_class
    -> xr_light_triangle_eliminant

xr_coordinate_hypersurface_reduction [PROVED]
    -> xr_eliminant_vanishing_class
    -> xr_light_triangle_eliminant

deep_link_staircase [CONDITIONAL]
    -> coordinate-special rationing in xr_light_triangle_eliminant
```

## xr_profile_eliminant_nonvanishing

Statement: for every budget-meeting light profile, the normal-form matrix from
`xr_triangle_eliminant_form` has at least one nonzero maximal minor as a
polynomial in the profile coordinates, except for paid/boundary classes.

Status: CONDITIONAL. The specialization semantics and triangular certificate
soundness are proved; the remaining open predicate is
`xr_profile_minor_record_inventory_payload`.

Falsifier: a light profile for which no admissible nonzero maximal-minor
specialization exists and which is not paid.

## xr_coordinate_hypersurface_reduction

Statement: if the profile eliminant is nonzero, the coordinate-special locus
is a proper bounded-degree hypersurface inside the aligned-support chart.

Status: PROVED. The population/rationing of that hypersurface remains routed
through `deep_link_staircase` in the consumer proof.

Falsifier: a proper-locus family with super-polynomial aligned triples outside
paid strata.
