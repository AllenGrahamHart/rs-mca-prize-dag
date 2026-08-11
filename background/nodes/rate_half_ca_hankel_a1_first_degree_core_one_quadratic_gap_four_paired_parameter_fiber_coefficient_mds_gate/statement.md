# `A=1` quadratic paired parameter-fiber coefficient-MDS gate

- **status:** PROVED
- **closure:** transposed full-support kernel test on zero-excess slopes
- **consumer:** `rate_half_band_crossing_location`

Let `Z` be a set of `C` distinct field points and suppose

```text
G(t,X)=sum_(i=0)^n h_i(t)X^i,
deg_t h_i<=m.                                       (PMG1)
```

Assume that every selected parameter fiber has exact `X`-degree `n` and
root polynomial

```text
F_delta(X)=product_(x in B_delta)(X-x)
            =sum_(i=0)^n f_(i,delta)X^i,
G(delta,X)=zeta_delta F_delta(X),
zeta_delta!=0.                                      (PMG2)
```

Then, for every `i`,

```text
(zeta_delta f_(i,delta))_(delta in Z)
                 in RS[F,Z,m+1].                   (PMG3)
```

Equivalently, with `L_Z(T)=product_(delta in Z)(T-delta)`, the matrix

```text
Kpar_((i,l),delta)
 =f_(i,delta)delta^l/L_Z'(delta),
0<=i<=n,
0<=l<=C-m-2,                                       (PMG4)
```

has a kernel vector `zeta=(zeta_delta)` with every coordinate nonzero.
Since `f_(n,delta)=1`, all root-coefficient profiles have the common
rational interpolation

```text
f_(i,delta)=h_i(delta)/h_n(delta),
deg h_i,deg h_n<=m,
h_n(delta)!=0 on Z.                                (PMG5)
```

Apply this to arbitrary subsets of the guaranteed zero-excess fibers.

## Extremal profile

Choose `C=2e` fibers. Then

```text
m=e-2,       n=p-3,
Kpar_ext: (p-2)(e+1) rows by 2e columns.            (PMG6)
```

## First strict profile

Choose `C=p+2` fibers. Then

```text
m=e-1,       n=p-2,
Kpar_strict: (p-1)(p+2-e) rows by p+2 columns.      (PMG7)
```

At the official row these dimensions are

```text
extremal: 50371909150609548946088 x 366503875926,
strict:   25185954575671278348969 x 274877906946.   (PMG8)
```

A proof that either matrix lacks a full-support kernel excludes the
corresponding pair boundary.

## Scope

The matrix row counts are not rank proofs. This gate is independent of, and
must remain compatible with, the fixed-domain row gate for the same biform.
