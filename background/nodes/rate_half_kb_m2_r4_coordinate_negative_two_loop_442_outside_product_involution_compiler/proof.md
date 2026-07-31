# Proof

The exceptional label classifier gives two complete antipodal pairs and one
singleton in each five-set `K`.  Reading their products from `(KB4P-1)`
gives the three rows of `(KB44O-2)`.  The source-facet signature makes the
completed source set antipodal, so the missing label is the negative of the
singleton: `-1` on `H6` and `-l` on either `H8` locus.

The paired-product theorem assigns the row `(KB44O-1)` to a product pair.
Taking the cross product of the two known rows gives `(KB44O-3)`.  The rows
are independent because their four product entries are distinct under the
parent injectivity guards.  The five common label-product correspondences
determine a nonconstant Mobius map `F`; conjugating label negation by `F`
is a nonsingular projective involution.  Hence the cross product is a
nonzero scalar representative of that involution.

Evaluate the homogeneous common-`K` Mobius kernel at the missing label.
After cancellation only by a common scalar, this gives the three fractions
in `(KB44O-4)`.  There is no hidden affine-chart assumption: if the
candidate row is written homogeneously as

```text
[-N,-N xi,H,H xi],                                (1)
```

then every `4 x 4` determinant formed from `(1)` and any three of the five
common rows reduces to zero modulo the appropriate exact row ideal.

To protect the fraction, eliminate `b` and then `l` from each of `N/b,H`
and the row equations.  The twelve resulting integer norms are exactly
`(KB44O-5)`.  Since `b!=0`, both `N` and `H` are nonzero away from
characteristics `2,7,23`.  The deployed prime is outside this set.  Mobius
injectivity and `xi notin K` then make `p_xi` distinct from every common
product.

The source singleton and `xi` are antipodal, so conjugation by `F` proves
that their products obey `(KB44O-3)`.  Independently, substituting
`p_xi=N/H`, clearing `H`, and reducing by each exact row ideal gives zero.

The twelve source labels form six antipodal pairs.  Two pairs are wholly in
`K`, and the singleton in `K` pairs with `xi`; therefore three pairs remain
wholly outside `K`.  Necessity of `(KB44O-3)` for them follows from the
paired-product theorem.  Conversely, the plane perpendicular to the cross
product is spanned by the two independent known rows, so requiring each
remaining row to lie in it is exactly the rank-at-most-two gate. QED.
