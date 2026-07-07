# Overnight Report 2026-07-08

## Executive Summary

Terminal A reached.  The h=3 characteristic-zero classification is proved
without Conway-Jones: for unit triples, `e2 = product * conjugate(e1)`, so a
distinct equal-`e1,e2` pair must have `e1=0`; every zero-sum unit triple is a
rotated `mu_3` coset.  Therefore the only persistent char-zero h=3 families are
the toral coset pairs, counted by `binom(n/3,2)`.  All non-toral finite-field
interior h=3 trades are norm-gate accidents: for each fixed shape, activation at
primes `p >= n^2` is bounded by the large-prime divisors of a nonzero
cyclotomic obstruction norm, at most `floor(phi(n) log(6)/(2 log n))` primes.
The exact replay verifies rows through `n=96` and confirms the three banked
norm-gate shapes activate only modulo their selected primes.  Terminal B is
partially banked: the h=2 trade/additive-energy reduction and Stepanov parameter
arithmetic replay exactly, and the external import has been sharpened to the
explicit Cochrane--Pinner constant `16/3`, but the in-house HBK/Konyagin energy
theorem is still open.  Terminal C has a light pilot: observed activated
`n=96` h=3 shapes do not repeat across the actual prime rows in the ladder.

## Claims

1. **PROVED:** h=3 char-zero classification.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_CLASSIFICATION.md
   ```

   Node-candidate files:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_NODE_STATEMENT.md
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_NODE_PROOF.md
   ```

   Content: every distinct disjoint pair of 3-root-of-unity subsets with equal
   `e1,e2` is a pair of `mu_3` cosets.  No exotic 5th/7th/9th-root char-zero
   families survive.

2. **PROVED:** per-shape norm-gate activation bound.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_CLASSIFICATION.md
   ```

   Bound: each fixed non-toral shape activates at no more than
   `floor(phi(n) log(6)/(2 log n))` primes `p >= n^2`.

   Scope caveat: this is per shape.  It does not prove pair-coprimality or bound
   how many shapes activate at a single prime.

3. **MACHINE-VERIFIED:** exact cyclotomic replay.

   Script:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_char0_classification.py
   ```

   Replay:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_char0_classification.py
   ```

   Expected digest:

   ```text
   CHAR0_CLASSIFICATION_PASS
   ```

   Coverage: exact `Z[X]/Phi_n` enumeration for
   `n = 3,4,5,6,7,8,9,10,12,15,18,21,24,30,36,48,96`; exact modular activation
   checks for the banked `n=96` shapes at `p=9601,13249,18433`.

4. **PROVED / MACHINE-VERIFIED:** h=2 trade count reduces to additive energy,
   with corrected midpoint accounting.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_STEPANOV_RECONSTRUCTION.md
   ```

   Script:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
   ```

   Replay:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
   ```

   Expected digest:

   ```text
   H2_ENERGY_REPLAY_PASS
   ```

   Content: for odd characteristic,
   `E(H)=8T_2+4M_2+2n^2-n`, hence `T_2 <= E(H)/8`.  Exact rows through
   `n=512` at `q~n^2` and `q~n^3` pass, with
   `max E(H)/n^2.5 = 0.8906`.  The script also verifies the arithmetic
   consequence of the explicit external Cochrane--Pinner constant
   `C=16/3`: if imported, `T_2 <= (2/3)n^2.5 < n^3` for all `n >= 1`.

5. **OPEN:** in-house explicit HBK/Konyagin h=2 energy theorem.

   Current banked frontier:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_STEPANOV_RECONSTRUCTION.md
   ```

   The auxiliary-polynomial parameter arithmetic is checked for the
   single-shift ansatz through `n=512`, but two proof steps remain:
   nonvanishing/rank for the constructed polynomial, and the dyadic
   level-set/higher-convolution upgrade from single-shift intersection bounds
   to `E(H) <= C n^2.5` with explicit `C`.

   Source trail for the explicit external constant:

   ```text
   https://www.math.ksu.edu/~cvs/cochrane_hart_pinner_spencer-waring_subgroup.pdf
   ```

   Cochrane--Hart--Pinner--Spencer record the Cochrane--Pinner explicit
   theorem `E(A) <= (16/3)|A|^2.5` for `|A| < p^(2/3)`.

6. **VERIFIED-AT-ROWS:** Terminal C pair-coprimality pilot on observed
   `n=96` h=3 shapes.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COPRIMALITY_PILOT.md
   ```

   Script:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
   ```

   Replay:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
   ```

   Expected digest:

   ```text
   H3_PAIR_COPRIMALITY_PILOT_PASS
   ```

   Result: over the seven actual prime `n=96`, `q=1 mod 96` rows in the banked
   ladder, three activated non-toral shapes appear and each activates at exactly
   one prime.  No repeated activation was found among observed shapes.  This is
   evidence only; the all-shapes `n=96` Modal census remains open.

## Catches

- The first checker version did repeated Sympy polynomial reductions inside the
  pair loop and had to be interrupted after about 60 seconds.  The replay was
  repaired by caching residues of `X^e mod Phi_n` and grouping triples by exact
  `(e1,e2)` signature before pairing.  The final replay runs in about two
  seconds locally.

- Terminal B initially used the false identity `E(H)=8T_2+2n^2-n`, omitting
  diagonal/nondiagonal midpoint collisions.  The direct ordered-energy bucket
  check failed at `(n,q)=(16,257)`, forcing the corrected identity
  `E(H)=8T_2+4M_2+2n^2-n`.

- The inherited `f3_h3_dichotomy_modal.py` `QS` list contains `23233` and
  `27649`, which are `1 mod 96` but composite.  The Terminal C pilot filters to
  the seven actual prime rows.

## Terminal Status

Terminal A reached.  A1/A2 are bypassed by a direct proof stronger than the
planned Conway-Jones/Mann enumeration.  A3 is covered by the exact replay
through `n=96` and by exact checks of the banked norm-gate shapes.  A4 is the
norm-gate corollary with explicit constants.  A5 is banked as node-candidate
statement/proof files.

Remaining frontier: pair-coprimality/on-average activation is still open
Terminal C.  The new theorem says finite non-toral h=3 interiors cannot be
persistent char-zero families; it does not yet bound simultaneous activated
shape counts at one prime.

Terminal B status: partial, not complete.  The h=2 stratum remains closed only
by external HBK/Konyagin/Cochrane--Pinner input until the two missing explicit
Stepanov/HBK steps above are proved in-house.

Terminal C status: started, not complete.  The observed-shape pilot supports
pair-coprimality, but the full `n=96` all-shapes census and exceptional-list
task remains open.
