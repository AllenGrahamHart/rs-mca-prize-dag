# Proof

Fix distinct supported slopes `alpha,beta` and let `f_alpha,f_beta` be their
unique centers. The affine codeword line through those centers differs from
the received pencil by a word pair whose joint support is exactly

```text
S_alpha union S_beta.                               (1)
```

The retained received pair is column-far at radius `rho`. Hence `(1)` has
size at least `rho+1`, proving `(CBG1)`. Since
`|S_alpha|=rho-c_alpha`,

```text
|S_beta\S_alpha|
 =|S_alpha union S_beta|-|S_alpha|
 >=c_alpha+1.                                       (2)
```

Interchanging the slopes proves the other half of `(CBG2)`. This also shows
that the `c_alpha`-point equality case of `(TSV7)` is impossible.

Assume `(CBG3)`. Equation `(2)` is then an equality, so

```text
|X_(alpha,beta)|=c_alpha+1.                         (3)
```

The right-radical equation for the first-jet pairing, in the source form
`(TSV3)`, is

```text
sum_(x in X_(alpha,beta)) mu_x A(x)R_alpha(x)=0
for every deg A<=c_alpha-1.                         (4)
```

The `c_alpha` by `c_alpha+1` evaluation matrix in `(4)` is a Vandermonde
matrix of full row rank. Its nullspace is one-dimensional. For a monic
polynomial

```text
P(X)=product_(x in X_(alpha,beta))(X-x),             (5)
```

the standard Lagrange coefficient identity gives

```text
sum_(x in X_(alpha,beta)) x^j/P'(x)=0,
0<=j<c_alpha.                                       (6)
```

Thus `(1/P'(x))_x` spans that nullspace. Equation `(4)` yields `(CBG5)` for
some scalar `kappa_(alpha,beta)`. This scalar is nonzero: otherwise every
nonzero `mu_x` would force `R_alpha` to vanish at the `c_alpha+1` distinct
points in `(3)`, impossible for a nonzero degree-`c_alpha` polynomial.

Finally substitute `(TSV4)` and

```text
Q_alpha=Q_min,alpha R_alpha                         (7)
```

into `(CBG5)` and clear `P'(x)` and `beta-alpha`. This gives `(CBG6)` and
also proves that `R_alpha(x)` is nonzero throughout the difference set. The
packetwise transversality scope follows directly from the `w` table in the
first-jet theorem. QED.
