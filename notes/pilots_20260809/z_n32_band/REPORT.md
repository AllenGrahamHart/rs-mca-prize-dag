# REPORT.md — z_n32_band (round 25) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ab9fe08fa658a522c, 2026-08-09. Pilot: Opus. No edits.

**ROUND-25 PILOT REPORT — Z-CEILING AT N = 32, σ ∈ [−2, 2]**

Registrations appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/z_n32_band/PREREG.md` lines **61–301** (sections Z0–Z6) **before any computation**. All runs via `tools/ramguard local -- python3` from repo root, stdlib only, 1G ceiling never relaxed (the modal profile's RAM was not used). Draft only in my own dir; no node/tool/dag/git writes; no Modal.

---

## 1. THE ALGORITHM (D1) — **BBM, bucket-bisect MITM.** The N = 32 wall is broken.

Round 24's blocker (`.../z_ceiling_assault/REPORT.md:98`): *"N=32 at σ≈0 needs 3^16 ≈ 43M states — out of reach at 1G by any κ."* The wall is **memory**, not arithmetic. BBM removes it without disk and without re-enumeration:

- Coordinates split 16/16, each half into two octets → tables `P`, `Q` of 3⁸ = 6561; `Q` **sorted by residue**.
- Buckets are **contiguous residue intervals**. For a fixed `P`-element, the `Q`-elements whose sum lands in a bucket form **≤ 2 contiguous ranges of sorted `Q`**, found by `bisect`. So the RBUCK bucket passes together cost **one** enumeration, not RBUCK.
- **Half-2's columns are negated**, so the join is plain equality — correctness needs no negation-symmetry theorem.
- κ ≥ 2 uses one SWAR packed add (`s -= (((s+K)&amp;G)&gt;&gt;(W-1))*p`), so multi-row cells cost the same per element.

**Registered cost model vs. measured** (`bbm.py`):

| | registered (Z1.1) | measured |
|---|---|---|
| inner ops/cell | 2·3¹⁶ = 86,093,442 | as designed |
| DPEAK at RBUCK=256 | 168,151 entries | **166,006** |
| wall/cell | &lt; 20 min, &lt; 400 MB | **117.5 s, ~50 MB RSS** (uncontended) |

**P-Z8 HIT with margin.** BBM is ~25× under the RAM ceiling and ~10× faster than the registered bound.

Three brief routes were **priced and rejected in the registration, with reasons** (Z1.0): **(i) RC-aided truncation is unsalvageable** — RC bounds weight from *below*; the mass sits at U ≈ 16 (E[mass at U] = C(32,U)/p), so 90% capture needs W ≥ 18 at cost ~3.5e13, worse than the full MITM. This is a forced correction of the brief's framing. **(ii) orbit quotients** shrink the *output* (~4.3e5 vectors → ~6.7e3 μ₆₄-orbits) but not the intermediate half-sums, which the shift mixes across halves — retained as an invariant (it paid off, §5). **(iv) character sum**: G is constant on μ₆₄-cosets (θ³² = −1), but that is still 1.7e7–2.7e8 terms × 32 cos in-band — rejected, and run only at N ≤ 16.

A late, unregistered bonus finding: UMITM (unbalanced 18/14, no bucketing) is **~12× slower** than BBM at identical asymptotic op count, because random lookups into a 4.8M-entry / 575 MB dict thrash cache. **Bucketing buys speed, not just memory.**

## 2. VERIFICATION

- **`ez.py`: 15/15 escape tests PASS** — EZ2 (BBM ≡ `zcore.tmass_exact` **exactly as Fractions**, 26 cells at N ∈ {8,16}, both families), EZ3 (degenerate identity), EZ4 (TNUM bit-identical over RBUCK ∈ {1,5,64,256}), EZ5 (negation identity), EZ1 (Z-FLOOR, 0 violations over the whole 1305-cell N=16 line), EZ6 (CATCH-Z6, CATCH-19B, RC(i)).
- **P-Z9 HIT**: round-24 record replayed exactly — N=16, p=161761, **TMASS = 159/64, CRATIO = 1.7680688810, NKER = 289**.
- **Four-way agreement at N ≤ 16**: BBM = UMITM = `zcore` (7/7 exact, κ = 1,2,3) and = floating character sum (5/5, rel. err **6.4e-14** at the record cell — matching round-24's 6.5e-14).
- **At N = 32: 33/72 cells re-derived, EXACT integer agreement on TNUM *and* NKER, 0 disagreements**, by BBM-ALT (even/odd coordinate split, RBUCK = 181 — different halves, octets, bucket boundaries and dict contents). Verification ran in **descending-CRATIO order**, so **all 12 leading cells — every cell the verdict rests on — are 2-way verified.**
- **Honest shortfall:** ALG-2 (UMITM) validated at N ≤ 16 but **did not complete a single N = 32 cell** within the wall (15+ min/cell on a box shared with two other round-25 pilots, load ~30 on 14 cores). So 39 of 72 N=32 cells are **single-algorithm**, and the N=32 second algorithm is BBM-ALT, not the fully independent UMITM. The brief's "every cell, two algorithms" is met for 33/72 and for the whole leaderboard, not for the tail.

## 3. THE REACHED GRID (D2) — 72 N=32 cells + 1324 ladder cells

| family | N | κ | cells | coverage | max CRATIO | at p | σ |
|---|---|---|---|---|---|---|---|
| M4 (I2 RSET) | 32 | 1 | **47** | registered Tier-1 sample of ~2.1e7 | **1.4210954721** | 4683696257 | −0.1250 |
| M2 (I1 GRS) | 32 | 2 | 18 | sample (registered 36, stopped at 18) | **1.3887176890** | 63361 | +0.0974 |
| M2 | 32 | 3 | 5 | **EXHAUSTIVE** | 1.0272525997 | 1217 | +1.2527 |
| M2 | 32 | 4 | 2 | **EXHAUSTIVE** | 1.0388843665 | 193 | +1.6302 |
| M4 | 16 | 1 | 1305 | **EXHAUSTIVE** | 1.7680688810 | 161761 | −1.3035 |
| M4 | 8 | 1 | 19 | **EXHAUSTIVE** | 0.9440406977 | 433 | −0.7582 |

Exact rationals at the leaders: `22852627/2²³` (1.4211), `96449299/2²⁵` (1.3887), `22397917/2²³` (1.3428), `37153417/2²⁴` (1.1073). Z-FLOOR holds at every cell.

## 4. THE N-LADDER VERDICT (D3)

**Raw max decays: 1.7681 (N=16) → 1.4211 (N=32). But that decay is NOT significant once M and σ are matched, and the census's own growth law fails.**

- **σ-stratified, M-matched null** (each of my 47 N=32 σ-values matched to a random N=16 cell in the same σ-bin; 20,000 draws): the N=32 max sits at **quantile 0.228** — median null 1.5378, p05 1.2412. **Mild decay, not significant at 5%.** (Plain unstratified null: quantile 0.348.) This matters because my N=32 sample is *designed* (σ-grid + dense σ≈0 cluster) while the N=16 line is every prime.
- **M-normalised N-exponent: −0.026** (2 usable points; N=8's max is &lt; 1 so log₂(MAXCR−1) is undefined there — RC extinguishes the kernel at small N). Round-24's P4a registered window was [−0.30, −0.12]; **−0.026 falls outside it, on the less-decay side.**
- **The variance does decay, significantly**: sd(CRATIO) at N=32 = 0.0694 vs σ-matched N=16 null median 0.1638 — **quantile 0.0000** (below all 4000 draws).
- **That tension is the finding.** The body shrinks; the tail does not. The registered SD-based extreme-value model predicted MAXCR−1 ≈ 0.041 at M=47; measured **0.4211 — 10× too small**. Round-24's P4d extrapolation ("C = 1 + o(1) with grotesque room") is **not supported at N = 32**.
- **Mechanism, from the weight enumerators** (`wenum.py`, AU[U] exact for U ≤ 12): the N=32 κ=1 distribution is a tight body plus rare spikes — median 0.9878, 46 of 47 cells in [0.95, 1.11], one at 1.4211. Typical cells have **UMIN = 11**; both record cells have **UMIN = 9**. The record cell carries AU[9]=128, AU[10]=320, AU[11]=192, AU[12]=704 — weights ≤ 12 alone supply **48% of TMASS−1**. Two weight-9 orbits instead of zero is the whole story. Every exact AU[U] is a **multiple of 64** — the μ₆₄ negacyclic-shift invariant from rejected route (ii), an independent structural check.
- **Heuristic band extrapolation** (registered as heuristic in P-Z4): EVX(47 → 2.1e7) = 2.094 gives an N=32 band max of **1.882 — above N=16's exhaustive 1.7681.** If that extrapolation is right, the N=32 band max *exceeds* N=16's. It is an extrapolation, not a measurement, and it is exactly the direction that would re-open the death question.

**Honest scope.** N=8 and N=16 in-band are exhaustive; **N=32 is a 47-cell sample of ~2.1e7 admissible primes**, so 1.4211 is a *lower bound* on the N=32 band max. κ=3 and κ=4 sub-bands are exhaustive but tiny (5 and 2 cells). No cell anywhere exceeded 1.7681 or 2. **No status flip, no closure, no node edit.** Census evidence is evidence, never proof; the f2 calibration clause binds — every number here is about the **FORM** of Z-CEILING, never about Z₁ at the official row.

**Secondary observation (hedged):** RC's low-weight kill weakens as κ grows at fixed σ — UMIN ≥ p^{2/N} = 2^{2(N−σ)/(κN)}, i.e. 4.02 (κ=1), 2.00 (κ=2), 1.56 (κ=3), 1.39 (κ=4). κ=2 produced 1.3887 from only 18 cells vs κ=1's 1.4211 from 47. Suggestive that κ — the direction of the official row — is a danger axis, but κ=3/κ=4 have too few admissible cells to confirm.

## 5. REGISTERED PREDICTIONS vs OUTCOMES

| | registered | measured | |
|---|---|---|---|
| P-Z1 | Tier-1 max = 1.041, [1.015, 1.12] | **1.4211** | **MISS** (10× in MAXCR−1) |
| P-Z2 | no cell &gt; 1.2 / &gt; 1.7681 / &gt; 2 | 1.4211, 1.3887, 1.3428 &gt; 1.2 | **1st clause FALSIFIED**; 2nd, 3rd HOLD |
| P-Z3 | M-matched ratio ∈ [0.03, 0.30] | **0.787** (&lt; 1, so not death) | **MISS** |
| P-Z4 | band extrapolation 1.097, [1.03, 1.28] | **1.882** | **MISS** |
| P-Z5 | NKER ≈ 431,000 ±20% | 425,089 / 431,425 at σ≈0 | **HIT** |
| P-Z5 | UMIN ∈ [7, 10] | **11** typical, **9** at records | **MISS** (mechanism found, §5 below) |
| P-Z6 | mean CRATIO 1.000 ± 0.010 | **1.00664** | **HIT** |
| P-Z7 | CRATIO(M2,R=4,p=257) ∈ [1.00,1.35] | **0.98912** | **MISS** (low); "&lt; 1.7681" HOLDS |
| P-Z8 | BBM &lt; 20 min, &lt; 400 MB | 117.5 s, ~50 MB, DPEAK 166,006 | **HIT** |
| P-Z9 | N=16 record = 1.7681 at p=161761 | exact | **HIT** |
| grid | T3 = {1153,1217,1409,1601,2113} | exactly that | **HIT** |
| grid | T2 = {193, 257} | exactly that | **HIT** |
| grid | lad16 ≈ 1300 cells | 1305 | **HIT** |
| grid | R=2 band ≈ 130–145 primes | **266** | **MISS** |

## 6. SELF-CORRECTIONS (all plainly)

1. **Route (i) rejected in the registration** — RC bounds weight from below, and the tail *is* the mass. A correction of the brief's framing, made before computing.
2. **T1a's σ = −2.00 anchor was silently dropped** by my own `[2^30, 2^34]` guard (the least prime ≡ 1 mod 64 above 2³⁴ exceeds 2³⁴). Tier 1 is 47 cells spanning σ ∈ [−1.875, +2.000], **not** the full [−2, +2].
3. **R=2 band-size prediction was 2× wrong** — I used 64 rather than φ(64) = 32 in the density. Registered ~130–145; actual **266**.
4. **UMIN prediction missed, and I found the reason**: I used the vector-count threshold C(32,U)2^U ≥ p (→ U ≈ 8.5). Kernel vectors come in **μ₆₄ orbits**, so the right threshold is C(32,U)2^U ≥ 64p → **U = 11**, which is exactly what was measured. The orbit structure I registered as a rejected *route* turned out to set the *answer*.
5. **Tier 4 cut from 36 to 18 cells**, and **UMITM produced no N=32 cell**, both because the box was shared with two other round-25 pilots. Reported as reduced coverage, not papered over.
6. **`analyze.py` gained the σ-stratified null after seeing the first results** — a post-hoc *methodological* correction (my designed sample would otherwise have been scored against an unfair random N=16 subsample). It moved the verdict quantile 0.348 → 0.228, i.e. *toward* decay, against my interest.
7. **The exhaustive κ=2 band (`t4full`, 266 cells) was added post-hoc and is declared as such** in the code; it was never reached.

**Artefacts** (all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/z_n32_band/`): `PREREG.md` (registrations at 61–301), `bbm.py`, `umitm.py`, `wenum.py`, `ver.py`, `ez.py`, `chars.py`, `run.py`, `analyze.py`, `CELLS*.tsv` (1396 cells), `VERIFY.alt.s*.tsv` (33 re-derivations, 0 disagreements), `ckpt/` (1402 per-bucket checkpoint files — every partial run is resumable).

**The single highest-value follow-on** is now the exhaustive N=32 band rather than a wider ladder: 47 of ~2.1e7 κ=1 primes were sampled, the distribution is a tight body plus rare low-UMIN spikes, and the heuristic extrapolation of that tail lands *above* the N=16 record. A UMIN-targeted search (enumerate cells by their weight-9/10 orbit count via `wenum.py`, which is ~3× a full cell) would find the spikes directly instead of waiting for a sample to hit one.
