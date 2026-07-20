# Audit

1. The inverse-locator gap begins only above complement degree `c=h+e`.
2. The comparison `D^(-1)=S^(-2)` is used only below degree `2h`.
3. The threshold `h>=2e+1` is exactly what places `e` consecutive dual-gap
   coefficients before degree `2h`; it cannot be weakened by this proof.
4. The recurrence coefficient at the first backward step is
   `3(c+e)-5e=3h+e=m`, so the characteristic hypothesis is load-bearing.
5. The recurrence would stall at `r=2e/3` if `3|e`. This cannot occur in the
   consumed scope because `e=m-3h` and dyadic `m` is nonzero modulo three.
   Dropping the dyadic hypothesis would require a separate argument.
6. The result is zero-cost. Retaining the older positive boundary or
   necklace debit after applying `(DGE2)` would double-charge the level.
7. The cell `(m,h,e)=(32,9,5)` fails `h>=2e+1` and remains outside the
   exclusion. It is a guard against rounding the threshold incorrectly.
