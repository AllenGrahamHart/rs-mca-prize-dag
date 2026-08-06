# PRE-REGISTRATION — SL-1: low-weight ternary vanishing odd-power-sum relations

Round 15, 2026-08-06. **Written BEFORE any computation.**
Pilot: `notes/pilots_20260804/f2_sl1_powersums/`.
Parent: `notes/pilots_20260804/f2_opening/` (PROOFS.md, verify.py, FABLE_AUDIT.md).

## 0. The statement under attack (verbatim from the task / the adopted audit)

> **SL-1**: at official rungs 14-16, the deployed window admits no
> low-weight ternary vanishing odd-power-sum relation — no
> `epsilon in {-1,0,1}^m`, `epsilon != 0`, weight `w = o(m)`, with
> `Sum_i epsilon_i y_i^l = 0` for every odd `l <= t`.
> Pre-registered prediction from round 14: none exists for `w < t/2`.

Audit line adopting it (`f2_opening/FABLE_AUDIT.md:28-31`, verbatim):

> Remaining for a complete (O1):
> SL-1 (rungs 14-16 — no low-weight ternary vanishing odd-power-sum
> relation; prediction w >= t/2) and SL-2/CATCH-3 (the average-vs-sum
> |K1| normalisation seam — settle WITH the PP5.0 freeze).

Pilot scope line it comes from (`f2_opening/PROOFS.md`, "Scope", verbatim):

> - Theorem A/B require `Lambda ⊇ {1,3,...,2m-1}`. At the official row
>   (`m_j = 2^{22+j}`, `t ~ 7e10`) that is **rungs 1..13**. Rungs 14-16 are
>   **NOT** discharged; there `L^perp != 0` is possible (at rungs 15-16 it
>   is forced, since `dim L <= t < m`) and (O1) reduces to bounding
>   `Z(L)` — the vanishing-power-sum problem of Lemma 1.

## 1. Notation (fixed here, matching `f2_opening/PROOFS.md`)

`W <= mu_n` antipodally closed, `m = |W|/2`, `y_1..y_m` one representative
per antipodal pair, `y_i` in `F_q^*` with `n | q-1`, `q` odd, `n` even.
Deployed rung-`j` window: `n_j = 2^{24+j}`, `W = {x : ord(x) = n_j}`,
`m_j = 2^{22+j} = n_j/4`, `y_i = zeta^{2i+1}`, `i = 0..m-1`.

`Lambda` = the condition set = **odd** exponents. Two readings of `t`
(both are live in the repo; see §5) — I pre-register the theorem in a
`t`-free form and instantiate afterwards:

```text
R := the number of exponents in a run of CONSECUTIVE odd exponents
     contained in Lambda:   {2a+1, 2a+3, ..., 2a+2R-1} ⊆ Lambda.
"odd l <= t" reading (a = 0):   R = ceil(t/2).
```

`L` = image of the evaluation map, `L^perp = {eps in F_p^m : sum_i eps_i y_i^l = 0
for all l in Lambda}`, `T := {-1,0,1}^m`,
`Z(L) = sum_{eps in L^perp ∩ T} 2^{-wt(eps)}`, `E_c[T_W] = 2^m Z(L)` (LEMMA 1).

## 2. Pre-registered claims

- **(SL-1-THM) the designed-distance law.** If `Lambda` contains `R`
  consecutive odd exponents, then every `eps in L^perp` (in particular
  every ternary one), `eps != 0`, has

  ```text
        wt(eps)  >=  R + 1.
  ```

  Reason to be checked: `(y_i^{2a+2r+1})_{r=0..R-1, i}` factors as
  `diag(y_i^{2a+1}) * Vandermonde(y_i^2)`, and the `y_i^2` are pairwise
  distinct because `y -> y^2` has antipodal fibres — so ANY `R` columns
  are independent. This is `f2_opening` LEMMA 2's own matrix, applied to
  `w x w` MINORS instead of the full `m x m` matrix.
  **Falsifier F2:** any ternary `eps != 0` with `wt(eps) <= R`.

