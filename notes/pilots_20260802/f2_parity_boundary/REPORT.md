# Pilot report: F2A.5b parity boundary (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# F2A.5b — the parity boundary. HEADLINE: parity-inhomogeneity is not merely insufficient, it is the wrong invariant.

## 0. The exact law the hypothesis must be written in

Validated 8/8 exactly (`F2A5B_VALIDATION_ALL_PASS`, replayable under `tools/ramguard local`). With `base = SUM_i sigma_i^-`:

```
V_b = (1/2p) SUM_{k odd} hhat_p(k) . omega^{k.base} . e_b(omega^{k Delta_1},...,omega^{k Delta_n})      (P1, exact in Z[zeta_p])
```

so the whole b-resolved object is the elementary symmetric polynomials of the **k-th power phases of the Delta multiset**. Two exact specialisations:

- **k = p is a Krawtchouk number**: `e_b(omega^{p Delta}) = [z^b](1-z)^{n_o}(1+z)^{n_e}`, contributing exactly `(-1)^base.Kr(b)/p` (B3). beta_min is *only* the k=p shadow.
- **Cauchy exponent** (B6, 1500 rows): `|e_b(omega^{k Delta})|/C(n,b) <= kappa(n,b).2^{-n.Lambda_k(beta)}`, where
  `Lambda_k(beta) = -(1/n).max_psi SUM_i log2(|1+r e^{i(theta_i+psi)}|/(1+r))`, `r = beta/(1-beta)`, `theta_i = pi.k.Delta_i/p`.
  `Lambda_k >= 0`, `= 0` iff mode k is slice-dead. The max over psi is forced — it is the phase-SPREAD constraint made into a functional.
- **Fourier surrogate** (B7): `Lambda_k >= beta(1-beta)(1-|R_k|)/ln2` with `R_k = (1/n)SUM_i omega^{k Delta_i}`, and `|R_p| = 1 - 2 beta_min`.
- **Certificate** (B8, sound on 232 rows, median slack 3.9 bits): `-log2 rho_b >= n.min_k Lambda_k - log2 M_p - log2 kappa(n,b)`, with `M_p = (2ln2/pi).log2 p + 0.96257` **exact to 1e-4** (so the official-scale value `log2 M_p = 3.87 bits` extrapolates a known asymptotic, not a trend).

## 1. THRESHOLD vs CONTINUOUS — verdict: CONTINUOUS (F1 fires)

The exact death criterion does flip instantly — k=p is slice-dead iff all Delta_i share a parity, so **one minority coordinate breaks slice-death exactly**. The *exponent* does not jump:

At n=96 the measured exact exponent **equals the k=p Krawtchouk floor** to a median of **0.005 bits (p=23), 0.007 (p=41), 0.017 (p=101)** for beta_min <= 0.13. Below the crossover, the k=p mode *is* the entire slice statistic. Each added minority coordinate buys exactly **1 bit** at the adversarial slice beta=1/4 (floor 1/p -> 1/2p -> 1/4p ...). Saturation onto the generic band only at beta_min ~ 0.25-0.29.

Exact exponent `lambda(beta_min, beta=1/4)`, n-stable to 3 decimals from n=256 to 2048:

| beta_min | 0 | 1/64 | 1/32 | 1/16 | 1/8 | 3/16 | 1/4 | 1/3 | 1/2 |
|---|---|---|---|---|---|---|---|---|---|
| lambda | 0 | .0162 | .0337 | .0751 | .1782 | .2539 | .3112 | .3663 | .4054 |

Closed form (B5, agrees to 4e-16): `Lambda_p = beta_min.log2(1/|1-2beta|)` while `1-2beta_min >= s/(1-s)`, else `(H(beta_min) - 1 - log2(1-s))/2`, `s = 2beta(1-beta)`. **A qualitative "not parity-homogeneous" clause is worthless; the clause must be quantitative — and its functional form is exactly known.**

## 2. NEW KILLER CLASSES — F2 fires maximally

**The adjacent-pair window.** Take the ~p-2 coordinates with Delta = a and the ~p-2 with Delta = a+1. It is **perfectly parity-balanced (beta_min = 0.5000, the maximum possible)** and has **rho_b = 1 exactly — eta = 0.000000 — at every prime 23...151 and every n up to 192** (exact integers, `arcscale_model.json`).

