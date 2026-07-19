# Claim contract: rate-half list low-budget exact crossing

- **claim:** for every multiplicative-coset rate-half row of length divisible
  by four, the ordinary-list adjacent crossing is exactly `3n/4` when the
  integer list budget is `B=1` or `B=2`;
- **safe side:** consume the proved exact-integer Johnson theorem at
  agreement `3n/4`;
- **unsafe side:** construct respectively two and three distinct degree-`<k`
  codewords around one explicit received word at agreement `3n/4-1`;
- **scope:** `n=4d`, `k=2d`, and an evaluation domain that is a multiplicative
  coset of order `n`; in particular every official rate-half row;
- **consumer:** the `B*=1,2` branches of
  `rate_half_list_adjacent_crossing`;
- **nonclaim:** no crossing is asserted for `B>=3`, for MCA/CA, or for a
  non-coset evaluation set in the three-codeword construction;
- **falsifier:** an in-scope row on which the displayed words are not
  codewords, do not all reach `3n/4-1`, or the Johnson inequality is not
  strict at `3n/4`.

This closes two complete budget branches. It does not introduce a premise or
change the status of the remaining rate-half list leaf.
