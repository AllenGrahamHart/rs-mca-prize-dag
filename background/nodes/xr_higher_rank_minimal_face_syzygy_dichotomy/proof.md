# Proof

The dependency gives, for a rank-two trade with `rho=|X|`,

```text
4<=t<=a+2,       rho>=a+2,
```

and every active row has weight at least `a+1`. Under `(MF1)`, no active row
can have full support `X`: its intersection with any other active row would
then have size at least `a+1`, contradicting the block intersection cap `a`.
Thus every row has exactly one zero in `X` and support size `a+1`. The
rank-two projective-kernel argument in the dependency says that distinct rows
have disjoint noncommon zero sets. Hence their omitted points are distinct,
proving `(MF2)`.

Fix a function `f` on `X`, and let its degree-at-most-`a+1` interpolant be

```text
F(T)=c_(a+1)T^(a+1)+c_aT^a+lower terms.
```

For `S_i=X\{x_i}`, subtracting
`c_(a+1) product_(y in S_i)(T-y)` removes the top term and gives the
degree-at-most-`a` interpolant on `S_i`. Its leading coefficient is

```text
[S_i]f=c_a+c_(a+1)(sum_(x in X)x-x_i).              (1)
```

Thus the facet divided differences of any function are affine-linear in the
omitted point. In particular, there are constants

```text
D_i=chi+delta x_i,       N_i=alpha+beta x_i.         (2)
```

Because `U-gamma_i q` agrees with a degree-less-than-`a` word on the selected
block containing `S_i`, divided differences give

```text
N_i=gamma_i D_i.                                     (3)
```

Suppose first that one selected denominator vanishes, say `D_i=0`. Equation
`(3)` gives `N_i=0`. If the affine form `D` is identically zero, then `(3)`
at two further selected facets forces the affine form `N` to be identically
zero as well. If `D` is not identically zero, both affine forms share the
root `x_i`; on every other selected point their quotient is constant. There
are at least three such points because `t>=4`, so `(3)` would give at least
three equal slopes, contradicting their distinctness. Therefore the only
singular possibility is

```text
D=N=0 identically.                                   (4)
```

By `(1)`, identity `(4)` says that the top two coefficients of both
interpolants vanish. They have degree less than `a`, proving `(MF6)`.

Undo the normalization. The flat-nullity common root set is
`P_0` of size `k-a`; on it both affine directions already agree with kernel
codewords. The normalized degree-less-than-`a` interpolation on `X` lifts to
kernel codewords on the additional `a+2` coordinates. The sets are disjoint,
so the common agreement support has size `k+2`. This proves `(MF7)` and the
printed tangent deficit.

It remains to treat the case in which every selected `D_i` is nonzero.
Equations `(2)--(3)` give the fractional-linear color law `(MF3)`. Its
determinant cannot vanish: a constant quotient would give equal colors at all
`t>=4` selected facets. Scale column `i` of

```text
B=(1; x_i; gamma_i; x_i gamma_i)_i                  (5)
```

by the nonzero denominator `chi+delta x_i`. The scaled column evaluates at
`x_i` the four polynomials

```text
chi+delta T,
T(chi+delta T),
alpha+beta T,
T(alpha+beta T).
```

They span the three-dimensional space of polynomials of degree at most two:
the nonzero Mobius determinant gives rank two in degrees zero and one, and
the multiplied pair supplies the quadratic direction. Since the `x_i` are
distinct and `t>=4`, evaluation is injective on that three-dimensional
space. Hence `rank B=3` and `dim ker B=t-3`.

For `y in X`, factorization of the locator gives

```text
mu_i(y)=(y-x_i)/Lambda'_X(y)
       =1/Lambda'_(S_i)(y)       when y in S_i,
```

and `mu_i(x_i)=0`. Thus `mu_i` is the unique, up to scale, dual-`GRS_a`
word on the `(a+1)`-point facet. Every active row is `c_i mu_i` for some
nonzero `c_i`. At a coordinate `y`,

```text
sum_i c_i mu_i(y)
 =(y sum_i c_i-sum_i c_i x_i)/Lambda'_X(y),
```

and the slope-weighted sum has the same form with `c_i` replaced by
`gamma_i c_i`. Therefore both trade identities hold exactly when

```text
sum_i c_i=sum_i c_i x_i=sum_i gamma_i c_i
 =sum_i gamma_i c_i x_i=0,
```

which is `c in ker B`. This proves `(MF4)--(MF5)` and the completeness of the
regular local relation space.

The singular argument proves that no mixed branch exists. Combining the two
branches with the dependency's lower bound `rho>=a+2` gives the final
post-quotient statement. QED.
