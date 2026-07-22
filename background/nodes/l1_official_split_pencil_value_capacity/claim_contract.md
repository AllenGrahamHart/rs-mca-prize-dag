# Claim contract - L1 official split-pencil value capacity

## Inputs

- an official `n`-point multiplicative coset in characteristic `p`;
- the proved inequality `p>n/24`;
- the first-checkpoint representation by two distinct fully split fibers of
  one normalized `Z^p+Q` pencil.

## Output

For fixed normalized `Q`, at most `floor(n/p)<=23` values give a fully split
degree-`p` fiber, and hence at most `253` unordered fiber pairs occur. The
degree-at-most-23 gcd of the coefficient remainders of
`(Z^n-alpha) mod (Z^p+Q-T)` is exactly the squarefree split-value polynomial.
A collision requires the associated narrow coefficient matrix to have rank
at most `floor(n/p)-1`. If `2p>n`, no pair exists. If `2p<=n<3p`, pair
existence forces `deg Q>=3p-n`, so first-checkpoint depths `d>=n-p` have no
minimum-width collision. In the surviving `m=2` band, the complement locator
uniquely determines the unordered pair through the test
`(Z^n-alpha)/C=R^2+c`, giving the cap `binom(n,n-2p)`.

## Falsifier

A fixed polynomial `P=Z^p+Q` with 24 distinct values whose degree-`p` fibers
all lie in the same official `n`-point domain, or more than 253 unordered
split-fiber pairs; a root of `G_Q` not giving a split fiber; a split value
missing from `G_Q`; or a collision whose remainder matrix has rank at least
`floor(n/p)`; or a two-fiber pencil with `2p<=n<3p` and `deg Q<3p-n`.
Also, two distinct collision pairs with the same complement locator falsify
the complement compiler.

## Nonclaims

No bound on the number of perturbations `Q` in the surviving band, no bound
on the number of complements satisfying the square-quotient condition beyond
the raw binomial cap, no bound on `t>p`, no row-sharp fiber estimate, and no
L1 status change.
