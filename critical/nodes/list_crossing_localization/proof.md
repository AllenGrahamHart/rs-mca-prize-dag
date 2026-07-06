# list_crossing_localization proof

This proof uses the agreement-index convention of `list_adjacency_closing`:
larger `delta` means a stronger agreement requirement and hence a smaller
list.

For a received word `U`, the sets `Lambda(U, delta)` are nested:

```text
Lambda(U, delta + 1) subset Lambda(U, delta).
```

Taking cardinalities and then the supremum over `U` preserves this
monotonicity, so

```text
L(delta) := sup_U |Lambda(U, delta)|
```

is nonincreasing and integer-valued.

If the list-window arithmetic supplies a bracket with

```text
L(delta_lo) > eps |F|
L(delta_hi) <= eps |F|,
```

then the first integer `delta*` in the bracket satisfying
`L(delta*) <= eps |F|` is well-defined and unique as a first crossing. It
satisfies

```text
L(delta* - 1) > eps |F| >= L(delta*).
```

Thus the list-side adjacency problem is reduced, exactly as on the MCA side,
to the finite set of grid candidates printed by the list-window arithmetic.
