# KoalaBear m12 outer-subdegree route cut

- **status:** PROVED
- **scope:** inner-degree-12 transverse branch of KoalaBear `Q=6,s=6,u=2`
- **dependency:** `rate_half_kb_source_pencil_rank_transverse_compiler`
- **consumer:** `rate_half_band_closure`

At inner degree `m=12`, the challenge-field outer map has degree five, one
pole of order five, and five distinct simple zeros in
`K=F_(2130706433^6)`. The transverse compiler initially permits

```text
(r,delta)=(1,48),(2,24),(3,16),(4,12).
```

The `r=3` type is impossible because a separable degree-five map is
indecomposable and its primitive geometric monodromy has no subdegree three.

The non-diagonal `r=1` type would be the graph of a nontrivial deck
automorphism. Since the cover has prime degree five, it would be cyclic. Its
unique pole and second total ramification point are `K`-rational, so after a
`K`-rational domain normalization the outer map is

```text
F(x)=a x^5+b,       a!=0.
```

But `gcd(5,|K|-1)=1`, so fifth power is injective on `K`; such a map cannot
have five distinct simple `K`-rational zeros. Hence `r=1` is impossible.

The only surviving inner-degree-12 transverse types are

```text
(r,delta)=(2,24),(4,12).                            (KB12-1)
```

This removes two of the 26 transverse types. It does not delete the two
survivors, close inner degree 12 or `u=2`, construct an owner, move the
ledger, establish cap `68`, or close the KoalaBear row.

## Falsifier

A primitive degree-five group with subdegree three, or a cyclic degree-five
cover over `K` with one rational total pole and five distinct rational zeros.
