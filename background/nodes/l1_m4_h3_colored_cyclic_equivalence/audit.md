# Audit - colored cyclic-code equivalence

1. One colored-code constraint is insufficient. Both `b` and its
   coefficientwise square are required to recover equality of all three
   color-class moments.
2. Coefficientwise powers are not polynomial powers in
   `F_p[T]/(T^n-1)`; the notation `b^[r]` is pinned explicitly.
3. The cube root lies in the prime field because every listed `m=4`
   characteristic is `1 mod 3`; Frobenius therefore preserves both words.
4. Equal moments through `p-1`, not the whole closure, recover the common
   locator prefix. The closure is the cyclic-code representation.
5. Maximal-degree emptiness is needed to replace `h>=3` by exact `h=3`.
6. The equivalence is a re-encoding, not an emptiness proof.
