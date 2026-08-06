(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Sanity check complete: clean single-invocation re-run of the full verifier exits 0 with **111 PASS, 0 FAIL**; all 8 files I wrote are inside `notes/pilots_20260806/tail_count/`; nothing outside the pilot directory was modified in this session; no `__pycache__` leaked into my dir or any banked dir; registrations were appended to PREREG.md before any computation; no REPORT.md written; I did not open `f2_repose/` or the CAMPAIGN_LEDGER.

---

# THE TAIL-COUNT CRITERION — PILOT REPORT (round 20, GENERATIVE)

**Files** (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tail_count/`): `PREREG.md` (coordinator brief + my appended registrations P1–P8, grid, honesty clauses — written before any computation), `PROOFS.md` (derivations), `VERIFY_LOG.txt` (111 PASS, 0 FAIL, exit 0), `verify_tail.py`, `tc_lib.py`, `t2_lib.py`, `t2_stage.py`, `stages2.py`.

**Licensing controls (a failure would have voided the pilot):** the character form reproduces an exact ternary census by disjoint code paths at G1–G4 (rel `&lt; 5e-12`), including the banked `Z_1 = 1.25` (G1) and `9.387207` (G4) of `tern_route_b/PROOFS.md:124-127`; my own from-scratch `F_{p^k}` construction and `3^16` meet-in-the-middle census reproduce the banked I3 row `6560 / 0 / 16640 / 148224` (`tern_small_scale_laws/PROOFS.md:114`) and the `288` / `{7,14}` cell.

## VERDICT (T4) — **STRUCTURE THEOREM + ONE PROVED LAYER + A NAMED OBSTRUCTION; LEAD 1(a) IS A MIRAGE, LEAD 2 IS FULLY EXPLAINED AND DOES NOT TRANSPORT**

Four outcomes, in the brief's own vocabulary:

1. **A proved tail bound, for a stated `c`-range** — `U_c = {0}`, i.e. `|U_c| = 1`, for every `c &gt; 1 − 2^{−124.191}`. Honest size: the range has **width `2^{−124.19}`**. It proves the ledger's `c = 1` layer in the strongest possible form and nothing else. **Endpoint, not progress into the bulk.**
2. **A structure theorem (route-shaped)** — the tail is *exactly* a small-values/box count: `U_c = {u : Σ_s d(f_u(ζ^s)) ≤ (1−c)S}` with `d(c) = −2log₂|cos(πc/p)|`, i.e. lattice points of the Construction-A lattice over the GRS value code `C*` in a box. The requested conversion "tail count → parametrized family count" is delivered; the family is *codewords in a box*, and the criterion is exactly "`C*` is not unusually smooth".
3. **A named obstruction (structural deficit, not a no-go)** — every input the object supplies is **`R`-local**, and `R`-local information can certify tail probabilities only down to `2^{−O(R log₂(e log₂ p))} = 2^{−0.116 S}`, against a required `2^{−0.443 S}`. **The gap is exactly the factor `log₂ p / log₂(e log₂ p) = 8.60`** — the same shape that makes Corollary 8's threshold `log₂ p ≤ O(log log p)`. The classical non-local escape (Poisson summation on the lattice) is **circular**: it returns `Z_1` itself.
4. **The measured tail law, banked** — with a new exact target for the whole campaign: **the binding layer is `c* = 1/ln 2 − 1 = 0.4426950409…`**, and it is measured at `0.45` on every toy row with enough resolution.

## T1(a) — the doubling/log-sine lead: **MIRAGE (CATCH-T1)**

**THEOREM 2.** Summing Proposition 10 by parts over the doubling map `c ↦ 2c` gives, for every `c ≠ 0`, `L(2c) − L(c) = log₂|2cos(πc/p)| = 1 − d(c)/2`, and Prop 10 collapses to

```
    log2 P(u)  =  S  -  sum_{s&lt;S} d(c_s(u)),      d(c) = -2 log2|cos(pi c/p)|
```

which is `log(1+cos t) = log 2 + 2 log|cos(t/2)|` applied `S` times. Machine-verified over **every** tuple at G1–G4 (max error `7e-13`), plus the per-value identity (`3.1e-14`) and `Π_{c≠0}|cos(πc/p)| = 2^{−(p−1)}`.

&gt; **CATCH-T1 (against the node statement).** `statement.md:68-69` records "the doubling/log-sine exact identity (Prop 10 — Dedekind-sum-shaped, no bound known)" as route (b)'s surviving lead. **The `(1−ω^{2c})/(1−ω^c)` rewriting creates the log-sine weights and the doubling shift; summing by parts destroys both.** There is no Dedekind sum here to bound, no orbit structure of `2` on `F_p^*` to exploit, and no place for the Dedekind-sum literature to act. Prop 10 remains true and remains finer than `V_1` — but its fineness is that of the value multiset `{n_c}`, not of the doubling map.

The collapse is a *gain*: the cost form is a sum of local costs, which is what makes everything below possible.

## T1(b) — the value-multiset second moment: exact, trap-free, and reach measured

**THEOREM 5 / COROLLARY 6 (exact).** `C*` is MDS, so the value vector is exactly **`R`-wise independent uniform**, and

```
    E_u[log2 P] = -S(1 - 2/p),   Var_u[log2 P] = S Var(d) (R&gt;=2),
    E_u[ sum_c n_c(u)^2 ] = S + S(S-1)/p          -- all EXACT, verified exactly
```

&gt; **Corollary-8 family-trap self-check, with the "HOW" the brief demanded.** These consume **no distance theorem and no count**. The only input is that `u ↦ f_u(x) − f_u(y)` is a nonzero functional for `x ≠ y` in `Y` — its `r=0` coefficient is `x − y ≠ 0`. That is a Vandermonde degree fact, **not** a low-`ℓ1` relation count and **not** THEOREM Z-2. Threshold: vacuous, the statements hold for every `p`. This is the evasion; it is also where the evasion stops.

**THEOREM 11 (the trap re-entered, quantified per layer).** Running the Z-2/Chebyshev supply layer by layer instead of in aggregate: at `log₂ p = 64` the certified set of layers is **EMPTY** (`max_c` deficit `−5.0e−5`, attained only in the trivial `c → 0` limit); bisecting in `p`, it becomes nonempty exactly at `log₂ p ≤ 3.0529`, i.e. `p ≤ 8.299`, and then only at `c = 1`. **COROLLARY 8's threshold recovered layer by layer.** Flagged DEAD FAMILY.

## T1(c) — the structure theorem, and both supplies for it

**THEOREM 9.** `U_c = {u : cost(u) ≤ (1−c)S}`; for every `δ`, at least `(1−δ)S` coordinates of the codeword lie in the interval `A(D) = {c : d(c) ≤ D}`, `D = (1−c)/δ`, of relative length `ρ(D) = (2/π)arccos(2^{−D/2})`.

**THEOREM 10 (interpolation supply) — dies at EVERY `p`.** `|U_c| ≤ C(S,R)·m^R` needs `H(1/L) + (1/L)log₂(m/p) ≤ −c`; as `c → 0` this is `H(1/L) − 1/L ≤ −c &lt; 0`, false for every `L &gt; 2`. Checked over `log₂ p ∈ {2,…,2^20}`: best `c` gives `−0.708 … −0.0005`, **negative everywhere, no threshold in `p`** — strictly worse than Corollary 8. **The failure mechanism is the entropy of the position set**: `S·H(R/S) = 0.1161 S` bits to say *which* `R` coordinates are small, against only `R log₂(1/ρ) = 0.0156 S` bits recovered from the values. The ratio worsens like `log₂ log₂ p`. Flagged DEAD FAMILY.

**THEOREM 12 (the one proved layer).** If `1 − c &lt; d(1)(1 − R/S)` then `U_c = {0}`. At the official row (`Decimal`, 60 digits) `d(1) = 2^{−124.168}`, `1 − R/S = 0.984127`, so `U_c = {0}` for `c &gt; 1 − 2^{−124.191}`. No union bound is needed here — which is exactly why Theorem 10's entropy term is absent.

## NEW, and the sharpest thing this pilot produces: **the criterion has zero margin, and its binding layer is `c* = 1/ln 2 − 1`**

- **THEOREM 3 (normalised ledger).** The criterion is *equivalent* to `Pr_u[P(u) ≥ 2^{cS}] ≤ 2^{−cS+o(S)}`. **The ledger's `+46.02` is exactly the saturation constant `Δ = R log₂ p − S`**; the normalised statement contains no `p` and no `R`.
- **COROLLARY 4.** `E(1) = −Δ` exactly (measured on every toy row). **The knife-edge constant IS the `c = 1` slack of the tail criterion**: 46.02 bits of slack under the banked reading, an 17.98-bit deficit under exact balance — and that deficit is precisely THEOREM Z-FLOOR's `2^{17.98}` firing, since the `u = 0` atom contributes `2^{−Δ}` to `Z_1`. An independent cross-validation of the knife edge from the tail side.
- **THEOREM 7 / COROLLARY ZM.** The flat model's CGF is `Λ(θ) = log₂ C(2θ,θ) − θ` in closed form, so `Λ(1) = 0` and the flat model gives `I(c) ≥ c` for every `c` **with equality exactly at `c* = Λ'(1) = 1/ln 2 − 1 = 0.4426950409`**. Margin profile: `0.157` at `c=0`, `0.021` at `0.3`, `0.0021` at `0.4`, **`0.0000` at `c*`**, `0.037` at `0.6`, `2.00` at `1`. Finite-`p` constants converge as `O(1/p²)`: `0.4421636, 0.4426922, 0.4426950, 0.4426950409` at `p = 17, 97, 673, 65537`.

**Consequence for the board:** the terminal must be proved at a *single* layer, `c ≈ 0.443`, where the flat model has **zero** margin. No "lose a constant per coordinate" argument can ever survive there, and no layer can be given away.

## T2 — the `p = 7, w = 4` creation mechanism: **IDENTIFIED EXACTLY**

**THEOREM 13.** `288 = 16 + 16 + 16×16`, all of it generated by ONE orbit at half the length:

1. **Decimation.** Every weight-7 codeword is supported on a single sublattice (16 even, 16 odd, **0 mixed**). Under `v(X) = g(X²)` the exponents matter only mod 16, and `T = {1,3,5,7,17,19,21,23}` collapses 2-to-1 to `{1,3,5,7}`: the even-sublattice system has **`F_7`-rank 4, not 8** (measured: length 8, rank 4, dim 4) — a `7^4 = 2401`-fold density gain.
2. **One orbit.** That `[8,4]_7` code is self-dual, so LEMMA TWT forces `7 | wt`, i.e. `wt = 7`; it contains exactly 16 ternary words = one free negacyclic orbit.
3. **Composition.** Even and odd supports are disjoint, so all `16×16 = 256` sums are codewords — and the measured weight-14 stratum is **exactly** that set (verified as set equality).

**The `484×` ledger:** `7^4` (decimation rank collapse) × `16` (orbit quantization) × `9` (composition, `288/32`), leaving **one residual: a single orbit where `0.0267` were expected** — a Poisson event at `P(≥1) = 2.6%`, not a `484×` anomaly. Cross-`p` scan of the decimated cell: the collapse occurs only for `p ∈ {7,17,23}` (`ord_16(p) = 2`), and among those **only `p = 7` admits any ternary word**, because TWT needs `p ≤ 8` = the sublattice length (measured counts `16, 0, 0`).

&gt; **CATCH-T2 (a structural symmetry worth banking).** The mechanism's second ingredient is `p ≤ (sublattice length)` — a **`p ≤ O(1)` condition of exactly the shape THEOREM Z-NOGO and COROLLARY 8 produce on the *bounding* side**. Creation-by-self-orthogonality and discharge-by-distance+counting die at the same place. Small-`p` over-representations are therefore not evidence of danger at the prize rows.

## T2 transport — **THEOREM 14 (decimation dichotomy): NO ANALOGUE, and saturation is the reason**

`S = 2^38` is a 2-power, so *every* sublattice is a `2^k`-decimation — the case analysis is complete. At level `k`, with `A = 2^{38−k}`:

```
    the window Lambda = {1,3,...,2R-1} COLLAPSES  &lt;=&gt;  A &lt;= R-1
    the sublattice code has POSITIVE dimension    &lt;=&gt;  A &gt; R
```

**Mutually exclusive**, and `A = R` is impossible (`v₂(R) = 2` for the banked `R`; the exact-balance `R` is odd). Verified for both `t`-readings over all 39 levels — no level has both — and the same dichotomy holds at every toy `I1` row and level. The crossover sits at `A ≈ R` **because `R/S = 1/log₂ p`**: the official window is a short initial segment of diameter `2R−2 = S/32.00`, whereas the `p=7` cell's `T` is spread (it contains `s` and `s+16`). The TWT ingredient fails independently (`|T| ≥ N/2` and `p ≤ length` both false at `R/S = 1/64`, `log₂ p ≥ 39`) — CATCH-19D re-derived.

**Banked as a tail-count constraint:** since `Z_1 = p^{−R}Σ_u P(u)`, a creation mechanism would force `Z_1` large and hence force the tail count large. The only creation mechanism observed in the small-scale census **cannot operate at the official parameters, so it forces no tail**. This removes a candidate refutation of the terminal; it does not prove the terminal.

## T3 — the measured tail profile (grid exactly as pre-registered; no shift-0 cells)

`S = 2^{v₂(p−1)−1}` forced by `p`; `Λ = {1,3,…,2R−1}` so the exponent `0` never occurs (asserted in code); all `2S` 2-powers. Every row exhaustive over all `p^R` tuples; nothing sampled. `E(c) = log₂Pr + cS`; `E_nz` strips the `u=0` atom (the trivial-character term) to expose the genuine tail.

| row | S | R | Δ | Z_1 | max E(c) | max E_nz(c) |
|---|---|---|---|---|---|---|
| G1 p=17 | 8 | 2 | +0.175 | 1.250000 | −0.175 @1.00 | −2.375 @0.10 |
| G2 p=113 | 8 | 1 | −1.180 | 2.375000 | +1.180 @1.00 | (empty) |
| G3 p=241 | 8 | 1 | −0.087 | 1.500000 | +0.087 @1.00 | −1.713 @0.15 |
| G4 p=97 | 16 | 2 | −2.800 | 9.387207 | +2.800 @1.00 | **+0.600 @0.55** |
| G5 p=353 | 16 | 2 | +0.927 | 1.156250 | −0.927 @1.00 | −2.727 @**0.45** |
| G6 p=673 | 16 | 2 | +2.789 | 1.097656 | −2.789 @1.00 | −2.197 @**0.45** |
| p=193 (off-sat) | 32 | 2 | −16.815 | 1.153e5 | +16.815 @1.00 | −4.385 @0.15 |
| p=193 (off-sat) | 32 | 3 | −9.223 | 5.984e2 | +9.223 @1.00 | −1.377 @**0.45** |
| p=577 (off-sat) | 32 | 2 | −13.655 | 1.290e4 | +13.655 @1.00 | −1.745 @0.30 |
| p=641 / p=257 / p=769 | 64/128/128 | 2/1/2 | −45.4/−120.0/−108.8 | 4.5e13/1.3e36/5.8e32 | −Δ @1.00 | (empty) |
| p=65537 | 32768 | 1 | — | — | **UNREACHED** (`p^R·S = 2.15e9`) | — |

1. `max_c E(c) = −Δ` at `c = 1` on **every** row, exactly — Corollary 4 measured.
2. **The genuine tail obeys the criterion's decay at every row measured**: `E_nz(c) &lt; 0` at every `(row, c)` bar one cell (G4, `+0.600` at `c=0.55`), and it does **not** grow with `S` (`S=8`: −2.4,−1.7; `S=16`: +0.6,−2.7,−2.2; `S=32`: −4.4,−1.4,−1.7). P8(ii),(iii) confirmed.
3. **The binding layer is measured where COROLLARY ZM predicts**: `argmax E_nz = 0.45, 0.45, 0.45` on the three rows with both resolution and tail, against `c* = 0.4427` (grid step `0.05`). P8(i) confirmed.
4. Against the flat rate function the measured tail sits `1.4`–`2.9` bits **below** flat across the whole `c`-range, tightening exactly at `c*`. Per the standing calibration clause (`statement.md:64-69`) this is **not** a claim that the object beats random.

## Catches minted

- **CATCH-T1** — Prop 10's doubling/log-sine functional telescopes to the elementary cost identity; the recorded lead at `statement.md:68-69` has no Dedekind content and no object to bound. *Against the node statement; should reach the maintainer stack.*
- **CATCH-T2** — the creation mechanism needs `p ≤ length`, i.e. `p = O(1)`, the same threshold shape as Z-NOGO/Corollary 8 on the bounding side.
- **Corollary 4** — the knife-edge constant is exactly the `c = 1` slack of the tail criterion (a re-identification of a banked constant, not a correction).
- **Theorem 10's diagnosis** — a distance+counting member whose threshold is *no `p` at all*, i.e. strictly worse than Corollary 8.

## Honest residuals

1. **No tail bound at the official row for `c ≤ 1 − 2^{−124.19}`.** The proved range has width `2^{−124.19}`; calling it "a proved `c`-range" would be misleading — it is an endpoint.
2. **§7 is a structural deficit, not a no-go.** I show the three inputs the object supplies are all `R`-local and quantify the shortfall (factor `8.60`); I do **not** prove that no argument can supply non-`R`-local information. Weil would have — it is vacuous by 26 bits.
3. **The Poisson-duality circularity is a structural observation**, not a theorem: it shows the two standard instruments coincide here, not that no third exists.
4. **Two of my own registered predictions missed**, reported not absorbed: **P6/H1** (I predicted a ternary generator polynomial; it is `h = 1 + 2X² + 2X⁴ + 5X⁶ + X⁸`, weight 5, not ternary — `h` being a polynomial in `X²` is a *consequence* of the decimation, not the cause), and **P7's stated reason** (the transport verdict stands but by Theorem 14, not by the constant-term argument I registered).
5. **A grid row of my own was mis-specified**: I registered A7 as `(65537, S=16, R=1)`, but `S` is *forced* by `p` (`S = 2^{v₂(p−1)−1} = 32768`), making it `2.15e9` evaluations. Declared **UNREACHED**, never estimated.
6. **The `p=7` residual is not explained further**: after decimation, TWT and orbit quantization, one orbit occurred where `0.0267` were expected (2.6% Poisson). I do not claim a mechanism for that single event.
7. **FAMILY B rows are far off-saturation** (`Δ` very negative), so their `Z_1` is dominated by the `u=0` atom; only their `E_nz` profiles carry tail information, and this is labelled throughout.
8. **`c* = 0.4427` is a FLAT-MODEL statement.** The true rate function at the official row is unknown — that *is* the terminal. What is proved is that the flat model saturates the criterion there with zero margin.
9. Calibration clause honoured: no toy is evidence about `Z_1` at the official row; toys verify identities and measure constants only. AK-UNIT respected — no congruence conclusion about any count.

result: The F2 tail-count terminal is re-shaped, not closed — LEAD 1(a) is dead (CATCH-T1: Prop 10's doubling/log-sine functional telescopes exactly to the elementary cost form `log2 P = S − Σ_s d(c_s)`, so there is no Dedekind sum to bound); the criterion is restated free of constants (`Pr[P ≥ 2^{cS}] ≤ 2^{−cS+o(S)}`, the banked `+46.02` being exactly the saturation constant `Δ`, and `E(1) = −Δ` re-identifying the knife edge as the `c=1` slack); its binding layer is pinned exactly at `c* = 1/ln 2 − 1 = 0.4427` where the flat model saturates with **zero** margin; the tail is proved to be a small-values/box count for the MDS value code, with one layer proved outright (`U_c = {0}` for `c &gt; 1 − 2^{−124.19}`) and both supplies for the rest killed with computed thresholds (Z-2 moments: empty range, `p ≤ 8.30` = Corollary 8's; interpolation: empty at *every* `p`, killed by position entropy `H(1/L) &gt; 1/L`), the common cause named as `R`-locality short by the factor `log2 p/log2(e log2 p) = 8.60` with the Fourier escape shown circular; and LEAD 2 is fully explained — `288 = 16 + 16 + 16²` by decimation rank-collapse (`T mod 16` collapses 8→4, rank 4 not 8) × TWT × composition, with the mechanism proved absent at the F2 parameters by an exact decimation dichotomy forced by saturation `R/S = 1/log2 p`; 111 checks, 0 fail.
