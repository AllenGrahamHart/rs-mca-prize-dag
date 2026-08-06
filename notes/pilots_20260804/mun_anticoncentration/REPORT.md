(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Replayed all five verifiers from clean: **50 checks, 0 failures**. Re-read the ask — all four deliverables are covered. REPORT.md writes are harness-blocked, so the report follows here in full.

---

# ROUND 15 — the shared terminal: arithmetic anti-concentration over mu_n

**Verdict in one line: the "external-shaped" label is WRONG in its useful direction.** The terminal is provably invisible to the entire classical weight-distribution toolkit (route cut, proved below), it is shared by **four** lanes not two, and one of those lanes already re-posed it correctly. A Pro brief should not buy a coding theorist.

## 0. SUBTRACTION FIRST — four withdrawals

| PREREG item | verdict | banked at |
|---|---|---|
| (Z) char-0 coset classification | **WITHDRAWN — already proved** | `critical/nodes/b1_char0_giant_coset_theorem/node.json:9` (PROVED, key): *"every 0/1 t-null vector on mu_n (n = 2^s) is a union of mu_M-cosets with M &gt; t"* |
| (F) exact additive-character formula | **WITHDRAWN** | `f2_annealed_phase_split` (I): *"N_b^(j) = (1/q^j) sum_c [z^b] prod_x (1 + z psi(c.(x,..,x^j)))"* |
| (W) Weil vacuity *verdict* | **WITHDRAWN as a verdict** | `f2_weil_newton_arc_bound` (PROVED), Lemma A at t=2: *"useless at the window peak b ~ n/2 ... THE MID-BAND REMAINS OPEN"* |
| (M) second moment + "L2 can't bound the max" | **WITHDRAWN** | `v13_second_moment_shift_pair_identity`; `v13_prefix_collision_ledger/statement.md:7` *"Does NOT by itself give max-fiber control"*; listsize REPORT:34-39 *"KILLED-WITH-CERTIFICATE"* |

Dead routes honoured, not re-walked: `route_anticonc`, `quotient_row_subjohnson_bound`, the listsize terminus, min-over-pencil, the averaging ledger, Corollary I.3, round-13's full-rank cut, SL-2 routes 1-2, absolute-value/annealed routes, Lam-Leung transport to F_q.

**Three catches against the existing tree:**

- **CATCH-15A** (dischargeable now). `xr_band_key_lemma_pencil_mass/statement.md:115-118` declares *"MC-4 (structured-floor completeness) is char-0 Lam-Leung input and is NOT claimed here"*, and `xr_mc_depth_quantization/statement.md:105-109` calls it *"machine-checked here empirically at one shape"*. **MC-4 IS `b1_char0_giant_coset_theorem`, a PROVED key node.** The band lane's only char-0 input can be discharged by citation.
- **CATCH-15B.** `critical/nodes/b1_char0_giant_coset_theorem/` contains **only `node.json`** — no proof.md, no verifier; its `refs` point to a path that does not exist in this repo. `verify_lemmaz.py` (20 checks) is the missing verifier plus an elementary re-proof and the exact scope.
- **CATCH-15C.** Round-14's crossing PREREG:105-106 claims *"No 'weight enumerator'/'weight distribution' string exists anywhere in the repo (checked)"*. **False** — `x4b_moment_trade_exclusion/statement.md:13`, and `moment_trade_staircase` (PROVED) states the identification outright: *"t-moment-null blocks are 0/1-coefficient dual codewords with t leading zero syndromes."* LEMMA Y's novelty is the linearity at `w &lt;= p`, not the identification.

## 1. THE UNIFIED STATEMENT

**Scope split first (measured, `verify_bandlinear.py`).** The mandate asked for the cyclic-code form. That form is **exact for the crossing consumer and only a relaxation for the band consumer**:

```
e_1 = ... = e_c = 0  (PREFIX)      -&gt; IS a constant-weight code slice
c generic linear forms on e-space  -&gt; NOT
top-c coeffs of u.E_T  (BAND)      -&gt; NOT
```

All 16 populated generic/band fixtures are strict (`|Sol| &lt; |slice|`, hull dimension n−1 or n−2). So:

&gt; **(ES) ENTROPIC SUPPRESSION OVER mu_n.** Let `n = 2^m`, `H = x_0 mu_n &lt;= F_q^*` split, `V` an affine subspace of codimension `c` in locator-coefficient space, `R(V) = {T &lt;= H : |T| = r', coeff(E_T) in V}`, and `R^per(V)` its `mu_M`-periodic members. If the row is **sub-balance**, `c·log2 q &gt;= log2 C(n,r') + sigma`, then `R(V) = R^per(V)` — **no accidental members**.

**Cyclic-code (prefix) instance — the crossing lane, exact.** With `V = {e_1 = .. = e_{w-1} = 0}` and `w &lt; p`, Newton makes this linear in the 0/1 indicator: `R(V) = {x in {0,1}^n : wt(x) = r', x in C(n,p,Z_w)}`. (ES) says the weight-`r'` coefficient of that code's 0/1 constant-weight enumerator equals its periodic value `C(n/M, r'/M)`, `M = 2^{ceil log2 w}`.

**Exact code parameters at each row:**

| row | field | length | zeros | code | weight | budget |
|---|---|---|---|---|---|---|
| crossing razor | `F_p`, `p &gt;= 2^39+1`; recorded rows `q = p` PRIME ~2^256, `delta = 1` | `2^41` | `Z_w = {1..w-1}`, `\|Z_w\| = w-1` | `[2^41, 2^41-w+1, w]` **MDS = Reed-Solomon** | `r' = 2^40-w`, `w in [2^34,2^39]` | `B* = floor(q/2^128) &lt; 2^128` |
| band 1/4 | `F_q`, `q &gt;= 2^209` | `2^41`, `k=2^39` | `2d` generic forms, `d in [2^32+1, 2^33-1]` | not cyclic, not a slice | `2^41-2^39-d` | `0.68n^2 = 2^81.444` |
| band 1/8 | same | `k=2^38` | same `d` | same | `2^41-2^38-d` | same |
| band 1/16 | same | `k=2^37` | `d in [2^31+1, 2^32-1]` | same | `2^41-2^37-d` | same |

