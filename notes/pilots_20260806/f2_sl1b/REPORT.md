(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# SL-1b — REPORT (round 16, pilot `notes/pilots_20260806/f2_sl1b/`)

**Verifier:** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/f2_sl1b/verify.py`, stages S0-S9, **37/37 PASS**, exit 0, digest `F2_SL1B_ALL_PASS`. Log: `.../f2_sl1b/results/VERIFY_LOG.txt`. Proofs: `.../f2_sl1b/PROOFS.md`. Registrations appended to `.../f2_sl1b/PREREG.md` before any computation. Run under `tools/ramguard local`; no file outside my directory was written.

## The target, verbatim (first reported item)

`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:316-319`:

> **SL-1b (the named residual, replacing SL-1 on the obligation list):** prove a **lower** bound `dim_{F_p} L >= m · log_p 3` (or a second-moment / anti-concentration step for `Z(L)`). This is a counting statement about the deployed `L`; SL-1 (distance) is now discharged and is not the obstruction.

**DEFECT-1 (the pre-registered ambiguity clause fires).** PROOFS.md:316-319 asks for an inequality; PROOFS.md:298 attaches a *conclusion* to it (`L^perp ∩ T = {0} iff ... d >= m · log_p 3 <-- existence`). These are two obligations, and they come apart:

- **(R-A) literal** — `dim_{F_p} L >= m·log_p 3`.
- **(R-B) intended** — `L^perp ∩ T = {0}` for the deployed `L`, which is what (O1) at rungs 14-16 needs.

**DEFECT-2.** The audit gloss ("the base-3 first-moment threshold, exactly `log2 3` from LEMMA 3's", `FABLE_AUDIT.md:19-22`) has the right ratio but mis-describes the object: PROOFS.md:296-299's two lines carry *different conclusions* (`E[Z]=O(1)` vs `L^perp ∩ T = {0}`), not one conclusion at two constants. PROOFS.md governs, as instructed.

## B3 (counterexample search — run first, as mandated) — VERDICT: falsifier S-F2 FIRES

Grid pre-registered before computing: `p ∈ {3,5,7,11,13,17,19}`, `n` even `≤ 48`, `k = ord_n(p) ≤ 3`, `m ≤ 12` (`≤ 10` for the ternary sweep), `R ≤ 8`, shifts `a ∈ {0,1,2}`, windows `mu_n` and `{x : ord x = n}`. **1060 configurations.** All decisions exact — the threshold is tested as the *integer* comparison `p^{dim L} ≥ 3^m`, never a float.

- **(S-F1) `dim L < min(m,R)`: never fired** (0/1060). **(S-F3) `dim L > min(m,k|Lambda|)`: never fired.**
- **(S-F2) FIRED, 61 times.** Of 714 configurations with `p > 3` satisfying (R-A), **61 still carry a nonzero ternary dual vector**. Smallest witness: `p=7, k=2, n=12, W=mu_12, m=6, Lambda={5,7}` — `dim L = 4`, `7^4 = 2401 ≥ 3^6 = 729`, minimum ternary dual weight **3**. Every witness respects `wt ≥ R+1`, so **none contradicts THEOREM SL-1**: the distance law holds exactly and the count still refuses to vanish.

Because this overturns a banked measurement, all witnesses were recomputed by a **disjoint code path** (S9: cyclotomic `Phi_n(X) mod p` + polynomial remainder, no field tuples, no generator search). Both routes agree on all 9 checked configurations.

## B1 (prove or refute) — VERDICT: **(R-A) PROVED, conditionally on `t`; (R-B) REFUTED**

**LEMMA SL-1b-DIM (new).** `min(m, R) ≤ dim_{F_p} L ≤ min(m, k·|Lambda|)`, `k = [F_q:F_p]`.

SL-1's own mechanism **does** extend, one square further — from the *distance* to the *rank*. Lower bound: `L^perp = ker_{F_p}(A)`, `A = (y_i^l)`; the `R×R` minor on the consecutive run factors as `diag(y_i^{2a+1}) × Vandermonde(y_i^2)`, invertible by the banked antipodal-fibre argument, so `rank_{F_q} A' = R`; base change (`F_p`-independent ⟹ `F_q`-independent) gives `dim_{F_p} L^perp ≤ m − R`. The `R > m` branch closes via SL-1's `wt ≥ R+1`. **The proof is `k`-free** — it holds over every extension degree. Distinctness of the run mod `n` is free at the official row (`n = 4m`, `R ≤ m`).

**Corollary:** (R-A) reduces to the numerical `ceil(t/2) ≥ m·log_p 3`, i.e. **`t ≥ 2m·log_p 3 = 0.102292984·m`**.

**Why the round-15 pilot missed it:** it had the *upper* bound and used it (`f2_opening/PROOFS.md:330`; `f2_sl1_powersums/verify.py:1044`, verbatim `cond_max = min(m_j, t) * log2p       # dim L <= min(m, 2R) ~ min(m,t)`) and never had the lower one. That asymmetry is the whole gap.

**(R-B) is REFUTED.** PROOFS.md:298's "iff" is derived *for a uniformly random subspace* (PROOFS.md:287-288) and is not a property of any particular one. Abstractly: `L^perp = span{(1,1,0,…,0)}` gives `dim L = m−1` satisfying (R-A) with room while containing a ternary vector — checked exactly at `(p,m) = (5,4), (7,4), (11,3)` and at the **official prime** `p = 2^31−2^24+1, m = 4`. Concretely: the 61 deployed-family witnesses. **Proving SL-1b as stated does not discharge (O1).**

## B2 (sharpness) — VERDICT: both bounds sharp; the constant cannot be improved

- **Lower bound attained.** When `k = 1` (`n | p−1`), `A` has entries in `F_p` and only `R` rows, so `dim L = min(m,R)` **exactly** — verified on **all 131** `k=1` rows, no exception.
- **No-go corollary.** Any proof using only `f2_opening`'s hypotheses (`n` even, `W` antipodally closed, `Lambda` a consecutive odd run) cannot conclude more than `dim L ≥ ceil(t/2)`. So **`t ≥ 2m·log_p 3` cannot be relaxed to `t ≥ m·log_p 3`** without importing information about `k`. The factor 2 is the truth on a nonempty family, not slack.
- **Upper bound attained** in 557/855 rows with `k ≥ 2`; 181 sit strictly interior. `dim L` genuinely ranges over the whole interval.

## B4 (discharge-chain consequence) — the obligation list shortens in name only

Per rung, `k`-free lower bound deciding (`m_16 = 2^38`):

| `t` | rung 14 | rung 15 | rung 16 |
|---|---|---|---|
| `7e10`, `2^36`, `2^41/log2 p` | PROVED (9.8-10.1x) | PROVED (4.9-5.0x) | **PROVED (2.44-2.52x)** |
| `t* = 8,592,912,739` | PROVED 1.222x | OPEN 0.611x | REFUTED 0.306x (`k≤3`) / OPEN (tower) |

Under `m_16 = 2^39` the margins halve (worst `PROVED` cell 1.222x) and `t*` degrades one rung further.

**Net effect on the chain:** SL-1b is discharged as stated at rungs 14-16 under the three large-`t` readings — but it is **non-load-bearing**, because (R-A) ⇏ (R-B). Mystery 2's obligation list shortens **in name only**. What genuinely survives is a *consistency check now proved rather than assumed*: the deployed `L` clears the base-3 first-moment threshold by a factor 2.49 in the exponent at rung 16, i.e. it is no worse than a random subspace at this statistic.

**One real gain:** LEMMA 3's proved *necessary* condition (`dim L ≥ m/log2 p`) is now **verified from below** (`3.44e10 > 8.87e9` at rung 16) under the three large-`t` readings — previously the repo could only note that its upper bound had not yet fallen below the requirement, which fails to refute LEMMA 3 but does not verify it.

**Renamed residual — SL-1b′:** at rungs 14-16, bound the ternary mass of the *deployed* alternant code, `Z(L) ≤ 2^{o(m)}` (equivalently `L^perp ∩ T = {0}`). `dim L` is now known to within `[ceil(t/2), min(m, k·ceil(t/2))]` and is **not** the obstruction. This is the terminal `f2_sl1_powersums/PROOFS.md:359-364` already named; this pilot's contribution is removing the obligation that looked like a way around it.

## Catches

1. **CATCH-A (code-level, against a banked verifier).** The sole empirical support for the implication I refute is `f2_sl1_powersums/PROOFS.md:320-322` ("the count threshold ... **never under-predicts**"). Its code, `f2_sl1_powersums/verify.py:454`, is verbatim `cond = dL * (p.bit_length() - 1)          # dim L * log2 p (approx)` — `floor(log2 p)`, not `log2 p` (`log2 7 = 2.807` vs `2`). It understates the condition budget by up to 40% on the grid's own primes, biasing toward over-prediction, the very "safe direction" the claim celebrates. Re-evaluated on my witnesses: **61 of 61 false negatives under the predicate as written**, 48 under the predicate as coded. The code does not implement the statement.
2. **CATCH-B (DEFECT-3, arithmetic).** `f2_opening/PROOFS.md:10` fixes `n | p^2-1`; `tower.py:15` fixes `n_j = 2^{24+j}, q_j = p^{2^j}, k_j = 2^j`. Since `v_2(p^2−1) = 25`, `n_j | p^2−1` **holds only at rung 1** and fails at every `j` in 2..16 (verified; LTE re-checked directly for `j = 0..8`). `f2_opening`'s stated setting is a rung-1-only reading.
3. **CATCH-C (uncited cross-lane precedent).** `critical/nodes/dli_prime_weighted_large_block_support/proof.md:18-21` already refuted this exact phenomenon in the DLI lane ("*... even though there is no rank defect*"). No F2 file cites it. Same DLI → F2 direction as round-15's uncited-reduction find. My §4 is the F2 instance of a banked refutation, not a new phenomenon; what is new is the identification, the deployed-family witnesses, and that it kills SL-1b.

## Flagged for the coordinator — do not resolve here (sibling `f2_tq_pin` owns it)

**INTERACTION-1: three banked conclusions rest on the same `k = 2` upper bound and fail together if the tower governs.**

```
k = 2      : dim L <= 8.593e9   <  8.870e9  -> LEMMA 3 VIOLATED (CATCH-4's sign flip)
k = 3      : dim L <= 1.289e10  >  8.870e9  -> no violation
k_16 = 2^16: k|Lambda| = 2.816e14 >> m_16   -> upper bound VACUOUS, none derivable
```

The three are: (a) round-15's **CATCH-4 rung-16 LEMMA 3 sign flip** (`PROOFS.md:391`, "VIOLATED, 0.9687x") — its maintainer-level catch; (b) `f2_opening/PROOFS.md:330`'s *"at rungs 15-16 it is forced, since `dim L <= t < m`"*; (c) **my own `t*` refutation at rung 16**. Under the tower, LEMMA 3 at rung 16 under `t*` is neither violated nor satisfied — it is **undetermined**. I take no position on which reading governs. Every `PROVED` cell above is `k`-free and unaffected.

## Honest residuals

- The 61 witnesses live inside the declared box (`p ≤ 19`, `n ≤ 48`, `k ≤ 3`, `m ≤ 10`, `R ≤ 8`). They refute the implication; they are **not** evidence about the official row's `Z(L)`, and no extrapolation is made.
- (R-A) at rung 15 under `t*` (`k=2`) and at rungs 15-16 under the tower is **OPEN**, not decided — the interval `[min(m,R), min(m,kR)]` straddles the threshold. I did not close it.
- SL-1b′ is untouched. This pilot bounds `dim L`; §4 shows no sharpening of a dimension bound can reach the count.
- A recorded **lead, not a claim**: `L^perp = ker_{F_p}(A_{Lambda*})` for `Lambda*` the Frobenius closure, so `dim L ≥ rank_{F_q}(A_{Lambda*})`. Whether that yields a longer *consecutive* odd run depends on the pinned `q`, and gapped minors do vanish in char `p` (`f2_sl1_powersums/PROOFS.md:158-162`), so full rank must not be assumed. Not evaluated.
- No status flip proposed for any minted node. DRAFT ONLY; no commit, no push.
