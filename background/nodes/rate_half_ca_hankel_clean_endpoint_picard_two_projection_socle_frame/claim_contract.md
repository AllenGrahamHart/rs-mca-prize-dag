# Claim contract

- **Claim:** the marked clean point selects the paired Serre-dual evaluation
  directions `ev_S` and `ev_x0` under the two finite projections, with the
  exact pushforward splittings `(PSF3)--(PSF4)`.
- **Dependencies:** the residual-evaluation direction and two-axis Picard
  normalization.
- **Output:** a domain-Veronese coordinate for the marked point that can be
  paired with the Hankel coefficient forms.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no common-orthogonal or second-section theorem is inferred.
- **Falsifier:** failure of the reciprocal pushforward splitting, a fibre
  quotient not representing the socle, or a reciprocal residue functional
  not proportional to evaluation at `x_0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_picard_two_projection_socle_frame/verify.py`
  and `verify_audit.py`.
