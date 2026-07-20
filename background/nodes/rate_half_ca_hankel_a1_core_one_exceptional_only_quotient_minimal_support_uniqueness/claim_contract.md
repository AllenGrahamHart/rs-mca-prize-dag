# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_support_uniqueness`
- **mathematical statement:** through quotient distance `e+1`, the exceptional
  coset has one minimal support, and minimum-complement ordinary fibers are
  exactly the internal fibers using that support
- **scope:** official `A=1` core-one exceptional-only high-distance branch
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependencies:** quotient-distance router and gap
- **new open content:** classify or exclude the unique support in the lower
  high-distance interval and control multiple leaders above `e+1`
- **falsifier:** two distinct size-`h` quotient supports with `h<=e+1`, or a
  minimum-complement ordinary fiber that is not internal
- **nonclaims:** uniqueness is not asserted for `h>=e+2`, and neither high
  interval is empty
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_minimal_support_uniqueness/verify.py`
- **upstream mapping:** exact SPI / exchange-degree ledger for the rate-half
  exceptional Hankel cell
