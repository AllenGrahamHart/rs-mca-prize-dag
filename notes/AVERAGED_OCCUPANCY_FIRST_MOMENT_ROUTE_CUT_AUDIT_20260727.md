# Averaged-occupancy first-moment route-cut audit

Date: 2026-07-27.

## Finding

The repository had proved the implication

```text
nu(A)>B*  implies an unsafe M payload,
```

but had not instantiated a post-paid family at the clean envelopes. Screening
the largest possible family resolves the route before overlap analysis. For
supports of size `m=k+r`, FM1 gives an expectation strictly below

```text
U_m=binom(n,m)q^(1-r).
```

The ratio `U_(m+1)/U_m` is below `n/q<1/2`. Thus every family over all witness
sizes at least `a` has expectation below `2U_a`.

## Exact certificates

At RowC, direct integer comparisons leave `40,309,23` bits at rates
`1/4,1/8,1/16`. At prize-max, no large integer is constructed: the standard
bound `binom(n,a)<(3n/a)^a` is certified by exact fifth powers with exponents
`18,23,28`, followed by exact integer exponent comparisons. The smallest
prize exponent slack is `901943131515`.

Since the fixed-slope factorial moment is nonnegative,

```text
nu(A)<=E[N(A)]<B*.
```

No overlap profile or first-match choice can rescue this supplier on a named
envelope.

## Scope

This is a route cut for averaged support-family occupancy. It is not a safety
bound, does not constrain a specially constructed received line, and leaves
direct quotient/value-set suppliers untouched. No Modal computation was used.
