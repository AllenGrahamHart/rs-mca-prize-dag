# REPORT.md — c2pp_falsifier_redesign (round 25) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task aaf6505beb45d0c59, 2026-08-09. Pilot: Opus. No edits.

# C2''-r3 FALSIFIER REDESIGN + GB-5 ESCALATION — round 25, `c2pp_falsifier_redesign`

**Headline: the GB-5 4.5× is a saturation artefact, and the official row is not in that regime.** A telescoping identity turns the unreachable multi-junction problem into a reachable per-level one; that gives a powered falsifier, an exact closed form that *reproduces the official ledger's own constants from the toy*, and — for the first time — an estimate of the official C2''-r3 junction sum: **≈ −0.0066 bits for every admissible `q` with `log2 q ≤ 255.9`, crossing 21 bits exactly at `log2 q = 256 − 107/2^33`.**

---

## 1. The enabling lemma (registered before computing, brute-force verified)

&gt; `N_{&gt;j-1} = E_j AND N_{&gt;j}`, hence for `W = {w0..w1}`
&gt; `R3_W = log2 P[N_{&gt;w0-1}] − log2 P[N_{&gt;w1}] − sum_{j in W} log2 P[E_j]`
&gt; `     = log2( P[AND_W E_j | N_{&gt;w1}] / prod_W P[E_j] )` — PREREG P1

So **R3_W is a difference of two level censuses plus J block censuses**, not a product of J hard things — and C2''-r3 says exactly *"the joint nullity probability exceeds the independent-block heuristic by at most 21 bits."* This is why a reachable falsifier exists at all: round 24's wall (every extra junction squares the census) applies to the *window*, not to the *levels*.

**PR-A PASS** by independent machinery: all `2^16` states enumerated directly at `(16,8,q=97)`, `(16,8,193)`, `(16,4,97)`, `(16,4,353)` — level censuses, block censuses, and `R3` all bit-exact against MITM, both forms of the lemma agreeing. **PR-I PASS 8/8** on round 24's banked `BANKED_F2B`.

## 2. (D1) THE FALSIFIER OF RECORD — G-c, LEVEL-DECAY EXPONENT

**Statement.** With `e = n/(2t)`, `T = t/2^lev`, `u = 2^lev`, and the frozen stratum `Zinf(lev) = (sum_c C(u,c)^{2T})^e`, measure the exact census `Zlev(q)` at primes `q = 1 mod n` across `log2 n &lt; Lam &lt; LamStar+3`, `LamStar = (n − log2 Zinf)/T`, and fit
`log2( Zlev(q) − Zinf ) = (n + log2 kappa) − alpha·Lam` over points with `Zlev &gt;= 2 Zinf`.
**G-c FIRES iff `alpha &gt;= 1.10 T` at ≥3 cells with ≥5 fit points spanning ≥2 distinct `T`.**

**Why it is about C2''-r3.** By the lemma, `R3_W` is *exactly* determined by these censuses, and the level-0 instance at the official schedule **is the ledger's own coset term** `128 − 2^33(256 − log2 q)`. `alpha_0 &gt;= 1.10 T_0` moves the level-0 crossover from `256` to `232.7`, so every admissible row with `log2 q &gt;= 233` becomes saturated and the coset term is 128 bits — 6.1× the reserve.

**Power control, run on synthetic worlds BEFORE any real census** (`power.py`, 11 usable cells, `T in {1,2,4}`):

| world | verdict | note |
|---|---|---|
| T (safe) | **LAW HOLDS** | `alpha/T = 1.0000`, resid `0.000` at every cell |
| F1 floor inflation `kappa=1/32` | detected | `alpha/T` collapses to 0.01–0.31 |
| F2 decay excess `delta=0.10` | detected; `0.15/0.30` **FIRES** | |
| F3 sqrt-stratum | **NOT detected** | but harmless — it does not move the official break scale |

Empirical thresholds (scan): `kappa_det = 0.03125 = 1/h_max`, `delta_det = 0.10` — both equal to the hand-registered values. Against the official reserve, `kappa_brk(Lam) = (256−Lam)/256`, `delta_brk(Lam) = (256−Lam)/Lam`, so **G-c is powered for official rows with `log2 q &lt;= 247` (F1) and `&lt;= 232` (F2), and blind above** — the knife edge (`107/2^33 ≈ 1.2e-8`) is unresolvable by any toy, exactly as registered in P9.

