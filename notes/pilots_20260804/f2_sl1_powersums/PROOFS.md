# SL-1 — low-weight ternary vanishing odd-power-sum relations: the proofs

Round 15, 2026-08-06. Pilot `notes/pilots_20260804/f2_sl1_powersums/`.
Verifier `verify.py`, stages S1-S13, **85/85 PASS**, digest
`F2_SL1_TERNARY_POWERSUM_ALL_PASS`. Log: `results/VERIFY_LOG.txt`.

Notation is `f2_opening/PROOFS.md`'s, restated in `PREREG.md` §1.
`R` := the number of exponents in a run of **consecutive odd** exponents
contained in `Lambda`. Under the task's `"odd l <= t"` reading,
`R = ceil(t/2)`.

---

## 0. SUBTRACTION LEDGER (hard law 5) — declared before any claim

Five surfaces swept (`critical/`, `background/`, `notes/`, `archive/`,
`dag.json`/`experiments/`). **The headline result of this pilot is that
SL-1 was ALREADY PROVED, in a stronger form, in a different lane, and no
F2 file has ever cited it.**

- **BANKED, PROVED, STRONGER — not ours.**
  `background/nodes/dli_wcl_newton_short_window_exclusion/statement.md:8-22`,
  verbatim:

  > Let `F` be a field of characteristic zero or characteristic greater than
  > `w`. Let `omega in F` have exact order `2N`, and let
  > `P(X) = sum_(i=1)^w s_i X^e_i`
  > be a reduced signed polynomial with distinct `e_i in {0,...,N-1}` and
  > `s_i in {+1,-1}`. If
  > `P(omega^(2j-1)) = 0  for j=1,...,ell`
  > and `w<=2ell`, then no such polynomial exists.

  This is SL-1's object **exactly**: signed (ternary) coefficients,
  exponents restricted to a half-period (= one representative per antipodal
  pair), vanishing on `ell = R` consecutive odd exponents. Its conclusion
  `w >= 2R+1` is **twice** the bound proved below.

- **BANKED — the proof mechanism.**
  `archive/compressed_dli_lane_20260705/b2b_primitive_core/notes/pro_skew_tower_packet.md:10-15`,
  verbatim: *"if the active support of a level-j skew is <= L_j = ceil(T_j/2),
  the only skew is zero (divide by x_i, the y_i are distinct, the Vandermonde
  minor is invertible)"*. The diag x Vandermonde-on-**minors** step is banked.
- **BANKED — LEMMA 2/THEOREM A** (`f2_opening/PROOFS.md`): the same
  factorization at the FULL `m x m` matrix. Cited, not re-derived.
- **BANKED — char-0 non-vanishing / "every relation is accidental"**:
  `critical/nodes/bounded_coeff_norm_gate/statement.md:7` (PROVED), verbatim:
  *"Tower sections contain no opposite pairs, so every nonzero tower skew is
  norm-gated at every imposed odd exponent simultaneously. No
  bounded-coefficient escape."* Plus the Lam-Leung input at
  `critical/nodes/u2c_giant_tnull_dichotomy/notes/F2_DEEP_REGIME_LAMLEUNG_NOTE.md:14-19`
  and `f2_deep_regime_exactness`, `f2_char0_sixterm_classification` (both
  PROVED). **§5 below is therefore NOT claimed as new** — only its one-line
  Z-basis phrasing is.
- **BANKED — the ternary `2^{-wt}` mass object**:
  `background/nodes/dli_c1_l1_block_owner_ledger/statement.md:15` (PROVED),
  verbatim: `Z = sum_(d in ternary kernel) 2^(-wt(d)).` — and that node already
  bounds it *via a min-weight exclusion*, which is §4's architecture at a
  different row. The "Haar baseline" at `:39` is the §6 first moment's
  precedent.
- **BANKED — Newton/BCH linearization** in the L1 lane
  (`l1_official_newton_cofactor_window_router`,
  `l1_official_frobenius_checkpoint_q_router`,
  `l1_mersenne_checkpoint_cyclotomic_normal_form`) and the 0/1 sibling's
  coding identity, `critical/nodes/moment_trade_staircase/statement.md:9`
  (PROVED), verbatim: *"CODING IDENTITY: t-moment-null blocks are
  0/1-coefficient dual codewords with t leading zero syndromes"*.
