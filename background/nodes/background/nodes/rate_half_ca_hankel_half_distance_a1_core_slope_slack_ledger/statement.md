# Half-distance `A=1` core-stratified slope-slack ledger

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:** `rate_half_ca_hankel_minimal_index_budget`,
  `rate_half_ca_hankel_exceptional_root_charge`

Consider the half-distance rate-half budget `B=2^39+1`. Put

```text
m=2^37,       rho=r=4m,       N=16m=4rho,       R=8m,
A=R+1-2rho=1.                                           (A1L1)
```

A profile with no generic-rank supported slope already has `T<=rho`. Retain
a live profile with a generic-rank supported slope. Write

```text
Q(U,V;X)=H(X) Qbar(U,V;X),
H=product_(x in S)(X-x),       s=|S|,
d=rho-s,       Delta=d-(1+s)e,                            (A1L2)
```

where `Q` is the primitive generic apolar generator, `e` is its parameter
degree, and `S` is its fixed evaluation-domain core. The exceptional-root
theorem leaves exactly

```text
s=0: m+1<=e<=rho,
s=1: m+1<=e<=floor((rho-1)/2),
s=2: m+1<=e<=floor((rho-2)/3).                          (A1L3)
```

The `e+1` parameter coefficient forms of `Qbar` are linearly independent.
Thus `Qbar` has separation rank exactly `e+1`, traces a degree-`e` rational
normal curve in its coefficient span, and evaluates injectively on `D\S`.

Define the exact Euclidean cap and remainder

```text
L=(N-s)e+Delta,       T_max=floor(L/d),
eta=L-T_max*d,        0<=eta<d.                         (A1L4)
```

They are explicitly

```text
s=0: T_max=4e,       eta=d-e;
s=1: T_max=4e+1,     eta=e;
s=2, 3e<d: T_max=4e+1, eta=3e;
s=2, 3e=d: T_max=4e+2, eta=0.                           (A1L5)
```

Let `Z` be the finite supported-slope set and `T=|Z|`. For `gamma in Z`, let
`ubar_gamma` count the distinct roots of `Qbar_gamma` in `D\S`, and put

```text
O=sum_(gamma in Z)(d-ubar_gamma).
```

If `cbar_gamma` is the rank loss of the contracted residual pencil, then

```text
0<=O<=sum_gamma cbar_gamma<=Delta,       T<=T_max.       (A1L6)
```

If the required half-distance cap `T<=rho+1` fails, define

```text
ell=T_max-T.
```

Every failure lies in the finite range

```text
0<=ell<=T_max-rho-2.                                    (A1L7)
```

For `x in D\S`, let `d_x` count the distinct finite supported roots of the
nonzero form `Qbar(U,V;x)`, and define

```text
C=sum_(x in D\S)(e-d_x).
```

The exact residual incidence ledger is

```text
I=T*d-O=sum_x d_x,
C=ell*d+eta-Delta+O,       0<=C<=ell*d+eta.             (A1L8)
```

At least

```text
max(0,N-s-ell*d-eta)                                   (A1L9)
```

residual domain rows are parameter-saturated. At least `T-Delta` supported
slopes make `Qbar_gamma` squarefree and completely split over `D\S`; at each
such slope `Q_gamma=H Qbar_gamma` is itself a squarefree degree-`rho` domain
locator.

The residual evaluation matrix

```text
W=(Qbar(gamma;x))_(x in D\S,gamma in Z)                (A1L10)
```

is a nonzero-row, nonzero-column word of

```text
RS[D\S,d+1] tensor RS[Z,e+1]
```

with exact rank `e+1` and weight

```text
wt(W)=T((N-s)-d)+O=T(N-rho)+O=(N-s)(T-e)+C.            (A1L11)
```

On the sharp-cap face `ell=0`, homogenize the supported slopes and put

```text
P=product_(gamma in Z)L_gamma,
Rbar=product_(x in D\S)Qbar(U,V;x),
J=product_(gamma in Z)L_gamma^(d-ubar_gamma).
```

There is a homogeneous form `Sbar` such that

```text
J Rbar=P^d Sbar,       deg Sbar=C<=eta.                 (A1L12)
```

If `D_sat` is the saturated residual domain set, `b=(N-s)-|D_sat|`, and
`P_sat(X)=product_(x in D_sat)(X-x)`, then

```text
0<=b<=C<=eta,
Qbar Vbar+P_sat Wbar=P,                                 (A1L13)
deg_(U,V)Vbar=T_max-e,       deg_X Vbar<N-s-b,
deg_(U,V)Wbar<=T_max,        deg_X Wbar<=d-1.
```

The sharp-cap component degrees lie in narrow necessary chambers. Factor
with multiplicity

```text
Qbar=product_i Q_i,       (r_i,e_i)=(deg_X Q_i,deg_(U,V)Q_i),
g=4e-d,       beta=T_max-4e,
lambda=4g+4beta-3s.                                    (A1L14)
```

Every `r_i,e_i` is positive. For `a_i=4e_i-r_i`,

```text
a_i>=0,       sum_i a_i=g,
lambda*e_i-Delta<=T_max*a_i<=lambda*e_i+eta.            (A1L15)
```

The chamber width `(Delta+eta)/T_max` is less than two. Thus each `e_i`
permits at most two `X`-degrees. For `s=1,2` the width is less than one, so
the `X`-degree is unique if it exists; the same is true for `s=0` once
`3e>d`.

At the first live degree `e=m+1`, every failure satisfies

```text
s=0: 0<=ell<=2, #saturated>=5m+1, #clean>=m+3;
s=1: 0<=ell<=3, #saturated>=3m+1, #clean>=2m+5;
s=2: 0<=ell<=3, #saturated>=m+1,  #clean>=3m+7.         (A1L16)
```

This theorem does not exclude any displayed stratum.
