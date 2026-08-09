# REPORT.md — freeze_tail_law (round 26) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a0f0729dc2e629212, 2026-08-09. Pilot: Opus. No edits.

All writes confined; the two `__pycache__` files in the read-only directories predate my session (Aug 8 12:47, Aug 9 12:40), so nothing was written there.

---

# FREEZE-TAIL CUTOFF LAW — round 26, `freeze_tail_law`

**Headline: the named residual obstruction is closed, and closed as a theorem rather than a fit — because there is no curve to fit. The freeze tail is not a steepened power law; it is exactly a short-vector census of a lattice inside a box, and it terminates at an explicit integer because a non-frozen state forces a prime to divide a nonzero bounded resultant. `S_inf = 1/ln 2` falls to a three-line factorial telescoping. And the law pays out: the G-c undecidable band shrinks from `(232, 256]` to `(251.1, 256]` — about 80% of it closed.**

---

## Verdict, up front

| question | answer |
|---|---|
| did the cutoff law land as a **fit**? | **No — and it should not have.** The tail has no deterministic exponent; my registered tail form (slope `2/e`) MISSED. |
| did it land as a **proof**? | **YES.** Theorem + 419/419 rows + five exact integer cutoffs + 8,279 fresh certifying primes. |
| did **S_inf = 1/ln 2** land? | **YES**, three lines, with the full asymptotic expansion as a bonus. |
| is the `(232,256]` band reachable? | **Not by census** (cheapest object `2^4224` states). **Yes by tolerance**: `232.7 -&gt; 251.1`. |

## Misses, first

1. **PR-6 MISSED, and badly.** I registered that refitting on `Lam &lt;= LamStar` would give `max|alpha/T - 1| in [0, 0.05]`. Measured: **0.736**. The registered window was simply the wrong window — freeze-tail contamination reaches **3 to 5 bits below `LamStar`**, not up to it. That mistake is itself the finding that fixed D2(iii) (see below).
2. **PR-6b (tail slope `= 2/e`) MISSED.** Measured tail slopes `0.47–0.87` against predicted `0.25 / 0.50 / 1.00`, residuals `0.24–0.79` bits. The Gaussian/theta heuristic gets the *shape* (exponential in depth) but not the exponent. Post-hoc, the reason is visible in the data: the tail rows are a censored sample (only `q` admitting a box-length short vector appear), so the slope is biased toward the box cap.
3. **PR-5 scraped through at exactly 5/7**, with two flat misses: round 25's reported freeze scale for `(32,2,1)` is `15.51` but the true cutoff is `2^18.063`; for `(64,4,2)` it is `21.00` but the true cutoff is `2^27.222` — a **6.2-bit understatement**. Cause: the excess is **non-monotone in `q`** (that cell is frozen at `2^21` and non-frozen at `2^21.5` *and* `2^22`), so "smallest frozen scale" was never a cutoff estimator.

Everything else passed: PR-1, PR-2, PR-3, PR-4, PR-7, PR-8, PR-9.

## Escape tests

- `escalate.py` phase A from a fresh checkpoint in my own directory: **positive control PASS 8/8, PR-A PASS** (telescoping lemma vs independent `2^16` brute force, all 4 configs, both forms agreeing).
- `analytic.py` read-only in place: reserve-break scale **255.999999987544** reproduced, ledger rebuild **5/5 True**, `S_200 = 1.4426950409`, catch C25-5 printed.

---

## D1 — THE FIT (what the excess actually is)

**L3, the negacyclic reduction (new, exact).** For any `T = 1` cell (`u = 2^lev`, `h = n/2^lev`, `e = n/2t`, `h = 2e`), write `A_i = c_i - c_{i+e} in [-u,u]`. Then

```
Zlev(q)  =  SUM over A in L_q ^ [-u,u]^e  of  PROD_i C(2u, u + A_i),
L_q = { A in Z^e : SUM_i A_i zeta^i = 0 (mod q) }   (rank e, determinant q)
```

`A = 0` is exactly the frozen stratum (`Zinf = C(2u,u)^e = sigma(u,2)^e`). **Verified bit-exactly on 181/181 banked rows across all five `T=1` cells, 0 mismatches.** It is literally `mitm_null_count(zeta powers, skew_alpha(2u), q, 1)` — the same skew census the junctions already use. It cuts the MITM state count from `(u+1)^{h/2}` to `(2u+1)^{e/2}`: e.g. `(256,32,5)` goes `1,185,921 -&gt; 4,225`.

