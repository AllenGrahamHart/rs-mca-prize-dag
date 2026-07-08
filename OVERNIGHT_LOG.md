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

## 2026-07-08 Terminal C affine-representative feasibility shard

Stage: Terminal C, deterministic exact resultant/common-root pass over affine
representatives.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_AFFINE_CENSUS_FEASIBILITY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_census_feasibility_modal.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_census_feasibility_modal.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Zxs2CntPQhR6CBzOeCT1U4
```

Result: deterministic slice, `4000` affine/Galois representatives,
`46` rational threshold norm exceptions, `3` actual common-root activation
exceptions:

```text
[0, 1, 2 | 3, 26, 74] activates at p=1033441
[0, 1, 2 | 3, 17, 81] activates at p=207073
[0, 1, 2 | 3, 51, 53] activates at p=13249
```

Digest: `H3_AFFINE_CENSUS_FEASIBILITY_DONE`.

Interpretation: the full Terminal C output must be a rate plus exceptional list.
The zero-exception common-root form is false on deterministic reps, but this is
exactly the kind of exceptional-list datum Terminal C asked for.

## 2026-07-08 Terminal C consecutive-core complete census

Stage: Terminal C, complete structural subfamily census.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_census_modal.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_census_modal.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-kXLMPfgavdlZF0IQFI2wXg
```

Result: complete scan of `A=[0,1,2]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1122 activation_exceptions=44
H3_CONSECUTIVE_CORE_CENSUS_DONE
```

Rates: rational norm exception `0.8646%`; actual common-root activation
`0.0339%`.  The full 44-shape activation list is banked in the node note.
Structural signal: many exceptions cluster around `[0,1,2 | 17,*,81]` and
reflected/48-shift tail patterns, with sporadic high-prime activations.

## 2026-07-08 Terminal C consecutive-core structure

Stage: Terminal C, structural classification of the complete consecutive-core
exception list.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_STRUCTURE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_structure.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_structure.py
```

Digest: `H3_CONSECUTIVE_CORE_STRUCTURE_PASS`.

Result: all 44 activation exceptions in the complete `A=[0,1,2]` slice are
covered by two simple families:

```text
{17,81} subset B                  (18 shapes)
{a,a+48} subset B for some a      (28 shapes)
overlap                           (2 shapes)
```

The affine stabilizer of `[0,1,2]`, namely `id` and `x -> 2-x`, pairs the 44
exceptions into 22 reflection orbits, and the activation prime is constant on
each orbit.

## 2026-07-08 Terminal C consecutive-core family rates

Stage: Terminal C, exact rate table for the two structural families.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_FAMILY_RATES.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_family_rates.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_family_rates.py
```

Digest: `H3_CONSECUTIVE_CORE_FAMILY_RATES_PASS`.

Result:

```text
all       :     44 / 129766 = 0.0339%
fixed     :     18 /     91 = 19.7802%
antipodal :     28 /   4095 = 0.6838%
overlap   :      2 /      2 = 100.0000%
union     :     44 /   4184 = 1.0516%
outside   :      0 / 125582 = 0.0000%
```

Interpretation: in the complete consecutive-core slice, the two structural
families are an exact activation cover and the complement is activation-free.

## 2026-07-08 Terminal C core-orbit count

Stage: Terminal C, organization of the remaining all-shapes census.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_ORBIT_COUNT.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_orbit_count.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_orbit_count.py
```

Digest: `H3_CORE_ORBIT_COUNT_PASS`.

Result: single 3-subsets of `Z/96Z` have exactly `91` affine/Galois core
orbits.  The completed consecutive-core census is the first core orbit,
represented by `(0,1,2)`, leaving 90 core types for a core-by-core full Terminal
C census.

## 2026-07-08 Terminal C core `(0,1,3)` complete census

Stage: Terminal C, second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_013_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_modal.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-PPkOFbEgdQJmer1TbRvNgV
```

Result: complete scan of `A=[0,1,3]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1224 activation_exceptions=3
H3_CORE_013_CENSUS_DONE
H3_CORE_013_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 3 | 9, 36, 84]    p=10273
[0, 1, 3 | 46, 47, 52]   p=40897
[0, 1, 3 | 46, 53, 55]   p=67777
```

Rates: rational norm exception `0.9432%`; actual common-root activation
`0.0023%`.  The second core type is much sparser than the consecutive core
`(0,1,2)`: `3` activations here versus `44` there.  The complete core-by-core
program now has 2 of 91 core types scanned.

## 2026-07-08 Terminal C core `(0,1,4)` complete census

Stage: Terminal C, third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_014_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_modal.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2l3BsQqnwrHBRX5d0uSYFg
```

Result: complete scan of `A=[0,1,4]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1142 activation_exceptions=5
H3_CORE_014_CENSUS_DONE
H3_CORE_014_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 4 | 9, 37, 60]    p=37633
[0, 1, 4 | 12, 23, 33]   p=17377
[0, 1, 4 | 40, 44, 53]   p=37633
[0, 1, 4 | 40, 61, 89]   p=37633
[0, 1, 4 | 45, 56, 60]   p=37633
```

Rates: rational norm exception `0.8800%`; actual common-root activation
`0.0039%`.  The complete core-by-core program now has 3 of 91 core types
scanned.

## 2026-07-08 Terminal C generic runner + core `(0,1,5)` complete census

Stage: Terminal C, fourth complete core-orbit slice.

New reusable runner:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
```

It accepts `--core` and `--tag`, uses the same exact resultant/common-root
logic as the banked core-specific scripts, and writes the same JSON schema.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_015_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_015_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_015_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,5 --tag 015
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_015_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2ryAMhRmAlb58PWJFKFt9U
```

Result: complete scan of `A=[0,1,5]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
H3_CORE_015_CENSUS_DONE
H3_CORE_015_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 5 | 10, 21, 38]   p=18913
[0, 1, 5 | 16, 27, 44]   p=18913
[0, 1, 5 | 46, 47, 54]   p=18913
```

Rates: rational norm exception `0.8492%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 4 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,6)` complete census

Stage: Terminal C, fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_016_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_016_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_016_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,6 --tag 016
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_016_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-wGDRlOfxcGYeiFJibnfhxD
```

Result: complete scan of `A=[0,1,6]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_016_CENSUS_DONE
H3_CORE_016_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 6 | 36, 42, 55]   p=27361
[0, 1, 6 | 43, 60, 66]   p=12289
[0, 1, 6 | 50, 51, 53]   p=40897
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 5 of 91 core types
scanned.
