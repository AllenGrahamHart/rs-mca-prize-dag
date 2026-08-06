(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Final sanity check passed: 7,192 real checks / 0 failures, both fail-closed controls exit 1, no writes outside my directory, no REPORT.md, git untouched. (`tail_count/PREREG.md` was already modified before my session — my `find -newermt` outside my dir returns empty.)

---

# ROUND 20 — THE CROSSING GAP: the even-condition route is provably dead, the constant-weight Z-FLOOR exists, and the PT-2 cliff fails on 58% of the live prime range

**Verdict in one line: the round-18 "most obvious next step" (an even-condition SP-COVER) is *impossible*, not merely hard — even exponents are non-units and can never cover `(Z/n)^*`, so **0.00%** of the gap closes; the round-19 adversary's untested cell yields a real new instrument, **THEOREM CW-FLOOR**, which upgrades round 18's heuristic tower-row excess `2^209.0` to a **proved** `2^205.7` but is vacuous at every prime row by 3.85 bits; and the adversarial C3 check **fires** — the PT-2 watch line's 0.336-bit clearance is the value at `log2 p = 256` **only**, and under *every* banked reading the bracket endpoint `w = 2^34` sits **below** the supercriticality threshold on part of the live admissible prime range (57.98% under the ternary functional, 100% under the GLOBAL (ES-G) functional).**

## 0. What was run

All from `/home/u2470931/smooth-read-solomin/prize` under the ramguard law (`tools/ramguard tiny|local -- python3`, literal `--`, every invocation including file patching). Files, all inside my directory:

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_gap/PREREG.md` — coordinator brief + my registrations **G0–G5, appended before any computation**
- `.../crossing_gap/PROOFS.md` — the derivations, with every relied-on statement quoted verbatim at `file:line`
- `.../crossing_gap/cg_arith.py` — stages `rhllb / pt2 / cover / cwfloor / failclosed`
- `.../crossing_gap/cg_census.py` — stages `haar / census / coupled / cwtoy / failclosed`
- outputs `arith_{rhllb,pt2,cover,cwfloor,failclosed}.out`, `census_{haar,census,coupled,cwtoy,cwexhibit,failclosed}.out`

**7,192 checks, 0 failures, every stage exit 0.** Fail-closed proven not asserted: both `failclosed` stages inject a false check and exit 1. No file written outside my directory (`find . -newermt '-4 hours'` outside it returns empty); no `git` write; `gamma_shell/` never read; CAMPAIGN_LEDGER after the ROUND 20 marker never read.

---

## 1. (C1) THE EVEN-CONDITION EXTENSION — formalized, proved, and proved USELESS for the threshold

### The recursion, stated exactly

&gt; **PROPOSITION HT (the 2-adic Haar tower).** With `m^{(a)}_j := #{i in S : i ≡ j mod 2^{m-a}}` and `eps^{(a)}_j := m^{(a)}_j − m^{(a)}_{j+n_a/2}`:
&gt; (i) `S ↔ (eps^{(0)},…,eps^{(m−1)}, r')` is a **bijection**;
&gt; (ii) writing `s = 2^a t` with `t` odd, **`f_S(xi^s) = eps^{(a)}(theta_a^t)`**, `theta_a = xi^{2^a}` of order `n_a`;
&gt; (iii) `strat(S) ≥ b ⟺ eps^{(0)} = … = eps^{(b−1)} = 0`.

This is LEMMA OE stated at *every* level. It makes the recursion exact: **the window condition set partitions by `v_2(s)`**, level `a` carrying the odd exponents `t ≤ (w−1)/2^a` on an alphabet `[0,2^a]` at length `n_a` — precisely LEMMA STRAT's reduction `(n_a, [0,2^a], w_a)` with `w_a − 1 = floor((w−1)/2^a)`, applied to the *folding* of `S` rather than to a periodic `S`. *Machine-verified: 6,802 checks, 0 failures — (ii) for **every** `s ∈ [1,n)` at `(n,p) ∈ {(16,3),(16,7),(32,7),(32,17),(64,5)}`, (iii) **exhaustively** over all `2^16` subsets.*

&gt; **THEOREM SP-COVER-R.** If level-`a` coverage holds — `w ≥ 2^a(w_cov(p,n_a) − 1) + 1` — **and `p &gt; 2^a`** (a new **integrality gate**, absent at `a=0` where it is LEMMA AB(2)) — then `eps^{(a)} = 0` over `Z`, i.e. `S` is **equidistributed** between the two halves of every residue class mod `n_a`.

### CATCH-20B — the extension cannot lower the exclusion threshold. Three proofs.

**(B1) Structural, and decisive.** The `a=0` exclusion *is* `eps^{(0)} = 0`, and by HT(ii) only exponents with `v_2(s) = 0` see `eps^{(0)}`. Even-condition coverage concludes `eps^{(a)} = 0` for `a ≥ 1`, a **counting-balance** condition strictly weaker than periodicity (at `n=8`, `S={0,1,2,3}` has `eps^{(1)} = 0` and `strat = 0`). **No amount of even-condition coverage can produce the exclusion, at any `n`, for any `p`.**

**(B2) Quantitative at official prime rows.** `e=1` forces `n | p−1`, so `delta = 1` at *every* level, every `&lt;p&gt;`-coset is a singleton, and `w_cov(p, n_a) = n_a`. Hence `w_min(a) = 2^41 − 2^a + 1`, minimised at the deepest level `a = 40` at exactly `2^40 + 1` — while every crossing instance has `r' = 2^40 − w ≥ 1`, i.e. `w ≤ 2^40 − 1`. **No level fires at any admissible `w`, ever, and the margin is exactly 2.**

**(B3) My own registered prediction FALSIFIED — reported, not buried.** I registered (G1.2) that `w_min(a)` is increasing in `a`. It is not: 42 `(p,m,a)` cells have `w_min(a) &lt; w_min(0)` (first: `p=3,m=4,a=2` → 5 &lt; 6; `p=7,m=4,a=1` → 7 &lt; 12). Every such cell has `m − a &lt; j_p = v_2(p²−1)`, i.e. LEMMA COS's uniformity hypothesis fails at the *reduced* level; 27 of the 42 are the `delta=1` family, which is exactly the official prime-row family. The corrected law is `(LVL-a)` with `w_cov` evaluated at the reduced length. **(B1)+(B2) make the campaign conclusion independent of this.**

### The census gate IS reproduced — by the coupled criterion and by nothing weaker

&gt; **THEOREM SP-COUPLE.** `strat(S)=0` and `p | N(I_S)` force **simultaneously**: `eps = A−B ∈ C_odd` (ternary, SP-TERNARY's code), `u = m^{(1)} ∈ C_even` (the `{0,1,2}` cyclic code at length `h`, zeros `eta^t`, `t ≤ floor((w−1)/2)`), and the **support coupling** `supp(eps) = {j : u_j = 1}`, `Σ u_j = r'`. Exactly:
&gt; `#{S : strat=0, all window conditions} = Σ_{0≠eps ternary ∈ C_odd} #{y ⊆ supp(eps)^c : 1_{supp(eps)} + 2·1_y ∈ C_even}`.
&gt; SP-TERNARY is the `eps`-half alone (inner count replaced by `2^{z(eps)}`).

Exact census over **all `2^n` subsets** (meet-in-the-middle), `n=32`, `p=7`:

| `w` | 2 | 3 | 4 | 5 | 6 | **7** | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| `a=0`, FULL window | 1916928 | 38272 | 320 | 64 | 64 | **0** | 0 | 0 |
| `a=0`, ODD only | 1916928 | 1916928 | 17408 | 17408 | 17408 | **17408** | 17408 | 17408 |

The only condition added from `w=6` to `w=7` is `s = 6`, **even**. The certificate: at `(32,7,7)` `C_odd` holds **288** nonzero ternary codewords (independently reproducing the banked SP-TERNARY count) and **none** admits a compatible `u ∈ C_even`. Same at `n=16` (16 codewords, 0 coupled). In all 15 tested cells the coupled count **equals** the independent exhaustive census, and `Σ2^{z(eps)}` equals the odd-only census. The banked round-18 table at `n=32,p=3` (`1048576/983040, 4096/3072, 4096/3072, 128/64, 64/0, 64/0, 64/0`) is reproduced **exactly**.

### (C1) GAP VERDICT: **0.00% closes.** (G1.6 held.)

The gap is governed by `w_cov(q, 2^41)`; by (B1) no even-condition coverage statement moves it. SP-COUPLE is strictly stronger than SP-TERNARY and explains every observed sub-`w_cov` emptiness — but like SP-TERNARY it is a per-`(n,p,w)` certified criterion with **no `n`-uniform form**; at prize length it is the (ES) problem again (CATCH E-2).

### CATCH-20C — CATCH E-3's gap constant is `2^3.6869`, not `2^4.6869`

CATCH E-3 derives "SP-COVER needs `w ≥ 2^42`" from `w_cov ≤ 2^{j_q}`, `j_q ≥ 42`. That is LEMMA COS's **bound**, whose `m`-uniformity requires `m ≥ j_p`; here `m = 41 &lt; 42`. The **operative** value is `w_cov(q,2^41) = 2^41` (B2), so the gap to CS's `w* = 2^37.3131` is `2^3.6869`. Correction is in the safe direction; no verdict moves (`2^41 &gt; 2^40 &gt; w`). CS's bracket arithmetic re-verified: **71.1645% closed / 28.8355% residual** on the banked linear-in-`w` convention.

### CATCH-20A — a banked constant is wrong (harmless, but wrong)

`w_cov(11) = w_cov(19) = **6**`, not 8. `efloor_sparsity/REPORT.md:33` and COROLLARY SP5 (`PROOFS.md:211-212`) print 8 — which is `2^{j_p}`, the wrong column of `PROOFS.md:193-205`'s own table. The corollary as printed stays **true** (`w≥8 ⟹ w≥6`) but is not sharp. **The minted node prints no value for 11 or 19, so no minted statement is affected.**

---

## 2. (C2) THE UNTESTED CELL — the constant-weight Z-FLOOR EXISTS

The mandate asked for the instrument *or* the proof that the restriction breaks. **Both exist, and the boundary between them is exact.**

&gt; **PROPOSITION SH (exact).** `|X_{r'}| = Σ_{W=0}^{r'} N(W, r'−W)`, where `X_{r'} = {S' ⊆ Z/2L : |S'| = r', Ψ(S') = 0}` and `N(W,W') = #{(a,b) ∈ Y_W×Y_{W'} : ψ(a)=ψ(b)}` on Johnson shells of `[0,L)`.
&gt;
&gt; **THEOREM CW-FLOOR.** For `r'` **even**: `|X_{r'}| ≥ N(r'/2, r'/2) ≥ C(L, r'/2)² / p^{delta_a}`. Hence `C(L,r'/2) &gt; p^{delta_a}` forces `|X_{r'}| &gt; C(L,r'/2) = |X^struct|` — a **non-structural** constant-weight solution, with a count.

The whole thing turns on one coincidence (registered as G2.1 and confirmed): **the constant-weight collision multiplicity `C(L−U, W−U/2)` at `W+W' = r'` is identically LEMMA TC's fibre size `C(L−U,(r'−U)/2)`.** This is the exact constant-weight analogue of THEOREM Z-FLOOR, with the cube `2^L` replaced by the shell `C(L,r'/2)` and the difference-multiplicity weight `2^{L−U}` replaced by LEMMA TC's binomial.

&gt; **PROPOSITION BR (the break, located).** (i) Cross-shell terms `N(W,r'−W)`, `W ≠ r'/2`, carry **no** Cauchy–Schwarz floor (C-S bounds them *above*; they can be 0 while `C(L,W)C(L,r'−W)/Q &gt; 1`). (ii) So Vandermonde's `Σ_W C(L,W)C(L,r'−W) = C(2L,r')` is unrecoverable and the floor loses exactly `log2 C(2L,r') − 2 log2 C(L,r'/2)` bits. (iii) At **odd `r'`** the route is *unavailable*: equal-weight collisions give balanced `eps` (even support `U`), while LEMMA TC's odd-`r'` index set has `U` odd — the sets meet only at `eps=0`.

*Machine-verified, 95 checks / 0 failures over 8 `(L,p)` toys × 2 weights: LEMMA TC reproduced against brute force over all `C(2L,r')` subsets; SH exact in every cell; the diagonal floor holds everywhere; and in **every** cell a cross-shell term violates the naive floor (`L=8,p=3,r'=6`: `N(2,4)=15 &lt; 24.198`; `L=6,p=7,r'=4`: `N(1,3)=0` vs `2.449`). Exhibit: `L=8,p=7,r'=6` (`Q=49 &lt; C(8,3)=56`) → CW-FLOOR gives `|X_6| ≥ 64`, truth is `168 &gt; 56`.*

### (C2) VERDICT at the crossing instance — new, and vacuous where wanted (G2.2/G2.3/G2.4 all held exactly)

At `(L, r'_a) = (128, 126)` (`r'_a = L−2` is even at every `v`, by LEMMA DS):

| quantity | bits |
|---|---|
| `log2 C(128,63)` = structural count = **CW-FLOOR's threshold** | **124.1491** |
| `log2 C(256,126)` = flat count (= the retired PER-WEIGHT value) | 251.6279 |
| shell-diagonal loss | **3.3298** |
| THEOREM DSA's threshold `L−2` | 126.0000 |
| CW-FLOOR strictly inside DSA by | **1.8509** |

- **Vacuous at every prime row.** CW-FLOOR needs `delta_a·log2 p &lt; 124.149`; live `e=1` rows start at `log2 p = 129.585` (`B*≥3`) — short by **5.436 bits** (3.851 at `B*≥1`).
- **Where it fires it dominates DSA.** At the banked witness row `p = 3·2^41+1` (`log2 p = 42.585`), CW-FLOOR **proves** `|X_126| ≥ 2^205.7132` against structural `2^124.1491`, where DSA proves only the single extra fibre `C(108,53) = 2^104.267`. Round 18's *heuristic* was `C(256,126)/p = 2^209.043`. **CW-FLOOR converts that heuristic into a theorem, losing exactly the 3.3298-bit shell-diagonal gap.**

**Subtraction:** `tern_master_threshold/statement.md:47-50` explicitly records the constant-weight functional as **outside** Z-FLOOR-M's scope, and the round-19 adversary registered this as the one untested cell. No floor of this shape exists in the repo. SH, CW-FLOOR and BR are new.

---

## 3. (C3) THE PT-2 CLIFF — **THE ADVERSARIAL CHECK FIRES. CATCH-20D (MAJOR).**

### RHL-LB's `2^34`: **EXACT**, not floored; **CONVENTIONAL** only in its extremality scope

`sigma_cyc = d·c + s = 2^33 + (2^33−1) = 2^34 − 1 = 17,179,869,183` is an **integer identity** — no floor, no rounding. `a_L ≥ k + 2^34` is the integer successor, also exact. I re-derived the extremality from scratch over all `N = 2^j`, `j = 2..28`, and all certified `d`: `2^34 − 1` at `(c,d) = (2^33,1)` is the **unique** maximum (runners-up `3·2^32−1 = 2^33.5850`, `5·2^31−1 = 2^33.3219`); `L_cyc = ceil(C(255,129)/256)` at `log2 = 242.6503`; the (CR5) margin at `q=2^256` is `114.6503` bits (source says "&gt; 114"). **Direction check: RHL-LB lower-bounds `a_L`, so any improvement moves `w` UP, away from the threshold. The endpoint cannot move down.**

### The clearance is `p`-DEPENDENT, and `0.336` is its value at `log2 p = 256` only

Closed form re-derived: subcritical iff `w &gt; w_tern(p) := 2^41·log2(3)/log2(p)`. At `log2 p = 256` that is `2^33.66445` and the clearance is `0.33555` bits — PT-2 reproduced to five decimals, with `tau=1, Tcrit=+149.75` at `v=33` and `Tcrit=−53.125` at `v=34` cross-checked. **Reading-invariance (G3.3 held):** the odd-part reading (`g=2^33, h=2^40`) and the deep-stratum reading (`g=delta_a=1, h=L=128`) give the identical `log2 p` threshold `202.8752` to `1e-9` — the answer does not depend on the Lambda parity convention.

**The LIVE range.** `B* ∈ {1,2}` is closed *exactly* by (RHL-B12) (`a_L = 3n/4`, i.e. `w = 2^39`, the top of the bracket), so the open crossing needs `B* ≥ 3`, i.e. `q ≥ 3·2^128`. For `e=1` (`q = p`, forced by `n | p−1`) the live range is **`log2 p ∈ [129.5849625, 256)`**.

### The answer to the pre-registered question is **YES — under every banked reading**

| reading (functional named, CATCH-19C) | clearance at `log2 p=129.585` | at `202.875` | at `255.999` | supercritical for | share of live range |
|---|---|---|---|---|---|
| TERNARY (odd-part = deep-stratum) | **−0.6467** | −0.0000 | +0.3355 | `log2 p &lt; 202.8752` | **57.98%** |
| TERNARY orbit-corrected (LEMMA ROT) | **−0.5662** | +0.0562 | +0.3820 | `&lt; 194.8752` | 51.65% |
| PER-WEIGHT (retired) | **−0.9393** | −0.3030 | +0.0251 | `&lt; 251.6279` | 96.54% |
| GLOBAL (ES-G) | **−0.9822** | −0.3356 | −0.0000 | `&lt; 256` | **100.00%** |

Reproduction script: `cg_arith.py pt2` → `arith_pt2.out`. Per the pre-registration I **stopped** the C3 line here rather than searching for a rescue.

### Honest calibration — what CATCH-20D is and is not

1. **Not a refutation of emptiness.** THEOREM MT proves existence only for `tau &lt; 1` (`log2 p &lt; 128`), which `B* ≥ 1` forbids; DSA needs `delta_a·log2 p &lt; 126`, also forbidden. On the live prime range the supercriticality is **first-moment (heuristic)**, inside the `tau ∈ (1, 1.585)` band the node itself labels heuristic. **The banked dichotomy (`e=1` rows are never in the DSA regime) is CORRECT and is re-verified here.**
2. **The mathematics is upstream; the defect is in the minted scope.** Round 18 already recorded (`crossing_low_w/PROOFS.md:393`, `REPORT.md:95`) that "only the `e=1` sub-range `log2 p &gt; 202.875` is expected clean". The **minted** watch line drops that scope — it prints "clears the ternary counting threshold by 0.336 bits" with no `p`-qualification and instructs "any change to the bracket's lower end must re-run this check". A maintainer following the minted text would compute `0.336` and conclude safety, when for **57.98%** of the live admissible prime range the correct value is negative. **CATCH-20D is a SCOPE DEFECT in a minted node statement, not a new theorem — priced accordingly.**
3. **The correct watch line** is `w_tern(p) = 2^41·log2(3)/log2(p)` together with `log2 p ∈ [129.585, 256)`; `0.336` is its value at the top of that range only.

---

## 4. (C4) THE EXACT REMAINING GAP

**Instance.** `n=2^41`, `k=2^40`, `e=1`, `q=p ≡ 1 mod 2^41`, `B*≥3` (`log2 p ∈ [129.585,256)`), `w = a_L−k ∈ [2^34, 2^39]`, `r' = 2^40−w`.

**Closed:** `w &gt; 2^37.3131` by THEOREM CS *at `log2 p = 256`* (71.1645% of the bracket, linear-in-`w`); and all `B* ∈ {1,2}` rows entirely, by (RHL-B12).

**Open — the exact residual:** `{w ∈ [2^34, 2^37.3131]} × {log2 p ∈ [129.585, 256)}` — i.e. **28.8355%** of the bracket at the top of the prime range and **more** below it, since CS's `w*` is itself `p`-dependent (CS3); plus the entire sub-range `log2 p &lt; 202.875` where the bracket's own lower endpoint is first-moment supercritical (CATCH-20D).

**Dead routes — named, not resurrected:**
1. **SPD union bound** — proved vacuous in every regime. Not touched.
2. **Even-condition SP-COVER** — dead by CATCH-20B(B1): even exponents are non-units. *This closes round-18 residual 5.*
3. **SP-COVER at prime rows, at any level** — dead by (B2): `min_a w_min(a) = 2^40+1 &gt; 2^40−1 ≥ w`.
4. **CW-FLOOR at prime rows** — dead by §2: vacuous by 3.851 bits even at the most favourable admissible row.
5. **CC-sparsity as a lemma** — CATCH E-2: it *is* (ES) again at half length over a ternary alphabet.

**Alive:** (a) an `n`-uniform form of SP-COUPLE/SP-TERNARY (SP-COUPLE explains every observed sub-`w_cov` emptiness; only length-uniformity is missing); (b) a `p`-uniform CS (would close both the residual bracket and CATCH-20D's exposure); (c) **raising the bracket's lower endpoint** — by §3.1 any improvement moves `w` up, and pushing it above `w_tern(129.585) = 2^34.6467` removes CATCH-20D outright, but the printed construction is provably extremal so this needs a *new* construction; (d) any proved statement inside `tau ∈ (1, 1.585)`, in either direction.

---

## 5. Honesty ledger

- **Registered and FALSIFIED: G1.2** (level-`a` coverage monotone in `a`) — 42 counterexample cells found, reported, corrected law stated; conclusion unaffected.
- **Registered and HELD:** G1.1, G1.3, G1.4, G1.5, G1.6, G2.1, G2.2, G2.3, G2.4, G3.1, G3.2, G3.3, G3.4 — including the numeric predictions `3.33` bits (got 3.3298), `1.851` bits (1.8509), `2^205.7` (2^205.7132), `−0.6465` bits (−0.6467), 57.98%.
- **Catches:** CATCH-20A (banked `w_cov(11)=w_cov(19)=6`, printed 8; minted node unaffected), CATCH-20B (the even-condition route is structurally dead), CATCH-20C (CATCH E-3's gap constant `2^3.6869`, not `2^4.6869`), **CATCH-20D (major: PT-2's minted watch line is missing its `log2 p` scope; the endpoint is below threshold on 57.98%–100% of the live prime range depending on functional)**.
- **Scope:** censuses are exhaustive over ALL `2^n` subsets at `n ∈ {16,32}` — nothing is an `n`-extrapolation. CW-FLOOR's toys are `L ≤ 8`; every prize-row number is closed-form arithmetic or a deduction from theorems proved for all `n`. CATCH-19C rule applied: every measured claim names its functional; 2-power lengths; shift-0 windows only.
- **COMPUTE LAW: no breaches.** No `git` write, no file outside `notes/pilots_20260806/crossing_gap/`, `gamma_shell/` never read.

result: Round-20 crossing_gap pilot complete (7,192 checks / 0 failures): the even-condition SP-COVER extension is formalized as the 2-adic Haar tower and proved **incapable** of lowering any threshold (0% of the gap closes) while the new coupled odd/even criterion exactly reproduces the p=7,w=7 census gate; a genuinely new instrument **THEOREM CW-FLOOR** (`|X_r'| ≥ C(L,r'/2)²/p^{delta_a}`, r' even) is proved and upgrades round 18's heuristic tower-row count `2^209.0` to a proved `2^205.7`, but is vacuous at prime rows by 3.85 bits; and the adversarial PT-2 re-check **fires** — RHL-LB's `2^34` is exact but its 0.336-bit clearance holds only at `log2 p = 256`, with the endpoint below the supercriticality threshold on 57.98% (ternary) to 100% (GLOBAL) of the live admissible prime range: a scope defect in a minted node statement, reproduced by `notes/pilots_20260806/crossing_gap/cg_arith.py pt2`.
