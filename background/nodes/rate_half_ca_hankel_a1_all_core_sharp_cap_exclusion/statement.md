# `A=1` all-core sharp-cap exclusion

- **status:** PROVED
- **closure:** contact-exclusion corollary across all core sizes
- **consumer:** `rate_half_band_crossing_location`

On the official half-distance `A=1` row, no failing profile can attain its
Euclidean slope cap:

```text
ell=T_max-T=0                                         (A1C1)
```

is impossible for every `s in {0,1,2}` and every degree in the live ranges.

More precisely:

- `s=2` is already empty;
- every `s=1` survivor satisfies

```text
ell>=e-2-floor(Delta/3)>=1;                           (A1C2)
```

- every `s=0` survivor has positive slope slack; the two degrees `m+1,m+2`
  are covered by four-contact vanishing and every `e>=m+3` by the adaptive
  three-contact theorem.

Thus the historical core-one maximal-degree sharp-cap corrected-square route
is no longer a live frontier.

## Scope

Positive-slack core-free and core-one profiles remain open.
