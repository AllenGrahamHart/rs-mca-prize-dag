# Claim contract

## Proved

- Every used heavy-plane factor datum has a unique minimal field over `B`.
- The only relative degrees on the official sextic row are `1,2,3,6`.
- One degree stratum has mass at least `2491351997` and uses at least 11
  projective factors.
- Field-internal Segre form, base-freeness, rank four, the 41-factor floor,
  and the fixed-factor cap do not alone imply base-field descent.

## Required semantics

- The input mass and fixed-factor cap are inherited without re-owning from
  the proved heavy Segre bucket.
- The minimal field is attached to the combined projective datum
  `(P,Q,[g])`, not to an arbitrary basis or one coefficient.
- Entropy or census costs are charged only over the resulting minimal field,
  in accordance with the base-field normalization guard.

## Not claimed

- That an actual MCA record realizes the symbolic countermodel.
- That the heaviest stratum has degree one.
- That a degree-one record already satisfies upstream's fixed rank-nine cell
  or aggregate selected-support owner.
- Payment of any extension stratum, the heavy bucket, or MCA.
