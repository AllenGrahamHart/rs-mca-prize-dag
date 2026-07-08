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

## 2026-07-08 Terminal C core `(0,1,7)` complete census

Stage: Terminal C, sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_017_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_017_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_017_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,7 --tag 017
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_017_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-ivTrtjSvUzRQIcBlHFnrNj
```

Result: complete scan of `A=[0,1,7]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_017_CENSUS_DONE
H3_CORE_017_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 7 | 37, 43, 54]   p=12289
[0, 1, 7 | 42, 61, 67]   p=12289
[0, 1, 7 | 77, 82, 93]   p=15361
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 6 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,8)` complete census

Stage: Terminal C, seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_018_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_018_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_018_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,8 --tag 018
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_018_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-DhkJpeEA9CfQaMA5s6V3yA
```

Result: complete scan of `A=[0,1,8]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1187 activation_exceptions=3
H3_CORE_018_CENSUS_DONE
H3_CORE_018_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 8 | 33, 73, 87]   p=31393
[0, 1, 8 | 35, 42, 55]   p=18913
[0, 1, 8 | 50, 51, 55]   p=18913
```

Rates: rational norm exception `0.9147%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 7 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,9)` complete census

Stage: Terminal C, eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_019_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_019_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_019_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,9 --tag 019
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_019_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-viSQQ5DxQjZn740e04Gikr
```

Result: complete scan of `A=[0,1,9]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1373 activation_exceptions=5
H3_CORE_019_CENSUS_DONE
H3_CORE_019_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 9 | 4, 29, 44]    p=37633
[0, 1, 9 | 10, 25, 81]   p=37633
[0, 1, 9 | 33, 58, 73]   p=37633
[0, 1, 9 | 46, 64, 80]   p=239233
[0, 1, 9 | 52, 77, 92]   p=37633
```

Rates: rational norm exception `1.0581%`; actual common-root activation
`0.0039%`.  The complete core-by-core program now has 8 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,10)` complete census

Stage: Terminal C, ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0110_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0110_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0110_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,10 --tag 0110
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0110_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-t5ffzZ4kRJDIuXb2AK9vw6
```

Result: complete scan of `A=[0,1,10]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1111 activation_exceptions=2
H3_CORE_0110_CENSUS_DONE
H3_CORE_0110_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 10 | 3, 4, 71]     p=10273
[0, 1, 10 | 28, 38, 59]   p=20929
```

Rates: rational norm exception `0.8562%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 9 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,11)` complete census

Stage: Terminal C, tenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0111_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0111_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0111_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,11 --tag 0111
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0111_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2qqugdb6ewZPnrvSMvpZtQ
```

Result: complete scan of `A=[0,1,11]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1110 activation_exceptions=3
H3_CORE_0111_CENSUS_DONE
H3_CORE_0111_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 11 | 26, 37, 60]   p=30817
[0, 1, 11 | 46, 47, 60]   p=30817
[0, 1, 11 | 75, 89, 95]   p=69313
```

Rates: rational norm exception `0.8554%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 10 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,12)` complete census

Stage: Terminal C, eleventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0112_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0112_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0112_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,12 --tag 0112
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0112_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-T5sO4psGiVnF7vIBCA7zRy
```

Result: complete scan of `A=[0,1,12]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1268 activation_exceptions=2
H3_CORE_0112_CENSUS_DONE
H3_CORE_0112_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 12 | 3, 8, 85]    p=19777
[0, 1, 12 | 9, 90, 92]   p=10273
```

Rates: rational norm exception `0.9771%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 11 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,13)` complete census

Stage: Terminal C, twelfth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0113_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0113_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0113_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,13 --tag 0113
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0113_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-iglT3LcjTyETCCvdc2B2da
```

Result: complete scan of `A=[0,1,13]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1289 activation_exceptions=1
H3_CORE_0113_CENSUS_DONE
H3_CORE_0113_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 13 | 16, 25, 62]   p=10177
```

Rates: rational norm exception `0.9933%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 12 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,14)` complete census

Stage: Terminal C, thirteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0114_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0114_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0114_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,14 --tag 0114
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0114_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-GjthTWoEoVjMCcGQdbpFnI
```

Result: complete scan of `A=[0,1,14]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1218 activation_exceptions=2
H3_CORE_0114_CENSUS_DONE
H3_CORE_0114_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 14 | 23, 36, 61]   p=30817
[0, 1, 14 | 50, 51, 61]   p=30817
```

Rates: rational norm exception `0.9386%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 13 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,15)` complete census

Stage: Terminal C, fourteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0115_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,15 --tag 0115
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-QYA4kM3GHwcFB12xBgkENm
```

Result: complete scan of `A=[0,1,15]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1117 activation_exceptions=2
H3_CORE_0115_CENSUS_DONE
H3_CORE_0115_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 15 | 21, 35, 62]   p=67777
[0, 1, 15 | 46, 47, 64]   p=10177
```

Rates: rational norm exception `0.8608%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 14 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,16)` complete census

Stage: Terminal C, fifteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0116_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,16 --tag 0116
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-gbPBZHbKK07l5tfI7uDjzC
```

Result: complete scan of `A=[0,1,16]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1275 activation_exceptions=7
H3_CORE_0116_CENSUS_DONE
H3_CORE_0116_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 16 | 8, 9, 41]     p=37633
[0, 1, 16 | 8, 41, 57]    p=1416317953
[0, 1, 16 | 8, 57, 89]    p=37633
[0, 1, 16 | 9, 41, 56]    p=37633
[0, 1, 16 | 9, 56, 89]    p=1416317953
[0, 1, 16 | 24, 52, 75]   p=20161
[0, 1, 16 | 56, 57, 89]   p=37633
```

Rates: rational norm exception `0.9825%`; actual common-root activation
`0.0054%`.  The complete core-by-core program now has 15 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,17)` complete census

Stage: Terminal C, sixteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0117_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0117_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0117_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,17 --tag 0117
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0117_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-HRey2hkBgCXpFD9HrdV09V
```

Result: complete scan of `A=[0,1,17]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1228 activation_exceptions=4
H3_CORE_0117_CENSUS_DONE
H3_CORE_0117_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 17 | 5, 25, 86]    p=32833
[0, 1, 17 | 10, 45, 63]   p=15361
[0, 1, 17 | 15, 74, 93]   p=15361
[0, 1, 17 | 22, 41, 85]   p=32833
```

Rates: rational norm exception `0.9463%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 16 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,18)` complete census

Stage: Terminal C, seventeenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0118_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,18 --tag 0118
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-kVG2QhlE4iVbbvcScuiu1S
```

Result: complete scan of `A=[0,1,18]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1135 activation_exceptions=4
H3_CORE_0118_CENSUS_DONE
H3_CORE_0118_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 18 | 6, 31, 84]    p=27361
[0, 1, 18 | 12, 30, 67]   p=27361
[0, 1, 18 | 15, 32, 65]   p=10177
[0, 1, 18 | 50, 51, 65]   p=10177
```

Rates: rational norm exception `0.8747%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 17 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,19)` complete census

Stage: Terminal C, eighteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0119_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0119_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0119_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,19 --tag 0119
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0119_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-AzWigAMCB8naG0Cxh8iVJw
```

Result: complete scan of `A=[0,1,19]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0119_CENSUS_DONE
H3_CORE_0119_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 19 | 7, 30, 85]    p=27361
[0, 1, 19 | 10, 29, 68]   p=40897
[0, 1, 19 | 13, 31, 66]   p=12289
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 18 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,20)` complete census

Stage: Terminal C, nineteenth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0120_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0120_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0120_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,20 --tag 0120
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0120_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lSW5XQbONVthGbIwDmg4zm
```

Result: complete scan of `A=[0,1,20]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
H3_CORE_0120_CENSUS_DONE
H3_CORE_0120_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 20 | 11, 30, 67]   p=18913
[0, 1, 20 | 16, 51, 95]   p=18913
[0, 1, 20 | 17, 34, 69]   p=18913
```

Rates: rational norm exception `0.8492%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 19 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,21)` complete census

