# Claim contract

- **Claim:** a strict official `A=3`, `e=2^37` counterexample must have
  exactly `2^39+1` supported slopes, total root-column deficit at most
  `2^37`, and at least `15/16` of all domain columns saturated at their full
  parameter degree.
- **Scope:** only the core-free strict-budget profile
  `rho=4m-1`, `N=16m`, `e=m`, with the exceptional-root charge already
  available.
- **Dependencies:** `rate_half_ca_hankel_exceptional_root_charge` supplies
  `u_gamma>=rho-c_gamma` and `sum c_gamma<=delta`; its core-free conclusion
  supplies `Q_Z(x) != 0` for every domain point.
- **Consumer:** the terminal `A=3` part of `rate_half_band_closure`.
- **Nonclaims:** no extremal configuration is excluded; no `e>m` profile,
  `A=1` profile, dyadic pullback classification, or adjacent rate-half row is
  closed.
- **Counting convention:** slopes and domain roots are distinct and finite.
  Parameter multiplicity is used only as the upper bound `d_x<=e`.
