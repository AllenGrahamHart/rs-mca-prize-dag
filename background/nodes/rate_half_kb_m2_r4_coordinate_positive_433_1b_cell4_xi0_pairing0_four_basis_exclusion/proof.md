# Proof

Use the four-basis algebra and global coefficient kernel supplied by
`(KBP1B4-TOWER-1)`.  Write the kernel as

```text
(A_0,A_1,A_2,B_0,B_1,B_2,beta_0,beta_1).
```

The missing mate of the singleton source label has quotient label `-t^2`.
Whenever `A(-t^2)` is invertible, its forced target product is

```text
m=B(-t^2)/A(-t^2).                              (KBP1B4-X0P0-2)
```

For products `u,v`, elimination of a source pair with opposite quotient
labels is the exact quadratic identity

```text
P(u,v)=(p_2q_0-p_0q_2)^2
       -(p_2q_1-p_1q_2)(p_1q_0-p_0q_1),        (KBP1B4-X0P0-3)
```

where `p_i=B_i-uA_i` and
`(q_0,q_1,q_2)=(B_0-vA_0,-B_1+vA_1,B_2-vA_2)`.
For `xi=0`, matching `0` pairs the residual positive and negative `DE`
records, so the necessary target-free cut is `P(m,-m)=0`.

The compiler performs all arithmetic after every multiplication in the
quadratic `t` basis and then in the quadratic `b` basis; `c` is recovered by
the proved linear relation.  It records every determinant inverted in this
process.  If `P(m,-m)=0` on a generic common point, its four-by-four
multiplication determinant, equivalently the quadratic-over-quadratic norm,
vanishes in `F_p(r)`.  This implication does not require either quadratic
algebra to be a field.

For each source-sign row, exact FLINT arithmetic computes the five roots of
the degree-298 norm numerator.  The union with roots of all inverse numerators,
inverse denominators, and the norm denominator contains seven values.  The
compiler then lifts each value through the base quadratic, the `b` quadratic,
and the linear `c` relation, rejecting a point only when an explicit route
guard vanishes.  The five values

```text
r in {0, 1, -1, iota, -iota}
```

hit an `r` guard.  The remaining two values lift only to `t=+/-iota`, so they
hit `t^2+1=0`.  Thus no candidate reaches the route-open common locus.  The
missing-record inverse and every other algebra boundary are included in the
same candidate union, leaving no omitted branch.

The computation is repeated independently for all four source signs.  The
cut is independent of `sigma_c,sigma_o`, so each result pays four target
lanes.  Hence all sixteen stated cases are empty. QED.
