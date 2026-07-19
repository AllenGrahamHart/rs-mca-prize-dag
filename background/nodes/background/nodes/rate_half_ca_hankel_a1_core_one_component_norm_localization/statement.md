# `A=1` core-one componentwise norm localization

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_max_component_localization`,
  `rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization`

Work at the official core-one maximal-degree sharp cap. Put

```text
m=2^37,       e=2m-1,       d=2e+1,
D_0=N-1=16m-1,       T=4e+1.                          (CNL1)
```

Factor the squarefree residual generator as

```text
Qbar=Q_* product_(i!=*)Q_i,
(r_*,e_*)=(2e_*+1,e_*),       (r_i,e_i)=(2e_i,e_i),
b=sum_(i!=*)e_i=e-e_*.                                (CNL2)
```

For a component `Q_i`, let `u_(i,gamma)` be its number of distinct roots in
`D\S` at a supported slope, let `v_(i,x)` be its number of distinct supported
parameter roots at a residual domain point, and define

```text
D_i=sum_gamma(r_i-u_(i,gamma)),
C_i=sum_(x in D\S)(e_i-v_(i,x)).                      (CNL3)
```

Let `E` be the overlap excess of component incidence sets. Then

```text
sum_i D_i=O-E in {0,1},       0<=E<=O<=1.             (CNL4)
```

All component omissions and all component intersections occur, if at all,
at the unique projective root of the middle-Hankel regular factor `lambda`.
At most one component has `D_i=1`; every other component has `D_i=0`.

The column deficits are exact:

```text
C_*=e-5b-1+D_*,
C_i=5e_i+D_i                         for i!=*.         (CNL5)
```

In particular `C_*>=2`, and the dominant component is completely split in
the parameter direction on at least

```text
D_0-C_*>=14m+5b                                      (CNL6)
```

residual domain rows. A residual component `Q_i` is completely split on at
least `D_0-5e_i-1` such rows.

These deficits lift to exact componentwise norm identities. Homogenize the
supported slopes, set

```text
P=product_(gamma in Z)L_gamma,
R_i=product_(x in D\S)Q_i(U,V;x),
J_i=product_(gamma in Z)L_gamma^(r_i-u_(i,gamma)).
```

There is a homogeneous form `S_i` with

```text
J_i R_i=P^r_i S_i,       deg J_i=D_i,       deg S_i=C_i. (CNL7)
```

For each component let `D_sat,i` be the residual domain rows where
`v_(i,x)=e_i`, let `b_i=D_0-|D_sat,i|`, and put
`P_sat,i(X)=product_(x in D_sat,i)(X-x)`. There are biforms `V_i,W_i` such
that

```text
0<=b_i<=C_i,
Q_i V_i+P_sat,i W_i=P,                                 (CNL8)
deg_(U,V)V_i=T-e_i,       deg_X V_i<D_0-b_i,
deg_(U,V)W_i<=T,          deg_X W_i<=r_i-1.
```

The remaining official object is therefore an irreducible dominant biform
of bidegree `(2e_*+1,e_*)`, separation rank at least five, at most one omitted
slope root, norm residual degree `e-5b-1+D_*`, and at least `14m+5b`
completely split residual domain fibers. This theorem does not exclude that
object or close the stratum.
