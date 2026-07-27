# L1 Mersenne m=16 reciprocal elimination result

Two exact Modal workers close the official `m=16,h=15`, order-zero outer
HNF chamber in characteristic `8191`.

The primary worker constructs

```text
Q_s(Z)=Res_W(P_s(W),Z-W^16)
```

and then the two eliminants `R12` and `R13`. Their exact gcd has degree
`9912`, but its squarefree radical is only

```text
s(s-1) product_(j=1)^15 (s+j).
```

This radical is squarefree and divides `s^8191-s`. Hence every common
reciprocal solution has `s in F_8191`, contradicting the HNF requirement.

The independent worker never constructs `Q_s` by a polynomial resultant. It
uses the companion matrix for multiplication by `W^16`, obtains its
characteristic polynomial from traces and Newton identities, and reproduces
the exact hashes of both eliminants, their gcd, and the radical.

```text
primary app: ap-TFttWNnwIi68tCQ3n32vBn, 16.746444 s, 110 MB
audit app:   ap-myN6sycfDSBAi2okj8hc2P, 12.792499 s, 110 MB
campaign spend: exact bill not queried; conservative bound < $0.05
```

This closes one outer endpoint chamber. It does not treat order one, lower
value degrees, inner lifts, or the aggregate L1 numerator.
