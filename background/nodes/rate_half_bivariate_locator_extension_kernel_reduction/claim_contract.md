# Claim contract

- **Claim:** `E_W r=0` is equivalent to coefficientwise `X`-degree-`rho`
  extension on `W`; every actual failure lies in `ker(M_W) intersect
  ker(E_W)` with every coordinate block nonzero.
- **Dependency:** `rate_half_bivariate_deficiency_clone_kernel_reduction`.
- **Inputs:** distinct support points, incidence factors `A_x`, deficiency
  clones, and the official locator degree bound.
- **Output:** the strengthened necessary matrix `C_W`.
- **Consumer:** the bivariate route for `rate_half_band_crossing_location`.
- **Nonclaims:** no full-rank theorem for `C_W`, no control outside `W`, and
  no adjacent-crossing closure.
- **Falsifier:** an extendable coefficient vector rejected by `(LEK2)`, a
  nonextendable vector accepted by it, or an actual locator kernel that
  fails `E_W r=0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_locator_extension_kernel_reduction/verify.py`
  and `verify_audit.py`.
