# REPORT.md — list_profile_bound (round 29) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a76b2cf8b476e498a, 2026-08-10. Pilot: Opus. No edits.

All deliverables complete. Writing the report of record.

---

# list_profile_bound — report of record (round 29)

## VERDICT (first)

**No UB theorem landed at small `c`, and I can now say why with an exact number rather than a shrug. Three things did land, and one of them is a correction that changes the working hypothesis's operational value.**

1. **THE HEADLINE (a consumer-bar correction, CATCH-24C).** The brief's premise — *"the PROVED floor at `k+2^34-1` already supplies the unsafe half IF the crossing lands at `k+2^34+c`"* — holds **only at `c = 0`**. For any `c &gt;= 1` the required unsafe index is `k+2^34+c-1` with `sigma &gt;= 2^34`, which is **beyond the floor's mechanism-space-exhausted reach of `2^34-1`** (round-28 F1). So `adjacency_closing` is not served by "`a_RH = k+2^34+O(1)`" for any `O(1)` other than zero: **every `c &gt;= 1` re-opens the unsafe half and demands a NEW floor, not just the upper bound.** The theorem target is therefore sharper than posed: *an upper bound at exactly `sigma = 2^34`*, or else *an upper bound at `2^34+c` plus a matching new lower bound at every smaller index*.

2. **THE INSTRUMENT VERDICT (D2, and it is a structure theorem, not a list).** All seven in-repo far-CA instruments have **the same domain, for the same reason**: `rate_half_ca_hankel_fullrank_branch` (`r &lt; R/2`), `..._fixed_kernel_branch` (same setting), `rate_half_far_ca_anchor_pencil_normal_form` (`2r &lt; d_min`), `rate_half_ca_hankel_..._quotient_minimal_support_uniqueness` (`r = 2^39-1`), apolar mechanism C (`2rho &lt; d(K) = R+1`), HD1 (`a = 3n/4`), and the trivial two-codeword bound (`2a-n &gt; k-1`). Every one of these is the **same inequality `2(n-a) &lt;= n-k`, i.e. `a &gt;= 3n/4`** — the unique-decoding threshold of the difference code. They are not seven instruments with seven reaches; they are **one threshold seen seven ways**, and the entire open bracket `[k+2^34, 3n/4)` is precisely its non-uniqueness region. Zero instruments reach below it (PRED-8 confirmed, 0 of 7).
   *The single exception cuts the other way and is a CATCH-24A firing against me:* `rate_half_list_integer_johnson_safe_anchor` (PROVED) **does** cross below `3n/4`, reaching `a &gt;= floor(sqrt(n(k-1)))+1 = k + 455,432,628,212 = 0.70711n` — 17.16% deeper in `sigma` than `3n/4`. But it bounds `L_1` (ordinary lists), **not** `B_ca^far`.

3. **THE MEASURED CORRECTION (D3-iii) — reported as a miss against an inherited number.** Round-28's load-bearing decay figure was transported as a **ratio**: `2.8074 bits = 0.6865 * log2 q -&gt; 175.744 bits/unit at razor -&gt; c = 1`. I computed `F_LMAX(8,4,5)` **exactly and exhaustively** (modulo the two exact symmetries) at **three** fields: **`F_LMAX = 7` at `q = 17`, `q = 41`, and `q = 97` — identical.** The decay is a **q-independent absolute constant of 2.8074 bits**; the ratio falls as `0.6868 -&gt; 0.5240 -&gt; 0.4254`, exactly as a saturated q-independent cap must. **The ratio transport is unsupported by its own cell, and overstates the razor decay by a factor 62.6 (5.97 bits).** Correct transport from that cell gives **`c = 32`, not `c = 1`.**

**What `c` is pinned at:** nothing pins it. **Sharpest honest bracket: `0 &lt;= c &lt;= 532,575,944,704`**, the upper end being the PROVED bracket top `3n/4` (HD1) and unbeaten by anything I could prove. Evidence concentrates in `c in [1, 32]` from three transports (family cliff -&gt; 1; measured `B_ca^far` ratio -&gt; 1; measured `F_LMAX` absolute -&gt; 32), **all four of which cross a mechanism change and none of which can resolve `c`** — see the structural reason in D3-iii below.

---

## Deliverables

### D1 — THE POSE

**(UB-far).** For every admissible razor row (`n=2^41`, `k=2^40`, `D` a multiplicative coset of order `n`, `q` prime `= 1 mod n`, `2^255.9 &lt; q &lt; 2^256`) and every `sigma &gt;= 2^34 + c`:
`B_ca^far(k+sigma) &lt;= UB(sigma) &lt; 2^128 &lt;= B*(q)`.

