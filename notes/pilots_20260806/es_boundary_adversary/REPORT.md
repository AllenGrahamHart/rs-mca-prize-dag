(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# (ES) BOUNDARY ADVERSARY — ROUND 16 REPORT

**Verdict in one line: (ES) as posed is FALSE — five verified non-periodic 0/1 codewords sit strictly below the balance boundary — but every one of them lives in the gap between two inequivalent readings of "balance", and the reading used by the HARDENED floor node survives untouched, as does the faithful crossing shape.**

## 0. What was run

All under the ramguard law from `/home/u2470931/smooth-read-solomin/prize`. Files (all inside my dir, nothing else touched):

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_boundary_adversary/es_lib.py` — exact cyclotomic/F_p machinery
- `…/es_selftest.py` — **296 checks, 0 failures** (fail-closed)
- `…/es_census.py` — the exact bad-prime census (method M1)
- `…/es_crossing.py` — the crossing-shape row
- `…/es_witness.py` — **self-contained ramguard-tiny witness reproduction**, exit 0
- `…/es_analyze.py` — curve / boundary / structure
- outputs: `census_n16_2_8.json`, `census_n32_2_6.json`, `crossing_n32_r8.log`

**The method (registered before computing).** Rather than sweeping p, for each subset S I compute the exact finite set of characteristics in which it is a solution: `S` is a solution in char p ⟺ `gcd(Phi_n, V_1, …, V_{w-1})` has degree ≥ 1 in `F_p[X]` ⟺ `p | N(I_S)`, `I_S = (x_1,…,x_{w-1}) ≤ Z[zeta_n]`. Candidate primes = prime divisors of `gcd_s |N(x_s)|`, each then confirmed by an exact `F_p[X]` gcd. **This decides all p at once**, so the results below are complete over every characteristic, not sampled.

**Cross-validations that had to pass first.** (i) The census identity vs independent Gray-code brute force with element arithmetic in explicitly constructed `F_p`, `F_{p^2}`, `F_{p^4}` — exact agreement. (ii) LEMMA Z's char-0 classification confirmed exhaustively over all 2^16 subsets × all w. (iii) **External:** my machinery recounts the *banked* number — `critical/nodes/u2c_giant_tnull_dichotomy/node.json:8` records "complements of size-6 accidents; **160 witnesses**" at (q=97, n=32, t=2); I get **exactly 160**, on a count it was not tuned to.

## 1. C1 — THE HUNT: **REFUTED**, with a decisive qualifier

Five in-scope sub-balance accidents, all at n=32, all with **structural family EMPTY** (M ∤ r', so (ES) predicts *zero* solutions, not "few"):

| r' | w | p | delta | \|Z_w\| | Lam (bits) | p>n? | stratum a |
|---|---|---|---|---|---|---|---|
| 6 | 4 | 7 | 4 | 10 | **−8.284** | no | 1 |
| 6 | 3 | 47 | 2 | 4 | **−2.429** | **yes** | 0 |
| 6 | 4 | 17 | 2 | 5 | −0.648 | no | 1 |
| 5 | 2 | 23 | 4 | 4 | −0.475 | no | 0 |
| 5 | 2 | 463 | 2 | 2 | −0.090 | **yes** | 0 |

The cleanest witness satisfying **every** registered scope pin including p > n (true at all prize rows): **n=32, r'=6, w=3, p=47, delta=2**, S = {0,6,14,23,24,31} against ζ = y in F_47[y]/(y²+y+46). Sub-balance decided by **exact integer comparison**: C(32,6) = 906192 < 47⁴ = 4879681.

`es_witness.py` rebuilds each field from scratch, proves the modulus irreducible, proves ord(ζ)=n exactly, evaluates the power sums, and proves non-periodicity — sharing no code path with the census that found them.

**Catch on my own first attempt (worth recording):** the initial witness script failed to reproduce. The cause was real, not cosmetic — the census decides "*some* prime above p contains every x_s", which pins a particular primitive n-th root; with ζ fixed the witness is a **dilate** cS (the Galois action). The script now searches dilates and pins the exact (field, ζ, set) triple. Failure for *every* dilate would have fired falsifier F3; it did not.

**The qualifier that decides campaign impact.** There are two inequivalent balance functionals in play, and my witnesses fall exactly between them:

- **per-weight** (round-15's own, `notes/pilots_20260804/mun_anticoncentration/PREREG.md:106-107`): "Define the equidistribution exponent `Lam(w) := log2 C(n, r') - |Z_w| * log2 p`" — and its measurement setting, `verify_fourier.py:247`: "balance point: the p at which the heuristic C(n,r')/p drops below 1".
- **global** (the floor node's, `critical/nodes/u2c_giant_tnull_dichotomy/node.json:10`): "Pre-registered: sub-balance (**q^t >= 2^n**) scaled rows with non-coset-union extras…".

Global ⟹ per-weight, strictly. **0 of my 5 witnesses are below the global boundary.** So:

- (ES) in the **per-weight** reading — the reading in which round-15 registered Lam and measured the suppression banked as "evidence FOR (ES) with margin" — is **FALSE**.
- The **HARDENED floor** `u2c_giant_tnull_dichotomy` is **NOT refuted**; its own falsifier explicitly excludes what I found.

**And the faithful crossing shape is clean.** At the scaled crossing row r' + w = n/2, i.e. (n=32, r'=8, w=8): all C(32,8) = 10,518,300 subsets in 21,283 orbits, exhaustive **over all characteristics** — **zero accidents of any kind**, in-scope or not. Mechanism: gcd(N(x₁),N(x₂)) = 1 for essentially every orbit, matching the banked F2-A2 finding "the multi-condition ideals are generically coprime".

## 2. C2 — THE CURVE: the "1-2 orders EARLY" margin **decays and crosses zero**

Exact (not fitted, not swept): the largest characteristic carrying an accident vs the balance point, in round-15's own setting (w=2, delta=1, so `|Z_w|`=1 and p_bal = C(n,r') exactly):

