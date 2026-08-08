# Proof

The actual-census dependency supplies the ordered list of 1,232 primitive
vectors.  FLINT and PARI independently compute each resultant with
`X^128+1`; their ordered ledgers agree.  Exact integer arithmetic gives 575
distinct values, the printed maximum, and
`4*N_max<2^250<5*N_max`.  The verifier reconstructs the input list, checks
both arrays entry by entry, and repeats the threshold comparison. QED.