- **BANKED — the crossing lane's LEMMA Y** (`crossing_w2_opening`, round 14).
- **The BCH bound, alternant codes, GRS/MDS**: classical (Bose-Ray-Chaudhuri,
  Hocquenghem). Not claimed.

**CLAIMED AS NEW BY THIS PILOT, and nothing else:**
1. §1 THEOREM SL-1 in its **characteristic-free** and **shifted-run** form,
   and its application to the F2 lane (§2) — the banked `2R+1` node does
   **not** apply at the official row.
2. §3 the explicit **counterexamples** showing the banked node's
   `char > w` hypothesis is NECESSARY, and the measured two-branch law.
3. §4 the mass bounds (M1),(M2) and the discharge criterion (M3).
4. §6 the exact first-moment identity and the `log2 3` threshold gap
   (SL-1b).
5. §7 the cross-lane verdicts.
6. §8 CATCH-4: `t` pinned as UNDETERMINED, with the sign flip.

---

## 1. THEOREM SL-1 (the characteristic-free designed-distance law)

*Verified: S2 (268 configurations, 0 violations), S7a, S13.*

> Let `F` be **any** field. Let `n` be even, `mu_n <= F^*` of order `n`, and
> let `W <= mu_n` be closed under `x -> -x`, with `m = |W|/2` and
> `y_1,...,y_m` one representative per antipodal pair. Suppose `Lambda`
> contains `R` consecutive odd exponents
> `2a+1, 2a+3, ..., 2a+2R-1` (any `a >= 0`). Then every `eps in F^m` with
>
> ```text
>       sum_{i=1}^{m} eps_i y_i^l = 0   for every l in Lambda
> ```
>
> and `eps != 0` satisfies **`wt(eps) >= R + 1`**.

*Proof.* Suppose `eps != 0` has `w := wt(eps) <= R`, with support
`A = {i_1 < ... < i_w}`. The `w` conditions at `l = 2a+1, ..., 2a+2w-1`
(available, since `w <= R`) give `M · (eps_{i_k})^T = 0` for the `w x w`
matrix `M = (y_{i_k}^{2a+2r+1})_{r=0..w-1,\, k=1..w}`. Factor

```text
      M  =  diag(y_{i_1}^{2a+1}, ..., y_{i_w}^{2a+1}) · ( (y_{i_k}^2)^r )_{r,k}.
```

The diagonal factor is invertible (`y_i != 0`). The second factor is a
Vandermonde matrix in the squares `y_{i_k}^2`; the map `y -> y^2` on `mu_n`
is exactly 2-to-1 with fibres the antipodal pairs `{y,-y}` (`n` even, so
`-1 in mu_n`, `-1 != 1`), and the `y_i` are one per pair, so the `y_{i_k}^2`
are pairwise distinct and the Vandermonde is invertible. Hence
`eps|_A = 0`, contradicting `A = supp(eps)`. **QED**

No hypothesis on `char F` is used, and no hypothesis relating `w` to
`char F`. This is the entire point (see §3).

**COROLLARY 1.1 (SL-1 as posed) — the answer to the task.** With
`Lambda = {odd l : l <= t}`, `R = ceil(t/2)`, so every nonzero ternary
relation has

```text
        wt(eps)  >=  ceil(t/2) + 1   >   t/2 .
```

The round-14 pre-registered prediction `w >= t/2` is **confirmed and
strictly beaten**, non-asymptotically, at every rung.

**COROLLARY 1.2 (SL-1 at rungs 14-16).** `R+1` is a constant fraction of
`m_j`, so no relation of weight `o(m)` exists (S10):

| rung | `m_j` | `(R+1)/m_j`, `t = 7e10` | `(R+1)/m_j`, `t* = 8.59e9` |
|---|---|---|---|
| 14 | `2^36` | 0.50932 | 0.06252 |
| 15 | `2^37` | 0.25466 | 0.03126 |
| 16 | `2^38` | 0.12733 | 0.01563 |

