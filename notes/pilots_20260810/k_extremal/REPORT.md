# REPORT.md — k_extremal (round 29) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ae70406e7acfa145e, 2026-08-10. Pilot: Opus. No edits.

Audit complete. Here is my report of record.

---

# k_extremal (round 29) — REPORT

## VERDICT: **HOLE**

The grand-challenge row family at rate 1/2 is **41 row sizes**, and the entire rate-half lane is posed at **one** of them. `k &lt;= 2^40` is an upper cap on a family, not a pin (`background/nodes/descriptor/proof.md:3-8`, PROVED and machine-checked); rate exactly 1/2 with a 2-power domain forces `n = 2^s, k = 2^(s-1)`, so the family is `s = 1..41`. The lane is posed at `s = 41` (`critical/nodes/rate_half_band_closure/statement.md:66`), **no node establishes `k = 2^40` as extremal, and no node reduces smaller-`s` rate-half rows to it.**

### Misses first

- I did not read all 239 critical + 1908 background statements. "Nothing covers it" rests on the targeted greps listed under D2, not exhaustion.
- **The one thing that could flip this to PINNED:** whether ABF26's proviso `assuming |F| is sufficiently large` (`background/nodes/official_row_primes_pinning/proof.md:27`) is intended to exclude small rows. I could not settle it from in-repo text — `abf26.pdf` and the `rules_freeze.json` certificate are **not vendored in this tree** (confirmed by find; consistent with `rules_freeze/proof.md:14`). I relied on `official_row_primes_reframe.json`. This needs a rules-citation pass I was not equipped to run.
- POSE 1's lower bound (`L_1(k-1) &gt;= q`) is my own 3-line sketch, not refereed.
- I audited the MCA side harder than the list mirror.

---

## D1 — THE QUANTIFIER MAP

**Anchors (escape test 1, verbatim).** `critical/nodes/rules_freeze/statement.md:9`: "smooth domain = coset of a power-of-2-order subgroup; **k &lt;= 2^40**; |F| &lt; 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16}… on any residual ambiguity the campaign plans against the stricter reading." `background/nodes/official_row_primes_pinning/proof.md:28`: "`for every choice of F, L, and k`".

**The family is a CAP OVER A FAMILY, decisively.** `background/nodes/descriptor/proof.md:3-6`: "Fix an admissible tuple `(p,e,s,rho)`. Put `q=p^e`, `n=2^s`, and `k=rho*n`… The descriptor checks `q&lt;2^256`, `k&lt;=2^40`, and `n | q-1`." `s` is free. `background/nodes/ww_row_envelope_clause/specification_frontier.md:9`: "admissible rows are parameterized by `(p,e,s,rho)`".

| consumer | file:line | k-range its claim covers |
| --- | --- | --- |
| `mca_grand` | `node.json` statement / `statement.md:9` | "For each admissible C" — **all s ≤ 41**; the RATE SCOPE clause makes the rate-1/2 instance conditional on `rate_half_band_closure` |
| `list_grand` | `statement.md:9` | "For each admissible C and constant m" — **all s ≤ 41** |
| `adjacency_closing` | `statement.md:9` | "For each admissible row" — **all s ≤ 41** |
| `list_adjacency_closing` | `statement.md:9` | "For each admissible row" — **all s ≤ 41** |
| `mca_safe` / `mca_unsafe` | `statement.md:9` both | no row quantifier at all; inherit the parent's |
| `s0_zero_open` | `statement.md:9` | axis discipline; row-agnostic |
| `mixed_radix_frontier` | `statement.md:9,21` | **supplies the pin that makes the family discrete**: "'smooth' … is 2-smooth (power-of-2 order)" |
| `rate_half_band_closure` | `statement.md:66` | **"Let n=2^41, k=2^40"** — s = 41 only |
| `rate_half_band_crossing_location` | `statement.md:11` | **"At every admissible row with n = 2^41, k = 2^40"** — universal in q, pinned in (n,k) |
| `rate_half_list_adjacent_crossing` | `statement.md:5` / sections `00:7` vs `00:25-29` | claims "**every** admissible official rate-half row"; supplies machinery "**At the prize-max razor row** n=2^41, k=2^40" |
| `unsafe_crossing_family_instantiation` | `statement.md:8` | "For every admissible row" — correctly posed, status TARGET |

