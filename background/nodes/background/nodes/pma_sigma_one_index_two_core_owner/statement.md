# PMA sigma-one index-two near-core owner

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **evidence consumer:** `pma_wide_residual`
- **role:** global owner for the reciprocal-quadratic obstruction and every
  listed codeword with the same four-defect index-two core signature

## General owner

Let `H` be cyclic of even order `n`, put `N=n/2`, and let `B_0,B_1` be
the two cosets of the unique subgroup of order `N`. Let `U:H->F`, let
`P` range over polynomials of degree less than `k`, and put

```text
A_P={x in H:P(x)=U(x)}.
```

Assume `|A_P|>=a>=k+1`. Fix `s>=0`. For `0<=e<=s`, put

```text
q_e=max(0,k-N+e).
```

Whenever `q_e<=N`, the source-level class

```text
CORE_s(U)={P: |B_i\A_P|<=s for some i in {0,1}}
```

has the chart-independent bound

```text
#CORE_s(U)
 <= 2 sum_(e=0)^s binom(N,e) binom(N,q_e).             (CORE)
```

The owner chooses the first qualifying coset, records its exact missed set,
and records the first `q_e` outside agreements. These data contain at least
`k` agreement points and therefore determine `P` uniquely.

## Official finite corollary

On the official dyadic `sigma=1` grid

```text
n=2^j, 13<=j<=44,
rho in {1/2,1/4,1/8,1/16},
k=rho n, N=n/2,
h=k/2+1,
Q_2(k+2)=binom(N-1,h),
```

apply `(CORE)` with `s=4` after the exact-periodic owner. Then

```text
#QOWN_core4 <= 2 sum_(e=0)^4 binom(N,e) binom(N,q_e)
             <= 10 N^8
             < Q_2(k+2).                              (FINITE-CORE)
```

Together with `pma_exact_periodic_owner`, both global source classes fit one
existing first-scale quotient-profile line:

```text
#(QOWN_per union QOWN_core4)
 <= 8(1+2^-690) Q_2(k+2)
 < 719(1+2^-690) Q_2(k+2).                            (COMBINED)
```

There is no sunflower, defect-chart, or petal-pairing multiplier.

## Reciprocal-quadratic subsumption

Every codeword counted by
`pma_sigma_one_d3_reciprocal_quadratic_obstruction` agrees on

```text
G \ ({b} union D),    |{b} union D|=4,
```

where `G` is the index-two subgroup. It is therefore in `QOWN_core4`, even
though its full agreement stabilizer is trivial. The explicit `Omega(n^7)`
per-sunflower family is now globally owned and removed before the complementary
diffuse incidence is charged.

## Scope

The general interpolation owner is independent of `sigma`; `(FINITE-CORE)`
and `(COMBINED)` are the official finite `sigma=1` absorption only. This
theorem does not bound the complementary diffuse class, defects `d>=4`, chart
composition, or the asymptotic `GROW union RES` residual.
