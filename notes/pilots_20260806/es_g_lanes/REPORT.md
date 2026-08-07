(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# (ES-G) LANE RE-CHECK — ROUND 17 REPORT

**Verdict in one line: of the four consuming lanes, only u2c can cite (ES-G) — its pin IS the global form. The rate-1/16 band row and the dli RES row are ABOVE global balance at EVERY admissible parameter, so their routing to the terminal is BROKEN; the crossing row is above global balance at explicit admissible rows and, under the C4-a stratum clause, at *every* admissible row for w = 2^34; the rate-1/4 and 1/8 band rows are broken on the low-depth fifth of their own scope.**

## 0. What was run

All under the ramguard law from `/home/u2470931/smooth-read-solomin/prize`. Files (all inside my dir, nothing else touched, no commits):

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/PREREG.md` — coordinator brief + my §4–§7 appended **before** any computation
- `.../esg_lib.py` — exact closure machinery + certified balance comparator
- `.../esg_selftest.py` — **1413 checks, 0 failures**, fail-closed
- `.../esg_analysis.py` — L1–L5 tables; `.../full_run.txt`, `.../esg_analysis.log` — outputs
- `.../PROOFS.md` — derivations with verbatim `file:line` for every statement relied on

Method note: **no float decides a boundary case.** Verdicts come from a 140-digit Decimal comparator with an explicit `10^-110` pad and a `10^-40` UNDECIDED gate; the closure closed-form is validated against brute force at `m = 5..16` over *all* `p` of order 1, 2, 4.

---

## 1. (L1) TRUE |Z_w| PER ROW

The condition count for the crossing (prefix/cyclic) instance is the **p-closure size**, and the base is **p, not q** — `crossing_w2_opening/REPORT.md:69` (THEOREM Q, PROVED): *"For every `q` with `n | q−1`, `W_w` and its entire sig-profile depend on `q` only through `p = char F_q` — never through `e` in `q=p^e`."* Since `ord_{2^m}(p) | 4` iff `p ≡ ±1 mod 2^{m-2}`, every admissible characteristic lies in exactly **eight** residue classes mod `2^41`. Exact closed forms (`w = 2^v`, `v = 34..37`):

| `p` class mod `2^41` | `delta` | exact `|Z_w|` | ratio to `w−1` |
|---|---|---|---|
| `1` | 1 | `w−1` | `1` |
| `2^40+1` | 2 | `3·2^{v−1} − 1` | ≈1.5 |
| `2^40−1`, `2^41−1` | 2 | `2(w−1)` | `2` |
| `2^39+1`, `3·2^39+1` | 4 | `11·2^{v−2} − 1` | ≈2.75 |
| `2^39−1`, `3·2^39−1` | 4 | `6·2^{v−1} − 2` | ≈3 |

For the **band/syzygy** rows there is no cyclotomic closure at all: the window is *"`2d` generic forms … not cyclic, not a slice"* (`mun REPORT.md:49`), so `c = 2d` exactly over base `q`, and for the syzygy branch `c = rank J_d ∈ [2h−d+ell, 2d]` by (SL2-ABN) (`xr_band_forced_commonroot_syzygy_count/statement.md:105`). For **u2c**, `c = t` over `q` (frozen wording) or `|B0|` (catch #11). For **dli RES**, `c = L_j` over the generated field (catch #13).

**CATCH-B.** The banked bracket `w-1 <= |Z_w| <= delta(w-1)` (`mun PREREG.md:60`) is correct but **its top is never attained at delta = 4** — the maximum is `3(w−1)`, i.e. `0.75·delta(w−1)`. Pricing a `delta = 4` row at the bracket top over-credits it by 33%.

**CATCH-C.** At `w = 2^38, 2^39` the two `ε=−1, delta=4` classes merge orbits (`s ↦ 2^39 − s`) and drop from ≈`3(w−1)` to **exactly** `2(w−1)`. The ratio is not `w`-uniform across the bracket; a single measured ratio must not be transported.

**My P1 is REFUTED AS STATED** and I record it as such: I registered the ratio set as exactly `{1, 3/2, 2, 11/4, 3}`; the true set carries `−1` offsets and is not `w`-uniform. The `|Z_w|` closed forms themselves are right and validated.

---

## 2. (L2) GLOBAL-BALANCE STATUS PER LANE — INCLUDING THE SIGN FLIPS

### Crossing (`|Z_w|·log2 p >= 2^41`), over all 19 admissible `(p-class, e)` pairs:

```
w=2^34: ALWAYS sub-balance  0, FLIPS  8, NEVER 11
w=2^35: ALWAYS sub-balance 10, FLIPS  5, NEVER  4
w=2^36 .. 2^39: ALWAYS 19, FLIPS 0, NEVER 0
```

C4-d's suspected sign flip is **confirmed and localised**: it is the `w ∈ {2^34, 2^35}` end, and the driver is **`e`, not `delta`** — THEOREM Q makes the tower degree free for the count while `q = p^e < 2^256` divides the available `log2 p` by `e`. **A tower row buys no balance and pays full price.**

Explicit admissible counterexample (P2 **FIRES**), every rules-freeze constraint satisfied:

```
p = 6597069766657 = 3·2^41 + 1  (prime, p ≡ 1 mod 2^41, delta = 1)
e = 6,  q = p^6,  log2 q = 255.509775 < 256,  2^41 | q−1,  k = 2^40
B* = floor(q/2^128), log2 B* = 127.510  >  log2 S(2^34) = 117.149  (so w = 2^34 is live here)
|Z_w|·log2 p − n = −1.467419e12   ->  ABOVE GLOBAL BALANCE
```

### Band (`2d·log2 q >= 2^41`), band-proper `d ∈ [ceil(h/2), h−2]` (`WIRING.md:59`), in scope per `xr_band_maximal_window_divisor_count/statement.md:5` (*"the three prize rows and high band-proper depths"*):

| rate | band-proper `d` | verdict over `q ∈ [2^209, 2^256)` |
|---|---|---|
| 1/4 | `[2^32+1, 2^33−1]` | FLIPS — sub-balance only for `d >= n/(2 log2 q)` |
| 1/8 | `[2^32+1, 2^33−1]` | FLIPS — same |
| **1/16** | `[2^31+1, 2^32−1]` | **NEVER** |

Rate 1/16, exact integers: `2d <= 2^33 − 2` and `log2 q < 256` give `2d·log2 q < (2^33−2)·256 = 2^41 − 512 < 2^41 = n`. Deficit ≥ **512 bits even in the limit q → 2^256**, rising to **1.0995e12 bits** at the bottom of the depth range (required `log2 q = 511.999999762` there).

Rates 1/4, 1/8: the lowest depth `d = 2^32+1` needs `log2 q >= 255.999999940` — a **6e-8-bit** sliver below the cap. Above-balance zone: `d ∈ [2^32+1, 5260821185]` = **22.5%** of band-proper at the banked pin `q >= 2^209`; **2.4%** at the `q >= 2^250` convention.

Syzygy (`d ∈ [ceil((2h+2)/3), h−2]`), both ends of the rank bracket per §2 clause 2: rates 1/4, 1/8 are ALWAYS sub-balance at nominal `c = 2d`, but **FLIPS at `d = h−2` under the worst rank deficit (SL2-ABN) permits**; rate 1/16 is **NEVER** at both ends.

### u2c and dli RES

u2c's row sits at global balance **by construction** — its own sliver `log2 Q ∈ [255.9113, 256)` is exactly the region where `t·log2 Q >= n`. dli RES is **strictly above** global balance by proof (see §4).

---

## 3. (L3) THE STRATUM CONDITION AND THE BINDING STRATUM

**Crossing.** The C4-a reduction, made exact: for `T` a union of `μ_{2^a}`-cosets, `p_s(T) = 2^a·p_{s'}(Y)` when `s = 2^a s'` and `0` otherwise, so

```
n_a = 2^{41−a},  W_a = 2^{v−a} − 1,  r'_a = r'/2^a,  |Z^{(a)}| = |closure of {1..W_a} in Z/n_a|,  a = 0..v−1.
```

Non-vacuity **checked**: `r' = 2^40 − 2^v` is divisible by `2^a` for every `a <= v−1` and every `v = 34..39`, so every stratum has candidate members — these are real obligations.

**The binding stratum is the DEEPEST one, `a = v−1`, uniformly over all 8 classes and all `v` tested.** The `2^{−a}` scaling cancels between `|Z^{(a)}|` and `n_a`; what does not cancel is the collapse of the closure factor (`ord_{2^{41−a}}(p) → 1`) and the `−1` in `W_a`. At `a = v−1` exactly ONE condition survives, so `|Z^{(a)}| ∈ {1,2}` and the requirement is `log2 p >= 2^{42−v}/|Z^{(a)}|`:

| `w` | required `log2 p` (ε=+1 / ε=−1) | admissible `(class,e)` pairs that meet it |
|---|---|---|
| `2^34` | **256 / 128** | **0 of 19** |
| `2^35` | 128 / 64 | 3 of 19 |
| `2^36` | 64 / 32 | 12 of 19 |
| `2^37..2^39` | ≤32 | 19 of 19 |

**At `w = 2^34` the deepest stratum requires `log2 p >= 256` (ε=+1) or `>= 128` (ε=−1), and no admissible row reaches either** — `|F| < 2^256` forces `e·log2 p < 256`, and every `ε=−1` class has `delta ∈ {2,4}` hence `e >= 2` hence `log2 p < 128`. **P4 FIRES, 19/19.**

The sharpest form: the deep-stratum global requirement is `log2 p >= 256` — *the same 256-bit wall as the rules cap itself*. It misses by exactly the width of the admissible sliver. At that same stratum the **per-weight** requirement is only `log2 C(256,126) = 251.628`, so the recorded razor rows (`log2 q ≈ 255.9`) sit **between the two forms**, satisfying the retired one and failing the one now of record, by ≤ 0.089 bits.

**Band.** The C4-a mechanism needs conditions indexed by cyclotomic exponents; `2d` **generic** `F_q`-linear forms have no such index and nothing vanishes for free on a coset union. **There is no stratum decomposition of the band window system — the only instance is `a = 0`**, which is what §2 reports.

---

## 4. (L4) THE PER-LANE OBLIGATION UNDER (ES-G)

| lane | obligation | can it cite (ES-G)? |
|---|---|---|
| **crossing** `rate_half_list_adjacent_crossing` | zero accidents at `w = 2^v`, `v = 34..39`, at every admissible `(p,e)` with `B* >= 3` | **NO at `w = 2^34`** (all 19 pairs fail the binding stratum; and at `a=0`, 11 of 19 fail outright with an explicit exhibit). YES for `w >= 2^37`. |
| **band full-rank** `xr_band_fullrank_window_divisor_count` | `|R_d| = 0` at every high band-proper depth, all three rates | **NO at rate 1/16 (all `d`, all `q`)**; NO at rates 1/4, 1/8 for `d < n/(2 log2 q)` (22.5% of scope at the pin) |
| **band syzygy** `xr_band_forced_commonroot_syzygy_count` | same, rank-deficient branch | **NO at rate 1/16 (all `d`, all `q`, both ends of the rank bracket)**; at 1/4, 1/8 YES nominally but FLIPS at `d = h−2` under the worst (SL2-ABN) deficit |
| **u2c / dli RES** | u2c: zero non-coset extras in sub-balance. dli RES: flatness `E_U[rho_j] <= 4` | **u2c YES** — its pin *is* (ES-G). **dli RES NO, anywhere** (§4.1) |

### 4.1 CATCH-F — the dli RES lane is above balance BY ITS OWN HYPOTHESIS

`critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md:164-166`:

> ```
>     2^N >= q^L    (balanced-volume / matched-alpha; automatic at production:
>                    N = 256L and q < 2^256).
> ```

carried as a scoping hypothesis at `critical/nodes/dli_c1r3_gated_envelope_bound/statement.md:12` — *"(H2)  2^N >= q^L,  N >= 16L,"* — and proved strict at `.../notes/m4_report.md:107-108`:

> - **A2** balance: `r_L = q^L / 2^{256L} < 1` for every admissible
>   `q < 2^256` — exact integer inequality at L = 1, 2, 34.

`2^N >= q^L` is **exactly the negation of global balance** `q^L >= 2^N`, proved strict at every one of the 34 levels for every admissible `q`. The lane's object is a **flatness** statement (mean ≥ 1 ⇒ above balance); (ES-G) is a **zero-count** statement conditioned on sub-balance. **Same shape, disjoint regimes.**

This **refutes the round-15 discharge claim** at `mun REPORT.md:53` — *"**(ES) discharges all four consumers.** … **dli RES**: same file, *"the SAME hard shape as the dli RES count."*"* — "same hard shape" was read as "discharged by". It is not.

### 4.2 What replaces (ES-G) where it cannot be cited

Stated plainly, not softened: **nothing currently does.** Three concrete options, none free:
1. **Rate 1/16 (and the low-depth 1/4, 1/8):** the retired per-weight form *does* hold there (that is precisely what `log2_q_critical = 208.476` computes). Either the per-weight form must be re-posed in a non-refuted variant (weight-aware, stratum-corrected), or the band lanes need a non-balance argument. (ES-G) is not available.
2. **Crossing at `w ∈ {2^34, 2^35, 2^36}`:** the deep strata need their own treatment; the `n_a = 256`, one-condition instance is small enough to be attacked directly rather than by balance.
3. **dli RES:** an above-balance flatness instrument, which is what the lane already has (C1'/C2''/WCL-ZONE). (ES-G) should be unwired from it.

### 4.3 CATCH-D — the band's field pin is derived from the REFUTED functional

`sl2_unstructured/descent.py:211-213` computes `log2_q_critical = (lbinom(n, n−k−dlo) − b)/(2·dlo)` — i.e. `(log2 C(n,r') − log2 budget)/(2d)`, the **per-weight** functional. My selftest reproduces `208.47593052630532` to `<1e-6` and confirms the `9.48e-9` offset from the mun reading is exactly `log2(0.68 n^2)/(2d)`. The (ES-G) threshold at the same depth is `255.999999940` — **47.5 bits higher**. The `q >= 2^209` pin does not deliver (ES-G) at the depth it was computed for.

---

## 5. (L5) THE u2c PIN CHECK

Pinned functional, verbatim, `background/nodes/u2c_giant_tnull_dichotomy/node.json:10`:

> "falsifier": "Pre-registered: sub-balance (q^t >= 2^n) scaled rows with non-coset-union extras exceeding the transported n^3 budget, sustained across >= 3 scales. Above-balance window accidents do NOT count."

and `node.json:8`: *"REPAIRED CLAIM: at rows with q^t >= 2^n (sub-balance everywhere; all official prize-max rows qualify by ~2%)"*. **This is the GLOBAL form verbatim — u2c pinned the surviving reading, not the refuted one.**

Round-16's exclusion claim **CONFIRMED independently** (P5 HOLDS), by exact integer comparison of `p^{|Z_w|}` against `2^32`, with `|Z_w|` recomputed from scratch (my machinery also reproduces the report's own `|Z_w|` and `Lam` columns):

| `r'` | `w` | `p` | `delta` | `|Z_w|` | `Lam` (per-wt) | `log2 p^{|Z_w|}` | vs `n=32` |
|---|---|---|---|---|---|---|---|
| 6 | 4 | 7 | 4 | 10 | −8.284 | 28.074 | ABOVE |
| 6 | 3 | 47 | 2 | 4 | −2.429 | 22.218 | ABOVE |
| 6 | 4 | 17 | 2 | 5 | −0.648 | 20.437 | ABOVE |
| 5 | 2 | 23 | 4 | 4 | −0.475 | 18.094 | ABOVE |
| 5 | 2 | 463 | 2 | 2 | −0.090 | 17.710 | ABOVE |

The falsifier is in fact strictly *stronger* than sub-balance (it also demands super-budget extras sustained across ≥3 scales); the five witnesses fail it on all three counts.

**CATCH-E — three drifts inside the pinned node.**
1. **Three different bases in one node.** The falsifier says `q^t`; catch #11 in the same statement says the frozen `q`-wording is *"untenable"* and the window must be read at `|B0| = |F_p(D)|`; (ES-G) says `p^{|Z_w|}`. For the crossing instance THEOREM Q settles it in favour of the **smallest** (`p`) — the least favourable. The wording must be pinned to one base.
2. **The "~2%" prose is wrong** by the node's own 3C annotation: *"the '~2% sub-balance' prose is wrong in both directions: the exact admissible prize-max sliver is log2 Q in [255.9113, 256), width 0.089 bits"*. u2c's sub-balance is a 0.089-bit sliver, not a 2% margin.
3. **The four lanes' field requirements are mutually unsatisfiable.** u2c needs `log2 Q >= 255.9113`; band 1/4, 1/8 at low depth need `>= 255.99999994`; band 1/16 needs `>= 256`; dli RES needs the *opposite* inequality (`< 256` strictly, by H2). **No single row satisfies all four.** (ES-G) cannot be a shared terminal for the four lanes as currently wired.

## 6. CATCH LEDGER

- **CATCH-A (against my own script, self-caught).** My first summary column used a float compare and reported 5/8 instead of 19/19 at L3, because `log2(2^128 − 1)` rounds to exactly `128.0` in float64 and silently flipped every boundary case. My own PREREG §7 forbade it; the clause caught it. All verdicts are now from the certified comparator.
- **CATCH-B.** `delta(w−1)` bracket top never attained at `delta = 4` (max `3(w−1)`) — 33% over-credit.
- **CATCH-C.** Orbit merge at `w = 2^38, 2^39` drops the `ε=−1, delta=4` ratio from ≈3 to exactly 2; the ratio is not `w`-uniform.
- **CATCH-D.** The band `q >= 2^209` pin is the per-weight (retired) threshold; (ES-G) needs 47.5 more bits at the same depth.
- **CATCH-E.** Three bases in the u2c node; the "~2%" prose; the four lanes' mutually unsatisfiable field requirements.
- **CATCH-F.** dli RES is above global balance by its own proved scoping hypothesis; the round-15 "discharges all four consumers" claim is refuted for that lane.
- **Mechanism finding (new).** Because of THEOREM Q, **tower rows (`e >= 2`) get no balance credit from the extension degree while `e` divides the available `log2 p`.** This is the single mechanism behind every crossing-lane flip, and it makes extension rows — proved admissible by `axis8_generating` — the adversary's best choice against (ES-G).

## 7. HONEST RESIDUALS

- **Band condition count is my reading.** I priced the band at `c = 2d` over base `q` from *"2d generic forms"* (`mun REPORT.md:49`) and `descent.py`'s `2·dlo`. If the band's true effective base is the *generated* field (the band analogue of catch #11 / catch #13, which I did **not** compute), the balance bits shrink and every band verdict gets **worse**, never better. I did not construct that correction.
- **The syzygy rank bracket** uses `ell = 0` at the pessimistic end; I did not determine which end is attained. Both reported, per §2 clause 2.
- **I did not re-derive u2c's `t`-range or its sliver**; I took the node's own numbers and only checked the functional's identity and the witness exclusion.
- **The stratum obligation's scope is the coordinator's adopted reading of C4-a** (`a = 0 … log2(M)−1`). If a proved lemma excludes strata below some `a*`, the crossing verdict at `w = 2^34` softens from "fails at every admissible row" to the `a = 0` analysis — which still leaves 11 of 19 `(class,e)` pairs above balance and the explicit exhibit standing. The finding does not disappear under that softening; it shrinks.
- **No extrapolation from small `n`.** Every prize-row number is exact arithmetic at `n = 2^41` itself; the `n ∈ {16,32}` census is used only to validate machinery.
- **Two of my six pre-registered predictions were self-refuted** (P1 as stated; P4's first evaluation was wrong for the float reason). Both are reported as refutations, not quietly repaired.