**SL-1 is therefore PROVED, under every live value of `t`** (§8).

**COROLLARY 1.3 (THEOREM A is the `R >= m` case).** If `R >= m` a nonzero
vector would need weight `>= m+1 > m`, so `L^perp = 0` and `Z(L) = 1`:
`f2_opening`'s THEOREM A is recovered. *One law now covers rungs 1-13 and
14-16* (S5: 13/13 shapes, `dim L = m` in every one).

**REMARK (why this is the BCH bound).** Extend `eps` to `nu` on `Z/n` by
`nu(a_i) = eps_i`, `nu(a_i + n/2) = -eps_i`, zero off `W`. Then
`nu_hat(l) = (1 - (-1)^l) sum_i eps_i y_i^l`, which vanishes for **every
even `l` automatically**; with the odd `l` from `Lambda` the defining set is
a consecutive run `{2a, 2a+1, ..., 2a+2R-1}` and `wt(nu) = 2 wt(eps)`. So
Theorem SL-1 is the BCH bound for that cyclic code, and equivalently
`L^perp = C ∩ F_p^m` is the **alternant** code of the `F_q`-GRS code
`C = [m, m-R, R+1]` (MDS). S11 machine-checks the consecutive defining set
on 200 nonzero witnesses.

**REMARK (the consecutive hypothesis is necessary).** S7b: over 2281 gapped
odd exponent sets, **1210** admit a singular `R x R` minor, i.e. the `F_q`
minimum distance drops to `<= R`. Gapped sets are generalized Vandermonde
(Schur) minors and do vanish in characteristic `p`. S7a: over 78 consecutive
configurations, **0** singular minors. The law is governed by the longest
consecutive odd **run**, not by `|Lambda|`.

---

## 2. Why the banked `2R+1` node does not settle SL-1

`dli_wcl_newton_short_window_exclusion` requires *"characteristic zero or
characteristic greater than `w`"*. At the F2 official row
`char = p = 2^31 - 2^24 + 1 ~ 2.13e9` while `w` ranges up to
`m_16 = 2^38 ~ 2.75e11`. **`char > w` fails by two orders of magnitude.**
The Vandermonde route of §1 is the only one of the two that applies, and it
is what discharges SL-1.

---

## 3. The TRUE weight law, and the necessity of `char > w`

*Verified: S13, 39 live configurations + 12 decisive probes.*

**MEASURED LAW (all 39 live configurations, 24 attaining it exactly):**

```text
        true min ternary weight   >=   min( 2R+1,  max(p, R+1) ),
```

with **both branches attained**. Concretely:

- The `2R+1` branch is attained in 18 of 39 configurations (large `char`).
- The `char` branch is real: **6 explicit counterexamples** to `2R+1` once
  `p <= 2R`, and in **every one** the true minimum weight equals `p` exactly:

  | shape | `R` | `2R+1` | true min wt |
  |---|---|---|---|
  | `p=3^2, n=8, m=4` | 2 | 5 | **3** `= p` |
  | `p=5^2, n=12, m=6` | 3 | 7 | **5** `= p` |
  | `p=5^2, n=24, m=12` | 3 | 7 | **5** `= p` |
  | `p=5^2, n=24, m=12` | 4 | 9 | **5** `= p` |
  | `p=7^2, n=16, m=8` | 4 | 9 | **7** `= p` |

  So the banked node's `char > w` hypothesis is **necessary, not
  cosmetic** — a fact worth reporting back to the DLI/WCL lane.

- **THE DECISIVE PROBE.** The characteristic cap can never drop below
  `R+1` (it would refute §1). 12 probes in the regime `p < R+1` — *which is
  exactly the official-row regime*, `p = 2^31 << R+1 ~ 3.5e10` — and in
  **all 12 there is no nonzero ternary dual vector at all**.

