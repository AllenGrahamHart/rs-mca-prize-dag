# F3 h=3 repeat forced-fiber degree bound

Status: PROVED ELEMENTARY FIBER BOUND.

This packet strengthens the forced-coordinate route from
`F3_H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION.md`.  The forced-fiber Stepanov
compiler is useful if one wants sublinear fiber bounds, but a simple degree
argument already gives a linear bound for every fixed forced coordinate.

## Statement

Fix `a in H \ {1}` and define

```text
w_a(X) = 1 - (a-1)(X-1)/(a+X-2),
lambda_a(X) = a+X+w_a(X)-2.
```

Let `N_a` count `X in H` for which

```text
w_a(X) in H,  lambda_a(X) in H,
```

with the usual exclusions for poles and repeated coordinates.  Then

```text
N_a <= 2n.
```

## Proof

Drop the condition `w_a(X) in H`; this can only increase the count.  The map
`lambda_a` has the form

```text
lambda_a(X) = P_a(X)/(a+X-2),
```

where `P_a` is quadratic with leading coefficient `1`.  Therefore for every
`mu in H`, the equation

```text
lambda_a(X) = mu
```

is, after clearing the nonzero denominator, a polynomial equation of degree
two in `X` with leading coefficient `1`.  It has at most two solutions.  Since
there are `n` choices of `mu in H`,

```text
N_a <= 2n.
```

## Consequence for Forced Covers

If a forced-coordinate set `A0` covers every active normalized triple, then
the forced-point reduction gives

```text
B_line <= 3 sum_{a in A0} N_a.
```

Using `N_a <= 2n`,

```text
B_line <= 6 |A0| n.
```

Consequently,

```text
repeat_residue <= 72 |A0| n^2 + 18 n^2.
```

Thus a forced-coordinate cover of size `O(n^eta)` with `eta < 1` would pay the
repeat residue subcubically.  A constant-size forced-coordinate cover would pay
it quadratically.

This does not prove such a forced-coordinate cover.  It reduces the forced
route to proving that active triples are covered by a small set of coordinates.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_degree_bound.py
```

Expected digest:

```text
H3_REPEAT_FORCED_FIBER_DEGREE_BOUND_PASS
```
