# Audit

1. The primary verifier exhausts all `40^2` nonzero `(d,s)` pairs and checks
   all seven eigenvalue equations, not only the selected first three.
2. Representative-square and twelve-product injectivity are both checked.
3. The audit verifier applies the Mobius involution directly to the six
   residual products.
4. The field is explicitly `F_41`; no deployed-characteristic survival is
   inferred.
5. No outside `q` or interpolation data are supplied by this fixture.
