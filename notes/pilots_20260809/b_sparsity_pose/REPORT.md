# REPORT.md — b_sparsity_pose (round 26) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ad5f97df6688e10b3, 2026-08-09. Pilot: Opus. No edits.

All deliverables are complete. Final report follows.

---

# ROUND 26 — b_sparsity_pose: report

**VERDICT (D4).** The ratified (b) is **not a conjecture at the prize cell — it is a theorem**, and I state and prove it: at `N'=128`, bad primes have density `≤ 2^-93.9` (bulletproof) / `≤ 2^-106.9` (with the exact orbit count) in the admissible window, uniformly over every `v_2`-stratum up to `v_2 ≤ 113.9`. The proof is four banked ingredients plus one pigeonhole; the union-bound route is **prior art in our own repo** (a retired proof attempt), and my increments are the height bound, the orbit count, the `v_2`-grading, and a runnable script. But the pose comes with three teeth that the slogan hides: **(i) "o(1)" has no valid asymptotic parameter** — at `N'=256` the same counting is vacuous by 41 bits and the heuristic says *every* admissible prime is bad, so (b) is a fixed-cell numeric statement, not a family-uniform-in-`N'` one; **(ii) the proved bound is vacuous by 62 bits on the stratum the deployment actually uses** (thin band ∧ `v_2 ≥ 92` ∧ Proth), so (a) and (b) are **complementary, not primary/fallback**; **(iii) the node's own status ruling admits no density branch** — adopting (b) requires amending it (the e1 lane already has the precedent shape, `e1_official_typicality_or_certificate`).

Registrations were appended to `notes/pilots_20260809/b_sparsity_pose/PREREG.md` (lines 87-286) before any computation.

## Misses first

1. **My registered pigeonhole margin `[0.2, 0.4]` bits is WRONG — it is exactly `0.0000`.** I had registered LEM-1 for odd-norm box vectors (`E ≤ 4h-3`, ceiling `253^32 = 2^255.46`). A bad prime is any odd `p` dividing `Norm(w)` for **any** nonzero box `w`; `Norm(w)` need not be odd. The correct ceiling is `(4h)^{h/2} = 256^32 = 2^256` exactly, so `CEIL^{1/2} = 2^128` is exactly the window floor. The lemma survives **only** by strictness: `p1,p2 &gt; 2^128 ⟹ p1p2 &gt; 2^256 ≥ Norm(w)`. Zero margin, but airtight. Caught because my first census returned 470/453 prime divisors instead of round-25's banked 554/536.
2. **GUESS-G (registered at 45%) is REFUTED**: 2/8 violations at `h=4`, 60/128 at `h=8`, 16176/32768 at `h=16` (exhaustive).
3. **F3 not run** — it was superseded: LEM-2 became a two-line proof, so sampling it adds nothing. Recorded, not quietly dropped.
4. **My first Burnside justification was wrong** (see self-corrections), and my first digit-law run failed at chance level from a coordinate bug.

## Escape tests (calibration, run first)

| test | result |
|---|---|
| `large_v2_hunt/d3_thm.py` (LAW 1 + LAW 2 suite) | **0 violations**, `h=2..64`; corollaries 0/3000 |
| exhaustive `h=8` census (my own, independent code) | **exact**: CLASSES 1450, 554 odd prime divisors, 536 `≡ 1 mod 16`, MAXNORM 614656, maxbad 463249, pooled **BADFRAC8 = 0.1117** (banked 0.1115) |
| W_TOP density `~2^-112` | **reproduced**: `PI(W_TOP) = 2^242.00`, so round-25's `log2 BADCOUNT = 130.2` gives `2^-111.80` |

## D1 — THE POSE, and the theorem behind it