**(ES) discharges all four consumers.** Band: `xr_mc_depth_quantization` proves `N_d^coset = 0` at band-proper depths, so (ES) gives `|R_d| = 0`. Crossing: (ES) gives `X_w = C(N,m)/N &lt; B*`. **u2c**: its own re-pose is (ES) verbatim — *"zero accidents when the expected count is &lt; 1 uniformly — an entropic-suppression / anti-concentration statement"*. **dli RES**: same file, *"the SAME hard shape as the dli RES count."* The round-14 merge verdict understated its own result: the terminal is shared by **four** lanes.

## 2. THE ROW MAP (`verify_rows.py`, 14 checks)

`Lambda(w) = log2 C(n,r') − |Z_w| log2 q_char`.

- **Crossing crossover sits at the bracket bottom `w = 2^34` exactly when `log2 q_char = 127.977`** — essentially `2^7 = n/w_min`, **the same 2^128 scale that defines `B*`**. At the razor rows: `Lambda(2^34) = −2.20e12` bits, `Lambda(2^39) = −1.39e14`. At minimal `q_char = 2^41`: `+1.49e12` bits. Both regimes admissible; the razor rows are deep in the empty one.
- **Band critical fields**: 208.475931 (1/4), 140.550 (1/8), 174.640 (1/16). **Subtraction alert confirmed:** 208.475931 vs the banked `log2_q_critical = 208.47593052630532` — agreement to **9.5e-9**. The `q &gt;= 2^209` pin *is* the `Lambda_band = 0` threshold at `d = ceil(h/2)`. Cited, not claimed.

