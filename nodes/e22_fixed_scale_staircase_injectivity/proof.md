# proof: e22_fixed_scale_staircase_injectivity

Fix `M`. A locator over distinct field points determines its root set
uniquely. Therefore equality of two fixed-scale staircase locators implies
equality of the underlying root sets.

Let `R` be such a root set. The quotient map `pi_M(x) = x^M` partitions the
domain into fibers of size `M`. A selected quotient fiber is exactly a fiber
contained in `R`.

Because the tail has size `< M`, it cannot contain an entire quotient fiber
that was not selected. Hence the selected-fiber set is recovered from `R` as

```text
H = {z : pi_M^{-1}(z) subset R}.
```

After removing those full fibers, the remaining roots are exactly the tail:

```text
B = R \ union_{z in H} pi_M^{-1}(z).
```

Thus `R` uniquely determines both `H` and `B` at the fixed scale `M`.
Since equality of locators is equality of root sets, two fixed-`M`
staircase parameter sets with the same locator have the same selected fibers
and the same tail. This proves fixed-scale injectivity.
