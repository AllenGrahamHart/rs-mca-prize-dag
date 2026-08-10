# Proof

The product-rank parent gives a nonzero maximal minor on every admissible
point, so its cofactor vector spans the one-dimensional kernel of the five
product rows. The displayed extension is obtained by solving the loop
constraint `beta_0+lambda_0 beta_1=0` and the pivot sum constraint. Its scale
is nonzero because the two source labels are nonzero and distinct.

Symbolic replay verifies the first seven row products are identically zero.
The only remaining common conditions are therefore the three other sum-row
dot products. Exact guard factors are divided only after zero-remainder
checks. Saturating their ideal by the complete source/target guard product
and computing a deterministic standard basis completes all sixteen cases.
Every original common row reduces to zero; the dimensions and basis sizes
are exactly those in the statement. Thus the compact ideals are complete on
the guarded cells. QED.
