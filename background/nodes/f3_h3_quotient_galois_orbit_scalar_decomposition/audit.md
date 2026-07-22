# Audit

1. Quotient lifts are ordered and exclude the diagonal; their count is
   `(n-1)(n-2)`, not half that value and not `(n-1)^2`.
2. The stabilizer depends on `min(v_2(u),v_2(v))`, because both coordinates
   must be fixed.
3. There is no size-one orbit: two distinct nonzero residues cannot both have
   valuation `s-1`.
4. The degree-`2^j` histogram is `3(2^j-1)`, including the three degree-two
   orbits.
5. Quotient Sidonicity is load-bearing: it identifies action orbits with
   distinct Galois root orbits and makes `Qhat_n` squarefree in characteristic
   zero.
6. Orbit polynomials live over `Z[1/2]`; shifted-root denominators have
   2-power norm, not necessarily unit norm over `Z`.
7. `(QOD8)` is an equality of odd prime radicals. It does not identify
   prime-adic valuations or assert a Chinese-remainder decomposition over
   `Z[1/2]` at bad resultants.
8. Sharding bounds block degree and memory ownership but leaves total degree
   unchanged. No dollar or runtime estimate follows without a pilot.
9. Block counts are not a sound load-balancing proxy. At the first official
   order, the maximum-degree class is just over half the blocks but about
   three quarters of the degree mass. A useful pilot must exercise that
   class; success on only the small classes is not a resource estimate.
