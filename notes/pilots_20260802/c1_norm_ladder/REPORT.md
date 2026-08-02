# Pilot report: C1 weight-stratified norm ladder (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable.
Coordinator verification and adopted posture: FABLE_AUDIT.md alongside.

---

# C1 lane pilot — the weight-stratified norm ladder and the c_w^(N/4) law

**Directory:** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/`
Nothing outside it was written; nothing committed or pushed. All compute via `tools/ramguard local -- python3 ...` (note: `ramguard` requires the literal `--` separator; the task text omitted it).

## HEADLINE VERDICTS

**F1 — FIRED. The c_w^(N/4) law as stated (one c_w valid across all N) is FALSIFIED, at two independent places, and the falsification has an exact repair with a proved mechanism.**

- Failure 1 (2N=8 -> 2N=16, w=4): predicted 8^2 = **64**, observed **196**. Ratio 49/16.
- Failure 2 (2N=16 -> 2N=32, w=8): predicted 2176^2 = **4 734 976**, observed **14 760 962**. Ratio 7380481/2367488.
- 17 of the 19 testable doubling steps pass exactly (ratio exactly 1).
- Both failures occur at exactly the same place: **w = the ring dimension of the lower level**. The repaired law, which survives every test performed, is

  **maxnorm(N, w) = maxnorm(N/2, w)^2  for all 1 <= w <= N/2 - 1**, and it fails at w = N/2.

  Equivalently: log maxnorm is *exactly* linear in N through the origin at fixed w, i.e. maxnorm(N,w) = c_w^(N/4), but only for N >= N_min(w) ~ 2w — not from the bottom of the ladder. c_w is **not** always an integer (c_6 = sqrt(1154)).

**F2 — DID NOT FIRE. The router survives as a finiteness tool.** The exceptional set is finite, explicitly enumerated, and sparse at every weight, with an exact q-independent threshold T(2N,w) = maxnorm(2N,w): *any admissible q > T carries no ternary relation of weight <= w.* At 2N=32 the complete census over **all** 16 weights is **23 194 primes, largest 1 568 247 649** — 5/49 of admissible q at the w<=3 cut, 24/259 at w<=4, 1422/24845 (5.7%) at w<=7. Density is a few percent and declining, not dense.

## Exact definitions used (lifted from the prior pilot, not guessed)

- **Admissible prime**: q prime with **q == 1 (mod 2N)** (`low_weight_router.py`: `p % args.twoN == 1`).
- **Ternary weight-w relation**: d in {-1,0,1}^N with exactly w nonzero entries and Sum d_i omega^i == 0 (mod q), omega of exact order 2N. **The vector has N = (2N)/2 entries** — the prior pilot's half-section `coeffs = [pow(omega,i,q) for i in range(N)]`, `N = twoN//2`.
- **Norm**: Norm(f) = Res(f, x^N+1) = det(mult-by-f on Z[x]/(x^N+1)); q carries a weight-w relation <=> q | Norm(f) for some ternary f of weight w. q-independent.

