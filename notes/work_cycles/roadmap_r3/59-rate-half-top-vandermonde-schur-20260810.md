# Cycle 59: rate-half top Vandermonde Schur reduction (2026-08-10)

## Universal rank payment

Normalize the parameter basis so every coordinate linear factor `L_x` has a
nonzero leading coefficient. In the deficiency-aware matrix, the highest
clone at each point then has top parameter coefficient `c_(1,x)`, while all
lower clones have zero top coefficient. The `j=m+1` slice is therefore a
scaled Vandermonde matrix on `W`.

Any `4m+1` point columns form an invertible pivot block. Exact Schur
elimination proves

```text
rank(M_W)=4m+1+rank(S_W),
v_W:=columns(S_W)=|W|+Delta_W-(4m+1).
```

Consequently

```text
v_W<=4m-2     on |W|<=7m-1,
v_W<=3m-1     when additionally O=0.
```

## Frontier

`rate_half_bivariate_top_vandermonde_schur_reduction` is added as a proved
leaf. It pays the universal part of the rank problem and localizes the
remaining theorem to a much smaller residual matrix.

The controls line up: the genuine `m=1` failure has residual width one and
rank zero; the bounded `m=2` bad-pattern campaign tests widths `2..5` and
always finds full residual rank. The next task is to derive an incidence-level
formula or minor system for `S_W` and connect bad overlap to its column
independence. No critical status changes.
