# Cycle 495: pair-pencil affine-line cap and direction router

## Result: PROVED line cap 15 and 38 root-rich directions

On one affine line of scalar polynomials, all quotient pair codewords agree
on the same root locus, so every two complete pair cores have one common
intersection `J`. Outside `J` the cores are disjoint. Since `|J|<=K-1`, the
exact union inequality permits at most 15 of the size-1,116,046 cores on one
affine scalar line. Scalar dimension one is therefore impossible.

A fixed projective direction may occur on many parallel lines. Maximizing
its pair count under the 15-point line cap gives

```text
34*C(15,2)+C(10,2)=3615.
```

The 520 selected points have 134,940 unordered pairs, so they determine at
least 38 projective directions. Every represented direction polynomial has
at least 134,940 official-domain roots. In scalar dimension two, all 38 are
members of one base-field polynomial pencil.

## Burn-down

```text
starting local pin:       dc3d28e6c
canonical prize pin:      0dd5b3244
upstream frontier pin:    PR #1173 at 2788d5ec3
DAG delta:                +1 PROVED direction-router node, +2 edges
critical status delta:    none
closed interface:         scalar dimension one and affine-line overpopulation
compute spend:            none
next action:              pay the 38-member dimension-two pencil or concentrate dimensions 3/4
```

## Nonclaims

- root-rich direction polynomials are not asserted to split completely;
- dimensions three and four are not reduced to one pencil;
- no high-complexity payment, rank-eleven closure, or MCA closure.
