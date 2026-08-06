# PRE-REGISTRATION — the Ax-Katz / Chevalley-Warning transfer on (ES)

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is the campaign's single
most important open thread: the ONE untested classical transfer on the
four-lane terminal.

## 0. The frontier (verbatim, FABLE_AUDIT of mun_anticoncentration)

> **THE FRONTIER**: the exact zero-count statement (0/1 codewords of
> the [2^41, 2^41-w+1, w] RS codes = periodic only), with four
> proved structural constraints on any solution, and **AX-KATZ /
> CHEVALLEY-WARNING as the untested transfer** — p-divisibility is
> the one classical family sensitive to defining sets.

And the route cut already PROVED (do not re-litigate): identical-
enumerator code pairs with different 0/1 counts — MacWilliams /
Delsarte / Krawtchouk / Sidelnikov / BCH-family CANNOT decide it in
principle; Weil vacuous 13.5-107 bits; L2 loses exactly 2^128.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/mun_anticoncentration/PREREG.md` section 0 —
  the object of record: the crossing count is the constant-weight
  count `W_w = { x in {0,1}^n <= F_p^n : wt(x) = r', x in C(n,p,Z_w) }`
  at n = 2^41, w in [2^34, 2^39], r' = 2^40 - w, delta = ord_n(p) in
  {1,2,4}, p >= 2^39+1; the band instance table (strictly finer);
  Newton invertibility at all four rows.
- `notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md` — the
  (ES) statement of record, the four structural constraints, the
  measured early suppression, the above-balance accident witness.
- The five verifiers in that dir — reuse their exact-count machinery
  for calibration rows (they are the banked ground truth).

## 2. Pre-registered claims

- **(A1)** The algebraization: exhibit the count |W_w| as the F_p
  point count of an explicit polynomial system (the 0/1 locus
  x_i^2 = x_i, the vanishing prefix e_1 = ... = e_{w-1} = 0 — or the
  power-sum prefix, Newton-invertible at all rows — plus the weight
  equation), with degrees and variable count stated exactly, in BOTH
  the base-field and delta-extension readings.
- **(A2)** The Ax-Katz divisibility exponent mu computed EXACTLY for
  that system at the four rows of record (both readings), and the
  Chevalley-Warning baseline. State the formula before plugging in.
- **(A3)** THE DECISION: does p^mu-divisibility, combined with the
  four proved structural constraints and the exactly-known periodic
  count, FORCE |W_w| = (periodic count)? Pre-register the three
  possible verdicts and what each requires:
  (i) TRANSFER LIVE — divisibility gap exceeds the accident budget;
  state the remaining obligation as a named lemma.
  (ii) TRANSFER DEAD-VACUOUS — mu too small to separate; prove it
  and state the exact shortfall in bits (as was done for Weil).
  (iii) TRANSFER DEAD-INSENSITIVE — divisibility holds equally for
  periodic-only and accident-bearing counts; exhibit the failure on
  the round-15 identical-enumerator pair or a new witness.
- **(A4)** Calibration: on toy rows where the exact counts are banked
  (reuse the round-15 verifiers), check the Ax-Katz prediction against
  the true counts. `tools/ramguard local -- python3 ...` scale only.
- **(A5)** If the transfer is dead, name what property of the
  defining-set structure a decisive method must see (sharper than
  "not the enumerator"), to steer the Pro brief and the next pilot.

## 3. Pre-registered falsifiers / honesty clauses

- If the algebraization itself is wrong (e.g., the 0/1 slice cannot be
  polynomial-encoded without blowing up degrees past usefulness),
  report that as the finding.
- Any claim of (i) must survive its own adversarial check: verify the
  divisibility bound is NOT satisfied by adding one accident pair to
  the periodic count. If it is, the verdict is (iii), not (i).
- Small-p calibration failures kill the row-level claim, not the
  method; separate the two explicitly.

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  `notes/pilots_20260806/es_axkatz_transfer/`. Never touch dag.json,
  node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.

---

# PILOT PRE-REGISTRATION (appended by the Opus pilot BEFORE any computation)

Round 16, 2026-08-06. Everything below is registered before a single line
of arithmetic is run. Repo root `/home/u2470931/smooth-read-solomin/prize`;
all compute under `tools/ramguard`.

## P0. The theorems I will use, STATED BEFORE PLUGGING IN

- **(AK) Ax-Katz** (Katz, *On a theorem of Ax*, Amer. J. Math. 93 (1971)).
  Let `f_1,...,f_m in F_q[x_1,...,x_N]` have degrees `d_1,...,d_m`, and let
  `V = {x in F_q^N : f_1(x) = ... = f_m(x) = 0}`. Then
  ```text
  |V| = 0  mod q^mu,      mu := ceil( (N - sum_j d_j) / max_j d_j ).
  ```
- **(CW) Chevalley-Warning.** If `sum_j d_j < N` then `p | |V|`.
  (The `mu >= 1` regime of (AK) up to `q` vs `p`.)
- **(W2) Warning's second theorem.** If `sum_j d_j < N` and `V != empty`
  then `|V| >= q^{N - sum_j d_j}`.
- **(MM) Moreno-Moreno.** The `p`-weight-degree refinement: replace each
  `d_j` by its `p`-weight degree (max over monomials of the sum of the
  `p`-adic digit sums of the exponents).
- **(McE) McEliece.** For a cyclic code of length `n` over `F_p`,
  `p ∤ n`: every codeword weight is divisible by `p^{ell-1}`, where `ell`
  is the least number of *nonzeros* of the code (repetitions allowed)
  whose product is `1`.

I pre-register that I will implement (AK)/(W2) and VALIDATE the
implementation by brute force on small systems (including systems with
`mu >= 1`) before applying it to any row. A validation failure kills the
row-level numbers, not the method (PREREG section 3, clause 3).

## P1. The two algebraizations I will exhibit and verify

- **(ALG-I) indicator reading.** `N = n` variables `x_1..x_n`; equations
  `x_i^2 - x_i` (n of them, degree 2), the window forms (degree 1), and
  the weight form `sum_i x_i - r'` (degree 1). Extension reading over
  `F_q`: `w-1` window forms. Base-field reading over `F_p`: `|Z_w|`
  window forms.
- **(ALG-L) locator reading.** Variables = the `r'` non-leading
  coefficients of a monic `E` of degree `r'` and the `n-r'` non-leading
  coefficients of a monic `F` of degree `n-r'`; equations = the `n`
  coefficient identities of `E*F = X^n - 1` (degree 2, bilinear), plus
  the window forms (degree 1) on `E`'s coefficients. I predict
  `N = n` (crossing prefix reading: `N = n - (w-1)` after eliminating
  the `w-1` forced zero coefficients) and hence a `mu` LESS negative
  than (ALG-I) by exactly `w` (resp. `w-1`).
- **Falsifier (registered):** at small fixtures the `F_q`-point count of
  (ALG-L) must equal the brute-forced `|W_w|` exactly. If it does not,
  the algebraization is wrong and THAT is the finding (PREREG section 3,
  clause 1).

## P2. Predicted verdict: **DEAD**, by three independent mechanisms

- **(P2a) VACUOUS.** `mu < 0` at all four rows in both readings. I
  predict, exactly, `mu_(ALG-I,ext) = -(n+w)/2` at the crossing row and
  a Chevalley-Warning deficit `sum d - N + 1 = n + w + 1`, i.e. a
  shortfall of `~2^41.0` degree-units (`41.0` to `41.3` bits) at every
  row. **Falsifier:** any row/reading with `mu >= 1`.
- **(P2b) LOGICALLY MIS-SHAPED (the p-adic unit obstruction).** At the
  crossing rows the (ES) target is `|W^struct| = C(n/M, r'/M)` with
  `M = w = 2^v`, `L = n/M = 2^{41-v} <= 2^7`. Every prime factor of a
  binomial coefficient `C(L, j)` is `<= L`; and `p >= 2^39 + 1 >> 128`.
  So `p ∤ |W^struct|` UNCONDITIONALLY. Hence a true statement
  `p | |W_w|` is *equivalent to* `|W_w| != |W^struct|`: p-divisibility
  is an ACCIDENT-EXISTENCE theorem here, never an accident-exclusion
  theorem. **Falsifier:** a crossing row where `L > p`, or where
  `|W^struct|` is not of binomial shape, or `|W^struct| = 0`.
- **(P2c) STRUCTURALLY IMPOSSIBLE (the Warning obstruction).** For ANY
  polynomial system over `F_q` whose `F_q`-point count equals `|W_w|`
  exactly: if `0 < |W_w| < q` then by (W2) `N - sum d <= 0`, hence
  `mu <= 0`. Under (ES), `|W_w| = C(L, r'/M) <= C(128,63) < 2^{125} < q`
  at every crossing row, so **no exact algebraization whatsoever can
  have a positive Ax-Katz exponent** at the crossing rows. I register
  the escape hatch explicitly: a *fibered* encoding with point count
  `c * |W_w|` evades this only by putting the divisibility into `c`,
  where it carries no information about `|W_w|`. **Falsifier:**
  `C(128,63) >= q`, or a counterexample to (W2) in validation.
- **(P2d) INSENSITIVE.** On the round-15 identical-enumerator witness
  (`n=16, p=17, w=3, r'=8`, defining sets `{1,2}` vs shifts `{a,a+1}`,
  0/1 counts that SEPARATE), I predict the Ax-Katz exponent is
  IDENTICAL for all shifts, in BOTH readings — including `|Z_w|`, since
  `ord_16(17) = 1` makes every `|Z| = w-1 = 2`. **Falsifier:** the
  exponents differ across the separating pair.
- **(P2e) McELIECE VACUOUS.** `0 ∉ Z_w` (the defining set is
  `{1,...,w-1}` and its p-closure, which cannot contain `0`), so
  `zeta^0 = 1` is a nonzero of the code and `ell = 1`: McEliece gives
  `p^0`. Vacuous at every row and for every shifted defining set.
  **Falsifier:** `0 in Z_w` at some admissible row.

## P3. The one LIVE shape I will test honestly

"Divisibility + a priori upper bound => vanishing": if `q^mu | |W|` with
`mu >= 1` and independently `|W| < q^mu`, then `|W| = 0`. This is the
only shape in which a p-divisibility theorem can PROVE a suppression
statement, and it is the relevant one at the BAND rows, where I predict
the structural count is `0` (I predict `M ∤ r'` at all three band rows,
`M = 2^33, 2^33, 2^32`, so `|W^struct| = 0` and the band target is a
genuine VANISHING statement, to which (P2b)/(P2c) do NOT apply).
**Predicted outcome:** both ingredients fail — `mu <= 0` by `~2^41`
degree-units, and the a priori upper bound is `C(n,r')`, astronomically
above `q^1`. I will state both shortfalls exactly, in bits.
**Falsifier:** `mu >= 1` at a band row, or an a priori bound below `q`.

## P4. Adversarial obligations (binding)

- If any reading yields `mu >= 1`, I report **TRANSFER LIVE** and
  immediately run the adversarial check required by PREREG section 3,
  clause 2: test whether the divisibility is also satisfied by
  `|W^struct| + (one accident pair)`. If it is, the verdict is (iii).
- I will NOT claim "no polynomial encoding can work" beyond what (P2c)
  proves; the fibered-encoding hatch stays named in the report.
- Calibration failures at small `p` kill the row-level claim only; I
  will separate method-level from row-level conclusions explicitly.

## P5. Additional registered falsifiers

- **(P5a)** If, at small fixtures, `p | |W_w|` *systematically* (not by
  accident), the p-adic unit obstruction is wrong and the verdict flips
  toward (i). I predict instead that `p ∤ |W_w|` at a clear majority of
  fixtures, and in particular `p = 17 ∤ 32` on the round-15 witness.
- **(P5b)** If the Moreno-Moreno p-weight-degree refinement gives a
  strictly larger `mu` than (AK) at any row, I report that; I predict it
  does not, because every degree in play (`1` and `2`) is `< p`, so the
  p-weight degree equals the degree.
- **(P5c)** If the `prod T = gamma` refinement of the crossing window
  (MC-1's third clause, dropped in the round-15 object of record)
  changes any verdict, I report it separately rather than silently
  folding it in.
