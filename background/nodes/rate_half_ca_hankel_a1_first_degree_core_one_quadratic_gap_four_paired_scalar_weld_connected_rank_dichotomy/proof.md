# Proof

For a selected fiber `delta`, at most `n` classified rows are roots of
`F_delta`. Hence two fibers `delta,epsilon` have at least

```text
R-|Z(F_delta) intersect X|-|Z(F_epsilon) intersect X|
 >=R-2n                                               (1)
```

common nonincident rows. The two substitutions are

```text
extremal: (3p-3+d_A)-2(p-3)=p+3+d_A,
strict:   (2p+r_A)-2(p-2)=4+r_A.                     (2)
```

Both are positive, so the nonincident row neighborhoods of every two fiber
vertices overlap.

For a classified row `x`, the degree-`m` polynomial `P_x` has at most `m`
roots in the selected fiber set. Thus its degree in `H` is at least

```text
|Z|-m.                                                (3)
```

This is `e+2` in the extremal profile and

```text
(p+2)-(e-1)=p-e+3=(e+5)/2                           (4)
```

in the strict profile. Every row therefore belongs to a fiber neighborhood.
Because all fiber neighborhoods overlap pairwise and cover the rows, `H` is
connected. This proves `(WRD4)--(WRD5)`.

Within one fiber neighborhood, the anchor equations `(SWG4)` relate every
coordinate `lambda_x` to the anchor coordinate by a nonzero scalar. If one
coordinate of a kernel vector is zero, the whole neighborhood is zero;
connectivity then propagates zero to every row. Hence every nonzero vector in
`ker W` has full support.

If `lambda,mu` are two nonzero kernel vectors, their coordinate ratio is
constant inside each fiber neighborhood, again by the anchor equations.
Overlaps and connectivity make that ratio constant on all rows. Therefore
`lambda` and `mu` are proportional, so `dim ker W<=1`. Since `W` has `R`
columns, `(WRD2)` follows.

If `rank W=R`, the scalar-weld theorem excludes a common biform. If
`rank W=R-1`, its unique projective kernel vector is full-support, and the
same theorem says common-biform realizability is equivalent to
`Krow lambda=0`. This proves `(WRD3)`. QED.
