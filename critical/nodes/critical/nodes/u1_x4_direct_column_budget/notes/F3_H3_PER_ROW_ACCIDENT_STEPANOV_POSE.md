# F3 h=3 per-row accident bound: Stepanov pose

Status: POSED TARGET + PROVED ARITHMETIC COMPILER.  This is bonus item (iii):
pose the h=3 per-row accident bound precisely, with the auxiliary-polynomial
ansatz written out.

This is not a proof of the per-row accident bound.  It is a clean target that
turns the h=3 norm-gate evidence into one explicit theorem statement.

## Pre-registration

Target object:

```text
H = mu_n <= F_p^*,    p = 1 mod n,    p >= n^2.
```

For h=3, let `A_3(n,p)` be the number of dilation-normalized non-toral
activated shape orbits: unordered disjoint triple pairs `{P,Q}` in `H`, modulo
common multiplication by `H`, such that `e1(P)=e1(Q)`, `e2(P)=e2(Q)`, and the
pair is not a pair of `mu_3` cosets.

Measured rows suggest `A_3(n,p)` is usually `0` or `1`; the full `n=96`
oriented core-slice census has activation rate `720/11808706`.

The theorem to prove is deliberately weaker:

```text
H3-ACCIDENT(C):  A_3(n,p) <= C n        for all p = 1 mod n, p >= n^2.
```

Any absolute `C` is already enough for the F3 floor with wide margin; `C=16`
is the default arithmetic compiler constant below.

Falsifier:

```text
a row (n,p) with more than C n activated non-toral h=3 dilation-shape orbits.
```

Such a row is machine-checkable by the existing core-slice resultant/common-root
pipeline.

## Arithmetic Compiler

At `q=p >= n^2`, the h=3 contribution decomposes as:

```text
T_3 <= toral + poisson_boundary + n * A_3(n,p).
```

The toral term is

```text
binom(n/3,2)       if 3 | n,
0                 otherwise.
```

The random boundary collision scale is at most

```text
binom(n,3)^2 / (2 p^2) <= n^2 / 72.
```

Thus `H3-ACCIDENT(C)` gives

```text
T_3 <= binom(n/3,2)[3|n] + n^2/72 + C n^2 = O_C(n^2),
```

which is far below the `n^3` F3 floor once `n` is modest.  The replay script
checks this arithmetic threshold for `C=16`; it gives `T_3 < n^3` for
`n >= 17`, leaving `n=16` to the existing direct small-row gates.

## Stepanov/Hyperbola Ansatz

For a triple with elementary data `(s_1,s_2,s_3)`, write

```text
F_{s_1,s_2}(X) = X^3 - s_1 X^2 + s_2 X.
```

Two triples with equal `e1,e2` are two distinct fibers of this cubic restricted
to `H`; the fiber value is `s_3`.

The proved h=3 hyperbola normal form says that, when a primitive cube root
`omega` lies in `F_p`, same-fiber pairs of the quadratic divided difference

```text
G_F(u,v) = (F(u)-F(v))/(u-v)
```

are equivalent after an explicit linear change of coordinates to

```text
X(u,v) * Y(u,v) = Delta(F).
```

Therefore activated non-toral h=3 shapes are controlled by a bounded family of
shifted-subgroup product incidences:

```text
u, v in H,        L_1(u,v) L_2(u,v) = Delta,
```

together with the second fiber compatibility condition for the partner triple.

The Stepanov target is a multi-Delta rich-value theorem:

```text
For H <= F_p^*, |H|=n<=p^(1/2), the number of dilation-normalized non-toral
two-fiber cubic configurations whose hyperbola parameters activate at a fixed
p is O(n).
```

Auxiliary-polynomial ansatz:

```text
Psi(U,V) = Phi(U,V, U^n, V^n, L_1(U,V)^n, L_2(U,V)^n)
```

where `Phi` has bounded degree in the affine variables and Stepanov-scale
degrees in the subgroup variables.  The intended vanishing conditions are
imposed simultaneously on all rich activated hyperbola parameters at the fixed
prime.  The needed proof has the same three gates as Terminal B:

1. enough coefficients after imposing multiplicity;
2. nonvanishing modulo the subgroup/hyperbola equations;
3. degree/multiplicity contradiction producing `A_3(n,p) <= Cn`.

This pose is intentionally weaker than a full classification of activated
shapes.  It only asks for a per-row rich-value bound.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_per_row_accident_pose.py
```

Expected digest:

```text
H3_PER_ROW_ACCIDENT_POSE_PASS
```
