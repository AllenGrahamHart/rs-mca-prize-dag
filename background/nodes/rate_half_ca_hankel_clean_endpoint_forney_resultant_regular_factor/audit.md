# Audit

1. `P` is defined without division by `a`; the formal resultant therefore
   extends through boundary values where `a=0`.
2. The Sylvester degree of `P` is fixed at `rho-1`, even if its actual degree
   drops at a specialization.
3. Scaling contributes `a^(rho-1)` from `q=aLambda` and `a^rho` from
   `P=aP_0`; the top cofactor contributes the additional `a^3`, giving the
   final exponent `2rho+2`.
4. The Forney weights are nonzero only on generic rank-`rho` supported
   slopes. Rank-drop slopes are retained in `Delta` and not used in `(FRF7)`.
5. Vandermonde signs depend on root ordering and are absorbed into one fixed
   nonzero constant.
6. The exact `m=1`, `F_17` fixture reconstructs `P` and gives the same
   nonzero resultant at all 17 affine parameters, as predicted by
   `deg Delta=0` and constant `a`.