**Consumers' consumers (the round-28 lesson, discharged).** `mca_grand` is a root: its `node.json` `requires` list is `{s0_zero_open, mca_safe, mca_unsafe, mixed_radix_frontier, adjacency_closing}` and nothing requires it. Nothing above re-pins the family. The chain terminates with the universal quantifier intact.

**Escape test 2 (worked example, verified).** The repo's own regression fixture is a **small rate-half row**: `background/nodes/descriptor/proof.md:29` — "reconstructs the pinned `F_(17^32)` row and obtains `n=512`, `k=256`, and `B*=6`." I verified it independently: `q = 17^32` is 131 bits (`&lt; 2^256`), `512 | q-1` with `v_2(q-1) = 9` exactly, `k = 256 &lt;= 2^40`, rate exactly 1/2, domain order `2^9`. **Fully admissible, and `k = 2^8`.** It is the "506/507 pinned row" of `staircase/statement.md:9` and `adjacency_closing/statement.md:13`. The campaign has a *proved crossing* at a small rate-half row — banked as a calibration **exhibit**, which by its own rule (`official_row_primes_reframe.json:25`) does not discharge the universal quantifier.

---

## D2 — THE COVERAGE AUDIT

**(a) Monotonicity — ABSENT.** Greps for `monoton` across all statements return only monotonicity *in the agreement index* (`crossing_localization:13` "first-crossing monotonicity packet"), *in dual weight*, *in deletion*. Zero hits for monotonicity in `k` or `n`. Greps for `smaller k` / `smaller row` / `extremal row` / `hardest row` / `worst row` return nothing on the crossing claim.

**(b) Clean-rate corridor — does not reach.** No corridor node quantifies over row size.

**(c) Admissibility exclusion — REFUTED.** The descriptor's predicate has no lower bound on `s`; and the repo *actively uses* small rows as admissible (`ww_parametric_row_scope_router/proof.md:25`: descriptor at `n=8192, k=2048`; the `F_(17^32)` fixture at `n=512`).

**(d) Row-transport theorem — ABSENT.** Every "transports" hit is across arity `m` (`list_large_m_scope_closure`) or across quotient rows within a fixed row. No row-size transport exists.

**What genuinely DOES cover row sizes (partial, and it matters):**
- `critical/nodes/census_bounded_scales/statement.md:9` (PROVED): "in an ABSOLUTE window `N' in [~120, ~400]` — **independent of n and k up to 2^40**. The census is **n-uniform**." *Caveat I add:* the deciding scale must divide `n`, so this window is **empty for s ≤ 6** and singleton at `s = 7` — the n-uniformity silently floors around `s ≈ 7-8`.
- `background/nodes/list_interleaved_support_census/statement.md:6-40` (PROVED): fully symbolic in `(n,k,q,m)`; gives a row-uniform **safe anchor** (least `a` with `binom(n,a) &lt;= B*`) and a row-uniform **unsafe anchor** at `a=k` when `binom(n,k) &gt; B*`. This is the strongest existing coverage — a row-uniform *bracket*, never *adjacency*.
- `staircase/statement.md:9`, `petal_g1_layer_maps/proof.md:38,47` (`s = 3..44` sweep), `descriptor`.

**Why this is still a HOLE, not COVERED:** the covering machinery supplies brackets and censuses; the grand-challenge content is **adjacency**, and every adjacency/floor node is pinned at `s = 41`. Per my pre-registered falsifier, COVERED required a node *statement* quantifying over `k &lt; 2^40` rate-half rows. None exists. `rules_freeze:9`'s own tie-break — "on any residual ambiguity the campaign plans against the stricter reading" — independently forces this verdict.

