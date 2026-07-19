# Canonical high-core component-union atlas

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`

Fix one generic post-strip received pair and write

```text
R=n-k,       h=A-k,       r=n-A=R-h.
```

A live ray at slope `gamma` has an error set `E subset D` with `|E|<=r`.
Join two distinct slopes when they admit live rays with error sets `E,E'`
satisfying `|E union E'|=R`. Let `Z_high` be the nonisolated slope set.

After fixing total orders on slopes and live rays, there is a canonical atlas
indexed by the connected components `C` of this slope graph. It assigns

```text
Z_C = the slopes in C,
U_C = the union of one selected live-ray error set at each slope in C,
|U_C| = R+d_C.
```

The component slope sets partition `Z_high`, every selected ray is supported
inside `U_C`, and `d_C>=0`. Consequently

```text
|Z_high| = sum_C |Z_C|,

|Z_C| C(d_C+h,d_C) <= C(R+d_C,d_C) R,

|Z_high| <= sum_C floor(C(R+d_C,d_C) R / C(d_C+h,d_C)).       (CA-GRK)
```

For the XR high-core stratum, the proved strip rungs make every cross-slope
core at most `k`; hence a shared `k`-core is exact and its two error sets have
union size `R`. Thus `Z_high` is exactly the distinct high-core slope set in
the target.

This theorem resolves slope/core/chart deduplication. It does not prove that
the final sum in `(CA-GRK)` is at most `8n^3`; controlling the number and
union excesses `d_C` of the canonical components is the remaining claim.
