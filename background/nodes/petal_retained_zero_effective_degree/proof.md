# Proof

Every polynomial `G` of degree at most `d` vanishing on all points of `R` is
uniquely divisible by the monic locator `L_R`; write

```text
G=L_R Q,    deg Q<=d-r.
```

Conversely every such `Q` gives a degree-`<=d` polynomial vanishing on `R`.
Since `R` and `T` are disjoint, `L_R(x)` is nonzero for every `x in T`, and

```text
G(x)=W(x)  iff  Q(x)=W(x)/L_R(x).
```

Thus `G->Q` is a bijection of the two lists and preserves every agreement
position, not merely the number of agreements. Any exact-support property,
including stabilizer-primitivity, is therefore preserved.

Distinct degree-`<=d-r` polynomials agree on at most `d-r` points. Applying
`petal_k4_johnson_slice` with effective degree `d-r` gives the displayed
bound whenever `a^2>(d-r)|T|`. In G1 notation, `|T|=mell` and
`a=ell+d-r`; substituting gives the final criterion and shows that its weak
reverse is the sole effective-degree range left to K4.
