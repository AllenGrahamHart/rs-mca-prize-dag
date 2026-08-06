# PRE-REGISTRATION — F2-ADM: re-derive mystery 2 on a prize-admissible row

Round 17, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is the named successor
task from round-16's f2_tq_pin (its honest residual 5: "I did not
re-derive the F2 tower on an admissible row... this is the natural
successor task").

## 0. The scope correction being executed (sources of record)

Round-16 f2_tq_pin CATCH-1 (banked, maintainer-level): the 16-rung
KoalaBear tower is NOT prize-admissible — the field cap |F| < 2^256 is
broken from rung 4; the complete admissible region at the maximal
rate-1/2 row (n = 2^41) is

> `v_2(e) <= 2`, `e <= 6`, `log2 p >= 39`, tower depth <= 2 rungs

with the explicit admissible prize-max witness
`p = 18446735827372343297` (v_2(p-1) = 39), `q = p^4`,
`log2 q = 255.99997`, `v_2(q-1) = 41`, `ord_{2^41}(p) = 4`.
Also banked: t pinned to the interval `(2^33, 5.364e10]` (t = n/L);
the F2 discharge headline WITHDRAWN to rungs 1-10 (1-9 stricter) ON
THE TOWER-AS-WRITTEN; round-16 f2_sl1b CATCH-B: f2_opening's stated
setting (n | p^2-1) is rung-1-only even on that tower.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260806/f2_tq_pin/REPORT.md` + `PROOFS.md` — the
  admissible region derivation, the explicit row, the t interval,
  CATCH-2 (the L = 255.9 vs 255.911275 seam), CATCH-3 (stricter
  window), the |K1|/PP5.0 pricing.
- `notes/pilots_20260804/f2_opening/PROOFS.md` — the (O1) obligation,
  LEMMA 3, the rung ladder and window mechanism, THEOREM A/B.
- `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md` — SL-1
  (characteristic-free), the Z(L) terminal (SL-1b').
- `notes/pilots_20260806/f2_sl1b/PROOFS.md` — LEMMA SL-1b-DIM
  (k-free), the (R-A)/(R-B) split, the 61-witness refutation.
- `notes/pilots_20260806/f2_tq_pin/REPORT.md` HONEST RESIDUALS —
  the t-naming collision is the SIBLING pilot's (t_naming); flag
  interactions, do not resolve.

## 2. Pre-registered deliverables

- **(D1) The admissible F2 object.** On an admissible row (use the
  explicit witness as the concrete instance, and state which parts
  hold for ALL admissible rows vs the instance), reconstruct the F2
  mechanism: what replaces the 16-rung tower when at most 2 rungs
  exist (ord_{2^41}(p) <= 4)? State the new rung/window ladder
  (m_j, n_j, q_j) exactly, under BOTH the new-part and nested window
  readings (the stricter governs headline margins per CATCH-3).
- **(D2) Theorem survival table.** For each banked F2-lane theorem —
  THEOREM A/B, LEMMA 3, SL-1, LEMMA SL-1b-DIM, the Z(L) reduction,
  the antipodal-fibre/parity results f2_opening relies on — state:
  survives VERBATIM (k-free / characteristic-free), survives WITH
  RESTATED CONSTANTS (give them), or NEEDS RE-DERIVATION (name the
  gap). No theorem may be carried over silently.
- **(D3) The margins on the admissible row.** Recompute the LEMMA 3
  necessary condition and the discharge margins at every rung of the
  ADMISSIBLE ladder, over the full pinned t-interval (2^33,
  5.364e10], both window readings, worst case first. State plainly:
  what is (O1)'s discharge status on admissible rows?
- **(D4) The re-based obligation list.** Mystery 2's obligations
  restated for the admissible object: does SL-1b' (the Z(L) bound)
  survive as THE terminal, and at which (m, p) does it now sit? Does
  the 2-rung structure make anything EASIER (e.g. fewer rungs = fewer
  obligations) or HARDER (e.g. the descent argument needed 16 steps)?
  This is the deliverable the board update will be written from.
- **(D5) The PP5.0 seam on the admissible row.** Recompute the
  |K1| pricing (avg-vs-sum = 2^{n/2} was proved via (t*/2)L = n/2 —
  does the identity survive when t is an interval and L is the
  admissible row's?). Do not choose the reading (user decision,
  pending); price both.

## 3. Pre-registered falsifiers / honesty clauses

- If the F2 mechanism CANNOT be reconstructed on a <= 2-rung tower
  (i.e. the descent genuinely needed the inadmissible depth), that is
  the finding: mystery 2's F2 lane would be VACUOUS as posed (its
  object excluded by the rules) — state what the lane's question
  becomes, do not force a reconstruction.
- If any banked theorem's survival is ambiguous, it goes in NEEDS
  RE-DERIVATION, never in survives-verbatim.
- All margins worst-case over the t-interval; no point-value t.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/f2_adm/`.
  Never touch dag.json, node shards, tools/, or push. Do NOT read
  `notes/pilots_20260806/t_naming/` (sibling this round).
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.

