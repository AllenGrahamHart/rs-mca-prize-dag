# F3 h=3 private-linear two-factor resultant relation

Status: PROVED ROUTE CUT / STRUCTURAL EXPLANATION, NOT THE THREE-FACTOR RANK
THEOREM.

The earlier two-factor guardrail gave a rational counterexample to naive
factor-by-factor rank induction.  This packet explains that loss: in the first
nontrivial two-factor box, there is always a bidegree `(2,2)` resultant
relation.

## Resultant Relation

Set

```text
u = ((X-alpha)/(X-beta))^2,
v = ((X-gamma)/(X-delta))^2.
```

Eliminating `X` from

```text
(X-alpha)^2 - u (X-beta)^2 = 0,
(X-gamma)^2 - v (X-delta)^2 = 0
```

gives

```text
Res_X((X-alpha)^2-u(X-beta)^2,
      (X-gamma)^2-v(X-delta)^2) = 0.
```

The replay verifies that this resultant has degree `2` in `u`, degree `2` in
`v`, and all nine monomials `u^i v^j`, `0<=i,j<=2`.

Multiplying by the common denominator

```text
(X-beta)^4 (X-delta)^4
```

turns this into a linear relation among the nine private-linear products

```text
(X-alpha)^(2i)(X-beta)^(2(2-i))
(X-gamma)^(2j)(X-delta)^(2(2-j)),
0 <= i,j <= 2.
```

Therefore the `A=1,B=3,H=2` two-factor span has rank at most `8` for structural
reasons.  The replay checks several rational parameter choices have exact rank
`8`, so the relation is the whole loss in those generic samples.

## Connection To The Guardrail

For the original guardrail parameters

```text
(alpha,beta,gamma,delta) = (2,3,5,7),
```

the resultant coefficient vector, ordered lexicographically by `(i,j)`, is

```text
(81, -450, 625, -72, 472, -800, 16, -128, 256),
```

which is exactly the integer relation recorded in
`F3_H3_PRIVATE_LINEAR_TWO_FACTOR_GUARDRAIL.md`.

## Consequence

The private-linear route cannot prove the three-factor rank theorem by showing
that each one-factor valuation interval contributes independently and then
tensoring the factors.  Once two degree-2 private maps share the same source
line, their images lie on a bidegree `(2,2)` curve in `P^1 x P^1`.

This does not refute the official private-linear route.  It says the remaining
proof must exploit the full three-generator geometry or the repaired F3
signature-curve hypotheses, not a naive product induction.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_two_factor_resultant.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_TWO_FACTOR_RESULTANT_PASS
```
