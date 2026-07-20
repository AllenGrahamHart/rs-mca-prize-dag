# Audit

- Did not assume the completed blocks partition the domain. Cross-block
  completion occurs exactly when two deleted roots are antipodal.
- Did not assume the four completion roots are distinct. Coincidence would
  put their common negative root in two pairwise-coprime block locators, so it
  is impossible.
- Classified all antipodal-pair counts `c=0,1,2`; the unused exceptional
  roots form exactly `c` antipodal pairs and repair the quartic denominator.
- Used pairwise coprimality twice: to make the `G_i` pairwise coprime and to
  rule out a one-dimensional monic pencil.
- Checked the parameter relation `2d=4s`. Only `c=0` has denominator
  `product_i(Y-rho_i^2)`; the other strata are not silently imported into the
  matched norm equation.
- Re-established the characteristic bound at the doubled quotient order.
  The old printed `p>d` specialization alone was not silently reused.
- Reproved the Mobius weld, primitive degree exclusion, and reverse-contact
  floor for the general quartic. The direct four-coset exclusion is imported
  only on the matched `c=0` stratum.
- The finite controls test nontrivial Mobius target changes and mutation of
  one paired parameter. No Modal computation was used.
