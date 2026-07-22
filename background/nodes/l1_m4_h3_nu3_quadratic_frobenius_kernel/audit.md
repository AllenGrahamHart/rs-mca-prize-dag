# Audit - L1 m=4, h=3, nu=3 quadratic Frobenius kernel

1. `nu=3` has `H=c!=0` and zero defect by the Cartier successor, not by an
   assumption of squarefreeness.
2. Multiplication of the reduced triple by `X^5` gives degree `4p`, exactly
   a fourth Frobenius power.
3. The integrand has degree `2p-2`; only the missing derivative slot `p-1`
   can obstruct integration.
4. That slot is exactly `[X^(p-5)]U^2`, already zero by `(CRR5)`.
5. Canonical integration kills every `X^(jp)` ambiguity and has degree at
   most `2p-1`.
6. A zero derivative gives a polynomial in `X^p`; perfectness supplies its
   unique coefficientwise `p`th root.
7. The second summand has exact degree `2p` because `a!=0`; this forces
   `Q=X^4-A` to have degree two, not merely at most two.
8. `A(0)=Q(0)=0`, so the quadratic has no constant term.
9. Its leading coefficient satisfies `q_2^p=a`; no base-field equality
   `q_2=a` is asserted.
10. The official primes exceed five, so degree-five comparison is below all
    nonconstant `p`th-power terms.
11. The result is a normal form, not an emptiness theorem.
