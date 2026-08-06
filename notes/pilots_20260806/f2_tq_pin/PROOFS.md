# PROOFS — the t/q pin (round 16, pilot `f2_tq_pin`)

Opus 5, 2026-08-06. Replay: `tools/ramguard tiny -- python3
notes/pilots_20260806/f2_tq_pin/verify.py` → **64 checks, 0 FAIL**,
digest `F2_TQ_PIN_VERIFY_ALL_PASS` (log: `VERIFY_LOG.txt`).

Every load-bearing statement is quoted VERBATIM with `file:line`.

---

## 0. The rules-level surface (what the freeze actually says)

`critical/nodes/rules_freeze/statement.md:9`:

> THE RULES-FACT (closed by citation, not proof): the operative prize rules are exactly — smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16} (no dither latitude); the m-quantifier per rules_m_reading (family-per-constant-m). Certificate = quote + hash of proximityprize.org and ePrint 2026/680 with a drift detector; on any residual ambiguity the campaign plans against the stricter reading.

`critical/nodes/field_cap_check/statement.md:13`:

> RESOLVED 2026-07-03: blueprint line 102 quotes the survey (= ePrint 2026/680, Arnon-Boneh-Fenzi, 'Open Problems in List Decoding and Correlated Agreement', April 2026): 'The survey focuses on rho in {1/2,1/4,1/8,1/16}, target error eps* = 2^-128, smooth domains, k <= 2^40, and |F| < 2^256.'

`background/nodes/official_row_primes_pinning/proof.md:25-33`:

> The decisive fragments are:
>
> - `assuming |F| is sufficiently large`;
> - `for every choice of F, L, and k`;
> - `k <= 2^40`;
> - `|F| < 2^256`.
>
> These are admissibility and quantifier conditions, not a list of prescribed
> prime constants.

**Reading.** The freeze pins an ADMISSIBILITY REGION and a quantifier, not
constants. There is no rules-level `p`, no rules-level `k` (extension
degree), no rules-level `q`, and no rules-level `t`. Three further facts
are rules-level *consequences*:

- **(R1)** the smooth domain is a multiplicative subgroup of `F^*` of
  2-power size `n`, hence **`n | q - 1`**, hence **`q > n`**. The repo
  states this independently at
  `archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`:
  *"THE FROBENIUS GAP — q = 1 mod n makes Frobenius act trivially on
  frequencies"*.
- **(R2)** `|F| < 2^256`, i.e. `L := log2 q < 256`.
- **(R3)** on residual ambiguity, **plan against the stricter reading**
  (`rules_freeze/statement.md:9`, quoted above). This clause is
  load-bearing in §4.

---

## 1. (P1) The provenance chain for `q`

### 1.1 What the F2 lane assumes

`notes/pilots_20260802/f2_deployed_windows/tower.py:11-18`:

> Official row: n a 2-power, p KoalaBear-shaped with p - 1 = 2^24 * 127, so
> e := v_2(p-1) = 24; gcd(n, p-1) = 2^24 = the FIXED sector; the Frobenius orbit
> of an element of order exactly 2^{24+j} has size ord_{2^{24+j}}(p) = 2^j, so
>
>     RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,
>     the descent step is the quadratic extension F_{q_j} / F_{q_{j-1}},
>     the moving coordinates are the elements of order EXACTLY 2^{24+j},
>     m_j = (n_j - n_{j-1}) / 2 = 2^{22+j} conjugate pairs.

`notes/f2_campaign/F2_CAMPAIGN_LOG.md:2158-2160`:

