# Cycle 113: core-free cubic two-slope source gate (2026-08-11)

## Cycle pins

```text
our start:       9d79033e0
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         local tiny verifier only
critical open:   28
```

## Two-slope source form

Subtract the affine codeword line through the unique centers at supported
slopes `alpha,beta`. At `alpha`, the derivative pairing becomes

```text
B_alpha(A,B)
 =sum_(x in S_beta\S_alpha) mu_x A(x)B(x),
mu_x!=0.
```

Its proved rank is `c_alpha`, so

```text
|S_beta\S_alpha|>=c_alpha.
```

At equality, Vandermonde inversion forces that difference to be exactly the
root set of `R_alpha`. In the three `w=0` packets every locator-support pair
has union at least `rho`.

## Burn-down

```text
result:                  COUPLED first jet to actual two-slope RS errors
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next combine the known row-wise distribution of excess roots with these
pairwise support differences. Equality is rigid; strict inequality retains
an explicit weighted-moment system rather than an abstract support count.
