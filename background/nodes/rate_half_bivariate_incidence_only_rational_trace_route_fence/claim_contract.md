# Claim contract

- **Claim:** the explicit `m=2`, `F_97` pattern satisfies the listed
  saturation/minimum-pair/bad-overlap conditions and has an all-nonzero
  rational-trace kernel for `M_W`, while `C_W` is full rank.
- **Dependencies:** the rational-interpolation criterion and the
  locator-extension reduction.
- **Output:** a route fence separating incidence-only rank from official
  locator extension.
- **Consumer:** the rank attack on `rate_half_band_crossing_location`.
- **Nonclaims:** no actual Hankel pencil, no extension outside `W`, no
  official-scale counterexample, and no critical status change.
- **Falsifier:** failure of any printed incidence count, rational identity,
  all-nonzero kernel equation, or rank `11/12` and `12/12` certificate.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_incidence_only_rational_trace_route_fence/verify.py`
  and `verify_audit.py`.
