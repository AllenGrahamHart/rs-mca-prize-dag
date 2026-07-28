# Claim contract

## Inputs

- the proved `V=50` endpoint, so `V=48` is the next live even level;
- the proved sparse-L1 slack recurrence and signed-chord identity;
- the proved complete even-parity light atlas from the E26 reduction;
- the collision norm criterion for the ambient E1 route.

## Output

Every `V=48` profile-(3,4,0) candidate lies in one of the six profiles and 154
affine templates printed in `statement.md`.

## Nonclaims

- no candidate in the six surviving profiles is excluded by this node;
- no cubic-Hermite inequality or nonnegative third-moment cutoff is used;
- no claim is made about profile `(4,2,0)`, later bands, or `N!=256`;
- the endpoint and either prize terminal remain open at this node alone.

## Falsifier

A `V=48` candidate with `L>14`, a tenth energy profile, a surviving eight-odd
profile, or a light support outside the pinned zero/four-odd atlases refutes
the reduction.