**The tail is a short-vector census (exact, not fitted).** Enumerating the box for every tail row of three cells, the identity `Zlev - Zinf = SUM_{A != 0} PROD_i C(2u,u+A_i)` held on every row (the assertion never fired). The mechanism is visible in the numbers — as `q` grows the surviving lattice points get scarcer and longer, and the binomial weight kills them:

| cell `(128,16,4)` | `Lam=11.39` | `12.13` | `13.21` | `14.13` | `15.03` | `&gt;= 34` |
|---|---|---|---|---|---|---|
| nonzero lattice points in box | 392 | 248 | 144 | 64 | 40 | **0** |
| `||A_1||^2` | 67 | 67 | 131 | 157 | 189 | — |
| depth `y = log2(Zinf/excess)` | 1.94 | 3.04 | 7.95 | 11.58 | 15.65 | `inf` |
| weight share of the shortest vector | 0.478 | 0.958 | 0.539 | 0.909 | **0.9997** | — |

So **there is no steepening *exponent*.** The local exponent grows without bound: `y ~ ||A_1||^2/(u ln 2)`, exponential in `Lam`, and violently non-monotone because `lambda_1` fluctuates prime to prime. The Gaussian predictor `||A_1||^2/(u ln 2)` overshoots the exact depth by `3.12, 2.52, 1.75` for `u = 2, 8, 16` — converging to 1 as `u` grows, as it must.

**The deep band, in the right coordinates.** With `x = log2 Zinf - n + T*Lam` (naive depth) and `y = log2 Zinf - log2(Zlev - Zinf)` (true depth), the registered law `alpha = T` is `y = x`. The deviation decays **exponentially in the depth**, `|y - x| = 2^(a + s x)`:

| cell | `T` | `s` | `a` | resid | sign |
|---|---|---|---|---|---|
| (32,2,1) | 1 | 0.908 | 0.202 | 0.248 | steepens |
| (64,4,2) | 1 | 0.914 | 0.029 | 0.244 | steepens |
| (128,16,4) | 1 | 1.023 | 0.698 | 0.045 | steepens |
| (32,2,0) | 2 | 0.764 | 0.329 | 2.081 | flattens |

`T = 1` cells steepen; `T &gt;= 2` cells flatten — exactly as the stratum count predicts, because for `T &gt;= 2` the sub-dominant strata carry `g_v = 1` residual conditions instead of `T` and so decay slower and take over near freeze. (The `T &gt;= 2` fits are noisy, resid ~2 bits; I do not lean on them.)

**Cutoff location as a function of `(n,t,lev,e)`**, and the integer at which it terminates:

```
log2 Q_H(n,t,lev) = max_{0&lt;=v&lt;=tau} (m_v/g_v)*(lev + v + 0.5 log2 m_v)     [Hadamard]
m_v = h/2^(v+1),  g_v = max(1, T/2^(v+1)),  tau = log2 T
```
and, sharply, for `T = 1` cells the exact maximum of the norm over the box is `M(e) u^e` with **`M(4) = 9 = 3^2`, `M(8) = 2401 = 7^4`** — i.e. `M(e) = (e-1)^{e/2}` (`e = 2` is the exception, `M(2) = 2`), giving

```
log2 (max nonzero norm) = e*lev + (e/2) log2(e-1)      -- reproduces all five cells EXACTLY
```

| cell | `B` (Hadamard) | `e*lev + (e/2)log2(e-1)` | max&amp;#124;Norm&amp;#124; | **exact cutoff `Q*`** | `B - log2 Q*` |
|---|---|---|---|---|---|
| (32,2,1) | 20.0 | **19.23** | 614656 | **273857** = `2^18.063` | 1.94 |
| (64,4,2) | 28.0 | **27.23** | 157351936 | **156542401** = `2^27.222` | 0.78 |
| (64,8,3) | 16.0 | **15.17** | 36864 | **26177** = `2^14.676` | 1.32 |
| (128,16,4) | 20.0 | **19.17** | 589824 | **509441** = `2^18.959` | 1.04 |
| (256,32,5) | 24.0 | **23.17** | 9437184 | **8677121** = `2^23.049` | 0.95 |

`Q*` is the largest prime `q = 1 mod n` whose census exceeds the frozen stratum. **Certified predictively**: excess is nonzero *at* `Q*` in every cell, and **every one of the 8,279 primes `= 1 mod n` between `Q*` and `2^B` is frozen — 0 violations** — plus 12 far-ladder points out to `2^44`.

## D2 — THE PROOF