| row | largest accident p | balance p | orders early |
|---|---|---|---|
| n=16, r'=3 | 17 | 560 | 1.52 |
| n=16, r'=8 | 577 | 12870 | 1.35 |
| n=32, r'=4 | 7937 | 35960 | 0.66 |
| n=32, r'=6 | 665857 | 906192 | **0.13** |
| n=32, r'=5 | 161761 | 201376 | **0.10** |

The banked "1-2 orders EARLY" (`FABLE_AUDIT.md:38-40`) reproduces **only at n=16**. It shrinks to ~0.1 orders at n=32 and, once w ≥ 3, goes **negative**. I therefore **decline to fit a decay law with the boundary as a fitted parameter**: the measured margins do not support one, and manufacturing a fit here would be exactly the "evidence dressed as proof" my pre-registration forbids. This is a **null on C2's fitted-curve sub-goal**, reported as a null.

Two-point scaling (n=16 clean, n=32 violated) cannot distinguish O(log n) from Θ(n) growth of the violation depth — my registered prediction H is therefore **half-scored**: existence of shallow sub-balance accidents **confirmed**; the scaling claim **unresolved**.

## 3. C3 — THE BOUNDARY: the known witness is **not** extremal

- **n=16 is completely clean**: over all r', all w, and **all characteristics**, zero sub-balance accidents; minimum margin **+1.74 bits**.
- Minimal above-balance accident: **Lam = +0.103** (n=32, r'=5, w=2, p=433, delta=2).
- Deepest sub-balance accident: **Lam = −8.284**.
- Accidents switch on/off inside a narrow band around Lam = 0, roughly **[−8.3, +0.1] bits** — the boundary is *thin*, not a cliff.
- The banked above-balance witness (q=97, n=32) is **sharpened, not extremal**: same row carries accidents at p up to **665857**, three orders beyond it.

## 4. C4 — Structural regularities (candidate lemmas for the transfer pilot and mint-4)

**(C4-a) THE STRATUM MECHANISM — the deep violations are a *mis-specified codimension*, not a conspiracy.** If T is a union of μ_{2^a}-cosets with 2^a < M, every odd-index window condition holds *for free*, and the surviving conditions reduce to a strictly smaller instance at n/2^a. The per-weight Lam then **over-counts** the constraint. Both deep witnesses are of this kind and are comfortably **above** balance on their own stratum:

- (r'=6,w=4,p=7): Lam = −8.284 but **Lam_a = +3.515** at a=1
- (r'=6,w=4,p=17): Lam = −0.648 but **Lam_a = +5.042** at a=1

Candidate lemma: *balance must be imposed stratum-by-stratum, a = 0 … log2(M)−1; the binding stratum is not always a = 0.*

**(C4-b) Stratification repairs only 2 of 5.** The remaining three are generic (a=0) and shallow (|Lam| ≤ 2.43, i.e. expected counts 0.19, 0.72, 0.94) — ordinary Poisson fluctuation at the boundary. No stratification removes them; they simply show a heuristic is not a theorem near its own boundary.

**(C4-c) Generic coprimality is the real suppressor.** Accidents require the ideals (x_1,…,x_{w-1}) to share a prime; for w ≥ 3 the gcd of norms collapses to 1 for almost every orbit. This — not entropy — is why the crossing shape is clean over all p, and it is the structural reason suppression beats the entropy prediction wherever it does.

**(C4-d) delta > 1 residual for the prize rows.** The banked Lambda uses `|Z_w| >= w-1 with equality iff delta = 1`. At delta ∈ {2,4} the prize-row balance status depends on the **actual** cyclotomic-closure size, not the bound: `verify_rows.py` reports `Lambda(2^34) = -2.1977e+12 bit` for a 256-bit prime (delta=1, deeply sub-balance) but `Lambda(2^34) = +1.4943e+12 bit` at the small-q_char end. Recommend the coordinator re-check, per lane, which reading each row actually satisfies using the true |Z_w|.

## 5. Subtraction (hard law 5) — what is NOT mine

The prior-art sweep came back with three hits I must concede:

- **The norm floor (my registered M3) is BANKED, and I withdraw the novelty claim.** `notes/U1_OFFICIAL_ROW_NORM_GATE_TABLE.md:19-31` (NG1/NG2); the Parseval+AM-GM sharpening verbatim at `notes/pilots_20260802/c1_norm_ladder/REPORT.md:52` ("**LEMMA B (AM-GM ceiling)** … AM-GM => **maxnorm(N,w) <= w^(N/2)**"); PROVED node `background/nodes/dli_c1_ternary_relation_norm_sandwich`. Mine adds only residue degree delta > 1 and the multi-condition window. It held at all 288 accidents tested (T5) and is reported as verification, not discovery.
- **Bad-prime census by resultant factorization is BANKED AND PROVED** for a different object: `background/nodes/dli_wcl_weight3_ambient_exclusion/proof.md:17-33`, `…weight4…`. The method is not new; its application to the (ES) object, exhaustively over all p, is.
- **LEMMA Z is the PROVED node** `critical/nodes/b1_char0_giant_coset_theorem` — cited, not re-derived. (This also re-confirms CATCH-15A.)
- Prior MITM sub-balance censuses with extras classification already exist (`critical/nodes/u2c_giant_tnull_dichotomy/notes/f2a1_subbalance_sweep_modal.py`).

What is new: the exhaustive-over-all-p census on the (ES) object, the two-readings separation, the five witnesses, the stratum mechanism, and the clean crossing-shape result.

## 6. Honest residuals

- **Scale gap.** Reachable n ∈ {16, 32}; the prize row is n = 2^41. My deepest violation is −8.28 bits against a prize-row per-weight margin of −2.2e12 bits. **Nothing here shows the violations scale**, and I claim no extrapolation.
- **Coverage gap.** Exhaustive over all p only for r' ≤ 6 at n=32 (plus r'=8 at w=8). **r'=7 and r' ∈ [9,16] were not covered** — that run hit the 5-minute wall twice (`census_n32_7_8.log` records it). **n=64 was registered in my grid and never executed.** A null from an unreached regime is not evidence.
- **Shape gap.** Census rows sit at rho = r'/n ≤ 0.25; prize rho ≈ 0.49 (crossing) and 0.75 (band). Only r'=8 approaches the crossing shape.
- **p gap.** Witness primes are 7…463 vs prize p ≥ 2^63.97; three of five have p < n (flagged per witness, never silently).
- **Unresolved reference.** The "four proved structural constraints" cited at `FABLE_AUDIT.md:48-51` **could not be located anywhere in the repo** — the round-15 REPORT was never persisted, so my registered pruner (b) was unusable and I substituted my own. That list should be reconstructed or retired.

## 7. Recommendation to the coordinator (re-pose, not mine to make)

(ES) must be re-stated with its balance functional pinned. The per-weight form is refuted; the global form (2^n ≤ p^{|Z_w|}) survives everything measured, and the four consuming lanes should each be checked against **that** form using true |Z_w| — plus the stratified condition of C4-a, which the per-weight form silently violates.
