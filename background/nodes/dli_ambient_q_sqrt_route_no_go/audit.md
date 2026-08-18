# Audit

- `q=33409` lies in the exact high-cap analogue: it is prime, below `2^16`,
  and `q=1 mod 32`.
- The primitive count is the raw subtraction `Z_0-C_1`; owner mass is not
  removed from either marginal.
- The ambient and Haar ratios use different denominators and are both
  recomputed from raw integers.
- The C++ exhaustive scan and the Python explicit-row verifier use different
  subset enumeration implementations.
- The 189-row statement is evidence because one implementation supplies the
  full sweep. The theorem needs only the independently replayed explicit row.
- Failure of a sufficient upper bound is not failure of its consumer. The
  target remains open.

