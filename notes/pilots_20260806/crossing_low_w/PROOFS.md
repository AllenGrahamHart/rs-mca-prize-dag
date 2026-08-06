# PROOFS — the LOW-w CROSSING CORE (round 18)

Opus pilot, `notes/pilots_20260806/crossing_low_w/`. Everything here is
registered in `PREREG.md` §X0–X9 **before** computation. Machine checks in
`toy_gate.py` (stages `strat / biject / fibre / accident / census / oddeven /
orbit`, plus a permanent `failclosed` stage that exits 1) and
`prize_exhibit.py` (stages `row / search / verify / coverage / wcover`,
plus `failclosed`).

---

## §0. Setup and the objects, quoted

`n = 2^m`, `S <= Z/n`, `|S| = r'`, `x_s(S) = sum_{i in S} zeta_n^{si}`.

**The window system**, verbatim
`notes/pilots_20260804/crossing_w2_opening/PREREG.md:19-22`:

> ```text
> W_w := {S <= Z/n : |S| = r', e_s(T(S)) = 0 for s = 1..w-1}
> ```

**Newton linearisation**, verbatim
`notes/pilots_20260804/crossing_w2_opening/PREREG.md:48-56`:

> - **(Y) Newton/BCH linearization, valid iff `w <= p`.** For `char p > w-1`,
>   Newton's identities give
>   `e_1 = ... = e_{w-1} = 0  <=>  p_1 = ... = p_{w-1} = 0`,
>   and `p_s(T(S)) = x_0^s * chi_S(zeta^s)`

and the row bound that makes it always apply, verbatim
`notes/pilots_20260804/mun_anticoncentration/PREREG.md:41-44`:

> **Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
> `n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
> `j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`.

**The (ES) target**, verbatim
`notes/pilots_20260804/mun_anticoncentration/PREREG.md:88-91`:

> Therefore `W_w^struct` is nonempty iff `M | r'`, and then
> `|W_w^struct| = C(n/M, r'/M)`.

**LEMMA STRAT**, verbatim `notes/pilots_20260806/es_coprimality/PROOFS.md:143-151`:

> > **LEMMA STRAT.** Suppose `strat(S) >= a >= 1`, i.e. `S` is
> > `(n/2^a)`-periodic. Put `n_a = n/2^a`, let `S' <= Z/n_a` be the
> > reduced set (`|S'| = r'/2^a`) ... Then
> > 1. `x_s = 0` whenever `2^a` does not divide `s`;
> > 2. `x_{2^a t} = 2^a * iota(p_t(S'))` ...

**The binding stratum**, verbatim
`notes/pilots_20260806/es_g_lanes/PROOFS.md:221-223`:

> At `a = v−1`: `n_a = 2^{42−v}`, exactly ONE condition survives
> (`s = 2^{v-1}`, since `2·2^{v-1} = 2^v > w−1`), so `|Z^{(a)}| ∈ {1,2}`

and the gap this pilot attacks, verbatim
`notes/pilots_20260806/es_g_lanes/REPORT.md:103`:

> **At `w = 2^34` the deepest stratum requires `log2 p >= 256` (ε=+1) or
> `>= 128` (ε=−1), and no admissible row reaches either**

Admissibility of tower rows, verbatim
`critical/nodes/axis8_generating/proof.md:13-14` (status PROVED):

> The official family admits non-generating rows. Therefore the tower case is
> admissible and must be priced by the `ext_lift` / `f1_classification` chain.

and the cap, verbatim `critical/nodes/rules_freeze/statement.md:9`:

> smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256;

---

## §1. LEMMA DS — the deep stratum, exactly (G1)

> **LEMMA DS.** Let `n = 2^41`, `w = 2^v`, `r' = 2^40 − w`, `a = v−1`. Put
> `n_a = 2^{42−v}`, `L = n_a/2 = 2^{41−v}`. Then
>
> ```text
> r'_a = r'/2^a = 2^{41−v} − 2 = L − 2,
> ```
>
> the surviving condition set is the single index `t = 1`, and
>
> ```text
> {S in W_w : strat(S) >= v−1}  <->  {S' <= Z/2L : |S'| = L−2, p_1(S') = 0},
> ```
>
> a bijection with **no side condition**. Under it, `S` is structural
> (`strat(S) >= v`) iff `S'` is a union of antipodal pairs `{j, j+L}`.

