# Pilot report: C1 imprimitivity attack (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# HEADLINE: THE IMPRIMITIVITY CONJECTURE IS FALSE

The lane's standing next-theorem target is **refuted**, exhaustively, inside its own claimed range.

**maxnorm(2N=64, w=11) = 34 921 634 364 102 721 = 186873311^2, but the conjecture predicts maxnorm(2N=32,11)^2 = 184497889^2 = 34 039 471 045 456 321.** Ratio 1.0259. Here w = 11 <= N/2 - 1 = 15, squarely inside the conjectured range. The argmax has support {0,1,2,6,7,9,11,12,16,17,18} — mixed parity, hence **primitive**. Verified by five independent paths (sympy `resultant`, fraction-free Bareiss, python-int field-norm descent, float DFT product, numpy 3-prime CRT), all agreeing.

Everything below is in `notes/pilots_20260802/c1_imprimitivity/`. Nothing was written outside it; no commits.

## 1. The enabling tool (why any of this was reachable)

The prior pilot quotiented only by `U` (order 2N). The full norm-preserving group `G = <U, Gal>` acts on the **support** of `f` by the affine group `Aff(N) = {i -> u i + c, u odd}`, of order `N^2/2`. Enumerating affine orbit-representatives of supports x all sign patterns (least support index pinned +1) is a **~850x exact reduction**. Calibration: it reproduces the entire published 2N=32 table (all 16 weights) and the 2N=8/16 brute-force tables **exactly, in 1.9 s** (`results/calib.json`, `ALL_AGREE: true`); the covering property was re-checked against brute-force orbit enumeration at N=16,32,64 (`results/validate_reps.json`, 0 uncovered of 300 random subsets per point).

## 2. Exhaustive ladder points (task 2, and well past it)

| 2N | w | polynomials scanned | naive space | maxnorm | law predicts | status |
|---|---|---|---|---|---|---|
| 64 | 8 | 3 176 448 (1 chunk) | 2.69e9 | 217885999165444 | 14760962^2 | **HOLDS** |
| 64 | 9 | 16 832 256 (4 chunks) | 7.18e9 | 1517108809906561 | 38950081^2 | **HOLDS** |
| 64 | 10 | 78 206 976 (2 chunks) | 1.65e10 | 7153912066963204 | 84580802^2 | **HOLDS** |
| 64 | 11 | 316 285 952 (12 chunks) | 2.64e11 | **34921634364102721** | 184497889^2 | **FAILS (1.0259x)** |
| 128 | 2,3,4,5,6 | 12 / 152 / 3704 / 80880 / 1497376 | — | all = maxnorm(64,w)^2 | | **HOLDS** |

Coverage is exact and complete for every row: parts n/n, orbits covered = orbits total, `n_polynomials_scanned == expected`. The assigned target (2N=64, w=8) is **law-confirming**, its argmax is exactly `iota` of the published 2N=32 w=8 argmax. All eight new maxima re-verified by sympy resultant + Bareiss + descent (`results/verify_sympy.json`).

## 3. Where the law actually breaks (task 3)

Exhaustive + certified-witness map at 2N=64 (`results/final.json`):

- **holds** (exhaustive): w = 1...10
- **fails**: w = 11 (exhaustive), 12 (1.2515x), 14 (1.4770x), 15 (1.9148x), 16 (2.8491x) — every witness primitive, sympy+Bareiss+descent verified
- w = 13 resisted two independent hunts (44 618 restarts, two seeds), both reaching *exactly* the law's prediction and 0 beats. Honest anomaly, not a claim.

So the break weight is `w*(8)=3, w*(16)=7, w*(32)=10` — i.e. `N/2 - 1` at N=8,16 but **10, not 15, at N=32**. The "breaks only at w = N/2" premise was an artifact of only ever testing N <= 16.

**New side result:** the break at w = N/2 is now verified at a *third* level — maxnorm(32,16) >= 15 217 367 133 662 920 708 > 2311094272^2 (2.85x), previously known only at 2N=16 and 2N=32.

Low density is safe: hunts at 2N=128 (w=8,9,10) and 2N=256 (w=4,5) all reach the prediction exactly with 0 beats; hunter calibration recovers the true exhaustive maximum at (2N=64,w=8).

**Mechanism.** With `delta = Norm / w^(N/2)`, the law *forces* `delta(N,w) = delta(N/2,w)^2` — the fraction of the AM-GM ceiling must square at every doubling — while a fresh primitive construction at the new level sustains delta roughly constant:

| w | delta(16,w) | law's delta(32,w) | true delta(32,w) |
|---|---|---|---|
| 10 | 0.84581 | 0.71539 | 0.71539 |
| 11 | 0.86070 | 0.74080 | **0.76000** |
| 12 | 0.79628 | 0.63406 | **0.79354** |

## 4. Proof-attack outcomes (task 1) — what died, and two things that survived

