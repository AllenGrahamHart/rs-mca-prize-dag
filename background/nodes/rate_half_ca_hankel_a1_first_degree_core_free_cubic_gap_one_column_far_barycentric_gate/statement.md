# `A=1` core-free cubic gap-one column-far barycentric gate

- **status:** PROVED
- **closure:** strict support difference and exact minimal-union weights
- **consumer:** `rate_half_band_crossing_location`

Retain any core-free cubic double-plus-simple `u=1` packet and the exact
error supports `S_gamma` from `(TSV2)`. For every two distinct supported
slopes,

```text
|S_alpha union S_beta|>=rho+1,                      (CBG1)

|S_beta\S_alpha|>=c_alpha+1,
|S_alpha\S_beta|>=c_beta+1.                         (CBG2)
```

Thus the equality branch `(TSV7)` never occurs in a retained column-far
packet. The first-jet source form at a transverse positive-loss slope always
uses at least `c_alpha+1` source points.

Suppose the pair is on the minimum-union boundary

```text
|S_alpha union S_beta|=rho+1.                       (CBG3)
```

Put

```text
X_(alpha,beta)=S_beta\S_alpha,
P_(alpha,beta)(X)=product_(x in X_(alpha,beta))(X-x).
                                                               (CBG4)
```

Then `|X_(alpha,beta)|=c_alpha+1`. If `alpha` is transverse as in
`(FJP1)`, there is a nonzero scalar `kappa_(alpha,beta)` such that for every
`x in X_(alpha,beta)`,

```text
mu_x R_alpha(x)
 =kappa_(alpha,beta)/P_(alpha,beta)'(x),             (CBG5)
```

where `mu_x` is `(TSV4)`. Equivalently,

```text
lambda_x e_beta(x) Q_min,alpha(x)Q_alpha(x)
 P_(alpha,beta)'(x)
 =kappa_(alpha,beta)(beta-alpha).                   (CBG6)
```

In particular, `R_alpha` has no root in `S_beta\S_alpha` on the
minimum-union boundary. For the three `w=0` packets, `(CBG5)--(CBG6)` apply
in every positive-loss direction of every minimum-union pair. The `w=1`
packet retains only its possible `E_1` exception.

## Scope

When the union has more than `rho+1` points, the Vandermonde nullspace has
dimension greater than one and no barycentric uniqueness is claimed. The
theorem does not prove that minimum-union pairs exist or exclude a packet.
It shows that support cardinality alone is exhausted at `(CBG2)`; further
progress must use the field-valued weights or higher coefficient jets.
