# Proof

The nonharmonic scalar compiler gives, on every source branch,

```text
4tH_(2L-1)(t)^2+y_Xj+2=0,       t=r^4.             (1)
```

By definition of `h_Xj`,

```text
y_Xj+2=4h_Xj^2.                                    (2)
```

The Legendre identity and source torsion give

```text
H_(2L-1)(t)=r^(4L-2)P_(2L-1)(x),
tH_(2L-1)(t)^2=r^(8L)P^2=epsilon P^2.              (3)
```

Equations `(1)--(3)` say `h_Xj^2=-epsilon P^2`. Both square roots of
`-epsilon` lie in `F_p`, so allowing both `s` with `s^2=-epsilon` is exactly
equivalent to `(AJC3)`.

For reference, direct simplification of the six cross ratios gives

```text
h_R0=(-1+iota)(r^2+iota)/(2r),

h_R1=-(r^2+3(1+iota)r+iota)/((r-1)(r-iota)),
h_R2=-(r^2-3(1+iota)r+iota)/((r+1)(r+iota)),

h_P0=-iota(r+1)/(r-1),                              (4)

h_P1=(1+2iota)(5r-4+3iota)/(5(r-iota)),
h_P2=(1-2iota)(5r-4-3iota)/(5(r+iota)).
```

Every denominator in `(4)` is nonzero: a zero would give
`r in {0,+/-1,+/-iota}`, contrary to `r!=0` and `r^4!=1`. The official
characteristic does not divide the displayed integer scalars.

The definition of `x` is equivalent to `(AJC4)`. For each line of `(4)`,
clear its denominator in `h_Xj-v` and take the resultant with `(AJC4)` in
`r`. Since no cleared denominator vanishes on `(AJC4)`, the resultant is zero
exactly when one of the four normalized source lifts passes `(AJC3)`. Direct
quadratic multiplication gives, up to nonzero scalars,

```text
Res_R0=N_R0,
Res_R1=Res_R2=N_R12,
Res_P0=N_P0,
Res_P1=Res_P2=N_P12.                                (5)
```

The inverse roots in `(AJC4)` do not enlarge the role inventory. Directly
from `(4)`, for all six labels,

```text
h_Xj(r^(-1);iota)=h_Xj(r;-iota).                    (6)
```

Gaussian conjugation is one of the allowed source-lift choices in the Mobius
router. Likewise `r -> -r` exchanges `R1,R2`, while the complete four-root
resultants for `P1,P2` coincide. Thus `(5)` is exact for the admitted lift
union. Expanding it gives `(AJC5)--(AJC8)`.

We now perform the second quadratic norm. The standard transformations give

```text
C_L^(1/4)(x)=nonzero_scalar*J(w),
P_(2L-1)(x)=xJ_(L-1)^(0,1/2)(w),                   (7)
```

so on `J=0` one may replace `P` by `xQ`. Put `q_s=sQ` and hence `v=xq_s`.
Reduce each expression in `(AJC5)--(AJC8)` modulo `x^2-z`. The `R1/R2`,
`P0`, and `P1/P2` remainders are respectively

```text
A_R+xB_R,       A_P0+xB_P0,       A_P+xB_P,         (8)
```

with the coefficients printed in `(AJC10)--(AJC12)`. Multiplication by the
conjugate under `x -> -x` gives the three exact norms in `(AJC13)`. Conversely,
if one norm vanishes, one of the two square roots of `z` makes its source
remainder vanish. These two signs are genuine lift choices: replacing `r` by
`iota r` preserves `r^4=t` and sends
`(r^2+r^(-2))/2` to its negative. Thus the second norm adds no source branch.

For `R0`, substitution gives

```text
N_R0=z(q_s^4z-2q_s^2+1).                            (9)
```

The primary polynomial has no root at `x=0`, hence `z!=0`. Since
`q_s^2=s^2Q^2=-epsilon Q^2`, the remaining factor in `(9)` is
`F_R0,epsilon/z` in the equivalent form `(AJC14)`. This recovers the
dedicated `R0` transfer and shows why its two choices of `s` coincide.

Source torsion and the even Chebyshev transformations give

```text
epsilon=-1  iff T_L(w)=0,
epsilon=+1  iff U_(L-1)(w)=0,                       (10)
```

on the primary locus. Thus each original source branch exists through the
primary/torsion/constant stage exactly when its corresponding three
polynomials in `(AJC16)` have a common algebraic root. The four resultant
families and two choices of `s` count as

```text
1 + 2*(1+1+1)=7
```

tests per torsion sign. Reducing every input modulo the degree-`M` polynomial
`J` proves the degree bound and the exact gcd criterion.

Finally, every test contains the same pair `(J,K_epsilon)`. Their two
resultants are exactly the norm pair imported and audited by the dedicated
`R0` transfer: the order-`8M=2^39` minus norm and the plus tower at orders
`2^2,...,2^38`. If an official characteristic divides neither norm, no gcd
in `(AJC16)` can be nontrivial. A divisor only opens the corresponding
scalar replay and later Euclidean gates. This proves the shared prefilter and
all claims. QED.
