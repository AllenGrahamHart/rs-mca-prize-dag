# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one singular-J0 univariate reduction

Equation (CMR7) gives

```text
dA(q)+144q=0.                                        (1)
```

If `A(q)=0`, then (1) gives `q=0`, contrary to the inherited saturation.
Thus `A(q)!=0`, and (1) is equivalent to (JUR2).

Write the second equation in (CMR7) as

```text
F_W=B(q)-504dq-72d^2q.                              (2)
```

Substituting `d=T/A` and multiplying by `A^2` gives

```text
A^2F_W=A^2B-504qTA-72qT^2=P_W,                     (3)
```

because `T=-144q`. This is (JUR3).

The h=7 conic is

```text
C(q,d)=35q^2+14q(11d^2+27d+27)
        +120(d^4+4d^3+7d^2+6d+3).                  (4)
```

Substituting `d=T/A` and multiplying by `A^4` gives exactly (JUR4):

```text
A^4 C(q,T/A)=P_C(q).                                (5)
```

Since `A!=0`, equations (3)--(5) prove both directions of (JUR5)--(JUR6).
The degree statements follow directly from `deg A=2`, `deg B=3`, and
`deg T=1`: `A^2B` gives the unique degree-seven leading term of `P_W`,
while `35q^2A^4` gives the unique degree-ten leading term of `P_C`.

Finally, two univariate polynomials over a field have no common root in an
algebraic closure exactly when their monic gcd is one. This proves (JUR7)
and the stated candidate interpretation. QED.
