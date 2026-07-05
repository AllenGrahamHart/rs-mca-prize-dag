# conditional: e22_cofactor_divisor_quotient_gluing

## Predicate nodes

- `e22_fixed_tail_local_saturation`
- `e22_dyadic_local_to_common_saturation`

## Claim

Conditional on fixed-tail local saturation, the E22 petal divisor constraints
force non-tail roots to be saturated on full fibers of one quotient map
`x -> x^M` with `M>t`.

## Proof

The predicate `e22_fixed_tail_local_saturation` supplies a single exceptional
tail `B`, local dyadic quotient moduli `M_i>t`, and local non-tail blocks
which are unions of full fibers of the corresponding maps `x -> x^{M_i}`.
It also supplies the tail bound

```text
|B| < min_i M_i.
```

The proved predicate `e22_dyadic_local_to_common_saturation` applies to this
fixed-tail situation. Since the quotient moduli are dyadic, the minimum local
modulus

```text
M_* = min_i M_i
```

divides every `M_i`. Therefore every local full `M_i`-fiber block is a union
of full `M_*`-fibers, and the union of all non-tail blocks is saturated on
full fibers of `x -> x^{M_*}`. Because each `M_i>t`, also `M_*>t`.

Thus the complete non-tail support is a union of full quotient fibers for one
modulus `M_*>t`, with the same bounded tail `B`. This is exactly the
divisor-to-quotient gluing conclusion.
