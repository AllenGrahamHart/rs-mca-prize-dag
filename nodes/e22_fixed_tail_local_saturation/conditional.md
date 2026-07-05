# conditional: e22_fixed_tail_local_saturation

## Predicate nodes

- `e22_local_quotient_factor_extraction`
- `e22_fiber_locator_saturation`

## Claim

Conditional on local quotient-factor extraction, the E22 cofactor divisors
isolate one bounded tail and local dyadic quotient-fiber saturated blocks.

## Proof

The predicate `e22_local_quotient_factor_extraction` supplies a common tail
`B`, the bound

```text
|B| < min_i M_i,
```

dyadic local moduli `M_i>t`, and quotient factors

```text
X^{M_i}-z
```

for every non-tail block forced by the touched-petal cofactors.

The proved predicate `e22_fiber_locator_saturation` says that divisibility by
`X^{M_i}-z` is equivalent to containing the whole fiber

```text
{x : x^{M_i}=z}.
```

Therefore every non-tail contribution supplied by the local quotient factors
is a union of full fibers of the appropriate map `x -> x^{M_i}`. Together
with the supplied common tail and tail bound, this proves fixed-tail local
quotient saturation.
