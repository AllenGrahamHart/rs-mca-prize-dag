# Completion-stratified fixed-union collision charge

- **status:** PROVED
- **correction dimension:** `10`
- **target support:** `2<=d<=9`

Let `V<=P_K` have dimension ten and empty common zero set. Let `D` be a
fixed set of `u` domain points and let `W<=V` have dimension `g`, with every
polynomial in `W` vanishing on `D`. Suppose every independent target
`(d-1)`-deletion has at most `M_d` exact support-`d` completions.

For `1<=j<=d`, put

```text
B_j = min(M_d,K-g-u),   j<=g,
B_j = M_d,              j>g.                         (CS1)
```

Then the number of target support-`d` circuit supports is at most

```text
C(u,d) + sum_(j=1)^d floor(
  C(u,d-j) C(m-u,j-1) B_j / j
).                                                        (CS2)
```

Their selected eleven-set incidence is at most `(CS2) C(m-d,11-d)`.

If `d>=3` and `D` contains a parallel class of size `b`, every binomial
`C(u,r)` in `(CS2)` may be replaced by

```text
I_b(u,r)=C(u-b,r)+b C(u-b,r-1),                    (CS3)
```

with out-of-range binomials zero.

## Falsifier

An exposed deletion for which the inside points cut `W`; an outside
completion budget above `(CS1)`; a circuit missed by its exact outside
stratum; or a support at least three containing two points of the named
parallel class while remaining minimal.
