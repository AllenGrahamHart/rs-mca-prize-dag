# F3 h=3 rich-curve exact reduced-condition profile

Status: PROVED ARITHMETIC SHARPENING OF `RC-RED`, NOT `RC-NV`.

The log-jet reduction proves more than the legacy scalar statement
`RC-RED(13)`.  For derivative order `j`, the reduced numerator has degree at
most

```text
(A-1) + 12j.
```

Therefore the `j`-th derivative condition is over-imposed by at most

```text
A + 12j
```

linear coefficient conditions per repaired curve.  Summing over
`0 <= j < D` gives the exact profile

```text
DA + 6D(D-1)
```

conditions per curve.

The previous downstream compiler used the coarser uniform bound

```text
13D(A+D).
```

This remains valid and is kept for legacy budget tables, but the exact profile
is strictly sharper on the sample boxes used by the reduced-condition compiler.

## Sample Rows

```text
    A     D    |Z|      exact_total      legacy_total       saved
   512    16      1             9632            109824       100192
   512    16      8            77056            878592       801536
  2048    32     16          1143808          13844480     12700672
  8192    64     32         17551360         219807744    202256384
 32768   128     64        274677760        3503292416   3228614656
```

## Role

This strengthens the arithmetic side of the h=3 rich-curve Stepanov route.  It
does not prove the nonvanishing/rank gate.  The sufficient rank form may now be
stated with either:

```text
rank(S_Z) > 13D(A+D)|Z|                 legacy sufficient form,
```

or the sharper profile

```text
rank(S_Z) > (DA + 6D(D-1))|Z|.          exact profile form.
```

Future bridge-budget optimizers should use the exact profile.  Existing legacy
tables are still valid because the old condition count is larger.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_condition_profile.py
```

Expected digest:

```text
H3_RICH_CURVE_CONDITION_PROFILE_PASS
```
