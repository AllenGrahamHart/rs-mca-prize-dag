# Proof

For `S0`, sign changes of `E` and `F` act on `(alpha,beta,gamma)` by

```text
E: (alpha,beta,gamma) |--> (-alpha,beta,-gamma),
F: (alpha,beta,gamma) |--> (alpha,-beta,-gamma).
```

Changing `D` only swaps members of the already complete `DE` and `DF`
signed pairs.  The two displayed generators span the even-parity subgroup
of `{+/-1}^3`, of order four.  Hence there are two orbits of size four, and
their invariant is `tau_0=alpha beta gamma`.

For `S1`, changes of `D,E,F` act on
`(alpha,beta,gamma,delta)` by flipping respectively

```text
(gamma,delta),       (alpha,gamma),       (beta,delta).
```

These three even-parity flip vectors are linearly independent over `F_2`.
They generate the full even-parity subgroup of `{+/-1}^4`, of order eight.
Thus there are two orbits of size eight, indexed by
`tau_1=alpha beta gamma delta`.

In `S2`, every nonloop edge occurs with both product signs and the loop
product is unchanged by representative sign.  There is therefore one cell.
The count and template cap in `(KB41SG-1)` follow immediately. QED.
