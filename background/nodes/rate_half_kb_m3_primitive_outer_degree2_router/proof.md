# Proof

Write the terminal decomposition as

```text
f=F composed h,       deg(h)=3,       deg(F)=20.
```

The transverse compiler supplies an irreducible non-diagonal component
`C=(h x h)(Gamma)` of the outer self-correspondence, with bidegree `(r,r)`
and `delta*r=12`. Its five possible `(r,delta)` pairs are exactly
`(KBM3-1)`.

Suppose `F` is indecomposable. Its geometric monodromy is primitive, and
`C` corresponds to a point-stabilizer suborbit of size `r`. The complete
GAP `PrimGrp` degree-20 entry is

```text
group          order          subdegrees
PSL(2,19)       3420             1,19
PGL(2,19)       6840             1,19
A20             20!/2            1,19
S20             20!              1,19.
```

The first two rows are the projective-line actions; the last two are the
natural actions. All are two-transitive. Since none contains a subdegree in
`{2,3,4,6,12}`, `F` cannot be indecomposable.

Write `F=F_1 composed q`, where `q` is a proper right factor. Degree
multiplicativity gives

```text
d=deg(q) in {2,4,5,10},
deg(q composed h)=3d in {6,12,15,30}.               (KBM3-2)
```

The imported decomposition route handles every row in `(KBM3-2)`:

1. The complete inner-degree-12 branch is empty.
2. Inner degree 15 violates the source-fiber Riemann--Hurwitz inequality
   and never entered the exhaustive eight-row decomposition adapter.
3. Every inner-degree-30 map factors through an inner-degree-six map.
4. Every inner-degree-six producer is impossible through degree five or
   has an inner-degree-two decomposition.

Thus every degree-three producer either dies in this routing or comes with
a degree-two decomposition of the same endpoint map. Removing the five
degree-three types from the previous eight-type independent frontier leaves
the three degree-two types. QED.