- **(a) spectral flatness / majorization: DEAD, with certificate.** At (N=16,w=6) the primitive `f = 1+x-x^4+x^5+x^8+x^9` has Norm 1331714 < 1331716 yet its spectral profile does **not** majorize the imprimitive optimum's. Schur-convexity is strictly coarser than the GM order here, so no majorization argument can work (`results/proof_probe.json`).
- **(b) autocorrelation: TRUE but INSUFFICIENT.** New **Lemma C** (proved, full text in `scripts/theorems.py`): for `f = p(x^2) + x q(x^2)`, `Norm_N(f) <= Norm_M(p p* + q q*)`, and `p p* + q q*` is exactly the even part of `f f*` — i.e. "odd autocorrelation mass only hurts" is literally a theorem. Exhaustively verified over all 3^8-1 ternary f at N=8 (0 violations, 672 equalities). But it cannot close even w=4: `p = 1+y, q = 1+y^7` at M=8 gives `pp*+qq* = 4`, bound `4^8 = 65536 > 38416 = maxnorm(8,4)^2`.
- **(c) local moves: DEAD.** The value function `k -> maxnorm(N,w | k)` (k = min(w_even, w_odd), an affine-orbit invariant) is **U-shaped, not monotone**: at N=16, w=7 it runs 5764801, 2024929, 4255969, 4879681. There are two competing branches (k=0 and k~w/2) that *cross*; no single-step move toward even support can be norm-non-decreasing. At N=16, w=6 the two branches differ by **exactly 2** (1331716 vs 1331714); the true resolution is that one doubling later the branches swap.

Two exact structures banked along the way (both new, both verified, in `scripts/theorems.py`):

- **Rotation identity.** For `f_c = p(x^2) + x^{2c+1} q(x^2)` (ternary of the same weight for every c), `prod_{c=0}^{M-1} Norm_N(f_c) = Norm_M(p^{2M} + q^{2M})`. Proof: for fixed j, `{eta^{j(2c+1)}}` is exactly the root set of `z^M+1`, and `prod(A - zB) = A^M + B^M`. Verified on 120 random (p,q) at M=4,8. Used as a large-move class in the hunter.
- **No flat ternary at weight 4^t** (arithmetic): `f f* = 4^t` forces `(f) = (lambda)^{tN} = (2^t)` since 2 is totally ramified with a conjugation-stable prime, so `f = 2^t.(root of unity)` by Kronecker — not ternary. Hence `c_w < w^2` strictly for w = 4, 16, 64, ... at every level, unconditionally.
- Two small tools: `Norm(f) == w (mod 2)`; and **imprimitive => Norm is a perfect square**, whose contrapositive certifies a primitive argmax from the value alone (e.g. 14760962 = 2.7380481 proves the 2N=32 break arithmetically, with no reference to level 16).

Also resolved from the prior report's caveats: `c_9 = 79` now rests on **two** ladder points, and c_8, c_10, c_11 are new (`c_w = maxnorm(N_0,w)^{4/N_0}`, `results/summary.json`).

## 5. What is NOT invalidated

The minted node `dli_c1_ternary_relation_norm_sandwich` is **untouched**: Lemmas A/A', B, the saturating family {1,2,3,7}, and the unconditional router threshold `q > w^(N/2)` are all still proved, and every one of them was re-exercised here. Only the paragraph under "Explicitly NOT claimed" — which already labels the imprimitivity conjecture a conjecture — now needs a line recording the refutation and the corrected range. That is a coordinator edit; I wrote nothing outside my directory.

## 6. Caveats

- w=13 at 2N=64 is unresolved (two hunts found no beat, but 11, 12, 14, 15 all fail — I expect 13 fails too and the hunter simply missed it). Not claimed either way.
- The 2N=64 failures at w=12,14,15,16 are **lower-bound certificates**, not exhaustions; the exact maxima there are unknown.
- 2N=128 above w=6 and 2N=256 rest on hunts only (consistent with the law, not proof). The hunter is weaker at large N (only ~500-5000 restarts fit the budget); at 2N=128 w=7 and w=9 it reached only 0.51 / 0.65 of the target, so "no beat" there is weak evidence.
- The float-scored scanner is rigorous by construction (exact re-evaluation of everything within 1e-3 in log of the target plus every numerically suspicious candidate), and was cross-validated against the exact-CRT scanner on the full 2N=64 w=8 space (identical max, identical count above threshold).
- `affine_reps` returns a *covering* set of orbit representatives, not exactly one per orbit — sufficient for maximisation, and validated as such.

## File inventory

`scripts/`: `affine.py` (the affine support-orbit reduction, memory-chunked), `scan.py` (exact CRT3 scanner), `scan_big.py` (float+exact scanner for large N), `hunt.py` (primitive-biased hill-climber with the rotation-family move), `calib.py`, `validate_reps.py`, `split.py`, `split_k.py`, `proof_probe.py`, `theorems.py` (**full proof texts of Lemma C, the rotation identity, and the arithmetic tools**), `merge.py`, `summary.py`, `final.py`, `verify_cert.py`, plus five `drive*.sh` chunk drivers.
`results/`: 59 JSON + 38 npy, 5.6 MB. Key files: `final.json` (the status table + break summary), `merged_n32big.json`, `n32/`, `n32big/`, `n64/` (per-chunk checkpoints), `hunt_N*_w*.json` (17 hunts incl. all refutation certificates), `proof_probe.json`, `theorems.json`, `calib.json`, `validate_reps.json`, `verify_sympy.json`, `summary.json`.
