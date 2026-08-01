# Audit

1. The exact deployed-field computation, not the exploratory `Q(i)`
   reconstruction, proves the claim.
2. Atomic localization is necessary: fast stripping left the factor `t-r`
   although `r^2-t^2` was already a declared nonzero guard.
3. The coordinate `x=c/b` is reversible only because `b` is guarded nonzero;
   the compiler retains that assumption.
4. Generic reconstruction divides by `a1`, so the denominator branch is
   explicitly retained as `a0=a1=0`; it is not silently discarded.
5. Two common-curve eliminants are not outside-system equations and do not
   imply route deletion.
