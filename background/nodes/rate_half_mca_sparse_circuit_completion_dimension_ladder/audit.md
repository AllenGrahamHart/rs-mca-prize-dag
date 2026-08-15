# Audit

1. Deleting a circuit point leaves an independent set, so `dim H_A=11-c`
   is exact.
2. The common-zero bound subtracts the `c-1` zeros already in `A`, leaving
   exactly `q=K-10` possible completions.
3. Equality labels are independent by private completion coordinates.
4. The carrier comparison uses at most `q+9=K-1` coordinates, inside the
   Vandermonde range.
5. A full-rank eleven-set cannot contain two completion labels because its
   quotient intersection is one-dimensional.
6. Formula `b C(m-c+1-b,11-c)` removes every competing completion before
   choosing the remaining coordinates.
7. Every circuit is counted exactly `c` times by deletion; the floor is
   applied after summing the support stratum.
8. Both branches are retained.  The verifier does not assume the
   unstructured branch is geometrically universal.
