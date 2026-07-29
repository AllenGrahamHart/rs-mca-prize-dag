# Audit

The symbols `p,eta` in (AIF4) are depressed-cubic invariants, not the
official prime or the HNF parameter `q`. Implementations should preserve
these names or rename them explicitly rather than conflate the roles.

Use the homogeneous factors (AIF6), not a division by `P^3`. The four
rational factors represent seven geometric color values because three are
quadratic conjugate pairs. A factor hit is only an affine-color-compatible
HNF point, not a valid base-field color assignment.

Equation (AIF7) is valid only on the generic locus `x*z*(q-d)!=0`. The two
exceptional slopes `x=0` and `z=0` are owned by their existing quintic and
degree-12 branches and must not be deleted.

All cleared denominators and inherited HNF saturations must be audited after
elimination. This node removes a resultant; it supplies no unit ideal or
packet witness.