**Consequence for the official row.** At `p << R+1`,
`min(2R+1, max(p, R+1)) = R+1`: the measured law collapses to exactly the
characteristic-free bound, i.e. **Theorem SL-1 is predicted to be SHARP at
rungs 14-16**, and the mechanism that breaks `2R+1` cannot reach below it.

---

## 4. New rigorous mass bounds at partial condition sets

*Verified: S8, 70 configurations, exact rational arithmetic.*

Since the minimum distance of `L^perp` is `>= R+1`, projection onto **any**
`m-R` coordinates is injective on `L^perp` (two codewords agreeing there
differ by a codeword of weight `<= R`, hence by `0`).

**(M1)** For `eps in L^perp` and a fixed coordinate set `S`, `|S| = m-R`, we
have `wt(eps) >= wt(eps|_S)`, so `2^{-wt(eps)} <= 2^{-wt(eps|_S)}`. By
injectivity the images are distinct ternary vectors of length `m-R`, and
`sum_{v in {-1,0,1}^{m-R}} 2^{-wt(v)} = 2^{m-R}` (per coordinate
`1 + 1/2 + 1/2 = 2`). Hence

```text
        Z(L)  <=  2^{m-R},        i.e.   E_c[T_W]  <=  2^{2m-R}.
```

(Trivially `E_c[T_W] <= 4^m`; this saves a factor `2^R`.)

**(M2)** Injectivity also gives `|L^perp ∩ T| <= 3^{m-R}`, and every nonzero
term is `<= 2^{-(R+1)}`, so

```text
        Z(L)  <=  1 + 3^{m-R} · 2^{-(R+1)}.
```

**(M3) — a new discharge criterion.** (M2) gives `Z(L) < 2` as soon as
`log2(3)·(m-R) - (R+1) < 0`, i.e.

```text
        R > (log2 3 / (1 + log2 3)) · m = 0.61315 · m,
   i.e. t >= 1.2263 · m       against LEMMA 2's   t >= 2m - 1,
```

a **1.631x weaker requirement on the condition count**. Honest limitation
(S10): because `m_j` doubles per rung, this widens the discharged band in
`t` but **does not move the rung cutoff** — 13 under every live `t`. It is a
better lemma, not a better rung.

---

## 5. No relation is structural (BANKED — cited, not claimed)

*Verified: S9.* For `n` a 2-power the minimal polynomial of `zeta_n` is
`X^{n/2}+1`, so `{zeta_n^a : 0 <= a < n/2}` is a **Z-basis** of `Z[zeta_n]`.
The deployed representatives `a_i = 2i+1` are distinct elements of
`[0, n/2)`, so `alpha = sum_i eps_i zeta_n^{a_i}` is a Z-combination of
distinct basis elements: `alpha = 0` iff `eps = 0`. Every ternary relation is
therefore an "accident" of `p`-divisibility.

This content is **banked** at `critical/nodes/bounded_coeff_norm_gate`
(PROVED) and in the F2 lane's own `f2_deep_regime_exactness` /
`f2_char0_sixterm_classification`; only the Z-basis phrasing is new.

*Secondary (norm) bound, recorded and DOMINATED:* `|N(alpha)| <= w^{n/2}`
while `alpha` is divisible by `>= ceil(R/f)` distinct primes above `p`
(`f = ord_n(p)`), giving `w >= p^{2R/n}`. At rung 16 this is `w >= 3.93` —
weaker than `R+1 = 3.5e10` by a factor `8.9e9`. Recorded so nobody re-runs it.

---

## 6. SL-1b — the residual, named precisely

*Verified: S12 (exact, by full enumeration over all subspaces).*

SL-1 is a **distance** statement. (O1) at rungs 14-16 needs the **mass**
`Z(L) <= 2^{o(n)}`, which is a **count**. These are strictly different, and
§4's bounds do not close the gap (at rung 16, (M2) gives `2^{0.27 m}`).

**The exact first-moment law.** For `L^perp` a uniformly random subspace of
`F_p^m` of codimension `d = dim L` (S12: verified exactly, by enumerating
*all* subspaces, at `(p,m,d) = (3,3,1), (3,3,2), (5,2,1), (3,4,2)`):

