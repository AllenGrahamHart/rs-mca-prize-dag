# Claim contract - L1 official Frobenius-checkpoint Q router

## Inputs

- the official generated field and strict 256-bit cap;
- a monic split locator of degree `a`;
- a prefix depth `0<=d<=a<=n-1`;
- for the shell consequence, one fixed error cofactor.

## Output

The characteristic satisfies `p>n/24`. The locator prefix is bijectively
equivalent to the p-free power sums through depth `d` plus the elementary
coordinates at the at most 23 positive multiples of `p`.

Every mixed fiber is contained in the coarse p-free fiber obtained by
forgetting its checkpoints. Direct coarse-fiber flatness therefore transfers
with no loss. A uniform conditional bound may instead be unioned at
qualitative cost `<n^453`, but that raw union can never certify the finite
`q/2^128` prize threshold when at least one checkpoint is present.

## Falsifier

Two locator prefixes with the same mixed coordinates; failure of the inverse
recursion; an official row with more than 23 characteristic checkpoints
below depth `n`; or a mixed fiber not contained in its coarse p-free fiber.

## Nonclaims

No p-free max-fiber bound, checkpoint-conditioning bound, finite raw `q^r`
payment, Pade-graph transversality, or implication from F2 Myerson. The
`n^453` estimate preserves only qualitative polynomiality.
