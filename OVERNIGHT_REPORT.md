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
norm-gate shapes activate only modulo their selected primes.  Terminal B now
has an in-house explicit h=2 energy theorem: the rich-coset Stepanov lemma is
proved with `K=129`, and the dyadic compiler gives
`E(H) <= 83851 |H|^2.5` for `|H| <= p^(2/3)`.  This is much weaker than the
external Cochrane--Pinner constant `16/3`, but it removes the black-box import
for the additive-energy theorem.  Used alone, it gives `T_2 < n^3` only above
`n > 7030990201/64`; the banked ladder rows below this pass exactly, and a
universal finite-midrange certificate is separated as future optimization.
Terminal C has a light pilot: observed activated
`n=96` h=3 shapes do not repeat across the actual prime rows in the ladder.
A random exact-norm Modal sample refutes the naive rational norm-coprimality
form as too strong, but finds zero actual common-root activations in 2000
random normalized shapes.  A 64-prime activation ladder finds 71 activated
shape orbits and zero repeated shapes.  The full all-shapes `n=96` census has
now been sized exactly: `3,135,641` affine/Galois orbit representatives.  A
deterministic affine-representative feasibility slice found the first three
common-root activation exceptions for the eventual exceptional list.  A complete
consecutive-core subfamily census gives the first exact activation rate:
`44/129766`, and those 44 exceptions are covered by two simple structural
families whose union has zero activation-free complement outside it.  The
remaining full census can now be organized into 91 affine/Galois core types.
That core-by-core program is now complete and aggregated: across the 91
oriented slices there are `11,808,706` oriented shapes, `106,250` rational
norm exceptions, and `720` actual common-root activation exceptions, giving
activation rate `0.0061%`.  This is the oriented core-slice rate; a
Burnside-deduplicated unordered pair-orbit rate is a separate accounting layer.
The second core type, `(0,1,3)`, is also complete: it has only `3/129766`
actual common-root activation exceptions.  The third core type, `(0,1,4)`, is
complete with `5/129766` actual activations.  The fourth core type `(0,1,5)` is
complete with `3/129766` actual activations.  The fifth core type `(0,1,6)` is
complete with `3/129766` actual activations.  The sixth core type `(0,1,7)` is
complete with `3/129766` actual activations.  The seventh core type `(0,1,8)`
is complete with `3/129766` actual activations.  The eighth core type
`(0,1,9)` is complete with `5/129766` actual activations.  The ninth core type
`(0,1,10)` is complete with `2/129766` actual activations.  The tenth core type
`(0,1,11)` is complete with `3/129766` actual activations.  The eleventh core
type `(0,1,12)` is complete with `2/129766` actual activations.  The twelfth
core type `(0,1,13)` is complete with `1/129766` actual activation.  The
thirteenth core type `(0,1,14)` is complete with `2/129766` actual activations.
The fourteenth core type `(0,1,15)` is complete with `2/129766` actual
activations.  The fifteenth core type `(0,1,16)` is complete with `7/129766`
actual activations.  The sixteenth core type `(0,1,17)` is complete with
`4/129766` actual activations.  The seventeenth core type `(0,1,18)` is
complete with `4/129766` actual activations.  The eighteenth core type
`(0,1,19)` is complete with `3/129766` actual activations.  The nineteenth
core type `(0,1,20)` is complete with `3/129766` actual activations.
The twentieth core type `(0,1,21)` is complete with `4/129766` actual
activations.  The twenty-first core type `(0,1,22)` is complete with
`3/129766` actual activations.  The twenty-second core type `(0,1,23)` is
complete with `2/129766` actual activations.  The twenty-third core type
`(0,1,24)` is complete with `67/129766` actual activations, all containing
the anchor exponent `49`.  The twenty-fourth core type `(0,1,25)` is complete
with `67/129766` actual activations, all containing the anchor exponent `48`.
The twenty-fifth core type `(0,1,26)` is complete with `2/129766` actual
activations.  The twenty-sixth core type `(0,1,27)` is complete with
`1/129766` actual activation.  The twenty-seventh core type `(0,1,28)` is
complete with `6/129766` actual activations.  The twenty-eighth core type
`(0,1,29)` is complete with `3/129766` actual activations.  The twenty-ninth
core type `(0,1,30)` is complete with `3/129766` actual activations.  The
thirtieth core type `(0,1,31)` is complete with `4/129766` actual activations.
The thirty-first core type `(0,1,32)` is complete with `14/129766` actual
activations.  The thirty-second core type `(0,1,33)` is complete with
`32/129766` actual activations.  The thirty-third core type `(0,1,34)` is
complete with `4/129766` actual activations.  The thirty-fourth core type
`(0,1,35)` is complete with `3/129766` actual activations.  The thirty-fifth
core type `(0,1,36)` is complete with `2/129766` actual activations.  The
thirty-sixth core type `(0,1,37)` is complete with `1/129766` actual
activation.  The thirty-seventh core type `(0,1,38)` is complete with
`2/129766` actual activations.  The thirty-eighth core type `(0,1,39)` is
complete with `1/129766` actual activation.  The thirty-ninth core type
`(0,1,40)` is complete with `4/129766` actual activations.  The fortieth
core type `(0,1,41)` is complete with `3/129766` actual activations.  The
forty-first core type `(0,1,42)` is complete with `3/129766` actual
activations.  The forty-second core type `(0,1,43)` is complete with
`3/129766` actual activations.  The forty-third core type `(0,1,44)` is
complete with `3/129766` actual activations.  The forty-fourth core type
`(0,1,45)` is complete with `7/129766` actual activations.  The forty-fifth
core type `(0,1,46)` is complete with `3/129766` actual activations.  The
forty-sixth core type `(0,1,47)` is complete with `0/129766` actual
activations.  The forty-seventh core type `(0,1,48)` is complete with
`37/129766` actual activations.  The forty-eighth core type `(0,1,49)` is
complete with `37/129766` actual activations.  The forty-ninth core type
`(0,1,50)` is complete with `0/129766` actual activations.  The fiftieth
core type `(0,1,51)` is complete with `3/129766` actual activations.  The
fifty-first core type `(0,1,52)` is complete with `7/129766` actual
activations.  The fifty-second core type `(0,1,53)` is complete with
`3/129766` actual activations.  The fifty-third core type `(0,1,54)` is
complete with `3/129766` actual activations.  The fifty-fourth core type
`(0,1,55)` is complete with `3/129766` actual activations.  The fifty-fifth
core type `(0,1,56)` is complete with `3/129766` actual activations.  The
fifty-sixth core type `(0,1,57)` is complete with `4/129766` actual
activations.  The fifty-seventh core type `(0,1,58)` is complete with
`1/129766` actual activation.  The fifty-eighth core type `(0,1,59)` is
complete with `2/129766` actual activations.  The fifty-ninth core type
`(0,1,60)` is complete with `1/129766` actual activation.  The sixtieth
core type `(0,1,61)` is complete with `2/129766` actual activations.  The
sixty-first core type `(0,1,62)` is complete with `3/129766` actual
activations.  The sixty-second core type `(0,1,63)` is complete with
`4/129766` actual activations.  The sixty-third core type `(0,1,64)` is
complete with `32/129766` actual activations.  The sixty-fourth core type
`(0,1,65)` is complete with `14/129766` actual activations.  The sixty-fifth
core type `(0,1,66)` is complete with `4/129766` actual activations.  The
sixty-sixth core type `(0,1,67)` is complete with `3/129766` actual
activations.  The sixty-seventh core type `(0,1,68)` is complete with
`3/129766` actual activations.  The sixty-eighth core type `(0,1,69)` is
complete with `6/129766` actual activations.  The sixty-ninth core type
`(0,1,70)` is complete with `1/129766` actual activation.  The seventieth
core type `(0,1,71)` is complete with `2/129766` actual activations.  The
seventy-first core type `(0,1,72)` is complete with `67/129766` actual
activations; this is another dense anchored slice, almost entirely through
the exponent `49`.  The seventy-second core type `(0,1,73)` is complete with
`67/129766` actual activations, now anchored almost entirely at exponent `48`.
The seventy-third core type `(0,1,74)` is complete with `2/129766` actual
activations.  The seventy-fourth core type `(0,1,75)` is complete with
`3/129766` actual activations.  The seventy-fifth core type `(0,1,76)` is
complete with `4/129766` actual activations, all at `p=37633`.
The seventy-sixth core type `(0,1,77)` is complete with `3/129766` actual
activations, all at `p=18913`.  The seventy-seventh core type `(0,1,78)` is
complete with `3/129766` actual activations.
The seventy-eighth core type `(0,1,79)` is complete with `4/129766` actual
activations.  The seventy-ninth core type `(0,1,80)` is complete with
`4/129766` actual activations.  The eightieth core type `(0,1,81)` is
complete with `7/129766` actual activations, including two at `p=1416317953`.
The eighty-first core type `(0,1,82)` is complete with `2/129766` actual
activations.  The eighty-second core type `(0,1,83)` is complete with
`2/129766` actual activations, both at `p=30817`.  The eighty-third core
type `(0,1,84)` is complete with `1/129766` actual activation.
The eighty-fourth core type `(0,1,85)` is complete with `2/129766` actual
activations.  The eighty-fifth core type `(0,1,86)` is complete with
`3/129766` actual activations.

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

