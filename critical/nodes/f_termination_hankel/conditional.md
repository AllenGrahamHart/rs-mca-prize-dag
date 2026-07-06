# f_termination_hankel conditional proof
## Predicate nodes
- `hankel_rank_profile_entropy`
- `hankel_moment_clean_leaves`
## Claim
The Hankel-family descent terminates with poly(n) cost and valid member
accounting: reachable unpaid primitive saturated states number n^{O(W^2)}
(fixed cutoff W), and leaves feed the moment/residue count.
## Proof
Saturated root-closure accounting (QF.12, states = forced-root sets, budget
drops per edge) + the rank-profile dichotomy (predicate 1) gives bounded
unpaid branching entropy along every path (wide: Delta_u <= 1; row-deficient:
principal/MDS, Delta_u <= 1; narrow row-full: O(W) branching levels of degree
<= n^W); the Kraft argument converts this to n^{O(W^2)} states. Paid states
route to the proved ledgers (gcd_reduction, scale_recursion, the projective
weight-2 inverse; the dihedral/Chebyshev syndrome transform M^chi_{i,r} =
S_{i+e+Mr} + eta^r S_{i+e-Mr} supplies the quotient instance — bookkeeping of
fixed fibers rides the paid ledger). Member counts at leaves = predicate 2.
