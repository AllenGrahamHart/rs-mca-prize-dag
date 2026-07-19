# axis4_predicate proof

## Sources

ABF26 local PDF:
`/home/u2470931/smooth-read-solomin/rs-mca-codex-critical/experimental/data/certificates/abf26.pdf`

SHA-256:
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5`

Local predicate node:
`noncontain_degeneracy` (PROVED)

## Claim

ABF's support-wise predicate
`Delta_S((f1,f2), C^{equiv 2}) > 0` is exactly the repo's same-support
degenerate-pencil residue predicate.

## Proof

ABF26 Definition 4.3 declares a line point bad when there is a support `S` on
which `f1 + gamma f2` agrees with some codeword, but the pair `(f1, f2)` does
not agree on that same support with any pair of codewords in the two-way
interleaved code.

In repo language, the first condition says the slope `gamma` has an aligned
support `S`. The second condition says the whole pencil is not contained in the
same support-wise code product. The proved node `noncontain_degeneracy`
identifies precisely this noncontainment with the degenerate-pencil residue
`a = b = 0`.

Therefore the ABF predicate and the repo's same-support degenerate-pencil
predicate are the same condition, written in the two notational systems.
