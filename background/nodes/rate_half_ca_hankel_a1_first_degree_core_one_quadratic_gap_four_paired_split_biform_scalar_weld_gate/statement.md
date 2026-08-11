# `A=1` quadratic paired split-biform scalar-weld gate

- **status:** PROVED
- **closure:** exact augmented-kernel test for one common biform
- **consumer:** `rate_half_band_crossing_location`

Let `X` be the `R` classified fixed-domain rows and let `Z` be a selected
set of full-degree zero-excess parameter fibers. Write the monic row and
fiber root polynomials as

```text
P_x(t)=product_(delta in A_x)(t-delta),
F_delta(X)=product_(y in B_delta)(X-y).             (SWG1)
```

On the grid `X times Z`, their zero patterns agree:

```text
P_x(delta)=0 iff F_delta(x)=0.                     (SWG2)
```

For every nonincidence cell, one common biform requires nonzero scalars
`lambda_x,zeta_delta` satisfying

```text
lambda_x P_x(delta)=zeta_delta F_delta(x).         (SWG3)
```

Choose for each `delta` one nonincident anchor `a_delta in X`. Define the
sparse weld matrix `W` by one row for every other nonincident `x`:

```text
(W lambda)_(delta,x)
 =lambda_x P_x(delta)F_delta(a_delta)
  -lambda_(a_delta)P_(a_delta)(delta)F_delta(x).    (SWG4)
```

Every row of `W` has exactly two nonzero entries.

Let `Krow` be the fixed-domain coefficient-MDS matrix from the paired row
gate. Then the row and parameter factorizations are realized by one biform
of bidegree at most `(m,n)` if and only if

```text
[Krow]
[  W ] lambda=0                                    (SWG5)
```

has a vector `lambda` with every coordinate nonzero. In that event the
fiber scalars are forced by

```text
zeta_delta
 =lambda_(a_delta)P_(a_delta)(delta)
    /F_delta(a_delta),                              (SWG6)
```

and the parameter-fiber coefficient-MDS gate follows automatically.

For the extremal profile take

```text
R=3p-3+d_A,       |Z|=2e,       (m,n)=(e-2,p-3),   (SWG7)
```

and for the first strict profile take

```text
R=2p+r_A,         |Z|=p+2,      (m,n)=(e-1,p-2).   (SWG8)
```

The number of weld rows is exactly

```text
sum_(delta in Z)(R-|B_delta intersect X|-1),        (SWG9)
```

and is at least

```text
extremal: 2e(2p-1+d_A),
strict:   (p+2)(p+1+r_A).                           (SWG10)
```

At zero line deficit on the official row these lower bounds are

```text
201487636602438195784362,
 75557863726738957139970.                           (SWG11)
```

## Scope

Neither the weld-row count nor the augmented row count is a rank proof. The
new content is common-biform compatibility; the transposed matrix must not be
counted as independent after `(SWG5)` is imposed.
