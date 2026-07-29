# Claim contract

## Object

The 64 degree-one prime ideals above 257 in
`K=Q(zeta_128)=Q[x]/(x^64+1)`.

## Direct claim

Their ideal classes are pairwise distinct.

## Required certificate

The certificate must be unconditional and must include enough exact ideal
relations, class-group relations, or a proof-producing equivalent to replay:

1. the claimed class group and its invariant factors;
2. the class coordinate of one specified prime above 257;
3. the action of `sigma_-1` and `sigma_3` on that coordinate; and
4. all 64 distinct resulting coordinates.

The primary computation and an independently implemented audit must agree.
The audit may instead certify the 64 prime classes directly.

## Nonclaims

- The published slide is evidence, not the required replay.
- A class-number-only calculation is insufficient.
- Nonprincipality of each prime is insufficient: pairwise class separation is
  required.
- GRH-conditional class-group output is insufficient for an unconditional
  prize proof.

## Consumer

`e1_profile018_qzeta128_class_descent_two_ideal_bound`.
