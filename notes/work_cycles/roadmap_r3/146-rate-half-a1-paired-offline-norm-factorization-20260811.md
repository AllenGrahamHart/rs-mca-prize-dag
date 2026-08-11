# Cycle 146: rate-half `A=1` paired off-line norm factorization (2026-08-11)

## Frontier correction

The newly merged Round-34 `Rout` question belongs to the strict `A=3`,
`e=m` endpoint. This worktree closed that entire endpoint in Cycles 71--74,
so another `Rout` audit would not move the live critical frontier. Likewise,
the oriented-gcd/heavy-incidence packet applies to the `rho+3` pair stratum
removed in Cycle 124; it is not an input to the surviving macroscopic pair
boundaries.

The live carrier remains the extremal `(e-2,p-3)` and first-strict
`(e-1,p-2)` split biforms.

## Off-line norm

For either carrier, multiply `G(delta,X)` over every off-line supported
slope. Each classified row is a root of exactly the full parameter-row
degree number of factors. Therefore

```text
product_delta G(delta,X)=L_M(X)^m S_G(X).
```

The extremal residual has degree at most

```text
d_A=0: 3e-9 =549755813880,
d_A=1: 2e-7 =366503875919.
```

Every selected padded-heavy factor lies in `S_G`; when `d_A=1` these are
exactly the selected roots outside the classified rows. The strict carrier
has the analogous exact quotient with degree

```text
[3e^2-4e-7-2r_A(e-1)]/2.
```

The extremal cap is below the classified-row count. Dividing the norm by
the row power and evaluating at each classified row gives

```text
S_G(x)=
 [product_(delta in A_x) partial_X G(delta,x)]
 [product_(delta outside A_x) G(delta,x)]
 /L_M'(x)^(e-2).
```

These values uniquely reconstruct `S_G` by Lagrange interpolation. The
residual is therefore an exact local-tangent object, not an unstructured
unknown polynomial.

An exact audit prevents an incidence-only overfill claim. If
`q_delta=(p-3)-deg_X G(delta,X)`, then

```text
deg S_G=cap-sum_delta q_delta.
```

The cap itself equals the sum of all triple-union excess, all padded-heavy
degree, and, for `d_A=0`, the incidences on the sole exceptional row. These
are the complete capacity, not independent charges beyond it.

## Burn-down

```text
result:                  PROVED paired off-line norm factorization
DAG delta:               +1 PROVED leaf
critical status delta:   none; rate-half crossing remains TARGET
compute:                 exact integer and finite-field tamper replay only
delta-star movement:     none
new assumptions:         none
```

The next route-deciding step is to evaluate these tangent products from the
retained source/Hankel equations or force an additional factor not already
present in the exact slack identity. Generic weld-rank probes and further
strict-`A=3` work have no priority here.
