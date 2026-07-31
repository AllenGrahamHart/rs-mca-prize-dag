# Audit

1. No generic Groebner basis or unbounded field scan is used.
2. Both rational denominator branches are checked before substitution.
3. The direct `b` resultant retains degree-drop branches; only explicit
   source-label guards are saturated from it.
4. Every retained point is replayed in all four original equations.
5. The node records a live finite locus and does not misstate it as an
   exclusion.