**Proof.** `r'/2^{v-1} = (2^{40} − 2^v)/2^{v-1} = 2^{41−v} − 2`. The multiples
of `2^a = 2^{v-1}` in `[1, w−1] = [1, 2^v − 1]` are exactly `s = 2^{v-1}`, so by
LEMMA STRAT (1) every other condition holds identically and by LEMMA STRAT (2)
the surviving one is `x_{2^{v-1}}(S) = 2^{v-1} p_1(S')`, which vanishes iff
`p_1(S') = 0` because `p` is odd. Structural means `strat(S) >= log2 M = v`,
i.e. `S` invariant under `+ n/2^v`, i.e. `S'` invariant under `+ L` in `Z/2L`.
Directly: `S = {j + 2L t}`, so `x_{2^{v-1}}(S) = sum_{j in S'} theta^j`
summed `2^{v-1}` times, `theta = zeta_n^{2^{v-1}}` of order `2L`. ∎

At `v = 34`: `(n_a, r'_a, L) = (256, 126, 128)` — the brief's instance.

*Machine check:* `toy_gate.py strat` — 348,102 checks, 0 failures, exhaustive
over every `mu_{2^a}`-periodic `S` at all three toy shapes, in char 0
(`Z[X]/(X^{n/2}+1)`) and in `F_p` for five primes each.

**X0 confirmed:** `r'_a = L − 2` at every shape, and at the prize row
(`prize_exhibit.py row`).

---

## §2. LEMMA FREE — the lift constraint is EMPTY (G2, and it REFUTES the
brief's conjecture)

The brief conjectured (`PREREG.md:59-64`) that *"the lift constraints kill
every non-structural reduced solution"*, the constraints being *"the
un-collapsed even-index conditions"*.

> **LEMMA FREE.** At the deepest stratum `a = v−1` there are no un-collapsed
> conditions at all. The number of surviving lift constraints is **0**.

**Proof.** Immediate from LEMMA DS: the only `s in [1, w−1]` with `2^{v-1} | s`
is `s = 2^{v-1}` itself, which is *the* reduced condition, not a lift
constraint. Every other `s` is killed identically by LEMMA STRAT (1),
independently of `S'`. ∎

*Machine check:* `toy_gate.py biject` — 81,005 checks, 0 failures. For every
`S'` at every toy shape and every prime, membership of the lift in `W_w`
(decided by **direct** evaluation of all `w−1` conditions, no lemma used) is
**identical** to `p_1(S') = 0`. Counts: at `(64,16)`, `p = 193`:
72 members = 72 reduced solutions, 56 structural — i.e. **16 non-structural
members**, and at `p = 257, 449, 641`: 56 = 56 = 56.

**Consequence.** The conjecture the brief asked me to test is FALSE, and it is
false for a structural reason, not a numerical one. G4 is therefore the live
branch. This is pre-registered as X1 and was registered before any run.

### 2.1 Where the brief's intuition IS right — LEMMA OE

The "even-index conditions" idea is correct at every *shallower* stratum. Let
`theta` have order `2L`, `S' <= Z/2L`, and put

```text
eps_j = [j in S'] − [j+L in S']  in {0,+1,−1},
sig_j = [j in S'] + [j+L in S']  in {0,1,2}.
```

> **LEMMA OE.** `p_t(S') = sum_j eps_j theta^{tj}` for `t` ODD, and
> `p_t(S') = sum_j sig_j (theta^2)^{(t/2)j}` for `t` EVEN.

**Proof.** `theta^{t(j+L)} = theta^{tj}(theta^L)^t = (−1)^t theta^{tj}`, since
`theta^L` is the unique element of order 2. Split the sum over antipodal
pairs. ∎

So ODD conditions constrain only `eps`; EVEN conditions constrain only `sig`
and are literally the conditions of the next stratum. At the **deepest**
stratum the only condition is `t = 1`, odd — hence LEMMA FREE. The brief's
mechanism is real but **vacuous exactly where the obstruction binds**.

*Machine check:* `toy_gate.py oddeven` — 1,108,832 checks, 0 failures;
exhaustive over all `2^8` and all `2^16` subsets, sampled at `2L = 32`.

---

## §3. LEMMA TC — the ternary collapse, and the corrected pricing (G2)

