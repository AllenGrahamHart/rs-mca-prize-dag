# frontier: e22_staircase_arithmetic_pricing

Conditional assembly.

The row arithmetic is not the active obstacle. The open predicates are the
formula and multiplicity inputs:

- `e22_staircase_parametrization`;
- `e22_staircase_injectivity`.

Once those are proved, the exact dyadic profile evaluator supplies the
staircase column and this node can flip with no additional search.
The current n=16 exact profile extractor is a calibration target for the
formula, not the official row arithmetic.
