# Proof

On `|X|=a+3`, the dual of normalized `GRS_a` has dimension three. A
rank-three trade row space contained in that dual is therefore the whole
dual code. Choose a polynomial basis. If `C=(c_ij)` is the active-row
coefficient matrix, the two trade identities show that every column of `C`
lies in

```text
ker (1;gamma_i)_(i=1,...,t),
```

which has dimension `t-2`. Since `rank C=3`, one has `t>=5`. Clearing the
common locator denominator gives `(P3E3)`.

A nonzero polynomial of degree at most two has at most two roots in `X`, so
`|Z_i|<=2`. For distinct rows, support containment in their selected blocks
and the pair cap give

```text
a+3-|Z_i union Z_j|
 =|supp(lambda_i) intersect supp(lambda_j)|<=a.
```

Hence

```text
|Z_i union Z_j|>=3.                                  (1)
```

Equation `(1)` excludes an empty zero set, excludes two singletons, makes
all two-sets distinct, and forces a possible singleton to avoid every
two-set. This is `(P3E2)`.

It remains to prove `(P3E4)`. Put

```text
S_i=supp(lambda_i),
Z=sum_i |Z_i|,
U_2=sum_(i<j)|Z_i union Z_j|.
```

Then

```text
sum_i |S_i|=t(a+3)-Z,
sum_(i<j)|S_i intersect S_j|=C(t,2)(a+3)-U_2.       (2)
```

Extend the supports to their selected `(a+h)`-blocks. The number of added
block incidences is

```text
E=t(a+h)-[t(a+3)-Z]=t(h-3)+Z.                       (3)
```

If `q` new coordinates outside `X` carry these incidences, every coordinate
saved relative to private placement creates at least one block-pair
incidence. The unused pair-cap supply in `(2)` is

```text
a C(t,2)-[C(t,2)(a+3)-U_2]=U_2-3C(t,2).
```

Therefore

```text
|union_i A_i|
 >=a+3+t(h-3)+Z-U_2+3C(t,2).                        (4)
```

First suppose there is no singleton. The `Z_i` are `t` distinct graph
edges. If `m_x` is the edge degree at vertex `x`, put

```text
I=sum_x C(m_x,2).
```

Two distinct edges share at most one vertex, so

```text
Z=2t,       U_2=4C(t,2)-I.                          (5)
```

Substitute `(5)` in twice `(4)`, minus `2a+ht`, to obtain

```text
Delta_G>=6+t(h-t-1)+2I.                             (6)
```

If one singleton occurs, the remaining `t-1` zero sets are graph edges and
the singleton is disjoint from all of them. Let `I` count intersecting pairs
among those edges. Then

```text
Z=2t-1,
U_2=3(t-1)+4C(t-1,2)-I.                             (7)
```

Substitution gives

```text
Delta_G>=2+t(h-t+1)+2I.                             (8)
```

This proves `(P3E4)`.

At all three prize rows, the core-size cap gives `t<=960`, while the smallest
`h` is `2^32+1`. Thus `h-t-1>0`; `(6)` is at least six, and `(8)` is still
larger because their constant parts differ by `2t-4>0`. A full minimal core
would have `Delta_G=-e<=0`, contradiction.

Finally, the uniform compiler excludes trade rank one. The prize shell-band
dependency excludes full-core rank two at `d=2`. Any row space on `(P3E1)`
has rank at most the dual-code dimension three, while the argument above
excludes full-core rank three. This proves `(P3E5)`. QED.
