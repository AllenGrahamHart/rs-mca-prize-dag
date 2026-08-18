# Proof

For `h in H`, multiplication by `h` is a bijection of `H`, and

```text
x in H, c-x in H
  <=> hx in H, hc-hx in H.
```

Thus `R_(hc)=R_c`; it is enough to inspect the `1016=(p-1)/N`
multiplicative `H`-cosets. The element `3` is primitive in `F_p`, so

```text
1,3,...,3^1015
```

are complete coset representatives.

The pinned C++ census evaluates all 1016 representatives. Its production
implementation materializes `H` as a bitset, walks it forward, and tests
membership of `c-x` by bit lookup. Its audit implementation walks `H`
backward and tests membership independently from `(c-x)^N=1`. Every row
agrees. The pinned result has 1016 rows and reports

```text
sum_(j=0)^1015 R_(3^j)=2097151=N-1,
max_(0<=j<1016) R_(3^j)=2308,
argmax={74}.
```

The first identity independently follows by scaling the ordered-pair identity

```text
sum_(c!=0) R_c=N^2-N
```

over the `N` constants in each coset. It is therefore a global coverage and
counting check, not merely a reported summary.

At `j=74`, the representative is `1177199610`. Direct exponent membership
shows that `c/2` is not in `H`, so all 2308 points form 1154 nonfixed
two-cycles. For every other row, reflection parity agrees with the presence
or absence of `c/2`, and `floor(R_c/2)<=1154`.

Each nonfixed orbit `{x,c-x}` has locator

```text
(X-x)(X-(c-x))=X^2-cX+x(c-x).
```

Distinct orbits are disjoint and have distinct products because sum and
product determine the unordered root pair. Hence the orbit cap is exactly the
fixed-pencil split-fiber cap. QED.

## Computational trust boundary

The finite count is load-bearing. It is pinned by source, dispatcher, checker,
result, and app identifiers. The primary checker verifies every row, coset
identity, paired count, reflection parity, first moment, maximizer, and source
hash; nine hostile mutations are rejected. The node auditor independently
reconstructs the coset traversal and all summary quantities from the pinned
row vector.
