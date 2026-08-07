# Conditional proof: FPC5 official-cell partition

Assume the three direct payment leaves:

```text
l1_fpc5_ratehalf_m4_t3_split_slice_payment,
l1_fpc5_m4_t2_payment,
l1_fpc5_large_source_payment.
```

The proved full-petal band composition first restricts every unpaid family to
FPC5, in particular `M>=4` and `2<=t<2M-4`.

If `M=4`, then `t` is `2` or `3`. The official small-source degree sieve
removes every strict `M=4` cell at rates `1/8` and `1/16`.

- For `t=3`, the projective Johnson theorem pays every rate-quarter cell and
  every rate-half cell with positive denominator. The only complement is the
  printed rate-half Johnson-nonpositive tail. The proved source/cross-ratio,
  support-fiber, and complement-slice chain identifies each fixed cell in
  that tail with LS6. This is exactly the first leaf.
- For `t=2`, only rates `1/2` and `1/4` remain. The proved two-full-petal
  theorem injects every fixed pair into its exact petal-equation coprime-pair
  envelope; the second leaf retains the background-root, exactness, and
  first-owner guards required for a full PMA cell.

If `M>=5`, the small-source sieve removes strict cells through `M=6` at rate
`1/8` and through `M=14` at rate `1/16`; it removes no additional `M>=5`
cell at rates `1/2` or `1/4`. Since FPC5 has unbounded root excess, bounded
transition cells are already in the root-pinning payment. The remaining
scales are exactly `M>=5,5,7,15`, the third leaf.

The cases are disjoint by `(M,t,rate)` and exhaustive. Granting their three
aggregate payments therefore pays every FPC5 contributor with no duplicate
owner. This proves the parent conditional. QED.
