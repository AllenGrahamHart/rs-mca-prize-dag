# Audit

1. The flag mass is the integer unsafe floor minus every paid category; the
   residual allowance is not reused as extra mass.
2. Residual classes inherit first-match ownership, so their slope masses are
   disjoint before weighted incidence is applied.
3. The class-count denominator is `R_6`, the larger of the dimension-four
   and dimension-six fixed-residual caps.
4. The coordinate incidence is weighted by slope mass. An unweighted count
   of residual classes would prove a weaker statement.
5. Base-freeness of `B` is needed for `dim B_x=4`. If evaluation vanishes on
   all of `B`, the coordinate is a common zero of all `C'=PB` and enters the
   existing global-core branch instead.
6. The output is bucket-local and does not silently become a global core.
