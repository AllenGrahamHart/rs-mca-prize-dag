# Proof

## Quotient bound

Let `G` be `Z/128 Z` or `Z/64 Z`, let `pi:G->Z/16 Z`, and let
`X,Y,Z` be symmetric, zero-free nested layers. Put
`x_r=|X intersect pi^-1(r)|`, and similarly for `y_r,z_r`. For a fixed
target residue `r`, the number of candidate ordered pairs is at most

```text
P_r=sum_s x_s y_(-r-s) - 1_(r=0) min(|X|,|Y|).          (1)
```

The subtraction is exact: symmetry and nesting give precisely
`min(|X|,|Y|)` pairs `(x,-x)`, and none can be completed by the forbidden
target `0`. For each fixed `z` in the target fiber, the map from `x` to `y`
is injective in every residue pair, so there are at most

```text
C_r=sum_s min(x_s,y_(-r-s))                             (2)
```

representations. Therefore

```text
R(X,Y,Z)<=sum_r min(P_r,z_r C_r).                       (3)
```

The same exact triple count may use any layer as the target; the census takes
the minimum of the corresponding bounds.

## Complete residue census

A symmetric zero-free set in `Z/128 Z` is represented by positive distances
`1,...,63`. Their nine negation-orbit capacities modulo 16 are

```text
(3,8,8,8,8,8,8,8,4).
```

After division by two, the positive representatives in `Z/64 Z` are
`1,...,31`, with capacities

```text
(1,4,4,4,4,4,4,4,2).
```

The C++ census enumerates every nonnegative allocation of the exact magnitude
counts to these categories, subject to capacity and the presence of an odd
outer category. It applies (3) to each ordered layer triple. Eighty disjoint
shards cover 43,153,083 allocations. The independent checker verifies the
source hash, shard partition, allocation count by a separate dynamic program,
every displayed maximizing allocation, and the six maxima

```text
2782, 2760, 2580, 2422, 840, 840.
```

The complete packet is
`e38_mod16_quotient_census_result.json`; Modal run
`ap-n57PHWIhpfTIODFu1x2CMu` produced the pinned transcript.

## Magnitude profiles

At `E=38,L<=22`, direct integer partition gives 32 profiles. Their four
largest abstract nested-layer caps are

```text
3012  for (6,8),
2828  for (9,5,1),
2820  for (2,9),
2668  for (12,2,2).
```

The two-layer census directly bounds the first and third profiles. In the
second profile the nested layer sizes are `(30,12,2)`. The abstract cap 2828
contains 870 from `R(A,A,A)`, 2 from `R(C,C,C)`, and 1956 from all remaining
ordered layer triples. The census replaces 870 by 840. Also
`C={c,-c}` has no zero-sum triple in a finite 2-group, so its contribution is
zero. Thus this profile is at most 2796. All remaining profiles are at most
2668 without quotient information.

If an outer support is not contained in `2G`, the order-128 census applies.
If it is contained in `2G` but not `4G`, division by two is a group
isomorphism onto `Z/64 Z`, preserves every weighted Schur count, and makes the
outer support odd. If it lies in `4G`, the proved subfield-norm dependency
excludes the row. These cases are exhaustive, hence `M_3<=2796`.

Finally, the parent's exact cubic at contacts 14 and 57 has positive
six-bit margin whenever `M_3<=2806`. Since `2796<2806`, the collision norm is
strictly below `2^250`, contradicting pair feasibility. QED.
