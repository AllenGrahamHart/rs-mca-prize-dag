# Proof

The bounded Modal computation reconstructs the six stripped common minors
and all twenty guards from the proved compiler.  In the block order with
the guard inverse first, Singular returns a dimension-one standard basis of
size seven.  Eliminating the inverse and recomputing in lexicographic order
`(r,c,b,t)` returns exactly the four polynomials `(KBC0L-1)`.

The discriminant of `b^2-6b+1` is `32`, whose Legendre symbol modulo `p` is
one.  Its two roots are `1547071505` and `583634934`.  Taking `t=2`, the
last and third lex equations give the two `(r,c)` pairs in `(KBC0L-2)`;
the second lex equation also vanishes.

Most importantly, the launcher does not infer lifting from elimination.
It substitutes both four-tuples directly into the original six stripped
minors and the twenty guards.  It records six zeros and twenty nonzero
values for each tuple.  Hence both are admissible deployed-field common
points. QED.
