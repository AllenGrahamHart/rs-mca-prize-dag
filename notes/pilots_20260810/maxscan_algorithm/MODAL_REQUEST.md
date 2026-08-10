# DRAFT compute request — exact n=32, t=1, δ=1 whole-word-space maxscan

Drafted by pilot `maxscan_algorithm` (round 28) for the coordinator to file
in `notes/compute_requests`. **Not filed, not run by me. NO MODAL was
invoked from this session.**

## Status: OPTIONAL, and much cheaper than the round-27 pricing implied

Round 27 named this run "Modal-class, out of stdlib reach" at C(32,15) ≈
5.7·10⁸ subset-evaluations *per word class*. Two things changed in round 28:

1. **The RAM wall is gone and the α=0 slice is already done in stdlib.**
   `scratch/ms_strat.py` (this dir) computes the exact α=0 maximum over the
   entire n=32 subset space in ≈4 minutes on one core inside
   `tools/ramguard local`, using ~130 MB. Answer: **MAXSCAN_0(32) = 1988**
   at q=30000001 and q=30000193 (identical), = **1974 exact char-0** plus a
   measured 14 of mod-q collision background.
2. **The α=0 slice is the global argmax at n=8 and n=16 (banked, two
   fields), and the char-0 answer 1974 is 3.26× BELOW the slack-0 plateau
   6435.** So the full scan is now *confirmation of an argmax location*, not
   the discovery run. The scaling verdict (COLLAPSE) does not wait on it.

File this only if the coordinator wants the argmax-at-α=0 law upgraded from
"three scales, two fields, empirical" to "proved at n=32 by exhaustion".

## What the run computes

MAXSCAN(32,q) = max over (W1,W2) ∈ F_q² of
F_SUBSET = #{B ⊂ μ₃₂, |B|=15 : e2(B) − W1·e1(B) + W2 = 0}, exactly, at two
independent fields q ≡ 1 (mod 32).

## Design — two-stage sieve (this is what makes it cheap)

**Precompute (once per field, per worker).** E1[i] = −e1(B_i), E2[i] = e2(B_i)
for all N = 565,722,720 subsets, as two int32 arrays (4.5 GB). Generate them
with the stratified antipodal recursion of `ms_strat.py` (S/σ/T), not
`itertools.combinations` — it is the only form that streams in bounded RAM.
Persist to a single `.npy` pair in a Modal volume so shards mmap it read-only.

**Field choice.** q ≈ 3·10⁷ (μ = N/q ≈ 18.9). Registered pair:
q₁ = 30000001, q₂ = 30000193 — the same two fields as the stdlib α=0 run, so
the shard results are directly comparable to the banked 1988.

**Stage 1 — subsampled sieve.** Only rotation-orbit representatives of
W1 are needed: (α,β) ↦ (ζα, ζ²β) is a free action on α ≠ 0, so
(q−1)/32 ≈ 937,500 representatives plus α = 0. For each representative
evaluate the maxscan on a fixed pseudo-random 1/64 subsample of the N
subsets: `V = (E2s + a*E1s) % q; bincount(V, minlength=q).max()`. A line of
true weight W has sample weight ~Binomial(W, 1/64); sieve threshold τ = 6
(a W = 800 line gives mean 12.5, P(miss) < 2·10⁻²; a background line has
mean 0.29). **Registered sieve floor: the sieve is only claimed to detect
lines of weight ≥ 800; the certified statement is therefore
"MAXSCAN(32) = max(1988, anything the sieve found)" together with
"no line of weight ≥ 800 exists off the surviving α list".**

Cost: 937,500 × 5.66e8/64 = 8.3·10¹² element-ops. At numpy throughput
2–8·10⁸ ops/core-s this is **3–12 core-hours per field**.

**Stage 2 — exact confirmation.** Re-evaluate every surviving α at full
resolution (5.66·10⁸ ops each). Expected survivors: O(10³) (at n=16 only 577
of 10177 α reached even the ≥20 level, and the levels above 26 occupied 3
rotation orbits). Cost ≈ 10³ × 5.66e8 = 5.7·10¹¹ ops ≈ **0.2–0.8
core-hours per field**.

## Sharding and fail-closed manifest

- Shard on contiguous blocks of α-orbit representatives, 4096 reps per shard
  → ~229 shards/field. Each shard mmaps the shared E1/E2 volume; no shard
  writes shared state.
- Each shard emits `shard_<field>_<lo>_<hi>.json`:
  `{q, g, lo, hi, n_reps, stage1_threshold, survivors:[[alpha, sample_max]],
    stage2:[[alpha, exact_max, argmax_W2]], sha256_of_E1E2, elapsed_s,
    code_sha256}`.
- **Fail-closed manifest**: the driver writes `MANIFEST.json` listing every
  expected shard id up front; the aggregator refuses to emit a maximum
  unless every listed shard is present, its `sha256_of_E1E2` matches the
  driver's, and its `code_sha256` matches. Any missing/mismatched shard ⇒
  hard error, no partial verdict. Same rule as the K3 campaign apps.
- **Cross-check gates (must pass or the run is void):**
  1. the α = 0 shard must reproduce **1988** at q₁ and q₂;
  2. the α = −x, x ∈ μ₃₂ orbit must reproduce **1697** at W2 = 0 (q₁);
  3. the same app run at n=16, q=10177/10193 must reproduce the banked
     per-W1 max histograms byte-for-byte (both are in
     `notes/pilots_20260809/nonpoly_flank_census/data/`), and
  4. the shard total Σ over all cells must equal N = 565,722,720 exactly.

## Expected cost

| item | per field | both fields |
|---|---|---|
| E1/E2 precompute + persist | ~1 core-h, 4.5 GB volume | 2 core-h |
| stage 1 sieve | 3–12 core-h | 6–24 core-h |
| stage 2 exact | 0.2–0.8 core-h | 0.4–1.6 core-h |
| **total** | **4–14 core-h** | **~8–28 core-h** |

At commodity Modal CPU pricing this is **well under $5**, on 64–128 GB
memory instances (the 4.5 GB arrays plus a q-length int32 bincount buffer,
120 MB, per worker). Wall time with 64 concurrent workers: **under 30
minutes.**

## Registered outcome thresholds (before any run)

- **Confirms**: MAXSCAN(32) = 1988 (i.e. no α ≠ 0 beats α = 0) ⇒ the
  argmax-at-α=0 law holds at three scales by exhaustion, and
  RATIO(32) = 1988/6435 = 0.309 is the exact whole-word-space value.
- **Refutes**: some α ≠ 0 gives > 1988. Then report that α, identify it as a
  cyclotomic integer (the n=16 second tier is exactly μ₁₆ at W2 = 0), and
  the COLLAPSE verdict must be recomputed against the new value. Note that
  even a 3× surprise (≈6000) still leaves RATIO < 1.
- **Void**: any cross-check gate fails.
