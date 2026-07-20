# Claim contract - L1 fixed-support codeword quotient bound

## Inputs

- one received word and maximal-sunflower source chart;
- one exact labelled petal-support pattern;
- degree-`<k` Reed-Solomon codewords and the L1 polarity/field bounds.

## Output

The fixed-support codeword cell injects into degree-at-most-`N-h`
polynomials. Every fixed `(p,N-h)` box is polynomial per source chart with
bound `(CQ4)`.

## Consumer rule

Consumers may require `N-h=a-s` to escape arbitrary fixed caps on the
bounded-polarity sub-Johnson branch. They may not infer that the quotient is
split or omit non-intrinsic chart multiplicity.

## Falsifier

Two distinct codewords with the same quotient `(CQ1)`, or a fixed-support
cell exceeding `(CQ2)`.
