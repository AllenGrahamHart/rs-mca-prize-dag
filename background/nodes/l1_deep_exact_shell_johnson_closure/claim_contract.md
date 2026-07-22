# Claim contract - L1 deep exact-shell Johnson closure

## Inputs

- Reed--Solomon pairwise agreement at most `k-1`;
- Cauchy--Schwarz incidence counting;
- exact-shell disjointness by complete agreement size.

## Outputs

- general Johnson list bound `(DJ2)`;
- implication `2m>n+k-1 => m^2>n(k-1)`;
- one-list payment of all deep exact shells by `n^2`;
- full-box length cap `n<=2^44 => n^2<=2^88`.

## Consumer rule

Aggregate the entire deep tail at the first deep threshold `m_J`.  Do not sum
one `n^2` allowance per shell level.

## Nonclaims

No exact budget crossing, primitive/quotient split, balanced-band count, or
MCA statement is proved.

## Falsifier

A pair of distinct degree-below-`k` codewords agreeing on `k` points, a list
violating `(DJ2)`, failure of `(DJ1)` at `m_J`, or a deep exact-shell member
outside the list at threshold `m_J`.
