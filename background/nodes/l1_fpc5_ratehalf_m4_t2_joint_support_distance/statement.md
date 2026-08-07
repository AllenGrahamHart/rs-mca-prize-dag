# Rate-half FPC5 joint support distance

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one rate-half `M=4,t=2` source, touched pair, and defect parameter

```text
d=ell+s,       0<=s<ell.
```

For an exact contributor, let `D subset C` be its missed-core set and
`R subset B` its exact background agreement set. Write its primitive
cofactor pair as `(A_1,A_2)`, where `deg A_i<=s`.

For any two distinct exact contributors in this fixed source/pair/`s` cell,

```text
|D intersect D'|+|R intersect R'|<=2s.               (JD1)
```

Equivalently, the combined supports

```text
S=D disjoint_union R subset C disjoint_union B
```

form a variable-weight family with pairwise intersections at most `2s` and

```text
|S|=ell+s+|R|>=ell+2s.                               (JD2)
```

Consequently the complete aggregate at this fixed touched pair and `s`
satisfies the explicit packing bound

```text
L_(s,pair)
 <= floor( binom(k-1+b,2s+1)
           / binom(ell+2s,2s+1) ).                   (JD3)
```

This bound does not choose or sum over background sets. It is polynomial for
each fixed `s`, but its exponent grows with `s`; therefore (JD3) is a proved
aggregate control theorem, not the required uniform prize payment.
