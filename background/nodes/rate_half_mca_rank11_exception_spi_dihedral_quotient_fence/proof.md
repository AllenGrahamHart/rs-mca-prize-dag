# Proof

The map `x -> x^d` sends `mu_N` onto `mu_M` and has kernel `mu_d`.
Therefore each `z in mu_M` has exactly `d` distinct preimages in `mu_N`.

Since `mu_M` is cyclic of even order, a generator is a nonsquare; fix such
an `a`. A fixed point of `iota(z)=a/z` would satisfy `z^2=a`, contrary to
the choice of `a`. Thus `iota` partitions `mu_M` into `M/2` two-element
orbits.

For one orbit, direct multiplication proves `(DQ1)`. Its two factors have
disjoint root sets because `z != a/z`, and each factor has `d` simple roots:
the characteristic is odd and does not divide `d`. All `2d` roots lie in
`mu_N` by the preceding homomorphism calculation.

If

```text
z+a/z=w+a/w,
```

then multiplication by `zw` gives

```text
(z-w)(zw-a)=0.
```

Hence `w=z` or `w=a/z`; equal slopes therefore represent the same orbit.
Different orbits are disjoint in `mu_M`, so their full preimages under
`x -> x^d` are disjoint in `mu_N`. This proves both the exact fiber count
`M/2=N/(2d)` and pairwise coprimality of the locators.

Finally `u(0)=a != 0` while `v=X^d`, so `gcd(u,v)=1`; the pencil members in
`(DQ1)` are monic, giving scalar one. All exception-SPI conditions stated in
the node follow. QED.
