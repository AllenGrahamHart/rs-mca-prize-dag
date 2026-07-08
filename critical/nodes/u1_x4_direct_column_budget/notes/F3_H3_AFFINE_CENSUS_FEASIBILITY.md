# F3 h=3 affine-representative census feasibility (Terminal C)

Status: PRE-REGISTERED FEASIBILITY SHARD.  This is the first deterministic
resultant/common-root pass over affine/Galois representatives.  It is not the
full `3,135,641`-orbit census.

## Pre-registration

Input space:

```text
affine/Galois canonical representatives of unordered disjoint h=3 shape pairs
in Z/96Z
```

Target under stress:

> In deterministic affine-orbit representatives, rational threshold norm-gcd
> exceptions can occur, but actual simultaneous primitive-root activations
> should be rarer.  A repeated/common-root activation is the refined Terminal C
> exceptional object.

Falsifier:

- find any canonical representative whose common obstruction norm factors
  contain a threshold prime `p = 1 mod 96`, `p >= 96^2` at which the two
  obstructions vanish at a common primitive 96th root.

Compute discipline:

- Modal only;
- `8` shards;
- worker timeout `60s`;
- each shard stops after `500` assigned affine reps or its raw scan limit;
- partial shard results print before aggregate summary.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_census_feasibility_modal.py
```

Expected digest:

```text
H3_AFFINE_CENSUS_FEASIBILITY_DONE
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Zxs2CntPQhR6CBzOeCT1U4
```

Output summary:

```text
TOTAL unique_reps=4000 norm_exceptions=46 activation_exceptions=3
H3_AFFINE_CENSUS_FEASIBILITY_DONE
```

Actual activation exceptions found:

```text
[0, 1, 2 | 3, 26, 74] activates at p=1033441
[0, 1, 2 | 3, 17, 81] activates at p=207073
[0, 1, 2 | 3, 51, 53] activates at p=13249
```

Local exact verification: each shape is char-zero nonzero for both
obstructions, and each has exactly one primitive 96th root modulo the listed
prime where both obstructions vanish.  The `p=13249` exception is the
affine/Galois representative of one of the observed activated ladder shapes.

Verdict: the full Terminal C deliverable must indeed be an empirical
coprimality rate plus exceptional list.  A zero-exception common-root statement
is false even in the first deterministic affine-representative slice.  This is
not a failure of the program; it supplies the first entries of the requested
exceptional list.
