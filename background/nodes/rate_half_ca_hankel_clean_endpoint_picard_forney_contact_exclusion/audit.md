# Audit

1. The recurrence range is inclusive: the `(rho+2) x (rho+1)` rectangular
   Hankel matrix has rows `0,...,rho+1`, killing coefficients
   `u^rho,...,u^(2rho+1)`. The first possible tail is `u^(2rho+2)`.
2. The local homogenization is exact:
   `u^(rho-1)P(z;u^(-1))=N(z;u)`.
3. The residual line bundle subtracts contact in the first, domain
   coordinate: `(rho-1,m+1)-(2rho+2,0)=(-rho-3,m+1)`.
4. The Picard sign is retained from the parent:
   `O_C(P_*)=O_C(N,-T)`, not its inverse.
5. The tensor arithmetic is mutation-sensitive:
   `4(-rho-3)+N=-8` and `4(m+1)-T=3`.
6. Smoothness is unnecessary. The restriction sequence only uses that the
   absolutely irreducible biform cuts out an integral Cartier divisor.
7. The exact `m=1`, `F_17` fixture replays all vanished convolution
   coefficients and detects the first permitted `u^(2rho+2)` tail. It audits
   contact only; the cohomology exclusion deliberately starts at `m=4`.
