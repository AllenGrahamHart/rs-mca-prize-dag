# xr_smallcore_spread_count

- **status:** CONDITIONAL (amber surgery 2026-07-10; dag.json is authoritative)
- **closure:** proof of the two wired predicates
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement (consumer-exact form; supersedes the stale generic-poly wording)

For every generic-branch pair (u,v) at each of the six clean-rate candidates:
the post-strip live bad-slope count satisfies R_post(u,v;A) <= 16 n^3 — the
exact form `xr_clean_residual_any_gate` consumes (sufficiency is exact integer
arithmetic at all six candidates; prize rows tight at 29n^3, slack to the
16-reserve log2(29/16) = 0.858 bits).

DRIFT CORRECTION (2026-07-10 audit, catch #43): this file previously stated
the floor as generic "<= poly(n)" — under-specified against the consumer (a
Cn^5 proof would have satisfied the old wording and broken the gate). It also
carried "WIRING FIX: u1_pullback_dichotomy promoted ev -> req" (RETRACTED —
the promotion died in the 07-05 retraction; the live edge is ev) and "~2^100
slack above n^3" (corrected: 2^92.000 at RowC, 2^4.9 at prize).

## Route of record (amber, 2026-07-10)

IF `xr_highcore_collision_count` (P-A: high-core stratum <= 8n^3) AND
`xr_lowcore_spread_heart` (P-B: low-core stratum <= 8n^3) THEN the floor,
with 8 + 8 = 16 exact. Non-predicate links carried by
`xr_strip_classification_rungs` (strips, rung-2a/2b forcing, consumption
arithmetic — three independent implementations) plus the definitional pins
P1-P6 in the dag statement. Full chain + audit record: dag.json node entry;
banked audit scripts in notes/ (audit_consumption_replay_20260710.py 69/69,
audit_p8p9_local_20260710.py 88/88).

## Attack surface

pairwise-small-core aligned families are sunflower-free configurations of
size-A sets; design/anticode bounds at intersection threshold k+t-1; the
eliminant route counts them as bounded-deficiency solutions; E27's spectrum
calibrates constants; f2_effective_energy_dichotomy portable verbatim to P-B.

## Falsifier

per-predicate pre-registered falsifiers on the P-A / P-B nodes (slope-count
form — moment values alone do NOT refute, posedness catch #42); a toy pair
with super-poly many pairwise-small-core aligned supports remains the
node-level shape (searchable with E27's pencil machinery).

## Ledger (migrated notes, retained)

DECOMPOSED (close-look pass, conventions pinned against qx13): the split is
FORCED by proved machinery — (2a) same-slope families are automatically
far-spread and equal the LIST challenge's worst-word object (the two grand
challenges meet); (2b) the partial-forcing band r in [k+1, A-2] reduces to a
graded tangent ledger via one-line two-slope forcing; (2c) the far-spread
core = the fresh-codimension-or-structure dichotomy — the face's single
irreducible statement. Pairwise additivity at distinct slopes is rank-level
PROVED (qx13 2b); only the m >= 3 stagnation dichotomy is genuinely open.
[2026-07-10 note: legs 2a/2b are the P1/P2 pins of the amber; leg 2c's
dichotomy lives inside P-B's attack surface.]
