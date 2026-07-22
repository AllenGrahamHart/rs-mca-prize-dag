# Claim contract - L1 official maximal split-value complement census

- **claim:** for every actual split-value degree `2<=h<=m`, the unused
  degree-`u=n-hp` complement uniquely determines the normalized Frobenius
  pencil. At depth `d`, its forced coefficient gap gives at most
  `floor(binom(n,ell_h)/binom(u,ell_h))` records, where `ell_h=u-d+p`,
  and `binom(h,2)` pairs per record. Polynomial abc gives the dichotomy
  `ord_0(R)<=u-p` or `u e_h<=p`, where `R` is the depressed pencil and
  `h e_h+1=0 mod p`. At capacity, all 16 official `m>=3` rows violate the
  second arm while the first is impossible, so their full maximal-capacity
  strata are empty.
- **scope:** minimum tail width `t=p`, first-checkpoint depths
  `p<=d<=2p-2`, and official multiplicative-coset rows. The polynomial
  abc exclusion is specific to `deg G_Q=m=floor(n/p)`.
- **proved dependencies:** the first-checkpoint split-pencil reduction, exact
  split-value capacity/eliminant, and official checkpoint atlas.
- **consumer:** the maximal-value branch of
  `l1_mixed_petal_amplification`.
- **falsifier:** a capacity-attaining pencil whose complement violates the
  coefficient gap; two normalized pencils with one complement; an official
  maximal-capacity record; or a row/count discrepancy against the exact
  atlas.
- **nonclaim:** the growing exponent `u-d+p` is not a polynomial payment for
  lower `h` in general; the centered-valuation bound alone does not count
  lower-`h` records. There is no higher-width census, complete first-checkpoint
  closure, or full L1 payment.
- **compute policy:** no maximal-capacity enumeration is needed on any of the
  16 rows. Any external computation must name a lower split-value stratum.
