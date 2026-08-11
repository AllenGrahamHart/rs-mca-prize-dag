# Claim contract

- **Claim:** every failing strict `A=3` slope-slack profile carries the
  nonzero residual Forney section `(FIC5)`.
- **Dependencies:** the strict slope-slack rational-normal ledger.
- **Output:** a section of `O_C(-rho-3,e+1)` whose degree is exactly the
  rank-loss budget `delta=rho-3e`.
- **Consumer:** the residual-pole interpolation exclusion.
- **Nonclaim:** the section is not asserted nonzero on every component.
- **Falsifier:** fewer than `rho+2` kernel rows, a zero canonical numerator,
  a repeated or one-coordinate component overlooked by the split fibres, or
  an incorrect coordinate in `(FIC5)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_endpoint_forney_infinity_contact_section/verify.py`
  and `verify_audit.py`.
