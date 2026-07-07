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
norm-gate shapes activate only modulo their selected primes.

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

## Catches

- The first checker version did repeated Sympy polynomial reductions inside the
  pair loop and had to be interrupted after about 60 seconds.  The replay was
  repaired by caching residues of `X^e mod Phi_n` and grouping triples by exact
  `(e1,e2)` signature before pairing.  The final replay runs in about two
  seconds locally.

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

