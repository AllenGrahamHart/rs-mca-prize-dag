# L1 balanced-pencil anchor determinant atlas

- **status:** PROVED
- **role:** turn every exact balanced split-pencil neighbor into one canonical
  low-degree determinant and pay each fixed common-complement chart
- **consumer:** `l1_mixed_petal_amplification`

## Balanced coefficient body

Let `H` be an `n`-point evaluation set with squarefree locator `Omega`, fix
an exact shell size `m>k` in the balanced band, and put

```text
w=m-k,       omega=n-m,       s=omega-w=n-2m+k>=1.    (DA1)
```

Use a shifted weak-Popov basis

```text
g_1=(W_1,N_1),       g_2=(W_2,N_2),
det(g_1,g_2)=gamma Omega,       gamma in F^x,
d_1+d_2=omega+w+1,
alpha=omega-d_1,     beta=omega-d_2.                  (DA2)
```

Then `alpha+beta=s-1`. Every exact shell member has a unique primitive
coefficient pair

```text
(W,N)=A g_1+B g_2,       deg A<=alpha,       deg B<=beta,
W monic of degree omega,  N=WP,              gcd(A,B)=1. (DA3)
```

Fix one member `(A_0,B_0,W_0,N_0,P_0)`. On the affine hyperplane of all
degree-capped coefficient pairs whose denominator is monic of degree
`omega`, the map

```text
Delta_0(A,B)=A_0B-B_0A                                  (DA4)
```

is an affine bijection onto `F[Z]_(<=s-1)`, sending the anchor to zero.

Choose Bezout polynomials `u,v` with

```text
uA_0+vB_0=1
```

and put

```text
(J,K)=-v g_1+u g_2,       L_0=Omega/W_0.             (DA4a)
```

Then every point of the monic coefficient body has a unique decomposition

```text
(W,N)=T(W_0,N_0)+Delta_0(J,K),                        (DA4b)
K=JP_0+gamma L_0,
W=T W_0+Delta_0J,
N=WP_0+gamma Delta_0L_0.                              (DA4c)
```

Moreover,

```text
gcd(J,W_0)=1,
gcd(W,W_0)=gcd(Delta_0,W_0).                          (DA4d)
```

For a codeword point `N=WP`, `(DA4c)` is the global Pade identity

```text
W(P-P_0)=gamma Delta_0 L_0.                           (DA4e)
```

## Exact neighbor certificate

For a distinct exact member put

```text
D=gcd(W_0,W),       W_0=DX,       W=DY,
Omega=DXYG,         P-P_0=GR.                           (DA5)
```

Thus `G` is the common agreement locator. Then

```text
Delta_0=D R/gamma,       gcd(Delta_0,W_0)=D.            (DA6)
```

In particular, `Delta_0` determines the neighbor uniquely and recovers its
common complement by one gcd. If

```text
j=s-1-deg D,       h=deg X=deg Y,
```

then necessarily

```text
0<=j<=min(k-1,s-1),
deg G=k-1-j,       h=w+1+j,       deg R<=j.            (DA7)
```

Moreover, `R` is nonzero on every root of `X` and `Y`.

The fixed-owner quotient also lies on the explicit remainder graph

```text
Y=X+rem_X((R/gamma)J).                                (DA7a)
```

## Fixed-owner linear-system bound

Fix a monic divisor `D|W_0` of degree `s-1-j`, and let `C_D` be the exact
neighbors satisfying `gcd(W_0,W)=D`. Define

```text
V_D=span_F({W_0/D} union {W/D: W in C_D}),
r_D=dim(V_D)-1.                                         (DA8)
```

If `C_D` is nonempty, then

```text
1<=r_D<=j+1                                             (DA9)
```

and the unconditional finite bound

```text
|C_D| <= floor( binom(m,r_D)/(h-r_D+1) ).              (DA10)
```

holds. At the top-intersection stratum `j=0`, this is exactly the
one-parameter moving-root payment

```text
|C_D|<=floor(m/(w+1)).                                  (DA11)
```

Summing only this proved fixed-owner bound gives

```text
N_j <= binom(omega,s-1-j)
       max_(1<=r<=j+1) floor(binom(m,r)/(w+j-r+2)),     (DA12)
```

where `N_j` is the number of neighbors with common-agreement deficiency
`j`.

## Scope

The determinant atlas is exact and the fixed-`D` estimate is a theorem, but
`(DA12)` can still be exponential because there may be exponentially many
common-complement owners `D`. It does not prove a row-sharp primitive BC/Q
bound, aggregate different `D`, control growing `j`, or close L1. Its value
is to identify the precise list-side bridge to Przemek's split-pencil
program: `j=0` is a paid projective pencil, while `j>=1` is a
dimension-at-most-`j+1` split linear system with an exact root-matroid basis
ledger. Equations `(DA4b)--(DA4e)` coalesce all owner charts into one
received-word-dependent Pade family; they do not bound the realized gcd
strata of that family.

## Falsifier

Two distinct exact neighbors with the same `Delta_0`; a neighbor for which
`gcd(Delta_0,W_0)!=gcd(W_0,W)`; or a fixed-`D` family violating `(DA10)`.
