# Result

Each fixed normalized first-checkpoint perturbation `Q` has at most 23 fully
domain-split values and at most 253 unordered split-fiber pairs. The surviving
minimum-width census is therefore a census of perturbations `Q` with a
constant-size value ledger, not an independent `(Q,b,c)` parameter space.
The value ledger is recovered exactly as the squarefree gcd of the
degree-at-most-23 coefficient remainders of
`(Z^n-alpha) mod (Z^p+Q-T)`. A `p` by at-most-24 coefficient matrix supplies
a necessary rank-defect filter for the existence of a pair.

Rows with `2p>n` have no minimum-width pair at all. In the next band
`2p<=n<3p`, pair existence forces `deg Q>=3p-n`, which closes every
first-checkpoint depth `d>=n-p`. For `(n,p)=(8192,3583)`, the closed boundary
is `d=4609`, improving the ratio-only boundary `d=5599`.
