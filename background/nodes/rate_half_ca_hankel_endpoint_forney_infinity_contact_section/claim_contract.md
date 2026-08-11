# Claim contract

- **Claim:** every strict `e=m` endpoint, including reducible positive-defect
  profiles, carries the nonzero residual Forney section `(FIC4)`.
- **Dependencies:** the full rational-normal kernel pencil and the reduced
  mixed-component theorem.
- **Output:** a defect-independent section of `O_C(-rho-3,m+1)`.
- **Consumer:** the residual-pole interpolation exclusion.
- **Nonclaim:** the section is not asserted nonzero on every component.
- **Falsifier:** fewer than `rho+2` kernel rows, a zero canonical numerator,
  a component at `X=infinity`, or an incorrect coordinate in `(FIC4)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_endpoint_forney_infinity_contact_section/verify.py`
  and `verify_audit.py`.
