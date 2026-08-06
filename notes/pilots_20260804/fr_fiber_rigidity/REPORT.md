(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

All four verifiers reproduce clean (47,111 + 1,716 + 36 + 8 runs, zero failures). Re-read the ask; pre-registration pre-dates every run. Reporting.

**VERDICT: (FR) is REFUTED as stated.** Pre-registered falsifier FR-F1 fired with an explicit, fully-audited witness. My pre-registered prior (P5) was confirmed. The counting consequence, however, survives — that is the useful half.

---

## 1. New proved structural layer (47,111 exact checks, 0 fail)

Reconstructing the lane's algebra from `(AD1)`–`(AD7)`, `(PP1)`–`(PP5)`, `(TKS1)`–`(TKS4)` gave four clean statements, each machine-verified as an *exact polynomial identity* over F_q (not a congruence on H):

- **(II) Master two-ray syzygy.** With `R_nu = C_nu − tau·L_nu` the ray-`nu` residual and `delta = alpha_2 beta_1 − alpha_1 beta_2`:
  `R_2 L_1 − R_1 L_2 = −delta · rho`.
  This is the correct home for the "forced common root" instinct — `rho` is the active defect itself.
- **(A) Self-fiber avoidance.** `B_nu ∩ phi^{-1}(nu) = ∅` for *every* `nu` in P¹. Equivalently, writing `psi(x) = [E'(x) : −E(x)]`: **`D = {x : psi(x) ≠ phi(x)}`**. Selected blocks are `psi`-fibers, `D`-fibers are `phi`-fibers, and the two maps agree exactly off `D`.
- **(LENS) The selection lens.** `B_nu(tau) = {x ∈ D : tau(x) = W_nu(x)}` with `W_nu = C_nu/L_nu` **independent of tau**, and `W_1 − W_2 = delta·rho/(L_1 L_2)`. The block census is therefore *exactly* an RS_{k−ell} agreement census on `D`.
- **(GATE-r)** `agr(nu) = |Core| + |psi^{-1}(nu) ∩ (H\Core)|`, so the tangent gate at `A = k+h` is precisely `|psi^{-1}(nu)| ≤ r` for all `nu`, tight at the selected slopes.

## 2. The refutation

Smallest boundary shape that can pose the question, **pinned not chosen**: `h=25 → ell=3, r=7, d=18, sigma=0, e=14, t=2`; `k=4, n=3d+k−1=57, q=229, A=29`. Witness block `B₁` has `phi`-fiber profile **(1,2,1,2,1)** — it splits two 3-fibers by 2 points each.

All 36 admissibility clauses pass, including: `D = supp(rho)`; joint core exact at `k+d`; blocks reconstructed from the words; disjoint, size `h−d`; LEMMA A; `z_lambda = 0`; `v ≥ 3`; exactly two live slopes at exact `A`; `dim K_d = sigma+1 = 1`; **the kernel generator verified to be `(Z_D·X³, Z_D)`, so the primitive pair really is `(X³,1)` with `ell = 3`**; and the **tangent gate exhausted over all 230 slopes × 52,360 competitors, max codeword agreement = 29 = A exactly** (tight, not slack).

Crucially `ell = 3 &gt; sigma+2 = 2` and the tail fiber has size `2 &lt; ell`, so the load-bearing exception is **not** invoked — the counterexample sits inside (FR)'s intended domain.

**Exhaustive liveness:** all **1,716** partitions of `D` into two `r`-blocks realise. **1,710 are strong (FR)-violations; only 6 are fiber-rigid** — and those 6 are exactly the packed `(P4F1)` blocks, reproducing `6t = 12`. The only structural quantity that sees the partition is the deficiency rank, and it equals `sigma+1` for every one of them. No PROVED node is contradicted (`T_3 = 25 ≥ T_pack = 9`, `(TKS2)`, `(AD6)`, `(P4F1)`–`(P4F4)` all hold).

## 3. The counting target survives — and the obligation should be re-posed

What `(WTB)` actually consumes is `|Bset|` for a **fixed** `(u,v)`. At a shape with a genuinely 4-dimensional family (`k=7, n=60, q=61`, `deg tau &lt; 4`), across 8 configurations and **58,872 exhaustively enumerated candidate blocks each**, every run gave **1 maximal selected member and |Bset| = 2 ≤ 6t = 12** — with splitting bases yielding splitting blocks and rigid bases rigid ones. Block scarcity is real; it just is not fiber rigidity.

Proposed replacement obligation of record:

&gt; **(BC) BLOCK CENSUS.** For fixed `(u,v,P,Q,D)` at the boundary, `|Bset| = #{(nu,tau) : |{x ∈ D : tau(x) = W_nu(x)}| = r, tau maximal-selected} ≤ X`.

By the LENS this is a punctured-RS list count on the `e = 2r` points of `D` at agreement `r = e/2`, coupled to `agr(tau,w) = k+d` on `H\D` via `(AD4)` — a standard, well-posed object, which (FR) was not. The sharp sub-question: `(WTB)` is non-vacuous only when `|Bset| ≪ 2|Tau|`, i.e. only under **block reuse across targets**. My toys all have `|Tau| = 1`, so reuse is exactly what is still unmeasured.

## 4. Flags

1. **Brief-staleness catch** (recorded in PREREG §1 before computing): THEOREM R is *not* "rank deficiency forces a Berlekamp–Massey locator". It states single-word window rank is exactly `d`; BM appears in its proof to **exclude** deficiency via over-agreement. Same class as round 13's catch.
2. **Label collision:** `xr_deficient_window_rational_direction_payment` already uses `(FR)` for a forced-root statement. Suggest `(FIB-RIG)` for the coordinator's conjecture.
3. **Regime caveat (the one place a rescue could hide):** the witness sits *above* the Johnson agreement radius (`A=29` vs `sqrt(kn)≈15.1`); the prize rows sit *below* it. The gate is verified exactly tight, but a prize-regime-only mechanism is not excluded by this pilot.
4. `|Bset| = 2` across 8 runs is **empirical at one shape**, never to be promoted; likewise "1 maximal member".
5. **No status flip proposed.** (FR) dies, the leaf stays TARGET, and `(WTB)` still pays nothing until `(BC)` is settled.

## 5. Files (all writes confined to the pilot dir; siblings read-only)

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/fr_fiber_rigidity/PREREG.md` (pre-dates every run)
- `.../identities.py` + `identities.json` — 47,111 checks, 24 instances
- `.../toy.py` + `toy.json` — exhaustive 1,716-partition liveness scan
- `.../gate.py` + `gate.json` — tangent gate, rigid vs splitting
- `.../witness.py` + `witness.json` — the audited counterexample, 36/36 clauses
- `.../census.py` + `census.json` — `|Bset|` sweep, 8 runs

result: (FR) fiber rigidity REFUTED — an audited, gate-tight admissible pair at the pinned smallest boundary shape (h=25, ell=3, sigma=0, exception not invoked) has a selected block splitting two phi-fibers by 2 points, and 1710 of 1716 boundary partitions realise; but the counting consequence survives (|Bset| = 2 ≤ 6t in all runs), so the leaf's obligation should be re-posed as the well-defined block census (BC) via the newly proved two-ray syzygy R₂L₁ − R₁L₂ = −delta·rho and the tau-independent selection lens.