# Proof

## 1. The kernel curve has maximal separation rank

At the strict budget, the syndrome Hankel pencil has

```text
R-r=4m+1 rows,       r+1=4m columns,
generic rank rho=4m-1.                                (1)
```

Its generic right nullity is one. The two-sided minimal-index theorem says
that every singular block has index `e`; hence the unique right singular
block is `L_e`. Its homogeneous kernel vector is, up to signs and reversal,

```text
(U^e,U^(e-1)V,...,UV^(e-1),V^e)^T.                   (2)
```

The `e+1` parameter coefficient vectors in `(2)` are independent. Kronecker
strict equivalence applies one constant invertible transformation to the
column space, so their images remain independent. The rational right kernel
is one-dimensional, and its primitive generator is unique up to a nonzero
constant. Its coefficient vector is the coefficient vector of `(SSL3)` in
the degree-`rho` monomial basis. Therefore `Q_0,...,Q_e` are independent.

The coefficient flattening of `Q` consequently has rank `e+1`, which is also
the largest possible rank at parameter degree `e`. The map `(SSL4)` is the
degree-`e` Veronese map followed by a projective linear isomorphism, hence a
rational normal curve. A degree-at-most-`rho` form vanishing on all `N>rho`
points of `D` is zero, so evaluation on `D` is injective.

## 2. Root omissions and the sharp slope cap

For a supported slope `gamma`, the exceptional-root theorem supplies a
specialized minimal apolar generator of degree `rho-c_gamma`. It divides both
`Q_gamma` and the squarefree degree-`r=rho` domain locator. Thus

```text
rho-c_gamma<=u_gamma<=rho.
```

The local Smith-form ledger in the same theorem gives

```text
sum_gamma c_gamma<=delta=rho-3e.
```

Summing proves `(SSL6)` and

```text
I=sum_gamma u_gamma=T*rho-O.                          (3)
```

The core size is `s=0`. Hence, for every `x in D`, the homogeneous form
`Q(U,V;x)` is nonzero and has at most `e` distinct finite roots. Counting
the same incidences by domain point gives

```text
I=sum_x d_x<=Ne.                                      (4)
```

Equations `(3),(4)` and `(SSL6)` imply

```text
T*rho<=Ne+delta.
```

Since `N=4rho+4`,

```text
Ne+delta=(4e+1)rho+e.
```

The live range has `0<e<rho`, so integrality yields `T<=4e+1`, proving
`(SSL7)`.

Assume now that the strict target fails. Then `T>=rho+2`, while `(SSL7)`
allows the definition `(SSL8)`. It gives

```text
0<=h<=4e+1-(rho+2)=4(e-m),
```

because `rho=4m-1`. This is `(SSL9)`.

## 3. Exact slope-slack and product-code ledgers

By definition and `(3)`,

```text
C=Ne-I=Ne-T*rho+O.
```

Substitute `N=4rho+4` and `T=4e+1-h`:

```text
C=4e-rho+h*rho+O.                                    (5)
```

Using `O<=delta=rho-3e` in `(5)` gives `C<=e+h*rho`, proving `(SSL10)`.
Every nonsaturated domain point has `e-d_x>=1`; hence their number is at
most `C`, which proves `(SSL11)`. At a saturated point the nonzero degree-`e`
parameter form has `e` distinct finite roots in `Z`, so it divides the
squarefree supported-slope polynomial.

At most `delta` supported slopes have positive rank loss. If `c_gamma=0`,
then `u_gamma=rho`; because `Q_gamma` has degree `rho` and divides the
squarefree degree-`rho` locator, it is itself squarefree and completely
`D`-split. This proves the clean-column count.

Each column of `W` is the evaluation on `D` of a nonzero degree-at-most-`rho`
form, and each row is the evaluation on `Z` of a nonzero degree-at-most-`e`
form. Thus `W` lies in the printed tensor-product code and has no zero row or
column. In a failing profile `T>=rho+2>e`, so evaluation on `Z` has full rank
on degree-at-most-`e` forms. Combined with the independence of the `Q_j` and
injectivity on `D`, this proves `rank W=e+1`.

