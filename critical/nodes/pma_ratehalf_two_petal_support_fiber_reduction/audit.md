# Audit - PMA rate-half two-petal support-fiber reduction

## Load-bearing inputs

| input | use | guard |
|---|---|---|
| normalized zero first label | common factor `L_1` | affine normalization must precede the reduction |
| source numerator factors | two quotient-ring target residues | arbitrary rational words are not covered |
| core/petal disjointness | invertibility of `L_S` and exact root transfer | no denominator root may lie in the core |
| nonzero third planted label | invertibility of `R_3 mod L_3` | `lambda=0` is excluded |
| `deg V_S<ell` | first congruence determines `V_S` as a polynomial | raw residue classes are insufficient |
| exactness gcd | root set is exactly `S` | lower-defect migrations must not be recounted |

## Nonclaims

- The guarded fiber is not proved small.
- An unguarded `Phi` fiber is not identified with the PMA list.
- The theorem does not handle partial petals or the fourth-petal first-match
  decision.
- No ambient codomain size is used as a realized-image lower bound.

## Mutations

The verifier rejects the wrong first modulus, omission of either modular
inverse, a nonconstant second residue, removal of the cofactor-degree guard,
removal of exactness, an extra factor for choosing the missed core, and a
nonintegral inverse reconstruction.
