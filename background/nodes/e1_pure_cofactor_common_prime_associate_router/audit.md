# Audit

- The proof is ideal-theoretic and uses no numerical search.
- The selected evaluation root is fixed throughout; this is what pins one
  prime ideal `P_r` above `p`.
- The factor of two is removed at the ideal level.  Total ramification and
  `Norm(1-zeta_256)=2` make the exponent exactly `v_2(Norm(alpha))`.
- Absolute element norms are used only to determine the ideal norm.  Their
  signs do not matter.
- The odd-cofactor mutation is deliberately excluded: if
  `Norm(alpha)=2^mu c p` with odd `c>1`, the quotient ideal has norm
  `2^mu c`, so normalized values need not generate `P_r`.
- The associate family is not identified with the 256 roots of unity.  A
  bounded-unit count remains a genuine theorem obligation.
- The coefficient box uses the multiplication matrix of `alpha`, whose
  columns are norm-preserving negacyclic shifts. Reversing `alpha,beta`
  independently supplies the inverse-unit box.
- The uniform constants use only the already proved exact floor
  `floor(18^64/p_min)=2013`; no floating-point estimate is used.
- The Cramer box is asserted only when the two cofactors agree.
- No verifier or TeX build requires significant RAM; no Modal job is used.