**The uncovered set, mapped exactly (E7 pattern):**
- **`s = 8..40` (33 row sizes): entirely uncovered**, all admissible `q ∈ (2^128, 2^256)` with `2^s | q-1`.
- **`s = 1..7`:** uncovered for `2^128 &lt; q &lt; 2^128·binom(2^s,2^(s-1))`; above that threshold, discharged by the elementary POSE 1 (thresholds `2^129, 2^130.6, 2^134.1, 2^141.7, 2^157.2, 2^188.7, 2^252.2`). At `s = 8` the threshold is `2^379.7 &gt; 2^256` — the corridor **shuts permanently**.
- **`s = 41`:** the existing lane.

**Two hard vacuity thresholds (exact integer checks, `tools/ramguard tiny`):** at rate 1/2 the proved bracket `[k+2^34, 3n/4] = [k+2^34, 1.5k]` is **empty unless `k &gt;= 2^35`** (`s &lt;= 35` have no bracket at all); and RH-LOW's floor at `k + sigma_0`, `sigma_0 = 8,594,128,895 ≈ 2^33.0007`, requires `k &gt;= sigma_0`, so it is **not evaluable for `s &lt;= 34`**. The lane's floors are absolute-width objects; they do not shrink with the row.

---

## D3 / D4 — DRAFT + BLAST RADIUS

Written to **`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md`** (draft only, nothing applied). Contains five exact-edit scope flags (A: `mca_grand`; B: `rate_half_band_closure`, which additionally has its `node.json` and `statement.md` **disagreeing on the (n,k) quantifier**; C: `rate_half_list_adjacent_crossing`, the claim⊋machinery seam; D: the "official row" alias collision; E below), and three posed-not-proved reductions with falsifiers — POSE 1 (list-side triviality corridor, elementary, exact reach tabulated), POSE 2 (k-monotonicity — **I argue against it and say so**), POSE 3 (the recommended per-`s` four-band family re-pose).

**D4 headline:** the blast radius is **narrow** — the supporting-lemma layer is already substantially k-uniform (descriptor, list_interleaved_support_census, census_bounded_scales, staircase, petal_g1), and what is k-specific is exactly four rate-half crossing/floor nodes plus two absolute-width constants. It is narrow for a bad reason: small-`s` rows are not covered by weaker machinery, they are simply not addressed. One softener verified: `petal_g3_pricing_multiplicity`'s constant 719 = `floor(n^6/C(n+6,6))` is 87/224/…/718 at `s = 3..13`, and the quantity is **increasing in n**, so quoting 719 transports downward **conservatively** — that one bends, it does not break.

**Second catch, out of mandate but reportable (FLAG E).** Two mutually exclusive descriptions of the four maximal rows coexist in critical nodes: **Convention A** (`x4_primitive_star_u1_coverage:11`, `b2b_near_tail_bound:8`, `u2c_exact_slice_extras_budget:6`) pins `N=2^41, K=rho·N` → `k = 2^40,2^39,2^38,2^37`; **Convention B** (`petal_g1_layer_maps/notes/cp_packet_20260713/cp_statement.md:33-35`, used by `petal_g3_pricing_multiplicity:19`) says "the four official maximal rows are `n = 2^41..2^44, k = 2^40`". They agree **only at rate 1/2**. Under the caps, Convention A's rates-below-1/2 rows are k-deficient by 1-3 binary orders — so this decides which rows the **clean-rate lane**, the campaign's primary closure target (`mca_grand/statement.md:13`), is actually about. Needs coordinator adjudication.

---

## Predictions vs outcomes

