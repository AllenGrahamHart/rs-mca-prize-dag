# Cycle 472: quotient-periodic exception-SPI fence

## Starting pins

```text
our SHA: 47fe89585
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED route fence

Let the smooth domain be `mu_N` with `N` a power of two. For every
`e in {1,2,4,8}`, the map `x -> x^e` is a quotient

```text
mu_N -> mu_(N/e)
```

with kernel `mu_e`. Hence each polynomial

```text
X^e-y,       y in mu_(N/e),
```

is a split squarefree degree-`e` domain locator, and distinct `y` give
disjoint root cosets. Taking `u=X^e`, `v=1`, and `gamma=-y` realizes
exactly the abstract exception-pencil equation with coprime generators and
nonzero scalar.

On the official `N=2^21` domain the fiber counts are

```text
2097152, 1048576, 524288, 262144
```

for `e=1,2,4,8`. Thus twenty disjoint split fibers cannot be excluded or
bounded from the abstract SPI interface. The survivor is precisely a
quotient-periodic power-map class of the kind anticipated by the upstream
inverse program.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: naive twenty-fiber emptiness fenced; periodic/nonperiodic dichotomy required
new assumptions: none
next action: classify nonperiodic e<=11 pencils and price periodic lifts using retained branch semantics
```

## Nonclaims

- no received pair, rational certificate, or heavy-ruling lift is
  constructed;
- no MCA counterexample or rational payment;
- no adjacent-row safety or prize closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_quotient_periodic_fence/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_quotient_periodic_fence/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_quotient_periodic_fence/verify_audit.py
```
