# `A=1` first-degree bounded residual table

- **status:** PROVED
- **closure:** exact capacity-to-heavy-factor arithmetic
- **consumer:** `rate_half_band_crossing_location`

Retain the notation of the first-degree ambient defect factorization. Let

```text
h_j=deg B_j,       a_j=d-3-h_j=deg_X A_j^res.          (BRT1)
```

Then the six official profiles satisfy the exact uniform bounds

```text
                 j=0     j=1     j=2
s=0:             a_j<=5  a_j<=12 a_j<=18
s=1:             a_j<=2  a_j<=9  a_j<=15.            (BRT2)
```

Equivalently, all but at most the displayed number of the available
`d-3` domain degrees of `A_j` are forced into the split heavy-row factor
`B_j`.

For every residual domain row outside `B_j`, the complete missing-root
factor has degree at most `j` and divides a specialization of the bounded
biform

```text
A_j^res,       bideg A_j^res<=(a_j,j).                (BRT3)
```

Thus the six formerly enormous boundary problems reduce respectively to
bidegrees

```text
(5,0), (12,1), (18,2), (2,0), (9,1), (15,2).         (BRT4)
```

## Scope

The table is a necessary reduction. It does not classify or exclude the six
bounded residual biforms.