**Crossing vs `B*`** (MC-3's exact `C(N,m)/N`): `w=2^34 -&gt; 2^117.15` (**−10.85 bit**), then −73.4, −103.9, −118.5, −125.2, −128.0. The coset family cannot fire the unsafe leg anywhere in the bracket — consistent with the staircase's last rung `L_1(k+2^34−1) &gt; B*`.

**Crossing raw window vs `0.68n^2`** (cross-lane datum, not an SL2 falsifier): the proved char-0 periodic family at `w=2^34` is `C(128,63) = 2^124.15`, **+42.7 bits above budget**.

## 3. THE TRANSFER INVENTORY, and the PROVED ROUTE CUT

| instrument | applies? | why not |
|---|---|---|
| **MDS weight enumerator** (M-S ch.11 thm.6) | code IS MDS, distribution **exactly known** | counts codewords with arbitrary `F_p^*` entries; the 0/1 slice is invisible to it |
| **Weil / Carlitz-Uchiyama** | **VACUOUS at all four rows** | needs `deg·sqrt(q_char) &lt; n`; measured `2^54.5`–`2^166.9` vs `n = 2^41`. Non-vacuity needs `deg &lt; 2^20.5`; bracket starts at `2^34`. Misses by 13.5–107 bits |
| **BCH / Hartmann-Tzeng / Roos / van Lint-Wilson** | give `d &gt;= w`, but `r' &gt; w` throughout | killed by the route cut |
| **MacWilliams / Delsarte LP / Krawtchouk / Sidelnikov** | **BLIND** | all functions of the weight enumerator |

**THE ROUTE CUT (proved, `verify_transfercut.py`, 5 checks).** T1/T1b: at `delta = 1` the code with defining set `{a,...,a+w-2}` is `[n, n−w+1, w]` MDS for every shift. T2: the classical closed form matches brute force digit-exactly. **T3/T4: 18 of 24 tested families have two codes with identical `(n,k,p)` — identical weight enumerator, identical MacWilliams dual, identical Krawtchouk/Delsarte data — and different 0/1 counts:**

```
n=16, p=17, w=3, r'=7 : zeros {1,2} -&gt; 32     zeros {3,4} -&gt; 0
n=16, p=97, w=2, r'=7 : zeros {1}   -&gt; 64     zeros {2}   -&gt; 0
n=16, p=17, w=3, r'=8 : a=1:54 a=2:54 a=3:98 a=4:98 a=5:22 a=6:54 a=7:276
```

Both defining sets are consecutive, so both codes are cyclic with the same designed distance.

&gt; **THEOREM (route cut).** The shared terminal is not a function of the weight enumerator, nor of (length, dimension, designed distance). No MacWilliams identity, Delsarte LP, Krawtchouk expansion, dual-distance argument, Sidelnikov/binomial-approximation theorem, or BCH/HT/Roos/shift-bound argument can decide it — **even in principle**.

**The square-root barrier, measured** (`verify_fourier.py` F4): the L2 bound exceeds the truth by 1–2 orders of magnitude at every fixture, because `sqrt(sum N^2) ~ C(n,r')/sqrt(p)` while the truth is `~C(n,r')/p`. **The loss is exactly `sqrt(p) ~ 2^128` at the prize rows — the entire budget.**

## 4. THE PROVED PARTIALS

- **(P1) The route cut** — the round's main asset.
- **(P2) The MDS/Reed-Solomon identification.** LEMMA Y said "cyclic/BCH"; the code is in fact **MDS**, strictly sharper, and what makes T2 exact and T3 decisive.
- **(P3) `w=2` exact, full-group.** `N(0) = [C(p-1,r') + (p-1)(-1)^{r'}]/p`, exact, verified `p = 5..29`. **HONEST SCOPE: this gives neither lane depth.** It needs `q_char = n+1 = 2^41+1 = 3·83·8831418697`, not a prime power — never applies at a prize row. And `w=2` is deep in the *above*-balance regime. The mandate's hoped-for "first unconditional depth" is not there.
- **(P4) The (E) dichotomy** — `v_2(r') = v_2(w)` forces `w` to be a power of two, so the structural family is nonempty for exactly 6 of ~5.3e11 bracket values: a **characteristic-zero rederivation of round-14's R2**.
- **(P5) Scope theorem (Z5), new relative to `b1`:** LEMMA Z/MC-4 is a **prime-power theorem**. Verified `n = 4,8,16,32,9,27,25` hold for every `w`; `n = 6,10,12,15,20,24,30,36` **fail**, first at `w=2`. `n = 2^41` is inside the good case by the rules freeze.
- **(P6) The row map** — the `2^128 = n/w_min` threshold, the +42.7 and −10.85 bit margins.

LEMMA Z re-proof evidence: (Z1) identity on **1012** `(n,w)` pairs; (Z3) exhaustive **262,944** (subset,A) pairs at `n=4,8,16` and **4,713,240** subsets at `n=32` — zero misclassifications.

## 5. REFUTED PREDICTIONS (recorded openly)

**(ACC) REFUTED — and the truth is better.** Accidental counts are **quantized in multiples of `n`** (the `mu_n`-rotation preserves the window) and hit **exactly zero far below the balance point**:

| n | r' | balance p = C(n,r') | suppression p | ratio |
|---|---|---|---|---|
| 8 | 4 | 70 | 17 | 0.243 |
| 16 | 8 | 12870 | 593 | 0.046 |
| 16 | 6 | 8008 | 593 | 0.074 |
| 32 | 4 | 35960 | 3617 | 0.101 |

Suppression arrives 1–2 orders of magnitude early — evidence FOR (ES) with room to spare. New falsifier for a later round: an `(n,r')` with nonzero accidentals at some `p &gt; C(n,r')`.

**(U2) strict form REFUTED**, restricted form holds: 5 of 22 generic fixtures are slices, all degenerate (`|Sol| &lt;= 6`); all 16 populated fixtures strict.

