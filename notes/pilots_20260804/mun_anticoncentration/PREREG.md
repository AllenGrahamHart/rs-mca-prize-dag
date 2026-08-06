# PRE-REGISTRATION — the shared terminal: arithmetic anti-concentration over mu_n

Round 15, 2026-08-06. Written BEFORE any computation in this pilot.
Mandate: TEST the "external-shaped" label on A5/A6 before the program
pays for outside help.

## 0. The object (both consumers, verbatim sources)

**Crossing consumer (mystery 4).** `critical/nodes/rate_half_list_adjacent_crossing`,
prize-max razor row

```text
n = 2^41,  k = 2^40,  q < 2^256,  log2 q in (255.900, 256),
a_L >= k + 2^34            (RHL-LB, proved floor)
a_IJ = floor(sqrt(n(k-1))) + 1 = 1554944255988    (Johnson anchor)
w := a_L - k  in  [2^34, 2^39]   (bracket as recorded in
                                  crossing_w2_opening/verify3_prizerow.py:49)
r' = n - k - w = 2^40 - w
```

By MC-1 (`background/nodes/xr_band_key_lemma_pencil_mass`, PROVED) with
`u = X^{n-1} + c X^{k+w-1}`, `H = x_0 mu_n`, the codewords of agreement
`>= k+w` are indexed by
`{T <= H : |T| = r', e_1(T) = ... = e_{w-1}(T) = 0, prod T = gamma}`.

**Band consumer (mystery 1).** `critical/nodes/xr_band_maximal_window_divisor_count`
(SL-2-RES), three prize rows, all `n = 2^41`:

| row | k | h | band-proper d | r' = n-k-d |
|---|---|---|---|---|
| prize 1/4 | 2^39 | 2^33+1 | [2^32+1, 2^33-1] | 1649267441664 - d |
| prize 1/8 | 2^38 | 2^33+1 | [2^32+1, 2^33-1] | 1924145348608 - d |
| prize 1/16 | 2^37 | 2^32+1 | [2^31+1, 2^32-1] | 2061584302080 - d |

budget `25 |R_d(u,v)| <= 17 n^2`, i.e. `0.68 n^2 = 3.28670...e24 = 2^81.442`.
`R_d` = monic squarefree split degree-`r'` divisors `E_T | X^n - 1` with the
top `d` coefficients of `u E_T` and of `v E_T` (mod `X^n - 1`) vanishing,
PLUS maximality (clause 2), selected liveness (clause 3), strip survival
(clause 4).

**Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
`n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
`j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`. Consequently
`p > w` on the whole crossing bracket and `p > 2^33 > d` on every band
depth: **Newton's identities are invertible at every one of the four
rows**, so a vanishing PREFIX of elementary symmetric functions is
equivalent to a vanishing prefix of power sums at all four rows.

## 1. Pre-registered claims

### (U) THE UNIFIED STATEMENT and its exact scope

- **(U1)** The crossing count is exactly a constant-weight count in an
  explicit p-ary cyclic code:
  ```text
  W_w = { x in {0,1}^n <= F_p^n : wt(x) = r',  x in C(n, p, Z_w) }
  ```
  where `C(n,p,Z_w)` is the cyclic code of length `n` over `F_p` with
  defining zero set `Z_w` = the p-cyclotomic closure of `{1,...,w-1}`
  mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.
  This is LEMMA Y, BANKED round 14 — cited, not claimed.
- **(U2) NEW, decisive, falsifiable.** The BAND window is **not**
  indicator-linear for a generic received pair. Precisely: the set
  `{1_S : S satisfies clause 1 of SL-2-RES}` is the weight-`r'` slice of a
  coset of an `F_p`-linear subspace of `F_p^n` **iff** the window is
  (equivalent to) a PREFIX coordinate subspace in `e`-space, which happens
  for MC-shaped two-term words and not for generic `(u,v)`.
  **Prediction:** at small fixtures, generic `(u,v)` give a clause-1
  solution set whose `F_p`-affine hull contains weight-`r'` points that
  FAIL clause 1; two-term MC words do not.
  **Falsifier:** a generic `(u,v)` fixture whose clause-1 set IS a code
  slice, or an MC fixture where it is not.
- **(U3)** Consequently the honest unified statement is at the level of
  **0/1 points of prescribed weight on a prescribed affine subspace of
  locator-coefficient (`e`) space**; the cyclic-code constant-weight form
  is the PREFIX sub-case, which is exactly the crossing instance and the
  band's extremal/MC instance. I pre-register that I will report this
  scope split rather than overclaim a single code statement.

### (Z) LEMMA Z — char-0 structural classification at n = 2^m

Let `n = 2^m`, `S <= Z/n`, `chi_S(X) = sum_{i in S} X^i`. Suppose
`chi_S(zeta^s) = 0 in C` for `s = 1..w-1` (`zeta` primitive n-th root of 1).
Put `A = floor(log2(w-1))`, `M = 2^{A+1}` (= least power of two `>= w`),
`L = n/M`. **Claim:** `chi_S` is divisible by `(X^n-1)/(X^L-1)`, hence `S`
is `L`-periodic, hence `T = zeta^S` is a union of cosets of `mu_M`.
Conversely every such union satisfies the conditions.
Therefore `W_w^struct` is nonempty iff `M | r'`, and then
`|W_w^struct| = C(n/M, r'/M)`.
**Falsifier:** one `n = 2^m`, `w`, `S` with all `chi_S(zeta^s) = 0`
(`s < w`) and `S` not `n/M`-periodic.

### (E) EXISTENCE DICHOTOMY at the crossing row

At `n = 2^41, k = 2^40`: `v_2(r') = v_2(w)` exactly, so `M | r'` and
`M >= w` force `w` to be an exact power of two.
**Prediction:** the char-0 structural family exists for exactly the SIX
values `w = 2^34..2^39` of the bracket and is EMPTY for the other
`~5.3e11` values; and this reproduces, from the char-0 side, the
independent round-14 finding R2 ("MC-3 applies iff `w` is a power of
two"). **Falsifier:** any mismatch with R2, or a non-power-of-two `w` in
the bracket with a nonempty structural family.

### (B) BUDGET / PHASE-TRANSITION MAP

Define the equidistribution exponent
`Lam(w) := log2 C(n, r') - |Z_w| * log2 p`.
**Predictions:**
- (B1) `Lam` is strictly decreasing on the bracket and changes sign
  INSIDE `[2^34, 2^39]`; I predict the crossover at
  `w* ~ 2^35.7` for `delta = 1` (and smaller for `delta = 2, 4`).
- (B2) Hence the RAW crossing count is heuristically `2^(1.5e12)`-ish at
  the bottom of the bracket and `< 1` at the top: **the raw count is NOT
  bounded by any polynomial in `n` at the bottom of the bracket**, so
  "`<= 0.68 n^2`" cannot be the shared terminal in raw form.
- (B3) Even the *proved* structural lower bound beats the band budget at
  the crossing row: at `w = 2^34`, `|W^struct| = C(2^7, 2^6 - 1)` which I
  predict is `> 0.68 n^2 = 2^81.44` by more than 40 bits.
- **Falsifier:** `Lam(w) < 0` throughout the bracket, or
  `C(2^7,2^6-1) <= 0.68 n^2`.

### (F) EXACT FOURIER FORMULA (the transfer test)

With `psi` a nontrivial additive character of `F_{p^delta}`,
`f_a(X) = sum_{s=1}^{w-1} a_s X^s`:
```text
|W_w| = p^{-delta(w-1)} * sum_{a in F_{p^delta}^{w-1}}
           [z^{r'}] prod_{i in Z/n} (1 + z psi(f_a(zeta^i))).
```
**Prediction:** exact (verified to the last unit) at small fixtures.
**Falsifier:** any mismatch with brute force.

### (W) WEIL / CARLITZ-UCHIYAMA VACUITY

The `a != 0` terms are governed by incomplete character sums
`sum_{x in mu_n} psi(f_a(x))` with `deg f_a <= w-1`. The Weil bound for
such sums over a multiplicative subgroup is nontrivial only when
`(w-1) * sqrt(p^delta) < n`.
**Prediction:** at every one of the four rows this FAILS:
crossing `(w-1) sqrt(q_char) >= 2^34 * 2^19.5 = 2^53.5 >> 2^41 = n`;
band `>= 2^31 * 2^19.5 = 2^50.5 >> 2^41`.
So the classical weight-enumerator/Weil transfer is **VACUOUS at all four
prize rows**, and becomes non-vacuous only for `w-1 < n/sqrt(q_char) <~ 2^21`.
**Falsifier:** an admissible row/depth with `(w-1) sqrt(p^delta) < n`.

### (M) SECOND MOMENT / L2

For `w = 2` put `N(b) = #{S : |S| = r', sum_{i in S} zeta^i = b}` for
`b in F_{p^delta}`. Then `sum_b N(b) = C(n,r')` and I pre-register the
exact identity
```text
sum_b N(b)^2 = p^{-delta} * sum_{a in F_{p^delta}} | [z^{r'}] prod_{i}
                (1 + z psi(a zeta^i)) |^2 * p^{delta}   (to be pinned exactly)
```
in the form `sum_b N(b)^2 = #{(S,S') : sum_S = sum_{S'}}`.
**Prediction (the barrier):** the L2/variance method controls the number
of bad targets but NOT the maximum; specifically I predict
`max_b N(b) / avg_b N(b)` stays `> 1 + c` for a constant `c > 0` as `p`
grows with `n` fixed, while the L2 bound on `max` is trivial.
**Falsifier:** `max_b N(b) = avg (1 + o(1))` uniformly, or an L2 bound
that does beat the max in the fixtures.

### (X) w = 2 EXACT SUB-CASES

- (X1) Full-group case `n = p-1` (`mu_n = F_p^*`, `delta = 1`): I predict
  the exact closed form
  `N(0) = (1/p)[C(p-1,r') + (p-1)(-1)^{r'}]` for `0 <= r' <= p-1`,
  from `prod_{t in F_p}(1 + z omega^t) = 1 + z^p`.
  **Falsifier:** any small `p` where it fails.
- (X2) I predict this case NEVER occurs at a prize row (would need
  `q = n+1 = 2^41 + 1` a prime power; `2^41+1 = 3 * 83 * 8831418697`),
  so (X1) is an honest toy, not a prize-row closure.
- (X3) I predict that for a proper subgroup `mu_n < F_p^*` there is no
  such closed form and the count genuinely depends on `p` (not only on
  `n, r'`) — consistent with THEOREM Q.
  **Falsifier:** a `p`-independent formula matching all fixtures.

### (ACC) ACCIDENTAL LAW (extends the round-14 accidental tables)

`|W_w| = |W_w^struct| + |W_w^acc|`. **Prediction:** for fixed `n, r', w`
the accidental count satisfies
`|W_w^acc| = C(n,r') / p^{|Z_w|} * (1 + O(p^{-1/2}))` once
`C(n,r') / p^{|Z_w|}` is large, i.e. the accidental part is
binomial/equidistributed to square-root accuracy.
**Falsifier:** a systematic multiplicative deviation bounded away from 1
across a p-sweep.

## 2. Subtraction (hard law 5) — declared BEFORE claiming anything

Cited, NOT re-derived:
- MC-1/MC-2/MC-3/MC-5 window system and coset lemma
  (`background/nodes/xr_band_key_lemma_pencil_mass`).
- `xr_mc_depth_quantization` (excludes the canonical MC/coset
  construction at band-proper depths, official odd `h`).
- Round-14 LEMMA X (general-T product equidistribution), THEOREM Q
  (p-only dependence), LEMMA Y/MW (`W_w <= BCH_w`, equality at `w <= p`;
  the constant-weight-in-cyclic-code identification; the MC window is a
  codim-`w` coordinate subspace), the `p >= 2^39+1` row arithmetic.
- Round-13 fullrank pilot: the ROUTE CUT (full rank buys no
  anti-concentration), the dual form, THEOREM SHIFT, the `M^2`-slack
  self-reduction and its TRANSFER GAP.
- Newton-identity linearization is BANKED IN THE L1 LANE
  (`critical/nodes/l1_mixed_petal_amplification/statement.md` 376-404).
- "BCH-type low-weight window" is BANKED for a DIFFERENT object (L1
  Mersenne collision words, same file 968-995) — a FALSE FRIEND, not
  claimed here.
- A dedicated repo-wide sweep for `weight enumerator / weight
  distribution / Carlitz / Uchiyama / Weil / character sum / Gauss sum /
  Lam-Leung / vanishing sum / constant weight / Krawtchouk / Delsarte /
  second moment` is running and its verdict is recorded in REPORT.md
  BEFORE any novelty claim is made. Nothing in section 1 is claimed as
  new until that sweep returns ABSENT for it.

Dead routes not to be re-walked: the sub-Johnson list-size route, the
`sl2` averaged single-member window route (`W_d(z)` large does not
refute SL2), and the round-13 full-rank route (proved to buy no
anti-concentration).

## 3. Measurement plan (all `tools/ramguard tiny -- python3`, exact ints)

1. `verify_lemmaz.py` — LEMMA Z: brute-force all `S <= Z/n` for
   `n = 4,8,16,32`, all `w`, exact arithmetic in `Z[X]/(X^n-1)`; check the
   periodicity classification and the count `C(n/M, r'/M)`; check (E) at
   the prize row by exact integer arithmetic.
2. `verify_rows.py` — (B) and (W): exact big-integer `Lam(w)` on the
   crossing bracket and the three band depth ranges; the crossover `w*`;
   the structural-vs-budget comparison (B3); the Weil-vacuity margins.
3. `verify_fourier.py` — (F), (X1), (M), (ACC): exact Fourier formula vs
   brute force; the `w = 2` closed form; the second-moment identity; the
   `max/avg` anti-concentration ratio across a `p`-sweep at `n = 8, 16`.
4. `verify_bandlinear.py` — (U2): clause-1 solution sets for MC-shaped
   vs generic `(u,v)` at small fixtures; `F_p`-affine hull test.

No Modal, no network. Anything larger becomes a COMPUTE REQUEST.
