# Claim contract - L1 exact-shell balanced shifted-lattice reduction

## Inputs

- the Pade/support-moment identity and complete-agreement gcd guard;
- the shifted interpolation module over an arbitrary evaluation set;
- the band inequality `2m<=n+k-1`;
- Reed--Solomon minimum distance.

## Outputs

- exact support-census representation in the shifted module;
- near-rational dichotomy at `d_1<=w`;
- emptiness of the level-`m` exact shell throughout that branch;
- balanced degree interval `w+1<=d_1<=d_2<=omega` for every nonempty shell;
- unique two-generator pencil coordinates of dimension `omega-w+1`;
- complement exactness guard `gcd(Q,W)=1`.

## Consumer rule

In the band, compute one shifted-reduced basis per received word.  Delete the
entire `d_1<=w` branch from the exact-shell ledger.  On the survivor, count
the guarded balanced split pencil; do not pay the near-rational binomial
support mass as though it were a list of distinct codewords.

## Nonclaims

No balanced-pencil count, owner classification, base-field normalization,
finite reserve inequality, or deep-shell theorem is proved.

## Falsifier

A band word with `d_1<=w` and a codeword of exact agreement `m`, a census
element outside the shifted module dictionary, nonunique balanced
coordinates, an incorrect degree/dimension ledger, or a guarded pencil point
with an extra complement agreement.
