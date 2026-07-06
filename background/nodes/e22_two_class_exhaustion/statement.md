# e22_two_class_exhaustion

- **status:** PROVED
- **closure:** proof

## Statement

At the relevant low-slack crossing radii, every non-planted list word for the
planted sunflower receiver lies in the structured E15 challenger class:
mixed-petal or full-petal. Equivalently, after planted words are removed,
there is no one-petal-only or background/core-only third challenger class.

## Proof artifact

`proof.md` gives the algebraic exclusion. A third-class word would have to
vanish on exactly `k-1` zero-valued coordinates and agree on one whole petal.
Replacing any core roots by background roots gives a rational function
`L_Z/L_C` constant on that petal; after cancelling common core roots this
would make a degree-`r < ell` polynomial vanish on `ell` petal points. Hence
the replacement is empty, so the word is planted.

`verify.py` is a finite sanity check over the reconstructed E22 sweep cells.

## Historical evidence

The exact local E15 gate at n=16, sigma=1 has UNCLASSIFIED=0 for
k in {1,2,4,8}; k=2,4,8 beat the planted count using mixed/full-petal
challengers. The detached 135-cell E22 census was canceled at 130/135 cells
and is not a complete certificate.

## Falsifier

An exhaustive cell with `unclassified > 0`, or an explicit low-slack word
family outside planted plus mixed/full-petal classes.
