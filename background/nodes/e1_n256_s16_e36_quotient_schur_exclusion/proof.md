# Proof

The parent closes `V>=74`, so consider `V=72`, or `E=36`. In the exact
relaxed slack table, a putative `L=21` has slack 18 and minimum energy 40,
while `L=20` has slack 22 and minimum energy 36. Hence `L<=20`. Integer
partition of energy 36 then gives 26 magnitude profiles. Their four largest
abstract nested-layer caps are

```text
2616 for (4,8),
2448 for (0,9),
2440 for (7,5,1),
2288 for (10,2,2).
```

The quotient inequality inherited through the E=37 parent applies
unchanged. The complete E=36 census distributes the exact layer counts over
the nine negation-orbit categories modulo 16, both in `Z/128 Z` and after
division by two in `Z/64 Z`. Forty-eight disjoint shards cover 8,144,380
allocations. The independent checker reconstructs every allocation total,
objective, chamber maximum, and source hash.

For `(4,8)`, first suppose the outer support is not contained in `2Z`. If
the weight-two layer `B` is not contained in `2Z`, the exact chamber maximum
is 2208. Otherwise division of `B` by two produces a symmetric 16-point
subset of `Z/64 Z` avoiding 0 and 32. A separate exhaustive census of all
`binom(31,8)=7,888,725` such subsets proves

```text
R(B,B,B)<=174.
```

Replacing the quotient bound for this term by 174 and maximizing the full
expression allocation by allocation gives 2344. If the complete outer
support lies in `2Z` but not `4Z`, division by two preserves the weighted
Schur count; the same refinement gives 2332.

For `(0,9)`, the odd-support chamber is at most 2000, while the divided
chamber is at most 1924. For `(7,5,1)`, the layer sizes are `(26,12,2)`.
Its abstract cap 2440 consists of 650 from `R(A,A,A)`, 2 from the top-layer
cubic, and 1788 from all other ordered layer triples. The quotient census
bounds the outer term by 556 in the odd chamber and 540 in the divided
chamber. The top layer `{c,-c}` has no zero-sum triple in a 2-group. Hence
this profile is at most `556+1788=2344`. All remaining profiles are at most
2288.

If the full outer support lies in `4Z`, then
`F(zeta)conjugate(F(zeta))` lies in `Q(zeta_64)`. Since `L<=20`, every
conjugate square is at most `16+2L=56`, and its degree-32 small-field norm is
nonzero with absolute value at most `56^32<2^250`. The tower identity used
in the preceding subfield exclusions prevents an official row prime from
dividing the collision norm. These cases prove `M_3<=2344` for every live
row.

Finally, exact substitution into the rational cubic-Hermite majorant at 14
and 57 shows that 2377 has positive margin against `(125/32)log 2`, while
2378 has negative margin. Since `2344<2377`, the norm is below `2^250`, a
contradiction. QED.
