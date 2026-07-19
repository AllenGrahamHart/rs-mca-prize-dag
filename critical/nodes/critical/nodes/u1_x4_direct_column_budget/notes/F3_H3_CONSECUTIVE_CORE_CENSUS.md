# F3 h=3 consecutive-core census (Terminal C)

Status: PRE-REGISTERED COMPLETE SUBFAMILY CENSUS.  This is not the full
`n=96` census, but it completely scans the structural slice suggested by the
first affine-representative exceptions.

## Pre-registration

Observed pattern:

```text
[0, 1, 2 | 3, 26, 74]
[0, 1, 2 | 3, 17, 81]
[0, 1, 2 | 3, 51, 53]
```

All current deterministic activation exceptions have one side equal to the
consecutive triple `[0,1,2]`.

Subfamily:

```text
A = [0,1,2],  B any 3-subset of {3,4,...,95}
```

There are `binom(93,3)=129766` shapes in this oriented slice.

Falsifier / deliverable:

- compute exact obstruction norms for every `B`;
- factor `gcd(N(E1),N(E2))`;
- record every threshold rational norm exception and every actual common-root
  activation exception;
- report the activation-exception count and examples.

Compute discipline:

- Modal only;
- `64` shards by combination index;
- worker timeout `60s`;
- partial per-shard counts print before aggregation.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_census_modal.py
```

Expected digest:

```text
H3_CONSECUTIVE_CORE_CENSUS_DONE
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-kXLMPfgavdlZF0IQFI2wXg
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1122 activation_exceptions=44
H3_CONSECUTIVE_CORE_CENSUS_DONE
```

Thus the rational norm-exception rate in this oriented slice is
`1122/129766 = 0.8646%`, while the actual common-root activation rate is
`44/129766 = 0.0339%`.

Complete activation list:

```text
[0, 1, 2 | 3, 17, 81]   p=207073
[0, 1, 2 | 3, 26, 74]   p=1033441
[0, 1, 2 | 3, 51, 53]   p=13249
[0, 1, 2 | 5, 17, 81]   p=40897
[0, 1, 2 | 7, 17, 81]   p=18913
[0, 1, 2 | 7, 55, 61]   p=2574433
[0, 1, 2 | 8, 56, 63]   p=12289
[0, 1, 2 | 9, 29, 77]   p=47137
[0, 1, 2 | 9, 57, 65]   p=62017
[0, 1, 2 | 10, 58, 67]  p=20929
[0, 1, 2 | 11, 30, 78]  p=49537
[0, 1, 2 | 12, 60, 71]  p=1857217
[0, 1, 2 | 13, 17, 81]  p=30817
[0, 1, 2 | 13, 61, 73]  p=244129
[0, 1, 2 | 15, 32, 80]  p=26682529
[0, 1, 2 | 15, 63, 77]  p=120097
[0, 1, 2 | 16, 64, 79]  p=281857
[0, 1, 2 | 17, 33, 81]  p=10177
[0, 1, 2 | 17, 37, 81]  p=30817
[0, 1, 2 | 17, 43, 81]  p=18913
[0, 1, 2 | 17, 45, 81]  p=40897
[0, 1, 2 | 17, 47, 81]  p=207073
[0, 1, 2 | 17, 51, 81]  p=207073
[0, 1, 2 | 17, 53, 81]  p=40897
[0, 1, 2 | 17, 55, 81]  p=18913
[0, 1, 2 | 17, 61, 81]  p=30817
[0, 1, 2 | 17, 65, 81]  p=10177
[0, 1, 2 | 17, 81, 85]  p=30817
[0, 1, 2 | 17, 81, 91]  p=18913
[0, 1, 2 | 17, 81, 93]  p=40897
[0, 1, 2 | 17, 81, 95]  p=207073
[0, 1, 2 | 18, 66, 83]  p=26682529
[0, 1, 2 | 19, 34, 82]  p=281857
[0, 1, 2 | 20, 68, 87]  p=49537
[0, 1, 2 | 21, 35, 83]  p=120097
[0, 1, 2 | 21, 69, 89]  p=47137
[0, 1, 2 | 24, 72, 95]  p=1033441
[0, 1, 2 | 25, 37, 85]  p=244129
[0, 1, 2 | 27, 38, 86]  p=1857217
[0, 1, 2 | 31, 40, 88]  p=20929
[0, 1, 2 | 33, 41, 89]  p=62017
[0, 1, 2 | 35, 42, 90]  p=12289
[0, 1, 2 | 37, 43, 91]  p=2574433
[0, 1, 2 | 45, 47, 95]  p=13249
```

Structural signal: many exceptions lie in the two visible families
`[0,1,2 | 17, b, 81]` and paired reflected tails
`[0,1,2 | a, a+48, *]`, but the list also contains sporadic high-prime
activations.  This subfamily should be the first target for a structural
exception classification.
