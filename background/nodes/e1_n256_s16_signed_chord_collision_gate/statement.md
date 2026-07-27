# E1 N=256 square-mass-16 signed-chord gate

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `F=sum_i c_i X^i` have folded profile `(3,4,0)` in the
`N=256,s=5` band, and suppose it survives the sparse-L1 variance
exclusion, so

```text
0<V<=76.
```

For an unordered support pair `e={i,j}`, let `d(e)` be its circular
distance in `Z/128Z`. If `d(e)<64`, orient it into the positive
half-circle and let `w_e` be the resulting signed coefficient product.
Put

```text
D_64 = sum_(d(e)=64) (c_i c_j)^2,
C = sum_(d=1)^63 sum_(e<f, d(e)=d(f)=d) w_e w_f.
```

Then the exact negacyclic autocorrelation identity is

```text
V/2 = 102-D_64+2C.                                    (1)
```

Diameter chords form a matching on the seven support points, and the profile
weights give `D_64<=21`. Consequently every surviving vector satisfies

```text
C<=-22.                                               (2)
```

In particular, some non-diameter circular distance is realized by two
distinct support chords with opposite signed products. The support is not a
circular Sidon set: it contains a signed three-term progression if the chords
share a vertex, or a signed four-point parallelogram if they are disjoint.

This is a structural gate, not a collision close. It reduces the
full-conductor low-variance residual to additive-relation templates.