> Verified:
> ord_{2^40}(KoalaBear p) = 2^16 exactly — the official row IS the
> minimal field (matches the banked tower constant k ~ 2^16;

The lane's own honesty note, `f2_deployed_windows/REPORT.md:21`:

> **Genuine ambiguities flagged**: ... q = p^k not officially pinned;

### 1.2 The derivation: `q = p^{2^16}` is not an admissible row (S2)

With `p = 2^31 - 2^24 + 1 = 2130706433` (prime, `p-1 = 2^24·127`,
`log2 p = 30.988685` — S1), the tower's own `q_j = p^{2^j}` gives
`log2 q_j = 2^j · log2 p`:

| rung `j` | `log2 q_j` | vs cap 256 |
|---|---|---|
| 1 | 61.977 | admissible |
| 2 | 123.955 | admissible |
| 3 | 247.909 | admissible |
| 4 | 495.819 | **OVER CAP** |
| 16 | **2,030,874** | **OVER CAP by 7933x IN BITS** |

**Rungs 4..16 are not prize-admissible rows.** The rung-16 field violates
`|F| < 2^256` by a factor of `2^2030618`.

### 1.3 The admissible `(p, e)` region at the maximal rate-1/2 row (S3)

Let `q = p^e`, `n = 2^41`, and write `e = 2^s·u` with `u` odd. LTE gives
`v_2(p^e - 1) = v_2(p-1)` for `s = 0`, and `v_2(p-1) + v_2(p+1) + s - 1`
for `s >= 1`. Since `p` is odd, exactly one of `v_2(p±1)` equals 1, so
(R1) `2^41 | q-1` forces `log2 p >= 41 - s`. Combined with (R2)
`e·log2 p < 256`:

| `e` | `s = v_2(e)` | forced `log2 p >=` | forced `log2 q >=` |
|---|---|---|---|
| 1 | 0 | 41 | 41 |
| 2 | 1 | 40 | 80 |
| 3 | 0 | 41 | 123 |
| 4 | 2 | 39 | 156 |
| 5 | 0 | 41 | 205 |
| 6 | 1 | 40 | 240 |

`s = 3` needs `log2 q >= 8·38 = 304 > 256` — excluded, and larger `s` is
worse. Hence at EVERY admissible maximal rate-1/2 row:

```
    v_2(e) <= 2,      e <= 6,      log2 p >= 39,
    ord_n(p) in {1,2,4}  =>  TOWER DEPTH <= 2 RUNGS.
```

**Two consequences.** (a) The KoalaBear base field (`log2 p ~ 31`) is
**inadmissible** at `n = 2^41`. (b) The 16-rung tower does not exist at any
admissible row — the Frobenius orbit structure supports at most two
moving rungs, because `ord_n(p) | e <= 6` and `ord_n(p)` is a 2-power.

At `n = 2^40` (the I1 alternative) the same argument gives `log2 p >= 38`,
`e <= 6` — the conclusions are unchanged (S15).

### 1.4 An explicit admissible prize-max row (S4)

Existence is not vacuous. The verifier constructs

```
    p = 18446735827372343297   (prime, v_2(p-1) = 39 exactly, log2 p = 64.0000)
    q = p^4,   log2 q = 255.99997...  < 256
    v_2(q - 1) = 41  =>  n = 2^41 divides q-1 exactly
    ord_{2^41}(p) = 4  =>  exactly 2 moving rungs
```

This is a fully rules-admissible maximal rate-1/2 row. Its corridor edge is
`t* = 8,589,556,515` (S7.8), and it lies INSIDE the prize-max sliver.

### 1.5 `L = log2 q`: the 255.9 gate vs the 255.900-256 window

`background/nodes/xr_radius_arithmetic/proof.md:33-34`:

> - **Prize convention.** `L = log2 q = 255.9` (the "`2^{255.9}`" prize row of the
>   budget audit), `n = 2^41`, `k = rho n`.

This is a **convention**, self-labelled, not a rules citation. The
rules-level statement is only `L < 256`. **Reconciliation:** the sliver's
left endpoint is `n/t* = 255.911275` (§5), and the convention point
`L = 255.9` lies **below** it — see CATCH-2.

---

## 2. (P2) A derivation of `t`

### 2.1 What `t` counts

`t = |Lambda|`, the number of power-sum (Newton) conditions
`p_l(S) = 0`, `l in Lambda`, imposed on a block `S ⊆ mu_n`. It is defined
once, globally, not per rung — `f2_deployed_windows/REPORT.md:21`:
*"per-rung frequency set absent (c defined once, globally)"*.

### 2.2 The mechanism that fixes it

`archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`:

> (ii) THE FIRST-MOMENT BALANCE: t log2 q ~ 2.15e12 vs log2(2^n) = 2.2e12 — the prize-max giant regime sits within ~2% of the counting threshold; pure counting can NEVER close it.

Each condition `p_l(S) = 0` is **one equation over the field in which the
power sums live**, costing `log2 q` bits; the space of blocks carries `n`
bits. The window of `t`-null blocks is empty iff `q^t > 2^n`, i.e.

```
                        t · L  >=  n .                                (C)
```

The exact FM+gate refinement is `xr_radius_arithmetic/proof.md:41-43`:

> ```
> t* = min { t : E[X] <= B* }
>    = min { t : log2 C(n, n-k-t) + (1 - t)L <= L - 128 }
>    = min { t : t * L  >=  log2 C(n, n-k-t) + 128 }.                        (T*)
> ```

Solving (T*) at `L = 255.9`, `n = 2^41` reproduces the banked table to the
last digit at all four rates (S5): `8592912739 / 7014660390 / 4722556392 /
2943177800`.

### 2.3 The formula, and the rules-forced interval

To leading order `log2 C(n, n-k-t) = n - O(1) - 2t²/(n ln 2)`, so (T*) and
(C) agree to `0.0044%` (S6.1, S6.3) and

```
                        t  =  n / L  ·  (1 + O(1e-4)).                (F)
```

`t` is therefore **not a free constant**: it is `n/L`. Applying (R1)
`L > log2 n = 41` and (R2) `L < 256` to (F) at `n = 2^41`:

```
        2^41/256  <  t  <=  2^41/41 ,        i.e.   8.590e9 < t <= 5.364e10 .
```

The lower endpoint is exactly `2^33 = 8,589,934,592`, attained as
`L → 256`. Under the **base-field** reading (conditions counted as
`F_p`-equations, valid for Frobenius-stable blocks) the divisor is
`log2 p >= 39` (§1.3), giving the slightly weaker cap `t <= 5.639e10`
(S6.7). At `n = 2^40` the interval is `(4.295e9, 2.749e10]` (S15).

### 2.4 Independent corroboration of the lower endpoint

Two other lanes land on `2^33` for `n = 2^41`:

- `notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json`
  — `"n": "2199023255552"`, `"t": "8589934592"` (= `2^41`, `2^33`);
  consumed at `background/nodes/dli_official_support_forcing/proof.md:16-19`:
  *"The banked official row (`official_scale.json`) fixes `n = 2^41`,
  `t = 2^33`, ... These are not assumed but DERIVED"*.
- `notes/kernel_basis/TARGET_3C_EXTRACTION.md:42-43`:
  *"I6 L7's (M_0, R) rate labels inconsistent with xr's t* table;
  (2^33, 256) is correct at rate 1/2."*

---

## 3. (P3) Adjudication: `7e10` vs `t* = 8,592,912,739`

### 3.1 Provenance of the two literals

`notes/pilots_20260802/f2_deployed_windows/selection.py:43`:

> `T_CONDITIONS = 70_000_000_000             # t ~ 7e10 (F2_NEWTON_EMPTY_EXTREMES)`

`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:372-377`:

> `t` has **no definition anywhere in the repo**. It is a bare literal
> `t = 7e10` at `f2_opening/verify.py:958` and `:1038`, traceable to the banked
> product `t·log2 q ~ 2.15e12`
> (`archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`
> via `notes/floor_campaign/SURVEY_X4_CLUSTER.md:15-17` and
> `notes/f2_campaign/F2_CAMPAIGN_LOG.md:184-187`) divided by `log2 p ~ 31`.

**Both literals descend from the SAME banked product.** They differ only in
the divisor. That makes this adjudicable: the question is not "which
constant" but "which divisor".

### 3.2 The verdict

The divisor must be `L = log2 q` (each condition is one field equation).
Dividing instead by `log2 p ~ 31` yields `n/log2 p = 7.096e10 ≈ 7e10`
(S6.8) — this reproduces the literal exactly and identifies its origin.

But `t = 7e10` back-implies `L = n/t = 31.415` (S6.4), and (R1) forces
`L > 41`. **A field with `log2 q ≈ 31` cannot contain a subgroup of order
`2^41`.** Hence:

```
  t = 7e10  is EXCLUDED by the rules, under BOTH field readings,
  at BOTH n = 2^40 and n = 2^41.                          (S6.6, S6.7, S15)

  t* = 8,592,912,739  lies INSIDE the rules-forced interval.        (S6.5)
```

**`t*` wins.** The `7e10` literal is an artefact of dividing the window-bits
product by the *characteristic* of a base field (`log2 p ~ 31`) that no
admissible row possesses — §1.3 forces `log2 p >= 39`. It is not a
competing modelling choice; it is a **unit error**, and the unit it uses
belongs to an inadmissible field.

**Residual honesty (pre-registered).** The derived value is an *interval*,
not a point: `t ∈ (2^33, 5.364e10]`, pinned to a point only once `L` is
pinned, and `L` is pinned only to `[255.911, 256)` at prize-max. `t*` is the
`L = 255.9` endpoint of that family, and `L = 255.9` is itself below the
sliver (CATCH-2). So the honest verdict is: **`t*` is right to three
significant figures and right in kind; `7e10` is wrong in kind.**

---

## 4. (P4) The `m_16` contradiction, resolved

The two readings, both computed exactly (S8):

```
    new-part  m_j = (n_j - n_{j-1})/2 = 2^{22+j}    =>  m_16 = 2^38
    nested    m_j =  n_j/2            = 2^{23+j}    =>  m_16 = 2^39
```

`f2_opening/PROOFS.md:233` uses `m_16 = 2^38`; `f2_opening/PREREG.json:58`
uses `2^39`:

> "official_row_check": "predicted to HOLD at the official row with a small margin: rung 16 has m = 2^39, so m/log2 p = 2^39/31 = 1.77e10, against dim L <= t ~ 7e10 -- a factor ~4, not orders of magnitude.",

`PREREG.json:57` reveals why — its own formula is `n/(2 log2 p)`, i.e. it
sets `m = n/2`, the **nested** count `n_16/2 = 2^39`. `PROOFS.md` uses the
tower's own ladder `m_j = 2^{22+j}` (`tower.py:18`), the **new-part** count.

**This is not an arithmetic error on either side.** It is exactly the 2x
ambiguity the lane already flagged at
`f2_deployed_windows/REPORT.md:69`:

> - Per-rung window/frequency set reconstructed from entry #76 (nowhere explicitly defined); a different reading changes m_j by 2x but CANNOT change the antipodal law.

**Verdict.** For the *deployed* window as the tower defines it —
`tower.py:17`, *"the moving coordinates are the elements of order EXACTLY
2^{24+j}"* — the correct count is **`m_16 = 2^38`** (the elements of order
exactly `2^{24+j}` number `φ(2^{24+j}) = 2^{23+j}`, giving `2^{22+j}`
antipodal pairs). `PREREG.json:58` is a stale pre-registration estimate that
was never reconciled with the ladder the pilot's own `PROOFS.md` adopted.

