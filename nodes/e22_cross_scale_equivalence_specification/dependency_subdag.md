# dependency sub-DAG: e22_cross_scale_equivalence_specification

Edges are directed from dependency to consumer.

```text
e22_cross_scale_rootset_recovery [PROVED]
    -> e22_cross_scale_support_canonical_form [PROVED]
    -> e22_cross_scale_equivalence_specification

e22_minimal_scale_pricing_compatibility
    -> e22_cross_scale_pricing_multiplicity
    -> e22_cross_scale_equivalence_specification

e22_dyadic_minimal_scale_selector [PROVED]
    -> e22_cross_scale_pricing_multiplicity
```

## Status

- `e22_cross_scale_support_canonical_form`: PROVED. Equal supports have one
  canonical set of admissible scales, tails, and full fibers.
- `e22_cross_scale_pricing_multiplicity`: CONDITIONAL. The dyadic
  minimal-scale selector is proved.
- `e22_minimal_scale_pricing_compatibility`: TARGET. This is the remaining
  pricing-column compatibility theorem.
- `e22_cross_scale_equivalence_specification`: CONDITIONAL.
