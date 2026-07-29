# Claim contract

## Imported facts

- Pair-feasible prize E1 rows are prime-field rows with `p=1 mod 256`.
- The profile-`(3,6,S=18)` cofactor list is exact.
- Eight complete cofactor exclusions leave `{2,4,8,16}`.
- The once- and twice-divided `m=16` support branches are empty.

## New theorem

At one fixed reduction root, every collision with absolute norm `2^mu p`
has principal ideal `P_r(pi)^mu`.  Dividing by `pi^mu` gives a generator of
`P_r`, and two such generators differ by a unit. In a fixed-cofactor branch,
Cramer and Hadamard bound every power-basis coefficient of that unit and its
inverse by `floor(18^64/(2^mu p))`.
The conjugate-square AM-GM deficit is exact, and same-cofactor shift/sign
orbits inject into the full rank-63 unit log lattice inside `(PCR5)`.
The exact weighted dictionary charges `128M_33(3,6)` edges per log point and
makes 367 the necessary aggregate orbit cap for this profile.

## Guards

1. The two collision values use the same row prime and the same quotient
   root.  A Galois-conjugate root generally defines a different prime ideal.
2. The cofactor must be a pure power of two.  An odd cofactor contributes
   additional prime ideals and invalidates `(PCR1)`.
3. Association is by an arbitrary algebraic unit of `R`, not only a root of
   unity. Membership in the cyclotomic-unit subgroup is not proved.
4. The theorem supplies coupling but no cardinality, edge, or image bound.
5. The profile corollary consumes the listed exclusions; it is not a claim
   that all lower-weight E1 profiles have pure cofactors.
6. The coefficient box uses equal cofactors. For `mu!=nu`, multiplication by
   different powers of `pi` must be retained and `(PCR3)` is not asserted.
7. The box is a finite interface, not a feasible exhaustive enumeration or
   a bound on the number of units inside it.
8. The logarithmic body uses natural logarithms and the full algebraic-unit
   lattice. No regulator, minimum vector, cyclotomic-unit index, or lattice
   point count is imported.
9. The 256-to-one statement is only modulo multiplication by roots of unity;
   different log-lattice points may still fail the sparse profile constraints.
10. The 367 cap is necessary for the complete edge budget, not sufficient:
    lower-weight profiles retain positive weights.
