# Claim contract - L1 official first-checkpoint split-pencil reduction

## Inputs

- an official multiplicative-coset evaluation domain;
- `p>=3583` and `11n<=256p`;
- one coarse collision with `p<=d<=2p-2` and tail width `t=p`;
- the Wronskian upper degree and tame-tail endpoint suppliers.

## Output

The two tails are distinct split fibers of `Z^p+Q` with
`deg Q<=2p-d-1`. If that degree cap is at most
`r_*(p,n)=floor((p(p-1)-1)/(n-1))`, no such tails exist and every collision
has width at least `p+1`. Uniformly, at least the final
`floor(11(p-1)/256)` depths close. The terminal affine-line case is included
and independently classified.

## Falsifier

A minimum-width collision not admitting `(FSP3)`, a nonzero split fiber
violating `(FSP5)`, or a collision with `t=p` inside the closed deep subband.

## Nonclaims

No bound for the surviving split-pencil census with degree cap greater than
`r_*(p,n)`, no control of `t>p`, and no L1 status change.
