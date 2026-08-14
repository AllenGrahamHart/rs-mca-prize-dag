# `A=1` shape-A locator-interpolation syzygy rank amplification

- **status:** PROVED
- **closure:** every Shape-A split biform has separation rank at least
  `(e+1)/2`
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and write

```text
m=e-2,       n=(3e-7)/2,       d=3e-2,
R=(9e-7)/2,  r=sr(G).                              (ISR1)
```

The `X`-interpolation parity checks for the primitive locator `Qbar` produce
a linear map

```text
T:S_n -> ker(Phi:V^3 -> S_e),                      (ISR2)
```

where `V` is the parameter coefficient space of `G` and `Phi` is the
three-class restricted Koszul map. Its projection to either of the two
source classes of size `n+2` has rank at least `r-1`. Consequently

```text
3r-(e+1)=dim ker Phi>=rank T>=r-1,                 (ISR3)
r>=ceil(e/2)=(e+1)/2.                              (ISR4)
```

On the official row,

```text
r>=91625968982.                                    (ISR5)
```

At the new boundary `r_1=(e+1)/2`, the quadratic Koszul kernel has exact
dimension

```text
dim ker Phi=r_1.                                   (ISR6)
```

Thus every tensor rank below `91625968982` is excluded, and the earlier
one-third rank boundary and its two syzygy profiles cannot occur.

## Scope

The theorem does not prove that `T` is injective or exclude ranks from
`(e+1)/2` through `e-1`. Improving the projection estimate or controlling
the common kernel of the three class maps is the next rank route.
