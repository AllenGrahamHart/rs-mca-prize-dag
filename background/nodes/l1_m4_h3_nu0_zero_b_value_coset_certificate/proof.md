# Proof - L1 m=4, h=3, nu=0 zero-b value-coset certificate

The three monic degree-`p` fiber locators are `R`, `R-s`, and `R+s`. Since
`p` is odd, their root products are respectively

```text
-r,       s-r,       -s-r.                            (1)
```

All roots lie in one multiplicative domain coset, so all three products lie
in its `p`-fold product coset. Dividing the last two products by the first
gives exactly `u=1-z` and `v=1+z` in `K`. The original identity at zero
shows `r(r^2+a)D(0)=-alpha`, so `r`, `u`, and `v` are nonzero. Also `s!=0`
gives `u!=v` and excludes `u=v=1`. This proves `(ZVC1)--(ZVC2)`.

Let `N=p+1`. For every `w in K`, put `theta=w^N in mu_4`; then

```text
w^p=w^(N-1)=theta/w.                                  (2)
```

Raising `u+v=2` to the `p`th power and using (2) gives

```text
epsilon/u+eta/v=2.                                    (3)
```

Substitute `v=2-u` and clear denominators. The result is precisely the
quadratic in `(ZVC3)`.

The checked-in exact verifier reduces both `N`th-power equations modulo this
quadratic over `F_(p^2)`, for all 16 pairs in `mu_4^2`. The independent audit
uses multiplication matrices. They prove the complete table `(ZVC4)`; the
sole pair on the first two characteristics has `u=v=1` and violates
`s!=0`.

For `(epsilon,eta)=(1,-1)`, substitution `u=1-z` turns the quadratic into

```text
z^2+z-1=0.
```

For `(-1,1)` it gives `z^2-z-1=0`. In either case `t=z^2` satisfies

```text
t^2-3t+1=0.                                           (4)
```

Since `t=s^2/r^2=-a/r^2`, clearing `r^4` in (4) yields the invariant in
`(ZVC5)`. This proves both characteristic-dependent conclusions.
