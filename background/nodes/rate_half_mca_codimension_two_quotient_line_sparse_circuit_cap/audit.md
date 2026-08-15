# Audit

1. The catalecticant entries use moments only through degree eleven.
2. A support-`c` functional gives rank exactly `c`, not merely at most `c`,
   because both Vandermonde factors have at least `c` rows or columns.
3. The noncontained determinant has degree `c+1`; the contained-line
   cofactor coordinates have degree `c`.
4. Parameters where the chosen row block loses rank are retained as `c`
   explicit exceptions rather than silently resolved by another chart.
5. Parameter gcd cancellation can only lower the kernel-map degree.
6. Fixed roots are counted inside the actual domain, and `g=c` is excluded
   only in the nonconstant (`e>=1`) branch.
7. The `e=0` branch does not bound the number of labels.  It bounds relevant
   full-rank eleven-sets, using `Lambda<=E_T` as the obstruction to two
   labels on one `T`.
8. The five support strata are bounded separately and then summed, so no
   nesting or classification theorem for secant varieties is imported.