Stage: Terminal C, twentieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0121_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0121_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0121_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,21 --tag 0121
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0121_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lXlVK4pYXPkVDMzXNfiS8O
```

Result: complete scan of `A=[0,1,21]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1232 activation_exceptions=4
H3_CORE_0121_CENSUS_DONE
H3_CORE_0121_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 21 | 9, 12, 56]    p=37633
[0, 1, 21 | 9, 29, 68]    p=37633
[0, 1, 21 | 13, 28, 89]   p=37633
[0, 1, 21 | 13, 40, 84]   p=37633
```

Rates: rational norm exception `0.9494%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 20 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,22)` complete census

Stage: Terminal C, twenty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0122_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0122_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0122_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,22 --tag 0122
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0122_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-X5UKanPVxyBP6ytshTKMTs
```

Result: complete scan of `A=[0,1,22]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1105 activation_exceptions=3
H3_CORE_0122_CENSUS_DONE
H3_CORE_0122_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 22 | 16, 52, 89]   p=10273
[0, 1, 22 | 18, 27, 92]   p=20929
[0, 1, 22 | 25, 38, 61]   p=10177
```

Rates: rational norm exception `0.8515%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 21 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,23)` complete census

Stage: Terminal C, twenty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0123_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0123_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0123_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,23 --tag 0123
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0123_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-3K3R4Gzr5eU15jaqN0jeGS
```

Result: complete scan of `A=[0,1,23]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
H3_CORE_0123_CENSUS_DONE
H3_CORE_0123_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 23 | 40, 59, 76]   p=19777
[0, 1, 23 | 43, 53, 59]   p=20353
```

Rates: rational norm exception `0.9332%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 22 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,24)` complete census

Stage: Terminal C, twenty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0124_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0124_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0124_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,24 --tag 0124
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0124_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-FslAe2mSjjOhtU9yf9eatF
```

Result: complete scan of `A=[0,1,24]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0124_CENSUS_DONE
H3_CORE_0124_CENSUS_CHECK_PASS
```

Activation structure:

```text
All 67 activation exceptions contain the anchor exponent 49.
```

Rates: rational norm exception `0.9425%`; actual common-root activation
`0.0516%`.  The complete core-by-core program now has 23 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,25)` complete census

Stage: Terminal C, twenty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0125_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0125_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0125_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,25 --tag 0125
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0125_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-oMy6XhOwKlCPZqmeODi0xr
```

Result: complete scan of `A=[0,1,25]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0125_CENSUS_DONE
H3_CORE_0125_CENSUS_CHECK_PASS
```

Activation structure:

```text
All 67 activation exceptions contain the anchor exponent 48.
```

Rates: rational norm exception `0.9425%`; actual common-root activation
`0.0516%`.  The complete core-by-core program now has 24 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,26)` complete census

Stage: Terminal C, twenty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0126_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0126_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0126_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,26 --tag 0126
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0126_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-ALiyWDso8TdNM66PmjSUTN
```

Result: complete scan of `A=[0,1,26]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
H3_CORE_0126_CENSUS_DONE
H3_CORE_0126_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 26 | 20, 36, 78]   p=20353
[0, 1, 26 | 36, 41, 77]   p=19777
```

Rates: rational norm exception `0.9332%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 25 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,27)` complete census

Stage: Terminal C, twenty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0127_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0127_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0127_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,27 --tag 0127
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0127_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-RS3zathUFmyuMPmghKRhMl
```

Result: complete scan of `A=[0,1,27]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1093 activation_exceptions=1
H3_CORE_0127_CENSUS_DONE
H3_CORE_0127_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 27 | 5, 22, 31]   p=20929
```

Note: Modal printed a worker-preemption notice after the digest/app completion;
the local checker pins the banked JSON.

Rates: rational norm exception `0.8423%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 26 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,28)` complete census

Stage: Terminal C, twenty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0128_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0128_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0128_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,28 --tag 0128
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0128_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-dMh7BB3hvXLwpewk2qh8E8
```

Result: complete scan of `A=[0,1,28]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1245 activation_exceptions=6
H3_CORE_0128_CENSUS_DONE
H3_CORE_0128_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 28 | 8, 21, 36]    p=37633
[0, 1, 28 | 20, 77, 88]   p=37633
[0, 1, 28 | 27, 36, 52]   p=20161
[0, 1, 28 | 36, 57, 61]   p=37633
[0, 1, 28 | 37, 41, 88]   p=37633
[0, 1, 28 | 72, 83, 88]   p=32833
```

Rates: rational norm exception `0.9594%`; actual common-root activation
`0.0046%`.  The complete core-by-core program now has 27 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,29)` complete census

Stage: Terminal C, twenty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0129_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0129_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0129_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,29 --tag 0129
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0129_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-H658oDpv2tX5tZQJyuBPx7
```

Result: complete scan of `A=[0,1,29]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=3
H3_CORE_0129_CENSUS_DONE
H3_CORE_0129_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 29 | 3, 4, 90]     p=10273
[0, 1, 29 | 18, 33, 44]   p=18433
[0, 1, 29 | 19, 78, 86]   p=18913
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 28 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,30)` complete census

Stage: Terminal C, twenty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0130_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0130_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0130_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,30 --tag 0130
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0130_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-W5D6GAutVYeBTfKLIkx5Yt
```

Result: complete scan of `A=[0,1,30]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0130_CENSUS_DONE
H3_CORE_0130_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 30 | 12, 19, 42]   p=27361
[0, 1, 30 | 18, 79, 84]   p=12289
[0, 1, 30 | 20, 77, 87]   p=40897
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 29 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,31)` complete census

Stage: Terminal C, thirtieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0131_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0131_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0131_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,31 --tag 0131
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0131_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Z7A1xv8N38whCXWCBuPZeO
```

Result: complete scan of `A=[0,1,31]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1070 activation_exceptions=4
H3_CORE_0131_CENSUS_DONE
H3_CORE_0131_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 31 | 13, 18, 43]   p=27361
[0, 1, 31 | 17, 80, 82]   p=10177
[0, 1, 31 | 19, 78, 85]   p=27361
[0, 1, 31 | 46, 47, 80]   p=10177
```

Rates: rational norm exception `0.8246%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 30 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,32)` complete census

Stage: Terminal C, thirty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0132_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0132_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0132_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,32 --tag 0132
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0132_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-GeIRA1BYqRhxdmEr9ZMpMM
```

Result: complete scan of `A=[0,1,32]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=957 activation_exceptions=14
H3_CORE_0132_CENSUS_DONE
H3_CORE_0132_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 32 | 2, 33, 81]    p=10177
[0, 1, 32 | 2, 36, 50]    p=20929
[0, 1, 32 | 5, 42, 53]    p=40897
[0, 1, 32 | 8, 36, 84]    p=37633
[0, 1, 32 | 11, 54, 59]   p=207073
[0, 1, 32 | 12, 56, 60]   p=37633
[0, 1, 32 | 17, 65, 66]   p=10177
[0, 1, 32 | 18, 66, 68]   p=20929
[0, 1, 32 | 20, 42, 90]   p=67777
[0, 1, 32 | 20, 68, 72]   p=37633
[0, 1, 32 | 21, 69, 74]   p=40897
[0, 1, 32 | 24, 44, 92]   p=37633
[0, 1, 32 | 26, 74, 84]   p=67777
[0, 1, 32 | 27, 75, 86]   p=207073
```

Rates: rational norm exception `0.7375%`; actual common-root activation
`0.0108%`.  The complete core-by-core program now has 31 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,33)` complete census

Stage: Terminal C, thirty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0133_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0133_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0133_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,33 --tag 0133
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0133_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-0ZhwSTOA3QarhPpd5aIabM
```

Result: complete scan of `A=[0,1,33]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1074 activation_exceptions=32
H3_CORE_0133_CENSUS_DONE
H3_CORE_0133_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
32 actual activations; full list pinned in
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0133_CENSUS.md
```

Rates: rational norm exception `0.8276%`; actual common-root activation
`0.0247%`.  The complete core-by-core program now has 32 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,34)` complete census

