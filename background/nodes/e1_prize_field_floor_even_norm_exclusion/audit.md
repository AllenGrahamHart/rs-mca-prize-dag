# Audit

- The proof uses the exact prize lower endpoint, not the common coarse
  `p>=2^250` floor.
- The strict inequality needed is `R<2p`; equality `R=2^256` is harmless
  because `p>2^255`.
- The parity argument is checked independently on complete small class
  models. It comes from equal class size, not from a profile assumption.
- The norm exponents are 64 for `N=256` and 128 for `N=512`.
- The argument intentionally does not strengthen RowC, whose prime floor is
  only `2^250`.
- No numerical search or remote computation is used.
