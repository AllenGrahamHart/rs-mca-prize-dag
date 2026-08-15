# Proof

After rank-seven canonical-basis cancellation, delete all global zero-normal
coordinates and write

```text
t=K'-10-z,              0<=t<=1048566,
a=t+1,
r=67474.
```

The remaining chart has

```text
n=1048579+t,       K=3+t,       m=67475+t=a+r,       s=3.
```

Its incident normal matroid at every selected record is loopless rank four.
For a one-dimensional normal span, support-local transversality leaves at
least `67474` incident normals outside, so every parallel class has size at
most

```text
m-67474=t+1=a.
```

For a two-dimensional normal span it leaves at least `67473` outside, so
every rank-two flat has size at most

```text
m-67473=t+2=a+1.
```

Apply `matroid_rank4_bounded_point_line_basis_floor`.  If `b` is the number
of unordered incident bases, then

```text
6b>=Q_a(r),       r=67474.
```

Thus each record owns at least `24b>=4Q_a(r)` ordered independent coordinate
quadruples.  Four independent affine agreement hyperplanes meet in at most
one parameter point, so

```text
M_3(t)<=floor(
  (1048576+t)(1048577+t)(1048578+t)(1048579+t)
  /(4Q_(t+1)(67474))
).                                                       (UC3)
```

It remains to compare the finite official parameter range.  Unfolding the
recurrence gives a base path and coloop-reset candidates

```text
C_a(j)+sum_(x=j+1)^r L_a(x).
```

Their successive difference has sign `3h_a(x)-a-2`, so only one reset can
minimize.  The sum of `h_a(x)(x-2)` is evaluated by splitting at the constant
branch of `h_a` and into the four residue classes of `a+x modulo 4`.
Consequently each row is checked with a fixed number of exact integer
operations, not by iterating the recurrence to depth `67474`.

The source-pinned verifier and bounded Modal replay exhaust all `1048567`
rows.  They find

```text
maximum cap:       983902549 at t=0,
adjacent cap:      983891721 at t=1,
far-endpoint cap:  951742008 at t=1048566,
first excess:      none.
```

At `t=0`, the division remainder is `1056607358217600` and the next-integer
gap is `172104506923776`.  Hence the floor is exactly `983902549`, and every
other official row is no larger.  This proves `(UC3)` uniformly.
