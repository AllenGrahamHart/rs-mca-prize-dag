# safe_assembly_uniformity

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s8_s9_assembly_and_negative.md']

## Statement

The implicit lemma 'counting_frame + fm1 + strip + paid_closure + r2 + ext_lift => mca_safe' holds UNIFORMLY over the admissible family: (i) every exponent (B <= 3, B_F, budget arithmetic) is an absolute constant, not n-drifting; (ii) the stratified sum + first-match dedup compose with endpoint conventions printed once (descriptor-generated); (iii) the composition survives k up to 2^40 scales symbolically (wp3_2). The last unpriced composite implication of the adjacency/payment-completeness class.

## Attack surface

mostly bookkeeping made explicit: a one-note assembly proof template with a constants ledger; the genuine content is the uniformity audit of each input's constant

## Falsifier

any input theorem whose constant is discovered to drift with n (would localize immediately in the constants ledger)

## Ledger (migrated notes)

prices the children => parent step that the map previously asserted silently; its mirror on the list side rides list_planted_arithmetic + imgfib's uniform exponent
