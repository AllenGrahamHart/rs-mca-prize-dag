# Proof

In profile 442, the three loop pairs have degree classes `H,H,L`, with
degrees `4,4,2`.  Interchanging the two equal high target pairs and
interchanging the quotient branch values identify all assignments with the
same class at the root slot.  Therefore there are exactly two orbits:
root-low and root-high.  The same argument for the classes `H,L,L` in
profile 433 again gives exactly two.

The common degree equations determine the nonloop edges.  In 442 both join
the two high pairs.  Defect saturation forces the two opposite signed deck
types, so after target sign normalization they are `{1,b}` and `{1,-b}`
in the root-low orbit, or `{1,c}` and `{1,-c}` in the root-high orbit.

In 433 the high pair joins once to each low pair.  This common graph is a
tree.  Changing the signed representative of either low pair absorbs the
two edge signs independently.  For root-low the normalized edges are
`{1,b}` and `{1,c}`.  For root-high they are `{c,1}` and `{c,b}`.

Insert these four records into the proved common-kernel matrix.  Direct
expansion gives

```text
det M_442,L = -xy(b-1)(b+1)(x-1)(x+1)(x-y)(x+y)
                (y-1)(y+1) R_442,L,

det M_442,H = -xy(c-1)(c+1)(x-1)(x+1)(x-y)(x+y)
                (y-1)(y+1) R_442,H,

det M_433,L =  xy(b+1)(c+1)(x-1)(x+1)(x-y)(x+y)
                (y-1)(y+1) R_433,L,

det M_433,H =  xy(b+c)(c+1)(x-1)(x+1)(x-y)(x+y)
                (y-1)(y+1) R_433,H.               (1)
```

The factors outside the residuals are collision or forbidden common-label
guards in the displayed normalizations.  The checker enumerates the role
assignments under branch interchange, constructs all four matrices from
the generic coefficient rows, and verifies `(1)` over the integer
polynomial ring. QED.
