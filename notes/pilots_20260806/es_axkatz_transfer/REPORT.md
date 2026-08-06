(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

result: Ax-Katz/Chevalley-Warning transfer on (ES) is **DEAD** by four independent mechanisms — vacuous by 2^41 degree-units, logically mis-shaped (target is a p-adic unit), impossible for *every* exact encoding (Warning-2), and insensitive on the separating witness.

---

# REPORT — the Ax-Katz / Chevalley-Warning transfer on (ES)

Round 16, 2026-08-06. Pilot dir `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_axkatz_transfer/`.
Files: `PREREG.md` (coordinator brief + my appended registrations P0-P5, written before any computation), `PROOFS.md` (derivations), `verify_axkatz.py`, `verify_axkatz.out`.
**32 checks, 0 failures, exit 0**, under `tools/ramguard local`. Fail-closed verified by injecting a false check (exit 1).

## Headline

**TRANSFER DEAD.** Not by one mechanism but by four, three of which are method-level and unrepairable by sharpening the exponent. The one classical family the round-15 audit named as untested is closed, and closed *structurally* rather than numerically.

## (A1) The algebraization — two encodings, both verified exact

**ALG-I (indicator).** `N = n` variables; `n` quadrics `x_i^2 - x_i`; window forms (`w-1` over `F_q`, `|Z_w|` over `F_p`); weight form `Σx_i - r'`. So `Σd = 2n + w` (extension) / `2n + |Z_w| + 1` (base field).

**ALG-L (locator).** Variables = the `r'` non-leading coefficients of monic `E` (deg `r'`) plus the `n-r'` of monic `F` (deg `n-r'`); equations = the `n` bilinear coefficient identities of `E·F = X^n − 1`, plus the window forms on `E`. Since `X^n−1` is squarefree and split, a monic `E` extends iff `E | X^n−1`, and `F` is then unique — so the `F_q`-points biject with size-`r'` subsets of `μ_n` meeting the window. Verified against the banked round-15 syndrome DP at **20 fixtures, 0 mismatches**. For a *prefix* window the forced-zero coefficients are eliminated: `N = n − (w−1)`, `Σd = 2n`, **no linear equations** — the best reading available anywhere.

**CATCH-16A — ALG-I is not an exact algebraization when `p ≤ n`.** Its weight form pins `wt(x)` only mod `p`. `δ=1` forces `p > n`, but `δ ∈ {2,4}` admits `p ~ 2^40 < n = 2^41`. Explicit witness (`n=8, p=7, δ=2`, arithmetic in `F_49`): the weight profile is `[1,0,4,0,6,0,4,0,1]`, so at `r'=1` the true count is `0` while ALG-I has `1` point. ALG-L has no weight equation and is exact at every row. All row numbers are reported for both, with ALG-L load-bearing.

## (A2) The exponent, exactly

Formula stated before plugging in, and **validated by brute force** on 144 random systems, **all 144 with `mu ≥ 1`** — 0 Ax-Katz violations, 0 Warning-2 violations.

Closed forms: `ALG-I ext: mu = −⌊(n+nforms+1)/2⌋`; `ALG-L ext/pfx: mu = −⌊(n+nforms)/2⌋`. At the crossing rows the ALG-I exponent is exactly `−(n+w)/2`.

| row | mu (ALG-I ext) | mu (ALG-L pfx) | CW deficit | log2 |
|---|---|---|---|---|
| crossing w=2^34 | −1108101562368 | −1108101562367 | 2216203124736 | 41.011 |
| crossing w=2^39 | −1374389534720 | −1374389534719 | 2748779069440 | 41.322 |
| band 1/4 d=2^32+1 | −1103806595073 | −1103806595073 | 2207613190147 | 41.006 |
| band 1/16 d=2^31+1 | −1101659111425 | −1101659111425 | 2203318222851 | 41.003 |

**Every exponent negative, every row, every reading. Shortfall `2^41.003`–`2^41.322` degree-units** — worse than the banked Weil/C-U vacuity of "13.5-107 bits" at the same rows. Not a near miss: `Σd/N > 2` where Ax-Katz needs `< 1`. Chevalley-Warning never bites. Moreno-Moreno gives *identical* `mu` (every degree in play is 1 or 2, `< p`, so p-weight degree = degree — verified).

## (A3) THE DECISION — DEAD, four ways

**(ii) DEAD-VACUOUS** — above.

**(ii+) DEAD-BY-SHAPE. THEOREM AK-UNIT (unconditional).** At every crossing row the (ES) target `|W^struct| = C(L, r'/M)` has `L = n/M = 2^{41−v} ≤ 128`, and every prime factor of `C(a,b)` is `≤ a`. Since `p ≥ 2^39+1 ≫ 128`, **`p ∤ |W^struct|` for every admissible `p`, with no case split on δ.** Verified: largest prime factors `127, 61, 31, 13, 7, 2`.
**COROLLARY AK-ACCIDENT (unconditional):** any theorem proving `p | |W_w|` forces `|W^acc| ≡ −|W^struct| ≢ 0 (mod p)`, hence `|W^acc| > 0`. **p-divisibility here is an accident-EXISTENCE theorem — the negation of (ES).** A non-vacuous Ax-Katz would *refute* the target, never prove it. This cuts the entire family (Chevalley-Warning, Ax, Katz, Ax-Katz, Moreno-Moreno, Adolphson-Sperber, Wan, McEliece) in one stroke, *regardless of how sharp the exponent gets* — which is why it is the strongest of the four.

**(ii++) DEAD-FOR-ALL-ENCODINGS. THEOREM AK-WARN.** For *any* system whose `F_q`-point count equals `|W_w|` exactly: if `0 < |W_w| < q` then Warning-2 forces `N − Σd ≤ 0`, hence `mu ≤ 0`. Under (ES), `|W_w| ≤ C(128,63) = 2^124.1491 < 2^255.900 < q` and `> 0` by LEMMA Z. So **no exact algebraization whatsoever — not ALG-I, not ALG-L, not any system anyone will ever write down — can have a positive Ax-Katz exponent.** The measured vacuity is forced, not an artefact of encoding. *Fibered escape hatch, named and closed:* if `|V| = c·|W_w|`, then since `gcd(|W_w|,p)=1` we get `q^mu | c` — all divisibility sits in the fibre, information-free.

**(iii) DEAD-INSENSITIVE.** On the round-15 separating witness (`n=16, p=17, w=3`, defining sets `{a,a+1}`), replayed against the banked `verify_transfercut.py`:

| r' | {1,2} | {2,3} | {3,4} | {4,5} | {5,6} | {6,7} | {7,8} |
|---|---|---|---|---|---|---|---|
| 7 | 32 | 32 | 0 | 0 | 16 | 16 | 0 |
| 8 | 54 | 54 | 98 | 98 | 22 | 54 | 276 |

Counts **separate** `{0,16,22,32,54,98,276}`; `mu` is **constant** at `−9` in both readings; `|Z_w|` **constant** at 2; McEliece `ell−1` **constant** at 0. The Ax-Katz exponent is a function of `(n, #forms, degrees)` only and is constant on precisely the family that separates the terminal. Moreover **every nonzero count is coprime to `p=17`**. The `r'=8` row reproduces `[T4]` exactly; the `r'=7` row contains the audit's cited "32 vs 0".

**PROPOSITION McE-VAC.** McEliece is vacuous at every row *and every shifted defining set*: `0 ∉ Z_w` (since `0·p^j = 0` and `0 ∉ {1,…,w−1}`), so `ζ^0 = 1` is a **nonzero** of the code, `ell = 1`, exponent `p^0`. The one classical p-divisibility theorem that *is* defining-set-sensitive is sensitive through a quantity pinned at its trivial value here.

**Adversarial obligation discharged** (PREREG §3 cl.2): at `n=16,p=17,w=3,r'=8` (`|W_w|=54`, `|W^struct|=C(4,2)=6`, 48 accidents), the divisibility statement is satisfied *identically* by `|W^struct|`, by `|W^struct|+1`, and by the true count. It cannot separate periodic from periodic-plus-one-accident — which by the pre-registered rule alone forces (iii) over (i).

## (A4) Calibration

34 fixtures, exact counts from the banked machinery (itself re-verified against full cube brute force in 64 cells). The Ax-Katz prediction is **never violated and never informative**: `mu ≤ 0` everywhere, and `q^0 | N` holds for every integer — true and empty. `p | |W_w|` in 11/34 fixtures, but **all 11 are the trivial `|W_w| = 0`**; among the 23 nonzero counts, `p` divides **0**. Honest scope split: the toys sit far below balance (`C(16,8)/p^2 = 44.5`), so they kill the *row-level* claim only; the *method* is killed by AK-UNIT/AK-WARN, which are proofs.

**Regime cross-check against banked results:** my `log2 C(128,63) = 124.1491` matches `verify_rows.py [B3]`'s `2^124.15`, and my δ=1 balance crossover `w* = 2^33.0` matches its `[B1/B2]` row `255.9 → 33.0005`. The whole crossing bracket is sub-balance at the razor row, consistent with the adopted (ES) phrasing.

## (P3) The one LIVE shape — tested, and the seam worth keeping

`q^mu | |W|` with `mu ≥ 1` **plus** `|W| < q^mu` gives `|W| = 0`. This is the only shape in which p-divisibility can *prove* suppression, and it is the relevant one at the band rows because **`[K3a]` shows all three band structural families are EMPTY** (`M = 2^33, 2^33, 2^32` never divides `r' = (n−k) − d` on the given `d` ranges) — the band target is a genuine vanishing statement, to which AK-UNIT/AK-WARN do not apply. Both ingredients fail: `mu` short by `~2^41`; and the only unconditional bound `U = C(n,r')` has `log2 U ~ 2.2e12`, needing `mu ~ 8.6e9` against `mu ~ −1.1e12`.

**CATCH-16B (bank this).** With **only** `mu ≥ 1` plus the band's own budget `0.68 n² = 2^81.442` as an a priori bound, the route *would* close, since `2^81.442 < q^1`. The entire gap is in ingredient 1. **The band rows are the only place in the whole terminal where a p-divisibility theorem could ever have been decisive, and there it needs only `mu ≥ 1`.**

## (A5) What a decisive method must see

Exclusions are now four deep: not the weight enumerator (round-15 cut); not designed distance or `|Z_w|` (constant across the separating family — also cuts BCH/HT/Roos, van Lint-Wilson); **not any congruence method** (AK-UNIT: the target is a p-adic unit, so the conclusion has the wrong shape however sharp the exponent); not archimedean-lossy (Weil vacuous, L2 loses `2^128`, required suppression is from `~2.2e12` bits down to `~2^124`).

The surviving invariant is the defining set *as a subset of `Z/n`*, at resolution no coarser than its **divisor profile** `D(Z) = {n/gcd(n,s) : s ∈ Z}` — exactly what LEMMA Z turns on, and exactly what the shift `{1,…,w−1} → {a,…,a+w−2}` changes while leaving every classical invariant fixed. The precise open problem:

> **a characteristic-`p` analogue of vanishing-sums-of-roots-of-unity rigidity (Lam-Leung / Conway-Jones): control 0/1 vectors of prescribed weight in the `F_p`-reduction of a cyclotomically rigid char-0 system, in the sub-balance regime `C(n,r') < p^{|Z_w|}`.**

That is a rigidity/equidistribution question (Deligne-Katz over the window parameter), not a divisibility question — the audience round-15 already identified. **This pilot narrows the Pro brief: ask for rigidity, and state up front that p-divisibility is excluded by AK-UNIT**, so correspondents don't spend the first exchange proposing Chevalley-Warning.

## Honest residuals

- **AK-WARN is conditional on (ES)** at the crossing rows (it uses `|W_w| < q`); unconditionally we know only `|W_w| ≥ |W^struct| > 0`. **AK-UNIT and AK-ACCIDENT are unconditional.**
- **Band rows are not covered by AK-UNIT/AK-WARN** (structural count 0 is divisible by everything); they are closed by vacuity and the ingredient-2 gap only. CATCH-16B is the one live seam — keep it on the board.
- `|Z_w|` is not pinned at the prize rows; bracketed by `[w−1, δ(w−1)]`, both ends vacuous, nothing turns on it.
- The `prod T = γ` clause of MC-1 (dropped in the round-15 object of record) is not folded in; in ALG-L it is one more degree-1 form, shifting `mu` by at most 1 — cannot change any verdict. Reported separately per P5c.
- `log2 C(n,r')` at `n = 2^41` via `lgamma`; error `≪ 1` bit on a `2.2e12`-bit quantity.
- **Adolphson-Sperber / Wan exponents are not computed numerically** — excluded by conclusion-shape (AK-UNIT), not by arithmetic. Stated as such rather than claimed as measured.
