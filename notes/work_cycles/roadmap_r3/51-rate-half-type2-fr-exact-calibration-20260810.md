# Cycle 51: rate-half type-2 FR exact calibration correction (2026-08-10)

## Finding

A theorem-led audit found that the Round-31 `(FR)` target retained the spend
needed at the old vacuous support size `a=8m-2`. After `(NEWCAP)` moves the
worst case to `a=7m-1`, the outside capacity is `(9m+1)m`, so spend `2m+2`
does not close the printed count.

## Proved correction

At `a=7m-1`, the type-1 cap is two. If every type-2 slope spends at least
`p` roots outside `W`, then

```text
T<=2+floor(((9m+1)m)/p).
```

The exact least closing spend is

```text
p_req=floor(((9m+1)m)/(4m-1))+1.
```

For every `4|m`, this is `9m/4+1`; for a clean locator the corresponding
intersection cap is `7m/4-2`. One less fails the floor inequality, so the
threshold is sharp for this route.

At `m=2^37`, the exact values are

```text
p_req=309237645313,
max clean intersection=240518168574,
old p=274877906946,
old total cap=618475290622,
target=549755813888.
```

Thus the old proposal leaves `68,719,476,734` slopes of room and approaches
a `9/8` residual. The new proved node is
`rate_half_type2_fr_exact_spend_calibration`.

## Consequence

The algebraic frontier is harder by `m/4-1` outside roots per clean slope
than previously recorded. The incidence-only quartic witness still fences
the corrected target, since at `m=64` its maximum intersection `189` also
exceeds the calibrated cap `110`. Its coset-preserving biform lift remains
impossible by cycle 49.

No critical status changes. Future work must target the exact spend or use a
different collective inequality; proving only the old `~2m` statement is not
a route to closure.
