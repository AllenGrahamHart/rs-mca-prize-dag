# L1 m=4 positive-valuation value-coset certificate

- **status:** PROVED
- **dependencies:** `l1_m4_h3_colored_cyclic_equivalence`,
  `l1_m4_h3_tangent_radical_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Fix an official `n=4(p+1),h=3` record with positive depressed inner
valuation `nu>0`. Its three depressed split values are nonzero and lie in one
multiplicative coset of the order-`n` subgroup. After scaling one value to
one, write them as

```text
1,u,v,       1+u+v=0.                                  (VCC1)
```

Put `N=p+1` and

```text
epsilon=u^N,       eta=v^N in mu_4.                    (VCC2)
```

Then every valid ordered pair is a common root of

```text
q_(epsilon,eta)(U)=U^2+(1+epsilon-eta)U+epsilon,
U^N-epsilon,
(-1-U)^N-eta.                                          (VCC3)
```

Exact quotient-ring certificates for all 16 pairs give

```text
p=8191:        no pair,
p=131071:      no pair,
p=524287:      (epsilon,eta)=(1,-1),(-1,1),(-1,-1),
p=2147483647:  (epsilon,eta)=(1,-1),(-1,1),(-1,-1).    (VCC4)
```

In each surviving quarter pair both roots of the quadratic are valid and
nondegenerate. The resulting six ordered pairs are the permutations of one
projective triple, normalized as the roots of

```text
Y^3-2Y+1=(Y-1)(Y^2+Y-1).                               (VCC5)
```

Consequently:

```text
p in {8191,131071}: no positive-valuation m=4,h=3 record;
p in {524287,2147483647}: every such record has
                          a^3+8b^2=0.                  (VCC6)
```

Here `Y^3+aY+b` is the depressed outer cubic. This does not exclude `nu=0`,
or the two surviving positive strata on the latter characteristics, classify
nonembedded `h=2`, treat `m=8,16`, or close L1.
