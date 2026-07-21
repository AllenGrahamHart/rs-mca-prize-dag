# Audit

1. The trace quotient is `Q_m=U_(m/2-1)(X/2)`, not `C_m-2` itself. The latter
   has the endpoint factors `X^2-4` and doubles every interior root.
2. `Q_m` is squarefree because it represents distinct inversion orbits in
   `mu_m`; gcd degree therefore equals root count without multiplicities.
3. When `q=(p-1)/m` is odd, the proved square-ratio gate permits replacing
   `Q_m` by `Q_(m/2)`. This is an optimization with a proved coverage argument.
4. The exponent in the modular power is `q`, not `m`, `(p-1)/2`, or `p-1`.
5. Compute the power modulo `Q_M`; materializing a degree-`q` polynomial is
   unnecessary and can be infeasible when `p` is large.
6. A gcd degree counts trace IDs. Ordered endpoint ratios have twice this
   count; one trace may support multiple primitive pencils, so those fibers
   remain presently unbounded.
7. The exact rows `(8,137)`, `(16,593)`, and `(32,1249)` have nonconstant
   gcds. They are scalar fixtures, not HGE4 survivors, because no complete
   pencil is asserted.
8. No official-scale run is needed to prove the compiler.
