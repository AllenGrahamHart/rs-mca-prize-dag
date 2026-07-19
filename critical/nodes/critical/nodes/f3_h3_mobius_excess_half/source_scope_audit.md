# Source and normalization audit for the cutoff-18 route

Date: 2026-07-12.

## Exact block form

Let `B` range over the proved quotient coefficient blocks and put

```text
Q_18(B)=sum_(t in B,P(t)>=19) [P(t)(P(t)-2)+D(t)].
```

Since `R(t)=|B|-1` is constant on each block,

```text
S_ns^rich=sum_B (|B|-1)Q_18(B).                   (BNS18)
```

Thus the missing theorem is a correlation bound between quotient-block size
and rich non-swap product-collision mass. A marginal block-size tail or
ordinary shifted energy does not by itself prove `(BNS18)<=1200n^2`.

## Konyagin--Shparlinski--Vyugin

The product fiber is the subgroup point count on

```text
P_t(X,Y)=XY-X-Y+1-t=0.
```

For `t!=0`, this is an irreducible bidegree `(1,1)` curve. Theorem 1.2 of
Konyagin--Shparlinski--Vyugin, *Polynomial Equations in Subgroups and
Applications* (arXiv:2005.05315), requires the lowest nonzero homogeneous part
`P_t^sharp` to contain at least two monomials. Here

```text
P_t^sharp=1-t,
```

a single nonzero constant. The theorem therefore excludes this shifted-product
family. The same paper's Conjecture 1.3 is a constant bound for a general
Möbius subgroup intersection; it is a conjecture, and its stated small-subgroup
range is not an official near-square-root theorem.

## Macourt--Shkredov--Shparlinski

Corollary 4.1 of *Multiplicative Energy of Shifted Subgroups and Bounds on
Exponential Sums with Trinomials in Finite Fields* (arXiv:1701.06192) bounds

```text
E_x(A)=sum_t P(t)^2
```

with an implicit `O(n^2 log n)` term in the relevant regime. It does not bound
the correlated moment `(BNS18)`, and multiplying by a pointwise bound for `R`
loses a power of `n`. Even if a direct proof established
`S_ns<=C n^2 log n`, the official maximum `log n=41 log 2` would require

```text
C <= 1200/(41 log 2) < 42.24.
```

No such explicit correlated theorem is printed in the audited source.

## Verdict

The current source route is `OPEN GAP`, not a citation close. The independent
proved norm-cutoff packet closes `p>6^(n/4)`. On the remaining range, a
successful proof must control the joint rich-block moment `(BNS18)`, retain
product/quotient correlation in a rich-level argument, or exploit the oriented
character phases. The cutoff optimization makes an explicit logarithmic proof
plausible but does not supply it.

The in-repo theorem `f3_h3_shifted_product_sidon` additionally proves that
the non-swap product-collision factor has no characteristic-zero component at
dyadic order. Thus a norm-divisor aggregation is now a fourth honest route.
Its per-collision divisibility statement does not control concentration at one
prime and is not itself a bound for `(BNS18)`.

## Combined-equation check

Eliminating the shared parameter from one product and one quotient
representation gives

```text
(1-x)(1-y)(1-z)=1-w,  x,y,z,w in H.
```

Its constant terms cancel and its lowest homogeneous part is
`w-x-y-z`, so it avoids the single-monomial defect of an individual product
fiber. This does not create a citation close: Konyagin--Shparlinski--Vyugin
Theorem 1.2 is a theorem for one irreducible bivariate polynomial on `H^2`,
whereas this is a four-variable hypersurface. Fixing any two variables
generically restores a nonzero constant lowest term in the remaining
bivariate equation. A multivariate Stepanov theorem with explicit constants
would be new input, not an instance of the cited result.