**BUT (CATCH-3):** `m_16 = 2^38` is the *less* conservative reading —
nested doubles `m`, making LEMMA 3 strictly harder. `rules_freeze/statement.md:9`
mandates: *"on any residual ambiguity the campaign plans against the
stricter reading."* Under that clause the **planning** value is `2^39`, and
every published margin should be halved for planning purposes. The pilot
adopted the looser one without invoking the clause.

---

## 5. (P5) LEMMA 3 and the surjectivity band, recomputed at every rung

LEMMA 3 (`f2_opening/PROOFS.md:225`, verbatim): `dim_{F_p} L  >=  m / log2 p
-  o(n)/log2 p`, official-row reading (`:232-233`) `t >= m_j / log2 p`.
THEOREM A/B additionally require `Lambda ⊇ {1,3,...,2m-1}` (`:327`), i.e.
`t >= 2 m_j - 1`.

Recomputed at `log2 p = 30.988685`, all 16 rungs, both window readings
(S9, S10). Reproduction checks first: the banked **7.89x** at rung 16 under
`7e10`/new-part comes out **7.8915x** (S9.1); the banked **0.9687x** sign
flip under `t*` comes out **0.9687x** (S9.2); the banked bands 1-13 and 1-10
reproduce exactly (S10.1, S10.2).