- **(SL-1) as posed.** With `R = ceil(t/2)`: `wt(eps) >= ceil(t/2) + 1 > t/2`,
  and `R+1` is a CONSTANT FRACTION of `m` at rungs 14-16, so no relation of
  weight `o(m)` exists. **Falsifier F1 (the task's):** a ternary relation
  of weight `< t/2`.

- **(GEN) strict generalisation of THEOREM A.** `R >= m` forces
  `L^perp = 0` (a nonzero vector would need weight `>= m+1 > m`), which is
  exactly LEMMA 2 / THEOREM A. So one law covers rungs 1-13 and 14-16.
  **Falsifier F5:** a nonzero ternary dual vector at `R >= m`.

- **(CONSEC) the consecutive hypothesis is necessary, not cosmetic.**
  For a GAPPED set of `R` odd exponents the bound must be allowed to fail.
  **Falsifier F6 — I PREDICT THIS FIRES:** a gapped `Lambda` of size `R`
  with a ternary relation of weight `<= R`.

- **(MASS) two new rigorous mass bounds at partial condition sets.**
  Projection onto any `m-R` coordinates is injective on `L^perp` (min
  distance `>= R+1`), and distinct ternary codewords are at Hamming
  distance `>= R+1`. Hence

  ```text
   (M1)   Z(L)  <=  2^{m-R}                       [so E_c[T_W] <= 2^{2m-R}]
   (M2)   Z(L)  <=  1 + 3^{m-R} * 2^{-(R+1)}
   (M3)   Z(L)  <  2   whenever  1.585*(m-R) - R - 1 < 0, i.e. R > 0.6132 m.
  ```

  (M3) is a NEW discharge criterion `t >= 1.2264 m` against LEMMA 2's
  `t >= 2m-1` — a 1.63x weaker condition requirement.
  **Falsifier F7:** any shape with `Z(L)` exceeding (M1) or (M2).

- **(NOSTRUCT) every ternary dual vector is "accidental".** `n` a 2-power
  and the representatives lying in a half-period force
  `alpha = sum_i eps_i zeta_n^{a_i} != 0` in `Z[zeta_n]` (Lam-Leung: for
  `n = 2^k` every vanishing sum of `n`-th roots of unity is a union of
  antipodal pairs, and no two representatives are antipodal). Hence a
  relation exists only by `p`-divisibility of a nonzero algebraic integer,
  and the norm bound `w >= p^{2R/n}` holds.
  **Falsifier F8:** a nonzero ternary relation valid in char 0 with
  `1 in Lambda`.

- **(TRUE LAW) the existence boundary is a COUNT threshold, not the
  distance threshold.** I predict the observed boundary for "a nonzero
  ternary dual vector exists at all" tracks

  ```text
        m * log2(3)   vs   dim_{F_p}(L) * log2(p)      (entropy vs conditions)
  ```

  and NOT `R+1 <= m`. Concretely: `(SL-1-THM)` will be a strict, far-from-
  tight lower bound whenever `p` is large relative to `m`; the true min
  weight will be `+infinity` (no vector) in that regime.
  **Falsifier F3 (tightness):** true min ternary weight `== R+1` exactly.
  Predicted to fire only in the small-`p` regime.

- **(REPLAY) LEMMA 1.** `E_c[T_W] = 2^m Z(L)` exactly, in `Z[zeta_p]`.
  **Falsifier F4:** any mismatch.

## 3. Pre-registered cross-lane verdict (route 1, to be adjudicated)

The crossing pilot's LEMMA Y (`crossing_w2_opening/PREREG.md`, verbatim):

> ```text
> W_w = {weight-r' 0/1 vectors in the cyclic code of length n over F_p
>        with defining zeros zeta, zeta^2, ..., zeta^{w-1}}
> ```
> i.e. a CONSTANT-WEIGHT COUNT IN A BCH CODE of designed distance `w`.

**Pre-registered prediction:** BOTH lanes' objects are codewords of a
cyclic code with a CONSECUTIVE defining set — the identification is REAL
at the level of the object class and the machinery imports (crossing ->
F2). But I predict the "sixth reduction" claim **FAILS** on three counts:
alphabet (ternary vs 0/1), weight regime (min-distance end vs
constant-weight-`r'` end), and question type (minimum distance vs
enumeration). Verdict to be recorded either way.
**Falsifier F9:** either object turning out not to be a cyclic code with a
consecutive defining set.

## 4. Measurement plan (all `tools/ramguard tiny -- python3`, exact arithmetic)

1. `F_q` arithmetic from scratch (`q = p` and `q = p^2`), `mu_n`, antipodal
   pairs, `y_i^2` distinct.
2. Meet-in-the-middle enumeration of the FULL set `L^perp ∩ {-1,0,1}^m`
   (split the `m` coordinates in half, hash `F_q^R` partial sums) — gives
   the complete ternary weight enumerator, exactly, for `m <= 16`.
3. Sweep `(n, p, q, R, a)` incl. gapped `Lambda`, general antipodally
   closed windows, and the `q = p^2` (zeta not in `F_p`) case.
4. Exact `E_c[T_W]` in `Z[zeta_p]` by averaging over `L`, vs `2^m Z(L)`.
5. Char-0 structural check in `Z[X]/(X^n-1)` for (NOSTRUCT).
6. Official-row arithmetic under EVERY live value of `t` (CATCH-4).

## 5. CATCH-4 — `t` is pinned FIRST, and it is pinned as UNDETERMINED

Recorded before computing, from the provenance sweep:

- `t` has **no definition** in the repo. It is a bare literal
  `t = 7e10` at `f2_opening/verify.py:958` and `:1038`.
- Provenance: the banked product `t*log2(q) ~ 2.15e12`
  (`archive/compressed_dli_lane_20260705/b2_modp_giant_extras/statement.md:9`,
  via `notes/floor_campaign/SURVEY_X4_CLUSTER.md:15-17`,
  `notes/f2_campaign/F2_CAMPAIGN_LOG.md:184-187`) divided by `log2 p ~ 31`.
- The competing generated-field reading is exact and formula-backed:
  `t* = 8,592,912,739` at rate 1/2 (`background/nodes/xr_radius_arithmetic/proof.md:41-58`).
- The conflict is already booked: `notes/kernel_basis/TARGET_3C_EXTRACTION.md:26-32`
  ("THE OFFICIAL FACTORIZATION q = p^k IS PINNED NOWHERE").
- Second, internal, competing value: `f2_opening/PREREG.json:58` uses
  `m_16 = 2^39` where `PROOFS.md:233` uses `m_16 = 2^38`.

**Pre-registered consequence to be checked numerically:** LEMMA 3's
necessary condition `t >= m_j / log2 p` is SATISFIED with margin 7.89x
under `t = 7e10` and **VIOLATED** under `t* = 8.59e9` at rung 16. I predict
the violation ratio is `0.969x` (i.e. a sign flip, not a shrinkage).
I further predict **(SL-1-THM) survives every reading of `t`**, since
`R+1 = Omega(m)` under all of them.
