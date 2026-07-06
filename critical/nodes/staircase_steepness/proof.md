# staircase_steepness proof

The leading aligned stratum has the exact shape

```text
M(j,t) = binom(n,j) (1 - q^(-t)) q^(1-t),
```

with `t = n - k - j` on an adjacent grid. Moving one grid step from `j` to
`j + 1` changes `t` to `t - 1`, so for `t > 1`

```text
M(j + 1, t - 1) / M(j,t)
  = ((n - j) / (j + 1))
    q
    ((1 - q^(1-t)) / (1 - q^(-t))).
```

The last factor is bounded above and below by absolute constants in the
corridor, and the binomial factor is a row-scale factor already included in
the corridor arithmetic. Thus one adjacent grid step changes the leading term
by a field-size factor, up to the explicit row constants.

The ACL terms used in the same corridor comparison have the same form: a
fixed row-scale coefficient multiplied by a power of `q` whose exponent
changes by one when `t` changes by one. Their adjacent ratios are therefore
the same kind of explicit `q`-scale ratios.

Consequently a candidate comparison against `B*` only needs relative
precision much coarser than an adjacent-step factor. The only excluded case is
the one named in the node statement: if the exact count lies inside the error
band of `B*`, then the coarse expansion cannot decide the sign and the row is
a knife-edge census cell.
