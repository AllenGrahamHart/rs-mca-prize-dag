# xr_band_ledger_theorems

- **status:** PROVED
- **closure:** proof
- **scope:** Claims 1-5 are interpolation/counting proofs valid at every
  scale; the six-row pricing is exact integer arithmetic at the pinned
  parameters; every empirical figure is toy-scale and labeled.
- **provenance:** graded-band-ledger pilot THEOREMs 3, 4, 5 (+corollary)
  and 7, with Theorem 6 recorded as a WARNING only
  (`notes/pilots_20260802/xr_graded_band_ledger/{REPORT,FABLE_AUDIT}.md`,
  `band_arith.py` ALL CHECKS PASS, battery > 4e7 pair comparisons, 0
  violations), CORRECTED by the same-day band-occupancy amendment
  (rigidity keyed on RAYS; the master inequality is worst-case TIGHT;
  the tangent gate is pencil-wide over `P^1` incl. `(0:1)`).

## Setting

`RS_k` on `n` distinct points of `F_q`, `A = k + h`, `R = n - k`.
Symbol pinned `k` (never `K`). Received pair `(u, v)`; **band pair**
`P = (f, g)` = codeword pair with joint agreement `Z_P` of size
`k + d`; **band (proper)** = depths `[1, h-2]`; the ledger extends to
the **band column** `[1, h-1]` with the depth-`(h-1)` CASCADE TIER
named (ratified Route T fold-in) at zero proof cost, because the
theorems below use ONLY the banked k-packing and the tangent gate —
per definitions item 5 the hypothesis line cites the **generic core
ceiling** (item 4: all distinct-slope selected-support cores
`<= A-1`), NEVER "below cascade". `L_P` counts SELECTED supports
containing `Z_P` (item 8); live slope over ALL of `P^1(F_q)` incl.
`(0:1)` (item 7).

Hypotheses: **(H1) k-packing** — BANKED verbatim at
`background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`,
consumed not re-derived (hard law 5); **(H3) tangent gate**,
pencil-wide.

## Statement (Claims 1-5 PROVED; W is a warning, not a claim)

1. **THEOREM 3 (line cap under `J >= k`).** For a codeword pair with
   `|Z_P| = J >= k`, the number of slopes `z` whose forced ray
   `f + zg` has agreement `>= A` is at most

   ```text
   L_P <= floor((n - J) / (A - J)).
   ```

   **Precision note (subtraction, hard law 5):** the banked
   `critical/nodes/common_code_line_budget` prints the same formula
   under the hypothesis `a + b - n >= k`, which EVALUATES FALSE at
   all six rows (`2k + h + d - n < 0`) — the banked node does not
   cover the band; THIS `J >= k` interpolation version is the one of
   record, and it is strictly sharper than the F5 sunflower form
   `(n-k)/(t-d)`. Verified TIGHT at `d = 1, 2, 3` (caps `2, 3, 4`)
   and `cap + 1` unrealisable by point count.
2. **THEOREM 4 (ray rigidity — keyed on RAYS).** Two distinct
   codeword pairs with `|Z| >= k` are subordinate to at most ONE
   common ray `(z, c)`, and only if `f_1 - f_2 = -z (g_1 - g_2)` as
   polynomials — which determines `z` uniquely. **The slope-keyed
   reading is FALSE**: re-selection freedom is real (15/76 admissible
   fixtures carry a slope with two distinct exact-`A` rays —
   band-occupancy correction), so every rigidity/coset statement must
   be keyed on rays, with the selected support the ONE first-match
   ray (item 7).
