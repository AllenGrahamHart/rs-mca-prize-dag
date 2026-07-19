# list_planted_arithmetic conditional proof

## Predicate nodes

- `worst_word_planted`
- `worst_word_challenger_pricing`
- `imgfib`

## Claim

Given the listed predicates, the list crossing is decided by integer
arithmetic on the planted column plus the certified challenger/envelope
contribution.

## Proof

The predicate `worst_word_planted` supplies the extremality reduction at the
crossing radii.  For this arithmetic node, the required form of that reduction
is rowwise: every contribution outside the explicit witness families is covered
by the safe-side envelope.  The predicate `worst_word_challenger_pricing`
supplies either an exact count for the structured challenger class or a
certified rowwise upper envelope with matching lower witnesses on the unsafe
rows.

For each candidate agreement index `delta`, the planted family count is a
finite product/sum of integer choices: core choices, petal choices, and scalar
choices.  The challenger/envelope contribution is likewise an explicit integer
quantity once its pricing predicate is supplied.  Therefore the unsafe side is
a direct integer comparison with `eps |F|`; witnesses are obtained by
exhibiting the corresponding planted or challenger configurations.

The predicate `imgfib` supplies the safe-side image-fiber bound above the
reserve, so all non-extremal list contributions are bounded by the printed
margin. Since the relevant quantities are integer counts, the undecided rows
are exactly the Diophantine windows where the integer threshold falls between
the certified lower count and the exact planted-plus-challenger count.

Unlike the MCA value-set census, there is no separate zone-(b) collision
column on this list side: after the predicates are assumed, all live columns
are explicit integer counts or certified integer envelopes. Hence the list
crossing reduces to the stated arithmetic window check.
