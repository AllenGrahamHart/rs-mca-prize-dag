# Claim contract

## Claim

The E1 class difference is controlled by the signed singleton-vector
difference. Its square mass is `S=4a+b`, while raw-representative padding is
invisible to the class value. At fixed `N,ell`, `S<=4min(ell,2h-ell)`.
The three additional `N=256,S=16` splits outside `(3,4)` are feasible class
pairs at both official values of `ell` and survive the available norm bound.

## Dependencies

- `acl_count` supplies the exact signed-singleton description of an
  antipodal-rearrangement class and `t+2u=ell`.
- `e1_prime_field_l2_norm_collision_radius` supplies folding, the norm bound,
  the all-even division-by-two branch, and the row-prime floor.

## Guards

1. "Norm-unresolved" means only that the printed norm inequality does not
   exclude the profile. It does not mean that a finite-field collision exists.
2. The extra `S=16` witnesses are class-pair feasibility witnesses, not row
   counterexamples.
3. The `(3,4)` variance results remain valid in their stated profile scope.
4. This node is evidence-only into both open E1 consumers.

## Falsifier

A violation of the class feasibility equations, a class pair with
`S!=4a+b`, an official parameter with `S>4T`, failure of one of the explicit
`S=16` constructions, or a cited theorem that excludes one of the three
additional splits under the official row hypotheses.
