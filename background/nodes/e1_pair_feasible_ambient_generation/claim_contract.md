# Claim contract

## Inputs

- the strict official cap `q<2^256`;
- the exact six `b_pair_min` values from
  `e1_clean_anchor_exact_collision_allowance`;
- the finite-field inclusion `F_p(Q) subset F_q`.

## Output

- ambient generation `F_p(Q)=F_q` throughout the pair-feasible E1 class at
  the six named clean anchors.

## Nonclaims

- No collision-pair upper bound is proved.
- Proper generated-subfield rows are not proved safe.
- The intermediate direct-image branch is not paid.
- No statement is made for another anchor whose pair threshold is at most
  `2^128`.

## Falsifier

A proper subfield of an official field with size at least one of the printed
pair thresholds, or an incorrect threshold in the source table, falsifies the
node.
