# Proof

## Exact row replay

The compact source snapshot records the four active rows from the upstream
completion compiler and the attack values from Paving v9.2 / Paper D v13.2.
For every row, exact integer comparison gives

```text
attack(a0)>B*,       attack(a0+1)<=B*.              (IP1)
```

The candidate-row value also reproduces the compiler's full-budget Q
multiplier by integer division. This checks row, object, endpoint, field, and
budget alignment without interpreting a lower value as an upper bound.

## List owner

At the boundary depth, an identity-prefix locator `L_M` and witness word `U`
give the codeword `U-L_M` with complete agreement exactly `M`. This is the
boundary prefix/Q owner.

For an interior support profile, put `m'=K-1+d1>m`. The proved
`l1_interior_bc_floor_higher_shell_q_routing` theorem shows that every one of
the `binom(m',m)` apparent level-`m` support witnesses has a positive
agreement cofactor dividing the complement locator. It fails the exact-shell
guard and cancels under binomial inversion. The codeword is retained once at
complete agreement `m'`, where the same profile is boundary Q. Thus the
discrete support spray is not an aperiodic exact-shell population.

## MCA owner

Paving's identity-prefix MCA corollary first constructs the dimension-`k+1`
identity-prefix list and then applies the collision-aware simple-pole
conversion. On the official KoalaBear extension row, the local F1
classification assigns this to the pole/list branch; the same-rate router
preserves the row parameters through field descent. The aperiodic residual is
defined only after this named pole/prefix owner has been stripped.

The Mersenne rows use circle domains and target `2^-100`, so they do not test
the official smooth-domain assertion. Their arithmetic still supplies an
independent endpoint regression.

Hence no deployed identity-prefix witness enters the local post-strip
aperiodic column. This proves the claimed `NO ISSUE` verdict. QED.
