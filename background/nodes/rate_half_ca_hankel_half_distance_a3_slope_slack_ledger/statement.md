# Half-distance `A=3` slope-slack rational-normal ledger

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:** `rate_half_ca_hankel_minimal_index_budget`,
  `rate_half_ca_hankel_exceptional_root_charge`

Consider the half-distance rate-half budget `B=2^39+1`. Put

```text
m=2^37,       rho=4m-1,       r=4m=rho+1,
N=16m,        R=8m,           A=R+1-2rho=3.           (HSL1)
```

Retain the live `A=3` moving-kernel branch. The exceptional-root theorem
forces

```text
m+1<=e<=floor(rho/3),       s=0,
delta=rho-3e,                                           (HSL2)
```

where `e` is the parameter degree of the primitive generic apolar generator

```text
Q(U,V;X)=sum_(j=0)^e Q_j(X)U^(e-j)V^j,       deg_X Q=rho. (HSL3)
```

Then `Q_0,...,Q_e` are linearly independent. Thus `Q` has separation rank
exactly `e+1`, and

```text
(U:V) |-> [Q(U,V;X)]                                  (HSL4)
```

is a degree-`e` rational normal curve in its coefficient span. Evaluation on
the order-`N` domain is injective on that span.

Let `Z` be the finite supported-slope set, `T=|Z|`, and define

```text
c_gamma=rho-rank M(gamma),
u_gamma=#(Z(Q_gamma) intersect D),
O=sum_(gamma in Z)(rho-u_gamma).                       (HSL5)
```

Then

```text
0<=O<=sum_gamma c_gamma<=delta,
T<=4e+1.                                               (HSL6)
```

If the half-distance target `T<=rho+2` fails, put

```text
h=4e+1-T.                                              (HSL7)
```

Every failure lies in

```text
0<=h<=4(e-m)-1.                                        (HSL8)
```

For `x in D`, let `d_x` count the distinct finite supported roots of the
nonzero form `Q(U,V;x)` and put

```text
C=sum_(x in D)(e-d_x).
```

The exact incidence ledger is

```text
I=sum_gamma u_gamma=T*rho-O=sum_x d_x,
C=4e-rho+h*rho+O<=e+h*rho.                            (HSL9)
```

At least

```text
max(0,N-e-h*rho)                                      (HSL10)
```

domain rows are parameter-saturated, and at least `T-delta` supported slopes
have generic Hankel rank and make `Q_gamma` squarefree and completely split
over `D`. The supported degree-`r=rho+1` locator then extends that split
factor by one further distinct domain root.

The evaluation matrix

```text
W=(Q(gamma;x))_(x in D,gamma in Z)                    (HSL11)
```

is a nonzero-row, nonzero-column word of

```text
RS[D,rho+1] tensor RS[Z,e+1]
```

with exact rank `e+1` and weight

```text
wt(W)=T(N-rho)+O=N(T-e)+C.                            (HSL12)
```

On the sharp-cap face `h=0`, put

```text
H=product_(gamma in Z)L_gamma,
R(U,V)=product_(x in D)Q(U,V;x),
J=product_(gamma in Z)L_gamma^(rho-u_gamma).
```

There is a homogeneous form `S` such that

```text
J R=H^rho S,
deg J=O<=delta,       deg S=C=4e-rho+O<=e.             (HSL13)
```

If `D_sat` is the saturated domain set, `b=N-|D_sat|`, and
`P_sat(X)=product_(x in D_sat)(X-x)`, then

```text
0<=b<=C<=e,       |D_sat|>=N-e,                        (HSL14)
Q Vbar+P_sat Wbar=H,                                   (HSL15)
deg_(U,V)Vbar=3e+1,       deg_X Vbar<N-b,
deg_(U,V)Wbar<=4e+1,      deg_X Wbar<=rho-1.
```

At least `3e+1-O` supported slopes are generic-rank, completely `D`-split,
and parameter-transverse at every root.

The sharp-cap component degrees are also quantized. Factor with multiplicity

```text
Q=product_i Q_i,       (r_i,e_i)=(deg_X Q_i,deg_(U,V)Q_i),
g=4e-rho=4(e-m)+1.                                      (HSL16)
```

Every `r_i,e_i` is positive. For the distinct component incidence counts
`I_i`, put `E=sum_i I_i-I`,

```text
D_i=T*r_i-I_i,       C_i=N*e_i-I_i.
```

Then

```text
sum_i D_i=O-E,       sum_i C_i=g+O-E.                  (HSL17)
```

For `a_i=4e_i-r_i`,

```text
a_i>=0,       sum_i a_i=g,
4g*e_i-(e-g)<=T*a_i<=4g*e_i+e.                        (HSL18)
```

The interval for `a_i` has width `(2e-g)/T<1/2`; hence each `e_i` permits at
most one component `X`-degree.

At the first live degree `e=m+1`, every failure has

```text
0<=h<=3,       #saturated rows>=N-e-3rho=3m+2,         (HSL19)
```

and at least `T-delta>=3m+6` completely split generic columns. This theorem
does not exclude a stratum and makes no claim about the separate
half-distance `A=1` profile.
