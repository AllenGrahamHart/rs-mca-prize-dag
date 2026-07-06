# dependency sub-DAG: worst_word_challenger_pricing

Edges are directed from dependency to consumer.

```text
e22_two_class_exhaustion
    -> worst_word_challenger_pricing
    -> worst_word_planted
    -> list_planted_arithmetic

e22_staircase_parametrization
    -> e22_challenger_staircase_pricing
    -> worst_word_challenger_pricing

e22_staircase_injectivity
    -> e22_challenger_staircase_pricing
    -> worst_word_challenger_pricing

e22_staircase_arithmetic_pricing
    -> e22_challenger_staircase_pricing
    -> worst_word_challenger_pricing

e22_challenger_staircase_pricing
    -> worst_word_challenger_pricing
    -> worst_word_planted
    -> list_planted_arithmetic
```

## Node statuses

- `worst_word_challenger_pricing`: CONDITIONAL. The assembly implication is
  now explicit and has no hidden predicate.
- `e22_two_class_exhaustion`: PROVED by the root-count plus ratio-flat
  exclusion in `nodes/e22_two_class_exhaustion/proof.md`.
- `e22_challenger_staircase_pricing`: CONDITIONAL. Its three open predicates
  are exact parametrization, injectivity/no-overlap, and arithmetic pricing.
- `e22_staircase_parametrization`: TARGET.
- `e22_staircase_injectivity`: TARGET.
- `e22_staircase_arithmetic_pricing`: TARGET.

## Light-compute boundary

Only small local checks have been run in this working copy: the E15 gate, the
ratio-flat sanity check, and the n=16 profile extractor. Larger E22
exhaustive/structured sweeps should run remotely or on a machine scheduled for
that memory/runtime profile.
