# Claim contract - L1 official coarse p-free entropy reserve

## Inputs

- the official generated-field and four-rate setup;
- the canonical reserve depth `d_0=ell_0-1`;
- `ell_0<=p-3174` and the at-most-23 checkpoint theorem.

## Output

At every checkpoint depth `d>=p`, the ambient average coarse p-free fiber is
less than `2^-28276`. Consequently ambient max-to-average inflation at most
`q 2^28148` is sufficient for the finite `q/2^128` bound. More sharply, a
per-p-free-condition bound
`max_s Exc_d(s)<=2^(15(d-r))mu_free(d)` on an exactly owner-pruned extras
residual forces that residual below one, hence makes it empty.

## Falsifier

An official parameter tuple for which the first checkpoint has
`d-d_0<3175`, more than 23 checkpoints occur, a legal binomial step exceeds
15, the generated-field degree at an active checkpoint is below two, or the
displayed exponent arithmetic fails.

## Nonclaims

No max-fiber theorem, no image-normalized average, no construction or payment
of the structured owner, no transport from F2's zero-target extras census, no
Pade-graph or cofactor coalescing, and no L1 status change.
