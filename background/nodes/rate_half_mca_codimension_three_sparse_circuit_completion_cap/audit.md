# Audit

1. The empty common zero hypothesis is used only to remove support-one
   circuits.
2. Deleting one point from a circuit leaves an independent set, so
   `dim H_A=11-c` is exact.
3. Generalized MDS counts all common zeros of `H_A`; subtracting the
   `c-1` points of `A` leaves at most three possible completions.
4. Three circuit labels are independent because each has one private
   completion coordinate in the Vandermonde basis on `U`.
5. The carrier comparison uses `|U union D|<=12`, below the thirteen-point
   Vandermonde limit.
6. In the two-completion branch, eleven-sets containing both completions are
   excluded because they have quotient intersection dimension at least two.
7. Each circuit is counted exactly `c` times by deletion; the integer floor
   is taken only after summing one support stratum.
8. Structured and unstructured capacities are both evaluated and the larger
   is retained.
