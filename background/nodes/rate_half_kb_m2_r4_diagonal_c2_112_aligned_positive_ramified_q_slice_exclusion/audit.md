# Audit

1. The calculation starts from the repaired `w=0` source equations; it does
   not substitute `w=0` into an affine near-aligned chart.
2. The exact relative scale is retained until its linear normalization is
   solved. This fences the earlier retracted unscaled norm calculation.
3. A separate audit reduces the raw `U^2-WV^2` modulo `q`, divides the
   forced `W^2`, and reconstructs all four allocation equations directly.
4. No generic-field gcd is used as an emptiness certificate. Each of the six
   full ideals is saturated by an explicit open-set product and has basis
   `<1>` in the deployed characteristic.
5. Moving inversion is handled only after proving every equation is a
   reciprocal quartic. The trace lift is checked symbolically.
6. The result is an aligned ramified deletion. The near-aligned boundary
   has a projective endpoint in `q` and is not covered by this monic chart.