> **LEMMA TC.** The single deep-stratum condition depends on `S'` only through
> `eps in {0,±1}^L`. The fibre over `eps` has size
> `C(L−U, (r'_a−U)/2)` where `U = |supp(eps)|`, nonempty iff `U ≡ r'_a (mod 2)`
> and `U <= r'_a`; and
>
> ```text
> sum_{eps} C(L−U(eps), (r'_a−U(eps))/2)  =  C(2L, r'_a).
> ```
>
> `eps = 0` is exactly the structural fibre, of size `C(L, r'_a/2)`.

**Proof.** LEMMA OE at `t = 1`. Given `eps`, the pairs with `eps_j != 0` are
forced (one element each, `U` in total); the pairs with `eps_j = 0` are "both"
or "neither", and `|S'| = r'_a` forces exactly `B = (r'_a−U)/2` of the `L−U`
zero-pairs to be "both". Summing the fibres partitions all `r'_a`-subsets. ∎

*Machine check:* `toy_gate.py fibre` — 24,522 checks, 0 failures; the identity
exhaustively over all `3^L` ternary vectors at `L = 4, 8, 10` for **every**
`r'_a`, and in closed form up to `L = 128` (the prize stratum).

### 3.1 The three functionals, at the prize deep stratum (`v = 34`, `L = 128`)

| functional | requirement on `log2 p` | value |
|---|---|---|
| GLOBAL `(ES-G)` — `es_g_lanes/PROOFS.md:226` | `n_a/|Z^{(a)}|` | **256** |
| PER-WEIGHT (retired) | `log2 C(256,126)` | **251.628** |
| **TERNARY (this pilot)** | `L·log2 3` | **202.875** |
| TERNARY, orbit-corrected (§5.1) | `L·log2 3 − log2(2L)` | **194.875** |

Computed exactly in `prize_exhibit.py row`. The per-weight functional
**mis-prices this stratum by 48.75 bits** because its solutions are fibred,
not independent: it counts `S'`, of which there are `C(256,126)`, when the
primitive object is `eps`, of which there are `3^128`.

---

## §4. THEOREM DSA — deep-stratum accidents EXIST (G4)

> **THEOREM DSA (unconditional).** Let `delta_a = ord_{2L}(p)`, so
> `theta = zeta_n^{2^{v-1}}` generates `F_{p^{delta_a}}` over `F_p`. If
>
> ```text
> p^{delta_a} < 2^{L−2}
> ```
>
> then there is `eps in {0,±1}^L`, `eps != 0`, with `sum_j eps_j theta^j = 0`,
> `U(eps)` even and `2 <= U(eps) <= L−2 = r'_a`. Consequently (LEMMA DS +
> LEMMA TC) `W_w` contains a **non-structural** member, so
>
> ```text
> |W_w|  >=  C(n/M, r'/M) + C(L−U, (r'_a−U)/2)   >   C(n/M, r'/M),
> ```
>
> i.e. **the (ES) crossing instance is FALSE at that row.**

**Proof.** Consider the `2^{L−2}` vectors `a in {0,1}^L` with `a_{L−1} = 0` and
`|a|` even (choose `a_0..a_{L−2}` freely subject to even parity: `2^{L−2}` of
them). Map `a |-> sum_j a_j theta^j in F_{p^{delta_a}}`, a set of size
`p^{delta_a} < 2^{L−2}`. By pigeonhole two distinct `a != b` collide. Put
`eps = a − b in {0,±1}^L`. Then `eps != 0`,
`sum_j eps_j theta^j = 0`, `supp(eps) = a Δ b` so
`U = |a| + |b| − 2|a ∩ b|` is **even**, and `eps_{L−1} = 0` gives `U <= L−1`,
hence `U <= L−2` by parity. LEMMA TC then gives a nonempty fibre with
`B = (r'_a−U)/2 >= 0` since `r'_a = L−2 >= U`. Any member of that fibre lifts
(LEMMA DS) to `S in W_w`, and it is non-structural because `eps != 0`. ∎

**No balance is used**: the argument is `|domain| > |codomain|`, not
`c·log2 V >= n` nor `>= log2 C(n,r')`. (PREREG F5 self-check, §7.)

### 4.1 The explicit prize-row exhibit

Row, taken **verbatim** from `notes/pilots_20260806/es_g_lanes/PROOFS.md:174-179`
(already certified there as satisfying *"every rules-freeze constraint"*):

