# Proof

With the exact relative `U/V` normalization, the four fixed-moving mixed
allocation equations are quadratic in `b`. A common root forces all maximal
minors of their `4 x 3` coefficient matrix to vanish and an appropriate
kernel vector to lie on the Veronese conic.

## Common support

The three minor projections share explicit open factors and four relevant
components:

1. `p=0`, which is forbidden;
2. `t^2-4p=0`, the repeated-endpoint boundary;
3. `L=4p+5t+4=0`, carrying a mixed-only quadratic rank curve in `w`;
4. one reciprocal degree-five component, with digest
   `de39723065f2a73569050f7290d326610ebfc5f4d9e4f6db969be30d5c414de9`.

## Degree-five component

The affine `w`-resultant of residual minor 0 and the residual kernel conic is
not divisible by the degree-five component. Their `p`-resultant is the
degree-338 polynomial with digest

```text
a6d9a723529fe31a1c3b5e7e6740ec4c87512f3f00e8473dad75b7ed71750d63.
```

It has 25 irreducible factors. Six have degrees not dividing `6` and hence
no roots in the deployed field. Exact replay on the other factors gives

```text
19 endpoint candidates;
9 boundary;
6 empty at the minor-conic or original-equation gate;
4 admissible quadratic-field q-slice points, at factors 1,2,3,4.
```

For each point reconstruct `H=U+XV` and `G=U^2-WV^2`. The q-slice resultant
first matches `(W-w)^4((W-c^-1)(W-d^-1))^2`. The aligned label locators then
give the necessary full quotient norms

```text
Res_T(P_J,G) ~ K_5^4 q^2,                 (1)
q^2 Res_T(P_I,G) ~ R_7^4.                 (2)
```

All four points fail both `(1)` and `(2)`.

## Linear rank curve

On `L=0`, the nonboundary common-minor factor is

```text
4t^3w^2+22t^3w+99t^3+124t^2w^2+200t^2w+76t^2
+320tw^2+160tw-160t+128w^2-128.           (3)
```

Intersect `(3)` with the raw first-pair kernel conic, before removing any
rank or leading factors. The `w`-resultant has degree 116, ten irreducible
factors, and digest

```text
f1884a7733eb15057db16a451feb9617e6df0e1dc3e281145b9ef7fa8b8ce089.
```

All factor degrees divide `6`. Four factor fields are immediately base
boundary. The other six fields give twelve linear `w` values: nine kill the
explicit `w` or scale guard, and three leave no common `b` in the original
four equations. Thus the raw rank-drop ledger is empty.

## Off-common intersections

After common/open removal, projections `01`, `02`, and `03` have `5`, `4`,
and `1` residual cofactors. All 20 triples are classified exactly. Their
pairwise endpoint norms reduce to five distinct deployed `(p,t)` values,
each killing the base forbidden product. None reaches the `w` gate.

The common components and all off-common projection intersections exhaust
the factorization. Therefore the fixed-mixed allocation is excluded.