### The bands

| window | `t` | LEMMA 3 holds | THEOREM A/B band |
|---|---|---|---|
| new-part | `7e10` (inadmissible) | 1-16 | **1-13** |
| new-part | `t* = 8.59e9` | 1-15 | **1-10** |
| new-part | `2^33` (rules floor) | 1-15 | **1-10** |
| nested | `7e10` (inadmissible) | 1-16 | 1-12 |
| nested | `t* = 8.59e9` | **1-14** | **1-9** |
| nested | `2^33` (rules floor) | **1-14** | **1-9** |

**Worst case over the rules-forced `t`-interval** (the pre-registered
protocol Q6 — report the worst, never the best), at `t = 2^33`:

```
    new-part : LEMMA 3 rungs 1-15 ,  THEOREM A/B rungs 1-10
    nested   : LEMMA 3 rungs 1-14 ,  THEOREM A/B rungs 1-9
```

**Stated plainly.** Under every admissible `t`, LEMMA 3 — *a proved
necessary condition for (O1)* — is **VIOLATED at rung 16** (and at rung 15
too under the stricter nested reading). The surjectivity/discharge band is
**rungs 1-10** under the reading the pilot adopted, and **rungs 1-9** under
the stricter reading the rules clause mandates. The published "discharged at
rungs 1-13" headline is reachable only at `t = 7e10`, which no admissible
field realises (S11.2).

