# `A=1` quadratic paired zero-excess padded-fiber factorization

- **status:** PROVED
- **closure:** every zero-excess parameter fiber splits, including padding
- **consumer:** `rate_half_band_crossing_location`

Retain either of the two proved quadratic `u=4` pair-boundary biforms. For
a zero-excess off-line slope `delta`, put

```text
I_delta=S_delta intersect U_0,
A_delta(X)=product_(x in I_delta)(X-x),
Q_delta=q_delta R_delta,                            (PZF1)
```

where `q_delta` is the actual residual-support locator after deleting the
fixed core and `R_delta` is the monic padded-heavy factor of degree
`r_delta`. Then the specialized biform has the exact factorization

```text
G(delta,X)=zeta_delta A_delta(X)R_delta(X),
zeta_delta!=0.                                      (PZF2)
```

The roots of `A_delta` and `R_delta` are disjoint. Thus `(PZF2)` is a
base-field split polynomial of the full `X`-degree of `G`, even when
`r_delta>0`.

## Extremal boundary

For the biform of bidegree `(e-2,p-3)`, at least `2e` slopes satisfy
`(PZF2)`, with

```text
deg A_delta=p-3-r_delta,
deg R_delta=r_delta,
deg_X G(delta,X)=p-3.                               (PZF3)
```

## First strict boundary

For the biform of bidegree `(e-1,p-2)`, at least `p+2` slopes satisfy
`(PZF2)`, with

```text
deg A_delta=p-2-r_delta,
deg R_delta=r_delta,
deg_X G(delta,X)=p-2.                               (PZF4)
```

For the official row, the guaranteed full-degree split-fiber counts are

```text
extremal:  2e  =366503875926,
strict:    p+2 =274877906946.                       (PZF5)
```

## Scope

This is a necessary factorization theorem, not an exclusion. It does not
assert that different slopes have different root sets or that the resulting
coefficient systems have full rank.
