# Audit

1. The parity domain is `X_delta=U_0\I_delta`, not all of `U_0`.
2. Padded-heavy roots are outside `U_0`, so division by `R_delta(x)` is
   legal on every parity coordinate.
3. The parity start is `R-n+r_delta-1=3e+r_delta-1`; the `-1` is required
   by leading-coefficient extraction.
4. The first nonzero parity equals `zeta_delta lc(H_delta)`, so the run is
   exact rather than a lower bound.
5. Row scalars are the single projective vector from the common biform;
   they are not reselected for each fiber.
6. The result is a reduction to a stacked linear flag, not a proof that
   the flag has small kernel or short runs.
7. The primary replay checks a monic parameter-degree-five row family, all
   drops `0,1,2,3`, and one padded root; the independent replay changes the
   field, dimensions, interpolation method, and drop range.
