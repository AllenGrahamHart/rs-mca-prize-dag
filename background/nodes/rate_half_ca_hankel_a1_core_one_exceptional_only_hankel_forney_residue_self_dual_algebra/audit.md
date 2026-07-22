# Audit

1. `Phi` renames the Forney numerator to avoid collision with the reciprocal
   biform `F` used by the jet compiler.
2. Column normalization uses `q_1(a)`, the nonzero derivative at the simple
   exceptional parameter root.
3. The new weight is `beta_a q_1(a)^2`; applying `(QFN5)` leaves one factor
   of `q_1(a)`, as printed in `(HFR6)`.
4. The residue coefficient in `(HFR3)` is taken after reduction modulo `A`.
5. Product-space codimension one makes the annihilating functional unique;
   identifying its representing class uses nondegeneracy of the residue
   pairing, not a dimension heuristic.
