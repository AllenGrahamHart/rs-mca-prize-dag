# `A=1` core-free residual-degree-two packet exclusion

- **status:** PROVED
- **closure:** full-omission overlap and local cube congruence
- **consumer:** `rate_half_band_crossing_location`

Neither core-free residual-degree-two packet in `(CTP4)` exists. Hence the
parameter-constant core-free first-degree range sharpens from

```text
a in {2,3,4,5}
```

to

```text
a in {3,4,5}.                                         (CFE1)
```

The exclusion uses no field enumeration. In both packets `O=Delta`, so
every degree of every specialized excess factor is omission-producing: no
simple new domain root can occur outside `Q_min`. Each packet has a
distinguished row of deficit one. The local cube identity then makes every
vertical multiplicity on that row congruent to one modulo three, except
that spending the sole possible extra determinant order raises one minimum
from one to three. The first alternative leaves total vertical degree
`e-1 mod 3`; the second already exceeds `e`. Both contradict the degree-`e`
row form.
