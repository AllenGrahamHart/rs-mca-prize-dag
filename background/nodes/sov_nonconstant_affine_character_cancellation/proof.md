# proof: sov_nonconstant_affine_character_cancellation

Translate the affine space so that `V` is a vector space plus a base point
`v_0`. Write

```text
c(v_0+u) = c(v_0) + ell(u),
```

where `ell` is a nonzero linear functional on the underlying vector space.
For `xi != 0`, the functional `xi ell` is also nonzero. Therefore its kernel
has codimension one, and each value in `F` has exactly `|ker ell|` preimages.

The character sum is

```text
sum_{u in V} psi(xi c(v_0+u))
  = psi(xi c(v_0)) sum_{u in V} psi(xi ell(u)).
```

Since `xi ell` is surjective onto `F`, the second sum is

```text
|ker ell| sum_{a in F} psi(a).
```

A nontrivial additive character sums to zero over the field, so the affine
piece contributes zero.

Now suppose a conditioning cell is a disjoint union of affine pieces of this
kind and an exceptional set `E`. Every cancellative affine piece contributes
zero to every nontrivial character sum. The remaining contribution comes only
from `E`, and each summand has absolute value one. Hence the total absolute
value is at most `|E|`.

This proves the formal cancellation lemma. The separate node
`sov_hminus1_affine_piece_decomposition` must still prove that the actual
anchored-core conditioning cells admit such a partition with a budget-small
exceptional set.
