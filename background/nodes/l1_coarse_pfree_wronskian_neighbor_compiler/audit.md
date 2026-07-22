# Audit - L1 coarse p-free Wronskian neighbor compiler

1. Injectivity fixes `X`; no uniqueness is claimed after `X` varies.
2. Monicity makes the difference of two candidate tails have degree below
   `t`.
3. Squarefreeness, not a characteristic-zero derivative argument, gives
   `gcd(F_X,F_X')=1`.
4. The Wronskian is nonzero on both tails, but `(WNC4)` consumes only the
   known `X` restriction.
5. Inclusion-exclusion counts the zero polynomial correctly when more than
   `D` vanishing conditions are imposed.
6. The complement count is `binom(n-a,t)`, since `Y` is disjoint from the
   entire anchor `A`.
7. The neighbor sum stops at `min(a,n-a)` and is empty when `tau` exceeds
   that endpoint.
8. The exponential `binom(a,t)` exchange choice remains explicit.
9. No computation or probabilistic estimate is load-bearing.
10. The parity hierarchy is indexed from the formal half-depth `tau_0`, but
    the neighbor sum starts at the stronger admissible endpoint `tau_p`.