Stage: Terminal C, thirty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0134_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0134_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0134_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,34 --tag 0134
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0134_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-bdLYftsAaMbhvkXj2B5F5w
```

Result: complete scan of `A=[0,1,34]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1224 activation_exceptions=4
H3_CORE_0134_CENSUS_DONE
H3_CORE_0134_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 34 | 2, 37, 89]    p=17377
[0, 1, 34 | 14, 76, 83]   p=67777
[0, 1, 34 | 26, 30, 76]   p=10369
[0, 1, 34 | 50, 51, 81]   p=10177
```

Rates: rational norm exception `0.9432%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 33 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,35)` complete census

Stage: Terminal C, thirty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0135_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0135_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0135_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,35 --tag 0135
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0135_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-t7NWDOeRiONcpI0pZC0XaZ
```

Result: complete scan of `A=[0,1,35]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1110 activation_exceptions=3
H3_CORE_0135_CENSUS_DONE
H3_CORE_0135_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 35 | 13, 74, 84]   p=30817
[0, 1, 35 | 33, 43, 61]   p=69313
[0, 1, 35 | 46, 47, 84]   p=30817
```

Rates: rational norm exception `0.8554%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 34 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,36)` complete census

Stage: Terminal C, thirty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0136_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0136_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0136_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,36 --tag 0136
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0136_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-beSLjyAlXasPFculCxrxVy
```

Result: complete scan of `A=[0,1,36]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1268 activation_exceptions=2
H3_CORE_0136_CENSUS_DONE
H3_CORE_0136_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 36 | 9, 54, 80]    p=10273
[0, 1, 36 | 27, 37, 44]   p=19777
```

Rates: rational norm exception `0.9771%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 35 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,37)` complete census

Stage: Terminal C, thirty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0137_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0137_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0137_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,37 --tag 0137
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0137_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-19yt6dzFPaxWliqIvUcw1r
```

Result: complete scan of `A=[0,1,37]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1289 activation_exceptions=1
H3_CORE_0137_CENSUS_DONE
H3_CORE_0137_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 37 | 16, 61, 86]   p=10177
```

Rates: rational norm exception `0.9933%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 36 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,38)` complete census

Stage: Terminal C, thirty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0138_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0138_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0138_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,38 --tag 0138
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0138_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lM2vW23zv8oazc679qGRA2
```

Result: complete scan of `A=[0,1,38]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1218 activation_exceptions=2
H3_CORE_0138_CENSUS_DONE
H3_CORE_0138_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 38 | 12, 71, 85]   p=30817
[0, 1, 38 | 50, 51, 85]   p=30817
```

Rates: rational norm exception `0.9386%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 37 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,39)` complete census

Stage: Terminal C, thirty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0139_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0139_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0139_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,39 --tag 0139
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0139_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2aFmqRHGsMhy3RLpCFRnib
```

Result: complete scan of `A=[0,1,39]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1194 activation_exceptions=1
H3_CORE_0139_CENSUS_DONE
H3_CORE_0139_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 39 | 11, 69, 86]   p=20929
```

Rates: rational norm exception `0.9201%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 38 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,40)` complete census

Stage: Terminal C, thirty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0140_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0140_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0140_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,40 --tag 0140
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0140_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-UzEqMZGr9ooEzamZIsK8Ir
```

Result: complete scan of `A=[0,1,40]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1381 activation_exceptions=4
H3_CORE_0140_CENSUS_DONE
H3_CORE_0140_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 40 | 16, 24, 39]   p=37633
[0, 1, 40 | 21, 29, 44]   p=37633
[0, 1, 40 | 64, 72, 87]   p=37633
[0, 1, 40 | 69, 77, 92]   p=37633
```

Rates: rational norm exception `1.0642%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 39 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,41)` complete census

Stage: Terminal C, fortieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0141_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0141_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0141_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,41 --tag 0141
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0141_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-WsCIoFqO1BeO2QDbOjZNT8
```

Result: complete scan of `A=[0,1,41]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1187 activation_exceptions=3
H3_CORE_0141_CENSUS_DONE
H3_CORE_0141_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 41 | 7, 62, 90]    p=18913
[0, 1, 41 | 24, 26, 32]   p=31393
[0, 1, 41 | 46, 47, 90]   p=18913
```

Rates: rational norm exception `0.9147%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 40 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,42)` complete census

Stage: Terminal C, forty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0142_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0142_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0142_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,42 --tag 0142
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0142_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-7yZ6b03mPlo6ClweVzZj2F
```

Result: complete scan of `A=[0,1,42]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0142_CENSUS_DONE
H3_CORE_0142_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 42 | 3, 70, 86]    p=15361
[0, 1, 42 | 6, 60, 91]    p=12289
[0, 1, 42 | 7, 36, 78]    p=12289
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 41 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,43)` complete census

Stage: Terminal C, forty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0143_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0143_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0143_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,43 --tag 0143
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0143_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-BThyLk2Jtw1kPW9C6CiQ4z
```

Result: complete scan of `A=[0,1,43]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0143_CENSUS_DONE
H3_CORE_0143_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 43 | 6, 37, 79]    p=12289
[0, 1, 43 | 7, 61, 90]    p=27361
[0, 1, 43 | 46, 47, 92]   p=40897
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 42 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,44)` complete census

Stage: Terminal C, forty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0144_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0144_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0144_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,44 --tag 0144
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0144_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Np4wuTycLOSpTKjypvWit9
```

Result: complete scan of `A=[0,1,44]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=3
H3_CORE_0144_CENSUS_DONE
H3_CORE_0144_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 44 | 7, 69, 76]    p=18433
[0, 1, 44 | 31, 34, 77]   p=10273
[0, 1, 44 | 50, 51, 91]   p=18913
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 43 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,45)` complete census

Stage: Terminal C, forty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0145_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0145_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0145_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,45 --tag 0145
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0145_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-qADxYHfoxrjMig5PadXICz
```

Result: complete scan of `A=[0,1,45]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=7
H3_CORE_0145_CENSUS_DONE
H3_CORE_0145_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 45 | 4, 41, 85]    p=37633
[0, 1, 45 | 5, 57, 92]    p=37633
[0, 1, 45 | 8, 57, 84]    p=37633
[0, 1, 45 | 12, 85, 88]   p=37633
[0, 1, 45 | 13, 44, 77]   p=207073
[0, 1, 45 | 38, 53, 56]   p=15937
[0, 1, 45 | 46, 47, 94]   p=207073
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0054%`.  The complete core-by-core program now has 44 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,46)` complete census

Stage: Terminal C, forty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0146_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0146_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0146_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,46 --tag 0146
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0146_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Fo3oDk68PB7xwhSY4mt5iT
```

Result: complete scan of `A=[0,1,46]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0146_CENSUS_DONE
H3_CORE_0146_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 46 | 3, 44, 90]    p=67777
[0, 1, 46 | 4, 45, 65]    p=18433
[0, 1, 46 | 50, 51, 93]   p=40897
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 45 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,47)` complete census

Stage: Terminal C, forty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0147_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0147_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0147_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,47 --tag 0147
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0147_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-I5QWoyZCnfZ2Fu4CHLIoep
```

Result: complete scan of `A=[0,1,47]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1152 activation_exceptions=0
H3_CORE_0147_CENSUS_DONE
H3_CORE_0147_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
none
```

Rates: rational norm exception `0.8878%`; actual common-root activation
`0.0000%`.  The complete core-by-core program now has 46 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,48)` complete census

Stage: Terminal C, forty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0148_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0148_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0148_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,48 --tag 0148
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0148_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-UjM6442S2oqGQ7MdXXLf9u
```

Result: complete scan of `A=[0,1,48]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1067 activation_exceptions=37
H3_CORE_0148_CENSUS_DONE
H3_CORE_0148_CENSUS_CHECK_PASS
```

Activation exceptions: see `F3_H3_CORE_0148_CENSUS.md` for the full
37-row list.  The dominant visible subfamilies contain the anchor pairs
`31,63` or `47,*`, with several reciprocal prime pairs.

Rates: rational norm exception `0.8222%`; actual common-root activation
`0.0285%`.  The complete core-by-core program now has 47 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,49)` complete census

