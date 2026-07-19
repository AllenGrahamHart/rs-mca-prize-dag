# Audit

- The graph uses nonincidences, where both locator evaluations are nonzero;
  no division is made at a root.
- The density calculation uses saturated rows only and remains valid when
  `X_0` is nontrivial.
- Connectivity makes the row/column potentials unique only up to one common
  nonzero scalar, which is exactly the normalization ambiguity of `Q`.
- Cycle consistency is not promoted to biform existence. The independent
  coefficientwise Reed--Solomon membership test `(AIR6)` is essential.
- Agreement at `n_Z>e_*` clean slopes proves the whole saturated fiber;
  agreement merely on its supported roots would not suffice.
- The rank identities use injectivity of both evaluation maps, not merely an
  upper bound from a displayed separated expansion.
- The reconstruction criterion concerns a biform with the proposed fibers.
  It does not enforce the syndrome Hankel chain, `adj M=lambda*q*q^T`,
  geometric irreducibility, or the active trace equations.
- No enumeration, random experiment, or Modal computation enters the proof.
- `check_packet.py` is a bounded prime-field pilot prefilter. It does not
  certify primality or any omitted Hankel, ambient-domain, or trace condition,
  and it is not an official-scale launcher.
