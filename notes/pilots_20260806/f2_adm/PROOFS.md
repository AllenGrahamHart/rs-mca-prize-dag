# F2-ADM — the F2 mechanism on a prize-admissible row: the proofs

Round 17, 2026-08-06. Pilot `notes/pilots_20260806/f2_adm/`.
Verifier `verify.py`, stages S0-S10, **373 PASS, 0 FAIL**, digest
`F2_ADM_ALL_PASS`.
Run: `tools/ramguard local -- python3 notes/pilots_20260806/f2_adm/verify.py`.
Log: `VERIFY_LOG.txt`.

Notation. `n = 2^41` (the maximal rate-1/2 row), `q = p^e = |F|`,
`L := log2 q`, `e_p := v_2(p-1)`, `k := ord_n(p) = [F_p(mu_n) : F_p]`,
`D := log2 k` = the number of MOVING rungs, `t = |Lambda|` the Newton
condition count, `R := |Lambda| = ceil(t/2)` under the banked
`Lambda = {odd l <= t}` reading, `m = |W|/2`, `T = {-1,0,1}^m`.
Every load-bearing statement is quoted VERBATIM with `file:line` and
machine-checked at that line by **S0**.

---

## 0. The surfaces this pilot stands on (verbatim)

`critical/nodes/rules_freeze/statement.md:9`:

> THE RULES-FACT (closed by citation, not proof): the operative prize rules are exactly — smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16} (no dither latitude); the m-quantifier per rules_m_reading (family-per-constant-m). Certificate = quote + hash of proximityprize.org and ePrint 2026/680 with a drift detector; on any residual ambiguity the campaign plans against the stricter reading.

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:114` (the admissible region):

> ```
>     v_2(e) <= 2,      e <= 6,      log2 p >= 39,
> ```

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:131` (the banked witness):

> ```
>     p = 18446735827372343297   (prime, v_2(p-1) = 39 exactly, log2 p = 64.0000)
> ```

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:174` (the counting balance):

> ```
>                         t · L  >=  n .                                (C)
> ```

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:202` (the pinned interval):

> ```
>         2^41/256  <  t  <=  2^41/41 ,        i.e.   8.590e9 < t <= 5.364e10 .
> ```

`notes/pilots_20260802/f2_deployed_windows/tower.py:15-18` (the tower being
replaced):

> ```
>     RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,
>     the descent step is the quadratic extension F_{q_j} / F_{q_{j-1}},
>     the moving coordinates are the elements of order EXACTLY 2^{24+j},
>     m_j = (n_j - n_{j-1}) / 2 = 2^{22+j} conjugate pairs.
> ```

`notes/pilots_20260802/f2_deployed_windows/tower.py:26,28` (the antipodal law):

> ```
>   (i)   v_2(q_j - 1) = e + j            for every j >= 0   [LTE],
>   (iii) every y of order exactly n_j satisfies  y^{q_{j-1}} = -y.
> ```

`notes/pilots_20260802/f2_fixed_sector/REPORT.md:33` (the obligation):

> **Replacement obligation (constructive)**: K1 must be paid by MASS, not cancellation: (O1) first-moment target E_{c in K1}[exp S_c] <= 2^{n/2 + o(n)} (2^{n/2} = the exact independent-value scale); (O2) the same at fixed b (the Hamming-slice fence forbids (O1) alone); (O3) PP5.0 must carry the pullback ramification 2^d.