Stage: Terminal C, forty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0149_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0149_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0149_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,49 --tag 0149
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0149_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2Veov6xX4JdbgHqLM1tV0s
```

Result: complete scan of `A=[0,1,49]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1067 activation_exceptions=37
H3_CORE_0149_CENSUS_DONE
H3_CORE_0149_CENSUS_CHECK_PASS
```

Activation exceptions: see `F3_H3_CORE_0149_CENSUS.md` for the full
37-row list.  The dominant visible subfamilies contain the anchor pairs
`34,66` or `50,*`, mirroring the adjacent `0148` exceptional slice.

Rates: rational norm exception `0.8222%`; actual common-root activation
`0.0285%`.  The complete core-by-core program now has 48 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,50)` complete census

Stage: Terminal C, forty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0150_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0150_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0150_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,50 --tag 0150
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0150_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-p7sSI4lJ0lmbpK4RCwJiLV
```

Result: complete scan of `A=[0,1,50]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1152 activation_exceptions=0
H3_CORE_0150_CENSUS_DONE
H3_CORE_0150_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
none
```

Rates: rational norm exception `0.8878%`; actual common-root activation
`0.0000%`.  The complete core-by-core program now has 49 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,51)` complete census

Stage: Terminal C, fiftieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0151_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0151_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0151_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,51 --tag 0151
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0151_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-zgu6zGAAkGBGE3MUCtmFgt
```

Result: complete scan of `A=[0,1,51]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0151_CENSUS_DONE
H3_CORE_0151_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 51 | 4, 46, 47]    p=40897
[0, 1, 51 | 7, 53, 94]    p=67777
[0, 1, 51 | 32, 52, 93]   p=18433
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 50 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,52)` complete census

Stage: Terminal C, fifty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0152_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0152_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0152_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,52 --tag 0152
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0152_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lz7VK8drBwBeyCF9YFtsSz
```

Result: complete scan of `A=[0,1,52]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=7
H3_CORE_0152_CENSUS_DONE
H3_CORE_0152_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 52 | 3, 50, 51]    p=207073
[0, 1, 52 | 5, 40, 92]    p=37633
[0, 1, 52 | 9, 12, 85]    p=37633
[0, 1, 52 | 12, 56, 93]   p=37633
[0, 1, 52 | 13, 40, 89]   p=37633
[0, 1, 52 | 20, 53, 84]   p=207073
[0, 1, 52 | 41, 44, 59]   p=15937
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0054%`.  The complete core-by-core program now has 51 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,53)` complete census

Stage: Terminal C, fifty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0153_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0153_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0153_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,53 --tag 0153
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0153_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JLJWt4tOj3i6oPrCKCMpV4
```

Result: complete scan of `A=[0,1,53]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=3
H3_CORE_0153_CENSUS_DONE
H3_CORE_0153_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 53 | 6, 46, 47]    p=18913
[0, 1, 53 | 20, 63, 66]   p=10273
[0, 1, 53 | 21, 28, 90]   p=18433
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 52 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,54)` complete census

Stage: Terminal C, fifty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0154_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0154_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0154_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,54 --tag 0154
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0154_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-RlkHDNw0g3bywV37n331IH
```

Result: complete scan of `A=[0,1,54]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0154_CENSUS_DONE
H3_CORE_0154_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 54 | 5, 50, 51]    p=40897
[0, 1, 54 | 7, 36, 90]    p=27361
[0, 1, 54 | 18, 60, 91]   p=12289
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 53 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,55)` complete census

Stage: Terminal C, fifty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0155_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0155_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0155_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,55 --tag 0155
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0155_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-pDoY9Su4T9E35WUdBM15XB
```

Result: complete scan of `A=[0,1,55]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0155_CENSUS_DONE
H3_CORE_0155_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 55 | 6, 37, 91]    p=12289
[0, 1, 55 | 11, 27, 94]   p=15361
[0, 1, 55 | 19, 61, 90]   p=12289
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 54 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,56)` complete census

Stage: Terminal C, fifty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0156_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0156_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0156_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,56 --tag 0156
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0156_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JKCcvdXdqUzuMV9bG4HMan
```

Result: complete scan of `A=[0,1,56]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1187 activation_exceptions=3
H3_CORE_0156_CENSUS_DONE
H3_CORE_0156_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 56 | 7, 35, 90]    p=18913
[0, 1, 56 | 7, 50, 51]    p=18913
[0, 1, 56 | 65, 71, 73]   p=31393
```

Rates: rational norm exception `0.9147%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 55 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,57)` complete census

Stage: Terminal C, fifty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0157_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0157_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0157_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,57 --tag 0157
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0157_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-AoFOWVF7au5eXK7uvTFKvc
```

Result: complete scan of `A=[0,1,57]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1381 activation_exceptions=4
H3_CORE_0157_CENSUS_DONE
H3_CORE_0157_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 57 | 5, 20, 28]    p=37633
[0, 1, 57 | 10, 25, 33]   p=37633
[0, 1, 57 | 53, 68, 76]   p=37633
[0, 1, 57 | 58, 73, 81]   p=37633
```

Rates: rational norm exception `1.0642%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 56 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,58)` complete census

Stage: Terminal C, fifty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0158_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0158_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0158_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,58 --tag 0158
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0158_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-FwiznN2rjMXsb4TwByPEoD
```

Result: complete scan of `A=[0,1,58]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1194 activation_exceptions=1
H3_CORE_0158_CENSUS_DONE
H3_CORE_0158_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 58 | 11, 28, 86]   p=20929
```

Rates: rational norm exception `0.9201%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 57 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,59)` complete census

Stage: Terminal C, fifty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0159_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0159_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0159_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,59 --tag 0159
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0159_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-FLebmtETEwaNlPlR9Z2Lbp
```

Result: complete scan of `A=[0,1,59]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1218 activation_exceptions=2
H3_CORE_0159_CENSUS_DONE
H3_CORE_0159_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 59 | 12, 26, 85]   p=30817
[0, 1, 59 | 12, 46, 47]   p=30817
```

Rates: rational norm exception `0.9386%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 58 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,60)` complete census

Stage: Terminal C, fifty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0160_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0160_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0160_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,60 --tag 0160
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0160_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-hrOuJOgzx7ULWxhG0K9v5g
```

Result: complete scan of `A=[0,1,60]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1289 activation_exceptions=1
H3_CORE_0160_CENSUS_DONE
H3_CORE_0160_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 60 | 11, 36, 81]   p=10177
```

Rates: rational norm exception `0.9933%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 59 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,61)` complete census

Stage: Terminal C, sixtieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0161_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0161_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0161_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,61 --tag 0161
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0161_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-4LbNmZQR0YwEADWDJVxq9n
```

Result: complete scan of `A=[0,1,61]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1268 activation_exceptions=2
H3_CORE_0161_CENSUS_DONE
H3_CORE_0161_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 61 | 17, 43, 88]   p=10273
[0, 1, 61 | 53, 60, 70]   p=19777
```

Rates: rational norm exception `0.9771%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 60 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,62)` complete census

Stage: Terminal C, sixty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0162_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0162_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0162_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,62 --tag 0162
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0162_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-y2Y0MnUItYd0Gp86z9QBdo
```

Result: complete scan of `A=[0,1,62]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1110 activation_exceptions=3
H3_CORE_0162_CENSUS_DONE
H3_CORE_0162_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 62 | 13, 23, 84]   p=30817
[0, 1, 62 | 13, 50, 51]   p=30817
[0, 1, 62 | 36, 54, 64]   p=69313
```

Rates: rational norm exception `0.8554%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 61 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,63)` complete census

Stage: Terminal C, sixty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0163_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0163_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0163_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,63 --tag 0163
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0163_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-NB7n91mFhCl9So8YdPQNWz
```

Result: complete scan of `A=[0,1,63]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1224 activation_exceptions=4
H3_CORE_0163_CENSUS_DONE
H3_CORE_0163_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 63 | 8, 60, 95]    p=17377
[0, 1, 63 | 14, 21, 83]   p=67777
[0, 1, 63 | 16, 46, 47]   p=10177
[0, 1, 63 | 21, 67, 71]   p=10369
```

