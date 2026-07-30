# Audit

1. The first attempted elimination was retracted at commit `a9761aa7`.
   `Poly(...,b,c,d).coeff_monomial(b)` returns only the coefficient of the
   exact monomial `b*c^0*d^0`, not the full coefficient in `QQ[c,d]`.
2. Both current checkers differentiate in `b`, compare the resulting rational
   `b(c,d)` with the old false constant, and fail unless the mutation is
   detected.
3. The primary checker uses direct matrix inversion, two resultants, and a
   univariate gcd. The independent checker uses a fraction-free DomainMatrix
   solve and cleared Bezout identities over `QQ(d)[c]`.
4. Exceptional support is eliminated in `d` by the independent checker and
   in `c` by the primary checker. The extra `c=-1/2` audit factor forces
   `d=2` or `d=1/2`.
5. Both checkers clear rational coefficient denominators before reducing the
   certificates modulo `2130706433`; they verify the modular gcd supports,
   not merely the characteristic-zero factors.
6. `H=0` is the `z=infinity` projective boundary and is outside this finite
   affine chart. It is not silently deleted.
7. The theorem stops at the necessary q-slice gate and makes no claim about
   the other allocations or full colored quotient identities.
