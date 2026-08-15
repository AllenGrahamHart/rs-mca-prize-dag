# Proof

At `K'=10`, dense-root saturation places a ten-dimensional correction space
`V'` inside the ten-dimensional degree-below-ten polynomial space. Thus

```text
V'=F[X]_<10.                                        (1)
```

Vandermonde interpolation gives rank ten on every set of at least ten
distinct evaluation coordinates and rank nine on every nine-set.
Consequently every positive-dimensional component incidence from the
dense-locator theorem is full-rank affine-owner, and every marked nine-set
is a rank-nine owner chart. The kernel and rank-eight alternatives are both
empty.

## Full-density weighted selector

The component-incidence theorem supplies at least

```text
lambda*N_min*C(m',11),
lambda=990810934/10^9,
N_min=274980728111260126                               (2)
```

positive-dimensional incidences `(gamma,T)`. Mark all `C(11,9)=55`
nine-subsets of every `T` and average over the `C(n',9)` nine-sets. One
fixed `B` therefore satisfies

```text
W_B >=ceil(lambda*N_min
            *C(m',9)C(m'-9,2)/C(n',9))
     =11736940042024039.                             (3)
```

This repeats the proved weighted concentrator without the half-lane loss;
the loss is unnecessary because (1) has already made both competing lanes
empty.

## Exact selected-support partitions

Fix the `B` from (3). Its evaluation kernel is spanned by the degree-nine
locator `u` of `B`, so `Z_D(u)=B`. In the affine owner plane, the common
owner core `J` satisfies

```text
B subset J subset Z_D(u),
```

hence `J=B` and `j=9`. Off `B`, every coordinate agreeing with the received
pair belongs to a unique owner petal `P_p`. The residual petal theorem gives

```text
s_p:=|P_p|<=m'-j-1=A-1,
sum_p s_p<=n'-j=S.                                  (4)
```

For a retained record `gamma`, let `L_gamma` be its affine owner line and
let `S_gamma` be its selected support of size `m'`. Because
`B subset S_gamma`, every coordinate of `S_gamma minus B` belongs to a
unique petal whose owner lies on `L_gamma`. Put

```text
x_(gamma,p)=|(S_gamma minus B) intersection P_p|.
```

Then

```text
0<=x_(gamma,p)<=s_p,
sum_(p in L_gamma) x_(gamma,p)=m'-9=A.              (5)
```

Distinct record slopes give distinct affine lines.

Every marked component extension is `T=B union {x,y}`. Both new
coordinates are outside `Z_D(u)=B`. Its affine component has one owner `p`
agreeing with the received pair on `T`; uniqueness off `B` puts both
coordinates in the same petal `P_p`. Therefore a fixed record contributes
at most

```text
sum_p C(x_(gamma,p),2)                              (6)
```

marked extensions. Notice that (5)--(6) use only the chosen support; no
claim about accidental agreements outside `S_gamma` is needed.

## Split-pencil capacity and contradiction

Apply the weighted split-pencil selected-support theorem to (4)--(6), with

```text
A=67473,       S=1048577,
h=floor(1048577/33737)=31.
```

Its three terms are

```text
clean dominant =floor(67471*1048577^2/8)
                =9273161316835569,
balanced       =C(1048577,2)
                =549756338176,
heavy collision=C(31,2)C(67472,2)
                =1058433770040.
```

Thus

```text
W_B<=9274769506943785.                              (7)
```

The lower bound (3) exceeds (7) by

```text
2462170535080254,
```

a contradiction. Hence the rank-nine component target is impossible at
`K'=10`; (1) also excludes the other component lanes on this row.