```text
        E[ Z(L) ]  =  1 + (2^m - 1)(p^{m-d} - 1)/(p^m - 1)   ~   1 + 2^m / p^d .
```

Two thresholds follow, and they are the same formula in two bases:

```text
   E[Z] = O(1)          iff  p^d >~ 2^m   iff  d >= m / log2 p     <-- LEMMA 3
   L^perp ∩ T = {0}     iff  p^d >~ 3^m   iff  d >= m · log_p 3    <-- existence
```

**The sharp observation: `f2_opening`'s LEMMA 3 — a PROVED *necessary*
condition for (O1) — sits EXACTLY at the first-moment threshold for the
mass.** The pilot's "dead heat, zero structural margin" is therefore not a
reading but a structural fact: (O1) at rungs 14-16 is precisely the
assertion that the deployed `L` is *no worse than a random subspace* at this
one statistic. The existence threshold is the same bound in base 3, so the
two differ by **exactly `log2 3 = 1.58496`** — LEMMA 3 falls 58.5% short of
what would kill `L^perp ∩ T` outright.

```text
   rung 14:  mass threshold dim L >= 2.2176e9   existence threshold 3.5148e9
   rung 15:  mass threshold dim L >= 4.4351e9   existence threshold 7.0295e9
   rung 16:  mass threshold dim L >= 8.8703e9   existence threshold 1.4059e10
```

**SL-1b (the named residual, replacing SL-1 on the obligation list):** prove
a **lower** bound `dim_{F_p} L >= m · log_p 3` (or a second-moment /
anti-concentration step for `Z(L)`). This is a counting statement about the
deployed `L`; SL-1 (distance) is now discharged and is not the obstruction.

*Supporting measurement (S4):* over 74 configurations the count threshold
`m·log2 3 > dim L · log2 p` **never under-predicts** — every configuration
admitting a nonzero ternary dual vector satisfies it (0 false negatives;
all 12 misses are over-predictions, the safe direction). The rival
"distance threshold" predicts correctly only 23/74.

---

## 7. The cross-lane verdicts

*Verified: S11, S13.*

**(a) F2 <-> DLI/WCL: a CONFIRMED IDENTIFICATION — and the real find.**
`dli_wcl_newton_short_window_exclusion` (PROVED) and F2's SL-1 are the
**same object**: signed coefficients, half-period exponents, vanishing on
consecutive odd exponents. No F2 file has ever cited it. This is a genuine
missed reduction, and it runs in the direction DLI/WCL -> F2. Its only
defect is the `char > w` hypothesis, which §3 shows is *necessary* and which
fails at the F2 official row — so the import is real but must be re-proved
characteristic-free, which §1 does.

**(b) F2 <-> crossing (the route the task asked me to check): a shared
LENS, NOT a sixth reduction.** Both objects are codewords of a cyclic code
with a **consecutive defining set** — machine-confirmed for the F2 side in
S11. But three blockers are each independently fatal to a drop-in
reduction:

- **(B1) alphabet.** Crossing uses 0/1 indicator vectors of subsets;
  SL-1 uses `{-1,0,+1}`, and the sign is not removable — the ternary
  alphabet *is* the binary alphabet of the full window folded by `x -> -x`.
- **(B2) weight regime.** Crossing counts at one huge weight `r' = n-k-w`
  with a tiny defining set (`w-1` zeros, `w = O(1)`), where the BCH bound is
  **vacuous**; SL-1 asks for the **minimum** weight with a huge defining set
  (`R ~ 3.5e10` zeros), where the BCH bound is **everything**. Same code
  family, opposite ends of its weight enumerator.
- **(B3) question type.** Minimum distance (a bound) vs enumeration (a
  count). The BCH machinery answers the first and is silent on the second.

**The honest upgrade:** (B3) is exactly §6's residual. Mystery 2's remaining
obligation (SL-1b, a ternary constant-weight **count** in a cyclic code) and
mystery 4's heart (LEMMA Y's constant-weight count in a BCH code) are the
**same species of open problem**. That is a shared terminal, not a
reduction — the same shape of verdict the crossing pilot reached with the
band lane.