**Also recorded (contradicts my own draft prose):** `b = 0` is **not** always the argmax — 4 of 18 rows have `max_b N(b) &gt; N(0)` (e.g. `n=16, p=113`: `N(0)=102`, `max=120`). Both consumers need the worst target, and it is not always the structured one.

## 6. THE HONEST VERDICT AND THE FRONTIER

**Internal-provable?** Partly — P1–P6 are internal and now proved, and CATCH-15A discharges MC-4 by citation at zero cost.

**Transfer-provable?** **NO, and this is now a theorem.** Every classical instrument is either vacuous at these parameters or provably blind. The one classical result that is exact — the MDS weight enumerator — is exact at the wrong granularity.

**The precise frontier:**

&gt; Let `C` be the `[2^41, 2^41−w+1, w]` Reed-Solomon code over `F_p` (`p ~ 2^256` prime, `2^41 | p−1`) with zeros `zeta,...,zeta^{w-1}`, `w in [2^34, 2^39]`. Show its **only 0/1 codewords of weight `r' = 2^40 − w` are the `mu_M`-periodic ones**, i.e. the count is exactly `C(n/M, r'/M)`, and `0` when `M` does not divide `r'`.

The obstruction is structural, not effort: (1) it must be sensitive to the arithmetic of the defining set (T3: 32 vs 0 at the same parameters); (2) it cannot be an absolute-value route (proved to lose `n log2(4/pi) ~ 3.8e11` bits); (3) it cannot be a first- or second-moment route (`sqrt(p) ~ 2^128` loss, measured); (4) it must use the balance inequality, since there is a **verified witness that accidents DO occur above balance** (`q=97, n=32, t=2`: 160 accidents at size 6, 81% non-coset-union giant block).

That is a **zero-count problem below the square-root barrier** — open research, but not *coding-theory* open research.

**What a Pro brief should ask.** NOT: weight-distribution bounds, Carlitz-Uchiyama, Delsarte LP, dual-distance. Instead, in order: (1) the zero-count question directly, to people who prove exact vanishing (Deligne-Katz, p-adic/Newton-polygon), not coding theorists; (2) **Chevalley-Warning / Ax-Katz** — `p`-divisibility of solution counts is the one classical family that is sensitive to the defining set and is *not* a weight-enumerator invariant; **this is the most promising untested transfer and it was not on the round-14 anchor list**; (3) why suppression arrives at `p ~ C(n,r')^{2/3}` rather than `C(n,r')`; (4) only then, subset-sums-in-subgroups (Li-Wan and successors).

## 7. FILES (all absolute)

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/PREREG.md`
- `.../verify_rows.py` — row map, budgets, Weil vacuity — **14 checks**
- `.../verify_lemmaz.py` — LEMMA Z re-proof + exact scope — **20 checks**
- `.../verify_fourier.py` — exact enumerator, `w=2` closed form, L2 barrier, suppression — **8 checks**
- `.../verify_transfercut.py` — MDS identification + route cut — **5 checks**
- `.../verify_bandlinear.py` — (U2) prefix vs generic windows — **3 checks**

## 8. FLAGS

1. **CATCH-15A** — MC-4 = `b1_char0_giant_coset_theorem`; node edits needed in `xr_band_key_lemma_pencil_mass` and `xr_mc_depth_quantization`. *Status flip — surfaced, not applied.*
2. **CATCH-15B** — `b1` has no proof.md, no verifier, dangling `refs`. `verify_lemmaz.py` is the repair.
3. **CATCH-15C** — round-14's "no weight enumerator string in repo" claim is false; the identification predates LEMMA Y.
4. **The terminal is shared by FOUR lanes**, not two. Suggest renaming it **(ES) entropic suppression** and wiring one node all four consume.
5. **Ax-Katz / Chevalley-Warning is the untested transfer** the route cut does not kill — recommend as the Pro-brief lead.
6. The crossing-side `log2 q_char = 127.977 ~ n/w_min` threshold appears new; the band-side 208.4759 is banked. Please confirm the crossing one is not banked elsewhere.

result: Shared terminal (mysteries 1+4, and in fact 4 lanes) unified as (ES) entropic suppression; the "external-shaped" label is REFUTED by a proved route cut — the question is not a function of the weight enumerator, so MacWilliams/Delsarte-LP/Krawtchouk/Sidelnikov/BCH-HT-Roos cannot decide it even in principle, and Weil/Carlitz-Uchiyama is vacuous by 13.5–107 bits at all four prize rows; 6 proved partials incl. the MDS/Reed-Solomon identification and the prime-power scope theorem; 50 checks 0 failures; 3 catches (MC-4 = the PROVED node b1, dischargeable now); Pro brief should ask Ax-Katz, not coding theory.