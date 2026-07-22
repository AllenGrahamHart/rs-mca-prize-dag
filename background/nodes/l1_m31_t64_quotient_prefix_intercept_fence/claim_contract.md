# Claim contract

- **Claim:** the explicit pinned M31 quotient profile contains six
  deficiency-64 neighbors of one anchor with a common depth-32 locator
  target, and this refutes `(T64-5)` for `b<=5`.
- **Scope:** support-level `479`-subsets in the fixed `c=2048`,
  `(u,v)=(0,1)` punctured quotient domain.
- **Consumer:** route selection for `l1_mixed_petal_amplification`.
- **Falsifier:** a duplicate quotient label, an invalid puncture, a support
  outside `Q'`, a support of size other than `479`, unequal depth-32
  prefixes, deficiency other than `64`, fewer than six distinct neighbors,
  or failure of `4H_64<p^32`.
- **Nonclaims:** no received-word realization, first-match survival,
  codeword/ray/slope projection, row-global payment, `(6+4)` theorem, or
  prize-row closure.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/l1_m31_t64_quotient_prefix_intercept_fence/verify.py`.
