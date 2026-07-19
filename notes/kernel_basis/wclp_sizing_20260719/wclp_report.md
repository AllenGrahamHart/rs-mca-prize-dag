# wclp_report.md — WCL production-run quotes (sizing pilots, 2026-07-19)

Mission: ACCURATE cost/time quotes for (A) the (1,5) streaming terminal
weight-five norm sweep and (B) the (2,7) recursive-norm census, from measured
cents-scale pilots. No production work was run; no repo or volume writes.

Pilots: Modal apps ap-zwfbJiBpoOLyEor2I8iam3 (A v1, aborted on a
checkpoint-scan timeout), wclp-a-...-v2 (A v2, complete),
ap-oHfxs9fC8S4EJLsk7McTpn (B, complete). Scripts wclp_a_tranche_modal_v2.py,
wclp_b_sample_modal.py, wclp_b_count.py, wclp_a_prod_analyze.py (this
directory); raw results wclp_a_tranche_result.json, wclp_b_sample_result.json,
wclp_a_prod_summary.json + wclp_a_batches/ (downloaded production
checkpoints). Total pilot spend: ~0.4-0.6 CPU-h of Modal function time
(≈ $0.10-0.15 at the assumed rates) — cents-scale.

## PRICING ASSUMPTION (flagged)

All dollar figures ASSUME Modal on-demand reserved-resource rates of
**$0.135 per CPU-core-hour + $0.024 per GiB-hour** (list prices as
remembered, mid-2025 — VERIFY at modal.com/pricing before authorizing).
"1c2G" worker = 1 core + 2 GiB ($0.183/h); "2c4G" = the production scripts'
2 core + 4 GiB shape ($0.366/h), which pays ~2x per useful CPU-second because
flint/gp work is single-threaded (2 gp threads only during the factor phase).

---

## THE QUOTE TABLE

### Job A — slot (1,5): terminal weight-five norm sweep, REMAINING work

| item | value |
|---|---|
| total size | 2,296,920 affine classes. **46.44% ALREADY DONE**: the volume holds 16,667 valid 64-row batch checkpoints = 1,066,688 rows (the audit record said 128 — see findings #1). **Remaining: 1,230,232 rows = 19,223 of 35,890 batches** (incl. 62 gap batches) |
| measured rate | **0.698 s/row** single-core mean (uniform over the remaining region, n=384, cpu=1, production-parity flint+gp 60s cap); frontier-contiguous control 0.714 s/row (n=128). Cross-checks: prior 2048-row uniform pilot 0.644 s/row; production's own 16,667 batch records: 0.4194 s wall/row on 2c/2-thread workers (= 0.84 reserved-core-s/row, ~80% util) |
| distribution (per row, uniform) | med 0.158 / p90 1.87 / p95 3.54 / p99 6.51 / max 11.3 s; contiguous max 20.4 s; **0/512 tranche timeouts**; production timeout rate 104/1,066,688 = **0.0097%** |
| CPU total (remaining) | easy pass ≈ 1,230,232 x 0.644-0.698 s = **220-239 CPU-h**; hard-tail stage ≈ ~120 more 60s-timeout rows expected (+104 banked) x ≤300 s ≈ 5-19 CPU-h; resume/aggregation overhead ~10-20 CPU-h => **~250-280 CPU-h** |
| wall time (1c workers, 128-row shards) | 24 workers: **10.4-11.7 h**; 64: **3.9-4.4 h**; 128: **2.0-2.2 h**. (Production 2c/2-thread shape: roughly half these walls per container, same dollars) |
| dollars (remaining) | **$45-60** at the stated assumption (1c2G 250-280 h x $0.183, or equivalently ~118-124 wall-h x $0.366 at 2c4G). Already spent on the covered 46.44%: ≈ $45 equivalent |
| checkpoint/resume | **CLEAN**: atomic per-64-row self-validating checkpoints (schema+run_id+sha+bounds), cache-hit resume, fail-closed aggregation. Two repairs needed before the finish: (i) `checkpoint_progress`/`aggregate_checkpoints` parse every part JSON over FUSE in one 300/900s function — will not survive 35,890 parts; re-shard the final aggregation. (ii) ~223 tail rows may include some unfactorable-in-300s norms (240-280-bit); plan an ECM/extended stage or accept a small PARTIAL tail loop |
| recommended production tranche | one resume pass at **64 containers (~4 h wall)**; or auditability tranches of 2,000-4,000 batches (~1-2 h each). Keep BATCH_SIZE=64; run the tail script after; then the re-sharded aggregation + prime vocabulary + Pocklington stage |

### Job B — slot (2,7): recursive-norm census (analogue of the audited (2,6) certificate)

| item | value |
|---|---|
| total size | **94,652,815 candidate orbits** (EXACT; Burnside count, validated by reproducing the audited (2,6) numbers 404,740 / 1,514 / 521,220 exactly from the same model — wclp_b_count.py, runs under ramguard tiny). **233.9x the (2,6) census.** Companions: 176,867,320 legal normalized triples; 401,712 triple dilation-orbits; 411,353,088 router presentations; candidate file ≈ 757 MB |
| measured rate | **1.434 s/orbit** raw (cpu=1, n=160, full pipeline: 4-term u, cleared cubic, 10 doublings, Norm(F), Norm(G), Norm(u), gcd+saturation); same-container (2,6) control 0.881 s vs audited (2,6) production 0.770 s/row => calibrated **1.25 s/orbit** production-equivalent. Phase split: recurrences 0.198 s, Norm(F) 0.046 s, Norm(G) 0.096 s, **gcd+saturate 1.095 s (76%)** |
| distribution | tight: med 1.463 / p90 1.537 / max 1.789 s/orbit; sampled saturated-gcd factoring ~0.015 s/value (60/60 complete, no timeouts); 148/160 nontrivial saturated gcds; 0/160 zero-branch |
| CPU total | 94,652,815 x 1.25-1.434 s = **33,000-37,700 CPU-h** (+ factor stage, sharded census generation, Pocklington graph ≈ +2-4%) => quote **33,000-39,000 CPU-h**. Optimization lever: the 76% saturate phase is python `math.gcd` on 632k/1,140k-bit ints — GMP/FLINT gcd should cut the row to ~0.40-0.55 s => est. **~10,500-14,500 CPU-h** (unmeasured estimate) |
| wall time | 24 workers: 1,375-1,625 h (**57-68 days**); 64: 516-609 h (22-25 days); 128: 258-305 h (**11-13 days**); 500 (production max_containers): 66-78 h (2.8-3.3 days) |
| dollars | as measured: 1c2G **$6,000-$7,100**; production 2c4G shape $12,100-$14,300. With the gcd optimization: **~$1,900-$5,300**. NOT a sub-$1 job under any configuration |
| structural warnings | (i) 233.9x orbit blow-up dominates everything; (ii) norms grow only x1.34 (F 632k / G 1,140k bits) and saturated gcds are SMALLER than (2,6)'s (sample max 1,625 bits vs 16,986) — factor/Pocklington stages get cheaper, no gcd blow-up; (iii) zero branch VACUOUS (odd cardinality 7 + power-of-two lemma); (iv) census generation needs a sharded redesign (411M canonicalizations won't fit the (2,6) single-worker pattern); (v) **Norm(u)-saturation soundness gap**: u = 1+x+y+z is a weight-4 single-equation sum — no paid single-equation weight-4 exclusion exists at order 1024; fix = factor Norm(u) (~318 bits, cheap) into the v_2 gate, or prove the exclusion first. Details: wclp_findings.md #6-#11 |

