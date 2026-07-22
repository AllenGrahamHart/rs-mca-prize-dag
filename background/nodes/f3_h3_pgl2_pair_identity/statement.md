# H3 product and quotient fibers are a paired PGL2 intersection

- **status:** PROVED
- **role:** exact reduction supporting the C36' attack

For `t!=0,1`, define

```text
I_inv(t) = #{x in H : 1 + t/(x-1) in H},
I_aff(t) = #{z in H : 1 + t(z-1) in H}.
```

Then

```text
P(t)=I_inv(t),
R(t)=I_aff(t)-1.
```

At an official split row, put

```text
A_t(Z)=(1-t+tZ)^n-1,
C_n(Z)=Z^n-(Z-1)^n,
D_n(Z)=Z^n-1.                                     (PGL1)
```

All three polynomials are squarefree, `deg C_n=n-1`, and

```text
I_inv(t)=deg gcd(A_t,C_n),
I_aff(t)=deg gcd(A_t,D_n).                         (PGL2)
```

Thus the critical score is one moving-polynomial weighted gcd:

```text
I_inv(t)+2I_aff(t)
 =deg gcd(A_t,C_n)+2deg gcd(A_t,D_n).              (PGL3)
```

Consequently, on quotient support `R(t)>=1`, the simultaneous intersection
bound

```text
I_inv(t)+2 I_aff(t) <= 39
```

would imply `P(t)<=35` and close the stronger background M35 route. The exact
pointwise C36' rectangle target is only

```text
I_inv(t)>=19  =>  I_aff(t)<=18,                    (PAIR-RECT)
```

because this is `P(t)>=19 => R(t)<=17`. A convenient stronger scalar
condition on the rich locus is

```text
I_inv(t)+2 I_aff(t) <= 56                          (PAIR56)
```

implies `R(t)<=17`. Hence

```text
X_18=sum_(t!=1)(P(t)-18)_+R(t)
    <=17 sum_(t!=1)P(t)<17n^2,
17X_18<289n^2<300n^2.                              (PAIR57)
```

Thus either `(PAIR-RECT)` or `(PAIR56)` closes C36'. The latter is imposed
only where `P>=19` and has seventeen more score units than the global M35
target, but it is stronger than `(PAIR-RECT)` when `P>19`. The identities and
both implication compilers are proved; neither rectangle emptiness nor either
uniform score bound is claimed. The gcd form is an exact theorem interface,
not a uniform subresultant certificate.