Per the pre-registered falsifier ("if the band is SHORTER than rungs 1-10,
report it without softening"): **under the stricter reading it is 1-9.**

SL-1 is unaffected — the `(R+1)/m_j` table reproduces `0.01563` at rung 16
under `t*` (S12.1), so `f2_sl1_powersums`'s immunity claim survives intact.

---

## 6. (P6) The `|K1|` normalisation seam, PRICED

`f2_opening/PROOFS.md:341-343`:

> - `E_c[.]` is an **average** over the K1 subspace. The consumer sums
>   over frequencies; the normalisation `|K1|` is a seam question for
>   PP5.0, raised as CATCH-3 in `REPORT.md`.

`f2_opening/FABLE_AUDIT.md:29-31` asks to *"settle WITH the PP5.0 freeze"*.

### 6.1 PP5.0 cannot be frozen from rules-level sources

PP5.0 is an internal composition law, explicitly unfrozen —
`f2_fixed_sector/REPORT.md:31`: *"per-sector trichotomy composes by
product/convolution (= PP5.0, unfrozen)"*. Its only "freeze" is a working
budget, `notes/roadmap/sections/00-overview-and-gate-addendum.md:58`:
*"(4) PP5.0 working budget = 1/43."* — an internal ratification dated
2026-08-02, not a rules citation. The rules freeze (§0) contains **nothing**
about composition laws. **Verdict: PP5.0 CANNOT be frozen from rules-level
sources. P6 cannot be discharged; it can only be priced.**

### 6.2 The price (S14)

`K1 = {c : f_even = 0}` (`f2_deployed_windows/REPORT.md:41`), the
frequencies supported on odd `l <= t`, so `dim K1 = ceil(t/2)` over the
coefficient field. With `t = t*`, `L = 255.9`, `n/2 = 2^40`:

```
  extension reading:  log2|K1| = (t*/2)·L      = 1.099463e12 = 1.0000 · (n/2)
  base reading:       log2|K1| = (t*/2)·log2 p = 1.331415e11 = 0.1211 · (n/2)
```

The first identity is **structural, not numerical**: `dim K1 · L =
(t*/2)·L = (t*·L)/2 = n/2` by the balance (F). So:

**In the extension reading, average-vs-sum is EXACTLY a factor `2^{n/2}`.**
(O1)'s target `E_{c in K1}[exp S_c] <= 2^{n/2 + o(n)}`
(`f2_fixed_sector/REPORT.md:33`) becomes `2^{n + o(n)}` under the sum
reading — the entire budget, doubled in the exponent. In the base reading
the cost is `n/(2e)` bits, still `Θ(n)`.

**Under BOTH readings the seam is `Θ(n)`, never `o(n)`** (S14.3). It
therefore **cannot** be absorbed into (O1)'s `+ o(n)` slack. The open
choice, stated exactly: *does the PP5.0 composition consume the K1 sector
as an average over `K1` (dividing by `|K1| = q^{ceil(t/2)}`) or as a sum
over `K1` (multiplying by it)?* Nothing at rules level decides it, and the
answer moves (O1) by a full `2^{n/2}`.

---

## 7. Catches

- **CATCH-1 (maintainer-level).** The 16-rung KoalaBear tower is **not a
  prize-admissible row**: `q_16 = p^{2^16}` exceeds `|F| < 2^256` by 7933x
  in bits, and (R1)+(R2) cap the tower at **2 rungs**, `e <= 6`,
  `log2 p >= 39`. Every "official row" statement in the F2 lane at rungs
  >= 4 is scoped to an inadmissible field. This also answers
  `field_cap_check/statement.md:9`'s standing question verbatim — *"and
  whether non-generating rows (hence the tower case) are admissible"* —
  **they are not, at rungs >= 4.**
- **CATCH-2.** The `L = 255.9` "prize convention"
  (`xr_radius_arithmetic/proof.md:33`) lies **below** the sliver's left
  endpoint `n/t* = 255.911275`: at `L = 255.9`, `t*·L = 2.198926e12 < n =
  2.199023e12`, so the counting/emptiness balance FAILS at the very point
  where `t*` is computed (S7.7). The corridor edge and the sliver are
  mutually inconsistent by 0.011 bits.
- **CATCH-3.** `m_16 = 2^38` is the looser of two correct readings;
  `rules_freeze/statement.md:9`'s "plan against the stricter reading"
  clause mandates `2^39` for planning, halving every published margin.
- **CATCH-4.** `b2_modp_giant_extras/statement.md:9`'s *"within ~2% of the
  counting threshold"* is wrong by ~500x: the true gap is **0.0044%**
  (S6.1, S6.3). The `2.15e12` literal understates the true product
  `t*·L = 2.198926e12` by 2.23%. The balance is far tighter than banked —
  which strengthens, not weakens, its *"pure counting can NEVER close it"*.
  (`TARGET_3C_EXTRACTION.md:33-34`'s I3 flagged the prose as wrong "in BOTH
  directions"; this is the quantitative version.)
- **CATCH-5.** The `[255.9113, 256)` sliver is generated by the **pure
  counting balance `t*·L >= n`**, i.e. `L >= n/t*`, NOT by the FM+gate
  formula (T*) — which would give `255.9887` (S7.1-S7.6). The two differ by
  0.077 bits. This is the falsification of my own Q5 (§8).

---

## 8. Falsified own-registration (Q5)

I pre-registered (PREREG.md, Q5) that the sliver equals
`{L : t*(L) <= 2^33}` under (T*). **FALSIFIED.** That set has left endpoint
`255.988729`; the banked endpoint is `255.9113`. The true generator, found
after the falsification and verified to `1e-4` (S7.4-S7.6), is
`L >= n/t* = 255.911275`, the counting balance. Recorded as a normal
outcome, not smoothed over; the corrected formula is CATCH-5.

Q1, Q2, Q3, Q4, Q6, Q7 all CONFIRMED.

---

## 9. Honest residuals

1. **The `t`-naming collision is real and unresolved.** LEMMA 3's `t`
   is `|Lambda|` (a condition count); `xr_radius_arithmetic`'s `t` is
   `A - k`, an agreement excess (`proof.md:24-25`). The repo adjudicates
   them as the same quantity (that is what CATCH-4 in
   `f2_sl1_powersums/PROOFS.md:368-391` does), and three lanes agree on
   `2^33`, but **no proof in the repo identifies them.** My §3 verdict
   inherits this. If they are distinct, the exclusion of `7e10` survives
   (it rests only on (R1)+(F)), but the positive identification of `t` with
   `t*` does not.
2. **(F) is a leading-order balance**, exact to `0.0044%` at prize-max but
   not a theorem; `t` is pinned to an interval, not a point.
3. `xr_radius_arithmetic` computes `t*` **given** the open ledger slot
   `xr_ledger_qpower` (`proof.md:31-32`: *"an OPEN packaging slot — used
   here as a hypothesis"*). `t*` is therefore conditional.
4. `background/nodes/rate_half_cyclic_simple_pole_mca_floor/node.json:9`
   already books a refutation of `8,592,912,739` as a *fixed safe point*
   (at excess `8,594,128,895`). That is about the safe point, not about
   `t*` as a corridor edge, but the two should be reconciled by a
   maintainer.
5. I did **not** re-derive the F2 tower on an admissible row. §1.3 shows the
   tower has <= 2 rungs there; what the F2 lane's obligations become on a
   2-rung tower is **open and not attempted**.
6. **Process defect, self-reported.** I ran one bare `python3` (a
   COMPUTE LAW violation) while extracting a JSON field; it was a read-only
   string extraction, it produced no result used anywhere, and it was
   immediately re-run under `ramguard tiny`. Disclosed rather than
   suppressed.
