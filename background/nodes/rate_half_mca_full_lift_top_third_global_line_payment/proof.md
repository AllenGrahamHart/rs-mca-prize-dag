# Proof

For every selected explanation in the high-deficit union, write `r_i` for
its missed-coordinate allowance.  For any three explanations,

```text
|S_i intersect S_j intersect S_k|
  >= e-(r_i+r_j+r_k)
  >= e-3s
  >= K.
```

Their normalized pair differences are degree-`<K` codewords and both equal
the gauged direction on this triple intersection.  Restriction injectivity
therefore synchronizes the pair directions.  Fixing two anchors puts every
explanation across every high-deficit layer on one affine codeword line.
Families of size at most two are immediate.

Every one of these explanations owns at most one selected slope because
`r_i<=s<e/2`.  The total common agreement core of the affine line is a
simultaneous base/direction support for one codeword pair.  Pair
noncontainment bounds it by `m-1`.  Away from the core, agreement sets for
different line parameters are disjoint.  If `L` is the size of the entire
high-deficit union and `g<=m-1` is the common core size, then

```text
L(m-g)<=N-g,
```

which gives `L<=N-m+1` and proves `(GL1)`.

Deficits at most `H=e-s-1` form the Johnson prefix.  Splitting its owner
weights at `u=floor(e/2)` gives `(e-1)J_u+J_H`.  Every remaining possible
deficit belongs to the synchronized high union, so `(GL1)` proves `(GL2)`.

The primary verifier scans every support in both newly paid intervals with
exact integer arithmetic.  The independent checker reconstructs the
cross-layer triple threshold, a sharp total-core packing model, both
endpoint and adjacent records, and hostile mutations.