`notes/pilots_20260804/f2_opening/PROOFS.md:81` (the dual description),
`:94` (the floor), `:106` (LEMMA 2's hypothesis), `:225` (LEMMA 3),
`:330` (the upper bound), `:341` (the seam);
`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:99` (SL-1),
`:316` (SL-1b); `notes/pilots_20260806/f2_sl1b/PROOFS.md:161` (the
bracket), `:259` (the `k = 1` sharpness), `:571` (SL-1b'). All checked at
their line by S0.

---

## 1. (D1) THE ADMISSIBLE F2 OBJECT

### 1.1 What the rules leave standing (S1, S2)

At `n = 2^41`, `n | q - 1` and `q = p^e` force
`k = ord_n(p) = 2^{(41 - e_p)_+}` and `k | e`; with `e <= 6` this gives
`D <= 2`. The banked witness realises `D = 2`:

```
    p = 18446735827372343297,  e_p = v_2(p-1) = 39,  e = 4,  k = ord_n(p) = 4,
    log2 p = 63.999999355,   L = log2 q = 255.999997420 < 256,   v_2(q-1) = 41,
    D = 2 moving rungs,   t = n/L = 8,589,934,678.6,   R = ceil(t/2) = 4,294,967,340.
```

**The admissible ladder (A2, S1.9) — this is what replaces the 16 rungs:**

| layer | order | `n_j` | `q_j` | `k_j` | `m_j` new-part | `m_j` nested | share of the domain |
|---|---|---|---|---|---|---|---|
| fixed sector | `<= 2^39` | `2^39` | `p` | 1 | `2^38` | `2^38` | **25%** |
| rung 1 | `= 2^40` | `2^40` | `p^2` | 2 | `2^38` | `2^39` | 25% |
| rung 2 | `= 2^41` | `2^41` | `p^4` | 4 | `2^39` | `2^40` | **50%** |

Two things change qualitatively against the tower. (a) The fixed sector is
**25% of the domain** instead of `2^-16` of it (S1.10, S1.11) — a quarter of
`mu_n` now sits in the prime field, where Frobenius is trivial. (b) The
ladder is **three factors**, not seventeen: `T(c) = F(c) · M_1(c) · M_2(c)`.

### 1.2 THE DEPTH-BUDGET TRADE-OFF (A3, S2.4-S2.8)

`D` moving rungs forces `k = 2^D | e` and `log2 p > e_p = 41 - D`, hence
`L > 2^D (41 - D)` and, by the balance (C), `t = n/L < 2^41/(2^D(41-D))`:

| `D` | forced `L >=` | `t <=` | realised classes `(e_p, e)` |
|---|---|---|---|
| 0 | 41 | 5.364e10 | (41,1) (41,2) (41,3) (41,4) (41,5) (41,6) |
| 1 | 80 | 2.749e10 | (40,2) (40,4) |
| 2 | 156 | 1.410e10 | (39,4) |
| 3 | 304 | — | **INADMISSIBLE** (`L > 256`) |

**Depth and condition budget are in strict competition: every extra rung at
least halves the largest admissible `t`.** The top of the pinned interval
`t ~ 5.36e10` is reachable ONLY at `D = 0`, i.e. only when there is no
moving rung at all — `mu_n <= F_p^*`. The 16-rung tower would need
`L >= 2^16 · 25`, i.e. `t <= 1.3e6`: the tower and a large `t` are
mutually exclusive even before the field cap is applied (§6, CATCH-3).

**Existence, per class (S2.9-S2.12).** Searching `p = c·2^{e_p} + 1`,
`c` odd, `e log2 p < 256`: every class is realised by an explicit prime
EXCEPT `(e_p = 40, e = 6)` — there `c < 6.35` and none of
`c in {1,3,5}` gives a prime, so **that class is empty**. Named witnesses
used below:

```
   (41, e) for e = 1..6 :  p = 3·2^41 + 1 = 6597069766657     (k = 1)
   (40, e) for e = 2, 4 :  p = 27·2^40 + 1 = 29686813949953   (k = 2)
   (39, 4)              :  p = 5·2^39 + 1 = 2748779069441     (k = 4)
```

### 1.3 LEMMA ADM-1 (the `F_p`-proportionality classes)

> Let `y in F_q` have order `n = 2^41`, `e_p = v_2(p-1) >= 2`,
> `D = (41 - e_p)_+`. Then `mu_n ∩ F_p^* = mu_{2^{min(41, e_p)}}`, and for
> integers `a, b`:
>
> ```
>       y^a  and  y^b  are  F_p-proportional   <=>   a ≡ b  (mod 2^D).
> ```

*Proof.* `mu_n ∩ F_p^*` is the subgroup of `mu_n` of order
`gcd(n, p-1) = 2^{min(41,e_p)}`. Now `y^a/y^b = y^{a-b}` has order
`2^{41}/gcd(2^{41}, a-b)`, which is `<= 2^{e_p}` iff `2^{41-e_p} | a-b`. QED

So the antipodal-pair representatives of any window fall into
`F_p`-proportionality classes indexed by residues mod `2^D`, each class of
the form `y^{i_0} · {ζ^s}` with `ζ := y^{2^D}` of order `2^{min(41,e_p)}`
**in the prime field**. *This is the structural fact the tower hid: on the
KoalaBear row `D = 16` and the classes are tiny; on an admissible row
`D <= 2` and each class is half of the whole fixed sector.*

### 1.4 LEMMA ADM-2 (the decomposition — what replaces the descent)

*Verified: S3.A (every toy row, both readings, all `R`), S3.N (the direct
sum verified at the level of SETS, not just dimensions — class kernels of
dimension up to 6 embedded and re-checked against the full kernel), S3.B
(the sl1b bracket holds as a control), S3.D (`Z` factorises), S3.K (MDS
parameters).*

> Let `W` be the layer `{x : ord(x) = 2^a}` (new-part) or `mu_{2^a}`
> (nested), `m = |W|/2`, one representative per antipodal pair; let
> `Lambda` contain a run of `R` consecutive odd exponents; put
> `D_a = (a - e_p)_+`,
>
> ```
>     C = 1 if D_a <= 1 else 2^{D_a - 1}   (new-part),     C = 2^{D_a}  (nested),
>     S = m / C .
> ```
>
> If the `C` class representatives `{y^{i_0(c) l}}_c` are `F_p`-independent
> for every `l in Lambda` — automatic when `D <= 2`, i.e. on every
> admissible row (proof below) — then
>
> ```
>   (i)   L^perp  =  (+)_{c=1}^{C} ker(A_c),   A_c = ((ζ^s)^l)_{l in Lambda, s<S},
>   (ii)  each ker(A_c) is the dual of a GRS code over F_p:  [S, S-R, R+1]_p, MDS,
>   (iii) dim_{F_p} L  =  C · min(S, R)      EXACTLY,
>   (iv)  Z(L)  =  prod_c Z_c  =  Z_1^C .
> ```

*Proof.* Write the representatives as `y_i = y^{a_i}`. By LEMMA ADM-1 they
split into `C` classes; inside the class with representative `y^{i_0}`ce
each element is `y^{i_0} ζ^s`, `s = 0..S-1`, and

```
    sum_i eps_i y_i^l  =  sum_c y^{i_0(c) l} · u_c(l),
    u_c(l) := sum_s eps_{c,s} (ζ^s)^l  in  F_p        (ζ in F_p^*).
```

By hypothesis the `y^{i_0(c)l}` are `F_p`-independent, so the whole system
vanishes iff every `u_c(l) = 0` — this is (i), and it is the exact point
where the tower's *ladder* is replaced by a *direct sum*. Each class system
is a **prime-field** system: `A_c[l, s] = (ζ^s)^l`, and with the run
`l = 2a_0+1, ..., 2a_0+2R-1`,

```
    A_c = diag(ζ^{s(2a_0+1)}) · Vandermonde(ζ^{2s}),
```

whose points `ζ^{2s}` are distinct (`ζ^2` has order `S`) — so `A_c` is a
GRS parity-check matrix and `ker(A_c)` is `[S, S-R, R+1]_p` MDS, giving
(ii), and `rank_{F_p} A_c = min(S,R)` exactly (`<= |Lambda| = R` because
the matrix has `R` rows over `F_p`; `>= min(S,R)` by the invertible minor).
This is verbatim the banked `k = 1` sharpness,
`f2_sl1b/PROOFS.md:259`: *"`k = 1   =>   dim_{F_p} L  =  min(m, R)   EXACTLY.`"*
Summing over classes gives (iii), and (iv) is immediate from (i) because
`wt` is additive across the summands. QED

**The independence hypothesis on admissible rows.** New-part: `C <= 2`,
and for `C = 2` (i.e. `D = 2`) the two representatives are `y^l, y^{3l}`
with ratio `y^{2l}` of order `2^40 > 2^{e_p} = 2^39`, hence not in `F_p`.
Nested: `C = 2^D <= 4`, representatives `1, y^l, y^{2l}, y^{3l}`; for `l`
odd `y^l` has order `2^41`, so `[F_p(y^l):F_p] = ord_n(p) = k = 4` and
those four elements are an `F_p`-basis of `F_{p^4}`. For `D = 1` the same
argument with two elements; `D = 0` is vacuous. **`D <= 2` is exactly the
admissible regime, so the hypothesis is free where it is needed** — and
this is the one place where admissibility *helps*.

**COROLLARY ADM-2.1 (the bracket collapses).** `f2_sl1b/PROOFS.md:161`'s
`min(m, R) <= dim_{F_p} L <= min(m, k·|Lambda|)` becomes an **equality**
`dim_{F_p} L = C·min(S, R)` on every admissible row. The banked
`OPEN`/`REFUTED` cells that turned on where `dim L` sat inside that
interval are now decided.

**COROLLARY ADM-2.2 (the terminal is a prime-field GRS code).** `Z(L)` is
determined by ONE class: `Z(L) = Z_1^C`, `C <= 4`, where `Z_1` is the
ternary mass of an explicit `[2^{e_p-1}, 2^{e_p-1} - R, R+1]_p` GRS code
whose evaluation points are the half-system of `mu_{2^{e_p}} <= F_p^*`.

### 1.5 LEMMA ADM-3 (the trace-tower collapse: the constant is `ord_n(p)`)

*Verified: S3.F, S3.L, S3.M (a disjoint image-rank route, coefficients
ranging over the LARGER field).*

> `L^perp = ker_{F_p}(A)` with `A = (y_i^l)` entried in `F_p(mu_n) = F_{p^k}`;
> hence `dim_{F_p} L <= min(m, k·|Lambda|)` with **`k = ord_n(p)`**, even
> when the frequency coefficients `C_l` range over the full `F_q = F_{p^e}`
> with `e > k`.

*Proof.* `eps in L^perp` iff `Tr_{F_q/F_p}(sum_l C_l u_l) = 0` for all
`C in F_q^Lambda`, `u_l := sum_i eps_i y_i^l`; the trace form is
non-degenerate, so this holds iff every `u_l = 0` — an equation in
`F_{p^k}`. Expanding each entry of `A` in an `F_p`-basis of `F_{p^k}` gives
a `k|Lambda| x m` matrix over `F_p`, so `dim ker >= m - k|Lambda|`. QED
Equivalently, by the trace tower
`Tr_{F_q/F_p} = Tr_{F_{p^k}/F_p} ∘ Tr_{F_q/F_{p^k}}`, the character only
sees `Tr_{F_q/F_{p^k}}(C_l)`: **the K1 sector collapses from `e|Lambda|` to
`k|Lambda|` `F_p`-dimensions.**

This is invisible on the tower (there `k_j` IS the ambient degree by
construction) and load-bearing on admissible rows, where `e > k` is common.
`f2_sl1b/PROOFS.md:161`'s `k = [F_q:F_p]` must be **restated** as
`ord_n(p)` (§2, and CATCH-2).

### 1.6 What the tower supplied, and what now supplies it (the A1 falsifier)

| tower service | needs depth? | admissible replacement |
|---|---|---|
| partition of `mu_n` into antipodally closed windows | no | the **order filtration**, still 41 layers deep — unchanged |
| per-rung Galois step `F_{q_j}/F_{q_{j-1}}` (antipodal law) | no — one quadratic step each | holds at both moving rungs with `e = 39` (S3.H) |
| ambient field per rung | no | a SINGLE field `F_{p^k}` for the whole ladder |
| relating windows to each other (the "descent") | the only candidate | **replaced by LEMMA ADM-2's direct-sum decomposition** — one step, not sixteen |
| pullback ramification `2^d` (O3) | no | the order filtration again: depth still up to 41 |

**Verdict on the pre-registered falsifier: it does NOT fire.** No
load-bearing F2 statement consumes tower depth; every one of LEMMAS 1-5 and
THEOREMS A-C is a per-window statement, as
`f2_opening/PROOFS.md:335` itself says — *"which cannot affect Lemmas 1-5,
which are window-agnostic"*. The mechanism reconstructs, and the
reconstruction is *sharper* than the tower's (LEMMA ADM-2 gives an exact
dimension where the tower gave a bracket). **The F2 lane is NOT vacuous.**
What collapses is not the mechanism but the **discharge band** (§3).

### 1.7 The coset (A10, S3.H, S3.I, S3.J)

The rules-level domain is a **coset** `g·mu_n`, not `mu_n`
(`rules_freeze/statement.md:9`, quoted in §0). Then:

- every K1 statement survives: `-(g u) = g(-u)` keeps the window
  antipodally closed, and `sum_i eps_i (g y_i)^l = g^l sum_i eps_i y_i^l`
  with `g^l != 0`, so `L^perp`, `dim L`, `Z(L)` and the minimum ternary
  weight are **unchanged** (S3.J, exact on the toy row);
- the antipodal-descent identity is **not** coset-invariant:
  `(gy)^{q_{j-1}} = -(gy)` iff `g^{q_{j-1}-1} = 1` iff `g in F_{q_{j-1}}`.
  S3.I exhibits a coset representative outside the subfield at which the
  identity fails.

---

## 2. (D2) THEOREM SURVIVAL TABLE

No theorem is carried over silently. "VERBATIM" means the statement and
its proof go through with no change of hypothesis or constant (a change of
the ambient-field *symbol* where the proof never used its degree is noted
inline); "RESTATED" gives the new constants; "NEEDS RE-DERIVATION" names
the gap.

| # | statement (source, verbatim-checked) | verdict on admissible rows |
|---|---|---|
| 1 | LEMMA 1, the ternary-dual identity `E_c[T_W] = 2^m Z(L)` (`f2_opening/PROOFS.md:47-74`) | **VERBATIM** (field-generic). Proof uses only: `W` antipodally closed, `Lambda` odd, `Tr` non-degenerate, `C_l` free. `f2_sl1b/PROOFS.md:171` verbatim: *"It is stated for `k = 2`; nothing in it uses `k = 2`."* Re-verified by brute force at three toy rows (S3.E). |
| 2 | Corollary 1.1, the unconditional floor `E_c[T_W] >= 2^m` (`:94`) | **VERBATIM**. (O1) stays equality-shaped with zero slack. |
| 3 | LEMMA 2 / THEOREM A, surjectivity ⟹ (O1) exactly (`:104-143`) | **VERBATIM as a conditional**, but its hypothesis `Lambda ⊇ {1,...,2m-1}` (`:106`) is **UNSATISFIABLE at every moving rung of every admissible row** (§3.1). RESTATED range: it discharges the order layers `a <= 42 - log2 L` only (layers 1-34 at prize-max), all inside the fixed sector. |
| 4 | THEOREM B, (O2) implied by (O1) (`:166-191`) | **VERBATIM** (a counting argument over `L^perp`; no field, no tower). The obligation list still shortens from three to two. |
| 5 | THEOREM B', `E_c[V_b] = C(m, b/2)` (`:198-209`) | **VERBATIM as a conditional**; same unsatisfiable hypothesis as #3, so it is now **vacuous at the moving rungs**. |
| 6 | LEMMA 3, `dim L >= m/log2 p - o(n)/log2 p` (`:225`) | statement **VERBATIM**; its *official-row reading* (`:232-233`) **RESTATED**: the margin is `max(2,k)/e` (new-part) / `k/e` (nested), no longer `7.89x` (§3.2). |
| 7 | LEMMA 4, (O3) pullback ramification `P_{mu_n}(f;z) = (P_{mu_{n/2^d}}(g;z))^{2^d}` (`:241-255`) | **VERBATIM**. Needs only `x -> x^{2^d}` on `mu_n` and `gcd(2^d,p)=1`. **Its depth is the ORDER filtration (up to `d = 41`), which the tower collapse does not shorten** — (O3) is unchanged in difficulty. |
| 8 | THEOREM C, T3-uniform is FALSE (`:267-296`) | **VERBATIM as a refutation**; RESTATED range: the construction needs `t >= n_j`, i.e. order layers `a <= log2 t = 33` at prize-max (rather than "official rungs 1-12"). One layer suffices to refute a uniform claim, so the verdict stands. |
| 9 | LEMMA 5, the parity certificate is the wrong functional for (O1) (`:300-321`) | **VERBATIM** (per-window; contrasts the `Delta` multiset with additive relations). |
| 10 | THEOREM SL-1, `wt(eps) >= R+1`, characteristic-free (`f2_sl1_powersums/PROOFS.md:85-99`) | **VERBATIM** (char-free and `k`-free). RESTATED constant: `(R+1)/m = 2/L`, i.e. `1/128` at prize-max (§4). Re-verified on every toy row (S3.C). |
| 11 | Corollary 1.3, THEOREM A = the `R >= m` case (`:141-144`) | **VERBATIM**. |
| 12 | (M1), (M2) mass bounds `Z <= 2^{m-R}`, `Z <= 1 + 3^{m-R}2^{-(R+1)}` (`:216-241`) | **VERBATIM** (they use only the distance and injectivity). |
| 13 | (M3), the discharge criterion `R > 0.61315 m` (`:243-254`) | **VERBATIM but VACUOUS on every admissible row**: `R/m = 2/L <= 2/41 = 0.0488 < 0.61315`, short by `>= 12.6x` (S10.5). |
| 14 | LEMMA SL-1b-DIM, `min(m,R) <= dim L <= min(m, k|Lambda|)` (`f2_sl1b/PROOFS.md:161`) | lower bound **VERBATIM** (`k`-free); upper bound **RESTATED**: `k` must be `ord_n(p)`, not `[F_q:F_p]` (LEMMA ADM-3). Both are **SUPERSEDED** on admissible rows by the exact `dim L = C·min(S,R)` (LEMMA ADM-2). |
| 15 | the `k = 1` sharpness `dim L = min(m,R)` exactly (`:259`) | **VERBATIM — and promoted**: it is the engine of LEMMA ADM-2 (every class is a `k=1` problem). |
| 16 | (R-A) ⇏ (R-B), the 61-witness refutation (`f2_sl1b/PROOFS.md:281-332`) | **VERBATIM**. Still governs: a dimension statement cannot deliver the ternary count. |
| 17 | the random-subspace first moment `E[Z] = 1 + (2^m-1)(p^{m-d}-1)/(p^m-1)` (`f2_sl1_powersums/PROOFS.md:288-292`) | **VERBATIM** (a statement about random subspaces; unaffected by the row). |
| 18 | the antipodal law (i)/(ii)/(iii) (`tower.py:26-33`) | **RESTATED CONSTANTS** (`e = 24 -> 39`, `j in {1,2}`), verified at both admissible rungs (S3.H). **NEEDS RE-DERIVATION for the rules-level domain**: it FAILS on a coset `g·mu_n` with `g` outside `F_{q_{j-1}}` (S3.I). |
| 19 | "every deployed window is parity-homogeneous, `flat = 0`" (`f2_deployed_windows/tower.py:44-50`) | **VERBATIM for K1 frequencies on any antipodally closed window** (it needs `chi_c(-y) = -chi_c(y)`, not Frobenius) — so it now also covers the fixed sector, which is 25% of the domain. |
| 20 | `f2_fixed_sector` Theorem B, "no absorption", because `-1 in mu_{2^24}` | **RESTATED CONSTANTS** (`-1 in mu_{2^39}`); conclusion unchanged. |
| 21 | the K1 budget arithmetic "16 x log2 p = 495.8 bits vs 1.278e10" (`f2_fixed_sector/REPORT.md:25`) | **RESTATED, and it gets worse**: `2 x 64 = 128` bits against `1.918e10` — a `1.50e8x` shortfall vs the banked `2.58e7x` (§4, S10). |
| 22 | CATCH-B / DEFECT-3, "`f2_opening`'s `n | p^2-1` is a rung-1-only reading" (`f2_sl1b/REPORT.md:67`) | **REPAIRED on admissible rows**: one field `F_{p^k}` hosts the entire ladder, so the fixed-ambient setting is consistent at every rung once `p^2` is read as `p^k`. |
| 23 | the tower itself (`tower.py:15`), and every "official row" statement at rungs `>= 4` | **NOT ADMISSIBLE** (sibling CATCH-1). Superseded by §1.1. |

---

## 3. (D3) THE MARGINS ON THE ADMISSIBLE ROW

Throughout: worst case over the pinned interval `t in (2^33, 5.364e10]`
**and** at the row-consistent `t = n/L`; both window readings; the stricter
(nested) reading governs headline numbers per
`rules_freeze/statement.md:9` and the sibling's CATCH-3.

### 3.1 THEOREM A / LEMMA 2: the discharge band is EMPTY at the moving rungs

*Verified: S4.1-S4.7.*

Layer `a` is discharged iff `2m(a) - 1 <= t`, i.e. `a <= 42 - log2 L`.

| layer `a` | `m(a)` | needs `t >=` | at the witness (`t = 8.5899e9`) |
|---|---|---|---|
| 34 | `2^32` | 8.590e9 | **discharged** (the last one) |
| 35 | `2^33` | 1.718e10 | no — 2.0x short |
| 39 (top fixed) | `2^37` | 2.749e11 | no — 32x short |
| 40 (**rung 1**) | `2^38` | 5.498e11 | no — **64x short** |
| 41 (**rung 2**) | `2^39` | 1.100e12 | no — **128x short** |

**THEOREM ADM-A (no admissible discharge).** On EVERY admissible row, no
moving rung satisfies LEMMA 2's hypothesis; the minimum shortfall over the
whole admissible region is `39x` (attained at `(e_p, e) = (39, 4)`, layer
40; exactly `39·(1-2^-39)`, S4.5). The discharged set is contained in the
fixed sector and covers exactly the layers of order `<= 2t`, a fraction

```
        2t/n  =  2/L   <=   2/41  =  4.88%   of the domain,
```

**`1/128 = 0.78%` at prize-max** (S4.2, S4.3, S4.7). Compare the tower's
banked claim: rungs 1-13 covered `2^37/2^40 = 12.5%` — the covered fraction
falls by `16x`, and, more importantly, **from "all but three rungs" to
"none of the moving rungs".**

### 3.2 LEMMA 3: exactly saturated, or violated

*Verified: S5.1-S5.9.*

By LEMMA ADM-2 `dim L` is exact, so the necessary condition
`dim L · log2 p >= m - o(n)` can be evaluated, not merely bracketed. With
`t = n/L` (the balance (C)) every scale cancels:

```
      ratio(top window)  =  dim L · log2 p / m  =  max(2, k)/e   (new-part)
                                                =  k/e           (nested).
```

It is **independent of `p`, `n` and `t`**, and over the pinned `t`-interval
the worst case is exactly the row-consistent value (S5.2): at
`t = 2^33+` the ratio is `1.000000`, rising to `6.24` only at
`t = 5.36e10`, which no `D >= 1` row can realise (§1.2).

| `(k, e)` | new-part | nested (governs) | verdict |
|---|---|---|---|
| (1, 1) `q = p` | **2.000** | 1.000 | the only row with any margin |
| (1, 2) | 1.000 | 0.500 | saturated / **(O1) REFUTED** (nested) |
| (1, 3) | 0.667 | 0.333 | **(O1) REFUTED** |
| (1, 4) | 0.500 | 0.250 | **(O1) REFUTED** |
| (1, 5) | 0.400 | 0.200 | **(O1) REFUTED** |
| (1, 6) | 0.333 | 0.167 | **(O1) REFUTED** |
| (2, 2) | 1.000 | 1.000 | **SATURATED, zero margin** |
| (2, 4) | 0.500 | 0.500 | **(O1) REFUTED** |
| (4, 4) **the witness** | **1.000** | **1.000** | **SATURATED, zero margin** |

**THEOREM ADM-B (the admissible dichotomy).** On every admissible maximal
rate-1/2 row:

- if `k = e` (the smooth domain **generates** `F` over `F_p`), LEMMA 3 holds
  with **exactly zero margin** — `dim L · log2 p = m` on the nose, so the
  proved necessary condition degenerates to Corollary 1.1's unconditional
  floor and carries no information;
- if `k < e`, LEMMA 3 **fails by a constant factor**, hence (O1) is FALSE at
  that window:

```
      E_{c in K1}[T_W]  >=  4^m / p^{dim L}  =  2^{m(2 - k/e)}   vs the target
      2^{m + o(n)}  —  an excess of  2^{m(1 - k/e)} = 2^{Theta(n)}.
```

At the explicit admissible row `p = 3·2^41+1`, `q = p^6` (`k = 1`, `e = 6`,
`L = 255.51 < 256`), the excess is `2^{5n/12}` under the nested reading and
`2^{n/6}` under the LOOSER new-part reading — so this is **not** a
stricter-reading artefact. **(O1), as posed, is false on explicitly
exhibited admissible rows.**

Under the stricter reading mandated by the rules clause, the ratio is
`k/e <= 1` on **every** admissible row, with equality iff `k = e`:
**no admissible row leaves (O1) any positive margin at the full-group
window.**

**REGIME ROBUSTNESS (S5.9) — the refutation does not depend on the exact
`t`.** Writing `c := tL/n`, the ratio is `c · k/e` (nested). The F2
question is non-vacuous only while the `t`-null block window is non-empty,
i.e. only while `c <= 1` (that is exactly what the balance (C) says:
`t·L >= n` empties it). **Over the entire non-vacuous regime the ratio is
`<= k/e`**, so `k < e` refutes (O1) for EVERY relevant `t` — the conclusion
does not inherit the sibling's honest residual that `t = n/L` is a
leading-order balance rather than a theorem. At the `(k,e) = (1,6)` witness
the refutation survives even if `t` were `6x` larger than the balance
value.

### 3.3 The rest of the admissible ladder (witness row)

`ratio(layer a) = C_a · 2^{42-a}/e` (new-part), `C_a · 2^{41-a}/e` (nested):

| layer `a` | `C_a` | new-part ratio | nested ratio |
|---|---|---|---|
| 41 (rung 2) | 2 / 4 | **1.000** | **1.000** |
| 40 (rung 1) | 1 / 2 | **1.000** | **1.000** |
| 39 (top fixed) | 1 / 1 | 2.000 | 1.000 |
| 38 | 1 / 1 | 4.000 | 2.000 |

**Both moving rungs sit exactly on the threshold, under both readings.**

### 3.4 (O1)'s discharge status on admissible rows, stated plainly

> On admissible rows (O1) is **discharged at no moving rung at all**. It is
> discharged by THEOREM A only on order layers `<= 2t`, i.e. on `2/L <= 4.9%`
> of the domain, all inside the fixed sector. At the two moving rungs it
> reduces entirely to bounding `Z(L)` — SL-1b' — with LEMMA 3 exactly
> saturated (`k = e` rows) or violated (`k < e` rows, where (O1) is false).

---

## 4. (D4) THE RE-BASED OBLIGATION LIST

### 4.1 SL-1b' survives as THE terminal, and it is now explicit

*Verified: S6.5, and structurally by S3.K.*

`f2_sl1b/PROOFS.md:571`, verbatim: *"prove `Z(L) = sum_{eps in L^perp ∩ T}
2^{-wt(eps)} <= 2^{o(m)}`."* By COROLLARY ADM-2.2 this is now a question
about **one explicit prime-field code**:

```
  SL-1b'(adm):  bound the ternary mass Z_1 of the GRS code
                [S, S-R, R+1]_p  with  S = 2^{e_p - 1},  R = ceil(t/2),
                evaluation points = the half-system of mu_{2^{e_p}} <= F_p^*,
                column multipliers ζ^s;   then  Z(L) = Z_1^C,  C <= 4.
```

At the banked witness: `S = 2^38 = 2.749e11`, `R = 4.295e9`, `d = R+1`,
`p = 1.845e19` (`log2 p = 64`), `C = 2` (new-part) / `4` (nested). Three
changes of kind against the tower version: the field is the **prime field**
(no extension), the code is **MDS with known parameters** (not "the
deployed alternant code"), and the mass **factorises** so a single class
decides everything.

### 4.2 What is EASIER on the admissible object

1. **`dim L` is exact** (LEMMA ADM-2), not bracketed: every `OPEN` cell of
   `f2_sl1b/PROOFS.md:449-474` that depended on where `dim L` sat inside
   `[min(m,R), min(m,kR)]` is decided.
2. **One ambient field** for the whole ladder — `f2_opening`'s fixed-extension
   setting becomes consistent at every rung (survival-table row 22), and the
   sibling's INTERACTION-1 (three conclusions resting on the `k = 2` upper
   bound) is resolved by LEMMA ADM-3: the constant is `ord_n(p)`.
3. **The terminal is classical and prime-field** (§4.1), and `Z(L) = Z_1^C`
   with `C <= 4` — a single-class bound suffices.
4. **Three factors instead of seventeen** in the census factorisation.
5. `k`-freeness caveats disappear: `k` is pinned by the row.

### 4.3 What is HARDER

1. **The discharge band is empty at the moving rungs** (§3.1) — the banked
   headline "discharged at rungs 1-13" has no admissible analogue at all;
   the analogue is "discharged on 0.78% of the domain, none of it moving".
2. **LEMMA 3 loses all margin**: `7.89x` (banked) → `1.000` (saturated) or
   `< 1` (refuted). At saturation the necessary condition coincides with the
   unconditional floor, so it can no longer certify anything.
3. **A new hypothesis is forced**: `k = e`. Without it (O1) is false
   (THEOREM ADM-B); the rules do not supply it, so the F2 lane must either
   justify restricting to domain-generating rows or re-pose (O1).
4. **The K1 cancellation shortfall worsens** (S10): the per-rung ceiling is
   `log2 p` bits (`f2_deployed_windows/REPORT.md:39`'s `1/p` ceiling ladder),
   so the admissible row delivers `2 x 64 = 128` bits against a `1/43`
   budget of `1.918e10` bits — a `1.50e8x` shortfall, versus the tower's
   `16 x 31 = 495.8` bits against `1.278e10` (`2.58e7x`). **Fewer rungs deliver
   ~3.9x less cancellation; the shortfall gets ~5.8x worse.**
5. **SL-1's designed distance halves as a fraction**: `(R+1)/m = 2/L = 1/128`
   at the top window, against the banked `0.01563` at tower rung 16 (S6.2).
6. **(M3) is vacuous**: `R/m <= 0.0488` against its `0.61315` requirement
   (S10.5) — the `1.631x` improvement is still `12.6x` out of reach.
7. **SL-1b (R-A) flips to REFUTED** on every admissible row except `q = p`
   (S6.3, S6.4): with `dim L` exact, the ratio is `2C/(e log2 3)` (new-part)
   `= k/(e log2 3)` (nested), which is `1.2619` only at `(k,e) = (1,1)` and
   `0.6309` at the witness. This *strengthens* the sibling's conclusion that
   SL-1b is non-load-bearing: it is not merely insufficient, it is false
   there.
8. **The descent is gone as an inductive device.** Two rungs give an
   induction no room; the replacement (LEMMA ADM-2) is a one-step direct
   sum. Any future argument that wanted to descend 16 times must instead
   settle a single prime-field code.

### 4.4 The obligation list, re-based

| obligation | status on admissible rows |
|---|---|
| (O1) at layers `a <= 42 - log2 L` (`<= 4.9%` of the domain) | **DISCHARGED exactly** by THEOREM A, `o(n) = 0` |
| (O1) at every layer above, incl. both moving rungs | **OPEN**, and equal to SL-1b'(adm); LEMMA 3 saturated |
| (O1) on rows with `k < e` | **FALSE** (THEOREM ADM-B) — re-posing required |
| (O2) | implied by (O1) (THEOREM B, verbatim) — still not independent |
| (O3) | exact (LEMMA 4, verbatim); **unchanged in depth** (order filtration) |
| SL-1 (distance) | **PROVED**, `wt >= R+1`, fraction `2/L` |
| SL-1b (R-A) | **REFUTED** except at `q = p`; non-load-bearing either way |
| SL-1b' (ternary mass) | **THE terminal**, now an explicit prime-field GRS count |
| NEW: the domain-generating hypothesis `k = e` | **UNJUSTIFIED at rules level** |
| NEW: the coset form of the antipodal law | **OPEN** (fails for `g` outside the subfield) |

---

## 5. (D5) THE |K1| / PP5.0 SEAM ON THE ADMISSIBLE ROW

*Verified: S7.1-S7.7.* The seam, verbatim
(`f2_opening/PROOFS.md:341-343`):

> - `E_c[.]` is an **average** over the K1 subspace. The consumer sums
>   over frequencies; the normalisation `|K1|` is a seam question for
>   PP5.0, raised as CATCH-3 in `REPORT.md`.

**The identity survives, and it survives exactly.** With
`dim K1 = |Lambda| = ceil(t/2)` and the balance `t L = n`:

```
   extension reading :  log2|K1|      = |Lambda| · L        =  n/2   EXACTLY
   base reading      :  log2|K1|      = |Lambda| · log2 p   =  n/(2e)
   effective reading :  log2|K1|_eff  = k |Lambda| log2 p   =  (k/e)(n/2)
```

The **extension reading is exactly `n/2` on EVERY admissible row**,
independent of `p`, `e`, `t` — verified at four classes (S7.5). It is
structural, not numerical: it uses only `t L = n`. The sibling's
`(t*/2)L = n/2` was the `L = 255.9` instance of this.

The **effective reading is new** and is forced by LEMMA ADM-3: PP5.0 cannot
consume more than the `k|Lambda|` `F_p`-dimensions the character actually
sees. At the witness (`k = e = 4`) it coincides with the extension reading
(`n/2`); at `k < e` it is strictly smaller (`(k/e)(n/2)`).

At the witness: `n/2 = 1.0995e12` bits (extension and effective),
`n/8 = 2.7488e11` bits (base). **All three are `Theta(n)`, never `o(n)`
(S7.4), so the sibling's verdict survives verbatim: the seam cannot be
absorbed into (O1)'s `+o(n)` slack.** I price; I do not choose.

**THE SEAM IDENTITY (new, S7.6-S7.7).** LEMMA 3 at the full-group window
requires `dim L · log2 p >= m = n/2`, and `dim L <= k|Lambda|`, so

```
      (O1) at the full-group window   ==>   log2|K1|_eff  >=  n/2 ,
```

i.e. **the necessary condition for (O1) and the average-vs-sum seam are the
same inequality**, and on the surviving (`k = e`) rows they are equal:
`log2|K1|_eff = n/2` exactly. Consequence for the pending decision: if
PP5.0 consumes K1 as a **sum**, it spends the identical `n/2` bits that
(O1) has already spent in full — the whole target, counted twice. If it
consumes an **average**, (O1) is exactly the statement that those `n/2`
bits suffice, with zero slack. The choice is therefore not a normalisation
convention but the difference between "exactly enough" and "twice the
budget".

---

## 6. CATCHES

- **CATCH-1 (maintainer-level).** **(O1) is FALSE on explicitly exhibited
  prize-admissible rows.** Whenever the smooth domain does not generate the
  field (`k = ord_n(p) < e`), LEMMA 3 — a PROVED necessary condition —
  fails by the constant factor `k/e`, so
  `E_{c in K1}[T_W] >= 2^{m(2-k/e)} = 2^{m+Theta(n)}`. Explicit row:
  `p = 3·2^41 + 1 = 6597069766657`, `q = p^6`, `L = 255.51 < 256`,
  `k = 1`, `e = 6` — the excess is `2^{n/6}` under the LOOSER window
  reading. The F2 lane therefore needs a new hypothesis, `k = e`, that the
  rules do not supply (`official_row_primes_pinning/proof.md:25-33`:
  *"These are admissibility and quantifier conditions"* — the quantifier is
  universal over admissible `F`).
- **CATCH-2 (against a banked lemma's constant).**
  `f2_sl1b/PROOFS.md:161`'s upper bound uses `k = [F_q : F_p]`; the correct
  constant is `k = ord_n(p)` (LEMMA ADM-3). The two coincide on the tower
  (where the ambient is minimal by construction) and differ on admissible
  rows with `e > k`, where the banked reading **overstates** `dim L` by a
  factor `e/k` — up to `6x`. Every verdict that used the upper bound must
  be recomputed; on admissible rows LEMMA ADM-2 supersedes both bounds.
- **CATCH-3 (the tower is inconsistent with its own `t`, independently of
  admissibility).** Using the tower's OWN field, `L = log2 q_16 = 2,030,874`,
  the balance (C) gives `t = n/L = 5.414e5` (at the tower's own `n = 2^40`) — the banked `t ~ 7e10` is
  **1.29e5x too large by the tower's own arithmetic** (S8.3, S8.4). Under
  its own `t`, **no tower rung is discharged at all**: rung 1 already needs
  `t >= 2^24` and misses by `30.99x` (S8.5). This is independent of the
  sibling's CATCH-1 (which is about the field cap) and independent of which
  `t`-reading one prefers.
- **CATCH-4 (an empty admissibility class).** The class
  `(e_p, e) = (40, 6)` (i.e. `k = 2`, `e = 6`) is **vacuous** (flagged in
  S5's table so the refutation examples use realised rows): it needs
  `p = c·2^40+1` prime with `c < 6.35`, and none of `c in {1,3,5}` is
  prime (S2.9). Any statement quantified over "all `(k,e)` with `k | e`,
  `e <= 6`" should exclude it. (This *removes* one of the rows on which
  CATCH-1 would otherwise fire, and it is why CATCH-1 is stated with the
  `k = 1, e = 6` witness instead.)
- **CATCH-5 (self-caught, code-level, in THIS pilot).** My first field
  builder accepted **reducible** degree-6 polynomials: the test
  `x^{p^d} = x` plus `x^{p^{d/r}} != x` passes a product of an irreducible
  quadratic and an irreducible cubic (`lcm(2,3) = 6`), so `F_p[x]/(f)` was a
  ring, not a field, and the toy reported `dim L = 2R` instead of `R`. It
  was caught by S3.A/S3.F failing against LEMMA ADM-2's prediction, fixed
  with the proper gcd-based Rabin test, and is recorded here because the
  same shortcut appears whenever `d` has two coprime factors. **The
  falsifier caught my own bug, not the theory.**
- **CATCH-6 (scope, rules-level).** The rules-level domain is a **coset**
  `g·mu_n`; the banked antipodal-descent law is stated for the subgroup and
  **fails** on a coset whose representative lies outside `F_{q_{j-1}}`
  (S3.I). The K1 mass machinery is unaffected (S3.J). Every parity/descent
  statement in the F2 lane inherits this scope gap; no F2 file mentions the
  coset.

---

## 7. FALSIFIED / CORRECTED OWN-REGISTRATIONS

- **A8 CORRECTED (self-falsification).** I registered the SL-1b (R-A) ratio
  as `2/(e log2 3) = 1.2619/e`. That omits the class factor: the exact law
  is `2C/(e log2 3)` (new-part), `k/(e log2 3)` (nested). At the witness the
  correct value is `0.6309`, not `0.3155`, and the verdict is **REFUTED**
  (not OPEN, as sl1b's bracket left it) because `dim L` is now exact. The
  qualitative registration ("PROVED only at `e = 1`") survives; the constant
  did not.
- **A7 REFINED.** I registered the LEMMA 3 ratio as `max(2,k)/e` /
  `k/e` — confirmed exactly (S5.1, S5.3, S5.4) — but I had also expected
  the `t`-interval worst case to be a *different* number from the
  row-consistent value; it is not (S5.2): the ratio is `t`-free on the row
  and the interval's worst case coincides with it.
- **A3 CONFIRMED with a correction.** The trade-off table is exact, but the
  `(e_p, e) = (40, 6)` class it lists is EMPTY (CATCH-4).
- **A6 CONFIRMED and strengthened**: not merely "the constant should be
  `ord_n(p)`" — `dim L` does not grow with the ambient degree at all
  (S3.M), so there is no coefficient-field reading ambiguity to price.
- A1, A2, A4, A5, A9, A10, A11, A12: **CONFIRMED** (see the stages cited
  inline).

---

## 8. SCOPE — what is NOT claimed

- LEMMA ADM-2's independence hypothesis is proved for `D <= 2` — exactly the
  admissible regime. It is **not** claimed for `D >= 3` (the toy row
  `p = 5, n = 32, D = 3` is checked computationally only).
- Everything here is at the **maximal rate-1/2 row** `n = 2^41`. The
  `n = 2^40` alternative shifts every exponent by one and is not tabulated.
- `t = n/L` is the banked leading-order counting balance (C), exact to
  `0.0044%` at prize-max, not a theorem; the `t`-naming collision
  (`f2_tq_pin/REPORT.md` residual 1) is inherited and **not resolved here**
  — it belongs to the sibling `t_naming`, whose directory I did not read.
- THEOREM ADM-B's "(O1) is FALSE" is a statement about the first moment at
  the stated window, with `o(n)` read as `o(n)`; a constant-factor failure
  of LEMMA 3 is an exponential failure of (O1) and cannot be absorbed, but
  it says nothing about whether some *other* route pays K1.
- Every toy row I could brute-force has a TRIVIAL ternary kernel
  (`Z = 1`), so S3.D exercises the mass factorisation only at `Z = 1`; the
  direct-sum structure that implies it is verified non-trivially by S3.N
  (kernel dimensions 2, 4, 6). No toy is evidence about `Z_1` at the
  official row.
- The toy verifications (S3) live at `p <= 41`, `n <= 32`, `m <= 16`. They
  test the **structure** (decomposition, MDS parameters, factorisation of
  `Z`, trace collapse, coset behaviour); the prize-scale numbers are exact
  arithmetic, not extrapolation, but no toy is evidence about `Z_1` at the
  official row.
- Nothing here bounds `Z(L)`; SL-1b' is untouched and remains open.
- PP5.0 is **not** frozen and no reading of the `|K1|` seam is chosen.
- No status flip is proposed for any minted node. DRAFT ONLY; no file
  outside `notes/pilots_20260806/f2_adm/` was written; no commit, no push.