Rates: rational norm exception `0.9432%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 62 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,64)` complete census

Stage: Terminal C, sixty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0164_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0164_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0164_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,64 --tag 0164
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0164_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JcoMjUD1N4iwoCQnKj80sY
```

Result: complete scan of `A=[0,1,64]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1074 activation_exceptions=32
H3_CORE_0164_CENSUS_DONE
H3_CORE_0164_CENSUS_CHECK_PASS
```

Activation exceptions: `32`, listed in
`critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0164_CENSUS.md`.
Many involve the exponent `80`, marking this as another dense structural slice.

Rates: rational norm exception `0.8276%`; actual common-root activation
`0.0247%`.  The complete core-by-core program now has 63 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,65)` complete census

Stage: Terminal C, sixty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0165_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0165_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0165_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,65 --tag 0165
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0165_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-X347WzdJkDL9npXkLMuJNt
```

Result: complete scan of `A=[0,1,65]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=957 activation_exceptions=14
H3_CORE_0165_CENSUS_DONE
H3_CORE_0165_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 65 | 5, 53, 73]    p=37633
[0, 1, 65 | 7, 55, 77]    p=67777
[0, 1, 65 | 11, 22, 70]   p=207073
[0, 1, 65 | 13, 23, 71]   p=67777
[0, 1, 65 | 13, 61, 89]   p=37633
[0, 1, 65 | 16, 64, 95]   p=10177
[0, 1, 65 | 23, 28, 76]   p=40897
[0, 1, 65 | 25, 29, 77]   p=37633
[0, 1, 65 | 29, 31, 79]   p=20929
[0, 1, 65 | 31, 32, 80]   p=10177
[0, 1, 65 | 37, 41, 85]   p=37633
[0, 1, 65 | 38, 43, 86]   p=207073
[0, 1, 65 | 44, 55, 92]   p=40897
[0, 1, 65 | 47, 61, 95]   p=20929
```

Rates: rational norm exception `0.7375%`; actual common-root activation
`0.0108%`.  The complete core-by-core program now has 64 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,66)` complete census

Stage: Terminal C, sixty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0166_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0166_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0166_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,66 --tag 0166
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0166_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-pqsEVoLKLtIsbD5mjZOFK5
```

Result: complete scan of `A=[0,1,66]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1070 activation_exceptions=4
H3_CORE_0166_CENSUS_DONE
H3_CORE_0166_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 66 | 12, 19, 78]   p=27361
[0, 1, 66 | 15, 17, 80]   p=10177
[0, 1, 66 | 17, 50, 51]   p=10177
[0, 1, 66 | 54, 79, 84]   p=27361
```

Rates: rational norm exception `0.8246%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 65 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,67)` complete census

Stage: Terminal C, sixty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0167_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0167_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0167_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,67 --tag 0167
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0167_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JX5ORTOuv59OJ8YGR8rYSJ
```

Result: complete scan of `A=[0,1,67]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0167_CENSUS_DONE
H3_CORE_0167_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 67 | 10, 20, 77]   p=40897
[0, 1, 67 | 13, 18, 79]   p=12289
[0, 1, 67 | 55, 78, 85]   p=27361
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 66 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,68)` complete census

Stage: Terminal C, sixty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0168_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0168_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0168_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,68 --tag 0168
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0168_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-6TpmxzkzreAip6GSCZTAfI
```

Result: complete scan of `A=[0,1,68]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=3
H3_CORE_0168_CENSUS_DONE
H3_CORE_0168_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 68 | 7, 93, 94]    p=10273
[0, 1, 68 | 11, 19, 78]   p=18913
[0, 1, 68 | 53, 64, 79]   p=18433
```

Rates: rational norm exception `0.8577%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 67 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,69)` complete census

Stage: Terminal C, sixty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0169_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0169_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0169_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,69 --tag 0169
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0169_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-RAHh5r5e7ez7NP0QVJRG3i
```

Result: complete scan of `A=[0,1,69]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1245 activation_exceptions=6
H3_CORE_0169_CENSUS_DONE
H3_CORE_0169_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 69 | 9, 14, 25]    p=32833
[0, 1, 69 | 9, 20, 77]    p=37633
[0, 1, 69 | 9, 56, 60]    p=37633
[0, 1, 69 | 36, 40, 61]   p=37633
[0, 1, 69 | 45, 61, 70]   p=20161
[0, 1, 69 | 61, 76, 89]   p=37633
```

Rates: rational norm exception `0.9594%`; actual common-root activation
`0.0046%`.  The complete core-by-core program now has 68 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,70)` complete census

Stage: Terminal C, sixty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0170_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0170_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0170_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,70 --tag 0170
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0170_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-7LjMSPNVQjM6KM2HvFJ2Ja
```

Result: complete scan of `A=[0,1,70]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1093 activation_exceptions=1
H3_CORE_0170_CENSUS_DONE
H3_CORE_0170_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 70 | 66, 75, 92]   p=20929
```

Rates: rational norm exception `0.8423%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 69 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,71)` complete census

Stage: Terminal C, seventieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0171_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0171_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0171_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,71 --tag 0171
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0171_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-qXzgTIKRvdKkIq1A4Qq15k
```

Result: complete scan of `A=[0,1,71]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
H3_CORE_0171_CENSUS_DONE
H3_CORE_0171_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 71 | 19, 61, 77]   p=20353
[0, 1, 71 | 20, 56, 61]   p=19777
```

Rates: rational norm exception `0.9332%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 70 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,72)` complete census

Stage: Terminal C, seventy-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0172_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0172_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0172_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,72 --tag 0172
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0172_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-8OvoNOPEwf71s8xrY8ooiw
```

Result: complete scan of `A=[0,1,72]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0172_CENSUS_DONE
H3_CORE_0172_CENSUS_CHECK_PASS
```

Activation exceptions: 67 total, nearly all containing anchor exponent `49`.

Rates: rational norm exception `0.9425%`; actual common-root activation
`0.0516%`.  The complete core-by-core program now has 71 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,73)` complete census

Stage: Terminal C, seventy-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0173_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0173_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0173_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,73 --tag 0173
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0173_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lBMaGlQqKmCcuj2c4TjQDy
```

Result: complete scan of `A=[0,1,73]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0173_CENSUS_DONE
H3_CORE_0173_CENSUS_CHECK_PASS
```

Activation exceptions: 67 total, nearly all containing anchor exponent `48`.

Rates: rational norm exception `0.9425%`; actual common-root activation
`0.0516%`.  The complete core-by-core program now has 72 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,74)` complete census

Stage: Terminal C, seventy-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0174_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0174_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0174_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,74 --tag 0174
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0174_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-x4to18ThkmvihlQ80tiP6g
```

Result: complete scan of `A=[0,1,74]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
H3_CORE_0174_CENSUS_DONE
H3_CORE_0174_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 74 | 21, 38, 57]   p=19777
[0, 1, 74 | 38, 44, 54]   p=20353
```

Rates: rational norm exception `0.9332%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 73 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,75)` complete census

Stage: Terminal C, seventy-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0175_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0175_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0175_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,75 --tag 0175
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0175_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-OC0QxUPzznXjtjzmmQtb32
```

Result: complete scan of `A=[0,1,75]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1105 activation_exceptions=3
H3_CORE_0175_CENSUS_DONE
H3_CORE_0175_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 75 | 5, 70, 79]   p=20929
[0, 1, 75 | 8, 45, 81]   p=10273
[0, 1, 75 | 36, 59, 72]   p=10177
```

Rates: rational norm exception `0.8515%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 74 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,76)` complete census

Stage: Terminal C, seventy-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0176_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0176_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0176_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,76 --tag 0176
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0176_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-fq2CI6hgqgXArcydxZlrra
```

Result: complete scan of `A=[0,1,76]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1232 activation_exceptions=4
H3_CORE_0176_CENSUS_DONE
H3_CORE_0176_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 76 | 8, 69, 84]   p=37633
[0, 1, 76 | 13, 57, 84]   p=37633
[0, 1, 76 | 29, 68, 88]   p=37633
[0, 1, 76 | 41, 85, 88]   p=37633
```

