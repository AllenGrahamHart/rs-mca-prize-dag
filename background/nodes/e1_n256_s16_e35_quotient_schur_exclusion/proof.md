# Proof

The parent closes `V>=72`, so consider `V=70`, or `E=35`. In the exact
relaxed slack table, a putative `L=20` has slack 21 and minimum energy 39,
while `L=19` has slack 25 and minimum energy 35. Hence `L<=19`. Integer
partition of energy 35 then gives 21 magnitude profiles. Their four largest
abstract nested-layer caps are

```text
2430 for (3,8),
2258 for (6,5,1),
2110 for (9,2,2),
2098 for (2,6,1).
```

The quotient inequality inherited through the E=36 parent applies unchanged.
The complete E=35 census distributes the exact layer counts over the nine
negation-orbit categories modulo 16, both in `Z/128 Z` and after division by
two in `Z/64 Z`. Thirty-two disjoint shards cover 2,946,287 allocations. The
independent checker reconstructs every allocation total, objective, chamber
maximum, and source hash.

For `(3,8)`, first suppose the outer support is not contained in `2Z`. If the
weight-two layer `B` is not contained in `2Z`, the exact chamber maximum is
2010. Otherwise the complete `Z/64 Z` theorem from the parent gives
`R(B,B,B)<=174`; maximizing this replacement allocation by allocation gives
2152. If the complete outer support lies in `2Z` but not `4Z`, division by two
preserves the weighted Schur count and gives 2100.

For `(6,5,1)`, the layer sizes are `(24,12,2)`. Its abstract cap 2258 consists
of 552 from `R(A,A,A)`, 2 from the top-layer cubic, and 1704 from all other
ordered layer triples. The top layer `{c,-c}` has no zero-sum triple in a
2-group. In the divided chamber, the quotient outer cap 454 therefore gives
2158.

In the odd chamber, a complete enumeration of all 104,750 outer quotient
allocations finds exactly four with `R(A,A,A)>458`, all with value 460. Every
other allocation is at most `458+1704=2162`. For each exceptional outer
allocation, exhaust every nested six-representative middle layer and every
nested one-representative top layer. There are 276 such allocations. Summing
the quotient bound over all 27 ordered layer triples, with the exact zero for
the top-layer cubic, gives maximum 2054. Thus this profile is at most 2162.
All remaining profiles are at most 2110.

If the full outer support lies in `4Z`, then
`F(zeta)conjugate(F(zeta))` lies in `Q(zeta_64)`. Since `L<=19`, every
conjugate square is at most `16+2L=54`, and its degree-32 small-field norm is
nonzero with absolute value at most `54^32<2^250`. The inherited tower
identity prevents an official row prime from dividing the collision norm.
These cases prove `M_3<=2162` for every live row.

Finally, exact substitution into the rational cubic-Hermite majorant at 14
and 57 shows that 2162 has positive margin against `(125/32)log 2`, while
2163 has negative margin. Hence the norm is below `2^250`, a contradiction.
QED.
