# Proof - L1 Mersenne HNF m=16 order-zero reciprocal elimination

Retain the notation of the reciprocal-gate dependency. Put

```text
Q_s(Z)=Res_W(P_s(W),Z-W^16)
      =sum_(j=0)^15 q_j(s)Z^(15-j),
C(s)=q_15(s)=-binom(s+14,15)^16.                    (1)
```

Every survivor gives `t=s^8191` and satisfies

```text
F_j(s,t):=C(s)q_j(t)-q_(15-j)(s)=0,   0<=j<=15.    (2)
```

In particular, define

```text
R_12(s)=Res_t(F_1,F_2),
R_13(s)=Res_t(F_1,F_3).                              (3)
```

Weighted homogeneity gives `deg q_j=16j`. Viewed as polynomials in `t`,
`F_1,F_2,F_3` have degrees `16,32,48`, while every coefficient has
`s`-degree at most `240`. Therefore the raw determinant bounds are

```text
deg R_12<=16*240+32*240=11520,
deg R_13<=16*240+48*240=15360.                       (4)
```

Exact polynomial arithmetic in `F_8191[s,t]` gives

```text
deg R_12=11472,       deg R_13=15296,
deg gcd(R_12,R_13)=9912.                             (5)
```

The squarefree radical of that gcd is exactly

```text
G_rad(s)=s(s-1) product_(j=1)^15 (s+j).              (6)
```

It has degree 17, is squarefree, and divides `s^8191-s`. Thus every root of
the common gcd lies in `F_8191`.

The certificate was constructed twice. The primary worker obtains `Q_s`
from the resultant in `(1)`. The independent worker instead builds the
companion matrix for multiplication by `W` in `F_8191(s)[W]/(P_s)`, raises
it to the sixteenth power, and reconstructs the characteristic polynomial
from traces and Newton identities. The two constructions reproduce the
exact hashes of `R_12`, `R_13`, their gcd, and `(6)`. The local verifier
independently expands `(6)`, checks its printed polynomial hash,
squarefreeness, and divisibility into `s^8191-s`.

If a survivor existed, `(2)` would make both resultants in `(3)` vanish at
its value of `s`. Hence `G_rad(s)=0`, so `s in F_8191`. This contradicts
`s notin F_p` in `(MRE1)`. Therefore the complete order-zero chamber is
empty. QED.
