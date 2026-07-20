# Proof - L1 cross-quotient split-descent obstruction

Direct multiplication verifies that `F_0` and `F_1` are the monic locators of
the two sets in `(SQ2)`. Evaluation verifies

```text
W_j(x)=c_iF_j(x)  at x=8+i,
W_j(13)=0,
W_j(14+i)!=c_iF_j(14+i) for every i.                    (1)
```

The numerators are nonzero on every root of their corresponding locators, so
`gcd(F_j,W_j)=1`. Thus the missed core is exact and both pairs are saturated.
The retained core contributes four agreements, `(1)` contributes five petal
agreements and one background agreement, and `k=9`; hence both pairs meet
the exact threshold `k+ell-1=10`.

Polynomial division gives `(SQ3)`. The quadratic discriminant is

```text
15^2-4*20*15=14 mod 23.                                 (2)
```

The nonzero squares modulo `23` are
`{1,2,3,4,6,8,9,12,13,16,18}`, so `(2)` is nonsquare. The quotient therefore
does not split over `F_23`. Finally `(SQ4)` is direct arithmetic, placing the
witness outside the positive-Johnson payment.