---

# PILOT APPENDIX — Opus 5's own pre-registrations (appended before ANY computation)

Round 17, 2026-08-06. Everything below was derived on paper from the five
source surfaces listed in §1, with no tool computation of any kind
performed yet (the first `ramguard` invocation of this pilot comes after
this block is written). Each item states a prediction and the observation
that would falsify it. Notation: `n = 2^41` (maximal rate-1/2 row),
`q = p^e`, `L = log2 q`, `e_p := v_2(p-1)`, `k := ord_n(p) = [F_p(mu_n):F_p]`,
`D := 41 - e_p` (clipped at 0) `= log2 k` = the number of MOVING rungs,
`R := |Lambda| = ceil(t/2)` under the banked `Lambda = {odd l <= t}` reading,
`t = n/L` the banked counting balance (`f2_tq_pin/PROOFS.md:194-196`).

**A1 (falsifier check — the headline).** I predict the pre-registered
falsifier does **NOT** fire: the F2 mechanism reconstructs on <= 2 rungs,
because LEMMAS 1-5 / THEOREMS A-C are per-window statements
(`f2_opening/PROOFS.md:335`: *"which cannot affect Lemmas 1-5, which are
window-agnostic"*) and the tower supplies only (i) a partition of `mu_n`
by element order and (ii) a per-rung quadratic Galois step; neither needs
depth 16. *Falsifier:* any load-bearing F2 statement whose proof consumes
the tower depth (rather than one rung's quadratic step) — if found, the
lane is VACUOUS as posed and I report that instead.

**A2 (the admissible ladder).** At the banked witness
(`p = 18446735827372343297`, `e_p = 39`, `q = p^4`) I predict the ladder is
exactly: fixed sector `n_0 = 2^39, q_0 = p, k_0 = 1, m_0 = 2^38`;
rung 1 `n_1 = 2^40, q_1 = p^2, k_1 = 2, m_1 = 2^38`;
rung 2 `n_2 = 2^41, q_2 = p^4, k_2 = 4, m_2 = 2^39` (new-part reading),
`m_j = n_j/2` under nested. The fixed sector is **25%** of the domain
(vs `2^-16` of it on the KoalaBear tower). *Falsifier:* any other
`(n_j, q_j, k_j, m_j)`.

**A3 (depth-budget trade-off).** `D` moving rungs forces
`L >= 2^D (41 - D)`, hence `t = n/L <= 2^41 / (2^D (41-D))`:
`D=0: t <= 5.364e10`, `D=1: t <= 2.749e10`, `D=2: t <= 1.410e10`,
`D=3: L >= 304 > 256` INADMISSIBLE. Depth and condition budget are in
strict competition; the top of the pinned `t`-interval is reachable only
at `D = 0` (no moving rungs at all). *Falsifier:* an admissible row with
`D >= 3`, or one with `D >= 1` and `t` above its stated cap.

**A4 (no admissible discharge).** THEOREM A / LEMMA 2 discharges a layer
of order `2^a` iff `R >= m(a)`, i.e. `a <= 42 - log2 L`. I predict: on
EVERY admissible row, **no moving rung is discharged** (each misses by a
factor `>= 39x`; `64x` and `128x` at the witness), the discharged set lies
strictly inside the fixed sector, and the discharged fraction of the
domain is exactly `2t/n = 2/L <= 2/41 = 4.88%` (`0.78%` at prize-max).
*Falsifier:* an admissible row + moving rung with `2m - 1 <= t`.

**A5 (the decomposition theorem — replaces the descent).** Because
`y^{2^D}` has order `2^{e_p}` and therefore lies in `F_p^*`, the
antipodal-pair representatives of a layer fall into `F_p`-proportionality
classes indexed by residues mod `2^D`. I predict the top-layer kernel
splits **exactly**:
`L^perp = (+)_{c=1..C} ker(A_class)`, `C = max(1, 2^{D-1})` (new-part) /
`2^D` (nested), each class being the SAME problem over the prime field on
a half-system of `mu_{2^{e_p}}` of size `S = m/C`; hence
**`dim_{F_p} L = C * min(S, R)` EXACTLY** (sl1b's bracket
`[min(m,R), min(m,k*ceil(t/2))]` collapses to a point), each summand is a
**GRS/MDS code `[S, S-R, R+1]_p`**, and `Z(L) = Z_class^C`.
*Falsifier:* a brute-forceable row where `dim L != C*min(S,R)`, or where
the class reps fail to be `F_p`-independent, or `Z(L) != Z_1^C`.

**A6 (trace-tower collapse; `k`, not `e`, is the constant).**
`L^perp = ker_{F_p}(A)` with `A = (y_i^l)` entried in `F_p(mu_n) = F_{p^k}`,
so `dim L <= min(m, k|Lambda|)` with **`k = ord_n(p)`**, unconditionally,
even when the coefficients `C_l` range over the larger `F_q`. I predict
sl1b's `k = [F_q:F_p]` must be RESTATED as `ord_n(p)`, that the two differ
on admissible rows with `e > k`, and that no reading ambiguity survives.
*Falsifier:* a row where `dim L > k|Lambda|` with `k = ord_n(p)`.

**A7 (LEMMA 3 on admissible rows — exact, `t`-free).** Combining A5+A6 with
`t = n/L`: the LEMMA 3 ratio `dim L * log2 p / m` at the top window is
**`max(2,k)/e` (new-part)** and **`k/e` (nested)** — independent of `p`,
`t` and `n`. Consequences predicted: (i) at the witness (`k = e = 4`) both
readings give **exactly 1.000** — zero margin — at every point of the
pinned `t`-interval; (ii) under the stricter (nested) reading mandated by
`rules_freeze/statement.md:9`, the ratio is `k/e <= 1` on EVERY admissible
row, `= 1` iff `k = e`; (iii) where the ratio is `< 1` by a constant,
LEMMA 3 — a PROVED necessary condition for (O1) — **fails**, so (O1) is
FALSE at that window by `2^{m(1-ratio)}`. *Falsifier:* any admissible
`(k,e)` where the computed ratio differs from the formula.

**A8 (SL-1 / SL-1b re-based).** SL-1 survives verbatim (characteristic-
and `k`-free); its designed distance as a fraction of the window is
`(R+1)/m ~ 2/L` (new-part) — `1/128` at prize-max vs the banked `0.01563`
at tower rung 16. SL-1b (R-A) at the top window has ratio
`2/(e log2 3) = 1.2619/e` from below; I predict it is PROVED only at
`e = 1` and REFUTED wherever the (A6-corrected) upper bound is below the
threshold. SL-1b' survives as THE terminal, re-based onto an explicit
prime-field GRS code. *Falsifier:* any of these verdicts changing under
exact recomputation.

**A9 (the |K1| seam).** `log2|K1| = |Lambda| * L = (t/2) L = n/2` EXACTLY
on **every** admissible row (structural, from `t L = n`), independent of
`p, e, t`; base reading `n/(2e)`; and a THIRD reading forced by A6 — the
effective sector `F_{p^k}^Lambda`, `log2 = k n/(2e)`. I further predict
the seam and LEMMA 3 are **the same inequality**: (O1) at the full-group
window requires `log2|K1|_eff >= n/2`, with equality iff `k = e`. All
three readings are `Theta(n)`, so the sibling's verdict (never `o(n)`,
never absorbable) survives. I price, I do not choose.
*Falsifier:* `log2|K1| != n/2` under the extension reading on some
admissible row.

**A10 (antipodal law + the coset).** `tower.py:26-33`'s law
(`y^{q_{j-1}} = -y` for `y` of order exactly `n_j`) survives VERBATIM at
both admissible rungs with `e = 39` in place of 24. But the rules-level
domain is a **coset** `g mu_n` (`rules_freeze/statement.md:9`), and
`(gy)^{q_{j-1}} = -(gy)` iff `g in F_{q_{j-1}}`. I predict: the K1 mass
machinery (LEMMAS 1-3, THEOREMS A/B, SL-1) is coset-invariant (power-sum
conditions only pick up `g^l != 0`), while the antipodal-DESCENT identity
is not. *Falsifier:* the mass machinery failing on a coset, or the
descent identity surviving a coset rep outside the subfield.

**A11 (tower self-consistency, control).** Using the tower's OWN field,
`L = log2 q_16 = 2,030,874`, the same balance gives `t = n/L ~ 1.1e6`,
i.e. the banked `7e10` is ~`6e4x` too large **by the tower's own
arithmetic**, and then NO tower rung is discharged (rung 1 already needs
`t >= 2^24`). *Falsifier:* the arithmetic not reproducing.

**A12 (protocol / honesty).** All margins reported worst-case over the
pinned interval `t in (2^33, 5.364e10]` AND at the row-consistent
`t = n/L`; ratios equal to 1 within the precision of the leading-order
balance (F) are reported as **SATURATED / zero margin**, never as
"holds with margin"; any theorem whose survival is ambiguous goes to
NEEDS RE-DERIVATION; I will not resolve the `t`-naming collision (sibling
`t_naming` owns it) and will not read that pilot's directory.
