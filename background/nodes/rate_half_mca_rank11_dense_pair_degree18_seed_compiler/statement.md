# Rank-eleven dense-pair degree-18 seed compiler

- **status:** PROVED
- **scope:** the deployed KoalaBear post-near error-rank-eleven branch
- **input:** the low-margin pair/core ledger and the common-support
  cancellation adapter

Every unsafe line in this branch contains `32` distinct actual records with
support-local margin at most `387` having the following properties.

1. Eighteen records are owned by one fixed minimizing pair `p_0`.
2. At least one selected record has an explanation outside the affine
   codeword line of `p_0`.
3. If `C` is the exact intersection of the selected supports, then

   ```text
   |C| <= K-2601.
   ```

Apply the proved common-support cancellation to `C`. The resulting
`32` explanations in `RS[F,D\C,K-|C|]` are not globally affine, and their
coefficientwise interpolation in the slope has degree between `18` and
`31`. The same is true of the residual slope-error polynomial.

Thus the degree-`3..17` staircase exposed by arbitrary common-support
shortening cannot occur for this deliberately selected unsafe rank-eleven
seed. The conclusion is a tuple compiler and degree pin. It is not a
whole-line payment and does not by itself discharge the rational,
pure-locator, denominator-root, high-complexity spread, or chronology-owner
branches.

## Falsifier

An unsafe deployed rank-eleven line for which the printed low-record and
pair-type bounds do not force one pair to own `220` records; a basis-pair
selection requiring more than `14` records or leaving more than six singly
represented cores; a selected common support larger than `K-2601`; or a
degree-at-most-`17` residual interpolation containing the eighteen dense-pair
records and the certified off-line record.
