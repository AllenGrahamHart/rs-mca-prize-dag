# Strict `A=3` slope-slack rational-normal ledger

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:** `rate_half_ca_hankel_minimal_index_budget`,
  `rate_half_ca_hankel_exceptional_root_charge`

Consider the strict rate-half budget `B=2^39`. Put

```text
m=2^37,       rho=r=4m-1,       N=16m,       R=8m,
A=R+1-2rho=3.                                      (SSL1)
```

Retain a live moving-kernel branch. The exceptional-root theorem forces

```text
m<=e<=floor(rho/3),       s=0,
delta=rho-3e,                                           (SSL2)
```

where `e` is the parameter degree of the primitive generic apolar generator

```text
Q(U,V;X)=sum_(j=0)^e Q_j(X)U^(e-j)V^j,       deg_X Q=rho. (SSL3)
```

Then the `e+1` coefficient forms `Q_0,...,Q_e` are linearly independent.
Consequently `Q` has separation rank exactly `e+1`, and

```text
(U:V) |-> [Q(U,V;X)]                                  (SSL4)
```

is a degree-`e` rational normal curve in its coefficient span. Evaluation on
the order-`N` domain is injective on that span.

Let `Z` be the finite supported-slope set, `T=|Z|`, and for `gamma in Z` put

```text
c_gamma=rho-rank M(gamma),
u_gamma=#(Z(Q_gamma) intersect D),
O=sum_(gamma in Z)(rho-u_gamma).                       (SSL5)
```

Then

```text
0<=O<=sum_gamma c_gamma<=delta,                        (SSL6)
T<=4e+1.                                               (SSL7)
```

If the desired strict cap `T<=rho+1` fails, define the nonnegative
**slope slack**

```text
h=4e+1-T.                                              (SSL8)
```

Every failure lies in the finite integer range

```text
0<=h<=4(e-m).                                          (SSL9)
```

For `x in D`, let `d_x` be the number of distinct finite supported roots of
the nonzero parameter form `Q(U,V;x)`, and define its total capacity deficit

```text
C=sum_(x in D)(e-d_x).
```

The exact incidence ledger is

```text
I=sum_gamma u_gamma=T*rho-O=sum_x d_x,
C=4e-rho+h*rho+O<=e+h*rho.                            (SSL10)
```

It follows that at least

```text
max(0,N-e-h*rho)                                      (SSL11)
```

domain points are parameter-saturated: their degree-`e` section has `e`
distinct roots in `Z` and divides `product_(gamma in Z)L_gamma(U,V)`. At
least `T-delta` supported slopes have generic Hankel rank and make `Q_gamma`
a squarefree degree-`rho` locator split completely over `D`.

Finally the evaluation matrix

```text
W=(Q(gamma;x))_(x in D,gamma in Z)                    (SSL12)
```

is a nonzero-row, nonzero-column word of

```text
RS[D,rho+1] tensor RS[Z,e+1]
```

with exact matrix rank `e+1` and weight

```text
wt(W)=T(N-rho)+O=N(T-e)+C.                            (SSL13)
```

The sharp-cap stratum `h=0`, equivalently `T=4e+1`, has a uniform low-defect
factorization. Homogenize the supported slopes, put

```text
H=product_(gamma in Z)L_gamma,
R(U,V)=product_(x in D)Q(U,V;x),
J=product_(gamma in Z)L_gamma^(rho-u_gamma).
```

There is a homogeneous form `S` with

```text
J R=H^rho S,
deg J=O<=delta,       deg S=C=4e-rho+O<=e.             (SSL14)
```

Let `D_sat` be the saturated domain set, `b=N-|D_sat|`, and
`P_sat(X)=product_(x in D_sat)(X-x)`. Then

```text
0<=b<=C<=e,       |D_sat|>=N-e,                        (SSL15)
Q Vbar+P_sat Wbar=H,                                   (SSL16)
deg_(U,V)Vbar=3e+1,       deg_X Vbar<N-b,
deg_(U,V)Wbar<=4e+1,      deg_X Wbar<=rho-1.
```

At least `3e+1-O` supported slopes are simultaneously generic-rank,
squarefree and completely `D`-split, and parameter-transverse at every root.

The geometric component degrees on this face are quantized. Factor with
multiplicity

```text
Q=product_i Q_i,       (r_i,e_i)=(deg_X Q_i,deg_(U,V)Q_i),
g=4e-rho=4(e-m)+1.                                      (SSL17)
```

Every `r_i,e_i` is positive. If `I_i` is the distinct `D x Z` incidence
count of `Q_i`, and `E=sum_i I_i-I`, then

```text
D_i=T*r_i-I_i,       C_i=N*e_i-I_i,
sum_i D_i=O-E,       sum_i C_i=g+O-E.                  (SSL18)
```

For

```text
a_i=4e_i-r_i
```

one has

```text
a_i>=0,       sum_i a_i=g,
4g*e_i-(e-g)<=T*a_i<=4g*e_i+e.                        (SSL19)
```

The interval for `a_i` has width

```text
(2e-g)/T<1/2,                                          (SSL20)
```

so the parameter degree `e_i` determines at most one possible integer
`a_i`, and hence at most one possible `r_i=4e_i-a_i`. At `e=m`, `g=1`;
there is exactly one `a_i=1` component and all others have `a_i=0`, recovering
the former defect-one/balanced endpoint profile.

The old first endpoint is the forced specialization `e=m,h=0`, where
`T=4m+1` and `C=1+O<=m`. For every larger `e`, `(SSL8)--(SSL13)` stratify the
previously undifferentiated residual by its exact distance from the sharp
`4e+1` slope cap, while `(SSL14)--(SSL16)` route the entire sharp-cap face to
a low-defect norm-power and complementary factorization and
`(SSL17)--(SSL20)` quantize every geometric component degree. This theorem
does not exclude any of those strata.
