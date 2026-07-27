# Averaged-occupancy clean-anchor first-moment route cut

- **status:** see `dag.json` (single source of truth; DAG status `CONDITIONAL`)
- **closure:** exact arithmetic proved; prize-level route cut conditional on
  `averaged_slope_conversion`

Fix one of the six named high-budget clean predecessor anchors, with agreement
`a`, field order `q`, and `B*=floor(q/2^128)` equal to its named budget. Let
`A` be any family of support sets `S subset D` with `|S|>=a`. For a uniformly
random received pair, let `N(A)` count supports in `A` that align at a unique
finite slope with the nondegeneracy required by `fm1`.

Then

```text
E[N(A)] < B*.
```

Consequently every occupancy payload of `averaged_slope_conversion` satisfies

```text
nu(A) = E[N(A)] - (q/2) C_t(A) <= E[N(A)] < B*,
```

because the fixed-slope second factorial moment `C_t(A)` is nonnegative. No
such family can meet the required strict inequality `nu(A)>B*` at any of the
six named envelopes.

This rules out the present `M` supplier at those envelopes before overlap or
first-match optimization. It is not safety and does not restrict quotient or
direct-value `Q`/`V` payloads. The displayed first-moment inequality remains
proved; the node is conditional because the interpretation as an occupancy
route cut requires `averaged_slope_conversion`, which now depends on the
TARGET `averaged_xr`.