&gt; **Theorem (freeze-tail cutoff).** Let `n, t` be powers of two, `u = 2^lev`, `h = n/2^lev`, `T = t/2^lev &gt;= 1`, `e = n/(2t)`, so `h = 2Te`. Let `q = 1 (mod n)` be prime and `zeta in F_q` of order `h`. If
&gt; `log2 q &gt; B(n,t,lev) = max_{0&lt;=v&lt;=tau} (m_v/g_v)(lev + v + 0.5 log2 m_v)`
&gt; then `Zlev(q) = Zinf(n,t,lev)` exactly.

*Proof.* The imposed conditions are `C(zeta^r) = 0 (mod q)` for `r = 1..T`, where `C(X) = SUM_i c_i X^i`; `zeta^r` has order `d_v = h/2^v`, `v = v_2(r)`, and `v` ranges over `0..tau`. A state is frozen iff `PROD_{v=0}^{tau} Phi_{d_v} = (X^h-1)/(X^e-1)` divides `C`, i.e. iff `c` is `e`-periodic (round 25's closed form, re-derived). So a **non-frozen** `c` has `Phi_{d_v} nmid C` for some `v`, hence `Res(Phi_{d_v}, C) = Norm(C(zeta_{d_v}))` is a **nonzero rational integer**. `Phi_{d_v}` is a power-of-two cyclotomic, so `q` is odd and coprime to its discriminant and it splits mod `q^k` with distinct Hensel-liftable roots; the `g_v` imposed frequencies at valuation `v` give `g_v` distinct roots at which `C` vanishes mod `q`, so `q^{g_v} | Res`. Reducing `C mod (X^{m_v}+1)` is an alternating sum of `2^{v+1}` coefficients each in `[0,u]`, so the entries lie in `[-u2^v, u2^v]` and Hadamard gives `|Res| &lt;= (u 2^v sqrt(m_v))^{m_v}`. Hence `q^{g_v} &lt;= (a_v sqrt(m_v))^{m_v}`, which is the bound. Being a maximum of finitely many nonzero integer norms over a finite box, the true cutoff is an **exact integer**. ∎

**Which stratum is last (L2).** The argmax is `v* = tau - 1` for `T &gt;= 2` and `v* = 0` for `T = 1`; both have `g_{v*} = 1`. The last surviving stratum is `{c : Phi_{d_v} | C for all v != v*, Phi_{d_{v*}} nmid C}` — the unique stratum with one residual mod-`q` condition and maximal entropy-per-condition. Empirically confirmed: `v*` came out `0` for ten of the eleven banked cells and `1` for `(32,4,0)` (`tau = 2`), matching the formula.

**(i) The named obstruction is closed.** 419/419 rows (275 banked + 144 new) obey the theorem: **zero rows with `log2 q &gt; B` and excess `&gt; 0`.**

**(ii) `alpha = T` becomes an actual theorem on the official domain.** The deviation decays as `2^{a+sx}` with `s in [0.91, 1.02]` per bit for the clean `T=1` cells. At the official schedule the level-0 depth is `x = e - n + t*Lam`, so `[law]`:

| `log2 q` | official depth `x` | `|alpha/T - 1| &lt;=` |
|---|---|---|
| 232 | `-2.06e11` bits | `2^(-1.58e11)` |
| 248 | `-6.87e10` | `2^(-5.25e10)` |
| 255 | `-8.59e9` | `2^(-6.56e9)` |

PR-D is exact there to any resolution that could ever matter — **but this is a toy-fitted decay extrapolated across 11 orders of magnitude in `e` and `T`, and is labelled `[law]`, not proved.**

**(iii) The licensed range moves — 232.7 -&gt; 251.1.** The `10%` tolerance that capped G-c's F2 power at `256/1.10 = 232.7` was set by scatter that is now *identified* as freeze-tail contamination with a known decay. Re-windowing the fit by depth, and using cells that only the L3 reduction makes reachable (mechanical selection rule fixed before measurement: `T = 1`, reduced half `&lt;= 2^21` states, deep-band span `&gt;= 10` bits — three cells, `(64,2,1)`, `(128,8,3)`, `(256,16,4)`, whose direct MITM costs are `4.3e7`, `4.3e7`, `7.0e9` states; 124 new exact rows):

| depth window | cells (`&gt;=5` pts) | distinct `T` | `eps = max|alpha/T - 1|` | G-c rule met | licensed `log2 q &lt;=` |
|---|---|---|---|---|---|
| `x &lt;= 0` | 8 | {1,2} | 0.7360 | yes | 147.5 |
| `x &lt;= -2` | 7 | {1,2} | 0.0948 | yes | 233.8 |
| `x &lt;= -4` | 5 | {1,2} | 0.0206 | yes | 250.8 |
| **`x &lt;= -5`** | **5** | **{1,2}** | **0.0195** | **yes** | **251.1** |

Per-cell at `x &lt;= -4`: `(64,2,1) 1.0006/36pt`, `(256,16,4) 1.0048/22pt`, `(128,8,3) 1.0071/16pt`, `(64,4,2) 1.0128/6pt`, `(32,2,0) 0.9805/7pt`. **The undecidable band shrinks from `(232, 256]` to `(251.1, 256]`.** Caveat, stated plainly: this converts a *fit-scatter* statistic into a *detection threshold*, reusing round 25's calibration `delta_det = tolerance - 1`. A clean claim needs `power.py` re-run on synthetic worlds at the new tolerance. That is the obvious next job and I did not do it.

## D3 — `S_inf = 1/ln 2`, PROVED

`c_k = 2^k - log2 C(2^k, 2^{k-1})`, so `2^{-k} log2 C(2^k,2^{k-1}) = 2^{-k} log2 (2^k)! - 2^{-(k-1)} log2 (2^{k-1})!` — **the summand telescopes against the factorial**. Hence exactly

```
S_K = SUM_{k=1..K} 2^{-k} c_k  =  K - 2^{-K} log2( (2^K)! )
```

and Stirling `log2 N! = N log2 N - N log2 e + (1/2)log2(2 pi N) + O(1/N)` at `N = 2^K` gives

```
S_K = log2 e - 2^{-(K+1)} log2(2 pi 2^K) + O(4^{-K})   -&gt;   S_inf = log2 e = 1/ln 2.  ∎
```

Verified `K = 1..18`: the identity holds to `8.9e-16` (float roundoff only), and `(log2 e - S_K)/(2^{-(K+1)}log2(2 pi 2^K))` is `1.000004` at `K = 12` and `1.000000` by `K = 15`.

**Mint, with the constant now explicit:**
```
R3inf_full(n, n/2) = (log2 e - 1) n - (1/2) log2(pi n) + 1/2 + O(1/n)
                   = 0.4426950409 n - (1/2) log2(pi n) + 1/2 + O(1/n)
```
Cross-check at `n = 16`: formula `4.7575`, exact `R3inf_full(16,8) = 4.7498595301` — which is bit-identical to the *measured* saturated `R3` at `(16,8,W=[0,1,2])` in the phase-A replay.

## D4 — THE `(232, 256]` PRICING

The official level-0 depth is `d(Lam) = e - n + t*Lam` — **this is precisely the ledger's coset term.** It crosses `0` at `log2 q = 256 - 128/2^33 = 255.999999985099` and `21` at `256 - 107/2^33 = 255.999999987544`. So:

- **The whole band `(232, 255.999999985]` is deep band, not tail.** The freeze tail occupies only the last `1.49e-8` of `log2 q` — exactly the knife edge where the reserve breaks.
- **Census cost.** Cheapest exact level census over all 34 official levels: `2^4224` states (at `lev = 33`); the L3 reduction applies there (`T = 1`) and halves the exponent to `2^2176`. Both are beyond any wall, and no cutoff law helps, because the band is deep-band. **Answer: NO, not reachable by census.** The band moves only through the tolerance route above.

## Catches

- **C26-1** the freeze-tail cutoff **theorem** — the round-25 named obstruction, closed.
- **C26-2** the **negacyclic reduction** L3: a `T=1` level census *is* a skew census on `e` coordinates; `181/181` exact; unlocks cells MITM cannot reach (`7.0e9 -&gt; 1.19e6` states).
- **C26-3** the freeze tail is exactly a **short-vector census**; the shortest vector's weight share `-&gt; 1.0000`.
- **C26-4** five exact integer cutoffs, and the sharp max-norm law `max |Res(X^e+1, A)| = (e-1)^{e/2} u^e` over `[-u,u]^e` for `e in {4,8}` (`e=2` exception) — reproduces all five cells exactly. Conjecture beyond `e = 8`.
- **C26-5** round 25's "measured freeze scales" are **not cutoffs**: the excess is non-monotone in `q`; `(64,4,2)` is frozen at `2^21` yet non-frozen at `2^21.5` and `2^22`, true cutoff `2^27.222` — a 6.2-bit understatement.
- **C26-6** `S_inf = 1/ln 2` proved (factorial telescoping) with the full asymptotic; mints `R3inf_full(n,n/2)`.
- **C26-7** the ledger's coset term is a **linear** model of the tail depth, and the toys show the true depth *exceeds* the linear model once the depth is positive — which is precisely the window `(256-128/2^33, 256]` in which the break constant `107` is defined. **Flag on the model, not a claim about the packet**: I have no licence to transport the toy correction there.
- **C26-8** the licensed range `232.7 -&gt; 251.1` (subject to the calibration caveat above).
- **C26-9** the tail contamination extends **3–5 bits below `LamStar`**, not up to it — this is why round 25's `alpha` fits scattered, and why my own PR-6 window was wrong.

## Self-corrections, plainly

1. **Disclosed in the PREREG before registering**: I ran one structural peek at round 25's `ckpt.json` (top-level keys, rows per cell) before writing my registrations. No census value or fit output was read.
2. **I nearly registered a falsification of my own theorem.** Working from the report's freeze scales `34` and `67`, I initially believed they exceeded every Hadamard bound I could compute and that the theorem was dead. Before registering I traced them to `(128,32,4)`/`(256,32,5)` and realised they are sparse *grid points far above* the cutoff. They are — `Q*(256,32,5) = 2^23.05`, first tested point above it: `2^67`.
3. **P4 memory.** My first enumeration stored every distinct norm; for the 17.8M-state cell that is a large set. I changed it to skip any norm `&lt;= ` the current best (which cannot carry a larger prime factor) *before* running the big cells. Declared in the code comment.
4. **P2 and P10 initially iterated a hard-coded 11-cell list**; after P11/P12 added rows and cells I extended both to iterate the data file, and re-ran P2 over all 419 rows.
5. **Divergence D-15 was declared but not exercised**: I used round 24's `get_zeta` convention for every new row. The Galois twist was used only as a *guard* (the reduced census is invariant under `zeta -&gt; zeta^s`, verified for `s = 3,5,7` on each new cell).
6. **The three new deep cells have no independent MITM cross-check** — their direct censuses are `4.3e7`, `4.3e7`, `7.0e9` states, which is the entire point of L3. They rest on L3's `181/181` verification plus two guards each (frozen at `2^{B+4}`; Galois-invariant). Declared, not hidden.

## Scope

Toy results are never official-row evidence in either direction. Every official-scale number here is labelled `[law]`: the `alpha = T` exactness bound (D2 ii), the licensed-range figure (D2 iii, which additionally inherits round 25's `delta_det` calibration), and the C26-7 flag on the break constant. The **theorem** (D2) and the **identity** (D3) are unconditional mathematics and hold at every scale, including the official one; what is *not* licensed is the numerical transport of the toy-fitted decay constants. No status flip, no closure claim on C2''-r3.

## Compliance

Registrations (candidate cutoff form L1/L2/L3, per-cell `B` table, PR-1..PR-9 with numeric windows, divergence D-15) were appended to `PREREG.md` with the `Edit` tool **before any computation**, and the one prior JSON key-peek is disclosed there. **Quarantine honoured**: `CAMPAIGN_LEDGER.md` never opened; `b_sparsity_pose`, `umin_spike_hunt`, `m7_falsifier_hunt` never read; no subagent dispatched. **Compute law**: every `python3` invocation ran as `tools/ramguard tiny|local -- python3 ...` from the repo root, including JSON peeks; `RAMGUARD_TIMEOUT` was used at 600, 900, 1800, 2400 and 3000 s and both long enumerations ran as background jobs with results files. **RAM discipline**: file-at-a-time reads, `dag.json` never opened, all phases checkpointed to `tailckpt.json`/`cdata.json`, the norm enumeration restructured to avoid a multi-million-entry set. **Draft-only**: all writes confined to `notes/pilots_20260809/freeze_tail_law/`; round 25's directory was read but never written (its `__pycache__` is dated 12:40, before my session), round 24's `gb_probe.py` reused verbatim via an absolute pin with its `__pycache__` dated Aug 8; no `dag`/`nodes`/`tools` edit, no git, no Modal, stdlib only.

**Artifacts** (all under `notes/pilots_20260809/freeze_tail_law/`): `PREREG.md` (brief + my registrations), `c2lib.py` (round-25 copy, R24 absolutely pinned), `escalate.py` + `ckpt.json` (escape-test replay), `tail.py` (12 checkpointed phases), `cdata.json` (419 exact level-census rows: 275 copied + 144 new), `tailckpt.json`, and the logs `P3.log`, `P4.log`, `P4b.log`, `P6.log`, `P8.log`.
