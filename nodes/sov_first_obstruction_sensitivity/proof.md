# proof: sov_first_obstruction_sensitivity

The forced root `S` is computed from the coefficients of the monic
degree-`2h` locator `L` in degrees

```text
2h-1, 2h-2, ..., h.
```

This is the triangular recursion proved in
`sov_forced_root_recursion_algebra`. The coefficient of `X^{h-1}` in `L` is
not used anywhere in that recursion. Therefore changing only `[X^{h-1}]L`
leaves the forced root `S` unchanged.

The first obstruction is

```text
O_{h-1} = [X^{h-1}](S^2 - L).
```

If `[X^{h-1}]L` is changed by `delta` and `S` is unchanged, then
`[X^{h-1}]S^2` is unchanged and

```text
O_{h-1} -> O_{h-1} - delta.
```

In particular, a unit bump changes `O_{h-1}` by `-1`. This proves that the
first obstruction is exactly sensitive to the coefficient direction isolated
by the SOV value-set scan.
