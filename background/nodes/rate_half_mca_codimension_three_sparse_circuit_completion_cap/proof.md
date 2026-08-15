# Proof

Write `E_A=span{ev_x:x in A}`.  Evaluation functionals at any at most
thirteen distinct points are independent on `P_13`.

If `T` has evaluation rank ten, annihilator duality gives

```text
dim(Lambda intersect E_T)=11-rank(ev_T|V)=1.          (1)
```

The unique nonzero quotient label in `(1)` has a unique representation in
the evaluation basis on `T`.  Its nonzero support `C_T` is a circuit of the
projected evaluations `ev_x|V`: any proper dependence would give a second
label in `Lambda intersect E_T` or a second support for the same label.
The empty common zero set excludes support one.

Fix `2<=c<=5` and an independent `(c-1)`-set `A`.  Put

```text
H_A={f in V:f|_A=0}.
```

Then `dim H_A=11-c`.  A point `x notin A` which completes `A` to a circuit
is a common zero of `H_A`: the projected evaluation at `x` lies in the span
of those at `A`.  Generalized MDS bounds the total common zero set of
`H_A` by

```text
13-dim H_A=c+2.
```

Since `A` already supplies `c-1` zeros, `A` has at most three circuit
completions.

Suppose some `A` has three completions `x,y,z`.  The three circuit labels
are linearly independent: in any relation among them, the coefficient of
`ev_x`, `ev_y`, or `ev_z` vanishes separately by Vandermonde independence
on

```text
U=A union {x,y,z},       |U|=c+2<=7.
```

They therefore span the three-dimensional `Lambda`, so `Lambda<=E_U`.
Let `mu in Lambda` have another circuit support `D` of size at most five.
It has representations on both `U` and `D`, while

```text
|U union D|<=7+5=12.
```

Vandermonde independence forces the two representations to agree and hence
`D subset U`.  This proves the structured-carrier branch.  Every relevant
support in this branch has size at least two and contributes at most
`C(m-c,11-c)` eleven-sets, giving the first cap in `(C3C)`.

Assume now that no independent set has three circuit completions.  For an
independent `(c-1)`-set `A`, let `b_A<=2` be its number of support-`c`
completions.  If `x` and `y` are distinct completions, their circuit labels
are independent.  Hence a rank-ten eleven-set containing `A union {x}`
cannot contain `y`, by `(1)`.  The number of relevant eleven-sets charged to
the completions of `A` is therefore at most

```text
b_A C(m-c+1-b_A,11-c)
 <=2 C(m-c-1,11-c)                                  (2)
```

at the official `m`; the verifier checks the two integer alternatives.
Every support-`c` circuit is counted exactly `c` times in `(2)`, once after
deleting each of its points.  Summing over the `C(m,c-1)` possible sets `A`
and dividing by `c` proves the second cap in `(C3C)`.

The two branches are exhaustive.  Direct integer evaluation at `m=67485`
gives the printed constants.  QED.
