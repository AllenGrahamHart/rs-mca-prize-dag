# list_planted_arithmetic conditional proof

## Predicate nodes

- `worst_word_planted`
- `worst_word_challenger_pricing`
- `imgfib`

## Claim

Given the listed predicates, the list crossing is decided by exact integer
arithmetic on the planted and structured-challenger columns.

## Proof

The predicate `worst_word_planted` supplies the extremality reduction at the
crossing radii: the worst received words are exhausted by the planted
sunflower family together with the revised structured challenger class. The
predicate `worst_word_challenger_pricing` supplies the explicit count for that
second class.

For each candidate agreement index `delta`, the planted family count is a
finite product/sum of integer choices: core choices, petal choices, and scalar
choices. The challenger column is likewise an explicit integer count once its
pricing predicate is supplied. Therefore the unsafe side is a direct exact
integer comparison with `eps |F|`; witnesses are obtained by exhibiting the
corresponding planted or challenger configurations.

The predicate `imgfib` supplies the safe-side image-fiber bound above the
reserve, so all non-extremal list contributions are bounded by the printed
margin. Since the relevant quantities are integer counts, the undecided rows
are exactly the Diophantine windows where the integer threshold falls between
the certified lower count and the exact planted-plus-challenger count.

Unlike the MCA value-set census, there is no separate zone-(b) collision
column on this list side: after the predicates are assumed, all live columns
are explicit counts. Hence the list crossing reduces to the stated exact
arithmetic window check.