Rates: rational norm exception `0.9494%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 75 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,77)` complete census

Stage: Terminal C, seventy-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0177_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0177_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0177_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,77 --tag 0177
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0177_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-OrZxQ07KUv5LlAcM7IQOXT
```

Result: complete scan of `A=[0,1,77]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
H3_CORE_0177_CENSUS_DONE
H3_CORE_0177_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 77 | 2, 46, 81]   p=18913
[0, 1, 77 | 28, 63, 80]   p=18913
[0, 1, 77 | 30, 67, 86]   p=18913
```

Rates: rational norm exception `0.8492%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 76 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,78)` complete census

Stage: Terminal C, seventy-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0178_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0178_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0178_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,78 --tag 0178
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0178_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-xjLXXJFBD67CskrC8CT4Z7
```

Result: complete scan of `A=[0,1,78]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0178_CENSUS_DONE
H3_CORE_0178_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 78 | 12, 67, 90]   p=27361
[0, 1, 78 | 29, 68, 87]   p=40897
[0, 1, 78 | 31, 66, 84]   p=12289
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 77 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,79)` complete census

Stage: Terminal C, seventy-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0179_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0179_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0179_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,79 --tag 0179
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0179_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-k0UU8lOxS5D8Ogh7ZDUebp
```

Result: complete scan of `A=[0,1,79]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1135 activation_exceptions=4
H3_CORE_0179_CENSUS_DONE
H3_CORE_0179_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 79 | 13, 66, 91]   p=27361
[0, 1, 79 | 30, 67, 85]   p=27361
[0, 1, 79 | 32, 46, 47]   p=10177
[0, 1, 79 | 32, 65, 82]   p=10177
```

Rates: rational norm exception `0.8747%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 78 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,80)` complete census

Stage: Terminal C, seventy-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0180_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0180_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0180_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,80 --tag 0180
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0180_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-M9WLAe4bgMnPvL1rOpWyXJ
```

Result: complete scan of `A=[0,1,80]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1228 activation_exceptions=4
H3_CORE_0180_CENSUS_DONE
H3_CORE_0180_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 80 | 4, 23, 82]   p=15361
[0, 1, 80 | 11, 72, 92]   p=32833
[0, 1, 80 | 12, 56, 75]   p=32833
[0, 1, 80 | 34, 52, 87]   p=15361
```

Rates: rational norm exception `0.9463%`; actual common-root activation
`0.0031%`.  The complete core-by-core program now has 79 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,81)` complete census

Stage: Terminal C, eightieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0181_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0181_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0181_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,81 --tag 0181
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0181_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JqfdOMUBzJaLErGLog9yep
```

Result: complete scan of `A=[0,1,81]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1275 activation_exceptions=7
H3_CORE_0181_CENSUS_DONE
H3_CORE_0181_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 81 | 8, 40, 41]   p=37633
[0, 1, 81 | 8, 40, 89]   p=37633
[0, 1, 81 | 8, 41, 88]   p=1416317953
[0, 1, 81 | 22, 45, 73]   p=20161
[0, 1, 81 | 40, 56, 89]   p=1416317953
[0, 1, 81 | 41, 56, 88]   p=37633
[0, 1, 81 | 56, 88, 89]   p=37633
```

Rates: rational norm exception `0.9825%`; actual common-root activation
`0.0054%`.  The complete core-by-core program now has 80 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,82)` complete census

Stage: Terminal C, eighty-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0182_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0182_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0182_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,82 --tag 0182
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0182_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-i2xKaFl2b3GNa9m9451TVR
```

Result: complete scan of `A=[0,1,82]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1117 activation_exceptions=2
H3_CORE_0182_CENSUS_DONE
H3_CORE_0182_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 82 | 33, 50, 51]   p=10177
[0, 1, 82 | 35, 62, 76]   p=67777
```

Rates: rational norm exception `0.8608%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 81 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,83)` complete census

Stage: Terminal C, eighty-second complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0183_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0183_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0183_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,83 --tag 0183
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0183_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-g6fzHa5Vn3lqrriOybwT4u
```

Result: complete scan of `A=[0,1,83]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1218 activation_exceptions=2
H3_CORE_0183_CENSUS_DONE
H3_CORE_0183_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 83 | 36, 46, 47]   p=30817
[0, 1, 83 | 36, 61, 74]   p=30817
```

Rates: rational norm exception `0.9386%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 82 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,84)` complete census

Stage: Terminal C, eighty-third complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0184_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0184_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0184_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,84 --tag 0184
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0184_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-amnz1D170zFOm8U52JYc7j
```

Result: complete scan of `A=[0,1,84]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1289 activation_exceptions=1
H3_CORE_0184_CENSUS_DONE
H3_CORE_0184_CENSUS_CHECK_PASS
```

Activation exception:

```text
[0, 1, 84 | 35, 72, 81]   p=10177
```

Rates: rational norm exception `0.9933%`; actual common-root activation
`0.0008%`.  The complete core-by-core program now has 83 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,85)` complete census

Stage: Terminal C, eighty-fourth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0185_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0185_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0185_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,85 --tag 0185
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0185_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-qolccCUtS8bPJCp3nEceZn
```

Result: complete scan of `A=[0,1,85]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1268 activation_exceptions=2
H3_CORE_0185_CENSUS_DONE
H3_CORE_0185_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 85 | 5, 7, 88]   p=10273
[0, 1, 85 | 12, 89, 94]   p=19777
```

Rates: rational norm exception `0.9771%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 84 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,86)` complete census

Stage: Terminal C, eighty-fifth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0186_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0186_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0186_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,86 --tag 0186
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0186_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-vOnbX8aXTCQxP4nFvhe608
```

Result: complete scan of `A=[0,1,86]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1110 activation_exceptions=3
H3_CORE_0186_CENSUS_DONE
H3_CORE_0186_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 86 | 2, 8, 22]   p=69313
[0, 1, 86 | 37, 50, 51]   p=30817
[0, 1, 86 | 37, 60, 71]   p=30817
```

Rates: rational norm exception `0.8554%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 85 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,87)` complete census

Stage: Terminal C, eighty-sixth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0187_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0187_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0187_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,87 --tag 0187
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0187_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-q1p2pNvCIDqcePjuek85mA
```

Result: complete scan of `A=[0,1,87]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1111 activation_exceptions=2
H3_CORE_0187_CENSUS_DONE
H3_CORE_0187_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 87 | 26, 93, 94]   p=10273
[0, 1, 87 | 38, 59, 69]   p=20929
```

Rates: rational norm exception `0.8562%`; actual common-root activation
`0.0015%`.  The complete core-by-core program now has 86 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,88)` complete census

Stage: Terminal C, eighty-seventh complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0188_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0188_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0188_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,88 --tag 0188
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0188_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-0jimzWo4eIvNesRyzYSr8q
```

Result: complete scan of `A=[0,1,88]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1373 activation_exceptions=5
H3_CORE_0188_CENSUS_DONE
H3_CORE_0188_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 88 | 5, 20, 45]   p=37633
[0, 1, 88 | 16, 72, 87]   p=37633
[0, 1, 88 | 17, 33, 51]   p=239233
[0, 1, 88 | 24, 39, 64]   p=37633
[0, 1, 88 | 53, 68, 93]   p=37633
```

Rates: rational norm exception `1.0581%`; actual common-root activation
`0.0039%`.  The complete core-by-core program now has 87 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,89)` complete census

Stage: Terminal C, eighty-eighth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0189_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0189_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0189_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,89 --tag 0189
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0189_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-XyRiWUKjMITZvPU3XPtExp
```

Result: complete scan of `A=[0,1,89]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1187 activation_exceptions=3
H3_CORE_0189_CENSUS_DONE
H3_CORE_0189_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 89 | 10, 24, 64]   p=31393
[0, 1, 89 | 42, 46, 47]   p=18913
[0, 1, 89 | 42, 55, 62]   p=18913
```

Rates: rational norm exception `0.9147%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 88 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,90)` complete census

