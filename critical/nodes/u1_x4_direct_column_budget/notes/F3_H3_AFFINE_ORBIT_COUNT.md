# F3 h=3 affine-orbit count for the full `n=96` census

Status: PRE-REGISTERED SIZING STEP for Terminal C.  This does not prove
pair-coprimality; it computes the exact size of the all-shapes census after the
translation and Galois symmetries that preserve the obstruction norms and
common-root activation.

## Pre-registration

Object:

```text
unordered pairs {A,B} of disjoint 3-subsets of Z/96Z
```

Symmetry group:

```text
x -> u*x + s,  u in (Z/96Z)^*, s in Z/96Z.
```

This symmetry preserves rational obstruction norms, and multiplication by
`u in (Z/96Z)^*` corresponds to changing the primitive 96th root, so it also
preserves the refined common-root activation property.

Falsifier:

- if the Burnside count is not an integer, the orbit-count implementation is
  wrong;
- if the count remains close to the raw normalized count, the full all-shapes
  resultant census is less feasible than hoped.

Compute discipline:

- Modal only;
- group elements are sharded;
- worker timeout `60s`;
- partial fixed-point sums print before the final integer check.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_affine_orbit_count_modal.py
```

Expected digest:

```text
H3_AFFINE_ORBIT_COUNT_PASS
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-XVtUnVPEitz3WXSczroC2x
```

Output summary:

```text
GROUP_ORDER 3072
FIXED_TOTAL 9632689152
AFFINE_ORBITS 3135641
H3_AFFINE_ORBIT_COUNT_PASS
```

Interpretation: the full `n=96` Terminal C all-shapes census reduces from the
raw unordered disjoint-pair count

```text
binom(96,3) * binom(93,3) / 2 = 9270483040
```

to `3,135,641` affine/Galois orbit representatives.  This is still too large
for local computation, but it is a feasible Modal campaign if the exact
resultant/common-root evaluator is sharded.