**Three corrections to the pose as briefed:**

- **The three objects are NOT equivalent.** The brief writes "the far-CA max list profile (equivalently `B_ca^far`, equivalently `F_LMAX`)". Measured refutation at one cell: at `(n_s,k_s,a)=(8,4,5)`, `F_LMAX` is **q-independent** (7, 7, 7 at q=17/41/97) while `B_ca^far` **grows with q** (17, 37, 51). `B_ca^far` counts slopes and is governed by the code-pair line structure; `F_LMAX` counts codewords. Conflating them transports the wrong exponent.
- **The consumer needs `c = 0`** (headline 1). `mca_safe`'s bar is the same moving bar.
- **`DEFICIT` is q-free.** The unsafe margin at the bracket bottom is **exactly 88.0000 bits at `q ~ 2^167`, `2^200`, and `2^256`** (exact integer replay, PRED-3), because the floor saturates at `(q-n)/k` against a budget `q/2^128`, so the ratio is `2^128/k = 2^88` with `q` cancelling. **The theorem target is uniform in `q` across the whole widened quantifier.** (Scope flag: HD1 needs `q &gt;= 2^169`, so `[2^167, 2^169)` has no far-CA discharge even at `3n/4` — that sliver is the apolar target's territory.)

**Registered falsifier with power — (FLAT), and the quantified link to the refuted `(RH-AC-hi)`.** `(RH-AC-hi)` needs average decay `&lt;= 2.152750e-10` bits/unit over **532,575,944,705** agreements. `(UB-far)` at `c` needs `&gt;= 88/(c+1)` bits/unit over `c+1` units. Power ratios: **`2^38.57` at c=0, `2^37.57` at c=1, `2^33.53` at c=32, `2^30.81` at c=216.** The two demands are **nested, not equivalent**: (FLAT) at small `c` is a strictly weaker demand than `(RH-AC-hi)`. **Refuting `-hi` by `2^40.11` therefore supplies no part of (UB-far)** — the 2^40 flatness result and the theorem target are about different orders of quantifier, and I flag that the round-28 verdict's rhetorical force does not transfer.

### D2 — THE INSTRUMENT SURVEY (own-repo first)

| instrument | status | domain | what it gives at `sigma=2^34` | gap to `2^128` |
|---|---|---|---|---|
| Hankel full-rank branch | PROVED | `r &lt; R/2` ⇔ `a &gt; 3n/4` | nothing | out of domain by `2^39-2^34` |
| Hankel fixed-kernel branch | PROVED | same setting | nothing | same |
| Hankel **moving-kernel** branch | **absent** | — | — | **PRED-8b: no node; only the residual sentence at `fixed_kernel_branch/statement.md:37`. The `a &gt; 3n/4` discharge is itself incomplete.** |
| anchor-pencil normal form | PROVED | presentation **domain-free**; uniqueness needs `2r &lt; d_min` ⇔ `a &gt; 3n/4` | (AP1)-(AP3) hold at `sigma=2^34`; no finiteness | the counting conclusion is out of domain |
| QMU/QMP minimal-support species | PROVED | `A=1` exceptional face, `e=2^38-1`, `r=2^39-1` | nothing | same `3n/4` face |
| apolar mechanism C | PROVED | `2rho &lt; d(K)=R+1` | **illegal**: margin `= (2^40+1) - (2^41-2^35) = -1,065,151,889,407` | PRED-10 confirmed |
| far-CA rider (RR2)/(RR4) | PROVED | any `r` | `log2 UB_RIDER &gt;= 5.4536e14` at `log2 q=256` (`3.5576e14` at 2^167) | **vacuous by 5.45e14 bits.** Round-28's "hopeless" **verified, not merely repeated** |
| HD1 half-distance bracket | PROVED | `a = 3n/4`, `q &gt;= 2^169` | `B_mca(3n/4) &lt;= n` | this IS the bracket top |
| **integer-Johnson safe anchor** | PROVED | `a &gt;= floor(sqrt(n(k-1)))+1 = 0.70711n` | bounds **`L_1`**, not `B_ca^far` | **crosses below 3n/4 by 94,323,185,676 units of sigma (17.16%)** — the only instrument that does |

**The structural finding** is the shared threshold (headline 2), plus its exact arithmetic companion: the classical Johnson entry point at rate 1/2 is `a/n = 1/sqrt(2) = 0.7071068` exactly, reproducing the banked node's own closed form `floor(sqrt(n(k-1)))+1`.

### D3 — THE ATTACK (what I proved, all validated)

**T1 (SUNFLOWER RIGIDITY).** For `(y_1,y_2)` column-far at `a &gt; n/2`, fix a witness `c_lambda` per bad slope. Pairs of bad slopes partition among code pairs ("lines"): for `lambda != mu`, `v=(c_lambda-c_mu)/(lambda-mu)`, `u=c_lambda-lambda v`. For a line `P` with `&gt;= 2` slopes and jointly-explained set `E_P`:
(i) `E_P subset A_lambda` for **every** slope on `P`; (ii) `A_lambda cap A_mu = E_P` for **every** pair on `P` — all pairwise intersections coincide; (iii) the petals `A_lambda \ E_P` are pairwise **disjoint**; (iv) hence `m_P (a-e_P) &lt;= n-e_P`, i.e. `m_P &lt;= 1 + r/(a-e_P)`, with `2a-n &lt;= e_P &lt;= a-1`.

**T2 (STRATIFIED RIDER).** With an anchor slope fixed:
`B_ca^far(a) &lt;= 1 + sum_P r/(a-e_P) &lt;= 1 + r * L_1(2a-n)`.
Against the banked `(RR2): 1+(r+1)L_2(2a-n)` this is a genuine double sharpening — the code-**pair** count `L_2` becomes the single-word list `L_1` (**halving the exponent**: `2.7268e14` vs `5.4536e14`), and the blanket factor `r+1 = 2^40` becomes a per-stratum weight that equals **exactly 1** at the minimal core `e = 2a-n`. In the banked anchor coordinates the weight is `s/(s+t-r)`, sharper still. **It changes nothing about reach** — both bounds are ~`2.7e14` bits above target — and I say so plainly.

**T3 (FISHER SUB-STRATUM, unconditional).** If all pairwise overlaps are `&lt;= theta &lt; a^2/n`, then `#slopes &lt;= (a-theta)/(a^2/n - theta)`. At `sigma = 2^34`, `a^2/n = 2^39+2^34+2^27` **exactly** (an integer). `theta = n/4` gives **`&lt;= 32`** (123 bits of margin); `theta = a^2/n - 1` gives **`&lt;= 549,621,596,161 = 2^39-2^27+1`** (89 bits of margin). So a UB with enormous margin holds on the entire quasi-random-overlap stratum.

**T4 (ELEMENTARY UNCONDITIONAL THRESHOLDS).** (a) `a &gt;= ceil((2n+k)/3) = 1,832,519,379,627` (`a/n = 5/6`) forces **one line**, hence `B_ca^far &lt;= n-a+1 = 366,503,875,926` (89.6 bits under budget). (b) `a/n &gt; (9+sqrt(17))/16 = 0.8201941` (verified against the exact integer search: `a = 1,803,625,903,488`) makes the number of lines through a slope Fisher-bounded, hence `B_ca^far` finite and `&lt; 2^128`. **Both are worse than the banked `3n/4`** — I report them as an independent elementary re-derivation reaching 0.82n, not as progress.

**T5 (THE EXACT OBSTRUCTION — the number I would carry forward).**
`GAP_FISHER = (k-1) - a^2/n = 532,441,726,975`, and the entire open bracket is `532,575,944,704`. **Ratio = 0.999748.** The amount by which the pairwise-overlap cap must be improved — from the MDS cap `k-1` down to the Fisher threshold `a^2/n` — is **99.975% of the whole open bracket**. The open bracket *is* the region where the MDS cap exceeds the Fisher threshold; they end together. Any theorem that pushes the achievable pairwise-overlap cap below `a^2/n` at `sigma = 2^34` closes (UB-far) outright with 89 bits of margin (T3).

**Validation (T1–T4).** `d2_sunflower.py` at `(8,4,17)`: **21,832 column-far configurations across `a in {5,6,7}`, 0 violations** of T1(i)-(iv), the `M_LINE` cap, the `E_P` range, T3, or T4. T4 is **tight**: at `a=7` the theorem forces `M &lt;= n-a+1 = 2` and the observed maximum is exactly 2.

**T6 (conditional UB).** Via T2: *if* `L_1(2a-n) &lt;= X` for the punctured word `y_2` then `B_ca^far(k+sigma) &lt;= 1 + r X`, so `X &lt; 2^88/(1-2^{-6})` suffices. The named hypothesis is a list bound at agreement `2*sigma = 2^35`, i.e. **`2^{-5} k`** — five doublings below dimension, where the list is at least `q^{k-2^35} = 2^{2.7e14}`. Stated for completeness; the hypothesis is false, not merely unproved. **No honest conditional UB exists on this route.**

**D3-iii — THE LADDER, and why the program cannot close.** Cells C1-C3 exact and exhaustive (`d3_ladder.py`, results in `d3_ladder_results.txt`):

| q | `F_LMAX(8,4,5/6/7)` | decay 5→6 | ratio to log2 q | `B_ca^far(8,4,5/6/7)` |
|---|---|---|---|---|
| 17 | **7 / 1 / 1** | 2.8074 | 0.6868 | 17 / 5 / 1 |
| 41 | **7 / 1 / 1** | 2.8074 | 0.5240 | 37 / 4 / 1 |
| 97 | **7 / 1 / 1** | 2.8074 | 0.4254 | 51 / 4 / 1 |

The per-cell **downward bias, quantified rather than waved at**: `F_LMAX` at this cell is pinned at its q-independent combinatorial value 7 across a 5.7x range of `log2 q`, so `log2 F_LMAX / log2 q -&gt; 0` by construction and the ratio transport is an artifact of `q=17` being the smallest admissible field. `B_ca^far` at the same cell does the opposite (17/37/51, ratio 0.43-0.60 of `log2 q`).

**The structural reason the ladder cannot pin `c`** (registered as this deliverable's negative result): at rate 1/2 the scaled bracket's **interior width is `n_s/4 - 1`** — **1** at `n_s=8`, 2 at `n_s=12`, 3 at `n_s=16` — while the razor bracket is `2^39-2^34 = 5.33e11` wide. The cells measure a **one-unit cliff**, not a decay rate over an interval, and exact cost grows like `q^{n_s/2}`. `n_s=12` was priced and is out of reach under the compute law (17.3M normalised words x 792 subsets); `n_s &gt;= 44` would be needed for even ten interior points. **The scaled-cell program is structurally incapable of resolving `c` and should not be re-commissioned for it.**

### D4 — THE CONSTANT

| basis | `c` | status |
|---|---|---|
| PROVED bracket top (HD1, `3n/4`) | **532,575,944,704** | **unconditional; unbeaten** |
| integer-Johnson anchor (bounds `L_1` only) | 438,252,759,028 | proved for the wrong object |
| family-cliff transport (126.5240 b/u) | 1 | one construction's death, not the profile |
| measured `B_ca^far` ratio transport (110-153 b/u) | 1 | cell has bracket width 1 |
| measured `F_LMAX` absolute transport (2.8074 b/u) | **32** | **the corrected round-28 number** |
| round-28 ratio transport (175.744 b/u) | 1 | **refuted by the q-ladder** |

**Sharpest honest bracket: `0 &lt;= c &lt;= 532,575,944,704`.** No lower bound on `c` exists (the floor's reach is exhausted at `2^34-1`), so `c = 0` remains open — and `c = 0` is the only value that serves `adjacency_closing`. **What closes it:** T5's inequality — a pairwise-overlap cap below `a^2/n = 2^39+2^34+2^27` at `sigma = 2^34`. That is the single named next object, and it is worth 89 bits of margin the moment it lands.

---

## Predictions vs outcomes

**MISSES, first (1 hard, 1 partial):**

- **PRED-4 MISS.** Registered `SIGMA_JOHN/2^34 in [30,36]`; measured **26.5097** (`SIGMA_JOHN = 455,432,628,212 = 2^38.7284`). My registration carried a point estimate of 31.9 derived from `2^39.245`, which is the *Hankel* threshold, not the Johnson one — a slip in my own arithmetic, disclosed. The conclusion (Johnson far out of domain) is unaffected; the direction of the error is that Johnson reaches **deeper** than I registered.
- **PRED-1 PARTIAL.** `d4_margins.py` reproduces 114.6503, 2^40.11, 532,575,944,705 and 2.152750e-10 exactly, but does **not** compute the `2^216.0000`/`88.0000` pair I registered against it; I recomputed those independently (PRED-3) and they match exactly at three fields. Scope error in my registration, not a numeric one.

**HITS (14):** PRED-2 (2/2 verbatim), PRED-3 (88.0000 at three q, q-free), PRED-5 (32 and 549,621,596,161 exact), PRED-6 (366,503,875,926 exact), PRED-7 (0.8201941), PRED-8 (0 of 7), PRED-8b (branch absent), PRED-9 (5.4536e14), PRED-10 (margin −1,065,151,889,407), PRED-11 (32 / 217 / 1), PRED-12 (unbeaten), PRED-13 (2^33.5281), PRED-14 (T1(i)-(iv) not in-repo, with the subtraction below), PRED-15 (7/1/1 replayed; 7 at q=41,97 as registered).

**Re-scoped and confirmed:** PRED-16. I registered it as `|F_DECAY - log2 CAP_COMB| &lt; 1e-3`, but the pure combinatorial ceiling is a weak object (I hand-derived `&lt;= 11` for that cell). The operative test is q-independence, which I substituted **before** running and which fired: `F_LMAX = 7` at three fields.

**NOT MEASURED (declared):** cells C4-C6 (`n_s = 12, 16`) — priced and out of compute-law reach; the reason is now a result (D3-iii), not a shortfall.

## Self-corrections (5, all disclosed)

1. **A real bug in my own validation, caught by my own theorem.** `d2_sunflower.py` v1 tested only the leading interpolation coefficient, so for `a &gt; k+1` polynomials of degree `k..a-2` leaked in as "codewords" — 1,682,607 apparent T1 violations including impossible empty cores. I did **not** weaken the theorem; I diagnosed the code (the fix requires `a-k` functionals, not one), and post-fix the count is **0 violations in 21,832 configurations**. Reported here because the first run's output would otherwise read as a refutation.
2. **PRED-4's registered window was wrong by my own slip** (Hankel threshold used in place of Johnson's).
3. **PRED-6's non-integrality worry was unfounded** — `ceil((2n+k)/3)` lands `n-a+1` exactly on the registered 366,503,875,926.
4. **CATCH-24A subtraction, three firings.** The anchor normalization and its `(AP1)-(AP3)` presentation are **banked** (`rate_half_far_ca_anchor_pencil_normal_form`, PROVED) — I claim only the multiplicity analysis T1(i)-(iv) that its uniqueness clause sidesteps. The Johnson threshold is **banked** with the identical closed form (`rate_half_list_integer_johnson_safe_anchor`). The `3n/4` top is **banked** (HD1). My genuinely additive content is T1(i)-(iv), T2's stratification, and T5's number.
5. **A brief-side defect.** The brief's "*the certified worst-case decay ratio (0.1451) clears the 88 bits in ~217 units*" is not reproducible from `d4_margins.py`'s own transport, which converts 0.1451 to **37.1456 bits/unit** and clears 88 bits in **2.37 units**. The 217 figure corresponds to `0.1451 x 2.8074 = 0.4074` bits/unit — treating the certified ratio as a multiplier on the *absolute* cell decay rather than on `log2 q`. Both readings are printed in `d1_core.py`; the discrepancy is 91x and should be resolved before the number is quoted again.

## Compliance

Brief and PREREG read first. All registrations (R0-R6, functionals, pose skeleton, instrument priors, cell ladder C1-C6, PRED-1..16 with numeric windows) appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/list_profile_bound/PREREG.md` with the Edit tool **before any computation and before any grep**; PRED-16's re-scoping was fixed before its run. QUARANTINE honored: `CAMPAIGN_LEDGER.md` never opened; `collinearity_object`, `k_extremal`, `slack_recursion` never read; no subagent spawned. COMPUTE LAW: **5 of 5 interpreter invocations** under `tools/ramguard`, each with `RAMGUARD_TIMEOUT` set explicitly (60s tiny for the banked replay; 120s, 290s, 290s, 290s local) — **no breaches**. The one banked script (`d4_margins.py`) was run from a **scratch copy** at `/tmp/claude-1000/.../scratchpad/lpb/`, never in place. DRAFT-ONLY: every write confined to `notes/pilots_20260810/list_profile_bound/` (`d1_core.py`, `d2_sunflower.py`, `d3_ladder.py`, `d3_ladder_results.txt`, PREREG appendix); one stray file created and removed; no `dag/`, `nodes/`, or `tools/` writes; no git, no Modal, stdlib only. RAM discipline: file-at-a-time reads, `dag.json` never opened, no bulk loads, largest run ~500k words streamed. F3 zero-power declaration honored — **no mean-model or random-word quantity enters any verdict**; every load-bearing number is an exact integer computation or an exhaustive max. Every measured functional named in R0. Misses reported first, in their sections and in the summary.
