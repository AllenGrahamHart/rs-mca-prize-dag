# Proof

Fix corank `d` in the completely shortened chart.  Here `K=s=d`, so the
support-local common-zero bound gives `z<=K-s=0`: every incident normal is
nonzero.  The chart has

```text
n=1048576+d,       m=67472+d.
```

For every proper normal span of vector dimension `r<d`, support-local MDS
transversality leaves at least `w+d-r=m-r` incident normals outside it.
Thus that span contains at most `r` incident normals.  Every set of at most
`d` normals is independent.  Same-support pair noncontainment gives full
incident rank `d+1`.

Apply `matroid_paving_basis_floor` with matroid rank `d+1`.  There are at
least `C(m-1,d)` unordered bases, hence at least

```text
(d+1)! C(m-1,d)=(d+1)(m-1)_fall_d
```

ordered bases.  An independent `(d+1)`-tuple of affine agreement
hyperplanes meets in at most one parameter point.  The record count is
therefore at most the floor of

```text
P_d=(n)_fall_(d+1)/((d+1)(m-1)_fall_d).
```

Exact division gives the nine caps and remainders in the source contract.
The argument uses `z=0` essentially; it does not promote these values to a
chart before complete shortening.
