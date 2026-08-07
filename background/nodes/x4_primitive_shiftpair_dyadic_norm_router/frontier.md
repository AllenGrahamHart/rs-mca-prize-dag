# Frontier

For each residual `(e,d)` cell, compile the actual first-owner predicates and
use its full effective prefix depth `T=e-d-1`.  Count the coefficient-
primitive vectors whose root fold satisfies

```text
p^ceil(T/2) <= p^(ord_N(p) o_0)
             <= |Norm(beta_0)| <= (4e)^(N/4).
```

Use higher folds only with their exact Frobenius-orbit count and retain every
zero-fold branch.  A useful next theorem must turn the necessary gates into a
population bound or eliminate a region of the Johnson-nonpositive wedge.
