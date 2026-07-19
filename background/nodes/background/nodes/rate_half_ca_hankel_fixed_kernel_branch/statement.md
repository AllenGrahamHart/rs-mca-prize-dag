# Fixed-kernel rate-half Hankel branch

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

In the setting of `rate_half_ca_hankel_split_pencil_equivalence`, write

```text
M(Z)=M_r(y_0)+Z M_r(y_1)
```

and let its rank over `F(Z)` be `rho>=1`. Suppose its generic right kernel is
defined over `F`: there is an `(r+1-rho)`-dimensional subspace
`K_0 subset F^(r+1)` such that

```text
ker_{F(Z)} M(Z)=K_0 tensor_F F(Z).                    (HK1)
```

If the received pair is column-far at radius `r`, then

```text
#{gamma in F:
  ker M(gamma) intersects D_r(D)}<=rho.               (HK2)
```

Indeed, every vector of `K_0` is annihilated separately by both endpoint
matrices, so column farness says that `K_0` contains no domain-split locator.
Away from the roots of one nonzero `rho x rho` minor, specialization preserves
rank and the kernel is exactly `K_0`. The minor has degree at most `rho`.

Consequently, throughout the first post-quadratic rate-half range, every
generically rank-deficient pencil satisfying `(HK1)` has at most
`rho<=r<r+1=B*(q)` CA-bad slopes. The same conclusion holds in this branch at
the forced-deficiency endpoint `r=(n-k)/2`. Only pencils whose generic kernel
moves nontrivially with `Z` remain.

The excluded generic-rank-zero case is vacuous for a column-far pair: both
endpoint matrices vanish, so every split locator is common.
