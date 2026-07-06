# S2: the analytic route corrected — moment transfer + the DYADIC-K compression
# (round S2, self-tennis, 2026-07-07; verifier s2_analytic_route_audit.py ALL PASS)

## 1. CORRECTION (self-found, window-law instance #10): the pinned per-λ display is FALSE

The pinned proof-architecture alternative — "for every λ ≠ 0:
Σ_y log2 cos²(π a_y(λ)/q) ≤ −(256+δ)L + O(log q)", justified by the −2
circle average giving a '100% margin' — is false in the random model
itself. The typical value of the log-sum is −2N, but the TAIL is fat:

>  P_iid( T(λ) ≥ 2^−N(1+δ) ) ≈ 2^−I·N with I ≈ 0.207  (measured; the
>  s = 1/2 fractional-moment Markov bound gives I ≥ 0.1515 with constant
>  E|cos πU|·√2 = 0.9003, and the display needs I ≥ ~1).

At production L = 1 the random model EXPECTS ~2^202 violating frequencies.
The round-3 toy observation (sup T exceeding the uniform bound by 117×) was
this phenomenon, misread as a peculiarity. The '100% margin' compared the
requirement to the MEAN when the enemy is the TAIL. Same lesson as round 6:
a reduction displayed next to a target needs its own falsification pass.

## 2. PROVED (moment transfer): analysis IS counting, in every alphabet

**Lemma (moment transfer).** For every integer s ≥ 1,
Σ_{λ ∈ F_q^L} T(λ)^s = 4^{−sN} · q^L · Σ_{k ∈ [−s..s]^N, A k ≡ 0 (mod q)}
Π_y C(2s, s+k_y).

*Proof.* cos^{2s}(πx) = 4^{−s} Σ_{|k|≤s} C(2s, s+k) e(kx); expand the
product over y, exchange sums, and Σ_λ e(λ·(A k)/q) = q^L·1[A k ≡ 0]. ∎
(Verified EXACTLY at a toy row for s = 1, 2 — zero error; s = 1 is the
pinned D2=D3 identity.)

CONSEQUENCE: the s-th moment of the Fourier mass is a binomially-weighted
(2s+1)-ary kernel count. Every analytic handle on near-peak λ (Markov on
any moment) is exactly a bounded-alphabet kernel-counting statement, and
conversely. **A2/R-bound and zone (b) are ONE leaf expressed in different
alphabets; there is no purely analytic escape.** The 'analytic route
subsuming (b)+(c)' was an illusion of notation.

## 3. The DYADIC-K compression (re-posed target — subsumes M AND R)

**Hypothesis DYADIC-K(K, j₁):** for every admissible row and every j ≥ j₁:
#{λ ≠ 0 : T(λ) ≥ 2^−j} ≤ K · q^L · P_iid(T ≥ 2^−j), where P_iid is the
iid-uniform model, and the top range j < j₁ carries no λ at all (dual
near-peak emptiness — the dual analogue of zone (b), to be priced by a
transference/dual-counting argument, NOT assumed silently).

**Theorem (compression; elementary given the hypothesis).** DYADIC-K(K, j₁)
with the top range empty implies Σ_{λ≠0} T(λ) ≤ 2K · q^L · E_iid[T] =
2K·r (E_iid[T] = 2^−N exactly), hence E ≤ 1 + 2K·r per level and

>  Σ_{L=1}^{34} log2 E_L ≤ 34·log2(1 + 2K)  ≤ 100  ⟺  **K ≤ 3.34.**

(The dyadic decomposition costs the factor 2; with the exact integral form
it disappears and the threshold is K ≤ 6.68.) At r < 1 the constraint
loosens level-by-level; 34·log2(1+2K·r_L) ≤ 100 is the exact form.

**Status of the hypothesis.** Measured at a real row (q = 65089, n′ = 64,
exhaustive λ-scan): K ≤ 1.45 at every well-sampled dyadic level (the one
larger ratio, 3.9 at j = 24, is a single signed-shift orbit of 64 λ's
against an iid prediction of 0.26 orbits — Poisson-ordinary). Near-peak
counts are orbit-quantized (all observed counts are multiples of 2N ✓
T is shift-invariant). The census, the exact-E computations, and this scan
are all consistent with K ≈ 1 + o(1) in the bulk.

## 4. What this changes in the campaign

- The node's hypothesis stack compresses: {M-bound ∧ R-bound} →
  **DYADIC-K(≤ 6.68) + dual-top emptiness** — one measurable constant plus
  one dual-window statement. The norm-sieve theorem (S1) makes the PRIMAL
  low-weight side unconditional in its covered zone; by moment transfer the
  same sieve applies per-alphabet to each moment's kernel (alphabet 2s+1,
  window rescaled) — sieve-coverage tables for s ≥ 2 are computable with
  the same code.
- The refutation surface for the self-adversary (and Pro): exhibit a row
  with a dyadic level j ≥ j₁ where near-peak counts exceed K× iid by an
  orbit-robust margin (not one Poisson orbit), or a top-range λ (a dual
  short vector) at a balanced row — the dual analogue of the round-5
  engineered prime. NEXT ROUND (S3): attempt exactly that dual engineering;
  if it succeeds, price it; if it fails structurally, extract the dual
  transference lemma that blocks it.

Verifier: s2_analytic_route_audit.py (ALL PASS: Markov constant exact;
Monte-Carlo tail; production violator count 2^202; real-row dyadic table;
moment-transfer identity exact at s = 1, 2).