5. **PROVED:** in-house explicit HBK/Konyagin h=2 energy theorem.

   Files:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_STEPANOV_RECONSTRUCTION.md
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_LEVEL_SET_REDUCTION.md
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_HBK_CONDITIONAL_COMPILER.md
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_RICH_COSET_STEPANOV.md
   ```

   Replays:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_levelset_replay.py
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_hbk_conditional_compiler.py
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
   ```

   Digests:

   ```bash
   H2_ENERGY_REPLAY_PASS
   H2_LEVEL_SET_REPLAY_PASS
   H2_HBK_CONDITIONAL_COMPILER_PASS
   H2_RICH_COSET_STEPANOV_PASS
   ```

   Content: the exact h=2 trade identity gives `T_2 <= E(H)/8`; the level-set
   reduction gives `E(H)=n^2+n sum_C r_C^2`; the dyadic compiler reduces the
   L2 estimate to the rich-coset lemma; and the Stepanov proof gives
   `R(U) <= 129(h|U|)^(2/3)`.  Therefore
   `E(H) <= 83851 h^2.5` for `h <= p^(2/3)`.

   Caveat: this in-house constant is conservative.  It proves `T_2 < h^3`
   from this route alone for `h > 7030990201/64`; all banked ladder rows below
   this pass exactly, but a universal finite-midrange certificate or sharper
   constant remains separate.

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
   one prime.  No repeated activation was found among observed shapes.  Exact
   norm-gcd factors for the three observed shapes are `{1153,9601}`,
   `{97,13249}`, and `{18433}`, so each observed shape has exactly one
   activation prime in the threshold regime `p = 1 mod 96`, `p >= 96^2`.  This
   is evidence only; the all-shapes `n=96` Modal census remains open.

