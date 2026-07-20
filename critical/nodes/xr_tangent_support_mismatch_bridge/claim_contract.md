# Claim contract

- **claim id:** `xr_tangent_support_mismatch_bridge`
- **scope:** all received pairs at the six clean-rate candidates
- **currency:** distinct support-wise MCA-bad slopes
- **quotient slot:** `B_quot_ub(A)` under the existing first-match convention
- **tangent slot:** at most `n-A`, now proved by the coordinate injection
- **residual slot:** at most `16n^3` for nongeneric pairs; generic residuals
  are transported to P-A/P-B without allocation inflation
- **proved residual normal form:** every nonzero mismatch enters a punctured
  GRS chart with invariant excess `h=A-K`
- **proved canonicalization:** the full external zero set gives one chart per
  selected slope/codeword pair
- **proved nongeneric router:** chart genericity failure is exactly a second
  joint `A`-support extending that zero set; distinct explanation supports
  intersect in at most `K-1`
- **proved descent potential:** `A-K` is invariant and ambient length falls
  by at least `A-K+1`; official depth is below `256/512`
- **proved terminal width:** with `H=A-K+1`, the `N<=4H` nongeneric subtree
  has at most `1+104H` live instances and at most `420H^2` genuine-tangent
  charges; every fixed logarithmic window has a polynomial whole-tree and
  tangent-charge bound when `H>=2C log_2 n`
- **consumer:** `xr_clean_residual_any_gate`
- **falsifier:** an official candidate pair for which every support-wise
  first-match split exceeds the three slots above
- **nonclaims:** global pair proximity alone is not a payment; the toy
  `F_17` counterexample is not an official-row falsifier
- **remaining open content:** aggregate generic-chart slopes without a
  binomial chart factor, and bound/aggregate slopes mapping to each low-core
  joint explanation before the paid terminal window without paying the full
  budget at every level