**RESULT: G-c is SILENT.** Deep-band `alpha/T` at the four well-determined cells (≥5 fit points): **0.9953, 0.9969, 1.0097, 1.0668** — all inside the ±10% tolerance, `T in {1,2}`. The three thin cells (2–4 points) read 1.19–1.42, but they sit in the freeze tail and cannot discriminate; the registered rule correctly withholds firing (all hot cells have `T=1`). **PR-D confirmed where determinable, refuted as a universal exact law**: the second term is not a pure `q^{-T}` power law — it steepens near freeze and terminates in an exact integer cutoff (measured freeze scales 14.5, 15.5, 18, 21, 22, 34, 67, versus the naive `n/T`). *That cutoff law is the named residual obstruction.*

## 3. (D2) THE ESCALATED GB-5 GRID — 11 windows, 78 exact rows, J = 4 exact

The GB-5 cell reproduces bit-exactly: `(32,16,W=0-3)`, `R3_W = 11.3367`, terms `[1.0000, 6.5322, 2.8502, 0.9543]`, ratio 4.454 — **and it is the FULL tower, 4 of 4 junctions, not 4 of 33.**

**The shape verdict — the 4.5× is regime-dependent:**

| cell | `n/t` | `Lam` | measured `R3_W` | saturated `R3inf` | RATIO |
|---|---|---|---|---|---|
| (32,2,W=[0]) | 16 | 6.60 | **−0.0030** | 3.3203 | −0.005 |
| (64,8,W=[2]) | 8 | 7.59 | **+0.0004** | 3.6459 | 0.001 |
| (32,4,W=[0,1]) | 8 | 6.60 | 1.3745 | 6.8032 | 1.080 |
| (32,16,W=[0-3]) | 2 | 6.60 | 11.3367 | 11.3367 | 4.454 |

**PR-E confirmed decisively.** The cells with the largest `n/t` (nearest the official 256) sit at `R3_W ≈ 0`; the 4.5× cell has `n/t = 2` and is *saturated at every admissible q* — it cannot show anything else. Full transitions were measured: `(32,2)` climbs `−0.003 → 3.3203` over `Lam ∈ [6.6, 16]` (non-monotone, dipping negative mid-band); `(64,8)` climbs `0.0004 → 3.08`.

**PR-F confirmed** (saturated ratio grows ~linearly in `n`): `2.49, 4.45, 7.86, 13.84, 24.47, 43.57, 78.22` for `n = 16…1024`; `4.6e10` at the official row.
**PR-G confirmed**: `PeakJ = 1` at every shape, no `q`-drift; `term_0 → e` exactly (1.0000 at `e=1`, 1.9999 at `e=2`, 4.0000 at `e=4`).

**More pre-saturation octaves at J ≥ 2 is starved, as registered:** multi-junction pre-saturation needs `(n/t)c_lev &gt; log2 n`, leaving only `(32,4,W=[0,1])`. Depth `J = 5` remains walled at `3^16` half-states. The escalation therefore moved the octaves into the *level* law, which the lemma makes equivalent.

## 4. (D3) THE ANALYTIC FORM — and it lands on the official ledger