7. **HEURISTIC / REFINED TARGET:** Terminal C random exact-norm sample.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_PAIR_COPRIMALITY_RANDOM_SAMPLE.md
   ```

   Script:

   ```text
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

   Result: `2000` unique random normalized `n=96` shapes; `22` had a shared
   rational threshold norm prime, but `0` had an actual simultaneous
   primitive-root activation.  Digest: `H3_RANDOM_ACTIVATION_SAMPLE_PASS`.

   Consequence: the rational norm-gcd form of Terminal C is too strong.  The
   refined target is the prime-ideal/common-root condition.

8. **VERIFIED-AT-ROWS:** Terminal C 64-prime activation ladder.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_ACTIVATION_LADDER_MODAL.md
   ```

   Script:

   ```text
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

   Result: first `64` actual primes `q = 1 mod 96` above `96^2`; `71`
   activated non-toral shape orbits; `71` distinct canonical shapes; `0`
   repeated activations.  Digest: `H3_ACTIVATION_LADDER_PASS`.

9. **MACHINE-VERIFIED:** exact affine/Galois orbit count for the full
   `n=96` Terminal C census.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_AFFINE_ORBIT_COUNT.md
   ```

   Script:

   ```text
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

   Result:

   ```text
   GROUP_ORDER 3072
   FIXED_TOTAL 9632689152
   AFFINE_ORBITS 3135641
   H3_AFFINE_ORBIT_COUNT_PASS
   ```

   This is the exact number of unordered disjoint h=3 shape orbits modulo
   translation and Galois multiplication on `Z/96Z`.

10. **VERIFIED-AT-ROWS / EXCEPTIONAL-LIST SEED:** deterministic
    affine-representative resultant/common-root slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_AFFINE_CENSUS_FEASIBILITY.md
   ```

   Script:

   ```text
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

   Result:

   ```text
   TOTAL unique_reps=4000 norm_exceptions=46 activation_exceptions=3
   H3_AFFINE_CENSUS_FEASIBILITY_DONE
   ```

   Activation exceptions:

   ```text
   [0, 1, 2 | 3, 26, 74] activates at p=1033441
   [0, 1, 2 | 3, 17, 81] activates at p=207073
   [0, 1, 2 | 3, 51, 53] activates at p=13249
   ```

   Consequence: Terminal C should not be phrased as zero common-root
   exceptions.  The full deliverable is an empirical activation rate and
   exceptional list over the `3,135,641` affine/Galois representatives.

11. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete consecutive-core slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_CENSUS.md
   ```

   Script:

   ```text
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1122 activation_exceptions=44
   H3_CONSECUTIVE_CORE_CENSUS_DONE
   ```

   This completely scans the oriented slice `A=[0,1,2]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8646%`; actual common-root
   activation `0.0339%`.  The full 44-shape activation list is in the note.

12. **MACHINE-CHECKED STRUCTURE:** consecutive-core activation exceptions.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_STRUCTURE.md
   ```

   Script:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_structure.py
   ```

   Replay:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_structure.py
   ```

   Expected digest:

   ```text
   H3_CONSECUTIVE_CORE_STRUCTURE_PASS
   ```

   Result: all 44 consecutive-core activation exceptions are covered by
   `{17,81} subset B` or by an antipodal pair `{a,a+48} subset B`.  Counts:
   fixed-pair family `18`, antipodal-pair family `28`, overlap `2`.  The
   stabilizer reflection `x -> 2-x` pairs them into 22 two-element orbits with
   constant activation prime.

13. **MACHINE-CHECKED RATE TABLE:** consecutive-core structural families.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CONSECUTIVE_CORE_FAMILY_RATES.md
   ```

   Script:

   ```text
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

   The complement of the fixed-pair/antipodal union is activation-free in this
   complete slice.

