# Audit

1. The coefficient index is `R-1-k`; the first nonforced coefficient occurs
   at `k=d+1` because `R-d-2=n`.
2. The quotient coefficient `c_k(x)` is monic of degree `k`. Lower powers
   disappear only through the proved moments `S_0,...,S_d=0`.
3. The top-coefficient/omitted-moment change of basis is unitriangular, so
   simultaneous initial vanishing is equivalent in both coordinates.
4. Division by `Lambda` is used only at off-line slopes, where it is nonzero.
5. `H_off` is squarefree; gcd degrees therefore count distinct slopes, while
   repeated top-coefficient vanishing is priced by nested gcds.
6. The verifier uses a small exact finite-field interpolation fixture and
   never constructs an official-size vector or gcd chain.
7. The theorem identifies but does not bound the new flag.
