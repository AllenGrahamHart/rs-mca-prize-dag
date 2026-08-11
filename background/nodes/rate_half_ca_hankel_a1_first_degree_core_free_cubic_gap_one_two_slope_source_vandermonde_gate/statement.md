# `A=1` core-free cubic gap-one two-slope source Vandermonde gate

- **status:** PROVED
- **closure:** first-jet pairing expressed on exact error-support differences
- **consumer:** `rate_half_band_crossing_location`

Retain a core-free cubic double-plus-simple `u=1` packet. For each supported
slope `gamma`, let `c_gamma` be its residual rank loss, let

```text
Q_gamma=Q_min,gamma R_gamma,
deg Q_min,gamma=rho-c_gamma,
deg R_gamma=c_gamma,                                (TSV1)
```

and let `S_gamma subset D` be the root set of the squarefree split minimal
locator `Q_min,gamma`. The unique decoding center `f_gamma` has exact error
support

```text
supp(y_gamma-f_gamma)=S_gamma,
|S_gamma|=rho-c_gamma.                              (TSV2)
```

Fix two distinct supported slopes `alpha,beta`. Assume `c_alpha>0` and that
`alpha` is not a zero of the residual factor `E_w` in `(CRF3)`. After a
projective coordinate change making both slopes finite, let `lambda_x` be
the nonzero dual RS multiplier and let `e_beta(x)` be the nonzero error value
on `S_beta`. Then the first-jet pairing at `alpha` has the exact source form

```text
B_alpha(A,B)
 =sum_(x in S_beta\S_alpha) mu_x A(x)B(x),           (TSV3)

mu_x=lambda_x e_beta(x)Q_min,alpha(x)^2/(beta-alpha)
     !=0,                                           (TSV4)

deg A<=c_alpha-1,       deg B<=c_alpha.             (TSV5)
```

Consequently

```text
|S_beta\S_alpha|>=c_alpha.                          (TSV6)
```

If equality holds, then

```text
roots(R_alpha)=S_beta\S_alpha                       (TSV7)
```

as reduced sets; in particular `R_alpha` is squarefree.

For each of the three `w=0` packets these conclusions hold at every
positive-rank-loss slope `alpha` and every other supported `beta`. Applying
the bound in both directions, with the zero-loss cases interpreted
trivially, gives for every pair

```text
|S_alpha union S_beta|>=rho.                         (TSV8)
```

If equality holds in `(TSV8)`, then both set differences attain their lower
bounds; whenever the corresponding rank loss is positive, that difference
is the root set of the corresponding `R_gamma`.

## Scope

The source weights in `(TSV4)` are field-valued and may cancel when the set
difference has more than `c_alpha` points. No positivity, pairwise
disjointness, or packet exclusion is asserted. In the `w=1` packet the
possible `E_1` slope retains the exception from the first-jet theorem.
