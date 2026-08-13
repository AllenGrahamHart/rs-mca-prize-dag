# Mersenne joint-core charge peeling payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `130199<=e<=130219`

For `r` distinct peeled parameterized affine explanation lines, let
`g_i` be their actual total common-core sizes.  Their inside cores lie in
the same `e`-coordinate gauged support and meet pairwise in at most
`c=K-1` coordinates; each line has at most `c` core coordinates outside
that support.  Hence

```text
sum_i g_i <= S_r := min(r(m-1), e+C(r+1,2)c).
```

A line with total core `g` has at most

```text
f(g)=(N-g)/(m-g)
```

assigned slopes.  Convex endpoint concentration therefore gives an exact
joint charge `L_r` for all `r` removed lines.  The residual target is
`B-L_r`, replacing the previous crude `B-r(N-m+1)`.

Using this target in the proved recursive line-bank argument pays every
support

```text
130199<=e<=130219.
```

At the endpoint, 13 forced lines have inside-core lower bounds

```text
18393, 9736, ..., 9736
```

and

```text
18393+12*9736-C(13,2)*5 = 134835 > 130219.
```

At adjacent `e=130220`, the first 43 positive-core lines give only
`97018`.  The next threshold is `13`, which has zero forced core, and
subsequent thresholds cannot increase.  This is a method wall, not an
unsafe certificate.
