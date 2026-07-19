# Arbitrary-arity list closure from the base crossing

- **status:** CONDITIONAL
- **consumer:** `list_grand`
- **predicate:** the `m=1` instance of `list_adjacency_closing`
- **proved bridge:** `list_subsqrt_interleaving_collapse`

## Statement

For every admissible row, assume the base code has adjacent agreements
`a0,a0+1` satisfying

```text
L_1(a0) > B* >= L_1(a0+1),
B* = floor(|F|/2^128).
```

Then for every fixed interleaving arity `m>=1`, the same adjacent agreements
satisfy

```text
L_m(a0) > B* >= L_m(a0+1).
```

Thus arbitrary constant arity introduces no additional prize threshold. This
node consumes only the base (`m=1`) instance of the stronger statement carried
by `list_adjacency_closing`.

## Scope pins

- `L_m(a)` is the worst received-word common-support list at agreement `a`.
- The denominator remains the base field size `|F|`.
- The official field cap `|F|<2^256` is load-bearing.
- The conclusion is uniform in `m`; no bounded-arity sweep is used.
