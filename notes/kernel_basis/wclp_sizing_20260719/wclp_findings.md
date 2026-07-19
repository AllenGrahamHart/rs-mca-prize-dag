# wclp_findings.md — sizing-pilot findings (2026-07-19)

Fresh-context sizing pilot; READ-ONLY on all repos; all artifacts under
scratchpad prefix `wclp_`. Modal apps: `ap-zwfbJiBpoOLyEor2I8iam3` (Pilot A),
`ap-oHfxs9fC8S4EJLsk7McTpn` (Pilot B). Total pilot spend: cents-scale
(measured function time ~0.35 CPU-h combined, see report).

## Where the (1,5) machinery actually lives

The streaming/checkpointed terminal weight-five sweep is NOT in the v5/v6
worktrees' experiments/ — it lives in the **v4 worktree**:
`/home/u2470931/smooth-read-solomin/prize-codex-resolution-v4-20260713/experiments/prize_resolution/`
files `dli_wcl_weight5_affine_representatives_modal.py`,
`dli_wcl_weight5_recursive_norm_{pilot,full,tail}_modal.py`. The named commits
("Stage weight-five hard-tail spending" 26beb2d7, "Stream weight-five
hard-tail factors" f2a8060b, "Checkpoint terminal weight-five norm sweep"
982cf29d, etc.) exist in the shared object store but are on NO branch
(`git branch --contains` is empty — they are dangling/unmerged; the v4
worktree carries the files as working-tree state, with the 2KB prefix-test
result `dli_wcl_weight5_recursive_norm_full_result.json` untracked).
If the worktree is ever cleaned, the only durable copies are the loose
objects. Worth vendoring to master before production.

## Pilot A findings (weight-5 (1,5) sweep)

1. **The checkpoint is 8,300x further along than the record says.** The
   wave-10 audit note (and the local 2KB prefix result) record 128 rows
   done; the volume (`rs-mca-dli-wcl-weight5-affine-classes-v1`,
   run `weight5-recursive-norm-full-v2/batch_summaries`) actually holds
   **16,667 COMPLETE, schema/sha-valid batch checkpoints** = **1,066,688
   rows (46.44%) already paid**, indices 0..16728 with 39 gaps (62 missing
   batches in-range). Rows remaining: **1,230,232** (19,223 of 35,890
   batches). All 16,667 checkpoints validate against the pinned
   representative sha `9ac0ca65...`; 104 unresolved FACTOR_TIMEOUT_60S rows
   (0.0097% of covered); max_v2(p-1) observed so far = 30 < 41; zero
   high-gate cases; max norm 284 bits; max certified prime factor 262 bits.
   The sweep evidently kept running after the last local result write
   (Jul 17 16:52) and its progress was never re-aggregated. I downloaded all
   16,667 batch JSONs (~25 MB, read-only) to
   scratchpad/wclp_a_batches/batch_summaries/ and analyzed them locally
   (wclp_a_prod_analyze.py, wclp_a_prod_summary.json).

1b. **Production-measured rate over the covered 1.07M rows**: batch wall
   (cpu=2 worker, 2 gp threads, 64 rows) sum 447,354 s = 124.3 h; mean
   26.84 s, med 22.70 s, p90 45.47 s, p99 95.57 s, max 297.75 s. Per-row
   batch wall 0.4194 s (0.839 reserved-core-s at the 2-core shape). The
   head decile (batches 0..1665) is the heavy region (mean 49.0 s/batch,
   56/104 of the timeouts); deciles 1-9 are stable at 22-27 s/batch with a
   mild downward trend, so the remaining region extrapolates at ~21-23
   s/batch.

1c. **Checkpoint-scan hazard (also a production risk)**: my v1 pilot's
   volume-wide scan died at the 280s function ceiling because parsing 16.7k
   small JSONs over the volume FUSE mount is slow (~1-2 min per 10k files,
   variable). The production `checkpoint_progress()` (300s) will NOT survive
   a full 35,890-part tree, and `aggregate_checkpoints` (900s) is
   borderline — the final aggregation pass should be re-sharded (e.g.
   group-merge like the prime shards) or given chunked reads before the
   full run finishes.

