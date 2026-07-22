# Audit - L1 boundary shifted-lattice affine Q cell

## Checked axes

1. Boundary means `d_1=w+1` and `d_2=omega` exactly.
2. The `B` coefficient is scalar, not an unrestricted polynomial.
3. Coordinates are projective before monic normalization.
4. The infinity ray may carry many support subsets but at most one complete
   agreement codeword.
5. The affine parameter is unique only after using support-codeword
   uniqueness and normalized module pairs.
6. The complement gcd guard remains active.
7. `W_1=1` gives `w+1` prescribed top coefficients.
8. Nonconstant `W_1` remains a quotient/residue Q cell.
9. Interior `d_1>=w+2` is not charged here.
10. No max-fiber estimate is inferred from the normal form.

## Route effect

The L1 residual now matches upstream's off-by-one convention exactly:
boundary to Q, strict interior to BC, with one separately paid projective
point.
