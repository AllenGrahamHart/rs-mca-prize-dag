# Proof

## Reciprocal gap

The separator theorem gives `gamma_0=-h/m`. The same reciprocal substitution
as at the linear and quadratic boundaries gives

```text
(hU-yU')(1-y^m)
 =-m gamma U^2V^2+(m/d^2)y^(h+e)UV(U+V).           (1)
```

Indeed, if `W=y^(m-2h)R(1/y)`, then `UVW=1-y^m` and
`XP'(X)|_(X=1/y)=y^(-h)(hU-yU')`; multiplying the separator identity by
`y^(m-h)UV/d^2` yields `(1)`.

Write `a=d/2`, so

```text
U=S-ay^h,       V=S+ay^h.
```

The Euler operator kills `ay^h`, and `c=h+e<2h`. Therefore, modulo `y^c`,
the factor `1-y^m` is one, the second term of `(1)` has not begun, and
`U^2V^2=S^4`. Hence

```text
hS-yS'=-m gamma S^4 mod y^c.                       (2)
```

For an invertible series `Y`, equation `(2)` is equivalent to

```text
y(Y^(-3))'+3hY^(-3)=-3m gamma mod y^c.             (3)
```

The coefficient of degree `j<c` on the left is multiplied by `3h+j`.
Every such scalar is invertible under the characteristic hypothesis. Since
`S(0)=1`, equation `(3)` has the unique solution `S^(-3)=Z mod y^c`, proving
`(NTB1)`. This also gives the endpoint tower

```text
[y^h]Z^(-1/3)=(P(0)+Q(0))/2,
[y^(h+r)]Z^(-1/3)=0,       1<=r<e.                 (4)
```

## Mason extremality and the passport

Put `Phi=ZS^3`. Equation `(NTB1)` gives `Phi-1=y^cT` for some polynomial
`T`. We first prove `deg S=h`. If `s=deg S<h` and `Phi` is nonconstant, let
`D=deg Phi`. Necessarily `D>=c`, and polynomial Mason applied to

```text
Phi-y^cT=1
```

gives

```text
D<=deg rad(Phi yT)-1
  <=(e+s)+1+(D-c)-1
  =D+s-h,
```

a contradiction. If `Phi` is constant, then `Phi=1`, so the polynomial units
`Z,S` are both constant. Thus `S=1` and
`U=1-ay^h`, `V=1+ay^h`; both supports are full `mu_h` fibers and have a
nontrivial common stabilizer. This contradicts primitivity. Therefore
`deg S=h`.

Its leading coefficient is `(P(0)+Q(0))/2`, so this scalar is nonzero.
Evaluating the separator identity at zero gives

```text
P(0)+Q(0)=P(0)Q(0)G(0).
```

Hence `G(0)` is nonzero. Since `3h+e=m`, the leading coefficient of `Z` is
`-3G(0)/d^2`, also nonzero. Thus `deg Z=e`, `deg Phi=m`, and `deg T=2h`.

Apply Mason once more. The radical degree is at most

```text
deg rad(ZS)+deg rad(yT)<=e+h+1+2h=m+1.
```

Mason supplies the reverse inequality `m+1`. Equality holds throughout.
Consequently `Z,S,T` are squarefree, `Z` and `S` are coprime, and no factor
is lost across the two fibers. Their multiplicities are exactly `(NTB3)`.
The ramification contribution is `2m-2`, so there is no further branch value.

## From covers back to ordered pairs

The tame central-star theorem bounds source-scaling classes of `Phi` by
`N(c,e)`. We show that at most two ordered pair orbits lie above one such
class.

The factor with triple zeros and normalization `S(0)=1` recovers `S`
uniquely from `Phi`; then `Z=Phi/S^3`, and

```text
yZ'+3hZ=-3m gamma
```

recovers `gamma`. At degree `c` in `(1)`, the Euler term vanishes and
`c<2h`, so `UV=S^2` to the required order. Therefore

```text
1/(2a^2)=[y^c](gamma S^4).                          (5)
```

Thus `a^2`, and hence the unordered pair `{U,V}`, is uniquely determined.
The two signs of `a` give at most the two ordered pairs; a swap stabilizer may
identify them, which only lowers the count.

Finally suppose two cyclotomic pairs give source-isomorphic maps. The unique
multiplicity-`c` point forces the source isomorphism to be `y -> alpha y`.
The normalized factors satisfy

```text
S_2(y)=S_1(alpha y),       a_2^2=alpha^(2h)a_1^2,
U_2V_2=D_1(alpha y).
```

Both root unions lie in `mu_m`. Comparing any corresponding root shows
`alpha in mu_m`, so the two pairs were already in the same allowed scaling
orbit. This proves `(NTB4)`.

## Explicit debits

For `e=1`, `(CSN1)` gives `N(h+1,1)=1`. For a dyadic `m=3h+2`, `h` and
`c=h+2` are even, and Burnside gives `N(c,2)=c/2`; these are `(NTB5)`.
Direct substitution in `(CSN1)` gives the five values in `(NTB6)`. Each is
strictly below its level allowance after adding the sharper `e=1` or `e=2`
boundary debit at that level. QED.
