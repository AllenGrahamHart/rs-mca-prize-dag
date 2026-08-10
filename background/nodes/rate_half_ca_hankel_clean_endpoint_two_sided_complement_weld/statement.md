# Clean-endpoint two-sided complement weld

- **status:** PROVED
- **closure:** exact interpolation and coprime elimination
- **consumer:** `rate_half_band_crossing_location`

Retain the clean hypothetical endpoint of
`rate_half_ca_hankel_clean_endpoint_irreducible_norm_corollary` over the
algebraic closure:

```text
rho=4m-1,       N=16m,       T=4m+1,       m>1,
G(X)=X^N-1=P(X)(X-x_0),
P(X)=(X^N-1)/(X-x_0).                              (CWD1)
```

Choose an affine parameter coordinate `z` in which every supported slope is
finite, and put

```text
H(z)=product_(gamma in Z)(z-gamma).
```

For every supported slope, `Q(gamma;X)` is squarefree of degree `rho` and
divides `G`. Interpolating the exact quotients over the `T` slopes gives
biforms `A,B` such that

```text
Q A+H B=G,                                           (CWD2)
deg_z A<T,                 deg_X A=N-rho=12m+1,
deg_z B<=m-1,              deg_X B<=N.               (CWD3)
```

Combine `(CWD2)` with the proved domain-side complement

```text
Q V+P W=H,
deg_z V<=3m+1,              deg_X V<N-1,
deg_z W<=T,                 deg_X W<=rho-1.           (CWD4)
```

Then there is a biform `K` satisfying the exact two-sided weld

```text
W B-(X-x_0)=Q K,                                     (CWD5)
V B+A=-P K,                                          (CWD6)

deg_z K<=T-1=4m,           deg_X K<=N-1.             (CWD7)
```

Both `B` and `W` are nonzero. Thus, in the function field of the remaining
absolutely irreducible curve, the low-parameter-degree element `B` and the
domain-complement error `W` factor the single linear function:

```text
W B=X-x_0       in Fbar(C).                          (CWD8)
```

## Scope

The weld is a necessary identity, not an exclusion. It replaces the lone
cyclic norm by a two-sided low-degree factorization. Closing the clean branch
still requires showing that this weld is incompatible with the Hankel/apolar
origin, or classifying and deleting its surviving boundary allocation.
