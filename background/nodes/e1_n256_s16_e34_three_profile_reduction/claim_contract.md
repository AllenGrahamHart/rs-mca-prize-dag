# Claim contract

## Claim

At `N=256,s=5`, folded profile `(3,4,0)`, and variance `V=68`, every
pair-feasible collision has autocorrelation magnitude profile

```text
(6,7),       (9,4,1),       or       (12,1,2).
```

All three residual profiles have `L=20`.

## Dependencies

- the exact sparse-L1 slack recurrence;
- the proved variance-70 endpoint closure;
- the exact `R(B,B,B)<=174` theorem inherited through the variance-72 packet;
- the collision-norm criterion;
- complete nested quotient and exact inner-`4Z` support certificates.

## Nonclaims

- no exclusion of the three displayed profiles;
- no exclusion of `V<=66`;
- no claim for folded profile `(4,2,0)`;
- no direct unsafe-crossing payload or distinct-value lower bound.

## Falsifier

A pair-feasible `V=68` collision in any other magnitude profile, an exact
quotient allocation exceeding the printed maxima in a closed chamber, an
inner-`4Z` weighted support exceeding 1536, or a failure of the rational
cubic sign check refutes the claim.
