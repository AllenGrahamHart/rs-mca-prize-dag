# OVERNIGHT LOG 2026-07-08

## 2026-07-08 initial entry

Stage: Terminal A, h=3 char-zero classification.

Banked pose: `critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_CLASSIFICATION.md`.

Current route: direct unit-circle proof using `e2 = product * conjugate(e1)`,
which should classify all distinct char-zero h=3 trades as toral `mu_3`
coset pairs. Exact checker written but not yet replayed.

Next step: run `f3_h3_char0_classification.py`, fix any exact-check failures,
then commit the banked theorem/checker.

## 2026-07-08 Terminal A core replay

Stage: A1--A4.

Banked claim: direct unit-circle proof classifies all char-zero h=3 trades as
toral `mu_3` coset pairs. Exact checker replays in about two seconds and verifies
rows through `n=96`; the `n=96` row gives exactly `496 = binom(32,2)` char-zero
trades, all toral. The three banked finite-field norm-gate shapes at primes
`9601`, `13249`, and `18433` have both obstructions nonzero in `Q(zeta_96)` and
both obstructions zero modulo their activating prime.

Catch: the first checker implementation did repeated Sympy reductions inside
the pair loop and had to be interrupted after 60 seconds. The replay was repaired
by caching `X^e mod Phi_n` residues and grouping triples by exact `(e1,e2)`
signature before pairing.

Next step: add the requested node-candidate statement/proof files and commit the
stage.

## 2026-07-08 Terminal B partial replay

Stage: Terminal B, in-house explicit h=2.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_STEPANOV_RECONSTRUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
```

Digest: `H2_ENERGY_REPLAY_PASS`.

Banked claim: exact h=2 F3 trade count is controlled by additive energy via
`T_2 <= E(H)/8`.  The exact energy decomposition is
`E(H)=8T_2+4M_2+2n^2-n`, where `M_2` is the diagonal/nondiagonal midpoint
count.  Rows `n=16,32,64,128,256,512` at the first primes `q=1 mod n` above
`n^2` and `n^3` replay exactly; max measured `E(H)/n^2.5 = 0.8906`.

Catch: the first written identity omitted midpoint collisions and claimed
`E(H)=8T_2+2n^2-n`.  The direct ordered-energy check falsified it immediately
at `(n,q)=(16,257)`.  The script and note now include the `4M_2` term.

Stepanov status: coefficient/degree arithmetic for a single-shift auxiliary
polynomial is checked through `n=512` with positive slack.  The missing in-house
steps are still the nonvanishing/rank lemma and the energy-level upgrade from
single-shift intersection bounds to `E(H) <= C n^2.5`.

External explicit-constant source located: Cochrane--Hart--Pinner--Spencer
record the Cochrane--Pinner explicit constant
`E(A) <= (16/3)|A|^2.5` for `|A| < p^(2/3)`; if accepted as an external import,
this gives `T_2 <= (2/3)n^2.5 < n^3` for every `n >= 1`.  This sharpens the
existing import but does not satisfy Terminal B's in-house proof requirement.

Next step: either reconstruct the HBK/Konyagin dyadic level-set upgrade with
explicit constants, or bank that exact step as the Terminal B blocker and move
to Terminal C per the brief's >90-minute rule.

## 2026-07-08 Terminal C pilot

Stage: Terminal C, pair-coprimality on observed h=3 shapes.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COPRIMALITY_PILOT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py
```

Digest: `H3_PAIR_COPRIMALITY_PILOT_PASS`.

Result: among the seven actual prime `n=96`, `q=1 mod 96` rows in the banked
ladder, exactly three non-toral activated shapes appear, and each activates at
exactly one prime (`9601`, `13249`, `18433`).  The remaining prime rows
`26113`, `36097`, `42337`, `46273` are empty.  No repeated activation was found
among observed shapes.  Stronger exact norm-gcd check: the three observed
shapes have common obstruction norm factors `{1153,9601}`, `{97,13249}`, and
`{18433}` respectively, so each has exactly one activation prime in the
threshold regime `p = 1 mod 96`, `p >= 96^2`.

Catch: the inherited `f3_h3_dichotomy_modal.py` `QS` list includes two composite
entries, `23233` and `27649`; the pilot filters to actual prime rows.

Next step: full Terminal C census is still open — enumerate all normalized
`n=96` shapes on Modal/shards and compute the empirical coprimality rate plus
exceptional list.

## 2026-07-08 Terminal C random exact-norm sample

Stage: Terminal C, random exact resultant sample over normalized `n=96` shapes.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COPRIMALITY_RANDOM_SAMPLE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_random_modal.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_random_modal.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-bYVtU4rZenbBi4NAsSmUEc
```

Result: `2000` unique random normalized shapes, `22` with a shared rational
threshold norm prime, `0` with an actual simultaneous primitive-root activation
prime.  Digest: `H3_RANDOM_ACTIVATION_SAMPLE_PASS`.

Catch/refinement: naive rational norm-coprimality is too strong; Terminal C
should be formulated at the prime-ideal/common-root level.  The observed-shape
gcds remain harmless because their extra common rational factors are
sub-threshold, but random shapes can share threshold rational factors without
activating.

## 2026-07-08 Terminal C activation ladder

Stage: Terminal C, refined common-root activation ladder.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ACTIVATION_LADDER_MODAL.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_ladder_modal.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_ladder_modal.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-r767UbDESh7BN6TaDEC7S6
```

Result: first `64` actual primes `q = 1 mod 96` above `96^2`; `71` activated
non-toral shape orbits; `71` distinct shapes; `0` repeats.  Digest:
`H3_ACTIVATION_LADDER_PASS`.

Interpretation: strong evidence for the refined common-root formulation of
Terminal C.  The all-shapes norm census remains open, but a direct finite-field
activation ladder found no repeated activated shape.

## 2026-07-08 Terminal C affine-orbit count

Stage: Terminal C, exact sizing of the full `n=96` all-shapes census.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_AFFINE_ORBIT_COUNT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_orbit_count_modal.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_orbit_count_modal.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-XVtUnVPEitz3WXSczroC2x
```

Result: Burnside count over the affine/Galois group
`x -> u*x+s`, `u in (Z/96Z)^*`, gives `3,135,641` orbit representatives:

```text
GROUP_ORDER 3072
FIXED_TOTAL 9632689152
AFFINE_ORBITS 3135641
H3_AFFINE_ORBIT_COUNT_PASS
```

Interpretation: the full Terminal C `n=96` census is finite and Modal-feasible
after quotienting by the symmetries that preserve obstruction norms and
common-root activation.  It remains open, but it is now sized exactly.
