# Repeated-BC cell-11 uncolored generic-rank atlas

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** generic fibers with missing record `DE+`, `DF+`, or `EF`

For each of the eight cell-11 source towers, both outside signs, all three
listed missing-record representatives, and all fifteen residual matchings,
adjoin the missing endpoint quartic determined by the common-kernel product
and squared sum.  Write the remaining outside endpoint as a free variable.
The three exact paired-product equations then have degrees drawn from

```text
(0,4,4), (2,2,4), (2,4,2), (4,0,4), (4,2,2).
```

For every one of the 720 representative systems, the first tested pair has a
square Sylvester multiplication matrix whose determinant is a nonzero rational
function of `x=bc`.  This is certified by exact full rank at the common
specialization `x=2`, where every recorded construction guard and every matrix
denominator is nonzero.

The flattened ranks are:

```text
BC+:  rank 64 in 248 cases; rank 96 in 112 cases,
BC-:  rank 96 in 248 cases; rank 144 in 112 cases.
```

Thus all 720 systems are empty over the generic point of their source curve.
The theorem does not identify or pay determinant-zero fibers, the missing
`BE/CF` systems, the selected-cofactor boundary, or role cell 14.

## Falsifier

A duplicated or absent formal case; a construction guard or matrix denominator
vanishing at `x=2`; a zero specialized determinant; or a selected Sylvester
matrix whose rank is smaller than its size.
