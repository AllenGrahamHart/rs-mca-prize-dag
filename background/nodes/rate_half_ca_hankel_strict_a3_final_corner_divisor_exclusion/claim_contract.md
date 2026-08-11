# Claim contract

- **Claim:** the final `delta=1,T=rho+2` corner contradicts its exact grid
  excess multiplicity, so all strict `A=3` failures are excluded.
- **Dependencies:** the integral Picard pin and slope-slack survivor theorem.
- **Output:** unconditional closure of the strict `A=3` branch.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** no residual `A=1` profile or adjacent unsafe witness closes.
- **Falsifier:** a pole divisor of degree above one, a zero of `A_d` not
  pulling back to a complete fibre, an overlooked fibre-degree multiple,
  or common-divisor excess below multiplicity minus one.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_strict_a3_final_corner_divisor_exclusion/verify.py`
  and `verify_audit.py`.
