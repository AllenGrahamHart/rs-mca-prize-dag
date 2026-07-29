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

Write the Euclidean division `(DA4f)`. Then

```text
W=(T+Q_Delta)W_0+R_Delta.                             (6)
```

The remainder has degree below `omega`, while `W` and `W_0` are monic of
degree `omega`. Therefore `T+Q_Delta=1`, proving `(DA4g)`.

The coefficient change of basis from `(A,B)` to `(T,Delta_0)` is unimodular,
so

```text
(A,B)=(T,Delta_0)                                    (7)
```

as ideals of `F[Z]`. By the coefficient-content exact-shell theorem, the
complete-agreement guard is therefore exactly
`gcd(Delta_0,1-Q_Delta)=1`.

It remains only to check that a split `W_Delta|Omega` automatically gives a
codeword point. Put

```text
E=gcd(W_Delta,W_0)=gcd(Delta_0,W_0).
```

Since both denominators are squarefree divisors of `Omega`, write
`W_Delta=EY` with `Y|L_0`. Also `E|Delta_0`, so `(DA4c)` gives

```text
N_Delta=W_Delta P_0+gamma Delta_0L_0,
```

and `W_Delta` divides both terms. The shifted-degree cap gives
`deg(N_Delta/W_Delta)<k`. Thus every split point gives one support codeword,
and the content guard makes its displayed support complete. Conversely every
exact member already supplies such a primitive split point. This proves
`(DA4h)`.

For the anchor and one neighbor, bilinearity of the module determinant gives

```text
W_0N-WN_0=(A_0B-B_0A) det(g_1,g_2)
          =Delta_0 gamma Omega.                       (8)
```

Since `N=WP` and `N_0=W_0P_0`, the left side is
`W_0W(P-P_0)`. The squarefree divisor decomposition `(DA5)` changes `(8)`
to

```text
D^2XY(P-P_0)=Delta_0 gamma DXYG.                      (9)
```

The two codewords agree with the received word on the roots of `G`, so
`P-P_0=GR`. Cancelling the nonzero polynomial `DXYG` in `(9)` proves the
first identity in `(DA6)`.

At a root of `X`, the neighbor agrees with the received word and the anchor
does not. At a root of `Y`, the anchor agrees and the neighbor does not.
Therefore `P-P_0`, and hence `R`, is nonzero on every root of `X union Y`.
Since `W_0=DX` is squarefree, `Delta_0=DR/gamma` now gives
`gcd(Delta_0,W_0)=D`. The affine bijection already proves that `Delta_0`
determines the complete coefficient pair and hence the neighbor.

Let `g=deg G` and `t=deg X=deg Y`. From `(DA5)`,

```text
t=m-g,       deg D=n-2m+g.                            (10)
```

Using `s=n-2m+k` and `j=s-1-deg D` in `(10)` gives

```text
g=k-1-j,       t=w+1+j.                               (11)
```

Also `deg R<=k-1-g=j`. Nonnegative degrees prove all of `(DA7)`.
Reducing `W=T W_0+Delta_0J` modulo `W_0`, substituting
`(W,W_0,Delta_0)=(DY,DX,DR/gamma)`, and cancelling `D` gives

```text
Y=(R/gamma)J mod X.                                   (12)
```

Both `X` and `Y` are monic of degree `h`, so `Y-X` has degree below `h`.
Taking the canonical remainder in `(12)` proves `(DA7a)`.

It remains to prove `(DA10)`. Fix `D`. By `(DA6)`, every coefficient pair
in `C_D` has determinant `DR` with `deg R<=j`. The affine bijection `(DA4)`
therefore puts these coefficient pairs in an affine space of dimension at
most `j+1`. Division of their denominators by the fixed monic `D` is linear,
so

```text
dim V_D<=j+2,       r_D<=j+1.                         (13)
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
|C_D|(h-r_D+1)<=binom(m,r_D),                         (14)
```

which is `(DA10)`. For `j=0`, `(DA9)` forces `r_D=1` and `(11)` gives
`h=w+1`, proving `(DA11)`. Finally there are
`binom(omega,s-1-j)` possible degree-`s-1-j` divisors of `W_0`.

For the rank-free fixed-owner payment, take two distinct neighbors in
`C_D`. Their degree-below-`k` codewords agree with each other on at most
`k-1` domain points. Since both individual agreement sets have size `m`,
their complement locators satisfy

```text
deg gcd(W_1,W_2)<=n-2m+k-1=s-1.                      (15)
```

Writing `W_i=DY_i` and `deg D=s-1-j` gives

```text
deg gcd(Y_1,Y_2)<=j.                                  (16)
```

Every `Y_i` is an `h=w+1+j` subset of the anchor's `m` agreement points.
Consequently no `(j+1)`-subset belongs to two different `Y_i`. Counting
these subsets proves `(DA11a)`. Summing the minimum of `(DA10)` and
`(DA11a)` over the possible `D`, and maximizing the former over its unknown
realized rank, proves `(DA12)`. QED.