**Scale correction to the task brief:** at 2N=32 the search space is 3^16 = 43 046 721, **not** 3^32; supports are C(16,w) x 2^w, not C(32,w) x 2^w. Consequently **2N=32 is fully exhaustible at every weight**, which is what I did. (The brief's "c_w^8 at 2N=32" is nonetheless exactly the test I ran: it is the statement maxnorm(2N=32,w) = maxnorm(2N=16,w)^2.)

## Symmetry group

Prior pilot's orbit notion (`structure_checks.py`, `scaling_transfer.py` divide the weight profile by 2N) is **U = {+-x^i : 0 <= i < N}**, order 2N.
- Norm(x) = zeta^(N^2) = 1 and Norm(-f) = (-1)^N Norm(f) = Norm(f) for N even => U preserves Norm **exactly**.
- Z[x]/(x^N+1) ~ Z[zeta_2N] is a domain (2N a 2-power) => U acts **freely** on nonzero f; every U-orbit has size exactly 2N. Verified exhaustively at N=4,8 (`results/slice_check.json`, 0 violations).

I additionally used the full norm-preserving group **G = <U, x -> x^u : u in (Z/2N)*>**, order 2N.phi(2N) = 2N^2. Galois preserves Norm exactly (permutes conjugates) and is a signed permutation of the monomial basis, so preserves ternariness and weight. |U|/|G| = 8/32, 16/128, 32/512, 64/2048 at 2N = 8/16/32/64. G-orbit counts by Burnside (Fix(g) generating function = prod over cycles with sign product +1 of (1 + 2z^|C|)); U-counts cross-checked against the free-action formula C(N,w)2^w/(2N).

**Enumeration reduction used (exact):** every nonzero f is U-equivalent to one with constant term +1, so the slice {d_0 = +1} attains the same norm **set** and the same max at every weight. Size 3^(N-1). Verified exhaustively at N=4,8 (max and full value-set identical, `slice_check.json`).

## The mechanism (two lemmas — these are the real result)

**LEMMA A (doubling embedding).** N = 2M. iota: Z[y]/(y^M+1) -> Z[x]/(x^N+1), g(y) -> g(x^2) preserves the coefficient multiset (hence weight and ternariness) and **Norm_N(iota g) = Norm_M(g)^2**.
*Proof:* iota g has even part g and odd part 0, so one step of the field-norm descent (f(x)f(-x) = g(x^2), g = f_e^2 - y f_o^2) gives g^2, whence Norm_N(iota g) = Norm_M(g^2) = Norm_M(g)^2. QED. Verified exhaustively for M = 2,4,8 (0 violations).
**Corollary A': maxnorm(N,w) >= maxnorm(N/2,w)^2 always.** So the "law" is one-sided for free; its content is *tightness*.

**LEMMA B (AM-GM ceiling).** Norm(f) = prod over the N/2 conjugate pairs of |f(zeta^j)|^2 >= 0 (so the resultant is non-negative — checked: 0 negatives over all 3^8 at N=8), and Sum_{j odd} |f(zeta^j)|^2 = N ||f||^2 = Nw (negacyclic Parseval). AM-GM => **maxnorm(N,w) <= w^(N/2)**.

**Corollary B' (free saturation propagation).** If maxnorm(M,w) = w^(M/2) then maxnorm(2M,w) = w^M — >= by A', <= by B. **This closes an infinite family with no enumeration**: since w in {1,2,3} saturate at N=4 and w=7 saturates at N=8, for every N >= 8 a power of two

  **maxnorm(N,1)=1, maxnorm(N,2)=2^(N/2), maxnorm(N,3)=3^(N/2), maxnorm(N,7)=7^(N/2), proved unconditionally.**

**Observable signature of the law:** in the stable range the argmax is *imprimitive* (even-supported = iota of the level-below argmax); the law fails at exactly the weight where the optimum first becomes primitive. Visible below in the argmax column.

## Weight-stratified tables (all values exact; `+`/`-`/`.` = coefficient +1/-1/0, index 0 leftmost)

### 2N = 8 (N = 4) — EXHAUSTIVE (3^4), census EMPTY
| w | max Norm | w^(N/2) | sat | n_w^U | n_w^G | #distinct norms | argmax f |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | YES | 1 | 1 | 1 | `+...` |
| 2 | 4 | 4 | YES | 3 | 2 | 2 | `+.+.` |
| 3 | **9** | 9 | YES | 4 | 2 | 2 | `++-.` |
| 4 | 8 | 16 | | 2 | 1 | 1 | `++++` |

Global max **9**; smallest admissible prime is 17 > 9 => **no admissible prime carries any relation** (prior pilot reproduced exactly).

### 2N = 16 (N = 8) — EXHAUSTIVE (3^8), census = 11 primes <= 881
| w | max Norm | w^4 | sat | n_w^U | n_w^G | #distinct | argmax f |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | YES | 1 | 1 | 1 | `+.......` |
| 2 | 16 | 16 | YES | 7 | 3 | 3 | `+...+...` |
| 3 | 81 | 81 | YES | 28 | 6 | 4 | `+.+.-...` |
| 4 | 196 = 14^2 | 256 | | 70 | 12 | 9 | `++.+-...` |
| 5 | 529 = 23^2 | 625 | | 112 | 17 | 11 | `+++-+...` |
| 6 | 1154 = 2.577 | 1296 | | 112 | 17 | 13 | `+++-++..` |
| 7 | **2401 = 7^4** | 2401 | YES | 64 | 10 | 9 | `+++--+-.` |
| 8 | 2176 = 2^7.17 | 4096 | | 16 | 3 | 2 | `+++++-++` |

Census (all with Bareiss + sympy recheck): 17(w3, `++.+....`, Norm 17), 97(w4, Norm 194 = 2.97), 113(w5), 193(w5), 241(w5), 337(w7), 353(w6, Norm 706), 401(w5), 433(w5), 577(w6, Norm 1154), 881(w7). **Exactly the prior pilot's eleven primes with identical minimal weights.**

### 2N = 32 (N = 16) — EXHAUSTIVE AT EVERY WEIGHT (3^15 = 14 348 907 slice members)
| w | max Norm | w^8 | sat | n_w^U | n_w^G | #distinct | new primes | argmax f |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | YES | 1 | 1 | 1 | 0 | `+...............` |
| 2 | 256 | 256 | YES | 15 | 4 | 4 | 0 | `+.......+.......` |
| 3 | 6561 = 9^4 | 6561 | YES | 140 | 14 | 10 | 5 | `+...+...-.......` |
| 4 | 38416 = 14^4 | 65536 | | 910 | 71 | 53 | 19 | `+.-...+.+.......` |
| 5 | 279841 = 23^4 | 390625 | | 4368 | 292 | 185 | 136 | `+.-.+.+.+.......` |
| 6 | 1331716 = 1154^2 | 1679616 | | 16016 | 1040 | 642 | 233 | `+.+.-.+.+.+.....` |
| 7 | 5764801 = 7^8 | 5764801 | YES | 45760 | 2900 | 1549 | 1029 | `+.+.-.+.+.+.-...` |
| **8** | **14760962 = 2.7380481** | 16777216 | | 102960 | 6506 | 3711 | 1221 | `++-.-+..++..+...` |
| 9 | 38950081 = 79^4 | 43046721 | | 183040 | 11510 | 6621 | 3812 | `+-+++.-..+.+..+.` |
| 10 | 84580802 | 100000000 | | 256256 | 16114 | 10367 | 3031 | `++++--+..+.+-...` |
| 11 | 184497889 | 214358881 | | 279552 | 17556 | 12130 | 5804 | `+++---+--+-.....` |
| 12 | 342386306 | 429981696 | | 232960 | 14644 | 11497 | 3517 | `++++-+-++.-++...` |
| 13 | 777684769 | 815730721 | | 143360 | 9016 | 7710 | 3004 | `+-+-++--+++++...` |
| 14 | 1040410946 | 1475789056 | | 61440 | 3880 | 3226 | 1024 | `+---+--+-+++++..` |
| 15 | 1612931233 | 2562890625 | | 16384 | 1040 | 987 | 359 | `++---+--+-+++++.` |
| 16 | **2311094272 = 2^15.70529** | 4294967296 | | 2048 | 136 | 74 | 0 | `+++--++-+-++++++` |

Note the argmax column: **even-supported (imprimitive) for w <= 7, primitive from w = 8** — exactly where the law breaks.

### 2N = 64 (N = 32) — weights 1-6 EXHAUSTIVE, weight 7 PROVED, weights 8-32 OPEN
| w | max Norm | status | argmax f |
|---|---|---|---|
| 1 | 1 | exhaustive (also proved) | `+`... |
| 2 | 65536 = 4^8 | exhaustive (also proved) | `+...............+...............` |
| 3 | 43046721 = 9^8 | exhaustive (also proved) | `+.......+.......-...............` |
| 4 | 1475789056 = 14^8 | exhaustive | `+...-.......+...+...............` |
| 5 | 78310985281 = 23^8 | exhaustive | `+...-...+...+...+...............` |
| 6 | 1773467504656 = 1154^4 | exhaustive (3 chunks) | `+...+...-...+...+...+...........` |
| 7 | **33232930569601 = 7^16** | **PROVED by the A'/B sandwich, not enumerated** | witness = iota of the 2N=32 w=7 argmax, Bareiss- and sympy-verified |

Every 2N=64 exhaustive value equals the 2N=32 value squared — a **fourth ladder point** confirming the repaired law at w <= 6.

## The c_w table (stable range only)

| w | stable from N | law | c_w (exponent N/4) |
|---|---|---|---|
| 1 | 4 | 1^(N/4) | 1 = 1^2 |
| 2 | 4 | 4^(N/4) | 4 = 2^2 |
| 3 | 4 | 9^(N/4) | 9 = 3^2 |
| 4 | 8 | 196^(N/8) | 14 (< 4^2 = 16) |
| 5 | 8 | 529^(N/8) | 23 (< 5^2 = 25) |
| 6 | 8 | 1154^(N/8) | **sqrt(1154) ~ 33.97 — irrational** (< 6^2 = 36) |
| 7 | 8 | 2401^(N/8) | 49 = 7^2 |
| >=8 | — | untestable | c_9 = 79 at N=16 only (one point) |

By Lemma B, c_w <= w^2, with **equality exactly at the saturating weights** {1,2,3,7} — the weights admitting a perfectly flat ternary polynomial. The "9, 7^4, 14^4, 23^4" ladder that motivated the conjecture is thus two different phenomena glued together: 9 and 7^4 are AM-GM saturations (c = w^2), 14^4 and 23^4 are strict deficits.

## Actual observed scaling where the law fails (w = N, full support)

| 2N | maxnorm(N,N) | factorisation | ratio to ceiling N^(N/2) |
|---|---|---|---|
| 8 | 8 | 2^3.1 | 1/2 |
| 16 | 2176 | 2^7.17 | 17/32 |
| 32 | 2311094272 | **2^15.70529** | 70529/131072 |

maxnorm(N,N) = 2^(N-1).P_N with P_4=1, P_8=17, P_16=**70529** — each P_N an admissible prime, and the ratio to the ceiling creeping up (0.5, 0.53125, 0.5381...). Growth is **not** exponential-in-N-through-the-origin here: 2176/8^2 = 34, 2311094272/2176^2 = 488.1.

## Exceptional-prime census

| level | weights | # admissible primes | smallest | largest |
|---|---|---|---|---|
| 2N=8 | 1-4 (complete) | **0** | — | — |
| 2N=16 | 1-8 (complete) | **11** | 17 | 881 |
| 2N=32 | 1-16 (**complete**) | **23 194** | 97 | 1 568 247 649 |
| 2N=64 | 1-6 (partial) | 14 441 | 193 | 330 076 815 361 |

Router thresholds T(2N=32, w) (any admissible q > T carries no relation of weight <= w): 1, 256, 6561, 38416, 279841, 1331716, 5764801, 14760962, 38950081, 84580802, 184497889, 342386306, 777684769, 1040410946, 1612931233, 2311094272.

Exact F2 densities at 2N=32 (# exceptional / # admissible q <= T): w<=2: 0/2; w<=3: **5/49**; w<=4: **24/259**; w<=5: **160/1522**; w<=6: **393/6405**; w<=7: **1422/24845**.

Sample certificates (all re-verified by Bareiss determinant **and** by `sympy.resultant`):
- 2N=32, q=97, w=3, f = `+-.+............`, Norm = 97, cofactor 1.
- 2N=32, q=193, w=3, f = `++..+...........`, Norm = 193, cofactor 1.
- 2N=32, w<=3 census is exactly {97, 193, 257, 353, 449}; w<=4 is exactly the prior pilot's 24 primes {97,193,257,353,449,577,641,673,929,1153,1217,1249,1409,2113,2273,2593,2689,3137,3457,4001,4129,4993,5857,7937}; w<=5 is exactly 160 primes (prior pilot: 160). **Closed loop with the prior pilot's independent router.**
- 2N=32, largest census prime q = 1 568 247 649, min weight 15, f = `+--+-+---++++++.`, Norm = 1568247649, cofactor 1.
- 2N=64, w<=3 census (15 primes): {193, 257, 449, 641, 7937, 14657, 15809, 21569, 27457, 33409, 48449, 63361, 65537, 65921, 204353}; e.g. q=193, f = `+.+.....+.......................`, Norm = 37249 = 193^2.

**q = 70529 cross-check.** Present at 2N=32 with **minimal weight 7**, matching the prior pilot exactly. Certificate: f = `++++.-.+..+.....` = [1,1,1,1,0,-1,0,1,0,0,1,0,0,0,0,0], **Norm = 70529, cofactor 1**. It divides some weight-w norm at w in {7, 8, 9, 12, 13, 16} and at no other weight. It is absent from the 2N=16 census (as it must be — it exceeds 2401) and present in the 2N=64 w<=6 census. New observation worth flagging to the ledger lane: **70529 is exactly the odd part of the global maximum norm at 2N=32**, 2311094272 = 2^15 . 70529 — the same prime the dynamics side flagged as the hard-regime maximal-excess row shows up as the full-weight norm champion.

## Non-exhaustive probe at 2N=64, w=8 (the weight where the law broke one level down)

Out of budget exhaustively (336 585 600 slice members). Steepest-ascent hill climb (neighbourhood: move one nonzero to any empty slot with either sign, or flip one sign) **calibrated on 2N=32 w=8, where it recovered the true exhaustive maximum 14760962**, plus 1 000 000 uniform random weight-8 samples. Best found: **217 885 999 165 444 = 14760962^2** — exactly the law prediction, attained by the embedding witness; **nothing above it**. Non-exhaustive: consistent with, does not prove, the repaired law at w=8. (Reported as such in `results/probe_2N64_w8.json`.)

## Verification discipline

Three independent code paths agree on every claim: (1) the vectorised field-norm descent used for enumeration (int64 for N<=16 with a written-out overflow bound 1->16->2048->1.68e7->5.6e14 << 2^63; 3-prime Garner CRT for N=32, valid while Norm < 1.15e18, guaranteed by Lemma B); (2) the prior pilot's fraction-free Bareiss determinant, run on **every** argmax and **every** census witness; (3) `sympy.resultant(f, x^N+1)` on all 38 argmaxes and 111 census witnesses — **0 failures**. Descent vs Bareiss also checked exhaustively over all 3^4 and all 3^8 ternary vectors. Every emitted certificate is a decimal string; there are no floats in any certificate field (the two density fields are exact `Fraction`s rendered `num/den`).

## Honest caveats / what is incomplete

1. **2N=64 weights 8-32 are NOT done.** Weight 8 alone is 336.6M slice members at ~33 us each ~ 3 h; a 32x multiplicative-symmetry quotient exists but canonicalisation costs more than it saves at this scale. Weight 7 is *proved*, not enumerated. So the repaired law is confirmed at four ladder points for w <= 6, at three for w = 7 (two enumerated + one proved), and **never tested above w = 8 at more than one level**.
2. **The repaired law is verified, not proved**, for w in {4,5,6} (and conjectural for w >= 8). Only the >= direction (Lemma A') and the saturating weights {1,2,3,7} are theorems. The natural next theorem is: *for w <= N/2 - 1 the norm-maximising ternary f in Z[zeta_2N] is imprimitive* — that single statement implies the whole stable-range law by induction.
3. c_9 = 79 (max = 79^4 at N=16) rests on **one** ladder point and is untested.
4. The census values are the primes dividing *attained* norms; I did not certify that no admissible prime was missed by factorisation — but every value is < 2^32 at 2N=32 and factored by `sympy.factorint`, which is exact.
5. Weights 8-16 at 2N=32 give a census of 23 194 primes; I verified 50 randomly sampled witnesses with sympy, not all 23 194 (all were verified by the independent Bareiss path).

## File inventory (all under `notes/pilots_20260802/c1_norm_ladder/`)

**scripts/** — `norm_core.py` (definitions, Bareiss reference, Python-int descent, int64/2-prime/3-prime batch norms, symmetry-group construction, Burnside; runnable self-test), `slice_check.py` (d0=+1 reduction and U-freeness, exhaustive at N=4,8), `small_tables.py` (exhaustive 2N=8 / 2N=16 tables + census), `enum_weight.py` (weight-stratified enumeration with `--part/--nparts` chunking), `orbits.py` (Burnside n_w^U, n_w^G), `census.py` (two-pass factor + witness census), `ladder.py` (part merge, Lemma A check, sandwich closure, F1 test), `probe.py` (sandwich certificates + 2N=64 w=8 probe), `summary.py` (thresholds, F2 density, c_w, full-weight anomaly), `verify.py` (independent sympy resultant audit).

**results/** — `selftest_norm_core.json`, `slice_check.json`, `table_2N8.json`, `table_2N16.json`, `orbit_counts.json`, `n16/N16_w01..w16.json` + `_norms.npy` (per-weight checkpoints, all 16 complete), `n32/N32_w01..w06.json` + `_norms.npy` (+ the three `w06_p*of3` part files), `census_2N32.json` (7.1 MB, complete), `census_2N64_w1to6.json` (6.0 MB, partial), `ladder.json`, `probe_2N64_w8.json`, `summary.json`, `verify_sympy.json`.

## Recommended consequence for the C1 lane

The prior pilot's retargeting item 1 ("bound max|Res| over ternary weight-w f — the c_w^(N/4) conjecture") should be **restated** before it is proved: the correct statement is the imprimitivity conjecture above, with the free saturating family {w=1,2,3,7 at every N} already a theorem, and the honest caveat that the base c_w need not be an integer or even rational. Item 2 (orbit counts n_w) is now closed combinatorially: n_w^U = C(N,w)2^w/(2N) exactly (free action, proved), and n_w^G is tabulated above by Burnside — these are the ledger's A_j multiplicities and need no further estimation.
