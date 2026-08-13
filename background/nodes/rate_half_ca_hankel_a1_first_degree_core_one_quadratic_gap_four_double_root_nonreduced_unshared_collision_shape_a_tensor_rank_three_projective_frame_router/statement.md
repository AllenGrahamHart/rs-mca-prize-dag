# `A=1` shape-A tensor-rank-three projective-frame router

- **status:** PROVED
- **closure:** rank three forces a four-row triple-free incidence frame
- **consumer:** `rate_half_band_crossing_location`

Retain an official Shape-A all-excess survivor and put

```text
m=e-2,
n=(3e-7)/2,
R=(9e-7)/2=3n+7,
|Gamma|=3e.                                         (TRF1)
```

Suppose its biform has tensor separation rank exactly three. Then there are
four domain rows `x_1,...,x_4` such that:

1. their projective coefficient vectors in a minimal rank-three
   representation are in general position in `P^2`;
2. each row root set

   ```text
   A_i={delta in Gamma:G(delta,x_i)=0}
   ```

   has size `m`;
3. no slope belongs to three of the four sets;
4. at least `e-8` slopes belong to exactly two of them.

Consequently

```text
sum_(1<=i<j<=4)|A_i intersect A_j|>=e-8,           (TRF2)
```

and one pair satisfies

```text
|A_i intersect A_j|>=ceil((e-8)/6).                (TRF3)
```

On the official row the right side is

```text
30541989660.                                        (TRF4)
```

After any three noncollinear coefficient rows are selected, at least seven
domain rows remain available for the fourth general-position row.

## Scope

Together with the rank-two exclusion, this routes every official survivor
to either the displayed rank-three frame or tensor rank at least four. The
theorem does not exclude the frame, prove that rank three occurs, or control
rank four and above.
