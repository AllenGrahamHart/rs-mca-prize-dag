# XR strip and classification rungs

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At each of the six clean-rate candidate rows:

1. the quotient strip costs at most `B_quot_ub(A)`, and the strict dyadic
   census is zero at the odd deciding complement;
2. the tangent strip costs at most `n-A+1`;
3. any two live rays at distinct slopes with a common core of size at least
   `k+1` determine a degree-`<k` codeword pair on that core and therefore
   enter the tangent/classified branch; hence the post-strip generic
   remainder has pairwise cores at most `k`; and
4. the conservative consumption inequality

```text
B_quot_ub(A) + (n-A+1) + 16 n^3 <= B*
```

holds on all six rows. On the prize rows `29 n^3` fits in the residual
allowance and `30 n^3` does not, so the chosen `16 n^3` reserve has
`log2(29/16)` bits of retuning headroom.

This node is the proved carrier for the XR amber implication. It does not
prove either open predicate P-A or P-B and does not replace their per-pair
slope-count quantifiers by collision moments.
