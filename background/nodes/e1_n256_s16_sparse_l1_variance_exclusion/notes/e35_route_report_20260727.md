# E1 N=256 E=35 quotient-Schur route report

This report is route analysis, not a proof node and not a DAG status change.

## Exact preflight

For `V=70`, put `E=35`. The relaxed slack recurrence gives

```text
L=20: slack 21, minimum energy 39 > 35,
L=19: slack 25, minimum energy 35,
```

so `L<=19`. There are 21 integer magnitude profiles. Their largest abstract
layered third-moment caps are

```text
2430  for (3,8),
2258  for (6,5,1),
2110  for (9,2,2),
2098  for (2,6,1).
```

The rational cubic-Hermite form at contacts 14 and 57 has positive exact
margin at `M_3=2162` and negative exact margin at 2163. At the boundary its
log-form coefficients are

```text
M_3=2162: (75141/79507, 4366/79507, -6310/737751),
M_3=2163: (75143/79507, 4364/79507, -4183/491834).
```

Thus only `(3,8)` and `(6,5,1)` require refinement.

## Exact decision

For `(3,8)`, replay the mod-16 quotient inequality in the odd outer-support
and divided-support chambers. The existing proved `Z/64 Z` theorem
`R(B,B,B)<=174` applies to the same 16-point weight-two layer, so no new inner
census is needed.

For `(6,5,1)`, the layer sizes are `(24,12,2)`. Its abstract cap decomposes as

```text
2258 = 552 from R(A,A,A) + 2 from R(C,C,C) + 1704 other terms.
```

The top-layer cubic is zero, so it is enough to prove
`R(A,A,A)<=458`. Full outer support in `4 Z/128 Z` is separately excluded by
the direct small-field bound `54^32<2^250`.

The registered decision run is `CR-E1-E35-Q16` in
`notes/PRIZE_COMPUTE_REQUESTS.md`. PASS closes `V=70`; FAIL returns an exact
quotient allocation and identifies the next support-specific obligation.

## Outcome

Run `ap-Gwlrl9cLfJsa2bS83BFw4k` completed all 2,946,287 quotient allocations.
The `(3,8)` caps are 2152 and 2100 after the inherited inner refinement. The
`(6,5,1)` outer cap is 454 after division, but the odd chamber reaches 460,
two above the sufficient target 458. Thus the original outer-only criterion
returned `FAIL` with an exact obstruction.

The obstruction has only four outer quotient allocations. An independent
exact coupling checker exhausted all 104,750 odd and 32,346 divided outer
allocations, identified exactly those four, and exhausted their 276 compatible
middle/top nestings. Their full three-layer maximum is 2054. Low odd outer
allocations are at most `458+1704=2162`, divided allocations are at most 2158,
and high odd allocations are at most 2054. This repairs the two-count miss and
closes `V=70` without another remote run.
