# proof: rules_freeze

- **status:** PROVED
- **closure:** citation

## Source

Vendored from the working record; primary artifact(s):
- `wp_detail/wp0_2_wp4_4_rules_freeze_and_dither.md#2`

## Ledger

ADD TO THE FREEZE TABLE (crux-2-relevant): does a proved-correct per-row decision procedure emitting machine-checkable certificates satisfy the grand challenges' 'determine for each admissible C' — i.e., are compiler semantics acceptable? The answer moves the certifier_uniformity burden dramatically. | WIRING COMPLETED (user catch #4, 2026-07-04): rules_m_reading (PROVED) was an unwired component — now req. Component ledger: field_cap_check WIRED+PROVED; m-reading WIRED+PROVED; smooth-reading and rates-exactness citations RESOLVED in the rules-layer resolution (blueprint line 102 / live-fetch quotes, ba75cec7) but not yet assembled as the quote+hash certificate — THAT assembly is exactly the declaration act this node's amber awaits. The amber is now honestly scoped: requirements-met on the wired components; certificate assembly pending. | PAPER VERIFICATION PASS (2026-07-04, abf26.pdf in-repo, sha256 426a979c13cc61db0f2cdb909067ef4c9f244388...): COMPONENT 1 CONFIRMED VERBATIM from the actual paper, p.4: 'we will focus almost exclusively on the Reed-Solomon code C := RS[F,L,k] where L is a multiplicative subgroup of F whose size is a power of two' — NUANCE: subgroup, not coset; our coset-form analysis is the conservative superset. NOT LOCATED in the pages read (1-4, 12-15, 32-33): the k <= 2^40 / |F| < 2^256 caps (sec 6.4 is the toy-protocol Koala Bear example, NOT the prize caps), the exact-rate set, the constant-m wording — these are PRIZE-PAGE constants per the earlier live-fetch quotes (wp0_2), and field_cap_check's provenance should be re-pointed accordingly. VERDICT: NO GREEN FLIP on a partial pass — remains amber; remaining act = locate/quote the caps' authoritative source (prize page + paper section sweep) and assemble the full quote+hash certificate. | FLIPPED GREEN 2026-07-04: ALL FOUR COMPONENTS CONFIRMED VERBATIM from abf26.pdf p.5 (the two grand-challenge boxes + the caps sentence) — citation certificate with quotes, pages, and PDF sha256 at experimental/data/certificates/rules-freeze/rules_freeze.json  <!-- filename fixed 2026-07-10, catch #63 -->. Closure: citation. BONUS: Theorem 4.7 [Jo26] (interleaved MCA = base MCA exactly) recorded for the m_handling consumers.
