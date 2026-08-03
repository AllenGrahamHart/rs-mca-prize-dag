# PRE-REGISTRATION — list-size terminus program (Opus 5 pilot, 2026-08-03)

Written BEFORE any computation in this pilot. Reading of banked material
(xr_band_occupancy, xr_graded_band_ledger, band_heart_consolidation,
xr_band_key_lemma_pencil_mass, list_bound_transfer, BAND_LANE_DEFINITIONS)
preceded this file; no machine run did.

Target of record as handed to this pilot (CONSOLIDATION.md UPDATE 3, item 1):

> for an admissible received pair, SOME pencil member w_z has at most
> C n^2 codewords at agreement >= tau = k + ceil(h/2),
> C = 0.80 / 0.686 / 0.660 at the three prize rows.

## Position entering the pilot

The target is ALREADY REFUTED in the tree
(`background/nodes/xr_band_key_lemma_pencil_mass/statement.md:100-114`;
`notes/pilots_20260802/list_bound_transfer/REPORT.md:12-18,39`;
`notes/pilots_20260802/xr_band_occupancy/FABLE_AUDIT.md:97-107`).
The pilot's job is therefore NOT to prove it. It is to (i) supply the
STRUCTURAL reason the refutation is inevitable rather than constructive,
(ii) localise exactly what THEOREM 2 discards, (iii) state the repaired
terminus. Predictions below are about those.

## Predictions (falsifiers pre-registered)

**P1 (band shadows every member).** For every fixture and every
`z in P^1(F_q)`:
`L(w_z, tau) >= #{joint-explanation events of size >= tau}` (RAW —
every joint pair, no `L_P >= 2` selection). Confidence 0.97 (I have a
proof from the banked KEY LEMMA rank-0 branch + the tangent gate).
FALSIFIER: one admissible fixture + member with `L_z` below the raw
high count.

**P2 (min-over-z buys nothing).** On fixtures with a nonempty high band
the minimum over `z in P^1` of `L(w_z,tau)` equals the raw high count
exactly on at least half the members (sporadic list members are the
exception, not the rule). Confidence 0.6.
FALSIFIER: `min_z L_z > raw_high` on every fixture with band mass, i.e.
the sporadic part is generically nonempty — that would mean the min is
strictly informative.

**P3 (census identity).** For every `j` with `k+1 <= j <= tau`, writing
`G_j(z) = #{j-subsets S : I_S(w_z) in C}`, `D_j = #{S : A(S)=B(S)=0}`,
`R_j = #{S : rank[A(S);B(S)] = 1}`:
`SUM_{z in P^1(F_q)} G_j(z) = R_j + (q+1) D_j` EXACTLY.
Confidence 0.95 (this is the banked KEY LEMMA summed over `S`).
FALSIFIER: any toy mismatch.

**P4 (every averaging bound is vacuous).** The resulting unconditional
bound `min_z L <= R_j/((q+1) C(tau,j)) + D_j/C(tau,j)` with the only
unconditional input `R_j <= C(n,j)` is vacuous at all three prize rows
for EVERY `j in [k+1, tau]` — not by a small factor but by ~1e11 bits.
Confidence 0.85.
FALSIFIER: some `j` at some prize row where the first term is
`<= 0.68 n^2`.

**P5 (selection-insensitivity of the refutation).** The gap between the
occupancy lemma (which survives MC) and the list statement (which MC
kills) is EXACTLY the `L_P >= 2` selection in the definition of `N_d`
(BAND_LANE_DEFINITIONS item 8): raw high-depth pairs inject into every
member's list, selected ones are a sub-count. Hence no selection
convention can rescue the list statement. Confidence 0.8.
FALSIFIER: a member whose list omits a raw (unselected) high-depth pair.

**P6 (second-moment ledger is scale-critical).** The pencil-global
two-tier Johnson/second-moment ledger closes iff
`tau^2/n > n/nu^2` with `nu = floor(n/tau)`; since `nu tau <= n` by
definition this never closes. Predicted deficit factor at the six rows:
between 1 and 16 (i.e. a constant, NOT an astronomical, miss).
Confidence 0.7 for the "constant factor" part.
FALSIFIER: a row where the computed closing ratio exceeds 1.

## Named non-goals

- Not re-deriving THEOREM I, the KEY LEMMA, MC, or the 2^130-2^197
  worst-case numbers: all cited, none re-proved (hard law 5).
- No claim that anything here is new mathematics until subtracted
  against `background/nodes/xr_band_key_lemma_pencil_mass` and
  `xr_band_ledger_theorems`. Expectation entering: P1 and P3 are
  COROLLARIES of banked nodes, and their value is the consequence
  (route death + localisation), not the mathematics.
