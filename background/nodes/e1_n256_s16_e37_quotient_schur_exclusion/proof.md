# Proof

The parent closes `V>=76`, so consider `V=74`, or `E=37`. In the exact
relaxed slack table, a putative `L=22` has slack `37+66-4(22)=15` and minimum
energy 41, while `L=21` has slack 19 and minimum energy 37. Hence `L<=21`.
Integer partition of energy 37 then gives 29 magnitude profiles. Their four
largest abstract nested-layer caps are

```text
2810 for (5,8),
2630 for (8,5,1),
2630 for (1,9),
2474 for (11,2,2).
```

The quotient inequality proved in the E=38 parent applies unchanged. The
complete E=37 census distributes the exact layer counts over the nine
negation-orbit categories modulo 16, in `Z/128 Z` and after division by two
in `Z/64 Z`. Forty-eight disjoint shards cover 19,732,753 allocations. The
independent checker reconstructs the allocation totals, all displayed
objectives, both chamber refinements, and the source hash.

For `(5,8)`, if the outer support is not contained in `2Z`, split according
to the inner layer `B`. The complete `B not subset 4Z` chamber has cap 2576.
If `B subset 4Z`, divide its eight positive representatives by four. They
form a symmetric 16-point subset of `Z/32 Z` avoiding 0 and 16. Enumerating
the `binom(15,8)=6435` possible sets gives

```text
R(B,B,B)<=174.
```

For every quotient allocation in this chamber, replace its residue bound for
`R(B,B,B)` by the minimum of that bound and 174 before maximizing. The exact
refined maximum is 2560. If the outer support lies in `2Z` but not `4Z`,
division by two preserves the weighted Schur count and gives cap 2576.

For `(1,9)`, the corresponding full caps are 2372 and 2168. For `(8,5,1)`,
the layer sizes are `(28,12,2)`. Its abstract cap 2630 consists of 756 from
`R(A,A,A)`, 2 from the top-layer cubic, and 1872 from all other ordered layer
triples. The quotient census bounds the outer term by 678, and the top layer
`{c,-c}` has no zero-sum triple in a 2-group. Hence this profile is at most
2550. All remaining profiles are at most 2474.

If the full outer support lies in `4Z`, then
`F(zeta)conjugate(F(zeta))` lies in `Q(zeta_64)`. Since `L<=21`, every
conjugate square is at most `16+2L=58`, and its degree-32 small-field norm is
nonzero with absolute value at most `58^32<2^250`. The tower identity from
the E=38 subfield argument again prevents an official row prime from dividing
the collision norm. These cases prove `M_3<=2576` for every live row.

Finally, exact substitution into the rational cubic-Hermite majorant at 14
and 57 shows that 2592 has positive margin against `(125/32)log 2`, while
2593 has negative margin. Since `2576<2592`, the norm is below `2^250`, a
contradiction. QED.
