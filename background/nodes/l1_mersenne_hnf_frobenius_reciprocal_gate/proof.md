# Proof - L1 Mersenne HNF Frobenius reciprocal gate

Let `x_1,...,x_h` be the roots of `P_s`. They are distinct and nonzero
because `P_s` divides the squarefree polynomial `W^(m(p+1))-1`. By the
root formula for the resultant,

```text
Q_s(Z)=product_(i=1)^h (Z-x_i^m).                    (1)
```

This proves that `Q_s` is monic of degree `h` and has coefficients in
`F_p[s]`. Put `a_0=P_s(0)=binom(s+h-1,h)`. Since `h=m-1` is odd and `m`
is even,

```text
product_i x_i=-a_0,
C(s)=(-1)^h product_i x_i^m=-a_0^m,                  (2)
```

which is (FRG3).

Set `y_i=x_i^m`. The cyclotomic divisibility in (FRG1) gives

```text
y_i^(p+1)=x_i^(m(p+1))=1,
y_i^p=y_i^(-1).                                      (3)
```

The construction of `Q_s` is defined over the prime field. Frobenius on its
coefficients therefore gives

```text
Q_(s^p)(Z)=product_i (Z-y_i^p)=product_i (Z-y_i^(-1)). (4)
```

On the other hand,

```text
Z^h Q_s(1/Z)
 =product_i(1-y_iZ)
 =((-1)^h product_i y_i) product_i(Z-y_i^(-1))
 =C(s)Q_(s^p)(Z).                                    (5)
```

This proves (FRG4). If
`Q_s=sum_(j=0)^h q_j(s)Z^(h-j)`, comparison of the coefficient of
`Z^(h-j)` in (FRG4) gives exactly

```text
C(s)q_j(s^p)=q_(h-j)(s).
```

The dependency proves `s notin F_p`, so `t=s^p` is off the diagonal. This
proves (FRG5).

The coefficients of `P_s`, and hence the resultant coefficients `q_j`, use
only factorial denominators at most `h`; these are invertible because `h<p`.
Thus the system has degree controlled solely by `h,m`. Saturating by `t-s`
retains precisely the Zariski closure of its off-diagonal locus. If that
saturation is the unit ideal after reduction modulo an official `p`, no
off-diagonal `(s,s^p)` can exist, proving the stated closure criterion.

The reverse implication is deliberately not claimed: (FRG4) says that
Frobenius permutes the `m`th-power roots by inversion, which is necessary but
need not identify every root pointwise. Surviving components must therefore
return to the original cyclotomic and inner equations.
