# Claim contract - L1 coarse p-free Wronskian neighbor compiler

## Inputs

- one finite field and distinct evaluation set;
- one coarse p-free depth-`d` fiber on `a`-subsets;
- the proved Wronskian distance theorem and tame-tail endpoint upgrade.

## Output

For a fixed anchor and exchanged subset `X`, every colliding tail has a unique
Wronskian certificate of degree at most `2t-d-2`, nonzero on `X`. The exact
certificate census gives `(WNC4)`, the max-fiber neighbor bound `(WNC5)`, and
the even/odd collision-gap hierarchy `(WNC6)`. Formal strata below `tau_p`
are absent.

## Falsifier

Two distinct monic degree-`t` tails with the same fixed `X` and Wronskian, a
Wronskian zero on `X union Y`, or a coarse fiber exceeding `(WNC5)`.

## Nonclaims

No compression of the exchanged-subset choice, no row-sharp finite payment,
no checkpoint-conditioned Pade theorem, and no L1 status change.
