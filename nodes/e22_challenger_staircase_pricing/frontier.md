# frontier: e22_challenger_staircase_pricing

The structural identification is recorded in the `worst_word_planted` ledger:
the E15 mixed-petal challenger family is a quotient-coset staircase rather
than a new unstructured mechanism.

Decomposed blockers:

- `e22_staircase_parametrization`: write the exact staircase parametrization
  in the current notation;
- `e22_staircase_injectivity`: prove injectivity and no overlap with planted
  words except declared degeneracies;
- `e22_staircase_arithmetic_pricing`: run the exact count through the
  list-side threshold arithmetic.

`verify_profiles.py` extracts the small n=16 exact profiles that any formula
must reproduce. It is calibration evidence, not a closure certificate.