3. **THEOREM 5 (union agreement) + COROLLARY (band interaction
   strip).** If `f_1 - f_2 = -z^* (g_1 - g_2)` then
   `c := f_1 + z^* g_1 = f_2 + z^* g_2` agrees with `u + z^* v` on
   ALL of `Z_1 u Z_2`. With (H1),
   `|Z_1 u Z_2| >= k + d_1 + d_2 + 1`, so **`d_1 + d_2 >= h` forces
   a T2/P2 tangent event** and the received pair leaves the generic
   branch entirely. When `|Z_1 ^ Z_2| = k - 1` exactly,
   proportionality is AUTOMATIC by degree (both differences are
   constant multiples of the overlap's vanishing polynomial) — that
   whole configuration class is stripped. This is a genuine STRIP
   EXTENSION, and it kills the shared-block doubling attack (the only
   battery fixture that beat the printed column).
4. **THEOREM 7 (two-column determinacy — the anti-concentration
   lever).** Let `zeta_P(i)` be the unique `z` with
   `(u_i - f(x_i)) + z (v_i - g(x_i)) = 0` (the pencil direction
   joining the received point to the pair's centre in `A^2`). For any
   two pairs with `zeta_{P_1}(i) != zeta_{P_2}(i)`, the values
   `(u_i, v_i)` — hence `zeta_P(i)` for EVERY other pair — are
   determined by that ordered pair of directions (`2 x 2` system,
   determinant `z_2 - z_1 != 0`). The banked
   `zeta_c(x) = (c(x) - u(x))/v(x)` (F5_SKELETON) is the one-sided
   `g = 0` special case; the centre-and-direction form for codeword
   PAIRS is this node's. Band occupancy becomes a point-line
   incidence count in `A^2` — the designated lever for the open
   lemma, recorded as structure.
5. **Master ledger inequality + exact pricing.**
   `|Gamma_band| <= SUM_{d} N_d L(d)`, `L(d) = floor((R-d)/(h-d))`
   (Claim 1 at `J = k + d`), `Gamma_band` = live slopes sharing a
   band core with another live member. Exact six-row pins
   (verifier-recomputed): band-proper `SUM_d L(d)` =
   **828 / 967 / 479** (RowC) and
   **36,839,268,578,566 / 43,010,571,891,409 / 44,764,496,190,275**
   (prize); `L(h-1) = n - A + 1` EXACTLY on all six rows (the printed
   tangent column is precisely one cascade pair — cascade
   separability); the printed `n - A + 1` column is exceeded by
   `SUM_d L(d)` on 5 of 6 rows even at `N_d = 1` (828 > 764;
   967 > 892; prize by ~22x; only RowC 1/16 fits) — **the band column
   must be a THIRD generic column from the `13n^3` headroom, never an
   enlargement of `B_tan`** (as ratified; see
   `xr_graded_tangent_band_charge`).

**WARNING W (Theorem 6 — recorded, NOT a tool).** Pairs subordinate to
a fixed ray `(z, c)`, `z != 0`, with `|Z_P| >= k` are in bijection
with codewords of the punctured `[A, k]` MDS code `C|_S` at agreement
`>= k` against `v|_S` (via `P = (c - zg, g)`,
`Z_P = {i in S : g(x_i) = v_i}`). Per-ray band multiplicity is
therefore an MDS list size at agreement `k+1` out of `A` — far below
the Johnson radius, and NOT polynomially bounded by anything banked.
The master inequality is lossy generically — **but worst-case TIGHT**
(amendment of record: slack exactly `1.000` attained on the banked
single-core family; exactly `2.000` on the entire max-`N_d` sunflower
family): slope-counting reformulations buy at most a factor 2. A
sharp ledger must eventually count slopes directly.

## Explicitly NOT claimed (context)

- **No occupancy bound**: `N_d` is bounded by NOTHING banked; the
  banked interleaving collapse (`list_subsqrt_interleaving_collapse`)
  is TRUE BUT VACUOUS here (`L(k+1)` astronomically above `n^2`) — do
  not cite it as progress. The band occupancy lemma is the single
  named open input of the red TARGET.
- **No Route-S impossibility**: re-selection freedom EXISTS (the
  ledger pilot's "no purchase" claim was refuted by the occupancy
  pilot); Claim 2's rigidity is exactly what survives.
- **Supersession flag (coordinator decision recorded, not taken
  here):** the band-occupancy pilot's unified fibre-strip THEOREM 1
  contains the mechanism of Claims 2-3 and extends it to
  `z in {0, (0:1)}` with weaker hypotheses; its mint was queued by
  that pilot's audit but is NOT part of this wave — if minted later,
  add a `ref` edge and keep these claims as the band-ledger form of
  record.
- Theorem 1 of the pilot (k-packing) is NOT minted — banked, cited.
- Nothing about official-scale band population (toy fixtures only).

## Falsifier

A codeword pair with `J >= k` carrying more than
`floor((n-J)/(A-J))` rays of agreement `>= A`; two distinct pairs
subordinate to two distinct common rays, or to a common ray without
the proportionality identity; a proportional pair with
`d_1 + d_2 >= h` inside the tangent gate; a fixture violating the
master inequality; or an exact-integer failure of the six-row pricing
pins.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory; NOTE: the prize-row divisor-block sums make this one of
the slower verifiers of the wave, ~2 s measured). Checks: cap
arithmetic
+ a planted single-core fixture with `L = cap` TIGHT at `d = 1, 2, 3`
and `cap + 1` point-count unrealisable; T4 on every witnessed common
ray of two fixtures (proportionality + unique `z`; at most one common
ray per pair of pairs); the T5 planted overlap-`(k-1)` fixture
(proportionality automatic, forced ray agreement
`= |Z_1 u Z_2| = A + 1` — the gate fires; the shared-block attack
self-refutes); T7 exact `2 x 2` reconstruction at every coordinate
with two distinct directions; the FULL sunflower fixture
(`m = 7` cores at `(16,3,3)`): `N_1 = 7`, `|Gamma_band| = C(7,2) =
21`, master-ledger slack EXACTLY `2.000`; W's bijection counted on
one ray; and the six-row pricing pins (band-proper `SUM L(d)` by
divisor blocks, `L(h-1) = n-A+1`, the printed-column kill on 5 of 6
rows).
