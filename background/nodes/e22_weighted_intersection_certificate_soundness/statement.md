# e22_weighted_intersection_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Assume a lower-scale intersection certificate supplies, for every dyadic pair
`M_i<M_j` and every subset `S` of smaller dyadic scales `M'<M_i`:

- a finite coefficient formula;
- a verified bijection between the formula's atoms and the residual-profile
  data raw-admissible at `M_j` and admissible at every scale in `S`;
- the same multiplicity weight as `dyadic_profile_evaluation` on every atom.

Then the certificate gives the exact weighted intersection counts required by
`e22_lower_scale_intersection_profile_counts`.

## Falsifier

A certificate whose bijection and weights verify but whose coefficient formula
does not equal the true weighted lower-scale intersection count.
