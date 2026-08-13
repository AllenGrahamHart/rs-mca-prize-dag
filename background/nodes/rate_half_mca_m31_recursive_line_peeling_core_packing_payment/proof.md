# Proof

## Residual line bank

Fix a support `e` in the stated interval.  Here

```text
H=e-floor((e-K)/3)-1 >= m,
```

so there is no separate top-union slot and every possible exact deficit is
at most `m`.

Let `Z_r` be the assigned slopes remaining after `r` affine lines have been
removed, and let every member of `Z_r` have deficit at most `U_r`.  The
printed cutoff `b=b_e` passes every prefix guard.  For `b<h<=U_r`, put

```text
A_h=2h-e,
J_h=floor(e(A_h-c)/(A_h^2-ec)).
```

The cutoff also guarantees `2h>e`, `A_h>c`, and `A_h^2>ec`.  Therefore an
explanation in one of these layers owns at most one slope, and the
constant-block Johnson theorem gives at most `J_h` normalized direction
classes relative to a layer anchor.

As in the parent line-bank theorem, each class and the anchor lie on one
affine explanation line.  Padding a nonempty layer with anchor-only slots,
or using the same expression as an upper bound for an empty layer, gives

```text
|Z_r| <= C_r + sum_(i=1)^G_r |L_i|,                 (RP1)
G_r   = sum_(h=b+1)^U_r J_h,
C_r   = P_b(e)+(U_r-b)-G_r.                         (RP2)
```

Here `P_b(e)` is the proved suffix-minimum Johnson/mean-centered prefix.

## Peeling recursion

Every affine explanation line has at most `Q=N-m+1` assigned slopes.  After
`r` lines have been charged, put `T_r=B-rQ`.  If the original family is
unsafe, then `|Z_r|>T_r`.  Combining this strict inequality with `(RP1)`
forces one slot of size at least

```text
lambda_r=ceil((T_r-C_r+1)/G_r).                    (RP3)
```

The replay checks `G_r>0` and `lambda_r>=2` whenever `(RP3)` is used, so
the selected slot is an actual line rather than a padded singleton.  Remove
all assigned slopes on that line.  The next residual has size greater than
`T_(r+1)` unless charging the line already proves safety.  Recomputing the
bank on the residual cannot select the same affine line again.

Total-core line packing gives

```text
g_r=max(0,ceil((lambda_r*m-N)/(lambda_r-1))).       (RP4)
```

At most `c` core coordinates lie outside the gauged direction support, so
the inside core has size at least `u_r=max(g_r-c,0)`.  The parent absorption
argument puts every residual explanation of deficit at least

```text
a_r=e-u_r+K
```

on the selected line.  Consequently the next residual ceiling may be
lowered to

```text
U_(r+1)=min(U_r,a_r-1).                             (RP5)
```

If the suffix-minimum prefix through `U_(r+1)` is defined and at most
`T_(r+1)`, charging the peeled lines and that prefix proves safety.

## Distinct-line core packing

Write a peeled affine line as

```text
c_gamma=a_i+gamma*b_i.
```

Its total common core consists of coordinates where
`(r_0,r_1)=(a_i,b_i)`.  Two distinct affine lines have distinct codeword
pairs `(a_i,b_i)`.  At least one of `a_i-a_j` and `b_i-b_j` is a nonzero
degree-`<K` codeword, so two total cores, and hence their inside-core
subsets, meet in at most `c=K-1` coordinates.  Since all inside cores lie
in the same `e`-coordinate gauged support, first-order inclusion-exclusion
gives

```text
sum_(i=1)^r u_i-C(r,2)c <= e.                      (RP6)
```

A strict reverse inequality is therefore a contradiction.  This remains
valid when `(RP5)` does not lower the deficit ceiling: removing the selected
line still makes the next forced line distinct.

## Finite corridor

Start from `b=65304`.  If the first boundary layer fails a line-bank guard,
raise to the least legal cutoff and then add two guard layers.  The verifier
checks the prefix and line-bank guards at every use; this is the printed
cutoff rule, not a heuristic optimization.

The source-bound endpoint verifier reconstructs the first profile payment,
the first core-packing termination, the last paid support, and the adjacent
wall.  The constant-memory C replay checks all `5,394` support values from
`124806` through `130199`, every recursion stage, the branch census, and the
line-count census.
