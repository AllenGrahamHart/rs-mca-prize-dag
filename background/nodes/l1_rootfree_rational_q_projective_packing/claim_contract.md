# Claim contract - L1 root-free rational-Q projective packing

## Inputs

- the boundary-Q planted-root descent;
- nonempty residual branch with `r<k`;
- the complete-agreement and root-free guards.

## Outputs

- exact projective space `V=span(G,W_1 F[X]_<d)`;
- projective dimension `d=k-r` and codimension `w`;
- no common domain root and no split point at infinity;
- exact packing bound `floor(binom(n-r,d)/binom(m-r,d))`;
- polynomial payment for fixed residual dimension `d`.
- `exp(O(d))` payment at linear locator density, hence a subexponential
  payment for `d=o(n)` and reserve absorption for `d=o(R log |B|)`.

## Consumer rule

Apply the exact packing payment before invoking Q.  Remove every fixed-`d`
cell analytically, and in asymptotic work remove every `d=o(n)` cell at its
printed reserve scale.  Pose the surviving frontier Q input only for
root-free projective Conjecture-F cells whose residual dimension is large
enough to escape `(PC4)`.

## Nonclaims

The packing ceiling is not an average-normalized Q estimate and may be
exponential for growing `d`.  No cross-cell owner sum or finite row numerator
is supplied.

## Falsifier

A nonempty cell with `dim P(V)!=d`, a common domain root, a split locator in
the infinity hyperplane, two locators sharing `d` roots, or a count exceeding
`(PC3)`.