```text
p = 6597069766657 = 3*2^41 + 1   (prime; p ≡ 1 mod 2^41, so delta = 1)
e = 6,  q = p^6,  log2 q = 255.509775 < 256,  2^41 | q−1,  k = 2^40
B* = floor(q/2^128), log2 B* = 127.510
```

Re-derived independently here (`prize_exhibit.py row`, 19 checks): `p` prime
(deterministic Miller–Rabin), `delta = 1`, `q < 2^256`, `2^41 | q−1`,
`B* >= 3`, `w = 2^34 <= p` (Newton), `p >= 2^39+1`, `delta_a = ord_256(p) = 1`,
`theta = zeta^{2^33}` of order 256. `log2 p = 42.585 < 126 = L−2`, so
THEOREM DSA applies.

`prize_exhibit.py search` produced (49 raw relations in a `3^30` window,
31.2 predicted) a relation with `U = 20`:

```text
support = [0,2,3,4,5,9,10,11,12,13,14,17,19,21,23,24,25,26,27,29]
eps     = [-1,-1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,1]
```

`prize_exhibit.py verify` — **2854 checks, 0 failures** — establishes at
`n = 2^41` itself:

* `S' <= Z/256`, `|S'| = 126`, and `p_1(S') = sum_{j in S'} theta^j = 0` in
  `F_p` by **direct summation over all 126 elements** (not via the relation);
* `S'` is **not** an antipodal-pair union, so the lift is non-structural;
* `|S| = 2^33 · 126 = 1082331758592 = 2^40 − 2^34 = r'` (exact integers);
* `x_{2^33}(S) = 2^33 · p_1(S') = 0`;
* for every other `s in [1, 2^34−1]`: `x_s(S) = (sum_{j in S'} zeta^{sj})·G(s)`
  with `G(s) = sum_{t<2^33} eta^{st}`, `eta = zeta^{256}` of order `2^33`.
  `G(s) = prod_{i=0}^{32}(1 + eta^{s·2^i})`, and with `v = v_2(s) <= 32` the
  factor at `i = 32−v` is `1 + eta^{2^32·odd} = 1 + (−1) = 0`. So `G(s) = 0`.
  Verified numerically on **1320 sampled `s` across all 33 valuation classes**
  plus boundary values, with the product formula itself cross-checked against
  brute summation, and the factorisation `x_s(S) = (sum_j)(sum_t)`
  re-verified exhaustively at `n = 64` and `n = 128`.

Hence `S in W_{2^34}` and `S` is not `mu_{2^34}`-periodic:

```text
|W^struct| = C(128,63) = 2^124.149
this single relation contributes C(108,53) = 24405824773509487458170913508896 = 2^104.267
=> |W_{2^34}| >= C(128,63) + 24405824773509487458170913508896  >  C(128,63).
```

**(ES) is FALSE at an admissible crossing row.** (The heuristic *total* excess
at this row is `~C(256,126)/p = 2^209.0`, i.e. the true count exceeds the
structural count by ~85 binary orders of magnitude; only the `2^104.267` above
is proved.)

### 4.2 Which admissible rows fall (`prize_exhibit.py coverage`)

Over the 19 admissible `(p-class, e)` pairs of `es_g_lanes/REPORT.md:46-51`
(reproduced here from scratch: 19, confirmed), at `w = 2^34`:

```
ALL = 10 pairs   (whole admissible p-range provably accident-carrying)
PART = 6 pairs   (log2 p < 126 for delta_a = 1;  log2 p < 63 for delta_a = 2)
NONE = 3 pairs
```

and the dichotomy is clean:

> **`e = 1` rows are NEVER in the provable regime.** `B* >= 3` forces
> `q = p >= 3·2^128`, i.e. `log2 p >= 129.585 > 126 = L−2`.

So THEOREM DSA kills **tower rows only** — exactly the rows
`es_g_lanes/REPORT.md:184` identified as *"the adversary's best choice against
(ES-G)"* — and leaves the recorded prime rows `q = p ~ 2^256` untouched.

---

## §5. The prime rows, re-priced (X4 — HEURISTIC, not proved)

