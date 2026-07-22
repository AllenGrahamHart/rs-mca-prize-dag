# Audit - L1 m=4, h=3, nu=2 fixed-point certificate

1. The two official characteristics have Mersenne exponents at least three,
   so `ord_n(p)=4` and not merely a divisor of four.
2. Frobenius stability of the fixed fiber uses the prime-field inner
   polynomial and the unique prime-field split value.
3. Orbit lengths divide four, so an odd stable root set has a fixed point.
4. A nonempty intersection with `F_p^*` gives exactly two domain points,
   because `gcd(n,p-1)=2`.
5. The fixed fiber has exactly one of those points: its fixed-point count is
   odd and at most two.
6. The product of roots of `R_0-c` is `c`; the two minus signs from odd degree
   and constant term are accounted for.
7. `K intersect F_p^*={1,-1}` forces `x=+c` or `x=-c`.
8. The opposite point cannot have a conjugate split value because both its
   input and `R_0` are prime-field.
9. The multiplicity equation uses `(3w)^p=3w`, not an integer power
   simplification outside `F_p`.
10. Scaling by `c` is simultaneous in input and output; `c^p=c` preserves
    monicity of the degree-`p` inner polynomial.
11. The complement scaling is monic because `c^(3-3p)=1`, not because
    `c=1`.
12. Passing either scalar sign test is necessary only and does not prove the
    canonical divisibility or construct the complement.