- **Universal, not accidental**: exhaustive over *every* frequency c in F_{p^2}* at p = 11,13,19,23,31 — **1768/1768** viable frequencies carry such a window, all with beta_min = 0.5000 and worst-slice eta = 0.000000.
- **Realisable at any scale**: the Delta multiset takes exactly p-1 distinct values with multiplicities exactly {1,...,p-1} (exact, p = 11...199, both frequencies). Adjacent-pair windows of size 43 (p=23), 199 (p=101), 394 (p=199) ~ 2(p-2).
- **Not a proxy artefact**: exact Z[zeta_p] with true weights `2cos(pi s/p)` gives -log2 rho = **0.00000** for `adjacent_pair`, `arc2`, `arc3`, `coset_trivial` at p = 11,13,19,23.
- **Never recovers**: at p=101 eta = 0 to n = 2048 and eta ~ 3e-5 at n = 65536 (6.4p^2). Asymptotically eta_inf ~ 0.33/p^2 — at official p ~ 2^31 that is ~7e-20. **This class clears no budget at any window size, ever.**
- Companions, all with beta_min up to 0.5: `coset_trivial` (all Delta equal -> rho_b = 1 at *every* b, exactly, true weights), `arc3/5/9/17`, `adjacent_triple`, `fewvalue_top2/top4`. At p=101 every one of these gives eta = 0.0000 at n <= 64 while the k=p parity floor claims 19-36 bits — **the parity clause is wrong by 25+ bits.**
- **Adversarial climb** (exact integer objective): from random/generic starts it drives -log2 rho 12.1->4.4 and 10.5->2.1 at n=32, always into beta_min ~ 0.44-0.50. Calibration passes: it cannot improve the all-odd killer (4.12->3.59) and cannot escape the adjacent-pair optimum (0.000->0.000).

## 3. THE BOUNDARY MAP — which dial actually works

761 exact windows at (p=23,n=48) and (p=41,n=48), lower envelopes:

| dial, restricted to | min eta (p=23) | min eta (p=41) | verdict |
|---|---|---|---|
| beta_min >= 0.25 | 0.00147 | **0.000000** | useless |
| beta_min >= 0.45 | 0.00147 | 0.00121 | useless |
| 1 - max_k\|R_k\| >= 0.10 | 0.0300 | 0.0252 | usable |
| 1 - max_k\|R_k\| >= 0.30 | 0.1114 | 0.0938 | usable |
| n.min_k Lambda_k >= 8 | 0.1883 | 0.1860 | usable, tight |

eta collapses onto a universal function of `flat := 1 - max_k|R_k|`, independent of p and n (arc-w families at different primes with matching flat give matching eta). **And the surrogate is asymptotically sharp, not just a bound**: eta/flat -> 0.2705 = beta(1-beta)/ln2 at beta=1/4 — measured **0.2685 (p=23, n/p^2=124) and 0.2641 (p=41, n/p^2=39)**, ratios 0.993 and 0.976.

## 4. RECOMMENDED HYPOTHESIS CLAUSE — **DRAFT, for the coordinator's theorem statement, not for minting**

> **(H-spread)** Let `Delta_i = sigma_i^+ - sigma_i^- in Z/2p`, `omega = e^{i pi/p}`, and for a slice fraction `beta = b/n` put `r = beta/(1-beta)`. Say the window is **eta-spread at b** if
> ```
> min_{k odd, 1 <= k < 2p}  Lambda_k(beta)  >=  eta,
> Lambda_k(beta) := -(1/n).max_{psi in R} SUM_i log2( |1 + r.e^{i(pi k Delta_i/p + psi)}| / (1+r) ).
> ```
> Then `-log2 rho_b >= n.eta - log2 M_p - log2 kappa(n,b)`, with `M_p = (1/2p)SUM_{k odd}|hhat_p(k)| = (2ln2/pi)log2 p + 0.9626 + o(1)` and `kappa(n,b) = (1+r)^n r^{-b}/C(n,b) = O(sqrt n)`.
>
> **(H-flat)**, the checkable surrogate: it suffices that `max_{k odd} |R_k| <= 1 - eta.ln2/(beta(1-beta))`, where `R_k = (1/n)SUM_i omega^{k Delta_i}` is the empirical Fourier coefficient of the Delta multiset at frequency k. Parity-inhomogeneity is exactly the single frequency **k = p** of this condition (`|R_p| = 1 - 2 beta_min`), and is therefore necessary but very far from sufficient.

Three structural notes for the drafting: (i) `Lambda_k` is rotation-invariant by construction, satisfying the F2A.5 phase-SPREAD constraint; (ii) the condition is **not uniform over odd k** — mode k=1 carries O(1) mass `(1/2p)|hhat_p(1)| ~ 2/pi`, versus 1/p for k=p, so a near-dead k=1 is ~p times more damaging than a dead k=p; (iii) there is a hard ceiling `Lambda_k <= Lambda_max(beta) = log2(1/max(beta,1-beta))`, so **no window whatever** reaches eta=1/3 outside beta in [0.2063, 0.7937], or eta=1/43 outside beta in [0.01605, 0.98395].

## 5. MARGIN TABLES

**Parity clause alone** (exact Krawtchouk, model-free, so official scale carries no proxy): largest n at which the k=p floor still permits the budget.

