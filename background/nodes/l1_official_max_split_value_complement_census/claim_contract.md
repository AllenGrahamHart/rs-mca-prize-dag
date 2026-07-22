# Claim contract - L1 official maximal split-value complement census

- **claim:** for every actual split-value degree `2<=h<=m`, the unused
  degree-`u=n-hp` complement uniquely determines the normalized Frobenius
  pencil. At depth `d`, its forced coefficient gap gives at most
  `floor(binom(n,ell_h)/binom(u,ell_h))` records, where `ell_h=u-d+p`,
  and `binom(h,2)` pairs per record. At capacity, the terminal layer is empty
  on all 16 official `m>=3` atlas rows.
- **scope:** minimum tail width `t=p`, first-checkpoint depths
  `p<=d<=2p-2`, and official multiplicative-coset rows. The polynomial
  payment and terminal exclusion are specific to
  `deg G_Q=m=floor(n/p)`.
- **proved dependencies:** the first-checkpoint split-pencil reduction, exact
  split-value capacity/eliminant, and official checkpoint atlas.
- **consumer:** the maximal-value branch of
  `l1_mixed_petal_amplification`.
- **falsifier:** a capacity-attaining pencil whose complement violates the
  coefficient gap; two normalized pencils with one complement; an official
  terminal record; or a row/count discrepancy against the exact atlas.
- **nonclaim:** the growing exponent `u-d+p` is not a polynomial payment for
  lower `h` in general; there is no higher-width census, complete
  first-checkpoint closure, or full L1 payment.
- **compute policy:** no enumeration is needed for the paid nine-row branch
  or the terminal exclusion. Any external computation must name a lower
  split-value stratum on one of the 16 atlas rows.
