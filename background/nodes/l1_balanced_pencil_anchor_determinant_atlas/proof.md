# Proof

Put

```text
C=F[Z]_(<=alpha) x F[Z]_(<=beta).
```

Its dimension is `alpha+beta+2=s+1`. The coefficient of `Z^omega` in
`AW_1+BW_2` is a nonzero linear functional on `C`, because it takes value
one at the anchor. Hence the monic coefficient body `M` is an affine
hyperplane of dimension `s`.

The map `(DA4)` takes values in `F[Z]_(<=alpha+beta)`, also of dimension
`s`. We prove that its restriction to `M` is injective. If two points of
`M` have the same determinant, their difference `(A,B)` satisfies

```text
A_0B-B_0A=0.
```

The anchor is primitive, so coprimality in the PID `F[Z]` gives

```text
(A,B)=T(A_0,B_0)                                      (1)
```

for some polynomial `T`. The corresponding denominator difference is
`TW_0`. It has zero `Z^omega` coefficient because both original
denominators are monic. If `T` is a nonzero constant, that coefficient is
nonzero; if `deg T>0`, then `deg(TW_0)>omega`, contradicting the coefficient
caps. Thus `T=0`. Equal finite dimensions now prove the affine bijection in
`(DA4)`.

Choose `u,v` with `uA_0+vB_0=1` and define the dual module vector

```text
(J,K)=-v g_1+u g_2.                                   (2)
```

The coefficient pairs `(A_0,B_0)` and `(-v,u)` form a unimodular basis.
Consequently every coefficient pair has the unique form

```text
(A,B)=T(A_0,B_0)+Delta_0(-v,u),                       (3)
```

which proves `(DA4b)` and the denominator formula in `(DA4c)`. The
determinant of the corresponding module vectors is unchanged by this
unimodular basis transformation:

```text
W_0K-JN_0=gamma Omega.                                (4)
```

Since `N_0=W_0P_0` and `Omega=W_0L_0`, cancellation gives

```text
K=JP_0+gamma L_0.                                     (5)
```

Substitution in `(3)` proves the numerator formula in `(DA4c)` and, when
`N=WP`, the Pade identity `(DA4e)`.

If a root `x` of `W_0` were also a root of `J`, then `(5)` would give
`K(x)=gamma L_0(x)!=0`, because `Omega` is squarefree. But `(J,K)` belongs
to the interpolation module, so `K(x)=J(x)U(x)=0`, a contradiction. Hence
`gcd(J,W_0)=1`. Reducing `W=T W_0+Delta_0J` modulo `W_0` now proves the gcd
identity `(DA4d)` for every point of the monic coefficient body.

For the anchor and one neighbor, bilinearity of the module determinant gives

```text
W_0N-WN_0=(A_0B-B_0A) det(g_1,g_2)
          =Delta_0 gamma Omega.                       (6)
```

Since `N=WP` and `N_0=W_0P_0`, the left side is
`W_0W(P-P_0)`. The squarefree divisor decomposition `(DA5)` changes `(6)`
to

```text
D^2XY(P-P_0)=Delta_0 gamma DXYG.                      (7)
```

The two codewords agree with the received word on the roots of `G`, so
`P-P_0=GR`. Cancelling the nonzero polynomial `DXYG` in `(7)` proves the
first identity in `(DA6)`.

At a root of `X`, the neighbor agrees with the received word and the anchor
does not. At a root of `Y`, the anchor agrees and the neighbor does not.
Therefore `P-P_0`, and hence `R`, is nonzero on every root of `X union Y`.
Since `W_0=DX` is squarefree, `Delta_0=DR/gamma` now gives
`gcd(Delta_0,W_0)=D`. The affine bijection already proves that `Delta_0`
determines the complete coefficient pair and hence the neighbor.

Let `g=deg G` and `t=deg X=deg Y`. From `(DA5)`,

```text
t=m-g,       deg D=n-2m+g.                            (9)
```

Using `s=n-2m+k` and `j=s-1-deg D` in `(9)` gives

```text
g=k-1-j,       t=w+1+j.                               (10)
```

Also `deg R<=k-1-g=j`. Nonnegative degrees prove all of `(DA7)`.
Reducing `W=T W_0+Delta_0J` modulo `W_0`, substituting
`(W,W_0,Delta_0)=(DY,DX,DR/gamma)`, and cancelling `D` gives

```text
Y=(R/gamma)J mod X.                                   (11)
```

Both `X` and `Y` are monic of degree `h`, so `Y-X` has degree below `h`.
Taking the canonical remainder in `(11)` proves `(DA7a)`.

It remains to prove `(DA10)`. Fix `D`. By `(DA6)`, every coefficient pair
in `C_D` has determinant `DR` with `deg R<=j`. The affine bijection `(DA4)`
therefore puts these coefficient pairs in an affine space of dimension at
most `j+1`. Division of their denominators by the fixed monic `D` is linear,
so

```text
dim V_D<=j+2,       r_D<=j+1.                         (12)
```

The anchor quotient `X=W_0/D` is monic of degree `h` and every neighbor
quotient `Y=W/D` is a monic degree-`h` divisor supported on the anchor's
`m` agreement points. Distinct exact neighbors have distinct `Y`: otherwise
they agree with the received word on the same `m>=k` points and are the same
degree-below-`k` codeword. Thus a nonempty `C_D` gives `r_D>=1`.

Fix one such `Y` and evaluate the polynomials in `V_D` on its `h` roots.
The kernel is exactly the line spanned by `Y`. Indeed, every member of
`V_D` has degree at most `h`, and a polynomial of degree at most `h`
vanishing on all `h` distinct roots is a scalar multiple of the monic
locator `Y`. Hence the evaluation rows on those roots have rank `r_D`.
They have no loops: `X` belongs to `V_D` and is nonzero at every anchor
agreement point.

A loopless rank-`r` matroid on `h` elements has at least `h-r+1` bases.
Choose one basis; every element outside it belongs to a fundamental circuit
and exchanges with some basis element, producing one distinct additional
basis. Applied here, each neighbor supplies at least `h-r_D+1` independent
`r_D`-subsets of its roots.

No such subset can belong to two neighbors. Its independent evaluation rows
have a one-dimensional kernel in `V_D`, so they determine one projective
polynomial; monicity then determines one `Y`. All roots lie among the
anchor's `m` agreement points. Counting the available `r_D`-subsets proves

```text
|C_D|(h-r_D+1)<=binom(m,r_D),                         (13)
```

which is `(DA10)`. For `j=0`, `(DA9)` forces `r_D=1` and `(10)` gives
`h=w+1`, proving `(DA11)`. Finally there are
`binom(omega,s-1-j)` possible degree-`s-1-j` divisors of `W_0`; summing
`(DA10)` and maximizing over the permitted `r_D` proves `(DA12)`. QED.
