# Proof - L1 full-pullback divisibility/Johnson closure

## 1. Dyadic threshold arithmetic

Because `s|n` and `n` is a power of two, `s` is a power of two. The official
dimension `k` is also a power of two. Since `s|ell`, equation `(FJ1)` gives

```text
a_* congruent k-1 mod s.                              (1)
```

If `s<=k`, then `s|k`, so `(1)` is `-1 mod s`. If `s>k`, then `k|s` and
`1<k<s`, so `k-1` is nonzero modulo `s`. Thus `s` never divides `a_*`.

A union of complete degree-`s` fibers has size divisible by `s`, proving the
exact-shell exclusion. The least allowed quotient agreement is
`h_0=ceil(a_*/s)`. In the first case the next multiple is `k+ell`; in the
second it is `ell+s`. This proves `(FJ3)`.

## 2. Pairwise quotient agreement

By `l1_general_pullback_interleaving_descent`, the full domain partition has
`kappa=0`; every codeword injects into an `s`-component quotient tuple whose
components have degree below `K_0` on `b` distinct labels. Two distinct tuples
differ in at least one component. The difference polynomial has degree at
most `d=K_0-1`, so the two tuples can agree simultaneously in all components
on at most `d` labels.

Fix a received quotient word and a list of `L` tuples agreeing on at least
`h_0` labels. Retain canonically exactly `h_0` agreement labels for each
tuple. If `m_x` is the number of retained sets containing label `x`, then

```text
sum_x m_x=Lh_0,
sum_x binom(m_x,2)<=binom(L,2)d.                       (2)
```

Cauchy--Schwarz gives

```text
sum_x binom(m_x,2)
 >=((Lh_0)^2/b-Lh_0)/2.                               (3)
```

Combining `(2)` and `(3)` and cancelling `L/2` yields

```text
L(h_0^2-bd)<=b(h_0-d).                                (4)
```

Under `(FJ4)`, division proves the first bound in `(FJ5)`. The denominator is
a positive integer. Validity `a_*<=n` gives `h_0<=b`, and hence
`h_0-d<=b`, so the bound is at most `b^2`.

## 3. Printed gate and aggregation

If `s<=k`, then `K_0=k/s`, `d=(k-s)/s`, `b=n/s`, and
`h_0=(k+ell)/s`. Multiplying `(FJ4)` by `s^2` gives `(FJ6)`. If `s>k`, then
`K_0=1`, so `d=0` and `(FJ4)` is immediate.

The tame fixed-petal census gives at most `n` map classes across the fixed
source. Union bounding `(FJ5)` over those classes gives `(FJ7)`. Duplicate
ownership can only decrease this bound. This proves the claimed sector
closure.
