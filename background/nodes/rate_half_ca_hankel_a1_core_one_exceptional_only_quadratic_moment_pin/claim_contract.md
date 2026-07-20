# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quadratic_moment_pin`
- **mathematical statement:** the first-order exceptional Hankel crossing is
  exactly the three shifted quadratic convolutions `Theta_0=Theta_1=0` and
  `Theta_2!=0`, equivalently the first three weighted moments of `A(x)^2`
- **scope:** only the official `b=0,D_*=1,c=z=1` corrected square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependency:** exceptional kernel-plane transversality
- **new open content:** combine the scalar moment gate with reciprocal
  reconstruction, all lower Hankel equations, and split-fiber constraints
- **falsifier:** a valid packet for which the Hankel pairings and the printed
  quadratic convolutions differ, or whose source-sum translation fails
- **nonclaims:** the contracted weights need not be original error values or
  nonzero; the three moments are not a converse, a splitting theorem, or a
  profile exclusion; `rate_half_band_closure` is not promoted
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quadratic_moment_pin/verify.py`
- **upstream mapping:** base-field-normalized exact SPI shift-pair moment gate