The zero entries of `W` are exactly the `I` incidences. Therefore

```text
wt(W)=NT-I=T(N-rho)+O=N(T-e)+C,
```

which is `(SSL13)`. Finally, `e=m` makes `(SSL9)` force `h=0`; equations
`(SSL8),(5)` become `T=4m+1` and `C=1+O`, recovering the prior endpoint
ledger.

## 4. The sharp-cap norm and complementary factors

Assume `h=0`. For each supported slope, its `u_gamma` distinct domain roots
show that `L_gamma^u_gamma` divides the domain norm `R`. Distinct slope forms
are coprime, so

```text
R=(product_gamma L_gamma^u_gamma)S.                   (6)
```

The residual degree is

```text
deg S=Ne-I=C=4e-rho+O<=e.
```

Multiplying `(6)` by `J` proves `(SSL14)`.

Every nonsaturated domain row contributes at least one to `C`, proving
`b<=C<=e`. For `x in D_sat`, the degree-`e` form `Q(U,V;x)` has `e` distinct
roots in `Z`, so it divides the squarefree degree-`T=4e+1` form `H`. Define

```text
V_x=H/Q(U,V;x),       deg_(U,V)V_x=3e+1.
```

Interpolate every parameter coefficient of `V_x` over the `N-b` saturated
domain points. This gives a biform `Vbar` of parameter degree `3e+1` and
`X`-degree less than `N-b`. The biform `Q Vbar-H` vanishes at every root of
`P_sat`; their distinct linear factors therefore divide it jointly. Choosing
the sign of the quotient gives `(SSL16)`. Its parameter degree is at most
`e+(3e+1)=4e+1`, and division by the degree-`N-b` polynomial `P_sat` gives
`deg_X Wbar<=rho-1`. This proves `(SSL15),(SSL16)`.

Finally at most `delta` supported slopes lose rank, and at most `deg S=C`
supported slope forms divide the residual norm factor. Outside their union,
`Q_gamma` has `rho` distinct domain roots and the norm has order exactly
`rho` at `L_gamma`. Each of those root incidences is therefore transverse.
The number of such slopes is at least

```text
T-delta-C=(4e+1)-(rho-3e)-(4e-rho+O)=3e+1-O.
```

This completes the sharp-cap factorization claims.

## 5. Component-degree quantization

Continue on `h=0` and factor `Q` over the algebraic closure. A component with
parameter degree zero would be a fixed `X`-factor. At any of the proved clean
supported slopes it would split over `D`, contradicting `s=0`. A component
with `X`-degree zero would be a common parameter factor of the primitive
coefficient vector. Thus every `r_i,e_i` is positive.

Let `I_i` count distinct zeros of `Q_i` on `D x Z`. Bezout on each vertical
and horizontal grid line gives

```text
I_i<=T*r_i,       I_i<=N*e_i.
```

Hence `D_i,C_i` in `(SSL18)` are nonnegative. Component overlaps contribute
`E=sum_i I_i-I>=0`; summing the two deficits and using `C=g+O` proves
`(SSL18)`. In particular `E<=O` and

```text
0<=D_i<=O-E<=delta=e-g,
0<=C_i<=g+O-E<=g+delta=e.                             (7)
```

For `a_i=4e_i-r_i`, direct subtraction gives

```text
C_i-D_i=N*e_i-T*r_i=T*a_i-4g*e_i,                    (8)
```

because `N=4rho+4`, `T=4e+1`, and `rho=4e-g`.
If `a_i<0`, equation `(8)` gives

```text
D_i-C_i=4g*e_i-T*a_i>=T>e-g,
```

contradicting `(7)`. Thus `a_i>=0`. Summing its definition gives
`sum_i a_i=4e-rho=g`. Finally `(7),(8)` imply exactly the two inequalities
in `(SSL19)`.

The real interval between those bounds has length `(2e-g)/T`, which is less
than `1/2` because `g>=1` and `T=4e+1`. It contains at most one integer.
When `e=m`, nonnegative integers `a_i` sum to one, so exactly one equals one
and all others vanish. This proves `(SSL17)--(SSL20)`. QED.