| beta_min | p=23: n(1/3) / n(1/43) | p=101 | OFFICIAL p~2^31 |
|---|---|---|---|
| 0 | 14 / 195 | 20 / 286 | **93 / 1333** |
| 1/64 | 14 / 637 | 21 / 938 | 98 / 4365 |
| 1/32 | 15 / inf | 22 / inf | 103 / inf |
| 1/8 | 29 / inf | 43 / inf | 199 / inf |
| 1/4 | 201 / inf | 296 / inf | 1380 / inf |
| >= 0.28 | inf / inf | inf / inf | inf / inf |

Exact thresholds: **1/3 needs beta_min >= 0.27686; 1/43 needs beta_min >= 0.02197.**

**Flatness clause.** 1/43 needs `flat >= 0.0860` (asymptotically sharp). 1/3 needs `min_k Lambda_k >= 1/3` against the ceiling `Lambda_max(1/4) = log2(4/3) = 0.41504` — i.e. the window must be within **80.3% of the absolute maximum**. Empirically at n=48: only **15.4% (p=23) / 15.8% (p=41)** of 761 windows clear 1/3; even at flat >= 0.60 the worst is eta = 0.257/0.246, still below 1/3. For 1/43, **97.7% / 94.9%** clear.

Startup deficit any certificate must overcome: 4.98 bits (p=23) -> 5.47 (p=151) -> **8.99 bits at official p and n=1024**.

## 6. FALSIFIER VERDICTS

- **F1 — FIRES.** Continuous, no usable threshold; but the functional form is exactly known (Krawtchouk / two-branch closed form above), so a quantitative clause is both required and writable.
- **F2 — FIRES, maximally.** A non-parity killer exists at **beta_min = 1/2 exactly** with **eta = 0 exactly**, at 100% of frequencies, confirmed with true weights, and it never recovers at any n. Parity-inhomogeneity alone is not merely insufficient — it is off by 25+ bits and mis-ranks the windows.
- **F3 — FIRES for 1/3, NOT for 1/43.** Under `flat >= 0.30` the worst window still gives eta = 0.094 (4x the 1/43 budget, 0.28x the 1/3 budget). Under the *parity* clause alone F3 fires for both budgets. So the theorem shape survives only if (a) the hypothesis is (H-spread)/(H-flat), and (b) the normative budget is 1/43 rather than 1/3 — PP5.0 is now load-bearing on which.

## 7. FILE INVENTORY (all under `notes/pilots_20260802/f2_parity_boundary/`)

Code: `boundary.py` (the exact law, Lambda/R/kappa/M_p, Krawtchouk, window constructors) . `verify_boundary.py` (B1-B8, ALL PASS) . `experiments.py` (stages `ramp|killers|climb|flatscan|margin|arcscale|arcsynth|weight|census`) . `thresholds.py` . `sharpness.py` . `reach_census.py` . `analyse.py` . `probe0.py`, `probe1.py` (recon).
Results (18 JSONs in `results/`): `ramp_p{23,41,101}.json` . `killers_p{23,101}.json` . `flatscan_p{23,41}_n48.json` . `arcscale_{model,synth}.json` . `reach_census.json` . `delta_multiplicity_law.json` . `margin_{lambda_p,parity_sharpness,arc}.json` . `thresholds.json` . `sharpness.json` . `true_weight_killers.json` . `climb_p23_n32.json`.

## 8. CAVEATS

- **Proxy scope.** Cancellation *magnitudes* at scale ride the balanced-weight integer proxy `V_b` (carry and cosine signs exact via sigma; only |2cos| magnitude set to 1), inherited from F2A.5. The **killers are proxy-independent**: `coset_trivial`, `arc2/3`, `adjacent_pair` give -log2 rho = 0.00000 in exact Z[zeta_p] with true weights (n <= 12, p <= 23). The structural laws (P1, the Krawtchouk identity, hhat_p(p)=2, the Cauchy bound, the death criterion) are weight-general.
- **Extrapolation.** Measured p <= 151 (structure to 199); true weights p <= 23, n <= 12. Official p ~ 2^31 enters only via (a) the exact Krawtchouk floor, which needs no model, and (b) `M_p`, whose slope 2ln2/pi is analytic (residual 1e-4). The claim that the adjacent-pair killer persists at official scale rests on the exact multiplicity law {1,...,p-1} verified to p=199 and on the n >> p^2 scaling measured to n/p^2 = 124.
- `Lambda_k`, `|R_k|`, `certified_bits` are float diagnostics (labelled everywhere); every banked exponent is exact-integer-derived.
- The adversarial climb is a weak local search (25 iterations, 4x12 neighbourhood); it establishes that beta_min-fine minima are easy to reach, not that eta = 0 is the global optimum — though `adjacent_pair` already attains the absolute optimum rho = 1.
- Single descent j = 1, q = p^2; tower functoriality untested. PP5.0 and the F2A.1 seam remain the unproven upstream gates — nothing here is mintable.
