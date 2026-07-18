# Replay result

The focused order-eight cutoff-two fixture passes under `ramguard tiny`:

```text
F3_H3_DOUBLE_ACCIDENT_DERIVATIVE_IDEAL_PASS
old_over_joint=390625 joint_bits=506 discriminant_bits=893
discriminant_gcd=old positive_rows=2/8 ideals=42
fixtures=[(17,48,32),(41,2,1),(73,0,0),(89,0,0),
          (97,0,0),(113,0,0),(137,0,0),(193,0,0)] dag=4/4
```

Each fixture tuple is `(p,X_2,Y_2)`. The joint exceptional integer is a
strict divisor of the old integer, with quotient `390625=5^8`. Its official
split-prime divisors among the fixtures are exactly `17` and `41`, exactly the
rows with positive `Y_2`.

The independent valuation audit also passes:

```text
AUDIT_F3_H3_DOUBLE_ACCIDENT_DERIVATIVE_IDEAL_PASS
local_valuation_checks=4160 residual_checks=29 dag=4/4
```

The fixture checks the generalized mechanism at cutoff two; the written proof
establishes the cutoff-eighteen theorem. The global quotient-discriminant gcd
is exactly the old integer in this fixture, so it misses the strict `5^8`
reduction captured by the target-local joint ideals.
