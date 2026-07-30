# Proof

Write `f=F composed h`, with `deg(h)=4` and `deg(F)=15`. The imported
transverse compiler gives an irreducible outer correspondence
`C=(h x h)(Gamma)` of bidegree `(r,r)`, where

```text
delta*r=16,       delta<=16,       r<=14.
```

Hence the four candidate pairs are

```text
(1,16),(2,8),(4,4),(8,2).
```

Suppose first that `F` is indecomposable. Its geometric monodromy is
primitive of degree 15, and `C` corresponds to a point-stabilizer suborbit
of length `r`. The complete primitive catalogue is

```text
group                 nontrivial subdegrees
A7                    14
A6 on two-subsets     6,8
S6 on two-subsets     6,8
PSL(4,2)              14
A15                   14
S15                   14
```

so no primitive outer action has subdegree 1, 2, or 4. Those three types
therefore force `F` to decompose.

Any proper right factor `q` of a degree-15 map has degree 3 or 5. Then

```text
f=(outer composed left factor) composed (q composed h)
```

has inner degree 12 or 20. The complete source-fiber profile theorem
already excludes degree 20: three exceptional four-point source fibers
would contribute `3*4*(5-1)=48` to ramification, above `2*20-2=38`.
The proved inner-degree-12 closure excludes the other route. Thus
`r=1,2,4` have no producer.

For `r=8`, the catalogue leaves exactly `A6,S6` in their degree-15
two-subset actions. A point stabilizer has orbits: the base pair; six
disjoint pairs; and eight pairs meeting the base pair in one point.
A five-cycle fixing the sixth point acts on the 15 pairs as three
five-cycles, matching the outer pole profile `5^3`. Therefore catalogue and
pole data do not delete this survivor. This proves the stated route cut.
