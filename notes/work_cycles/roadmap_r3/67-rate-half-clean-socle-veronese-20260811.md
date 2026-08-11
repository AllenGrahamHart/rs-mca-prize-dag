# Cycle 67: clean socle frame and marked Veronese reduction (2026-08-11)

## Cycle pins

```text
our start:       bcf5f26df
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; updated PR #1151 is already harvested in the DAG
critical open:   28
```

## Residual evaluation direction

For the marked clean point

```text
P_*=(x_0,S),       Q(z;x_0)=A_0(z)S(z),
```

the positive modification direction in the `X`-projection is the fibre
socle class `[A_0]`. The canonical connecting map and Serre duality send it
to

```text
ev_S in H^0(O(m-2))^*.
```

This remains exact when `S` is a repeated supported root: `A_0` then contains
the preceding ramification power and is still the local socle generator. The
nonzero negative-block coordinate independently forces the unique-section
splitting. This is
`rate_half_ca_hankel_clean_endpoint_picard_residual_evaluation_direction`.

## Two-projection socle frame

The reciprocal projection gives the second fibre quotient

```text
C_0(X)=Q(S;X)/(X-x_0)
```

and maps its socle class to `ev_x0 in H^0(O(rho-2))^*`. Hence

```text
(pi_X)_*O_C(P_*)=O+O(1-rho)+O(-rho)^(m-2),
(pi_z)_*O_C(P_*)=O+O(1-m)+O(-m)^(rho-2).
```

The marked point therefore selects rational-normal evaluation directions on
both axes, placing `x_0` directly in the domain coefficient geometry of the
Hankel forms. This is
`rate_half_ca_hankel_clean_endpoint_picard_two_projection_socle_frame`.

## Marked-row elimination

Subtracting `x_0` times each unshifted endpoint frame from its shifted frame
deletes the sole deficient row. If `U` is the remaining joint source support,
column-farness first gives `|U|>=rho`. The full marked Hankel pencil then
excludes both boundary sizes:

- `|U|=rho+1` makes its square Vandermonde factorization invertible;
- `|U|=rho` makes `Q(t;X)` the same fixed domain locator for every generic
  parameter, contradicting the rational-normal motion of `Q`.

Thus

```text
|U|>=rho+2=4m+1.
```

A generic combination of the two source identities has no zero coefficient
on `U` and gives

```text
sum_(x in U) lambda_x v_xv_x^T=0,       lambda_x!=0,
v_x=(Q_0(x),...,Q_m(x)).
```

Every `v_x` is the coefficient vector of a fully saturated squarefree
degree-`m` locator split on the common supported set. This is
`rate_half_ca_hankel_clean_endpoint_marked_row_split_veronese_dependency`.

## Burn-down

```text
result:                  NARROWED; abstract Picard branch made explicit
DAG delta:               +3 PROVED leaves, +7 req edges, +3 ev edges
critical status delta:   none
upstream terminal delta: none; PR #1151 already represented
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The clean endpoint is now the incompatibility of one full-support quadratic
dependence on at least `4m+1` saturated split-locator vectors with their
simultaneous degree-`rho` interpolation and supported-root incidence. A
split-only independence statement would be too broad; the next proof must
retain both structures.
