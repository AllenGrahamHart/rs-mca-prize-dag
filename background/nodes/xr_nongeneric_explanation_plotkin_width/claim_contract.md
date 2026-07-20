# Claim contract - XR nongeneric-explanation Plotkin width

## Inputs

- pairwise intersection at most `K-1` for distinct joint explanations;
- invariant excess `h=A-K` and ambient drop at least `h+1`;
- the true-tangent coordinate injection;
- deterministic canonical support and explanation ordering.

## Output

The support code satisfies `(XW2)--(XW4)`. The terminal nongeneric subtree
satisfies the exact instance and tangent-charge bounds `(XW5)--(XW6)`, and
every fixed logarithmic terminal window satisfies `(XW7)--(XW9)`.

## Consumer rule

Consumers may discard the entire nongeneric instance tree and genuine-tangent
charges in every fixed logarithmic terminal window. They must retain
generic-chart slopes and slope-to-explanation fibers.

## Falsifier

An explanation family violating `(XW2)--(XW4)`, a terminal canonical descent
tree with more than `1+104H` live instances, or a use of `(XW6)` that includes
generic mismatch slopes.
