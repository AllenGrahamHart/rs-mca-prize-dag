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
- No cyclotomic-unit subgroup claim is made. The ideal proof supplies an
  arbitrary algebraic unit; a subgroup replacement needs a separate index or
  class-number theorem.
- The coefficient box uses the multiplication matrix of `alpha`, whose
  columns are norm-preserving negacyclic shifts. Reversing `alpha,beta`
  independently supplies the inverse-unit box.
- The uniform constants use only the already proved exact floor
  `floor(18^64/p_min)=2013`; no floating-point estimate is used.
- The Cramer box is asserted only when the two cofactors agree.
- The AM-GM identity uses 64 conjugate pairs: their square-modulus sum is
  `64*18` and their product is the absolute norm, not its square.
- Pinsker is applied to `q_a=1/64` and `p_a=z_a/64`, giving the exact factor
  `sqrt(128D)` in the unnormalized `L1` deviation.
- The log-lattice kernel is `mu_256`; no class-number or cyclotomic-unit
  subgroup assertion enters the orbit injection.
- The orbit charge restores both currencies exactly: 256 oriented vectors
  and the dictionary factor one half give `128M` unordered edges per orbit.
- The cap 367 is labeled necessary only; all lower-weight profile charges are
  intentionally retained.
- No verifier or TeX build requires significant RAM; no Modal job is used.
