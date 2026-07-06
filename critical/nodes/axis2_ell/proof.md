# axis2_ell proof

## Source

ABF26 local PDF:
`/home/u2470931/smooth-read-solomin/rs-mca-codex-critical/experimental/data/certificates/abf26.pdf`

SHA-256:
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5`

## Claim

The official MCA challenge quantifies over pairs of words, not arbitrary
ell-tuples.

## Proof

ABF26 states the grand MCA challenge for Reed-Solomon codes with respect to the
family of lines. In Section 4.1, both CA and MCA are defined from two words
`f1, f2`; the local bad event compares the same pair against the two-way
interleaved code `C^{equiv 2}` on the relevant support.

The paper separately discusses interleaved codes and records that MCA for
`C^{equiv t}` equals MCA for the base code, but that is an interleaving
stability theorem, not a change of the grand MCA sampler into arbitrary
ell-tuples. Therefore the official MCA object is pair/line based.
