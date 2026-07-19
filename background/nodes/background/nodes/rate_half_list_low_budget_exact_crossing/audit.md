# Audit

1. The Johnson comparisons are strict: their margins are `1` for `B=1` and
   `3` for `B=2`.
2. The budget-one center is well-defined because the only overlap lies in
   the root set of `c_1`.
3. In the budget-two construction, `4|n` and `n|(q-1)` force odd
   characteristic and supply four distinct fourth roots. Every fiber of
   `y=(X/gamma)^d` on `D` has exactly `d` points.
4. Both nonzero codewords have degree exactly at most `2d-1`, so no degree
   `k` term is silently consumed.
5. The received word need not be a polynomial evaluation; ordinary list
   decoding takes the supremum over all words in `F^D`.
6. The conclusion is restricted to budgets one and two. In particular, the
   fact that the Johnson anchor is also `3n/4` at budget three is not used as
   predecessor unsafety.

The focused verifier replays both constructions on two finite fields and two
different multiplicative cosets. The independent audit uses a separate
implementation and checks that mutating the coefficient `i` destroys the
three-codeword predecessor witness.
