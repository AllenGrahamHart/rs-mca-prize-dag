# list_grand

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md']

## Statement

For each admissible C and constant m: exhibit adjacent delta with |Lambda(C^{==m},.)| crossing 2^-128 |F| at it.

## Root interface

The logical premise set is `s0_zero_open`, `mixed_radix_frontier`, and
`list_large_m_scope_closure`. The latter consumes the ordinary crossing from
`list_adjacency_closing` and proves that the same adjacent pair works for every
constant `m`. The direct `list_adjacency_closing`, `list_safe`, and
`list_unsafe` root edges are evidence/support only.

## Ledger (migrated notes)

Same three-rate pivot applies (list side mirrors: clean extras-zero margins at 1/4-1/16; the rate-1/2 band is a list-side object). | TOP-LAYER SUFFICIENCY AUDIT (2026-07-04, user-prompted): the conjunction of the five req children IS sufficient, definitional-with-guards: list_adjacency_closing carries the grand's operational content per-row (the adjacent-delta exhibit); list_safe/list_unsafe supply the two bounds the exhibit consumes; s0_zero_open guards object-identity (axes EQUAL or BRIDGED, loss printed); mixed_radix_frontier guards the domain family (likely vacuous under the 2-power reading). QUANTIFIER COVERAGE VERIFIED: rate 1/2 is NOT silently missing — it enters as rate_half_coverage_gap, a req of list_adjacency_closing; the m-quantifier is carried by rules_m_reading (PROVED) as ev of the closing node and inside list_safe's statement. NOTED REDUNDANCY (harmless): safe/unsafe are partially restated inside the closing node's exhibit — conjunction remains sufficient. SEAM TO WATCH: list_safe's 'above the window' language must match the closing exhibit's delta convention — that seam is exactly s0's axis discipline. | FLIPPED TARGET -> CONDITIONAL 2026-07-04: the assembly implication is a PACKET (list_grand_assembly_implication.md) with a statement-pin verifier — edits to any child's statement fail the packet and force re-refereeing. The prize's list half is now proved conditional on its five inputs.

On 2026-07-18 the live edge set was reconciled with the 12 July arity repair:
the lower-level closing node now owns only `m=1`, and
`list_large_m_scope_closure` owns the universal constant-arity transport.