At the recorded rows (`mun REPORT.md:48`: *"recorded rows `q = p` PRIME
~2^256, `delta = 1`"*), `log2 p ≈ 256`. The expected number of nonzero ternary
relations is `3^128/p = 2^{202.875−256} = 2^{−53.1}`, and orbit-corrected
(§5.1) `2^{−61.1}`.

**This is a counting heuristic and is labelled as such.** But it replaces a
0.089-bit *failure* of the global functional with a **53–61 bit margin**, and
it is a strictly better-founded count than the retired per-weight form (which
gave only 4.37 bits and, as §3.1 shows, mis-prices the stratum by counting
fibred objects as independent).

### 5.1 LEMMA ROT — why the naive count over-predicts

> **LEMMA ROT.** The relation set is closed under `eps -> −eps` and under the
> twisted rotation `(R eps)_0 = −eps_{L−1}`, `(R eps)_j = eps_{j−1}`; `R` has
> order `2L`. Hence relations come in orbits of size dividing `2L`.

**Proof.** `sum_j (R eps)_j theta^j = theta·sum_{j<L−1} eps_j theta^j −
eps_{L−1}`; and `theta·sum_{j<L} eps_j theta^j = 0` gives
`theta·sum_{j<L−1} eps_j theta^j = −eps_{L−1}theta^L = eps_{L−1}`. ∎

*Machine check:* `toy_gate.py orbit`, 66 checks, 0 failures. At `(64,16)`,
`L = 8`, `2L = 16`:

| `p` | relations | orbits | naive `#eps/p` | orbit-corrected |
|---|---|---|---|---|
| 193 | 16 | **1** | 15.67 | 0.98 |
| 257 | 0 | 0 | 11.77 | 0.74 |
| 449 | 0 | 0 | 6.73 | 0.42 |
| 577 | 16 | **1** | 5.24 | 0.33 |
| 641 | 0 | 0 | 4.72 | 0.29 |

Observed 2 orbits; orbit-corrected prediction 2.76; naive prediction 44.1.
The naive functional over-predicts accidents by the factor `2L`. In the
tables of §6 I nevertheless use the **naive** `3^L` threshold, because it
over-states the accident zone and is therefore conservative against every
cleanliness claim I make.

---

## §6. G3 — the refined covered/uncovered split (`prize_exhibit.py wcover`)

Banked, `es_coprimality/REPORT.md:79`: THEOREM CS already makes every
`w > w* = 2^37.3131` unconditional. The CS-uncovered set is
`w in {2^34, 2^35, 2^36, 2^37}`. At the **binding (deepest) stratum**:

```
   w      rows   PROVED-ACCIDENT     EXPECTED-ACCIDENT    EXPECTED-CLEAN
   2^34    19    10 full +  6 part   16 full + 3 part      0 full
   2^35    19     3 full +  5 part   10 full + 6 part      3 full
   2^36    19     0 full +  0 part    2 full + 6 part     11 full
   2^37    19     0 full +  0 part    0 full + 0 part     19 full
   2^38    19     0 full +  0 part    0 full + 0 part     19 full
   2^39    19     0 full +  0 part    0 full + 0 part     19 full
```

Per-`w` thresholds (`L = 2^{41−v}`, exact):

| `w` | `L` | `n_a` | `r'_a` | global | per-weight | **TERNARY** | provable-existence |
|---|---|---|---|---|---|---|---|
| `2^34` | 128 | 256 | 126 | 256 | 251.628 | **202.875** | `log2 p < 126` |
| `2^35` | 64 | 128 | 62 | 128 | 124.082 | **101.438** | `log2 p < 62` |
| `2^36` | 32 | 64 | 30 | 64 | 60.491 | **50.719** | `log2 p < 30` |
| `2^37` | 16 | 32 | 14 | 32 | 28.812 | **25.359** | `log2 p < 14` |
| `2^38` | 8 | 16 | 6 | 16 | 12.967 | **12.680** | `log2 p < 6` |
| `2^39` | 4 | 8 | 2 | 8 | 4.807 | **6.340** | `log2 p < 2` |

Since every admissible `p >= 2^39+1`, the provable-existence column is
unreachable for `w >= 2^36`, and the ternary threshold is below `2^39` for
`w >= 2^37` — so **the deep stratum is expected-clean at every admissible row
for `w >= 2^37`, and at `w = 2^36` only for `log2 p < 50.719`.**

**The exact remaining set**, stated plainly:

1. `w = 2^34`: (ES) **REFUTED** on 10 of 19 `(class,e)` pairs outright and on
   part of 6 more; the rest is expected-accidental. Only the `e = 1` sub-range
   `log2 p > 202.875` is expected clean — which is where the recorded rows sit.
2. `w = 2^35`: (ES) **REFUTED** on 3 pairs outright, part of 5 more.
3. `w = 2^36`: nothing proved; a heuristic accident zone at `log2 p < 50.719`.
4. `w = 2^37`: deep stratum expected clean everywhere; **no proof**.
5. **What is NOT covered by any of this:** strata `a < v−1`, including `a = 0`.
   My work re-prices and refutes at the *binding* stratum only.

---

## §7. Self-checks

**F5 — no balance smuggling.** THEOREM DSA uses only pigeonhole
(`|domain| > |codomain|`). It never asserts `c·log2 V >= n` or
`>= log2 C(n,r')`. It is *consistent* with
`es_g_lanes/REPORT.md:103` (*"no admissible row reaches either"*) and
explains it: the global functional's failure at these rows is not an artefact,
there really are accidents there. The TERNARY functional of §3.1 **is** a
counting functional and is used **only** in the explicitly heuristic §5/§6
columns, never in a proof.

**F6 — AK-UNIT.** `es_axkatz_transfer/REPORT.md:44` forbids routes concluding
a congruence on the count. My conclusions are (i) existence of an individual
`S in W_w` and (ii) the inequality `|W_w| > C(n/M, r'/M)`. Neither is a
congruence, and no congruence on `|W_w|` is asserted or used. **PASSES.**

**F1/F2 — the registered falsifiers of the brief's conjecture** both fired in
the direction I registered (X1): the lift is free, and the toy accidents lift.

**F7 — the failed first search, reported not buried.** My first `search`
implementation enumerated even-weight `0/1` subsets of a 24-index window and
looked for birthday collisions, predicting ~5.3 per window; it found **0 in
six windows**. The prediction was wrong, not the code: collisions from an
`m`-window are **clustered** — one vanishing `eps` of support `U` yields
`2^{m−U}` colliding pairs — so the count of *distinct* relations with support
in an `m`-window is `3^m/p`, which at `m = 24` is `0.043`, not `5.3`. The toy
had already shown exactly this over-dispersion (16-or-0). LEMMA ROT (§5.1) is
the structural explanation. THEOREM DSA is unaffected: it uses all `L = 128`
coordinates, where `2^{L−2} = 2^126 > p`. The search was resized to a ternary
meet-in-the-middle over 30 coordinates (`3^30/p = 31.2` expected, 49 observed).

**Ground truth (F4).** `toy_gate.py census` — a FULL exhaustive census of
`W_8` at `n = 32, r' = 8` over all `C(32,8) = 10,518,300` subsets (by exact
meet-in-the-middle, not sampling), at five primes: `|W_8| = 4` = `C(4,1)` =
the structural count, at every `p`, with **no non-structural member at any
stratum**. This matches the deep-stratum prediction there (`L = 4`, `r'_a = 2`
admits no `U = 2` relation, since `theta^{i−j} = ∓1` is impossible for
`i != j` in `[0,4)` when `theta` has order 8).

**Fail-closed, proven not asserted.** `toy_gate.py failclosed` and
`prize_exhibit.py failclosed` inject a false check and exit **1**; every other
stage exits **0**.

---

## §8. What is NOT proved

1. **Emptiness at prime rows is NOT proved** — §5 is a counting heuristic.
2. **Strata `a < v−1` are untouched**, including `a = 0`. LEMMA OE gives the
   recursive structure but I did not carry it out.
3. **The `w = 2^36, 2^37` deep strata** are expected clean but have no proof.
4. **The sig/`gamma` shell.** `crossing_w2_opening/PREREG.md:26` defines the
   crossing count as `X_w(gamma) = #{S in W_w : prod T(S) = gamma}`. I refute
   the (ES) statement about `|W_w|`; I computed `sig(S) = 1941325217792` for
   the exhibit but did **not** determine which `gamma`-shells the accidents
   populate, nor the consequence for `L_1`.
5. **`delta_a = 2` rows** are handled only through the crude bound
   `p^{delta_a} < 2^{L−2}`; a Frobenius-adapted pigeonhole would do better.
6. **Scale of the toy gate** is `n in {32, 64, 128}`; the prize-row statements
   are consequences of lemmas proved for all `n`, and the prize exhibit is
   verified at `n = 2^41` itself, not extrapolated.
