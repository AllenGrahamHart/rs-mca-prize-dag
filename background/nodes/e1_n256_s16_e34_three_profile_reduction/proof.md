# Proof

The variance-70 parent makes `V=68` the next endpoint. Put `E=34`. The exact
slack recurrence gives

```text
L=21: slack 16, minimum energy 38>34,
L=20: slack 20, minimum energy 34,
```

so `L<=20`. Enumerating the integer solutions of

```text
sum_j j^2 n_j=34,       sum_j j n_j<=20
```

gives 24 profiles. Their six largest abstract nested-layer third-moment caps
are

```text
2428  (6,7),
2264  (9,4,1),
2252  (2,8),
2124  (12,1,2),
2084  (5,5,1),
1956  (14,1,0,1).
```

Every other profile has cap at most 1940 and is therefore below the exact
cubic threshold 1947.

## Nested quotient closures

For the three latter profiles, allocate each exact magnitude layer over the
nine negation-orbit categories modulo 16. The associated nested layers are

```text
X_i={d: |A_d|>=i}.
```

For each unordered layer triple, apply the target-fiber quotient bound in all
three orientations and take their minimum; then multiply by the exact ordered
triple multiplicity. Requiring an odd outer category gives the live
`Z/128Z` chamber. Dividing an outer-even but non-`4Z` support by two gives the
live `Z/64Z` chamber.

A complete 42,413,558-allocation census gives

```text
profile             order 128    order 64
(5,5,1)                   1880        1828
(14,1,0,1)                1922        1922.
```

For `(2,8)`, write the weighted autocorrelation support as

```text
b=1_U+2 1_B,       |U|=4,       |B|=16.
```

The exact theorem `R(B,B,B)<=174` applies throughout the order-64 chamber and
whenever `B` is even in the order-128 chamber. Replaying all 809,474 quotient
allocations gives

```text
order-64 refined maximum                 1942,
order-128 maximum with B not subset 4Z  1942.
```

The only larger quotient allocation has `B subset 4Z`. Write its eight
positive representatives as an 8-subset of
`{4,8,...,60}`. The two positive representatives of `U` are disjoint from
`B`, and at least one is odd. There are exactly

```text
binom(15,8) * (binom(55,2)-binom(23,2))
=6435*1232
=7,927,920
```

such weighted supports. The complete exact census evaluates

```text
M_3=sum_(x+y+z=0 mod 128) b(x)b(y)b(z)
```

and gives maximum 1536. This closes the inner-`4Z` chamber.

If the complete outer support is contained in `4Z`, then
`F(zeta)conjugate(F(zeta))` belongs to `Q(zeta_64)`. Since `L<=20`, every
conjugate square is at most 56, and the degree-32 small-field norm is nonzero
with absolute value at most

```text
56^32<2^250.
```

The inherited tower identity prevents a pair-feasible row prime from dividing
the collision norm. The odd, divided, and outer-`4Z` cases are exhaustive.

## Cubic certificate

The rational cubic-Hermite majorant at contacts 14 and 57 has positive margin
at `M_3=1947` and negative margin at 1948. Exact atanh-series bounds verify
the two signs. Since every excluded profile above has `M_3<=1942`, its norm is
strictly below `2^250`. Therefore a pair-feasible `V=68` collision can have
only the three profiles in the statement. Each has `L=20`. QED.
