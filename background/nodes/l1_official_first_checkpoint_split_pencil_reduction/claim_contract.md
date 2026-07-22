# Claim contract - L1 official first-checkpoint split-pencil reduction

## Inputs

- an official multiplicative-coset evaluation domain;
- `p>=3583` and `n<24p`;
- one coarse collision with `p<=d<=2p-2` and tail width `t=p`;
- the Wronskian upper degree and tame-tail endpoint suppliers.

## Output

The two tails are distinct split fibers of `Z^p+Q` with
`deg Q<=2p-d-1`. At terminal depth `d=2p-2`, no such tails exist and every
collision has width at least `p+1`.

## Falsifier

A minimum-width collision not admitting `(FSP3)`, an affine `F_p`-line
inside an official smooth coset, or a terminal collision with `t=p`.

## Nonclaims

No bound for the surviving higher-degree split-pencil census, no control of
`t>p`, and no L1 status change.
