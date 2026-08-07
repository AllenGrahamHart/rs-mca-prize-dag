# Claim contract - L1 general first-layout domination

## Inputs

- one admissible maximal sunflower source layout representing the same
  received word `U`;
- its common base polynomial, core, background, petals, and distinct nonzero
  labels;
- the ordinary Reed--Solomon list threshold and degree bound.

## Output

Every listed non-anchor is carried in the first layout by `(GL5)`, and every
selected source-admissible class satisfies the global composition bound
`(GL6)`. The result is uniform in `ell`.

## Consumer rule

Apply all per-source payments only to the fixed first layout and add at most
`M` anchors. Do not sum the same payment over maximal source layouts. Any
remaining first-match obligation must name an internal contributor-dependent
rechart not covered by universal source carriage.

## Nonclaims

The theorem does not bound the first layout's non-planted residual, force its
arbitrary petals into a quotient pencil, or aggregate internal quotient and
Forney chart cells.

## Falsifier

A listed codeword that is not a planted anchor of an admissible layout but
fails `(GL5)`, or a later first-carried source-layout member outside the first
layout's anchor set.
