# `A=1` core-one distance-three pair-locator Mobius dichotomy

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`

Let `e>=2` and retain the disjoint exceptional pairs

```text
D_i(X)=(X-a_i)(X-b_i)=X^2-s_iX+p_i.                 (PMD1)
```

The pair locators are distinct monic quadratics, so

```text
dim span{D_1,...,D_e} in {2,3}.                      (PMD2)
```

The dimension is two if and only if there is one nonidentity Mobius
involution `phi in PGL_2(Fbar)` such that

```text
phi(a_i)=b_i,       phi(b_i)=a_i       for every i.  (PMD3)
```

Equivalently, there are scalars `alpha,beta,gamma`, with
`alpha^2+beta gamma!=0`, such that every pair satisfies

```text
beta a_i b_i+alpha(a_i+b_i)=gamma,                  (PMD4)
phi(x)=(gamma-alpha x)/(alpha+beta x).               (PMD5)
```

Thus the pair-Lagrange chart has an exact structural split:

1. a rank-two pair-locator branch owned by one common Mobius involution;
2. a rank-three generic branch.

This theorem classifies the degeneration but does not exclude a Mobius
matching on the official multiplicative subgroup.
