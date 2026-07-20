# Proof

The primary coefficient identity and the Legendre formula are
parameter-uniform. With `t=u^2=r^4`, they give

```text
F_L(t)=u^L C_L^(1/4)(x),
H_(2L-1)(t)=u^(2L-1)P_(2L-1)(x),                    (1)
```

where `L=2M` and `x=(u+u^(-1))/2`. Since `u` is nonzero, the primary gap is
exactly `C(x)=0`.

The `R0` lift-free constant gate is

```text
4t(1+tH_(2L-1)(t)^2)^2+(t-1)^2=0.                  (2)
```

Put `P=P_(2L-1)(x)`. Equation `(1)` gives

```text
tH_(2L-1)(t)^2
 =u^2 u^(4L-2)P^2
 =u^(4L)P^2
 =r^(8L)P^2
 =epsilon P^2.                                      (3)
```

Also

```text
(t-1)^2/u^2=(u-u^(-1))^2=4(x^2-1).                 (4)
```

Divide `(2)` by `4u^2` and apply `(3)--(4)`. The result is exactly
`E_epsilon(x)=0`, proving the constant equation in `(RJN3)`.

Source torsion gives `epsilon^2=r^(32M)=1`. If
`a=(r+r^(-1))/2`, then the Chebyshev trace identity gives

```text
T_(8L)(a)=epsilon.                                  (5)
```

Since `x=T_2(a)`, composition and doubling give

```text
T_(8L)(a)=T_(4L)(x),
T_(4L)=2T_(2L)^2-1,
T_(2L)^2-1=(x^2-1)U_(2L-1)^2.                      (6)
```

The Gegenbauer primary has no root at zero or `+/-1`: its values there are
nonzero products of integers smaller than the official characteristic.
Therefore `(5)--(6)` are equivalent to `G_-=0` for `epsilon=-1` and
`G_+=0` for `epsilon=1`. Three univariate polynomials have a common
algebraic root exactly when their monic gcd is nontrivial. This proves
`(RJN4)--(RJN5)`.

Use the standard quadratic transformations

```text
C_(2M)^(1/4)(x)=((1/4)_M/(1/2)_M)
                 J_M^(-1/4,-1/2)(w),
P_(4M-1)(x)=xJ_(2M-1)^(0,1/2)(w),
T_(4M)(x)=T_(2M)(w),
U_(4M-1)(x)=2xU_(2M-1)(w),                          (7)
```

where `w=2x^2-1`. Every scalar in `(7)` is invertible. Reduction of the odd
Legendre polynomial modulo the even primary gives `P=xQ` on `J=0`, so

```text
E_epsilon=(1+epsilon x^2Q^2)^2+x^2-1
          =(1+epsilon zQ^2)^2+z-1=F_epsilon.        (8)
```

The harmless factor `2x` in the transformed plus-torsion equation is
nonzero on the primary locus. Thus `(7)--(8)` prove the exact equivalence
`(RJN6)--(RJN7)`. Reducing all inputs modulo the degree-`M` polynomial `J`
gives the degree bound.

The torsion-cyclotomic-norm dependency applies to this same `J` and the same
two torsion polynomials. It proves

```text
R_-^2=2^(2M(2M-1)) Res_z(Phi_(8M),H_M),             (9)

R_+^2=2^(2M(2M-1))
       product_(d=2^j, 2<=j<=38) Res_z(Phi_d,H_M),  (10)
```

with `H_M(z)=z^M J((z+z^(-1))/2)`. These identities depend only on the
primary Jacobi polynomial and torsion sign, not on the later scalar branch.
They are therefore literally the same norm pair used by the matched-cycle
packet at `M=2^36`. This proves `(RJN8)` and the shared-compute assertion.

Finally, in the nonsplit shard `p-1` has exact 2-adic valuation 40. If
`r^p=r`, the power-of-two order of `r` divides `2^40=16M`, so
`epsilon=1`; if `r^p=-r`, then `r^(p-1)=-1` and `epsilon=-1`. The split
shard contains all `32M`th roots and allows both signs. QED.

