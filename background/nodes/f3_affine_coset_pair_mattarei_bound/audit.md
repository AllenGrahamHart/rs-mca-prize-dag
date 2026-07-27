# Audit

The audit guards the following scope errors.

1. Mattarei's Fermat exponent is our subgroup index `d=(p-1)/m`, not our
   subgroup order `m`.
2. Dividing the projective point bound by `d^2` is valid because only the
   nonzero affine lifts of the desired pairs are used; projective axis points
   can only increase `N_d`.
3. Arbitrary nonzero Fermat coefficients cover `alpha notin K`. No
   same-coset or `t in H` hypothesis is inserted.
4. Nonproportionality is essential: when `beta=0`, the intersection may have
   size `m`, and `(MAC1)` can fail.
5. The official `m=3n` hypothesis is checked from `p>=n^2`; it is not inferred
   from the easier `m=n` case.
6. The theorem is prime-field only. It is not transported to a deployed
   extension-field row.
7. NSB2 is a method barrier. Mattarei's own Remark 3 separates that method
   from the Garcia--Voloch route used by his Corollary.

`verify_audit.py` exhausts small admissible prime-field affine-coset fixtures,
including slopes outside the subgroup, checks the cubed strict inequality,
and confirms a proportional-form counterexample to the forbidden extension.

