# ATTACK - e22_staircase_arithmetic_pricing

Status: conditional assembly.

The local leaf is no longer a primary blocker. It is wired to:

- `e22_staircase_parametrization`;
- `e22_staircase_injectivity`;
- `dyadic_profile_evaluation`.

If the formula or injectivity predicates change, re-run the exact integer
checker analogous to the arithmetic side of `list_planted_arithmetic`:
planted count plus staircase count, compared against the row threshold with no
floating point decisions.
