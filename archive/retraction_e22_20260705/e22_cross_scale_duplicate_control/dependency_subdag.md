# dependency sub-DAG: e22_cross_scale_duplicate_control

Edges are directed from dependency to consumer.

```text
e22_fixed_scale_staircase_injectivity [PROVED]
    -> e22_cross_scale_rootset_recovery [PROVED]
    -> e22_cross_scale_support_canonical_form [PROVED]
    -> e22_cross_scale_equivalence_specification
    -> e22_cross_scale_duplicate_control

e22_cross_scale_pricing_multiplicity
    -> e22_cross_scale_equivalence_specification
    -> e22_cross_scale_duplicate_control
```

## Status

- `e22_cross_scale_rootset_recovery`: PROVED. Equal locators have equal root
  sets, and fixed-scale recovery recovers each scale's tail and selected
  fibers.
- `e22_cross_scale_support_canonical_form`: PROVED. Equal supports have one
  canonical set of admissible scales, tails, and full fibers.
- `e22_cross_scale_equivalence_specification`: CONDITIONAL. This now assembles
  canonical support-scale recovery with pricing multiplicity.
- `e22_cross_scale_pricing_multiplicity`: TARGET. This is the remaining exact
  cross-scale pricing-column compatibility problem.
- `e22_cross_scale_duplicate_control`: CONDITIONAL.
