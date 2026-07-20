# L1 background-overlap singleton payment

- **status:** PROVED
- **role:** remove the low retained-core/petal-surplus side of the tail
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart with

```text
N=k-1,       |B|=b<ell,       g=ell-b,
```

one defect degree `d`, and one exact labelled petal-support pattern `X` of
size `h`. Put

```text
a=N-d,       s=h-d.                                    (BO1)
```

If

```text
a+s<ell+g,                                               (BO2)
```

then at most one compatible listed codeword exists in this cell.

For every fixed petal-polarity cap `p<=P`, the union of all cells satisfying
`(BO2)` is polynomial per source chart. At the L1 cutoff an explicit bound is

```text
(P+1)n^(1/c_0+P+1).                                     (BO3)
```

In the nonpositive-Johnson tail define the support codimension

```text
c=N-h=a-s.
```

Combining the complement of `(BO2)` with `a^2<=Nc` gives the exact survivor
strip

```text
a^2/N<=c<=2a-ell-g.                                     (BO4)
```

The strict inequality in `(BO2)` is sharp: an exact `F_17`, `ell=2` maximal
chart has two saturated threshold contributors at

```text
a+s=ell+g=3.                                            (BO5)
```

## Scope

This theorem is per source chart. It does not count the strip `(BO4)`,
unbounded petal polarity, or non-intrinsic first-match chart multiplicity.
