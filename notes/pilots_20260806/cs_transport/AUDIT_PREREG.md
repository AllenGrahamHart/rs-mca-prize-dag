# Ideal/Galois multiplicity transport audit - preregistration

- **date:** 2026-08-06
- **candidate supplier:** `rate_half_crossing_ideal_galois_multiplicity_exclusion`
- **candidate consumers:** `rate_half_list_adjacent_crossing` and
  `u2c_giant_tnull_dichotomy`, as evidence only
- **source:** `notes/pilots_20260806/es_coprimality/PROOFS.md`, THEOREM CS

## Purpose

Independently replay the exact algebra behind THEOREM CS before minting a
PROVED DAG supplier.  The computation is audit support, not a proof.  The
paper proof must independently establish the ideal divisibility, the exact
archimedean norm ceiling, and the finite stratum recursion.

## Registered checks

1. Compute cyclotomic norms by an independent multiplication-matrix
   determinant, not by the source pilot's resultant implementation.
2. Exhaustively check
   `N(x_1)^2 <= (|S|-a_{n/2}(S))^(n/2)` for every subset at `n=8`, and
   for every three-element subset at `n=16`.
3. In `F_9` (`n=8,p=3`), `F_17` (`n=16,p=17`), and `F_49`
   (`n=16,p=7`), enumerate the registered subset-size bands.  Whenever
   the first `w-1` moments vanish but the characteristic-zero `x_1` is
   nonzero, verify
   `p^|Z_w^odd| | N(x_1)` and the resulting exact integer ceiling.
4. Require a fixture that rejects the strengthened exponent
   `p^(|Z_w^odd|+1)` and a nonzero fixture attaining equality in the
   archimedean ceiling.
5. Independently bisect the near-256-bit benchmark threshold and recover
   `170,752,922,588`; also demonstrate that the threshold changes at
   128 bits and that the bound is vacuous through the bracket at 64 bits.
6. Verify the exact power-of-two tower coefficient identity, and require
   an arbitrary-window fixture that rejects the old floor-free shortcut.

## Falsifiers

Any failed divisibility, norm ceiling, threshold boundary, or tower identity
blocks promotion.  Absence of the two tamper witnesses also blocks promotion,
because it would leave the checker unable to distinguish the stated theorem
from natural stronger but false variants.

## Resource ceiling

One Modal container, one CPU, 1 GiB RAM, a 120-second function timeout, and a
90-second subprocess timeout.  No retries, no parallel workers, and no local
enumeration.  Expected cost is below `$0.01`.

```text
./tools/ramguard modal -- modal run \
  notes/pilots_20260806/cs_transport/cs_independent_audit_modal.py
```

## Promotion rule

Mint the supplier as PROVED only if all registered checks and both tamper
self-tests pass, and the written audit confirms that:

- the theorem is rowwise in the base characteristic `p`;
- `71.16%` is only the near-256-bit characteristic benchmark;
- arbitrary windows use exact per-stratum inequalities; and
- no consumer target changes status merely from this supplier.
