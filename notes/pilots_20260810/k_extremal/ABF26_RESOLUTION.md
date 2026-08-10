# ABF26 proviso — RESOLVED NEGATIVE (coordinator, 2026-08-10)

The round-29 k_extremal pilot's one honest unresolved — whether the ABF26
"sufficiently large |F|" proviso excludes small rows and flips the HOLE to
PINNED — is settled from the primary source, without an outward question.

## Source

abf26 = Gal Arnon, Dan Boneh, Giacomo Fenzi, **"Open Problems in List
Decoding and Correlated Agreement"**, dated 2026-04-08 (the Proximity
Prize survey, https://proximityprize.org/). Read as the vendored
`rs-mca/open-proximity.pdf`, sha256

```text
e543ec6a4f3312b4383000e72e5aa23862e79cc9770ce21db2c48db679581de3
```

Version note: `official_row_primes_reframe.json` pins sha256
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5` — a
different version of the same paper. All four pinned fragments were
re-verified VERBATIM on page 5 of the version read (the grand MCA
challenge box, the grand list decoding challenge box, and the paragraph
between them). The rules_freeze custody chain should eventually re-pin
against one declared version; flagged, not blocking.

## The decisive text (page 5, verbatim)

The grand MCA challenge box:

> We are given a Reed–Solomon code C := RS[F, L, k] defined over some
> smooth evaluation domain L ⊆ F. The code has constant rate, and in
> particular the rate ρ(C) := k/|L| is one of {1/2, 1/4, 1/8, 1/16}.
> For a given ε\*, say ε\* = 2^-128, determine the largest δ\*_C ∈ [0,1]
> such that ε_mca(C, δ\*_C) ≤ ε\*, **assuming |F| is sufficiently large
> so that such a δ\*_C exists.**

The paragraph immediately below:

> Resolving the challenge for a code C and ε\* requires specifying a
> δ\*_C ∈ [0,1] along with a proof that for all δ > δ\*_C we have
> ε_mca(C, δ) > ε\*. Ideally we could determine this δ\*_C for every
> Reed–Solomon code RS[F, L, k], namely, **for every choice of F, L,
> and k. However, we are mostly interested in determining δ\*_C when
> L ⊆ F is a smooth domain, k ≤ 2^40, and |F| < 2^256.**

The grand list decoding challenge box carries the identical proviso
("assuming |F| is sufficiently large so that such a δ\*_C exists").

## The ruling

1. **The proviso conditions on |F|, not on k or n.** Its stated purpose
   is existence of δ\*_C: ε_mca has 1/|F| scaling (Table 1: even at
   δ = 0, ε_mca = 2/|F|), so ε\* = 2^-128 demands a large field. It is
   a well-definedness clause about the FIELD, silent about the ROW.
2. **Small rows are not excluded — they are easier.** At fixed |F|, a
   smaller n only shrinks the n-dependent error terms, so the clause
   binds more weakly at small rows. Nothing in the text reads as "only
   the largest row per rate counts."
3. **k ≤ 2^40 is a cap over a family of interest, not a pin** — stated
   in the challenge's own words ("for every choice of F, L, and k...
   mostly interested in... k ≤ 2^40"). This confirms the round-29
   k_extremal reading against the primary source.

**Consequence: the HOLE stands.** The rate-half grand-challenge family
is the 41 row sizes n = 2^s, k = 2^(s-1), s = 1..41, and the lane's
s = 41-only coverage is a real gap for full grand-challenge resolution.
POSE 3 (the per-s four-band family re-pose) is adopted in consequence —
BAND_LANE_DEFINITIONS items 14-15. No Przemek/rules question is needed;
the pending "rules-citation question" is retired.

## Collateral ruling (FLAG E)

The same box adjudicates FLAG E: rate ρ ∈ {1/2, 1/4, 1/8, 1/16} under
k ≤ 2^40 makes the cap-saturating rows k = 2^40, n = 2^40/ρ ∈
{2^41..2^44} the maximal admissible rows per rate — Convention B.
Recorded in BAND_LANE_DEFINITIONS item 13.
