# Proof

For an independent target deletion `A` of size `d-1`, put

```text
H_A={f in V:f|_A=0}.
```

Independent evaluation gives `dim H_A=11-d`.  Grassmann in the
ten-dimensional space `V` gives

```text
dim(W intersect H_A) >= g+(11-d)-10 = g+1-d=r_d.       (1)
```

The intersection vanishes on `D` and on the complete target carrier
`U_A`.  When `r_d>0`, the common-root bound therefore gives

```text
|U_A setminus D| <= K-r_d-u=R_d.                       (2)
```

There are at most `C(u,d)` target circuits wholly inside `D`.  A target
circuit with exactly `j>=1` points outside `D` is exposed by deleting each
of those `j` points.  The remaining independent deletion has `j-1` points
outside `D`, so `(2)` leaves at most

```text
max(0,R_d-(j-1))=max(0,R_d-j+1)
```

outside completions.  There are at most

```text
C(u,d-j) C(m-u,j-1)
```

such deletions.  Every circuit in this stratum is counted exactly `j`
times.  Multiplication, division by `j`, integer flooring, and summation
prove `(MC1)`.  Each target circuit extends to at most
`C(m-d,11-d)` selected eleven-sets.  QED.
