# Clean-endpoint Picard multiplication injectivity reduction

- **status:** PROVED
- **closure:** exact cohomology and relative bundle reduction
- **consumer:** `rate_half_band_crossing_location`

Retain the degree-one Picard pin on the absolutely irreducible curve
`C:Q=0` of bidegree `(rho,m)`:

```text
O_C(N,-T)=O_C(P_*),
rho=4m-1,       N=16m,       T=4m+1.                (PMI1)
```

Multiplication by `Q` induces the explicit map

```text
mu_Q:
H^1(P^1xP^1,O(N-rho,-T-m))
 -> H^1(P^1xP^1,O(N,-T)).                            (PMI2)
```

Every clean endpoint failure forces

```text
ker mu_Q!=0.                                         (PMI3)
```

The exact dimensions are

```text
dim source=(12m+2)(5m)=60m^2+10m,
dim target=(16m+1)(4m)=64m^2+4m.                    (PMI4)
```

Equivalently, project to the domain line. Multiplication by `Q` gives a
fiberwise-surjective vector-bundle map

```text
O(N-rho)^(5m) -> O(N)^(4m)                          (PMI5)
```

with kernel bundle `K_Q` satisfying

```text
rank K_Q=m,
deg K_Q=5m(N-rho)-4mN=m(5-4m),
H^0(P^1,K_Q)!=0.                                     (PMI6)
```

The same `Q` also carries the four-Hankel bi-isotropic coefficient frame of
the preceding theorem. At the level of this reduction, either of the
equivalent statements

```text
mu_Q is injective,
every Birkhoff-Grothendieck summand of K_Q has negative degree             (PMI7)
```

would exclude the clean endpoint.

## Scope

`deg K_Q<0` alone does not prove `(PMI7)`: an unbalanced bundle can have a
nonnegative summand and negative total degree. The subsequent elementary-
modification theorem audits this candidate and proves that `(PMI7)` is in
fact impossible. This node is retained as the exact cohomological bridge,
not as the live closing strategy.