14. **MACHINE-VERIFIED SIZING:** affine/Galois core-orbit count.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_ORBIT_COUNT.md
   ```

   Script:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_orbit_count.py
   ```

   Replay:

   ```bash
   python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_orbit_count.py
   ```

   Digest: `H3_CORE_ORBIT_COUNT_PASS`.

   Result: single h=3 cores in `Z/96Z` have exactly `91` affine/Galois orbits.
   The completed `(0,1,2)` consecutive-core census is one core type, leaving
   90 core types for the full Terminal C census.

15. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,3)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_013_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1224 activation_exceptions=3
   H3_CORE_013_CENSUS_DONE
   H3_CORE_013_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 3 | 9, 36, 84]    activates at p=10273
   [0, 1, 3 | 46, 47, 52]   activates at p=40897
   [0, 1, 3 | 46, 53, 55]   activates at p=67777
   ```

   This completely scans the oriented slice `A=[0,1,3]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9432%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 2 of 91 core types
   complete.

16. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,4)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_014_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1142 activation_exceptions=5
   H3_CORE_014_CENSUS_DONE
   H3_CORE_014_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 4 | 9, 37, 60]    activates at p=37633
   [0, 1, 4 | 12, 23, 33]   activates at p=17377
   [0, 1, 4 | 40, 44, 53]   activates at p=37633
   [0, 1, 4 | 40, 61, 89]   activates at p=37633
   [0, 1, 4 | 45, 56, 60]   activates at p=37633
   ```

   This completely scans the oriented slice `A=[0,1,4]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8800%`; actual common-root
   activation `0.0039%`.  The core-by-core census is now 3 of 91 core types
   complete.

17. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,5)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_015_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
   H3_CORE_015_CENSUS_DONE
   H3_CORE_015_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 5 | 10, 21, 38]   activates at p=18913
   [0, 1, 5 | 16, 27, 44]   activates at p=18913
   [0, 1, 5 | 46, 47, 54]   activates at p=18913
   ```

   This completely scans the oriented slice `A=[0,1,5]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8492%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 4 of 91 core types
   complete.

18. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,6)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_016_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
   H3_CORE_016_CENSUS_DONE
   H3_CORE_016_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 6 | 36, 42, 55]   activates at p=27361
   [0, 1, 6 | 43, 60, 66]   activates at p=12289
   [0, 1, 6 | 50, 51, 53]   activates at p=40897
   ```

   This completely scans the oriented slice `A=[0,1,6]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8654%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 5 of 91 core types
   complete.

19. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,7)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_017_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
   H3_CORE_017_CENSUS_DONE
   H3_CORE_017_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 7 | 37, 43, 54]   activates at p=12289
   [0, 1, 7 | 42, 61, 67]   activates at p=12289
   [0, 1, 7 | 77, 82, 93]   activates at p=15361
   ```

   This completely scans the oriented slice `A=[0,1,7]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8523%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 6 of 91 core types
   complete.

20. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,8)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_018_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1187 activation_exceptions=3
   H3_CORE_018_CENSUS_DONE
   H3_CORE_018_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 8 | 33, 73, 87]   activates at p=31393
   [0, 1, 8 | 35, 42, 55]   activates at p=18913
   [0, 1, 8 | 50, 51, 55]   activates at p=18913
   ```

   This completely scans the oriented slice `A=[0,1,8]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9147%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 7 of 91 core types
   complete.

21. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,9)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_019_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1373 activation_exceptions=5
   H3_CORE_019_CENSUS_DONE
   H3_CORE_019_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 9 | 4, 29, 44]    activates at p=37633
   [0, 1, 9 | 10, 25, 81]   activates at p=37633
   [0, 1, 9 | 33, 58, 73]   activates at p=37633
   [0, 1, 9 | 46, 64, 80]   activates at p=239233
   [0, 1, 9 | 52, 77, 92]   activates at p=37633
   ```

   This completely scans the oriented slice `A=[0,1,9]`, `B` any disjoint
   triple.  Rates: rational norm exception `1.0581%`; actual common-root
   activation `0.0039%`.  The core-by-core census is now 8 of 91 core types
   complete.

22. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,10)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0110_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1111 activation_exceptions=2
   H3_CORE_0110_CENSUS_DONE
   H3_CORE_0110_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 10 | 3, 4, 71]     activates at p=10273
   [0, 1, 10 | 28, 38, 59]   activates at p=20929
   ```

   This completely scans the oriented slice `A=[0,1,10]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8562%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 9 of 91 core types
   complete.

23. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,11)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0111_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1110 activation_exceptions=3
   H3_CORE_0111_CENSUS_DONE
   H3_CORE_0111_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 11 | 26, 37, 60]   activates at p=30817
   [0, 1, 11 | 46, 47, 60]   activates at p=30817
   [0, 1, 11 | 75, 89, 95]   activates at p=69313
   ```

   This completely scans the oriented slice `A=[0,1,11]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8554%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 10 of 91 core types
   complete.

24. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,12)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0112_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1268 activation_exceptions=2
   H3_CORE_0112_CENSUS_DONE
   H3_CORE_0112_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 12 | 3, 8, 85]    activates at p=19777
   [0, 1, 12 | 9, 90, 92]   activates at p=10273
   ```

   This completely scans the oriented slice `A=[0,1,12]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9771%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 11 of 91 core types
   complete.

25. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,13)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0113_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1289 activation_exceptions=1
   H3_CORE_0113_CENSUS_DONE
   H3_CORE_0113_CENSUS_CHECK_PASS
   ```

   Activation exception:

   ```text
   [0, 1, 13 | 16, 25, 62]   activates at p=10177
   ```

   This completely scans the oriented slice `A=[0,1,13]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9933%`; actual common-root
   activation `0.0008%`.  The core-by-core census is now 12 of 91 core types
   complete.

26. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,14)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0114_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1218 activation_exceptions=2
   H3_CORE_0114_CENSUS_DONE
   H3_CORE_0114_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 14 | 23, 36, 61]   activates at p=30817
   [0, 1, 14 | 50, 51, 61]   activates at p=30817
   ```

   This completely scans the oriented slice `A=[0,1,14]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9386%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 13 of 91 core types
   complete.

27. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,15)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0115_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1117 activation_exceptions=2
   H3_CORE_0115_CENSUS_DONE
   H3_CORE_0115_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 15 | 21, 35, 62]   activates at p=67777
   [0, 1, 15 | 46, 47, 64]   activates at p=10177
   ```

   This completely scans the oriented slice `A=[0,1,15]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8608%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 14 of 91 core types
   complete.

28. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,16)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0116_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1275 activation_exceptions=7
   H3_CORE_0116_CENSUS_DONE
   H3_CORE_0116_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 16 | 8, 9, 41]     activates at p=37633
   [0, 1, 16 | 8, 41, 57]    activates at p=1416317953
   [0, 1, 16 | 8, 57, 89]    activates at p=37633
   [0, 1, 16 | 9, 41, 56]    activates at p=37633
   [0, 1, 16 | 9, 56, 89]    activates at p=1416317953
   [0, 1, 16 | 24, 52, 75]   activates at p=20161
   [0, 1, 16 | 56, 57, 89]   activates at p=37633
   ```

   This completely scans the oriented slice `A=[0,1,16]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9825%`; actual common-root
   activation `0.0054%`.  The core-by-core census is now 15 of 91 core types
   complete.

29. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,17)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0117_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1228 activation_exceptions=4
   H3_CORE_0117_CENSUS_DONE
   H3_CORE_0117_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 17 | 5, 25, 86]    activates at p=32833
   [0, 1, 17 | 10, 45, 63]   activates at p=15361
   [0, 1, 17 | 15, 74, 93]   activates at p=15361
   [0, 1, 17 | 22, 41, 85]   activates at p=32833
   ```

   This completely scans the oriented slice `A=[0,1,17]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9463%`; actual common-root
   activation `0.0031%`.  The core-by-core census is now 16 of 91 core types
   complete.

30. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,18)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0118_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1135 activation_exceptions=4
   H3_CORE_0118_CENSUS_DONE
   H3_CORE_0118_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 18 | 6, 31, 84]    activates at p=27361
   [0, 1, 18 | 12, 30, 67]   activates at p=27361
   [0, 1, 18 | 15, 32, 65]   activates at p=10177
   [0, 1, 18 | 50, 51, 65]   activates at p=10177
   ```

   This completely scans the oriented slice `A=[0,1,18]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8747%`; actual common-root
   activation `0.0031%`.  The core-by-core census is now 17 of 91 core types
   complete.

31. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,19)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0119_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
   H3_CORE_0119_CENSUS_DONE
   H3_CORE_0119_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 19 | 7, 30, 85]    activates at p=27361
   [0, 1, 19 | 10, 29, 68]   activates at p=40897
   [0, 1, 19 | 13, 31, 66]   activates at p=12289
   ```

   This completely scans the oriented slice `A=[0,1,19]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8654%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 18 of 91 core types
   complete.

32. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,20)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0120_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1102 activation_exceptions=3
   H3_CORE_0120_CENSUS_DONE
   H3_CORE_0120_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 20 | 11, 30, 67]   activates at p=18913
   [0, 1, 20 | 16, 51, 95]   activates at p=18913
   [0, 1, 20 | 17, 34, 69]   activates at p=18913
   ```

   This completely scans the oriented slice `A=[0,1,20]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8492%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 19 of 91 core types
   complete.

33. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,21)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0121_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1232 activation_exceptions=4
   H3_CORE_0121_CENSUS_DONE
   H3_CORE_0121_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 21 | 9, 12, 56]    activates at p=37633
   [0, 1, 21 | 9, 29, 68]    activates at p=37633
   [0, 1, 21 | 13, 28, 89]   activates at p=37633
   [0, 1, 21 | 13, 40, 84]   activates at p=37633
   ```

   This completely scans the oriented slice `A=[0,1,21]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9494%`; actual common-root
   activation `0.0031%`.  The core-by-core census is now 20 of 91 core types
   complete.

34. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,22)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0122_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1105 activation_exceptions=3
   H3_CORE_0122_CENSUS_DONE
   H3_CORE_0122_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 22 | 16, 52, 89]   activates at p=10273
   [0, 1, 22 | 18, 27, 92]   activates at p=20929
   [0, 1, 22 | 25, 38, 61]   activates at p=10177
   ```

   This completely scans the oriented slice `A=[0,1,22]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8515%`; actual common-root
   activation `0.0023%`.  The core-by-core census is now 21 of 91 core types
   complete.

35. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,23)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0123_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
   H3_CORE_0123_CENSUS_DONE
   H3_CORE_0123_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 23 | 40, 59, 76]   activates at p=19777
   [0, 1, 23 | 43, 53, 59]   activates at p=20353
   ```

   This completely scans the oriented slice `A=[0,1,23]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9332%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 22 of 91 core types
   complete.

36. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,24)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0124_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
   H3_CORE_0124_CENSUS_DONE
   H3_CORE_0124_CENSUS_CHECK_PASS
   ```

   This completely scans the oriented slice `A=[0,1,24]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9425%`; actual common-root
   activation `0.0516%`.  All 67 activations contain the anchor exponent `49`.
   The core-by-core census is now 23 of 91 core types complete.

37. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,25)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0125_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
   H3_CORE_0125_CENSUS_DONE
   H3_CORE_0125_CENSUS_CHECK_PASS
   ```

   This completely scans the oriented slice `A=[0,1,25]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9425%`; actual common-root
   activation `0.0516%`.  All 67 activations contain the anchor exponent `48`.
   The core-by-core census is now 24 of 91 core types complete.

38. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,26)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0126_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1211 activation_exceptions=2
   H3_CORE_0126_CENSUS_DONE
   H3_CORE_0126_CENSUS_CHECK_PASS
   ```

   Activation exceptions:

   ```text
   [0, 1, 26 | 20, 36, 78]   activates at p=20353
   [0, 1, 26 | 36, 41, 77]   activates at p=19777
   ```

   This completely scans the oriented slice `A=[0,1,26]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.9332%`; actual common-root
   activation `0.0015%`.  The core-by-core census is now 25 of 91 core types
   complete.

39. **MACHINE-VERIFIED SUBFAMILY CENSUS:** complete core `(0,1,27)` slice.

   File:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CORE_0127_CENSUS.md
   ```

   Scripts:

   ```text
   critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py
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

   Result:

   ```text
   TOTAL shapes=129766 norm_exceptions=1093 activation_exceptions=1
   H3_CORE_0127_CENSUS_DONE
   H3_CORE_0127_CENSUS_CHECK_PASS
   ```

   Activation exception:

   ```text
   [0, 1, 27 | 5, 22, 31]   activates at p=20929
   ```

   This completely scans the oriented slice `A=[0,1,27]`, `B` any disjoint
   triple.  Rates: rational norm exception `0.8423%`; actual common-root
   activation `0.0008%`.  Modal printed a worker-preemption notice after the
   digest/app completion; the local checker pins the banked JSON.  The
   core-by-core census is now 26 of 91 core types complete.

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

- The random norm sample found `22/2000` shared rational threshold norm primes,
  so the naive rational norm-coprimality phrasing is false as a universal
  heuristic.  None of these were actual common-root activations, which points to
  the correct prime-ideal/common-root formulation.

- The deterministic affine-representative slice found actual common-root
  activations.  This corrects the overly optimistic zero-exception
  common-root phrasing; Terminal C is now an exceptional-list/rate census.

- The consecutive-core census shows the first structural cluster:
  `[0,1,2 | 17,*,81]` and reflected/48-shift tail patterns account for many
  activations, but sporadic high-prime examples remain.

- The subsequent structure check shows the cluster is exact for the
  consecutive-core slice: every activation is in the fixed-pair or antipodal
  family.  What looked sporadic is still covered by that two-family union.

- The family-rate check strengthens this: outside the two-family union, the
  complete consecutive-core slice has zero activations.

- The next complete core slice `(0,1,3)` has only three actual activations,
  showing that the dense consecutive-core behavior is not typical across the
  first two core types.  The third core slice `(0,1,4)` also remains sparse,
  with five actual activations.  The fourth core slice `(0,1,5)` returns to
  three activations, all at the same prime.  The fifth core slice `(0,1,6)`
  also has three activations, at three different primes.  The sixth core slice
  `(0,1,7)` again has three activations.  The seventh core slice `(0,1,8)`
  also has three activations.  The eighth core slice `(0,1,9)` has five
  activations and the largest rational norm-exception rate among the completed
  non-consecutive cores so far.  The ninth core slice `(0,1,10)` is the
  sparsest non-consecutive slice so far, with two activations.  The tenth core
  slice `(0,1,11)` returns to three activations.  The eleventh core slice
  `(0,1,12)` again has two activations.  The twelfth core slice `(0,1,13)`
  has a single activation, the sparsest complete slice so far.  The thirteenth
  core slice `(0,1,14)` has two activations, both at `p=30817`.  The
  fourteenth core slice `(0,1,15)` also has two activations.  The fifteenth
  core slice `(0,1,16)` has seven activations, including two at the large prime
  `p=1416317953`.  The sixteenth core slice `(0,1,17)` has four activations.
  The seventeenth core slice `(0,1,18)` also has four activations.  The
  eighteenth core slice `(0,1,19)` returns to three activations.  The nineteenth
  core slice `(0,1,20)` also has three activations, all at `p=18913`.  The
  twentieth core slice `(0,1,21)` has four activations, all at `p=37633`.  The
  twenty-first core slice `(0,1,22)` has three activations.  The twenty-second
  core slice `(0,1,23)` has two activations.  The twenty-third core slice
  `(0,1,24)` is the first high-activation non-consecutive slice since
  `(0,1,2)`: it has 67 activations, and every one contains the anchor exponent
  `49`.  The next slice `(0,1,25)` mirrors this high-activation behavior with
  67 activations, all containing anchor exponent `48`.  The following slice
  `(0,1,26)` returns to the sparse two-activation regime, `(0,1,27)` has a
  single activation, `(0,1,28)` has six activations, `(0,1,29)` and
  `(0,1,30)` each have three activations, `(0,1,31)` has four activations,
  `(0,1,32)` has fourteen activations, `(0,1,33)` has 32 activations,
  `(0,1,34)` has four activations, and `(0,1,35)` has three activations.

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

Terminal B status: energy theorem complete with explicit in-house constants.
The new self-contained route proves `E(H) <= 83851 h^2.5`; the external
Cochrane--Pinner `16/3` constant remains far sharper.  Using the in-house
constant alone, the h=2 floor is automatic only for
`h > 7030990201/64`; smaller universal rows would need a finite certificate or
a sharper constant, while all banked ladder rows pass exactly.

Terminal C status: complete for the oriented core-slice census.  The
observed-shape pilot supports common-root pair-coprimality, and the random
exact-norm sample refines the statement away from rational norm gcds.  The
64-prime activation ladder gives stronger direct finite-field evidence.  The
full `n=96` all-shapes census is exactly sized at `3,135,641` affine/Galois
representatives, and the core-by-core program covers all `91` core types with
one complete oriented `B`-slice each.  The aggregate has `106250/11808706`
rational norm exceptions and `720/11808706` actual common-root activation
exceptions.  The full 720-entry oriented activation-exception list is banked in
`f3_h3_all_core_census_summary.json`.  Burnside-deduplicated pair-orbit
accounting remains a separate optional post-processing layer.
Continuation update: the complete core-by-core census is now all 91 of 91 core
types complete, through `(0,1,92)`.  The latest slice has `1102/129766`
rational norm exceptions and `3/129766` actual common-root activation
exceptions.
The oriented core-slice resultant/common-root pass and aggregate empirical rate
are banked.

Bonus queue update: item (i) has a replayed h=4/h=5 reduction/status note.
`h4_terminal_dichotomy` and `x83_uniform_square_shift_obstruction_gate` are
verified as `PROVED` structural inputs; the existing f3a1/f3a2 rows retain the
positive control and zero q>=n^2 h=4/h=5 residue checks.  The h=5 no-primitive
theorem remains a norm-gate exclusion/certificate problem, not a promoted
theorem.

Follow-up h=5 update: a compiled complete `n=32,h=5` multirow certificate now
covers `p=1153,3137,12289,32801,40961,61441,65537`.  Each row checks `31465`
anchored left subsets and `169911` right subsets, with zero anchored nontoral
trades.  This strengthens the h=5 certificate evidence but does not promote the
uniform h=5 no-primitive theorem.

Catch update: the compiled h=8/h=5 certificate scripts initially used a fixed
11-bit signature packing shift, unsafe above `p=2048`.  The committed scripts
now use `BITS=ceil(log2 p)` and the multirow JSON artifacts were regenerated;
the certified counts remain unchanged.

Bonus queue update: item (ii) has a replayed h=6/7/8 sweep status note.  It
verifies 11 full h=6/h=7 q>=n^2 rows with zero anchored nontoral trades and no
n^3 alarm.  The three h=8 rows are explicitly partial zero slices, so h=8 still
needs shard-complete certificates or x83 norm-gate keys.

Follow-up h=8 update: `boundary_n32_h8_p1153_FULL` is now a complete anchored
certificate via a compiled replay.  It checks `2629575` left anchored subsets
and `7888725` right subsets, finding `3` paid toral anchored trades and `0`
anchored nontoral trades.  The same compiled certificate now also covers
boundary primes `p=3137,12289` and smooth primes `p=40961,61441,65537`.  The
aggregate h=6/7/8 replay reports six full h=8 n=32 certificates and two
remaining h=8 partial n=64 slices.

Bonus queue update: item (iii) now has a posed h=3 per-row accident theorem.
With `A_3(n,p)` the number of activated non-toral dilation-shape orbits at a
fixed row, the target `A_3(n,p) <= Cn` compiles to `T_3<n^3` for all `n>=17`
when `C=16`.  The note records the hyperbola/Stepanov ansatz as a multi-Delta
rich-value theorem; no proof of this target is claimed.

Continuation h=5 update: a compiled complete `n=64,h=5` multirow certificate
now covers `p=4289,12289,40961,65537,262337`.  Each row checks `595665`
anchored left subsets and `7028847` right subsets, with zero anchored
nontoral trades and no `n^3` alarm.  The replay is local-light
(`p=4289` under 4 seconds; all five primes under 18 seconds; peak RSS below
90 MB).  This extends the h=5 finite-row zero evidence from n=32 to n=64, but
does not promote a uniform h=5 no-primitive theorem.

Continuation h=5 scale update: the next boundary row `n=96,h=5,p=9601` now has
a complete anchored certificate as well.  The replay checks `3183545` anchored
left subsets and `57940519` right subsets, finds zero anchored nontoral trades,
and stays within the local light-compute rule (`48.70s`, about `152 MB` RSS).
This is the largest complete h=5 row banked so far; it remains finite evidence,
not a proof of the uniform h=5 theorem.

Continuation h=5 Modal update: the boundary row `n=128,h=5,p=17921` now has a
complete 32-shard Modal certificate.  The heaviest shard gate passed in
`15.051s`; the full replay checked `254231775` right subsets with `10334625`
anchored left subsets per shard, finding zero anchored toral trades, zero
anchored nontoral trades, and no `n^3` alarm.  Max shard elapsed time was
`17.488s`.  The aggregate h4/h5 replay verifies the pinned JSON without
rerunning Modal.  A small catch was banked: Modal remote imports broke
`Path(__file__)`-based root detection, so the script now uses `F3_PRIZE_ROOT`.

Continuation h=5 n=128 ladder update: the same sharded Modal replay now also
certifies `p=18049,18433,19073,19457,19841,20353`.  Each row checks
`254231775` right subsets with `10334625` anchored left subsets per shard,
finding zero anchored toral trades, zero anchored nontoral trades, and no
`n^3` alarm.  Max shard times were `17.419s`, `14.298s`, `13.750s`,
`15.603s`, `17.424s`, and `14.759s`.  The n=128 h=5 ladder therefore has
seven complete zero rows: `17921,18049,18433,19073,19457,19841,20353`.

Continuation h=6 Modal update: the first complete `n=64,h=6` boundary row is
now certified at `p=4289`.  A single local compiled run hit the 60-second cap,
so the replay was converted to 16 Modal shards with 60-second container
timeouts.  The complete aggregate checks `67945521` right subsets with
`7028847` anchored left subsets per shard, finding zero anchored toral trades,
zero anchored nontoral trades, and no `n^3` alarm.  Max shard elapsed time was
`10.634s`.  The aggregate h6/h8 replay now requires this JSON certificate and
still reports the two remaining h=8 n=64 slices as partial evidence.

Continuation h=6 falsifier/classification update: the extra-prime `n=64,h=6`
Modal sweep now certifies `p=4481,4673,4801,4993,5441,5569`.  The `p=4993` row
has exactly `6` anchored nontoral witnesses; the other five rows are zero.  A
follow-up verifier proves all six p4993 witnesses are antipodal square-lifts of
the complete h=3 anchored trade set on `mu_32` at the same prime.  So this
refutes the crude toral-only h=6 emptiness proxy, not the fully stripped
primitive h=6 column, and it remains far below the direct-column budget (`6`
versus `n^3=262144`).  The repaired h=6 target separates paid square-lifts of
h=3 norm-gate accidents from genuinely primitive h=6 accidents.

Continuation h=7/h=8 feasibility update: exact counts explain why the remaining
n=64 partials should not be promoted by a blind h=8 all-left hash sweep.  h=7
n64 has `67945521` left records and `553270671` right probes, so it needs a
single Modal timing gate before a full sweep.  h=8 n64 has `553270671` left
records and `3872894697` right probes; the left table alone is about `16.5 GiB`
at 32 bytes per record.  The h=8 route should therefore use square-shift/x83
structure or a new external/sharded signature join.

Continuation h=7 certificate update: the h=7 n64 gate was upgraded to a
rank-balanced full certificate at `p=4289`.  All 16 Modal shards completed under
60 seconds (max `55.1206s`), each building the full `67945521`-record
anchored-left table; together they probed all `553270671` right subsets.  The
aggregate has zero anchored toral trades, zero anchored nontoral trades, and no
`n^3` alarm.  The aggregate h6/h8 replay now requires this h=7 JSON certificate.

Continuation h=8 structural update: a light square-lift probe reduces the
antipodal h=8 n64 branch to h=4 on `mu_32`.  The low `p=193` diagnostic row has
`15` quotient h=4 anchored trades (`7` toral, `8` nontoral), but the `q3_n64_h8`
prime `p=262337` has only `7` toral quotient trades and zero nontoral quotient
residue.  This does not certify the full h=8 n64 row; it says the remaining
q3 obstruction, if any, is non-antipodal primitive structure or another paid
branch, not an antipodal square-lift.
