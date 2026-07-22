# Claim contract - L1 Pade split-section/support-moment inversion

## Inputs

- an arbitrary finite evaluation set and its interpolation polynomial;
- the full-locator Pade section;
- the exact-shell complement gcd guard;
- uniqueness of a degree-below-`k` interpolant on at least `k` points.

## Outputs

- equality of the unguarded Pade split count and upstream support census;
- exact support-moment identity `C_m=sum_a binom(a,m)Z_a`;
- finite binomial inversion recovering every exact-shell count;
- direct upper-bound transfer `Z_m<=C_m`.

## Consumer rule

Use the unguarded support census only with its binomial multiplicity visible.
Use the gcd guard or `(PS2)` to recover complete agreement shells.  An
upstream support-census theorem may upper-bound L1 directly through `(PS3)`,
but its owner and finite-budget conventions must still be checked.

## Nonclaims

No prefix flatness, split-pencil bound, primitive/quotient label transport,
base-field normalization, or finite adjacent-row reserve is proved.

## Falsifier

A valid support missing from the Pade section, a Pade split point with no
degree-below-`k` explanation, a support with two explaining codewords, a
profile violating either transform, or a guarded split point that is not a
complete agreement set.
