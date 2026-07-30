# KoalaBear m2 r4 coordinate-transpose transport

- **status:** PROVED
- **scope:** every actual order-two component with stabilizer
  `S=<1 x tau>` in the residual `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_q6_u2_primitive_subdegree4_route_cut` and
  `rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler`
- **consumer:** `rate_half_band_closure`

Let `theta(T,W)=(W,T)`. The endpoint self-correspondence is

```text
f(T)=f(W),
```

so it is preserved by `theta`. If `Gamma` is an actual irreducible
bidegree-`(4,4)` component, put `Gamma^tr=theta(Gamma)`. Then

```text
Stab_V4(Gamma^tr)=theta Stab_V4(Gamma) theta^(-1). (KBTT-1)
```

In particular,

```text
Stab(Gamma)=<1 x tau>
if and only if
Stab(Gamma^tr)=<tau x 1>.                         (KBTT-2)
```

The source record on `Gamma^tr` must be rebuilt after exchanging endpoint
roles. Set `T'=W`, `W'=T`, run the degree-two source reduction on the
second coordinate `W'=psi'(X')`, and denote its data by

```text
H'(T',X'), b', I', J', L', K'.                    (KBTT-3)
```

This fresh record is an actual coordinate-order-two packet and therefore
satisfies the complete proved coordinate chain: the exact source-facet
census and two paired profiles, the universal `45 x 12` source-row gate,
the 8/7-dimensional parity forms, the colored quotient-resultant system,
and the `10 x 8` or `10 x 7` common-`K'` Vieta-rank gate.

Consequently the two coordinate subgroups are one existence/deletion
route. A universal exclusion of all coordinate packets excludes both
`<tau x 1>` and `<1 x tau>`. The original and primed source forms are not
identified, and packet-specific equations must be evaluated on the primed
record. The diagonal subgroup remains a separate route. No orientation is
yet deleted, and no type, owner, payment, row, or Prize result is proved.

## Falsifier

An actual `<1 x tau>` component whose transpose is not an actual
`<tau x 1>` component of the same endpoint self-correspondence, or whose
fresh transposed source record falls outside any theorem in the proved
coordinate chain.
