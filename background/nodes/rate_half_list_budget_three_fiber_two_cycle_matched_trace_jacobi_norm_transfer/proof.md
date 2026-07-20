# Proof

The post-field dependency retains the primary gap, the exact
constant/Legendre gate, source torsion `r^(32M)=1`, and all relevant data in
`F_p`. Put `u=r^2`. Then

```text
t=u^2,       x=(u+u^(-1))/2=2y^2-1.                 (1)
```

The Gegenbauer and Legendre generating functions give, for every `M`,

```text
F_L(t)=u^L C_L^(1/4)(x),
H_n(t)=u^nP_n(x).                                    (2)
```

Here `L=2M` and the constant gate uses `n=4M-1=2L-1`. Also

```text
epsilon=r^(8L)=r^(16M),       epsilon^2=r^(32M)=1.
```

The trace identity for `T_(8L)` and substitution of `(2)` into the three
constant equations prove `(JNT2)--(JNT3)` and their three squared branch
equations. Since `p=1 mod 2N`, both square roots of `-1` lie in `F_p`; hence
both roots of `s^2=-epsilon` lie there. Factoring each squared equation into
its two signs gives exactly `(JNT4)`.

The field router supplies one additional sign pin. In the nonsplit class it
excluded `r^(2N)=-1`. Since `2N=8L`, this says `epsilon=1`. Thus
`epsilon=-1` can occur only in the split class, proving the assertion after
`(JNT4)`.

We next replay the trace-gcd reduction. Deleted-pair distinctness gives
`x^2!=1`. Chebyshev composition and doubling give

```text
T_(8L)(y)=T_(4L)(x),
T_(4L)=2T_(2L)^2-1,
T_(2L)^2-1=(x^2-1)U_(2L-1)^2.                       (3)
```

Therefore the torsion equation is `G_-=0` for `epsilon=-1` and `G_+=0`
for `epsilon=1`. On `C=0`, replace `P_(2L-1)` by its remainder `R`.
Squaring the three rational reconstructions

```text
y=(R+s)/(2s),       y=(R+s)/(R-s),
y=-2s/(R-s)                                          (4)
```

gives `(JNT6)`. The denominators in `(4)` are nonzero on their corresponding
equations, so every calculation reverses. Three univariate polynomials have
a common algebraic root exactly when their monic gcd is nontrivial. This
proves `(JNT5)--(JNT7)` at the new `L`.

For the even reduction, use the parameter-uniform identities

```text
C_(2M)^(1/4)(x)=((1/4)_M/(1/2)_M)
                 J_M^(-1/4,-1/2)(2x^2-1),
P_(2L-1)(x)=xJ_(L-1)^(0,1/2)(2x^2-1),
T_(2L)(x)=T_L(2x^2-1),
U_(2L-1)(x)=2xU_(L-1)(2x^2-1).                      (5)
```

Every scalar in `(5)` is nonzero because the characteristic exceeds `16M`.
The primary polynomial has no root at `x=0,+/-1`, so none of the removed
factors creates or loses a branch. Division of the odd Legendre polynomial
by the even primary polynomial leaves `xQ(w)`. Substituting that remainder
into `(JNT6)` gives

```text
E_(j,s)(x)=A_j(w)+xB_j(w).                           (6)
```

Multiplying the two choices `x` and `-x` gives the quadratic norm
`F_(j,s)=A_j^2-zB_j^2`. Conversely, a zero of this norm chooses one of the
two nonzero square roots of `z` and recovers a zero of `E_(j,s)`. Equations
`(5)` preserve the matching torsion factor. This proves the exact equivalence
`(JNT8)--(JNT11)`. Since `deg J=M`, reducing every input modulo `J` gives the
new maximum degree `M=2^36`.

It remains to audit the norm interface. For a formal variable `z`, put

```text
w=(z+z^(-1))/2,       H_M(z)=z^M J(w).
```

The polynomial `H_M` is reciprocal of degree `2M`. Pairing roots under
`z<->z^(-1)` and using

```text
T_(2M)(w)=(z^(2M)+z^(-2M))/2,
U_(2M-1)(w)=(z^(2M)-z^(-2M))/(z-z^(-1))             (7)
```

gives the exact resultant identities

```text
R_-^2=2^(2M(2M-1)) Res_z(Phi_(8M),H_M),              (8)

R_+^2=2^(2M(2M-1))
       Res_z((z^(4M)-1)/(z^2-1),H_M).                (9)
```

All Jacobi denominators are powers of two, so odd-prime valuations discard
only the displayed powers of two. Since `M=2^36`, the first order is
`8M=2^39`. Factoring the second binomial into dyadic cyclotomic polynomials
after removing orders one and two gives exactly the `37` orders
`2^2,...,2^38`. This proves `(JNT13)--(JNT14)`.

Iterating `U_(2m-1)=2T_mU_(m-1)` down the dyadic chain gives

```text
U_(2M-1)=2M product_(j=0)^36 T_(2^j),               (10)
```

and multiplicativity of the resultant proves `(JNT15)`. Finally,
`T_(2M)=2T_M^2-1` gives `(JNT16)` over `Q(theta)`. The official congruence
puts a primitive eighth root in `F_p`, so `theta^2=2` is available. Here `M`
is even, and the two degree-`M` resultants are conjugates with product `R_-`.

Any common root in `(JNT11)` first makes `J` share a root with
`K_epsilon`, so its odd characteristic divides the corresponding resultant.
Conversely, absence of every official-compatible divisor of both resultants
removes all six triples in each corresponding `epsilon` packet. A surviving
torsion gcd is only a necessary candidate and must still pass `F_(j,s)` and
the exact twisted-fourth-power compiler. This proves the endpoint semantics
and all claims. QED.