| prior | outcome |
| --- | --- |
| **P1** cap-over-a-family, 0.75 | **HIT**, and stronger than registered — a PROVED machine-checked descriptor node settles it |
| **P2** no reduction/monotonicity theorem, 0.80 | **HIT** |
| **P3** HOLE 0.55 / COVERED 0.30 / PINNED 0.15 | **HOLE.** My COVERED mass was right to exist: real k-uniform machinery was found, just not at the adjacency layer |
| **P4** uncovered set is `k = 2^j, j &lt; 40`, discrete and small | **HIT** — exactly 41 row sizes, lane covers one. My "small" was wrong in spirit: 40 uncovered sizes is not small |
| **P5** larger k is harder; small-k breaks a "sufficiently large" proviso | **PARTIAL/RECAST.** The break is not a proviso — it is **absolute-width floor constants** (`sigma_0 ≈ 2^33`) exceeding `k`, and an **empty bracket** below `k = 2^35`. Sharper and more mechanical than I predicted |
| **P6** literal constants baked in, 0.60 | **HIT** — `2^41`, `2^40`, `sigma_0`, `sigma*`, `719`, `v_2(q-1) &gt;= 41` |
| **P7** the rescue sits one level above the obvious consumers, 0.50 | **HIT on location, MISS on outcome.** `ww_parametric_row_scope_router` / `ww_row_envelope_clause` / `descriptor` are exactly one level up — and they **confirm** the hole rather than close it. The round-28 lesson paid: reading them changed my D1 from inference to citation |

## Self-corrections

1. **I initially reasoned about `B_C` as a codeword count** and drafted a triviality argument on that basis. Reading `rate_half_band_closure/statement.md:78-80` — "`B_mca(a)` is the maximum number of finite **slopes** … `B_mca(a)/q = epsilon_mca`" — showed the binomial argument transfers only to the **list** side (`L_1(a) = max_u #{c : agr &gt;= a}`). POSE 1 is scoped to the list side and the MCA analogue is flagged as unposed.
2. **I nearly reported `census_bounded_scales` as clean n-uniform coverage.** Its window `N' ∈ [~120,~400]` must divide `n`, so the claim is empty at `s &lt;= 6`. Recorded as a caveat rather than a contradiction.
3. **Convention A vs B (FLAG E) was not in my priors at all** and I found it only via a stray grep line. It is a distinct catch and I have not audited its consequences.

## Compliance

Blind priors were registered by Edit into `PREREG.md` under "## Pilot registrations" **after reading only the two named anchors** (`rules_freeze/statement.md` and the `official_row_primes_pinning` ABF26 lines) and before any other read or computation. QUARANTINE honoured in full: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line, and the round-29 pilot dirs `collinearity_object`, `list_profile_bound`, `slack_recursion` were never read (the only `pilots_20260810` paths I touched were my own `k_extremal/` and one incidental grep line from `mca_safe_rewire/REPORT.md`, which is round-28 and not quarantined). No subagents were launched. COMPUTE LAW: all three interpreter invocations ran as `tools/ramguard tiny -- python3 …` from the repo root, including the JSON peeks; stdlib only (`json`, `math`); no Modal, no network, no banked-script execution. RAM discipline: file-at-a-time reads, targeted offsets on long statements, `dag.json` never opened, node.json shards + grep throughout. DRAFT-ONLY honoured: my only writes are `notes/pilots_20260810/k_extremal/PREREG.md` (the registration append) and `notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md`; no `dag/`, `nodes/`, or `tools/` edits, no git operations. Every quantifier claim above is quoted with `file:line` (CATCH-24C); the "nothing covers it" verdict is gated on own-repo greps over `monoton`, `smaller k`/`smaller row`/`extremal row`/`hardest row`/`worst row`, `2^40`/`2**40`/`1099511627776`, `admissible`, `official row`, `for all s`/`every s`/`n-uniform`/`k-uniform`, `transport`/`reduces to`, and a node-name sweep for `small|reduc|transport|monoton|extremal|row_scope` (CATCH-24A). The round-28 lesson was executed explicitly: `mca_grand`'s consumers were traced to the root via `node.json`, and the rescue candidate one level up (`ww_parametric_row_scope_router` → `descriptor`) was read in full before the verdict.
