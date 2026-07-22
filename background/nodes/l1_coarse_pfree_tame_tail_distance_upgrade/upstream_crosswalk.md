# Upstream crosswalk - tame-tail collision-gap upgrade

This strengthens the upstream-style collision-gap hierarchy for coarse
p-free `(Q)`. In the tame-tail range, the first nontrivial gap is `d+1`, not
the formal half-depth Wronskian floor. At checkpoint depth, the first possible
collision has width at least the characteristic; on official rows this is
greater than `n/24`.

The proof is elementary and vendorable: a too-small Wronskian forces the
first `t` moments to agree, and Newton identities identify the tails when
`t<p`. The strict endpoint must travel with the result, since the sharp
characteristic-two fixture at `t=p` defeats the non-strict statement.
