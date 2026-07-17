# rate_half_band_closure

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md']

## Statement

Cover the 2,978,147-radius band at prize-max rate 1/2 (M_max = 2^33 vs sigma* = 8,592,912,738) by a new mechanism (quotient windows and integrality both fall short) — or the rate-1/2 determination lands bracket-grade there. Rates 1/4, 1/8, 1/16 need nothing (clean by margins < -121). THE rate-1/2 battlefield node.

## Attack surface

a third mechanism for the band: extended quotient scales, averaged conversion at giant M, or the B2b-style balance analysis

## Falsifier

a band radius provably uncoverable by any priced mechanism

## [LIST-SIDE RETIREMENT + MCA/CA RE-SCOPE (wave-8 audited, 2026-07-16)]

The GRAND-LIST-DECODING half of this obligation is RETIRED BY THEOREM:
`rate_half_cyclic_rotated_prefix_floor` (PROVED, imported; + background
`rate_half_fixed_tail_prefix_floor`) proves the entire residual band
2^33 < sigma <= sigma* list-unsafe at sigma* — the trigger count
> q/2^128 is exactly the prize's |Lambda(C^{==m})| <= 2^-128 |F| object
— for ordinary + every constant common-support arity, every admissible
q < 2^256 (margin 75.0796 bits at q=2^256; cap boundary 256.0366 > 256;
agreement = k+sigma* exact). With the banked safe side, the rate-1/2
LIST crossing is DETERMINED; list_adjacency_closing consumes the PROVED
node directly. REMAINING for this red: the support-wise MCA/CA crossing
only (trigger ~ q/k). GUARD (verbatim, audited): any MCA-side argument
must not reuse the list threshold q/2^128 as an MCA surrogate — the two
triggers are different objects (separation measured:
notes/rate_half_trigger_separation_modal.py).

## [CORRECTION to the wave-8 addendum above (2026-07-17, w9-C2 — our
## own overclaim, caught by the wave-9 audit via v4's scope audit)]

The sentence "With the banked safe side, the rate-1/2 LIST crossing is
DETERMINED" is WITHDRAWN. The "banked safe side above sigma*" was
planning prose, not an in-repo theorem (the Paper D pincer stops at
half distance; r2_clean_rates excludes rate 1/2), and the s = c-1
instantiation of the cyclic floor proves list-unsafety THROUGH
sigma_0 = 8,594,128,895 > sigma*. Corrected state: the LIST UNSAFE
side is proved through sigma_0 (the cyclic floor node, strengthened);
the LIST SAFE side is OPEN (field-dependent); the crossing is NOT
determined. The retirement claim narrows accordingly: what is retired
is the unsafety obligation on the band, not the crossing location.
This node's own open content remains the MCA/CA half — now re-posed by
the audited v4 work as (RH-ADJ): find field-dependent a_RH(q) >=
k + 8,594,128,896 with B_mca(a_RH) <= floor(q/2^128) < B_mca(a_RH - 1).
