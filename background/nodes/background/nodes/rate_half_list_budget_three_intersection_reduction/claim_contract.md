# Claim contract: budget-three list intersection reduction

- **claim:** every four-codeword witness at agreement `3n/4-1` in a
  rate-half RS code has one of six incidence types up to codeword relabeling,
  and supplies a pairwise-distinct vector in the kernel of an explicit
  4-wise RS intersection matrix;
- **scope:** `n=4d`, `k=2d`, four distinct codewords, and arbitrary distinct
  evaluation points;
- **consumer:** the `B*=3` branch of
  `rate_half_list_adjacent_crossing`;
- **route fence:** an exact `RS[F_17,mu_8,4]` witness realizes one of the six
  types, so Johnson incidence balancing and pairwise MDS distance alone
  cannot prove predecessor safety;
- **new selected input:** full-column-rank control for the six matrix types on
  the fixed official multiplicative-coset evaluation vector;
- **nonclaim:** no official predecessor witness, safe bound, or adjacent
  crossing is proved for `B*=3`;
- **falsifier:** a four-codeword predecessor witness whose selected agreement
  supports have another incidence type, or whose coefficient vector fails
  the displayed kernel equations.

This is a proved reduction and route exclusion. It is evidence for the
critical leaf and does not create a new required premise.
