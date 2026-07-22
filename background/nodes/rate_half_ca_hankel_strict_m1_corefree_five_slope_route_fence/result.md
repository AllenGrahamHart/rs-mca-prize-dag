# Exact result

```text
RATE_HALF_STRICT_M1_LOCATOR_LINES_PASS
points=560
core_free_max=5
core_free_five_lines=16
hankel_nullity_histogram={1:16}
compatible_lines=16
```

One normalized witness is

```text
Q(z;X)=X^3+(9+4z)X^2+12zX+7,
y_0=(1,10,16,2,14,0,3,11),
y_1=(0,14,9,7,13,12,15,0),
supported slopes=(0,1,2,4,15).
```

The source is
`experiments/prize_resolution/rate_half_strict_m1_locator_lines.py`, SHA-256
`b0f03a9b167857810aaab64cbfccec052dafa8b51ae0e34d117e247793faec02`.
The run is local, exact, deterministic, takes under two seconds, and uses no
Modal resource.
