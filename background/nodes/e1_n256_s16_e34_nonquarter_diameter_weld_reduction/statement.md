# E1 N=256 E=34 nonquarter-diameter weld reduction

- **status:** PROVED
- **closure:** proof

Every residual nonquarter-diameter template can be normalized by translation,
reflection, and exchange of the antipodal heavy positions to

```text
H={0,64,t},                 1 <= t <= 31.
```

Define

```text
C_t={64-t,64+t,128-t},      U_t={2t,64+2t}.
```

The five displayed positions are distinct and disjoint from `H`. The two
singleton heavy-heavy distance classes are welded to heavy-light chords if
and only if the four-position light support satisfies

```text
L intersect C_t is nonempty     or     U_t is a subset of L.       (W_t)
```

Moreover, `D_64=20` exactly when `64+t` is light; otherwise `D_64=16`.
For each `t`, exactly

```text
binom(125,4)-binom(122,4)+binom(120,2)=915,125
```

four-position light supports satisfy `(W_t)`. After global sign
normalization, the complete necessary-condition chamber therefore contains

```text
31 * 915,125 * 4 * 16 = 1,815,608,000
```

signed vectors.

This is an exact reduction, not an exclusion: `(W_t)` is necessary for a
residual collision, but vectors counted by it need not have `E=34`, profile
`(6,7)`, full conductor, or pair-feasible norm.
