# Frontier

Use `ell=x1+2*x0+3b` as the primitive coordinate.  The downstream residue
ledger now computes its degree-24 polynomial and factors it into four
quartics and one octic.  Work in those five fields:

1. compute its discriminant and every denominator norm to isolate the finite
   exceptional-`t` locus;
2. express source-square and distinctness guards in `K[ell]`;
3. evaluate the residual colored `BE` cubic and unsquared sum as norms or
   gcds in each factor.

Do not recompute the radical, primitive polynomial, or factorization.  The
24 geometric points belong to the squared generic algebra, not to guarded
source configurations.
