# F2 RE-POSE — the proofs (round 20, 2026-08-06)

Replay: `tools/ramguard local -- python3 notes/pilots_20260806/f2_repose/verify.py`
→ **60 checks, 0 FAIL**, digest `F2_REPOSE_ALL_PASS`.

Everything relied on is quoted verbatim with `file:line`. Statements I
DERIVE are labelled DERIVED and carry their verifier stage; statements
I QUOTE are labelled QUOTED. Nothing here is a status flip.

---

## 0. THE SOURCES (verbatim)

**(Q1) The obligation as posed** —
`notes/pilots_20260802/f2_fixed_sector/REPORT.md:33`:

> **Replacement obligation (constructive)**: K1 must be paid by MASS, not cancellation: (O1) first-moment target E_{c in K1}[exp S_c] <= 2^{n/2 + o(n)} (2^{n/2} = the exact independent-value scale); (O2) the same at fixed b (the Hamming-slice fence forbids (O1) alone); (O3) PP5.0 must carry the pullback ramification 2^d.

**(Q2) The terminal consumer** —
`background/nodes/u2c_giant_tnull_dichotomy/node.json:8`:

> the consumer (x4 via b2_modp_giant_extras) consumes ONLY the count '#{non-coset-union t-null blocks + trade families} <= n^3 = 2^123 at official prize-max rows'.

**(Q3) The tolerance chain — the whole derivation of `2^{1.05e12}`** —
`notes/f2_campaign/EXTRAS_CONTRACTION_TARGET.md:24-27`:

