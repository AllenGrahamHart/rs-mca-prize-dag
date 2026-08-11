# `A=1` quadratic paired split-biform coefficient-MDS gate

- **status:** PROVED
- **closure:** exact full-support kernel test for both pair boundaries
- **consumer:** `rate_half_band_crossing_location`

Let `X` be a set of `R` distinct field points and suppose

```text
G(t,X)=sum_(j=0)^m g_j(X)t^j,
deg_X g_j<=n,                                       (CMG1)
```

has exact row degree `m` at every `x in X`. If the row roots form the
`m`-set `A_x`, write

```text
P_x(t)=product_(delta in A_x)(t-delta)
      =sum_(j=0)^m p_(j,x)t^j.                      (CMG2)
```

Then there are scalars `lambda_x!=0` such that, for every `j`,

```text
g_j(x)=lambda_x p_(j,x),
(lambda_x p_(j,x))_(x in X) in RS[F,X,n+1].         (CMG3)
```

Equivalently, with `L_X(Z)=product_(x in X)(Z-x)`, the explicit matrix

```text
K_((j,l),x)=p_(j,x)x^l/L_X'(x),
0<=j<=m,
0<=l<=R-n-2,                                       (CMG4)
```

has a kernel vector `lambda=(lambda_x)` with every coordinate nonzero.
Writing `lambda_x=g_m(x)` also shows that all elementary-symmetric root
profiles have one common rational interpolation:

```text
p_(j,x)=g_j(x)/g_m(x),
deg g_j,deg g_m<=n,
g_m(x)!=0 on X.                                    (CMG5)
```

Apply this to the two proved split biforms.

## Extremal profile

For `d_A in {0,1}` take the classified split rows. Then

```text
m=e-2,
n=p-3,
R=3p-3+d_A,                                        (CMG6)
```

and `A_x` is the set of off-line supported slopes whose supports contain
`x`. Thus `K_ext` has

```text
R columns,
(e-1)(2p-1+d_A) scalar rows.                        (CMG7)
```

## First strict profile

For the endpoint-missing rows,

```text
m=e-1,
n=p-2,
R=2p+r_A,                                          (CMG8)
```

where `0<=r_A<=e-6`. Thus `K_strict` has

```text
R columns,
e(p+1+r_A) scalar rows.                             (CMG9)
```

In both profiles, a proof that the corresponding matrix has no
full-support kernel excludes that boundary.

## Scope

The theorem does not prove either matrix has full column rank. It replaces
the geometric compatibility question by an exact finite-field kernel
condition; incidence counts without `(CMG3)` are not realizability
certificates.