---

## 8. CATCH-4 — `t` pinned, and it pins as UNDETERMINED

*Verified: S10.*

`t` has **no definition anywhere in the repo**. It is a bare literal
`t = 7e10` at `f2_opening/verify.py:958` and `:1038`, traceable to the banked
product `t·log2 q ~ 2.15e12`
(`archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`
via `notes/floor_campaign/SURVEY_X4_CLUSTER.md:15-17` and
`notes/f2_campaign/F2_CAMPAIGN_LOG.md:184-187`) divided by `log2 p ~ 31`.
The competing reading is exact and formula-backed:
`t* = 8,592,912,739` (`background/nodes/xr_radius_arithmetic/proof.md:41-58`).
The conflict is already booked at
`notes/kernel_basis/TARGET_3C_EXTRACTION.md:26-32`: *"THE OFFICIAL
FACTORIZATION q = p^k IS PINNED NOWHERE."*

Recomputed with `log2 p = 30.988685`:

| `t` | source | LEMMA 2 cutoff | LEMMA 3 @ rung 16 |
|---|---|---|---|
| `7e10` | `verify.py:958,1038` literal | rungs 1-13 | **OK, 7.892x** |
| `2^36` | `F2_CAMPAIGN_LOG.md:213,376,717,734` | rungs 1-13 | OK, 7.747x |
| `2^41/log2 p` | base-field reading | rungs 1-13 | OK, 8.000x |
| `t* = 8,592,912,739` | `xr_radius_arithmetic/proof.md:41-58` | **rungs 1-10** | **VIOLATED, 0.9687x** |

- The 7.892x reproduces `PROOFS.md:233`'s claimed 7.89x **exactly**.
- Under `t*` the margin is a **sign flip, not a shrinkage**: a PROVED
  necessary condition for (O1) is violated at rung 16 by 3.1%.
  `PROOFS.md:235-237` says *"any re-pricing of `t` downward by an order of
  magnitude would violate"* it; the actual competing value re-prices
  downward by only 8.15x and **already violates it**.
- Under `t*` the LEMMA 2 discharge band also shortens from rungs 1-13 to
  **rungs 1-10**, i.e. six open rungs instead of three.
- Independent corroboration (S12): under `t*` at rung 16 the maximum
  possible condition budget `dim L · log2 p <= 2.66e11` bits is **below**
  the entropy `m log2 3 = 4.36e11` bits (headroom 0.61x), so the ternary
  dual would be expected to be non-trivial there — the same conclusion by a
  different route.
- The internal `m_16 = 2^38` (`PROOFS.md:233`) vs `2^39` (`PREREG.json:58`)
  ambiguity halves or doubles every margin; under `t*` and `m_16 = 2^39`,
  LEMMA 3 is violated at **rungs 15 AND 16**.

**Load-bearing verdict: `t` cannot be pinned from the repo, and which value
is correct decides whether rung 16 is discharged. This is a maintainer-level
question (`q = p^k`), not a hygiene item.** SL-1 itself is **immune**: the
designed distance is `Omega(m)` at rungs 14-16 under all four values
(minimum fraction 0.01563).

---

## 9. Scope — what is NOT claimed

- §1 is characteristic-free but says nothing about the **count** of ternary
  dual vectors; (O1) at rungs 14-16 remains open on SL-1b (§6).
- §3's law `min(2R+1, max(p, R+1))` is a **measurement** over 39
  configurations with `m <= 16`, not a theorem. Its official-row reading
  (Theorem SL-1 is sharp) is a pre-registered prediction.
- Extending `dli_wcl_newton_short_window_exclusion` to `char <= w` is a
  named conjecture (SL-1c); §3 shows it is FALSE as literally stated once
  `p <= 2R`, so any extension must carry the `max(p, R+1)` branch.
- Nothing here touches SL-2/CATCH-3 (the `|K1|` normalisation seam) or
  freezes PP5.0.
- No status flip is proposed for any minted node. The recommended board
  edits are: SL-1 -> discharged; add SL-1b; flag CATCH-4 upward.