**Scope (B0).** Cell `N' = 128`, `h = 64`, `R = Z[x]/(x^64+1)`, box `B = {-2..2}^64`, support bound `2l' ≤ 128`. `W_ADM = {p prime : p ≡ 1 mod 128, 2^128 &lt; p &lt; 2^256}`. `p` is BAD iff `K_p` carries a non-cyclotomic ternary vector of support `≤ 2l'`; by the banked fold reduction this is `p | Norm(w)` for some `w ∈ B \ {0}` — **uniformly in `2l'`**, since a full-support ternary vector folds into the same box.

**B1 (density core) — PROVED.** `#{p ∈ W_ADM : BAD} ≤ 2^135.6034`, hence `BADDENS(W_ADM) ≤ 2^-106.93`.
*Proof.* (i) fold reduction [banked PROVED, `kernel_lattice_reframing`]; (ii) energy ceiling `|Norm(w)| ≤ E(w)^{h/2} ≤ (4h)^{h/2} = 2^256` [banked PROVED, `dli_norm_gate_energy_ceiling` LN4 — **a cross-lane reuse: the DLI lane's ceiling is exactly the mystery-5 MAXNORM bound**]; (iii) pigeonhole: two prime factors `&gt; 2^128` would force `Norm(w) &gt; 2^256`, so each `w` contributes at most one bad prime in `W_ADM`; (iv) `Norm` is constant on the group `G = {w ↦ x^a σ_s w}`, `|G| = 8192`, whose **exact orbit count I computed by Burnside over all 8192 elements: `2^135.6034`** (`h=8` check: `2^11.6366 = 3184 ≥ 1450` actual distinct norms); (v) `PI(W_ADM) = 2^242.54` by PNT in arithmetic progressions for the **fixed** modulus 128 — the only analytic input, effective for fixed `q`. ∎
Without (iv) the fully elementary bound is `5^64 = 2^148.60`, i.e. `2^-93.93`.

**B2 (stratum-uniformity).** On `{p ∈ W_ADM : v_2(p-1) ≥ v}` the same proof gives `2^{v-113.94}`. So **PROVED for `v ≤ 113`**, **OPEN for `v ≥ 114`**. Measured: flat at every `v` (F2 below). `VSPARSE(128) = 113.93`. The four deployed Proth rows (`v_2 = 92,93,95,97`) sit inside with 16.9 bits to spare; the E1-128 pinned field (`v_2 = 200`) is outside and is covered instead by its per-row certificate.

**B3 (what it buys — the row-SELECTION reading).** Good rows form a `1-ε` fraction of every octave of `W_ADM`, so one is found in `O(1)` expected draws and certified per-row. It is **not** a for-all-rows statement: `lattice_cone_certificate/conditional.md:41-45` needs "the row-specific certificate" for **each** assigned knife-edge row — for an adversarially assigned row only (a) closes it. The consumer (b) actually replaces is `generator_economy/statement.md:100-102` ("per-row certification is cheap; UNIVERSAL closure over the unbounded row set is the open content").

**The honest negative clauses (all measured, none registered in advance):**
- **`N'`-scope collapse.** Under the prize's fixed `|F| &lt; 2^256`, the bound is `2^-216` (`N'=32`), `2^-180` (`N'=64`), `2^-106.9` (`N'=128`), **`2^+42.7` VACUOUS (`N'=256`)**. Worse: the retired proof's own heuristic gives `E S_p = 2^64.2` collisions *per prime* at `N'=256` (I reproduce `2^63.6`), i.e. **essentially every admissible prime is bad at `N'=256`**. So "o(1) as `N' → ∞`" is not merely unproved, it is heuristically **false**; the only `N'→∞` reading that survives uses a window growing to MAXNORM (there the bound decays doubly exponentially: `2^-0.4, -9.8, -36.4, -105.9, -276.6, -683.2` for `N' = 16…512`). **Recommendation: pose (b) as a numeric per-cell bound, not an asymptotic.**
- **Sub-family vacuity.** `W_DEP` unrestricted: bound `2^-23.49`. `W_DEP ∧ v_2 ≥ 92`: `PI = 2^74.09`, bound **`2^+61.51` VACUOUS**. Proth `k·2^92+1`: `PI = 2^73.10`, bound **`2^+62.50` VACUOUS**. Heuristically that stratum has density `2^-29`, but nothing proves it. **The deployed rows are exactly where (b) has no proof and (a) does the work.**
- **Governance.** `status_ruling.md:11-15` permits return to PROVED only via a family-uniform theorem (FALSE since round 24) or an exhibit-scoped certificate with consumers narrowed. A density theorem is a third thing with no slot. Amending the ruling is a prerequisite to banking (b) — precedent exists one lane over.

**Falsifiers (registered with power controls).**
- **F1 (run, exhaustive, full power).** `h=8`: LEM-1 violations **0**; LEM-2 violations **0**; `BADCOUNT/PI` in `W_ADM(16) = (2^16, 2^20]` is `73/9407 = 0.00776` against the proved bound `3184/9407 = 0.3385` — **non-vacuous already at the toy**, over-predicting truth by 43.6×. Not falsified.
- **F2 (run, the uniformity clause).** Cochran-Armitage trend on `BADFRAC8(v)`, `v=4..12`: **pooled `Z = -0.472`**, **dyadic-stratified `Z = -1.336`** — not falsified. Power: an ≥ **10.0%** (pooled) / **15.6%** (stratified) per-`v`-step multiplicative trend would be caught at 80%. This resolves round-25's marginal `χ² p=0.07` as omnibus noise, not a trend.
- **F3** superseded by proof (not run). **F4** registered for the future: a collision at any deployed Proth row — probability `≤ 4·2^-29` heuristic; it would be a `≥2^27` surprise.
- **Consistency check that could have failed:** round-25's measured `log2 BADCOUNT(W_ADM) = 132.0` must lie under my proved ceiling `135.60`. **Headroom 3.60 bits.** It does.

## D2 — LAW 2 general-`w` (named gap 1): CLOSED, two ways

Write `s(w) := ((Norm(w)-1)/2h) mod 2` (legal by LAW 1).

- **P1 (PROVED + 0 violations, `h=4..32`).** `s` is a homomorphism — `Norm` multiplicative and `(1+2ha)(1+2hb) ≡ 1+2h(a+b) mod 4h`. Two lines.
- **P2 (PROVED + 0 violations, `h=4,8,16,32,64`) — the general-`w` law.** With `u = w mod 2` (a unit of `F_2[x]/(x^h+1)`), `û` its 0/1 lift, `z = ((w-û)/2) mod 2`:
  **`Norm(w) ≡ 1 + 2h·[ σ(u) + (u^{-1}z)_{h/2} ] (mod 4h)`**, `σ(u) := s(û)`.
  Proof: `w = û·(1 + 2v)` in `R_2` with `v = û^{-1}z' `; apply P1 and round-25's LAW 2 (a polynomial congruence, so valid for 2-adic `v`). Round-25's law is the case `u = 1`; its rotated corollary is `u = x^j`. **The entire `z`-dependence is exactly linear via `u^{-1}` — the general-`w` gap reduces to the single function `σ`.**
- **P2' (0 violations).** Consequently `s(w)` depends only on `w mod 4` (because `s(1+4r) = (2r)_{h/2} = 0`).
- **σ has no low-degree closed form.** Exact ANF in the `(x+1)`-adic coordinates: `h=4` → `σ = a_3(a_1+a_2)` (2 terms, degree 2); `h=8` → 24 terms, degree 3; `h=16` → degree 5. GUESS-G refuted.
- **The linear form (the clean statement).** `(R/4)^* = 1+πR`, `π = ζ-1`, has the canonical filtration with quotients `F_2` generated by `1+π^k`, so every odd-norm `w` has a **unique** expansion `w ≡ ∏_{k=1}^{2h-1}(1+π^k)^{ε_k} (mod 4)` and therefore
  **`s(w) = Σ_k ε_k c_k`, `c_k := s(1+π^k)`.**
  Verified by explicit digit extraction: **0 violations / 200 random `w` at `h = 4, 8, 16, 32`.** Tables computed; `c_k = 1` for **all `k ≥ h-1`** at every `h` tested; the low half has no evident closed form (`h=32` support below 31: `{3,7,10,11,14,16,18,20,23,25,27,29}` — parity and binary-weight patterns checked, none). So general-`w` LAW 2 is now a **linear law with a computed `2h-1`-bit constant table**, and `σ` is evaluable by one norm computation.

## D3 — box depth (named gap 2): `2^17 → 2^40`, no structure

`n = 2^20` box vectors (4 registered seeds), `Norm mod 2^48` by a Kronecker-packed tower recursion validated against the exact norm (**0/60 mismatches**, 3344 samples/s). **LAW-1 replay: 1,048,576/1,048,576 norms `≡ 1 mod 128`.**

| D | AVAIL `2^{D-7}` | distinct | uniform pred. | collisions | `M̂col/AVAIL` |
|---|---|---|---|---|---|
| 12-22 | to `2^15` | **all** | — | — | 1.000 |
| **23** | `2^16` | **65536 = FULL** | — | 8,381,348 | 1.001 |
| 24 | `2^17` | 131032 | 131028.0 | 4,188,153 | 1.001 |
| 28 | `2^21` | 825393 | 825165.0 | 262,074 | 1.000 |
| 32 | `2^25` | 1032297 | 1032361.3 | 16,453 | 0.996 |
| 36 | `2^29` | 1047567 | 1047552.7 | 1,010 | 1.014 |
| **40** | `2^33` | 1048512 | 1048512.0 | 64 | **1.000** |
| 44 / 48 | `2^37`/`2^41` | 1048573 / 1048575 | — | 3 / 1 | 1.33 / 0.25 (no power) |

**Registered falsifier (`M̂ ≤ AVAIL/2` at 3σ) not triggered at any depth.** Full realization proved by exhibition to modulus `2^23` (banked was `2^17`); the effective class count equals the available count to within 1.4% out to `2^36` and 12.5% at `2^40` — a factor-2 gap at `D=40` is excluded at `&gt;5σ`. Honest resolution limit: `D=44` gives ~2σ, `D=48` none. **No structure; `v_2`-uniformity has no hidden 2-adic obstruction down to depth `2^40`.**

## Registered predictions vs outcomes

| registered | outcome |
|---|---|
| LEM-1 0 violations | **CONFIRMED** (h=8 exhaustive; h=64, 4000 samples, max norm `2^220.3`) |
| pigeonhole margin `[0.2,0.4]` bits | **MISSED — exactly 0.0000** (wrong box scope; lemma survives by strictness) |
| `log2 BADDENS ≤ -93 ± 3` bulletproof | **CONFIRMED** (`-93.93`) |
| `log2 BADDENS ≤ -106 ± 3` orbit | **CONFIRMED** (`-106.93`) |
| `VSPARSE(128) ∈ [108,118]` | **CONFIRMED** (`113.93`); deployed rows inside, E1-128 outside — as predicted |
| retired proof reproduces within 1 bit | **CONFIRMED** (`2^-88.0` vs their `2^-87.4`; `N'=256`: `2^63.6` vs `2^64.2`) |
| F1 (exhaustive) | **not falsified** |
| F2 trend, `|Z| &lt; 1.96` | **not falsified** (`-0.472` / `-1.336`; MDE 1.100 / 1.156) |
| P1 homomorphism (95%) | **CONFIRMED**, 0 violations |
| P2 reduction (85%) | **CONFIRMED**, 0 violations to `h=64`; now proved |
| P3 GUESS-G (45%) | **REFUTED** |
| P-D3a full realization `D ≤ 23` | **CONFIRMED** (exactly `2^16` classes at `D=23`) |
| P-D3b coupon/collision within 2× where `#coll ≥ 5` | **CONFIRMED** (`1.000-1.014` through `D=40`) |
| D3 structure falsifier | **not triggered** |

## Self-corrections

1. **Scope error (above):** registered LEM-1 on odd-norm vectors; the bad set needs the full box. Ceiling `253^32 → 256^32`, margin `0.27 → 0.00` bits.
2. **Burnside justification was wrong.** I first bounded `|Fix(g)| ≤ 5^{h/2}`; false — an affine index map `i ↦ si+a` can fix `gcd(s-1,h)` coordinates. Replaced by the **exact** orbit count over all `2h²` elements (`h=8`: 3677 → 3184; `h=64`: `2^135.6034` either way, since the correction is `&lt; 10^-4` bits).
3. **Coordinate bug:** `to_pi_basis` expanded at `x=0` instead of `x=1`; the digit law "failed" 100/200 (chance). Fixed → 0/200 at every `h`.
4. **Registered D2 fallback deviated from.** I registered "if P3 fails, fit `σ` and validate out-of-sample". I computed the exact ANF instead (no fit needed) and, finding no low-degree form, pivoted to the multiplicative-digit coordinates — an unregistered instrument that worked. Declared.
5. **A write outside my dir.** Running the banked `large_v2_hunt/d1_h8.py` as an escape test rewrote `large_v2_hunt/state/d1_h8.json`. The script is deterministic and its output reproduces the banked numbers exactly, but this violates DRAFT-ONLY and I disclose it; I checked for and avoided further such writes.
6. **Ladder extended:** added `D = 22, 23` to the registered D3 ladder — required to test my own "every `D ≤ 23`" prediction.
7. **Novelty subtraction, stated before computing and confirmed after.** The union bound is **prior art in our own repo**: `background/nodes/e1_folded_no_vector_certificate_256_payload/retired_proof.md` (with `PRO_W3_e1_density.md:33-39` naming it as ask (A)(i), and the open payload `e1_open_cell_control_payload`). I claim **no novelty for the route**. New here: LN4 as the height bound (192 bits at `N'=128`; `r_N` 4→2 at `N'=256`), the exact orbit count (13.00 bits), the `v_2`-grading and `VSPARSE`, the `N'`-scope and sub-family findings, the `h=8` exhaustive validation of the whole chain, and a **runnable script** — which is the standing **catch #61 restore item** (`retired_proof.md:15`, "cited script NOT ON DISK").

## Compliance

QUARANTINE HELD: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line; the three other round-26 pilot dirs (`umin_spike_hunt`, `freeze_tail_law`, `m7_falsifier_hunt`) were never opened — one `ls` of `notes/pilots_20260809/` listed their names only. No subagents spawned, so the clause needed no forwarding. COMPUTE LAW: every `python3` invocation went through `tools/ramguard tiny|local -- python3` from the repo root, including all JSON peeks; **`RAMGUARD_TIMEOUT` was never used**; the D3 sampling ran as one background job of four sequential `ramguard local` calls (~75 s each, checkpointing every 50k samples to `state_d3_*.bin`). RAM DISCIPLINE: file-at-a-time reads, `dag.json` never opened (node.json shards and grep only), no bulk directory loads; peak analysis footprint one 1M-element list per depth. DRAFT-ONLY: all authored files in `notes/pilots_20260809/b_sparsity_pose/` (`PREREG.md` registrations at lines 87-286, `d1_toy.py`, `d1_prize.py`, `d1_burnside.py`, `d2_law2.py`, `d2_anf.py`, `d2_digits.py`, `d3_depth.py`, `d4_checks.py`, `state_d1_toy.json`, `state_d1_prize.json`, `state_d3_*.bin`), with the single disclosed exception in self-correction 5. Python stdlib only; no git, no Modal, no edits to `dag.json`, `nodes/`, or `tools/`; no status flips. Every measured functional is named in R0 of the PREREG; no shift-0 cells.