Stage: Terminal C, eighty-ninth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0190_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0190_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0190_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,90 --tag 0190
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0190_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-K94FGlqfZdCa1ybMkHfcwA
```

Result: complete scan of `A=[0,1,90]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0190_CENSUS_DONE
H3_CORE_0190_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 90 | 4, 15, 20]   p=15361
[0, 1, 90 | 30, 36, 55]   p=12289
[0, 1, 90 | 43, 54, 60]   p=12289
```

Rates: rational norm exception `0.8523%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 89 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,91)` complete census

Stage: Terminal C, ninetieth complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0191_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0191_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0191_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,91 --tag 0191
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0191_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-zRIDZE37aG5vsCehwJucJa
```

Result: complete scan of `A=[0,1,91]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0191_CENSUS_DONE
H3_CORE_0191_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 91 | 31, 37, 54]   p=12289
[0, 1, 91 | 42, 55, 61]   p=27361
[0, 1, 91 | 44, 46, 47]   p=40897
```

Rates: rational norm exception `0.8654%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has 90 of 91 core types
scanned.

## 2026-07-08 Terminal C core `(0,1,92)` complete census

Stage: Terminal C, ninety-first complete core-orbit slice.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0192_CENSUS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0192_census_results.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0192_census_check.py
```

Replay:

```bash
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,92 --tag 0192
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0192_census_check.py
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-OWUB50mCPs2Fd7woOljfP7
```

Result: complete scan of `A=[0,1,92]`, all `B` disjoint triples:

```text
TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
H3_CORE_0192_CENSUS_DONE
H3_CORE_0192_CENSUS_CHECK_PASS
```

Activation exceptions:

```text
[0, 1, 92 | 43, 50, 51]   p=18913
[0, 1, 92 | 53, 70, 81]   p=18913
[0, 1, 92 | 59, 76, 87]   p=18913
```

Rates: rational norm exception `0.8492%`; actual common-root activation
`0.0023%`.  The complete core-by-core program now has all 91 of 91 core types
scanned.

## 2026-07-08 Terminal C all-core aggregate

Stage: Terminal C, complete aggregate of the 91 core-orbit slices.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ALL_CORE_CENSUS_SUMMARY.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.json
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.py
```

Result:

```text
TOTAL core_types=91 oriented_shapes=11808706 norm_exceptions=106250 activation_exceptions=720
RATES norm=0.8998% activation=0.0061%
H3_ALL_CORE_CENSUS_SUMMARY_DONE
```

Interpretation: the complete oriented core-slice census is aggregated, with
the full 720-entry activation-exception list written to JSON.  This does not
claim the Burnside-deduplicated unordered pair-orbit rate; that is a separate
accounting layer if the consumer asks for it.

## 2026-07-08 TERMINAL-COMPLETE: Terminal C oriented core-slice census

Terminal C is complete for the scoped computational deliverable:

```text
an exact computational census over all 91 n=96 h=3 core-orbit slices,
with empirical rational-norm and actual common-root activation rates plus
the complete oriented activation-exception list.
```

Banked terminal artifact:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ALL_CORE_CENSUS_SUMMARY.md
```

Replay digest:

```text
H3_ALL_CORE_CENSUS_SUMMARY_DONE
```

Scope caveat: this terminal completion is for the oriented core-slice program.
Burnside-deduplicated unordered pair-orbit accounting is explicitly separated
and not claimed.

Next queue item: re-enter Terminal B, because the in-house explicit h=2
Stepanov/HBK energy proof remains the only non-complete terminal after A and C.

## 2026-07-08 Terminal B re-entry: h=2 level-set reduction

Stage: Terminal B, missing B2 energy-level upgrade.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_LEVEL_SET_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_levelset_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_levelset_replay.py
```

Result:

```text
max coset_l2 / n^1.5 = 0.6406
max E(H) / n^2.5 = 0.8906
H2_LEVEL_SET_REPLAY_PASS
```

Claim banked: for a multiplicative subgroup `H <= F_p^*`, if `r_C` is the
common shifted-intersection count on a multiplicative coset `C=sH`, then
`E(H) = n^2 + n * sum_C r_C^2`.  Therefore the missing HBK/Konyagin upgrade is
exactly the explicit L2 estimate `sum_C r_C^2 <= C' n^(3/2)`, not just a
single-shift maximum bound.  The replay grid runs through `n=2048`; the largest
observed L2 ratio is still the smallest row `n=16`, and the `n=2048` rows are
already down to `0.0629` (`q~n^2`) and `0.0442` (`q~n^3`).

## 2026-07-08 Terminal B: HBK conditional compiler

Stage: Terminal B, reduction of B2 to the rich-coset Stepanov lemma.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_HBK_CONDITIONAL_COMPILER.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
```

Digest: `H2_HBK_CONDITIONAL_COMPILER_PASS`.

Compiler statement:

```text
R(U) <= K(h|U|)^(2/3) for every coset set U
=> sum_C r_C^2 <= 5(K^2+K)h^(3/2)
=> E(H) <= (1+5(K^2+K))h^(5/2).
```

Then-open core: prove the rich-coset Stepanov lemma in-house with an explicit
`K`.  This is discharged in the following Terminal B completion entry.

## 2026-07-08 TERMINAL-COMPLETE: Terminal B explicit h=2 energy theorem

Stage: Terminal B, rich-coset Stepanov proof.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_RICH_COSET_STEPANOV.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
```

Digests:

```text
H2_RICH_COSET_STEPANOV_PASS
H2_HBK_CONDITIONAL_COMPILER_PASS
```

Claim banked: the rich-coset Stepanov lemma is proved in-house with
`K=129`, and the dyadic compiler gives

```text
E(H) <= 83851 h^(5/2)
```

for `H <= F_p^*`, `h <= p^(2/3)`.

Caveat: the constant is conservative.  It proves the h=2 floor from this route
alone only for `h > 7030990201/64`; the banked ladder rows below this pass
exactly, but a universal finite-midrange certificate or sharper constant is a
separate optimization task.  This completes Terminal B's explicit in-house
energy theorem; A and C were already complete, so the next queue item is the
brief's bonus queue.

## 2026-07-08 Bonus queue: h=4/h=5 reduction status

Stage: bonus item (i), h=4/h=5 emptiness route.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H4_H5_BONUS_REDUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digest: `H4_H5_BONUS_REDUCTION_PASS`.

Claim banked: h=4 already has the proved DAG dichotomy
`h4_terminal_dichotomy` (antipodal quotient pullback or top-level sparse
norm-gate, no hidden third mechanism), and the h-uniform x83 square-shift gate
reduces h=5 over `n=2^s` to p-specific norm-gate certificates.  Existing row
evidence keeps its positive control (`n=16,h=4,p=17` has 60 nontoral trades)
and verifies zero h=4/h=5 primitive residue in the q>=n^2 test rows.  Remaining
work: the h=5 no-primitive theorem itself, as a symbolic norm-gate exclusion or
per-row certificate family.

Update: h=5 now has a complete compiled `n=32` multirow certificate:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N32_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.json
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n32_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digests:

```text
H5_N32_MULTIROW_CERTIFICATE_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: for `n=32,h=5` and
`p in {1153,3137,12289,32801,40961,61441,65537}`, the replay checks all
`31465` anchored left subsets and `169911` right subsets and finds zero
anchored nontoral trades.  This strengthens the h=5 no-primitive evidence but
does not prove the uniform theorem.

Catch banked: while preparing larger compiled certificates, the fixed-width
signature key was found to use an unsafe 11-bit shift for primes above `2048`.
The h=8 and h=5 compiled replays now use `BITS=ceil(log2 p)` in generated C++.
Both multirow JSON artifacts were regenerated after the fix; the replay counts
are unchanged.

## 2026-07-08 Bonus queue: h=6/7/8 sweep status

Stage: bonus item (ii), h=6/7/8 ladder sweep.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H6_H8_BONUS_SWEEP.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digest: `H6_H8_BONUS_SWEEP_PASS`.

Claim banked: existing f3a1/f3a2 artifacts give 11 full h=6/h=7 q>=n^2
boundary/smooth rows with zero anchored nontoral trades and no n^3 alarm.  The
three h=8 rows currently banked are zero only in checked slices and remain
`partial=True`; they are useful evidence, not certificates.  Next h=8 action:
shard-complete anchor certificates or x83 square-shift norm-gate keys.

Update: the smallest h=8 partial row is now upgraded by a complete compiled
anchored MITM certificate:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H8_N32_FULL_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_full_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_full_certificate.json
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_full_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digests:

```text
H8_N32_FULL_CERTIFICATE_PASS
H6_H8_BONUS_SWEEP_PASS
```

Result: `boundary_n32_h8_p1153_FULL` is now complete with `3` paid toral
anchored trades and `0` anchored nontoral trades over all `2629575` left
subsets and `7888725` right subsets.  Follow-up multirow replay extends the
same complete certificate to boundary primes `p=3137,12289` and smooth primes
`p=40961,61441,65537`:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n32_multirow_certificate.json
```

