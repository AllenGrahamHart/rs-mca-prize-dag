# xr_pencil_cascade

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

If a pair (u,v) has two aligned supports (distinct slopes) whose agreement sets share a common core of size >= k+t-1 = A-1, then the slope pencil is FORCED on the core (interpolation: core >= k determines both explaining codewords, the 2x2 slope system inverts), and the alignment CASCADES: every off-core point upgrades one further slope. E27 verified every observed cascade algebraically at RS[F_97, mu_16, k=8] (the multiplicity-2 stratum has a -8.8 sigma HOLE at cores >= A-1: big-core mult-2 events are impossible, exactly as the lemma predicts). The argument is interpolation + the two-slope trick — scale-free.

[SCOPE CORRECTION, ratified 2026-08-02 — see
`notes/PAYMENT_UNSOURCED_FLAG_20260802.md`.] PROVED = the forcing and the
cascade ONLY. The former clauses "the pair's multiplicity is ~n-core" and
"the pair is a TANGENT-PENCIL pair — paid" are WITHDRAWN from the proved
scope: the multiplicity clause silently assumed ONE forced pencil (the
F_17 witness realizes 8 forced pencils against n-core = 6), and no banked
payment covers the tier (T2/P2 never fires at exactly A; the
coordinate-injection hypothesis |T| <= n-A sits one notch short; the
upstream "paid" sense is a CONJECTURE clause). Under the ratified Route T
fold-in, the depth-(h-1) cascade tier is charged as a NAMED tier of the
band column (`xr_graded_tangent_band_charge`); the cascade forcing stays
citable as structure.

## Attack surface

specialize two_slope_intersection to cores >= k+t-1; the cascade step is one line (pencil evaluation off-core); write-up is a small packet

## Falsifier

a toy multiplicity-2 pair with core >= A-1 and no pencil (E27's machinery searches this directly; zero found in 2000 constructed + 10^5 organic)

## Ledger (migrated notes)

PROVED (W1, PR #10, 70/70 replayed): the forcing lemma at core >= k+t-1 with the cascade, scale-free, E27-calibrated. Face 4 rung 1 closed.
