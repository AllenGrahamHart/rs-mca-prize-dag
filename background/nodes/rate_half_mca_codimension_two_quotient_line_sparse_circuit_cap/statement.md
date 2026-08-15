# Sparse circuits on a codimension-two quotient line

- **status:** PROVED
- **ambient space:** `P_12=F[X]_<12`
- **scope:** rank-ten eleven-subsets of a ten-dimensional subspace

Let `V<=P_12` have dimension ten and put `Lambda=V^perp`, so
`P(Lambda)` is a projective line.  Let `D subset F` be a set of distinct
coordinates and let `S subset D` have size `m>=11`.

For every eleven-set `T subset S` with `rank(ev_T|V)=10`, the intersection

```text
Lambda intersect span{ev_x:x in T}
```

is one-dimensional.  Call its projective point `[lambda_T]` and let `C_T`
be the support of its unique expression in the evaluation functionals on
`T`.  For `c=|C_T|<=5`, put

```text
Q_1(m)=2,

Q_c(m)=max {
  c+1,
  c+floor(e(m-g)/(c-g)) : 1<=e<=c, 0<=g<c
}                                                   (QL1)
```

for `2<=c<=5`.  Then the number of these full-rank eleven-sets satisfies

```text
#{T subset S: |T|=11, rank(ev_T|V)=10, |C_T|<=5}
 <=sum_(c=1)^5 Q_c(m) C(m-c,11-c).                  (QL2)
```

At the official `K'=12` support size `m=67484`, the five terms in `(QL2)`
are

```text
c=1:  1078750868720738453399620490525287637386970
c=2: 10787668542410727707603394807967712004715600
c=3:     2158077224701397279407082869815859503975
c=4:          341120452889213251661148929866641600
c=5:               44231768400528829040414294388775
```

and their sum is

```text
11868577829520852215896202871552159662636920.       (QL3)
```

## Falsifier

Three distinct one-point evaluation labels on one quotient line; a
support-`c` label outside the degree-`c+1` determinantal root set when the
line is not contained in that determinantal locus; a contained-line kernel
map of parameter degree above `c`; a nonfixed domain root occurring in more
than `e` parameter fibers; a full-rank `T` carrying two quotient labels; or
failure of `(QL2)`.
