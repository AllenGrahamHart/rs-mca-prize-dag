# Proof - L1 bounded retained-core payment

Orient every petal as sparse or dense and record its exceptions from the
empty or full baseline. On `p<=P`, the number of exact labelled petal-support
patterns is at most

```text
2^M sum_(j=0)^P binom(Mell,j)
 <=2^M(P+1)n^P.                                       (1)
```

For retained-core size `a`, the exact defect locator is the complement of an
`a`-subset of the fixed core. Hence there are exactly

```text
binom(N,a)<=n^a                                       (2)
```

possible monic split locators `F=L_D`.

For a fixed support pattern and locator, the numerator is unique. Indeed, if
`W_1,W_2` both have degree at most `d` and satisfy the same labelled petal
equations, then `W_1-W_2` vanishes on all `h` petal-support points. The list
threshold and maximality give

```text
h+r_bg>=d+ell,       r_bg<=b<ell,
```

so `h>d`; therefore `W_1=W_2`. Exact-defect, split, saturation, and
no-extra-agreement conditions only discard candidates.

Summing `(2)` over `0<=a<=A` costs at most `(A+1)n^A`. Multiplication by
`(1)` and `2^M<=n^(1/c_0)` proves `(RC3)`. Finally, substituting `d=N-a` in
`d^2<=N(d-g)` and rearranging gives `(RC4)`.