**Saturated closed forms, 98/98 exact** at `n ∈ {16,32,64,128}`, `t ∈ {2..64}`, **every `e ∈ {1,2,4,8}`** (round 24's V4 covered `e=1` only):
`Zinf = sigma(u,2T)^e`, `Cinf = 2^e`, `Binf = C(2^{j+1},2^j)^{h_{j+1}}` — the frozen stratum is exactly the **`e`-periodic** stratum, `e = n/(2t)`, by the cyclotomic factorization `prod_a (X^{h/2^{a+1}}+1) = (X^h−1)/(X^e−1)`.

**PR-H confirmed 5/5 — the toy law rebuilds `official_scale.json:78-83`:** `n/t = 256`; `e = 128` = `coset_stratum_cells`; `2^128` = `coset_stratum_size`; `2^-2199023255424` = `coset_stratum_probability`; and `e − n + t·Lam = 2^33(log2 q − 256) + 128` = `coset_term_log2_formula`. **The ledger's coset stratum IS the `e`-periodic stratum**, derived here independently from toy censuses.

**The official-row junction sum `[law]`** (`R3_full = R3inf + log2(1+rho_0) − log2(1+rho_m) − sum_j log2(1+beta_j)`):

| `log2 q` | lev-0 coset term | `R3_full` [law] | ≤ 21? |
|---|---|---|---|
| 41 … 255 | −1.85e12 … −8.59e9 | **−6.59e−3** | YES |
| 255.9 | −8.59e8 | −6.71e−3 | YES |
| `256 − 107/2^33` | 21.0000 | **20.9934** | YES |
| 256 | 128.0000 | 126.99 | **NO** |

The law reproduces the packet's own break criterion *from the junction-sum side*, and explains its magic constant: **`107 = e − 21 = 128 − 21` exactly.** Saturated ceiling `R3inf(official) = 9.735e11` bits = `4.64e10 ×` reserve.

**Two new laws.** (i) `S_inf = sum_{k&gt;=1} 2^{-k}(2^k − log2 C(2^k,2^{k-1})) = 1/ln 2` to full double precision (diff exactly 0.0), hence **`R3inf_full(n, n/2) → n(log2 e − 1) = 0.4426950 n`**. (ii) The freeze law is **per level**: `LamStar(lev) = (n − log2 Zinf(lev))/T_lev ≈ (n/t)c_lev` — round 24's `log2 q &gt;= n/t` is the `lev = 0` case. Official crossovers: `lev 0,1 → 256.0`, `lev 2 → 362`, `lev 5 → 726`, `lev 33 → 2218`, so **the official row is pre-saturation at every level, terminating exactly at the level-0/1 crossover** (strengthens GB-3).

## 5. Catches

- **C25-1** the telescoping lemma (makes C2''-r3 measurable at all).
- **C25-2** the `e`-periodic frozen stratum closed form, 98/98 exact, all `e` — and it is the official ledger's coset stratum.
- **C25-3** the freeze law is per-level; round 24's form is the `lev=0` special case.
- **C25-4** **GB-5's 4.5× is a saturation artefact**; measured `R3_W ≈ 0` in deep pre-saturation, where the official row lives.
- **C25-5** `official_scale.json:83` prints `"107/2^33 = 1.24556e-05"`; the true value is `1.245644e-08` — the decimal is `10^3` too large (fraction correct, decimal wrong). Not edited.
- **C25-6** `107 = e − 21`; the constant was never explained on the surface.
- **C25-7** `S_inf = log2 e`, giving `R3inf ~ 0.4427 n`.
- **C25-8** the reused instrument's `least_primitive_root` trial-divides `q−1` and is unusable past `~2^32`; worked around with Proth primes `k·2^B+1` (declared divergence **D-14**), which is what unlocked the 260-octave range.

## 6. Self-corrections, plainly

1. **Phase-A check 4 was mis-stated, not the lemma.** My first conditioned-joint check dropped the conditioning on `N_{&gt;w1}` and "failed"; the lemma held throughout. Both forms now printed and agreeing.
2. **Phase B's first run produced 29 spurious failures** by choosing `q` at `LamStar+3` instead of past the true freeze — the very effect I had registered in C-4 and then walked into. Re-run per-object at the freeze scale: 98/98.
3. **A registered cell was invalid**: `(128,16,W=[4])` — `t=16` has junctions 0–3 only, so junction 4 is a `T=0` shift-0 cell (CATCH-19B). Dropped as never-measurable, not filtered post hoc.
4. **The statistic was recalibrated** (fit window `excess &gt;= 1` bit; tail-robust three-point estimator added after seeing the freeze tail). All calibration was done on **synthetic** worlds and then frozen; the post-hoc addition is declared.
5. **My PREREG P4 rationale phrased the power backwards**: G-c is powered at *low* `log2 q` and blind near 256, not the reverse.
6. **My hand-registered GB-5 terms** `(0.99996, 6.5323, 2.8518, 0.9544)` vs measured `(1.0000, 6.5322, 2.8502, 0.9543)` — third term off by 1.6e-3 from my own rounding.
7. **`alpha = T` is not exact** — PR-D survives only on well-determined cells; the freeze-tail law is unfitted and is the named obstruction.

## 7. Scope, and what this cannot decide

Toy-to-official transport of the *numbers* is not licensed; every official-scale figure is labelled `[law]` — it is the closed form extrapolated, anchored by the 5/5 reproduction of `official_scale.json`. The reachable data licenses the `[law]` estimate for `log2 q &lt;= 232`; on `(232, 256]` it cannot decide; and within `107/2^33` of `256` the law itself says the reserve is broken — which is precisely where the packet's own two 256-bit rows sit (`official_scale.json:181-183`, `"exceeds_2^21": true`). No status flip, no closure claim. Census evidence is evidence, never proof.

**Artifacts** (all under `notes/pilots_20260809/c2pp_falsifier_redesign/`, stdlib only, every `python3` via `tools/ramguard local|tiny -- python3`): `PREREG.md` (registrations appended before any script existed), `c2lib.py` (reuses round 24's `gb_probe.py` verbatim; nothing in that directory written), `power.py` + `power_results.json`, `escalate.py` (4 checkpointed phases: 4 brute-force rows, 98 closed-form checks, 275 exact level-census rows, 78 exact window rows), `analytic.py`, `ckpt.json`. **Quarantine honoured**: `CAMPAIGN_LEDGER.md` never opened, the four sibling round-25 pilot directories never read, no subagent dispatched. No `dag.json`/`nodes/`/`tools/` edit, no git, no Modal.
