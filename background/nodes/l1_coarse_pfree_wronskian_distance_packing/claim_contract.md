# Claim contract - L1 coarse p-free Wronskian distance packing

## Inputs

- a finite field of characteristic `p`;
- an `n`-point set of distinct field elements;
- degree `a` root sets and p-free power sums through depth `d<=a`.

## Output

Distinct members of one arbitrary coarse p-free fiber have disjoint-tail
size at least `ceil((d+2)/2)`. Consequently every fiber obeys the exact
constant-weight packing cap `(PWD4)` and the scalar L1 specialization
`(PWD5)`. When `a+k>=n`, the cap is at least `2^(n-a)` and therefore cannot
pay an official finite numerator by itself if `n-a>=128`.

## Falsifier

Two distinct `a`-sets with equal p-free moments through `d` and disjoint-tail
size below `ceil((d+2)/2)`, or a fiber exceeding the displayed packing cap.

## Nonclaims

No row-sharp finite payment in the linear band, no lower bound on actual
fiber size, no improvement to the stronger full-prefix distance, no
classification of equality families, no Pade-graph coalescing, and no L1
status change.
