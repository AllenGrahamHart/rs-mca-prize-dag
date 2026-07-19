# axis8_generating proof

## Source

ABF26 local PDF:
`/home/u2470931/smooth-read-solomin/rs-mca-codex-critical/experimental/data/certificates/abf26.pdf`

SHA-256:
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5`

## Claim

The official family admits non-generating rows. Therefore the tower case is
admissible and must be priced by the `ext_lift` / `f1_classification` chain.

## Proof

ABF26 defines the Reed-Solomon code over an arbitrary finite field `F` with a
smooth multiplicative subgroup `L` of power-of-two size. The grand MCA
challenge asks for the threshold for Reed-Solomon codes of this form under the
printed rate and size caps; it does not impose that `L` generate `F` as a
field.

Consequently extension rows are admissible. For example, if a base field
contains the required power-of-two subgroup `L`, the same `L` can be viewed
inside a finite extension field `F` while preserving the smooth-domain and rate
requirements. This is exactly the non-generating case: the evaluation subgroup
lies in a proper subfield of the ambient field.

Thus the adverse reading is the official one for the campaign: non-generating
rows are not excluded by the source, so intermediate-field/tower slopes must be
priced rather than discarded.
