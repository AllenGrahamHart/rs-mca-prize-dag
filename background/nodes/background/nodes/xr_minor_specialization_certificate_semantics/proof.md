# proof: xr_minor_specialization_certificate_semantics

Fix a light-triangle profile chart and the normal-form matrix supplied by
`xr_triangle_eliminant_form`. The chart coordinates live in a coordinate ring
`R`; if the chosen chart uses denominators, admissibility means those
denominators are chart units at the specialization, and the determinant can be
read after clearing those units. Thus each maximal minor is represented by a
well-defined polynomial function on the chart.

Let `Delta` be the maximal minor named by the certificate, and let `a` be the
admissible specialization named by the certificate. Evaluation at `a` is a ring
homomorphism from the chart coordinate ring to the coefficient field:

```text
ev_a : R -> K.
```

If `Delta` were the zero polynomial in `R`, then every ring homomorphism would
send it to zero, so `ev_a(Delta) = 0`. The certificate asserts the opposite:
the determinant of the specialized minor is nonzero. Therefore `Delta` is not
the zero polynomial on the chart.

The light-profile eliminant is the collection of maximal minors controlling
rank stagnation in the normal form. Once one maximal minor is a nonzero
polynomial, not all maximal minors vanish identically. Hence the profile
eliminant is not identically zero on that profile chart.

This proves the certificate semantics. The separate node
`xr_profile_minor_certificate_coverage` is still responsible for producing
such a certificate for every unpaid non-boundary light profile.
