# Audit

1. The `delta=0` branch uses a label representation on `B` and checks the
   final support union against `K`.
2. The outside strata `j=1,2,3,4` are disjoint and exhaust every circuit not
   contained in `B`.
3. Deleting an outside point leaves exactly `j-1` outside points.
4. Minimality of the support-four circuit makes every three-point deletion
   independent.
5. The outside-carrier budget spends the deletion points before counting
   outside completions.
6. Every stratum-`j` circuit is divided by exactly `j`, not by four.
7. Floors are taken separately after each exact charge division.
8. The maximum ranges over every permitted `t,delta`; it does not select the
   numerically favorable quotient case.