2. **Resumption is clean by design**: each 64-row batch writes an atomic
   (tmp+rename) self-validating checkpoint keyed by
   (schema, run_id, representative sha, batch_index, bounds, rows, COMPLETE)
   plus a prime shard file, and `process_batch` returns the cached checkpoint
   on re-dispatch (`cache_hit`). Re-running `main()` with the same RUN_ID
   resumes exactly; the prefix rows will be cache hits. Aggregation re-reads
   all batch files and fails closed on any gap/mismatch. One operational
   hazard: `main()` maps ALL 35,890 bounds every invocation, so each resume
   pass re-schedules completed batches (cheap cache-hit containers, but
   nonzero overhead ~35,890 container-invocations/pass).

3. **Timing tranche (v2, complete: 32 shards, 512 rows, 0 errors, 0
   timeouts, 0 skips)**: uniform-over-remaining mean 0.698 s/row (med 0.158,
   p90 1.87, p95 3.54, p99 6.51, max 11.3); frontier-contiguous mean 0.714
   (max 20.4); max_v2 seen 21. Per-row cost is factor-dominated and
   heavy-tailed (recursive norm ~0.3 ms/row; PARI `factor()` of the
   200-284-bit norms is the entire cost). The head of the class file
   (batches 0..~1700, already covered) is the heavy region — mean 49
   s/batch and most timeouts — because the file is sorted by packed key and
   early rows have clustered small exponents; the remaining region is
   stable at ~21-23 s/batch equivalents. Uniform-over-remaining is the
   right estimator and it agrees with production's own batch records to
   within ~8%.

4. **Worker-shape note**: the production easy pass reserves cpu=2 with a
   2-thread gp pool per 64-row batch; gp and flint are single-threaded, so
   the CPU-second cost per row equals the single-core measurement and the
   2-core reservation roughly doubles the reservation-billed cost per
   CPU-second of useful work. A cpu=1, one-gp-at-a-time worker with 128-row
   batches would be ~2x cheaper on reservation billing at identical total
   CPU work (Modal bills reserved cores; flag: verify billing model).

5. **Hard-tail second stage**: 60s-timeout rows defer to the tail script
   (300s/norm, distinct-norm dedup). Production-measured timeout fraction:
   104/1,066,688 = 0.0097% (0/512 in my remaining-region tranche —
   consistent, expected 0.05). Extrapolated total tail ≈ 223 rows
   (norm bits med ~246, max 279). Every timeout row costs 60 wasted
   easy-pass seconds plus up to 300 tail seconds, and rows still unresolved
   after 300s currently have NO further stage (the tail result would come
   back PARTIAL — ECM/mpqs budget beyond gp's default `factor` is the open
   risk item; gp `factor` on 240-280-bit semiprime-ish cofactors can exceed
   300s).

## Pilot B findings (weight-7 (2,7) census)

6. **Exact analogous orbit count: 94,652,815** (weight-7 router: selected
   quadruple {1,x,y,z} normalized, complementary triple with free product
   d = zeta^c; quotient by odd Galois dilation x rebasing exactly as the
   audited (2,6) census). Derivation validated by reproducing the audited
   numbers EXACTLY from the same model: 404,740 (2,6) candidate orbits,
   1,514 pair orbits, 521,220 legal pairs (script wclp_b_count.py; Burnside
   after a translation-conjugacy collapse; exact integers; runs in ~2s under
   ramguard tiny). Companion exact counts: 176,867,320 legal normalized
   triples; 401,712 triple dilation-orbits; 411,353,088 router
   presentations. Blow-up vs (2,6): **233.9x in orbit count**.

7. **Per-orbit cost blow-up is modest (1.6-1.9x)**: measured 1.434 s/orbit
   (cpu=1) vs 0.881 s/orbit for (2,6) candidates on the SAME containers
   (audited production (2,6) rate was 0.770 s/row, so containers/pipeline
   calibrate to ~1.14; calibrated w7 production-equivalent ~1.25 s/orbit).
   Phase split (w7): recurrences 0.198 s, Norm(F) 0.046 s, Norm(G) 0.096 s,
   Norm(u) ~1 ms, **gcd+saturation 1.095 s (76% of row cost)**. The
   saturation is python `math.gcd` on 632k/1,140k-bit norms — switching to
   GMP/FLINT subquadratic gcd (`flint.fmpz.gcd`) is the obvious ~2-3x
   whole-row optimization lever for BOTH (2,7) and any (2,6)-style rerun.

