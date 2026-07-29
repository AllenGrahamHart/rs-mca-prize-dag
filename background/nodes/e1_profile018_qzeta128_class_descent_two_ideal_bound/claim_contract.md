# Claim contract

## Hypothesis

`e1_qzeta128_p257_class_orbit_certificate` is `PROVED` at its printed scope.

## Input

A fixed degree-one row prime `P_r` in `Q(zeta_256)` and any set of
degree-one primes `Q_s` above 257 satisfying

```text
(alpha_s)=P_r(1-zeta_256)Q_s.
```

## Output

At most two distinct `Q_s` occur.

## Quantifier

Uniform in the row prime, row root, collision coefficients, energy, and
profile.

## Normalization

`Q_s=(257,zeta_256-s)` and its prime below in `Q(zeta_128)` is indexed by
`s^2`. Replacing all signs in the prime convention does not change the
two-to-one descent.

## Nonclaims

- This node does not prove the class-orbit certificate.
- The published S-unit slide is evidence for the hypothesis, not its replay.
- The theorem bounds occupied ideals, not raw roots of an autocorrelation
  polynomial.

## Consumer

`e1_profile018_m514_five_ideal_occupancy`.
