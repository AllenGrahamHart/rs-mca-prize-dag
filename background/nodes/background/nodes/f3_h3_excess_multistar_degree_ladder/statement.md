# H3 rich-excess multistar degree ladder

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_rich_fiber_norm_cutoff`,
  `f3_h3_weighted_multistar_router`

Fix a nonzero product target `t` in an odd-characteristic order-`n` row. Put

```text
P=P(t),
D=#{a in A:a^2=t},
m=#{unordered representations E of t with ||v_E||^2<=3}.
```

Then

```text
m >= (P-D)/2-1.                                    (EML1)
```

When `m>=1`, weight squared-distance-four edges among the `m` small
representations by two, distance-six edges by one, and every other edge by
zero. If `W` is total edge weight and `Delta` is maximum incident weight, then

```text
W >= ceil(m(m-4)/2),                               (EML2)

Delta >= L(m):=ceil(2 ceil(m(m-4)/2)/m)
              = m-4  for even m,
                m-3  for odd m.                    (EML3)
```

For a cutoff-18 rich target, write `e=P-18>=1`. Parity and `D<=2` sharpen
`(EML1)` to

```text
m >= 7+ceil(e/2).                                  (EML4)
```

Consequently a rich target has a center of incident weight at least

```text
L(7+ceil(e/2)).                                    (EML5)
```

In particular, degree four is needed only at excess `e=1,2`; every `e>=3`
fiber has a center of weight at least six, and every `e>=7` fiber has one of
weight at least eight. If no center has weight at least six, then necessarily

```text
(P,D)=(19,1) or (20,2).                            (EML6)
```

For any guaranteed center, a minimal leaf set reaching the stated weight has
between `ceil(L/2)` and `L` leaves. The normalized collisions on those leaves
generate an ideal whose norm is divisible by the row prime. Thus `(EML5)` is
an exact fixed-root candidate-sieve ladder, not only a graph estimate.

This theorem does not bound the number of candidate primes or the quotient
weight `R(t)`.