Digest: `H8_N32_MULTIROW_CERTIFICATE_PASS`.

Remaining h=8 partials are the two `n=64` rows.

## 2026-07-08 Bonus queue: h=3 per-row accident Stepanov pose

Stage: bonus item (iii), pose the h=3 per-row accident bound.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PER_ROW_ACCIDENT_STEPANOV_POSE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Digest: `H3_PER_ROW_ACCIDENT_POSE_PASS`.

Pose banked: define `A_3(n,p)` as the number of non-toral activated h=3
dilation-shape orbits at a fixed row.  The target theorem
`A_3(n,p) <= Cn` for `p=1 mod n`, `p>=n^2` would compile to
`T_3 < n^3` from `n>=17` already for `C=16`.  The note records the
hyperbola/Stepanov ansatz as a multi-Delta rich-value theorem for shifted
subgroup product incidences.

## 2026-07-08 Bonus queue continuation: h=5 n=64 certificates

Stage: bonus item (i), h=4/h=5 emptiness evidence extension.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N64_MULTIROW_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.json
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n64_multirow_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digests:

```text
H5_N64_MULTIROW_CERTIFICATE_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: complete anchored certificates at `n=64,h=5` for
`p=4289,12289,40961,65537,262337`.  Each row checks `595665` anchored
left subsets and `7028847` right subsets, with zero anchored nontoral trades
and no `n^3` alarm.  The single-prime timing gate `p=4289` ran in under
4 seconds and the full five-prime replay ran in under 18 seconds, with peak
RSS below 90 MB.  This strengthens finite-row h=5 no-primitive evidence; no
uniform h=5 theorem is claimed.

## 2026-07-08 Bonus queue continuation: h=5 n=96 boundary certificate

Stage: bonus item (i), h=4/h=5 emptiness evidence extension.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N96_BOUNDARY_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n96_boundary_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n96_boundary_certificate.json
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n96_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digests:

```text
H5_N96_BOUNDARY_CERTIFICATE_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: complete anchored certificate at `n=96,h=5,p=9601`.  It checks
`3183545` anchored left subsets and `57940519` right subsets, with zero
anchored nontoral trades and no `n^3` alarm.  The replay stayed inside the
60-second local cap (`48.70s`) with peak RSS about `152 MB`.  This is the
largest h=5 complete finite-row certificate banked so far; no uniform theorem
is claimed.

## 2026-07-08 Bonus queue continuation: h=5 n=128 Modal boundary certificate

Stage: bonus item (i), h=4/h=5 emptiness evidence extension.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H5_N128_BOUNDARY_MODAL.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_gate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_certificate.json
```

Replay:

```bash
F3_H5_N128_MODE=gate ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
F3_H5_N128_MODE=full ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digests:

```text
H5_N128_BOUNDARY_GATE_PASS
H5_N128_BOUNDARY_CERTIFICATE_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: complete Modal-sharded anchored certificate at
`n=128,h=5,p=17921`.  The heaviest-shard gate checked `13643876` right
subsets in `15.051s` with zero anchored nontoral trades.  The full 32-shard
replay checked `254231775` right subsets, with `10334625` anchored left
subsets per shard, zero anchored toral trades, zero anchored nontoral trades,
and no `n^3` alarm.  Max shard elapsed time was `17.488s`.  This extends the
h=5 finite-row zero evidence to n=128; no uniform h=5 theorem is claimed.

Catch banked: the first Modal attempt failed before computation because remote
imports mount the script at `/root`, invalidating `Path(__file__).parents[4]`.
The script now anchors local output through `F3_PRIZE_ROOT` and remote
computation no longer depends on the worktree path.

## 2026-07-08 Bonus queue continuation: h=5 n=128 extra primes

Stage: bonus item (i), h=4/h=5 emptiness evidence extension.

Banked file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_extra_primes_certificate.json
```

Replay:

```bash
F3_H5_N128_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py
```

Digests:

```text
H5_N128_EXTRA_PRIMES_CERTIFICATE_PASS
H4_H5_BONUS_REDUCTION_PASS
```

Result: six more complete Modal-sharded certificates at `n=128,h=5`:
`p=18049,18433,19073,19457,19841,20353`.  Each row checks `254231775`
right subsets with `10334625` anchored left subsets per shard, finding zero
anchored toral trades, zero anchored nontoral trades, and no `n^3` alarm.
Max shard times were `17.419s`, `14.298s`, `13.750s`, `15.603s`,
`17.424s`, and `14.759s`.  The n=128 h=5 boundary ladder now has seven
complete prime rows: `17921,18049,18433,19073,19457,19841,20353`.

## 2026-07-08 Bonus queue continuation: h=6 n=64 Modal boundary certificate

Stage: bonus item (ii), h=6/7/8 ladder sweep.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H6_N64_BOUNDARY_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.json
```

Replay:

```bash
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digests:

```text
H6_N64_BOUNDARY_CERTIFICATE_PASS
H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H6_H8_BONUS_SWEEP_PASS
```

Result: complete Modal-sharded anchored certificate at `n=64,h=6,p=4289`.
The first local compiled attempt was killed by `timeout 60s` at `60.00s` with
max RSS `86840KB`, so the row was sharded into 16 Modal tasks under the
60-second container cap.  The complete replay checks `67945521` right subsets
with `7028847` anchored left subsets per shard, finding zero anchored toral
trades, zero anchored nontoral trades, and no `n^3` alarm.  Max shard elapsed
time was `10.634s`.

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-9ZeZrlz8FyYuLIIJAq2TgD
```

## 2026-07-08 Bonus queue continuation: h=6 n=64 extra-prime falsifier sweep

Stage: bonus item (ii), h=6/7/8 ladder sweep.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/F3_H6_P4993_SQUARE_LIFT_ANALYSIS.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_p4993_square_lift_analysis.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
critical/nodes/u1_x4_direct_column_budget/notes/F3_H6_N64_BOUNDARY_CERTIFICATE.md
critical/nodes/u1_x4_direct_column_budget/notes/F3_H6_H8_BONUS_SWEEP.md
```

Replay:

```bash
F3_H6_N64_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_p4993_square_lift_analysis.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Digests:

```text
H6_N64_EXTRA_PRIMES_SWEEP_DONE
H6_N64_EXTRA_PRIMES_SWEEP_VERIFY_PASS
H6_P4993_SQUARE_LIFT_ANALYSIS_PASS
H6_H8_BONUS_SWEEP_PASS
```

Result: six additional complete Modal-sharded `n=64,h=6` rows were swept at
`p=4481,4673,4801,4993,5441,5569`.  Five rows have zero anchored nontoral
trades.  The `p=4993` row has exactly `6` anchored nontoral trades, all decoded
in the verifier, with no `n^3` alarm (`6` versus `262144`).  The follow-up
square-lift analysis proves these six witnesses are exactly the antipodal
pullbacks of the complete h=3 anchored trade set on `mu_32` at `p=4993`.
This is a useful falsifier for the crude toral-only h=6 emptiness proxy, but
not for the fully stripped primitive h=6 column.  The h=6 target should
separate paid square-lifts of h=3 norm-gate accidents from genuinely primitive
h=6 accidents.

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-OBattAeGlh1H0GoKvCs5Fo
```
