# Proof

Let `b_d=|A_d|` on the symmetric non-diameter support and put

```text
S_i={d:b_d>=i}.
```

For profile `(4,5,1)`, the nested layer sizes are

```text
|S_1|=20,       |S_2|=12,       |S_3|=2.              (1)
```

For three symmetric layers `U,V,W`, distribute their residues over the nine
negation-orbit categories modulo 16. In each orientation, the target-fiber
bound is

```text
R(U,V,W)
 <=sum_c min(
      # ordered (u,v) in U*V with u+v=-c,
      W_c sum_a min(U_a,V_(-c-a))).                    (2)
```

For `c=0`, remove the `min(|U|,|V|)` pairs `(u,-u)` that would force the
third entry to zero. Take the minimum of (2) over all three orientations.
Expanding `b=1_(S_1)+1_(S_2)+1_(S_3)` and multiplying by the exact ordered
layer multiplicities gives a rigorous upper bound for `|M_3|`. The cubic of
the symmetric two-point top layer is zero because a 2-group has no nonzero
element of order three.

The category capacities at orders 128 and 64 are respectively

```text
(3,8,8,8,8,8,8,8,4),
(1,4,4,4,4,4,4,4,2).
```

The deterministic census enumerates every allocation of the exact counts
`(4,5,1)` under these capacities and requires an odd outer category. Sixteen
disjoint shards in each chamber give

```text
order 128: 5,421,301 allocations, maximum 1732;
order  64: 3,086,861 allocations, maximum 1670.         (3)
```

An independent checker reconstructs every shard total, every maximizing
allocation, and every objective from (2). Repartitioning the same complete
space into seven shards gives the same totals and maxima.

If `S_1` contains an odd distance, the first line of (3) applies. If `S_1`
is even but not contained in `4Z`, division by two identifies it with the
order-64 chamber and preserves the weighted zero-sum count. Finally, if
`S_1 subset 4Z`, then for a primitive 256-th root `zeta`,

```text
F(zeta) conjugate(F(zeta)) in Q(zeta_64).
```

Here `L=17`, so every conjugate square is at most `16+2L=50`. Its nonzero
degree-32 small-field norm therefore has absolute value at most

```text
50^32<2^250.
```

The tower identity makes every rational prime divisor of the full collision
norm divide that small norm, contradicting pair feasibility. Thus the three
support chambers are exhaustive and all have `|M_3|<=1732` or a direct
small-field contradiction.

The exact cubic-Hermite certificate has positive strict norm margin at 1732
and negative margin at 1733. Therefore the two quotient chambers also have
collision norm below `2^250`, completing the exclusion. QED.
