# axis1_batching proof

## Source

ABF26 local PDF:
`/home/u2470931/smooth-read-solomin/rs-mca-codex-critical/experimental/data/certificates/abf26.pdf`

SHA-256:
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5`

## Claim

The official MCA sampler batches along affine lines `u + z v`, matching the
repo convention.

## Proof

ABF26 Section 1 introduces the relevant family as lines of the form
`{f1 + gamma f2}_gamma`. The grand MCA challenge then states that the paper
considers MCA with respect to that line family. Section 4.1 repeats the formal
definition using arbitrary words `f1, f2` and the corresponding line
`L = {f1 + gamma f2}`.

Thus the sampled object is an affine line in the two received words. No
powers-of-alpha or nonlinear batching convention appears in the official MCA
definition being used by the prize challenge.
