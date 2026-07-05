# ATTACK - e22_fixed_tail_local_saturation

This node is now an assembly point.

Start from the proved divisor translation:

```text
L_{T_i} | H_i,
H_i = U L_{Z\C} - a_i L_{C\Z}.
```

The remaining E22-specific task is now isolated as
`e22_local_quotient_factor_extraction`: extract local quotient factors from
these polynomial divisibilities:

- identify the exceptional roots that must stay in a single tail `B`;
- prove `|B| < min_i M_i`;
- identify the local dyadic moduli `M_i > t` produced by the degree/scalar
  equations;
- prove that all non-tail forced roots occur through factors `X^{M_i}-z`.

Once this is proved, `e22_fiber_locator_saturation` turns the factors into
local full-fiber blocks, and `e22_dyadic_local_to_common_saturation` glues the
local blocks to the minimum modulus automatically.
