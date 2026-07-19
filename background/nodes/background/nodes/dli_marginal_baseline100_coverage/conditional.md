# Conditional proof: DLI 100-bit marginal baseline

## Predicate nodes

- `dli_dyadic_k_core`
- `dli_wcl_zone_coverage`

## Exact assembly

Fix an official row and a production level `L`. The schedule has `N_L=256L`
and the field pin gives `q<2^256`, hence

```text
r_L = q^L/2^(256L) < 1.
```

C1' and WCL-ZONE give

```text
E_L - 1 <= 4r_L(1+W_cl(R,L))
          <= 4(1+1/32) = 33/8,
E_L <= 41/8.
```

There are 34 levels, so

```text
A(R) = product_(L=1)^34 E_L <= (41/8)^34 < 2^100.
```

The last inequality is exact integer arithmetic:

```text
(41/8)^34 < 2^100  <=>  41^34 < 2^202.
```

This proves `dli_marginal_baseline100_coverage` from the two wired predicates.
No C2'' reserve, endpoint certificate, reserve credit, typical-prime
assumption, or floating-point comparison is used.


---

## Corrected derivation (2026-07-13, wave-7 w7-C1, maintainer-ratified schedule r2; the original section above is superseded per #155 — its per-level arithmetic is right, its depth-set identification is not)

## Exact assembly

Fix an official DLI row. Put `t=2^33` and, for `j=0,...,33`,

```text
ell_j = ceil(floor(t/2^j)/2),
N_j   = 256 ell_j.
```

These are the actual odd-index tower dimensions:
`(ell_0,...,ell_33)=(2^32,2^31,...,2,1,1)` and
`sum_j ell_j=t`. The field pin gives `q<2^256`, hence at every level

```text
r_j = q^ell_j/2^(256 ell_j) < 1.
```

C1' and WCL-ZONE give

```text
E_j - 1 <= 4r_j(1+W_cl(R,j))
          <= 4(1+1/32) = 33/8,
E_j <= 41/8.
```

There are 34 levels, so

```text
A(R) = product_(j=0)^33 E_j <= (41/8)^34 < 2^100.
```

The last inequality is exact integer arithmetic:

```text
(41/8)^34 < 2^100  <=>  41^34 < 2^202.
```

This proves `dli_marginal_baseline100_coverage` from the two wired predicates.
No C2'' reserve, endpoint certificate, reserve credit, typical-prime
assumption, or floating-point comparison is used.
