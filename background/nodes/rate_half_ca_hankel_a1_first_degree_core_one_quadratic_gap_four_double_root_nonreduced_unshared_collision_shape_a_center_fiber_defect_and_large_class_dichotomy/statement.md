# `A=1` shape-A center-fiber defect and large-class dichotomy

- **status:** PROVED
- **closure:** the two small-class defects are the actual center fibers,
  while the large class has an exact rank/factorization dichotomy
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and the notation

```text
m=e-2,       n=(3e-7)/2,       r=sr(G),
G(t,X)=sum_(j=1)^r A_j(t)B_j(X),
V=span{A_j},       W_X=span{B_j}.                 (CFD1)
```

For a center `gamma`, put

```text
V_gamma={f in V:f(gamma)=0}.                      (CFD2)
```

The coordinate projection from the restricted Koszul kernel satisfies

```text
im(pi_gamma)=V_gamma,       rank(pi_gamma)=r-1    (CFD3)
```

for all three centers. For either small source class `M_gamma`, the
locator-interpolation map is also onto this hyperplane:

```text
im(T_gamma)=V_gamma.                              (CFD4)
```

Contracting the minimal tensor in `(CFD1)` identifies `V^*` with `W_X`:

```text
iota(lambda)=sum_j lambda(A_j)B_j(X).             (CFD5)
```

Under this identification, the unique small-class defect is not an
anonymous coefficient form. It is

```text
B_gamma proportional to iota(ev_gamma)=G(gamma,X). (CFD6)
```

If `L_rest,gamma=L_(U_0\M_gamma)`, then the center locator and center
fiber obey

```text
Qbar(gamma,X)=chi_gamma L_rest,gamma(X),
G(gamma,x)=kappa_gamma eta_x L_Mgamma'(x)
                         L_rest,gamma(x)^2
                                      (x in M_gamma),          (CFD7)
```

with nonzero scalars. In particular, the two small defects are two fibers
of the same parameter coefficient map.

Let `gamma_0` be the large-class center. Thus

```text
|M_(gamma_0)|=n+3,
Qbar(gamma_0,X)=chi_0(X-x_*)L_rest,0(X),          (CFD8)
```

where `x_*` is the unique padded center root. Its interpolation map has
exactly one of the following two profiles:

```text
rank T_(gamma_0)=r-1:
  ker(T_(gamma_0)^*)=span{G(gamma_0,X)};

rank T_(gamma_0)=r-2:
  G(gamma_0,X)=(X-x_*)B_0(X)
  for some nonzero B_0 in W_X intersect S_(n-1). (CFD9)
```

In the second branch, the exact heavy-row residual

```text
G(t,x_*)=g_off(t)S_B(t)T_3(t)                    (CFD10)
```

satisfies

```text
ell_(gamma_0) divides T_3,
T_3=ell_(gamma_0)T_2,       deg T_2=2.            (CFD11)
```

## Scope

The theorem does not exclude either large-class rank profile. In the
`r-2` branch the new target is the multiplication chain
`B_0,(X-x_*)B_0 in W_X`; in the `r-1` branch the target is compatibility
of the three center-fiber defects in the common coefficient space.