---

## RECOMMENDED PRODUCTION PLAN

1. **Job A — proceed now.** Vendor the v4-worktree scripts to master first
   (the enabling commits are on NO branch — dangling objects; findings
   "where the machinery lives"). Then: one resume pass of
   `dli_wcl_weight5_recursive_norm_full_modal.py` at 64 containers (~4 h
   wall, ~$50), tail pass, then a RE-SHARDED aggregation (the current
   single-function aggregate will time out on 35,890 parts), prime
   vocabulary + Pocklington certification, and the (2,5)/(2,6)-shaped
   certificate audit. Budget envelope incl. contingency: **<$100**.
2. **Job B — do not launch as-is.** Before any full run: (a) swap the
   saturation gcd to GMP/FLINT and re-pilot (expected ~2.5-3x, one
   cents-scale rerun of wclp_b_sample_modal.py); (b) design the sharded
   census generator fail-closed against the exact pre-pinned count
   94,652,815; (c) close the Norm(u) soundness gap (cheap route: factor
   Norm(u) into the gate); (d) seek further quotienting or a cheap
   pre-filter that kills most orbits before the full recurrence+gcd —
   every 2x there is ~$1-3k saved. Re-quote after (a); authorize an
   explicit multi-hundred-dollar-to-few-$k budget only then.

## GO / NO-GO

- **Job A: GO.** ~250-280 CPU-h remaining, $45-60 at assumed rates, 2-12 h
  wall at 24-128 workers, clean resumption verified, 46.44% already banked.
- **Job B: NO-GO at current machinery.** 33,000-39,000 CPU-h ($6k-$14k,
  weeks of wall at moderate fleets) for the direct analogue; even the
  optimized estimate (~$2k-$5k) is 3-4 orders above the standing sub-$1
  policy. Needs the optimization + soundness fixes above and an explicit
  budget decision, or better algebra (further quotienting / obstruction
  pre-filter) before it becomes launchable.
