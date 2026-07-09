# F3 h=3 repeat-support forced-point reduction

Status: CONDITIONAL COMPILER PLUS FINITE EVIDENCE.

This packet records a possible route for the quotient-support theorem.  In the
first nonzero boundary-style row currently observed, every active normalized
triple contains the same subgroup element.  If that phenomenon can be proved
or replaced by a small forced-coordinate cover, the support problem reduces to
one-variable PGL2 fibers.

## Pre-registration

Question:

```text
If active repeat-boundary triples are forced to contain a small set of
coordinates, what exact support bound does that imply?
```

Success criterion:

- derive a deterministic reduction from a forced-coordinate cover to
  one-variable fibers;
- verify the reduction on the boundary-style evidence rows;
- keep the forced-coordinate hypothesis explicit.

Failure criterion:

- claim that every row has a forced point from finite evidence;
- hide the factor from ordered triples;
- treat the one-variable PGL2 fiber as already bounded by h=2 affine cosets.

## Reduction

Let `A <= H \ {1}` be a set of forced coordinates with the property that every
active normalized ordered triple `(u,v,w)` has at least one of `u,v,w` in `A`.

For `a in A`, define `N_a` as the number of `v in H \ {1,a}` for which

```text
w_a(v) = 1 - (a-1)(v-1)/(a+v-2)
lambda_a(v) = a+v+w_a(v)-2
```

satisfy

```text
w_a(v) in H,  lambda_a(v) in H,  a,v,w_a(v) distinct.
```

This counts active ordered triples whose first coordinate is `a`.

Because the boundary equations are symmetric in `u,v,w`, the number of active
ordered triples containing a fixed `a` is at most `3 N_a`: each ordered triple
with `a` in one of the three coordinate positions is obtained by moving `a` to
the first coordinate and preserving the order of the other two coordinates.
Therefore

```text
B_line <= 3 sum_{a in A} N_a.
```

Thus a forced-coordinate theorem plus a one-variable PGL2 fiber bound would
prove a support theorem.  For example, if `|A| <= F n^eta` and
`N_a <= K n^gamma`, then

```text
B_line <= 3 F K n^(eta+gamma).
```

This is a different route from LP4 rank: it tries to prove that active lines
are geometrically localized before bounding the remaining fibers.

## Boundary Evidence

On the boundary-style rows currently replayed:

```text
p=257     n=16   B_line=0
p=1153    n=32   B_line=0
p=4289    n=64   B_line=0
p=17921   n=128  B_line=0
p=65537   n=256  B_line=48, common forced coordinate {2}
p=262657  n=512  B_line=0
p=1051649 n=1024 B_line=0
```

For the nonzero row, `N_2=16`, so the reduction is exact:

```text
B_line = 48 = 3 N_2.
```

This is finite evidence only.  It suggests a forced-coordinate support route,
but does not prove one.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_forced_point_reduction.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION_PASS
```
