# Audit

1. The witness is generating, so the failure is not caused by the known
   non-generating-row obstruction.
2. It satisfies the official field-size cap by a margin of 134 bits.
3. The failure is the omitted `p=3 mod 4` order branch. The formula based
   only on `v2(p-1)` is valid in the deployed form only for `p=1 mod 4`.
4. Singleton proportionality classes do not imply independent
   prime-field equations: the Frobenius action couples the positions over
   `F_{p^2}`. Therefore the minus branch needs a different kernel model.
5. This refutes only the all-admissible bounded-class reduction. It neither
   refutes the plus-branch theorem nor the final F2 extras budget.

Modal app `ap-gD4VmoDpSyQJ2F6a5xsRnQ` independently checked the Lucas-Lehmer
certificate, field cap, order, erroneous formula, and class count. It
returned `F2_MINUS_BRANCH_COUNTEREXAMPLE_PASS`.
