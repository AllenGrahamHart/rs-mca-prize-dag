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

## Falsifier

Two locator prefixes with the same mixed coordinates; failure of the inverse
recursion; or an official row with more than 23 characteristic checkpoints
below depth `n`.

## Nonclaims

No p-free max-fiber bound, checkpoint-conditioning bound, raw `q^r` payment,
Pade-graph transversality, or implication from F2 Myerson.
