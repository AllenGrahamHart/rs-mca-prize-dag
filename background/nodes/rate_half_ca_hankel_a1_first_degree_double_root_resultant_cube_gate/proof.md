# Proof

Let `K=F(z)` and put `K_C=K[X]/(Q)`. Since `C` is reduced and every
component is mixed, `K_C` is a finite reduced `K`-algebra of rank `d`; it
need not be a field. On a splitting extension its roots are
`alpha_1,...,alpha_d`. For any nonzero polynomial `P(X)` of degree `b`, the
standard first-polynomial-leading resultant convention gives

```text
Res_X(Q,P)=q_d^b product_(i=1)^d P(alpha_i).          (1)
```

The product on the right is the determinant norm from `K_C`, equivalently
the product of its component field norms. Thus

```text
Norm_(K_C/K)(P)=Res_X(Q,P)/q_d^b.                    (2)
```

The radical cube bridge gives in `K_C`

```text
W^3=P(X)/H(z),                                       (3)
```

with `P=P_3` or `P_2` as in `(RCG2)`. Take the norm of `(3)`. Since
`H(z)` belongs to the base field `K` and the algebra has rank `d`,

```text
Norm(W)^3
 =Norm(P)/H^d
 =Res_X(Q,P)/(q_d^b H^d)
 =Xi_P.                                              (4)
```

This proves `(RCG4),(RCG5)`. The equality is in `F(z)`, not merely after
extension of constants, because `Q,P,H,W` are all defined over `F` in the
retained packets.

For completeness, recall exact cube detection in a rational function
field. If `char F!=3`, unique factorization writes any `Xi in F(z)^x` as a
constant times irreducible factors to integer powers. It is a cube exactly
when every exponent is divisible by three and the constant is a cube in
`F`.

If `char F=3`, the derivative of every cube is zero. Conversely, the kernel
of `d/dz` on `F(z)` is `F(z^3)`. The finite field `F` is perfect, so every
coefficient has a unique cube root; consequently every element of
`F(z^3)` is a cube in `F(z)`. This proves `(RCG6)`. QED.
