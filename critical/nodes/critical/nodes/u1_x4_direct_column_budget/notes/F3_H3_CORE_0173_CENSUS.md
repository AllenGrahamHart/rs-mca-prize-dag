# F3 h=3 core `(0,1,73)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the seventy-second of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,73],  B any 3-subset of Z/96Z disjoint from A.
```

There are `binom(93,3)=129766` shapes in this oriented slice.

Deliverable:

- compute exact obstruction norms for every `B`;
- factor `gcd(N(E1),N(E2))`;
- record threshold rational norm exceptions;
- test actual common primitive-root activation for each threshold factor;
- write the full activation list to JSON.

Compute discipline:

- Modal only;
- generic runner `f3_h3_core_census_modal.py`;
- `64` shards by combination index;
- worker timeout `60s`;
- partial per-shard counts print before aggregation.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,73 --tag 0173
```

Expected digest:

```text
H3_CORE_0173_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0173_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-lBMaGlQqKmCcuj2c4TjQDy
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0173_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1223 / 129766 = 0.9425%
actual common-root activation:   67 / 129766 = 0.0516%
```

Activation list:

```text
[0, 1, 73 | 2, 48, 74]   p=400033
[0, 1, 73 | 3, 27, 48]   p=105601
[0, 1, 73 | 3, 48, 75]   p=19009
[0, 1, 73 | 4, 48, 76]   p=80449
[0, 1, 73 | 5, 29, 48]   p=38113
[0, 1, 73 | 5, 48, 77]   p=10753
[0, 1, 73 | 6, 30, 48]   p=956929
[0, 1, 73 | 6, 48, 78]   p=18049
[0, 1, 73 | 7, 31, 48]   p=93889
[0, 1, 73 | 8, 32, 48]   p=7799809
[0, 1, 73 | 8, 48, 80]   p=37633
[0, 1, 73 | 9, 33, 48]   p=41432641
[0, 1, 73 | 11, 35, 48]   p=24001
[0, 1, 73 | 11, 48, 83]   p=117889
[0, 1, 73 | 12, 36, 48]   p=52334209
[0, 1, 73 | 12, 48, 84]   p=13729
[0, 1, 73 | 13, 37, 48]   p=12289
[0, 1, 73 | 13, 48, 85]   p=12289
[0, 1, 73 | 14, 48, 86]   p=16121089
[0, 1, 73 | 15, 39, 48]   p=2556577
[0, 1, 73 | 15, 48, 87]   p=937537
[0, 1, 73 | 17, 41, 48]   p=9699841
[0, 1, 73 | 19, 43, 48]   p=690817
[0, 1, 73 | 19, 48, 91]   p=690817
[0, 1, 73 | 20, 44, 48]   p=43201
[0, 1, 73 | 21, 45, 48]   p=6743809
[0, 1, 73 | 21, 48, 93]   p=1857217
[0, 1, 73 | 22, 46, 48]   p=30817
[0, 1, 73 | 22, 48, 94]   p=30817
[0, 1, 73 | 23, 47, 48]   p=244129
[0, 1, 73 | 23, 48, 95]   p=37633
[0, 1, 73 | 27, 48, 51]   p=17377
[0, 1, 73 | 28, 48, 52]   p=471649
[0, 1, 73 | 29, 48, 53]   p=38113
[0, 1, 73 | 30, 48, 54]   p=49921
[0, 1, 73 | 32, 48, 56]   p=9043009
[0, 1, 73 | 33, 48, 57]   p=9601
[0, 1, 73 | 34, 48, 58]   p=25633
[0, 1, 73 | 35, 48, 59]   p=24001
[0, 1, 73 | 36, 48, 60]   p=13729
[0, 1, 73 | 37, 48, 61]   p=27361
[0, 1, 73 | 38, 48, 62]   p=1259329
[0, 1, 73 | 39, 48, 63]   p=2240449
[0, 1, 73 | 40, 48, 64]   p=208921057
[0, 1, 73 | 42, 48, 66]   p=1799617
[0, 1, 73 | 43, 48, 67]   p=39841
[0, 1, 73 | 44, 48, 68]   p=1529089
[0, 1, 73 | 46, 48, 70]   p=8807521
[0, 1, 73 | 48, 50, 74]   p=418177
[0, 1, 73 | 48, 52, 76]   p=33601
[0, 1, 73 | 48, 53, 77]   p=10753
[0, 1, 73 | 48, 54, 78]   p=120577
[0, 1, 73 | 48, 55, 79]   p=93889
[0, 1, 73 | 48, 56, 80]   p=37633
[0, 1, 73 | 48, 59, 83]   p=117889
[0, 1, 73 | 48, 60, 84]   p=35417281
[0, 1, 73 | 48, 61, 85]   p=27361
[0, 1, 73 | 48, 62, 86]   p=21601
[0, 1, 73 | 48, 63, 87]   p=600577
[0, 1, 73 | 48, 64, 88]   p=10657
[0, 1, 73 | 48, 65, 89]   p=9699841
[0, 1, 73 | 48, 66, 90]   p=14593
[0, 1, 73 | 48, 67, 91]   p=39841
[0, 1, 73 | 48, 68, 92]   p=3970273
[0, 1, 73 | 48, 69, 93]   p=24481
[0, 1, 73 | 48, 70, 94]   p=32833
[0, 1, 73 | 48, 71, 95]   p=244129
```

This is another dense anchored slice.  Nearly every activation contains
anchor exponent `48`, pairing with the previous `(0,1,72)` slice anchored at
`49`.

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0173_census_check.py
```

Expected digest:

```text
H3_CORE_0173_CENSUS_CHECK_PASS
```
