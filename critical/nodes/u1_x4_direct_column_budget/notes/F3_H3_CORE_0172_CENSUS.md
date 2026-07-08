# F3 h=3 core `(0,1,72)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the seventy-first of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,72],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,72 --tag 0172
```

Expected digest:

```text
H3_CORE_0172_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0172_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-8OvoNOPEwf71s8xrY8ooiw
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1223 activation_exceptions=67
H3_CORE_0172_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1223 / 129766 = 0.9425%
actual common-root activation:   67 / 129766 = 0.0516%
```

Activation list:

```text
[0, 1, 72 | 2, 26, 49]   p=37633
[0, 1, 72 | 2, 49, 74]   p=244129
[0, 1, 72 | 3, 27, 49]   p=30817
[0, 1, 72 | 3, 49, 75]   p=8807521
[0, 1, 72 | 4, 49, 76]   p=24481
[0, 1, 72 | 5, 29, 49]   p=3970273
[0, 1, 72 | 6, 30, 49]   p=690817
[0, 1, 72 | 6, 49, 78]   p=690817
[0, 1, 72 | 7, 49, 79]   p=1799617
[0, 1, 72 | 8, 49, 80]   p=9699841
[0, 1, 72 | 9, 33, 49]   p=10657
[0, 1, 72 | 10, 34, 49]   p=937537
[0, 1, 72 | 10, 49, 82]   p=2556577
[0, 1, 72 | 11, 49, 83]   p=1259329
[0, 1, 72 | 12, 36, 49]   p=27361
[0, 1, 72 | 12, 49, 84]   p=27361
[0, 1, 72 | 13, 37, 49]   p=35417281
[0, 1, 72 | 13, 49, 85]   p=13729
[0, 1, 72 | 14, 38, 49]   p=117889
[0, 1, 72 | 14, 49, 86]   p=24001
[0, 1, 72 | 15, 49, 87]   p=25633
[0, 1, 72 | 16, 40, 49]   p=9601
[0, 1, 72 | 17, 41, 49]   p=37633
[0, 1, 72 | 17, 49, 89]   p=37633
[0, 1, 72 | 18, 49, 90]   p=93889
[0, 1, 72 | 19, 43, 49]   p=956929
[0, 1, 72 | 19, 49, 91]   p=49921
[0, 1, 72 | 20, 44, 49]   p=38113
[0, 1, 72 | 20, 49, 92]   p=10753
[0, 1, 72 | 21, 45, 49]   p=33601
[0, 1, 72 | 21, 49, 93]   p=80449
[0, 1, 72 | 22, 46, 49]   p=19009
[0, 1, 72 | 22, 49, 94]   p=105601
[0, 1, 72 | 26, 49, 50]   p=244129
[0, 1, 72 | 27, 49, 51]   p=30817
[0, 1, 72 | 28, 49, 52]   p=6743809
[0, 1, 72 | 29, 49, 53]   p=1529089
[0, 1, 72 | 30, 49, 54]   p=39841
[0, 1, 72 | 32, 49, 56]   p=9699841
[0, 1, 72 | 33, 49, 57]   p=208921057
[0, 1, 72 | 34, 49, 58]   p=600577
[0, 1, 72 | 35, 49, 59]   p=16121089
[0, 1, 72 | 36, 49, 60]   p=12289
[0, 1, 72 | 37, 49, 61]   p=13729
[0, 1, 72 | 38, 49, 62]   p=117889
[0, 1, 72 | 40, 49, 64]   p=41432641
[0, 1, 72 | 41, 49, 65]   p=9043009
[0, 1, 72 | 42, 49, 66]   p=93889
[0, 1, 72 | 43, 49, 67]   p=18049
[0, 1, 72 | 44, 49, 68]   p=38113
[0, 1, 72 | 45, 49, 69]   p=471649
[0, 1, 72 | 47, 49, 71]   p=400033
[0, 1, 72 | 49, 51, 75]   p=32833
[0, 1, 72 | 49, 52, 76]   p=1857217
[0, 1, 72 | 49, 53, 77]   p=43201
[0, 1, 72 | 49, 54, 78]   p=39841
[0, 1, 72 | 49, 55, 79]   p=14593
[0, 1, 72 | 49, 58, 82]   p=2240449
[0, 1, 72 | 49, 59, 83]   p=21601
[0, 1, 72 | 49, 60, 84]   p=12289
[0, 1, 72 | 49, 61, 85]   p=52334209
[0, 1, 72 | 49, 62, 86]   p=24001
[0, 1, 72 | 49, 65, 89]   p=7799809
[0, 1, 72 | 49, 67, 91]   p=120577
[0, 1, 72 | 49, 68, 92]   p=10753
[0, 1, 72 | 49, 70, 94]   p=17377
[0, 1, 72 | 49, 71, 95]   p=418177
```

This is a dense structural slice.  Nearly every activation contains the
anchor exponent `49`, mirroring the earlier dense anchored slices.

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0172_census_check.py
```

Expected digest:

```text
H3_CORE_0172_CENSUS_CHECK_PASS
```