> Tolerance chain (log #9, banked): official rows have t*log2(q) ~
> 2.15e12 > n ~ 1.1e12 with the window empty at every b — the flat
> model predicts < 2^{-1e12}-scale occupancy vs budget n^3, so
> max/mean <= L^t with L <= 2^{(1.05e12)/t} ~ 2^15 wins.

**(Q4) The consumable form** —
`background/nodes/u2c_giant_tnull_dichotomy/notes/QUALITY_f2_growing_order_myerson.md:7-9`:

> The statement's tolerance 2^{1.05e12}
> (equivalently per-condition extras <= 2^15 on the p-free ladder) is the
> calibrated consumable form.

**(Q5) The `o(n)` label is fenced by the chain itself** —
`notes/pro_briefs_20260801/responses/BRIEF5_PRO_DOSSIER.md:43-45`:

> Also fenced: bare `2^o(n)` is NOT a finite
> certificate (a 2^(10^15 + sqrt(n)) counterexample beats the label and
> busts the allowance).

**(Q6) The consumer's own scope rule** —
`background/nodes/u2c_giant_tnull_dichotomy/node.json:8` (CATCH #11, 2026-07-07):

> the sub-balance window must be read at the GENERATED field B0 = F_p(D), i.e. |B0|^t >= 2^n, NOT at the ambient q. [...] Consumer rule: x4/b2_modp_giant_extras consumes F2 only where |B0|^t >= 2^n; base-domain extension rows route through the f1/ext descent (s6 imported window).

**(Q7) The ambient/moving-top notation correction (I1)** —
`background/nodes/u2c_giant_tnull_dichotomy/node.json:8`:

> I1 — the consumer budget n^3 = 2^123 pins prize-max N = 2^41 (older '~2^40' prose is the base-field window reading)

**(Q8) Lemma 1, the ternary-dual identity** —
`notes/pilots_20260804/f2_opening/PROOFS.md:52-57`:

> ```text
>     E_{c in K1(Lambda)} [ T_W(c) ]  =  sum_{eps in L^perp cap {-1,0,1}^m}
>                                               2^{m - wt(eps)}
>                                     =  2^{m} * Z(L),
> ```

and `:157-158` (the punctured form, `N := |K1(Lambda)| = p^{2|Lambda|}`):

> ```text
>     E_{c != 0}[T_W] = (N * 2^m - 4^m) / (N - 1)  <  2^m,
> ```

**(Q9) `|Lambda| = ceil(t/2)`, `t_F2` pinned by the counting balance** —
`notes/pilots_20260806/t_naming/REPORT.md:13`:

> `t_F2` := the **largest Newton index** in `Lambda ⊆` **frequency space** (not `|Lambda|`), governed by the counting balance, rate-independent.

**(Q10) The three readings of `log2|K1|`** —
`notes/pilots_20260806/f2_adm/PROOFS.md:559-561`:

> ```
>    extension reading :  log2|K1|      = |Lambda| · L        =  n/2   EXACTLY
>    base reading      :  log2|K1|      = |Lambda| · log2 p   =  n/(2e)
>    effective reading :  log2|K1|_eff  = k |Lambda| log2 p   =  (k/e)(n/2)
> ```

**(Q11) The `(T*)` deficit** —
`notes/pilots_20260806/o1_generating_adversary/REPORT.md:22`:

> `n − t*L = (2n/(L² ln2))(1+O(L^{-2}))` and `Δ = −n/(L² ln 2) + O(L)`

**(Q12) THEOREM Z-3 (non-generating)** —
`background/nodes/f2_o1_status_split/statement.md:20-22`:

> (ii) THEOREM Z-3 (independent route,
> object-level): Z(L) >= 2^{m(1 - (k/e)(tL/n))} = 2^{Theta(n)} — the
> K1 first moment itself exceeds its target.

**(Q13) THEOREM 7, unconditional** —
`background/nodes/f2_z1_mass_knife_edge/statement.md:59-61`:

> the executable substitute (AM-GM + Z-2 moments, THEOREM 7: Z_1 <= 2^{0.8908·S}
> unconditional) closes only at p <= 8.30 — Z-NOGO's own threshold.

**(Q14) The knife edge** —
`background/nodes/f2_z1_mass_knife_edge/statement.md:48-51`:

> and FIRES at +17.98 bits under the exact-balance reading (in which case ternary kernel vectors provably exist at the witness row: Z_1 >= 2^{17.98}, the EXACT-ZERO form of the terminal is dead, yet Z = 2^{o(n)} so the MASS form survives).

**(Q15) The prime-field discharge** —
`critical/nodes/f2_k1_contraction_theorem/node.json:7` (status PROVED):

> at prime-field rows (q = p prime, mu_n in F_p^x) with n >= 512 and n >= 3 sqrt(p): every p-free moment condition contracts the t-null census with per-condition loss L <= 4.

---

## 1. THEOREM C1 — THE CONSUMER CONTRACT, ABSOLUTE FORM. *DERIVED. Verified: S1.*

Write `N` for the ambient domain (`N = 2^41` at prize-max, by (Q7)),
`t` the condition count, `L = log2 q`, and `b` a block size.

**Claim.** The consumer's requirement (Q2) is equivalent to

```text
    | sum_{c != 0} eps_c exp(S_c)  -  STRUCT DRIFT |   <=   N^3 · q^t
                                                      =   2^{3 log2 N + t·L}
```

at each `b`, and to `2^{4 log2 N + t·L}` when summed over all `b`.

*Proof.* The census identity (`PRO_FLOOR_2_F2_SUMMIT_V4.md:26-27`,
*"sum_{c != 0} eps_c exp(S_c) = q^j N_total - 2^n"*) gives
`extras = (census deviation − STRUCT DRIFT)/q^t`. (Q2) requires
`extras <= N^3`. Multiply through by `q^t`. Summing over the `N+1`
values of `b` replaces `N^3` by `N^3(N+1)`, i.e. `3 log2 N → 4 log2 N`. ∎

**COROLLARY C1.1 (the tolerance is the balance surplus). *Verified: S1.***
Expressed as a max-to-mean ratio at slice `b`, with flat mean
`C(N,b)/q^t`, the tolerance is

```text
    log2 TOL(b)  =  3 log2 N  +  t·L  -  log2 C(N, b),
```

which at the central slice is `3 log2 N + (t·L − N) + (1/2)log2(πN/2)`.
**The consumer's tolerance is the counting-balance surplus `t·L − N`,
up to `O(log N)`.**

*Check.* On the tower row of (Q3) — `n = 2^40`, `t·L = 2.15e12` — the
formula returns **1.05049e12** against the banked **1.05e12**: agreement
to **0.047%** (S1.2). The banked number is reproduced exactly by
`t·L − n` (S1.3). This is not a coincidence of my reading; it *is* their
arithmetic, since (Q3)'s "`< 2^{-1e12}-scale occupancy`" is
`C(n,b)/q^t = 2^{n − t·L}`.

**COROLLARY C1.2 (the `2^{1.05e12}` figure does not survive its own
node's correction). *Verified: S2.*** (Q7) pins the consumer's budget to
`N = 2^41`. Evaluating C1.1 at `N = 2^41` with the same `t·L = 2.15e12`
gives log2 TOL = **−4.90e10**: *negative*. The deficit `4.90e10`
matches BRIEF5's *"`n_r/2` fails by 49.5G bits"*
(`BRIEF5_PRO_DOSSIER.md:37`) to 1%, and equals `N/2 − 1.05e12` (S2.3)
— **the "49.5G bits" threshold and the ambient/moving-top notation
hazard are the same number.**

---

## 2. THEOREM C2 — THE COLLAPSE, AND THE FINITE MASS TARGET. *DERIVED. Verified: S3, S4, S5.*

By (Q8), (Q9), (Q10) with the extension reading, and the balance
`t·L = N` (calibration (C)):

```text
    log2|K1| = |Lambda|·L = ceil(t/2)·L = t·L/2 = N/2,      m = |W|/2 = N/2,
```

so at the **full-group window**

```text
    |K1| · 2^m  =  2^{N/2 + N/2}  =  2^N  =  4^m         (THE COLLAPSE)
```

— verified to within `L` bits (S4.1/S4.2: the residue is `182.98` bits,
from `ceil` and the balance surplus). Hence, by (Q8)'s punctured form,

```text
    sum_{c in K1, c != 0} T_W(c)  =  |K1|·2^m·Z(L) − 4^m  =  2^N ( Z(L) − 1 ).
```

**THEOREM C2 (the consumer-exact K1 obligation).** Under calibration (C),
THEOREM C1 applied to the K1 class reduces **exactly** to

```text
                        Z(L)  <=  1 + N^3 .
```

*Verified: S5.* The measured budget at `t* = 8,589,934,679`,
`L = 255.999997420` is `log2 Z <= 90.98` bits; the general range is
`[4 log2 N − L/2, 4 log2 N + L/2] = [36, 292]` bits (the `ceil(t/2)`
rounding costs up to `L/2`, the balance surplus returns up to `L/2`).

**This is the re-pose.** Three things change:

1. **The target is FINITE.** `Z <= 1 + N^3` is a certificate; `2^{o(n)}`
   is not — by the chain's own fence (Q5).
2. **It is not implied by, and does not imply, (O1).** (O1)'s
   `Z <= 2^{o(n)}` is *weaker* in `n` than `Z <= 2^{O(1)}`. **The lane's
   posed obligation was UNDER-posed, not over-posed.**
3. **It is not refuted by any banked lower bound.** Z-FLOOR gives
   `Z >= 1`; the knife edge's firing value (Q14) gives
   `Z = Z_1^e >= 2^{17.98 e}`, i.e. `2^{71.9}` at `e = 4` — **inside**
   the `90.98`-bit budget, with `19.1` bits to spare (S7).

**COROLLARY C2.1 (the terminal, finitely posed).** With `Z = Z_1^e`, the
target is `Z_1 <= 2^{(4 log2 N + (t·L − N) − (ceil(t/2)L − t·L/2))/e}`.
At the witness (`e = 4`): **the live window is `Z_1 ∈ [2^{17.98},
2^{22.75}]`, width 4.77 bits** (S7.4). The F2 terminal is a
**4.77-bit question**, not an asymptotic one.

---

## 3. THEOREM C3 — THE FIFTH FACE. *DERIVED. Verified: S1.3, S4, S6.*

`f2_o1_status_split/statement.md:61-65` records a **four**-face seam
(the balance `t·L >= n`; LEMMA 3's requirement; the vacuity boundary of
Z-FLOOR; the PP5.0 average-vs-sum seam). C1.1 adds a fifth:

> **THE CONSUMER'S OWN TOLERANCE IS THE SAME INEQUALITY'S SLACK.**

`log2 TOL = 3 log2 N + (t·L − N) + O(log N)`. All five faces are
`t·L − N`, and the campaign's own calibration puts it at zero.
Consequences:

- **Under (C)** (`t·L − N ∈ [0, L)`): the budget is `O(log N) + O(L)`
  bits — THEOREM C2.
- **Under the RULED (T\*)** (Q11: `N − t·L = 2N/(L² ln2) = 9.68e7`,
  S6.1): `log2|K1| = t·L/2 = N/2 − 4.84e7`, so LEMMA 3 **forces**
  `Z >= 4^m/(|K1|2^m) = 2^{4.84e7}` (S6.2) while THEOREM C1 caps
  `|K1|2^m Z <= 4^m + 2^{4log2N + t·L}`, whose right side is dominated
  by `4^m` because `4 log2 N + t·L − 2m = 164 − 9.68e7 < 0` (S6.3).
  **The contract therefore pins `Z` to its LEMMA-3 floor with
  multiplicative headroom `2^{164 − 9.68e7}`** (S6.4) — an
  **exact-value obligation**. No mass *upper* bound of any strength can
  discharge an exact-value obligation.

**VERDICT.** Under (C) the lane has a finite target (C2). Under the
ruled (T\*) **the lane has NO candidate at generating rows**, and the
reason is not `Z_1`: it is that the consumer's budget is negative.

---

## 4. THE READING AMBIGUITIES, PRICED (PREREG §2 clause 1)

The chain does not determine the contract uniquely. Four live readings,
each quoted, each priced:

| # | ambiguity | readings | price |
|---|---|---|---|
| A1 | ensemble calibrating `t` | (C) `2^n` vs (T\*) slice | budget `+91` bits vs `−9.68e7` bits — **decides whether a candidate exists at all** |
| A2 | ambient `N` | `2^41` (Q7) vs `2^40` (Q3 prose) | tolerance `+1.05e12` vs `−4.90e10` (C1.2) |
| A3 | `log2\|K1\|` (Q10) | extension `N/2` / base `N/2e` / effective `(k/e)(N/2)` | extension ⇒ THE COLLAPSE; base ⇒ budget `+3N/8` bits (a `Theta(N)` contract, trivially met) |
| A4 | PP5.0 composition | *"add / Cauchy / multiply"* (`BRIEF5_PRO_DOSSIER.md:41-42`) | for a **fixed** `c` the composition is forced MULTIPLICATIVE (`T_{mu_N} = prod_j T_{W_j}`, a product over a partition); but the class `K1` is a property of `Lambda`, hence global, so the **sum over `c` does not factor** — the per-rung slack of §5(iv) is NOT aggregable (S12) |

**A2 is a defect, not a choice**: (Q3) computes the tolerance against
`n = 2^40` while (Q7) pins the budget's `n^3` to `N = 2^41`. One chain,
two `n`s, in the same product.

**A1 is likewise not fully free**: (Q3)'s own mean is the *slice*
`C(n,b)/q^t` while its window-empty test is the *`2^n` balance*. The
consumer uses both ensembles in one sentence.

---

## 5. THE WEAKNESS LADDER (R2) — tested weakest-first

**(i) MEDIAN / typical value — REFUTED as sufficient.**
PP5.0 is ruled = SUM (`f2_o1_status_split/statement.md:85-86`), and by
(Q8) the consumer's object is the *exact first moment*, which Lemma 1
identifies with `2^m Z` — there is no mean/median gap to exploit,
because `Z` is not a distribution over `c` but a single number
determined by `L^perp`. A median bound gives only
`median <= 2·budget/|K1|` (Markov, one direction). **Necessary, never
sufficient.** *This kills the brief's suggested weakening.*

**(ii) TAIL-COUNT — not weaker.** The banked criterion
(`f2_z1_mass_knife_edge/statement.md:65-67`,
*"the TAIL-COUNT |{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)} for all c"*)
quantifies over **all** `c` and is equivalent to the mass bound.

**(iii) CAUCHY–SCHWARZ (my pre-registered B3) — REFUTED. *Verified: S9.***
All K1 terms are non-negative, so
`sum_{c} T <= sqrt(|K1|)·sqrt(sum_c T^2)`, giving an unconditional
*ratio* bound `sqrt(|K1|) = 2^{N/4}`. But THEOREM C1's contract is
**absolute**, and `E_c[T^2] >= 6^m` (the constant term of
`(2 + z + z^{-1})^2` is 6), so the C-S bound is
`log2|K1| + (m/2)log2 6 = 2.52e12` against the exact Lemma-1 value
`log2|K1| + m + log2 Z = 2.199e12` — **worse by 3.22e11 bits**, and
`3.22e11` bits over the budget. A ratio bound cannot discharge an
absolute contract whose denominator is larger than the numerator.
**B3 dies exactly at its pre-registered falsifier.**

**(iv) WEAKENED EXPONENT AT PARTIAL WINDOWS — a real candidate,
CONDITIONAL. *Verified: S11, S12.*** At a rung window with `m_W` pairs
the budget for `log2 Z_W` is `4log2N + (t·L − N) + N/2 − m_W`. At the
top rung (`m_W = N/4`) that is **5.498e11 bits**, and THEOREM 7 (Q13)
gives `log2 Z_W <= 0.8908·m_W = 4.897e11` — **it FITS, with 6.00e10
bits of slack** (S11), at *every* `k`. **But the slack is not
aggregable**: the sectors partition `mu_N`, so `sum_j m_j = N/2`
exactly (S12.1), and the sum over `c` does not factor across sectors
(A4). **VERDICT: a candidate that exists only if PP5.0 supplies a
Hölder-type composition across sectors. PP5.0 has no statement.
Labelled CONDITIONAL, not sound.**

**(v) THE FINITE MASS TARGET `Z <= 1 + N^3` (THEOREM C2) — THE WEAKEST
SUFFICIENT INTERMEDIATE, at generating rows, under (C).**
Status: **OPEN, not refuted, NOT proved.** Instruments and their exact
distance from it:

- Z-FLOOR: `Z >= 1` — inside.
- Knife edge (Q14): `Z >= 2^{71.9}` at `e = 4` — inside, 19.1 bits.
- Z-1 (min weight `>= 2R+1 = 8.59e9`): no upper bound.
- THEOREM 7 (Q13): `log2 Z <= 0.8908·m = 9.794e11` — **misses by
  9.794e11 bits; the exponent constant must shrink by 1.08e10×**
  (S8.2). That factor is the exact size of the remaining gap.

**PRE-REGISTERED FALSIFIER for (v):** an admissible generating row
exhibiting `Z_1 > 2^{22.75}` (equivalently `> N^3/e` ternary dual mass)
— e.g. more than `2^{22.75 + 2R+1}` nonzero ternary dual codewords, or a
proof that the negacyclic shift-and-sign group's `4S = 2^40` orbits
already contribute `> 2^{22.75}`.

---

## 6. NON-GENERATING ROWS (R3)

### 6.1 THEOREM D (EXACT DESCENT). *DERIVED HERE. Verified: S15, 89,252 checks, 0 bad, 4 rows.*

Let `q = p^e`, `mu_N <= F_q^*`, `k = ord_N(p)`, so `F_p(mu_N) = F_{p^k}`
and `k | e`. For `x in mu_N` we have `x^l in F_{p^k}`, so by trace
transitivity and `F_{p^k}`-linearity of `Tr_{F_q/F_{p^k}}`:

```text
  chi_C(x) = Tr_{F_q/F_p}( sum_l C_l x^l )
           = Tr_{F_{p^k}/F_p}( sum_l Tr_{F_q/F_{p^k}}(C_l) · x^l )
           = chi_{c}(x),      c_l := Tr_{F_q/F_{p^k}}(C_l) in F_{p^k}.
```

Hence `C |-> c` is surjective with **all fibres of size
`p^{(e−k)|Lambda|}`**, and therefore: the evaluation image `L`, its
ternary dual, `dim L`, `Z(L)`, the minimum weight, and
`E_{c in K1}[T_W]` are **IDENTICAL** to those of the row `(p, q' = p^k)`
at the same `Lambda` and the same window. The ambient extension beyond
the generated subfield acts by an invertible diagonal and is invisible.

*Verified* by explicit finite-field arithmetic at `(p,e,n,k) =
(7,2,6,1)`, `(7,4,8,2)`, `(5,4,6,2)` (all non-generating) and
`(3,2,8,2)` (generating control): every identity held, image size
`p^k`, fibre sizes `p^{e−k}`, 0 discrepancies.

**COROLLARY D.1 — the descent does NOT rescue; it EXPLAINS the kill.**
The descent holds at *fixed* `Lambda`. The non-generating row's `t` is
pinned by the **ambient** balance `t·(e log2 p) = N`, so
`dim L <= k|Lambda|` gives `dim L·log2 p <= (k/e)(N/2) = (k/e)m < m`,
and LEMMA 3 forces `Z >= 2^{m(1−k/e)}` — **which is exactly THEOREM Z-3
(Q12)**. Against C2's budget of `~91` bits the excess is `2^{5N/12}` at
`(k,e) = (1,6)` (S10.8, matching `f2_adm` CATCH-1's nested reading
exactly) down to `2^{N/10}` at `(4,5)` — **every non-generating class
misses by `2^{Theta(N)}`** (S10). *The row is not underpowered; its `t`
was allocated against a field it cannot use.*

### 6.2 THE THREE REGISTERED ROUTES — verdicts

**(i) the coset/class decomposition (ADM-1/2) — NO CANDIDATE.**
The decomposition survives at `k < e` (it never uses `k`), but the
deficit is **object-level** (Z-3 / THEOREM D.1), not a decomposition
artefact. Re-decomposing cannot pay a `2^{m(1−k/e)}` excess.
*Scope correction (coordinator, §8): ADM-1/2's direct-sum GRS structure
is **plus-branch only**; on the minus branch the reduction is a coupled
negacyclic one whose root-disjointness is not closed-form. My verdict
here does not depend on ADM-1/2 — it depends only on `dim L <= k|Lambda|`
(ADM-3) — so it holds on both branches.*

**(ii) partial windows — CANDIDATE, CONDITIONAL ON PP5.0.**
As §5(iv): at `m_W = N/4` the budget is `5.498e11` bits and THEOREM 7
delivers `4.897e11` **at every `k`, generating or not** (S11). The
`k`-dependence vanishes because LEMMA 3 is *vacuous* at `m_W = N/4`
(S11.3). Blocked only by the non-aggregability of §5(iv)/A4.

**(iii) an existing proved node covers small-ord rows — YES, at `k = 1`,
by a one-line reduction. *Verified: S13.***
`k = 1  ⟺  N | p−1  ⟺  mu_N <= F_p^*`. For `S ⊆ mu_N <= F_p^*` every
power sum `p_j(S)` lies in `F_p`, so the condition `p_j(S) = 0` in `F_q`
is the *same condition* as in `F_p`: **the `F_q`-census and the
`F_p`-census are the same integer.** Hence `f2_k1_contraction_theorem`
(Q15, status **PROVED**, critical) applies verbatim, and its hypotheses
hold at admissible scale (`N >= 512`; `N = 2.199e12 >> 3 sqrt(p) =
7.71e6`, S13.2). It gives per-condition loss `<= 4` against a tolerance
of `2^15` — **four orders of margin, bypassing (O1) entirely.**
*This covers the banked killer exhibit `p = 3·2^41+1, q = p^6` (k=1<e=6)
and the whole `e = 1` generating class.*
**NOT covered: `k ∈ {2,4}`** — and the node itself names that gap:
*"The k = 2 breakage study (what fails at q = p^2) is the summit's
minimal probe"* (`f2_k1_contraction_theorem/node.json:7`).

### 6.3 THE SCOPE QUESTION IS ALREADY ANSWERED BY THE CONSUMER. *Verified: S16, S17.*

`f2_o1_status_split/statement.md:25-28` records as an open
**MAINTAINER QUESTION**:

> the F2 lane requires a hypothesis "the
> smooth domain generates F" that the rules freeze does not supply

**The consumer supplies it — a month earlier.** (Q6), banked
2026-07-07: *"Consumer rule: x4/b2_modp_giant_extras consumes F2 only
where |B0|^t >= 2^n"*, with `B0 = F_p(D) = F_{p^k}`. Combining that
rule (`t·k·log2 p >= N`) with the lane's ambient balance
(`t·e·log2 p = N`) gives `k/e >= 1`, i.e.

```text
        the consumer's beta-normalization rule  ==  k = e.
```

Verified at 7 `(k,e)` pairs: the rule holds **exactly** on the
generating ones and fails on every non-generating one (S16).
Non-generating rows *"route through the f1/ext descent"* — a different
lane, by the consumer's own instruction.

**And the kill was already banked there too.** CATCH #11's KoalaBear
instance (`n = 2^21`, `q = p^6`, effective `k = 1`) records an excess of
`2^{1,740,627}`; I reproduce **1,747,600** from its own parameters
(0.4%), and it equals `(1 − k/e)·t·log2 q = (5/6)·t·log2 q` (S17) —
**the same theorem as Z-3 / ADM-B at a different scale, one month
earlier.** (Hard-law-5 subtraction: the 2026-08-06 non-generating kill
is a re-derivation, not a discovery.)

---

## 7. THE LANE STATEMENT (R4) — NODE-DRAFT, coordinator mints after audit

```text
id:      f2_consumer_contract_repose            (DRAFT — not minted)
status:  DRAFT (contains PROVED, OPEN and FALSE parts, separated below)

STATEMENT. THE F2 LANE'S OBLIGATION, RE-POSED FROM THE CONSUMER DOWN,
on the prize-admissible object at ambient N = 2^41.

[PROVED — THEOREM C1 + C1.1] The consumer requires
  |census deviation − STRUCT DRIFT| <= N^3 q^t  (per b; N^4 q^t summed),
equivalently a max-to-mean tolerance log2 TOL(b) = 3 log2 N + t·L
− log2 C(N,b). THE TOLERANCE IS THE COUNTING-BALANCE SURPLUS t·L − N up
to O(log N). Reproduces the banked 2^{1.05e12} to 0.047% on the tower row.

[PROVED — THEOREM C2, the COLLAPSE] At the balance t·L = N with the
extension reading, |K1|·2^m = 4^m exactly (m = N/2), so
  sum_{c in K1, c != 0} T_W(c) = 2^N (Z(L) − 1),
and the consumer contract on K1 is EXACTLY  Z(L) <= 1 + N^3.
Measured budget at the witness: log2 Z <= 90.98 bits; range [36, 292].

[OPEN — the re-posed terminal, F2-MASS-N^3] Prove Z(L) <= 1 + N^3 at
generating admissible rows, i.e. Z_1 <= 2^{22.75} at e = 4. Live window
[2^{17.98}, 2^{22.75}] — 4.77 bits. Not refuted; NOT proved. Best
unconditional instrument (THEOREM 7) misses by 9.794e11 bits; its
exponent constant must shrink by 1.08e10x.
FALSIFIER: an admissible generating row with Z_1 > 2^{22.75}.

[FALSE / NO CANDIDATE — under the ruled ensemble] Under (T*) the budget
is negative: LEMMA 3 forces Z >= 2^{4.84e7} while the contract caps Z at
the same value with multiplicative headroom 2^{164 − 9.68e7}. The
obligation becomes an EXACT-VALUE obligation on Z, which no mass upper
bound can meet. THE LANE HAS NO CANDIDATE AT GENERATING ROWS UNDER (T*).

[SCOPE — settled inside the chain, not a maintainer question] The
consumer consumes F2 only where |B0|^t >= 2^n, B0 = F_p(mu_N) = F_{p^k}
(u2c CATCH #11, 2026-07-07). Given the ambient balance this rule IS
k = e. Non-generating rows route through the f1/ext descent.

[PROVED — THEOREM D, exact descent] At fixed Lambda the row (p, p^e)
and the row (p, p^k) have identical L, L^perp, dim L, Z, min weight and
E_{c in K1}[T_W]; the ambient extension acts by an invertible diagonal
with equal fibres p^{(e−k)|Lambda|}. Consequence: Z-3's excess is the
mis-allocation of t against a field the row cannot use.

[PROVED — coverage at k = 1] mu_N <= F_p^*, so the F_q-census IS the
F_p-census and f2_k1_contraction_theorem (PROVED) discharges the row
with per-condition loss <= 4 vs tolerance 2^15. Covers the e = 1
generating class AND every k = 1 non-generating row (incl. the banked
exhibit p = 3·2^41+1, q = p^6).

[OPEN — k in {2,4}] Neither covered by the k=1 route nor discharged by
the mass route. Named upstream as "the summit's minimal probe".

[CONDITIONAL — partial windows] At m_W = N/4 the budget is 5.498e11 and
THEOREM 7 delivers 4.897e11, at every k. Blocked: sectors partition
mu_N (sum_j m_j = N/2 exactly) and the sum over c does not factor, so
the slack is not aggregable without a PP5.0 Hölder composition. PP5.0
HAS NO STATEMENT.

NOT CLAIMED: any bound on Z_1; the ensemble pin; PP5.0; the minus-branch
object structure; that (O1) is true or false (superseded — it is the
wrong intermediate either way).
```

---

## 8. THE COORDINATOR CORRECTION, RECORDED VERBATIM AND CHECKED

Received mid-pilot; recorded as instructed:

> 1. THE THREE-CLASS GENERATING CENSUS IS FALSE. Canonical's THEOREM G1/G2 ("generating classes are exactly (e_p,e,k) in {(>=41,1,1),(40,2,2),(39,4,4)}") ran the LTE law D = 41 - v_2(p-1) throughout — that is the p ≡ 1 mod 4 law only; the p ≡ 3 mod 4 branch runs on v_2(p+1). The correct census is FIVE signed types: the three banked PLUS-branch types AND two MINUS-branch types (a=1, b>=40, e=2) and (a=1, b=39, e=4). Explicit new admissible generating row: p = 2^61 - 1 (Mersenne, p ≡ 3 mod 4), q = p^2, 2^41 | q-1, ord = 2 = e. [...] LEMMA ADM-1/2's direct-sum/GRS structure is PLUS-BRANCH-ONLY — on the minus branch the reduction is a COUPLED NEGACYCLIC one (structurally different; a coupled kernel reduction exists but its root-disjointness is not yet closed-form).
> 2. For your R2: the generating-row domain is five classes, not three [...]
> 3. For your R3(i): "the coset/class decomposition still holds" is true on the plus branch only. Do not price minus-branch rows with ADM-2.
> 4. [...] an exact-descent mechanism exists showing non-generating rows reduce to generating rows of the SAME lane [...] verify it yourself rather than citing this message.

**Independently verified (S14):** `p = 2^61 − 1` is `3 mod 4`;
`v_2(p−1) = 1`, `v_2(p+1) = 61`; `v_2(q−1) = 62` so `2^41 | q−1`;
`p ≡ −1 mod 2^41` so `ord = 2 = e` — **generating**; `log2 q = 121 <
256`, `e = 2 <= 6`, `v_2(e) = 1 <= 2`, `log2 p = 61 >= 39` —
**admissible**; and `e_p := v_2(p−1) = 1` is outside `{>=41, 40, 39}` —
**outside the banked census. THEOREM G1 is FALSE as stated.**

**Item 4 verified independently as THEOREM D (§6.1) — and my verdict
differs from the coordinator's expectation.** The descent is real and
exact (89,252 checks, 0 bad), but it does **not** "answer R3 nearly
completely": it holds at *fixed* `Lambda`, and the non-generating row's
`t` is pinned by the *ambient* balance, so the descent reproduces
THEOREM Z-3's excess rather than removing it (COROLLARY D.1). What
actually answers R3 is (a) the consumer's own CATCH-#11 scope rule
(§6.3) and (b) the `k = 1` reduction to `f2_k1_contraction_theorem`
(§6.2(iii)).

**Effect on my deliverables.** THEOREM C1/C2/C3 and the descent use only
Lemma 1, the balance, `|Lambda| = ceil(t/2)`, and ADM-3
(`dim L <= k|Lambda|`) — **none uses ADM-1/2**, so the contract and the
finite target are branch-independent and cover all five classes. What is
**plus-branch only** is the *object* whose `Z_1` must be bounded (the
`[S, S−R, R+1]_p` GRS code) and therefore every instrument quoted
against it: THEOREM 7, Z-1's `2R+1`, Z-NOGO. **Named residual: on the
two minus-branch generating types the re-posed target `Z <= 1 + N^3`
stands, but the campaign has no object model to attack it with.**
