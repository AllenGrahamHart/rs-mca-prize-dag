# Proof

The actual-census dependency supplies an ordered list of exactly 86
full-conductor vectors.  FLINT computes the resultant of each sparse
polynomial with `X^128+1`; PARI independently computes the same integer
resultants.  The two ordered ledgers coincide.  Exact integer comparison gives
42 distinct values, the printed maximum, and
`12*N_max<2^250<13*N_max`.  The verifier reconstructs the input vector list,
checks both ledgers entry by entry, and repeats the integer inequalities. QED.