8. **Norm sizes**: Norm(F) ~632k bits, Norm(G) ~1,140k bits (vs (2,6)
   473k/842k — x1.34); raw gcd ~164k bits (vs 125k). BUT saturated gcds are
   dramatically SMALLER than weight-6's (sample deciles 1/45/83/112/147/199
   bits, max 1,625 bits over 160 orbits, vs (2,6) sample median ~3,073 bits
   and production max 16,986 bits). 148/160 sampled orbits had a nontrivial
   saturated gcd; 0/160 hit the zero branch. Sampled factoring of saturated
   gcds: 60/60 complete, ~0.015 s/value (sample biased toward the small end:
   6 smallest distinct values per shard) — the factor/Pocklington stages
   look CHEAPER per orbit than (2,6), not more expensive. No 16,986-bit-style
   gcd blow-up observed.

9. **SOUNDNESS GAP in the ported saturation (load-bearing, certificate
   design, not sizing)**: the (2,6) certificate removes gcd factors shared
   with Norm(u) because u = 1+x+y = a weight-THREE single-equation relation,
   excluded by the paid `dli_wcl_ell2_weight3_ambient_exclusion`. For
   weight 7, u = 1+x+y+z is a weight-FOUR single-equation sum at order 1024,
   and NO paid single-equation weight-4 exclusion exists (the weight-4
   Newton exclusion consumes BOTH moment equations). Since saturation is
   doing heavy lifting (164k-bit raw gcd -> ~100-bit saturated), the (2,7)
   certificate must either (a) also factor Norm(u) (~318 bits, cheap) and
   include its prime roots in the v_2 gate, or (b) first prove a
   single-equation reduced weight-4 exclusion. Route (a) fits the same cost
   envelope.

10. **Zero branch is vacuous for weight 7**: a candidate with F = G = 0
    reconstructs a 7-element multiset of 1024th roots summing to zero; the
    power-of-two vanishing-sum lemma partitions any such zero sum into
    antipodal pairs, impossible at odd cardinality 7. So (2,7) has no
    analogue of the 510 structural cases — every orbit must die by norms
    (consistent with 0/160 zero rows sampled).

11. **Census generation needs a redesign**: the (2,6) generator holds all
    legal pairs / orbit dicts in one worker's RAM and enumerates 1,514x1024
    canonical keys in 300 s. The (2,7) analogue is 401,712 triple orbits x
    1024 = 411M canonical-key evaluations and ~94.65M orbit set — far beyond
    one 4 GiB/300 s worker (est. tens of GiB and ~100+ CPU-h if done the
    same way). Needs a sharded canonicalization (the Burnside count above
    pre-pins the expected total, which makes a sharded census fail-closed
    auditable). Candidate file: 94,652,815 x 8 bytes (4x uint16) = 757 MB.

## Cross-cutting

12. The stock `tools/modal_run_script.py` image lacks python-flint and
    pari-gp, so both pilots ran as standalone law-shaped Modal apps
    (cpu=1, <=280 s function timeout, no volume writes) with the production
    image chain `debian_slim().pip_install("python-flint").apt_install("pari-gp")`
    — byte-identical to the production apps' image, so measurements are
    production-parity and the image build was a cache hit.
13. Dollar rates are ASSUMPTIONS (Modal list prices from memory, mid-2025:
    $0.135/CPU-core-h + $0.024/GiB-h reserved): VERIFY against
    modal.com/pricing before authorizing either production run.
14. Pilot execution record: A v1 (ap-zwfbJiBpoOLyEor2I8iam3) aborted when
    its checkpoint-scan function hit the 280s ceiling (see #1c) — Modal
    raises FunctionTimeoutError from `.remote()` and (observed) it can also
    surface through `.map(return_exceptions=True)`, so production drivers
    should wrap map iteration. A v2 rerun completed clean (32 shards,
    512 rows). B completed clean first try (10 shards, 160+10 rows,
    60 factor samples, worker-side sum 240.6 s). Total measured pilot
    function time ~0.4-0.6 CPU-h => ~$0.10-0.15 at the assumed rates
    (cents-scale, as required). Note: the B factor-time sample is biased
    toward the SMALL end of the saturated-gcd distribution (each shard
    factored its 6 smallest distinct values); the max sampled saturated gcd
    (1,625 bits) went unfactored — still far below the (2,6) max
    (16,986 bits) that production factored routinely in-batch.
