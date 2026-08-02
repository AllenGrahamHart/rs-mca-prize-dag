# Proof

The source-facet theorem makes the five common quotient labels two opposite
pairs and a singleton.  Choosing the singleton and then one of the three
pairings of the other four roles gives `5*3=15` cells.  The two source
square-root signs give four rows per cell, hence 60 rows.

The complete-fiber Vieta theorem gives `(KBP1BC-2)`.  All five product rows
and the loop's zero-sum row are mandatory.  On the open stratum where these
six rows have rank six, extend them by the four remaining sum rows.  The
full matrix has rank at most seven exactly when every pair of those four
rows fails to raise the rank to eight.  These are the six determinants in
`(KBP1BC-3)`.

The compiler constructs each determinant symbolically over the deployed
prime field and makes it primitive.  It then repeatedly divides only by
the printed source/target guard factors in `(KBP1BC-4)`, checking zero
remainder at every division.  On the admissible open set those factors are
units, so raw and stripped zero loci agree.

Modal replay completed all `2*15*4=120` mode/cell/sign cases.  The sealed
result records every role assignment, matrix shape, minor count, polynomial
degree, term count, and digest.  The aggregate histograms and custody
verifier independently account for all 720 raw-plus-stripped minors. QED.
