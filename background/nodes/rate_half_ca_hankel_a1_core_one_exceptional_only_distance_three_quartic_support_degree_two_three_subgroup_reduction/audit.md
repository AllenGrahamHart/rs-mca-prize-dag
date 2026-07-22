# Audit

1. The fiber counts retain the normalization losses: `e-40` for degree two
   and `e-85` for degree three.
2. A general degree-three rational map is put into the cubic-over-quadratic
   form before importing the corner calculation. The choice also enforces
   a nonzero cubic constant term; this is not assumed.
3. The worst irreducible constant remains `1440`, including the two
   exceptional determinant-one torus changes.
4. Geometric reducibility is treated separately. Exchanged Frobenius
   components cannot carry the printed base-field point count.
5. The subgroup-heavy graph forms are not discarded. Their automorphism
   orders give antipodal/constant-product in degree two and exclude degree
   three because `mu_(2^41)` has no nontrivial 3-torsion.
6. The degree-two conclusion is near-dihedral, not fully dihedral. All
   downstream uses must pay or remove the at-most-40 tail pairs.
