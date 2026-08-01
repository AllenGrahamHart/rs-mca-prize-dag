# KoalaBear m2 r4 positive 433-1a common Vieta pivot-chart reduction

- **status:** PROVED
- **scope:** the rank-six-base common Vieta systems for the positive route
  `433-1a -> O0b`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
- **consumer:** `rate_half_band_closure`

Let `B` be the six-row base of the common Vieta compiler and assume
`rank B=6`.  Write `q_i` for the image of the nonloop sum row `Q_i` in

```text
V=F^8/rowspan(B),       dim V=2,       1<=i<=4.    (KBPCR-1)
```

The common matrix has rank at most seven exactly on the following
five-branch cover:

```text
Z:    q_1=q_2=q_3=q_4=0;
C_i:  q_i!=0 and det(B,Q_i,Q_j)=0 for every j!=i. (KBPCR-2)
```

The four chart triples, using the six-minor order
`12,13,14,23,24,34`, are

```text
C_1: 12,13,14       C_2: 12,23,24
C_3: 13,23,34       C_4: 14,24,34.                (KBPCR-3)
```

The cover need not be disjoint.  It reduces every nonzero chart from six
minor equations to three without changing its localized solution set.  The
all-zero branch has common rank six, not seven, and remains a separate
algebraic branch.  The base-rank-drop branch `rank B<6` is outside this
theorem and remains open.

This theorem does not solve a chart, delete `433-1a -> O0b`, append outside
rows, close positive coordinate parity, close K3 or a Prize row, or prove
either Prize result.

## Falsifier

A rank-six base and four quotient images for which `(KBPCR-2)` disagrees
with rank at most seven, or a nonzero pivot chart requiring any minor not
listed in `(KBPCR-3)`.
