# L1 m=4, h=3 tangent-radical exclusion

- **status:** PROVED
- **dependencies:** `l1_m4_h3_cartier_resonance_reduction`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Let `eta=deg H`. For a surviving positive valuation `nu in {1,2,3}`, put

```text
y_0=-3b/(2a),
kappa=4alpha y_0/(g(y_0)),
T=2aR+3b,
P=X^nu H-kappa.                                         (TRE1)
```

Then `b`, `y_0`, and `g(y_0)` are nonzero, and

```text
rad(T) divides P,
deg rad(T)<=nu+eta.                                     (TRE2)
```

On the other hand, with `V=nu U+XU'`,

```text
T'=2aX^(nu-1)V,
deg V=p+eta-4.                                          (TRE3)
```

Since `T(0)=3b!=0`, the factor `X^(nu-1)` contributes no common root with
`T`. Consequently every positive-valuation record must satisfy

```text
nu+2eta>=4.                                             (TRE4)
```

Together with `eta<=3-nu`, this excludes

```text
(nu,eta)=(1,0),(1,1),(2,0),(3,0).                      (TRE5)
```

In particular the clean `nu=3` case is empty. The only positive-valuation
strata left are

```text
(nu,eta)=(1,2),(2,1).                                  (TRE6)
```

For `(nu,eta)=(2,1)`, equality is forced throughout:

```text
deg rad(T)=3,
rad(T) is proportional to P,
T/rad(T) is proportional to V.                         (TRE7)
```

For `(nu,eta)=(1,2)`, `2<=deg rad(T)<=3`. The `nu=0`
strata require separate treatment because `b` may vanish and this tangent
root argument can become identically zero. The theorem does not exclude the
two surviving positive strata or any `nu=0` stratum, classify nonembedded
`h=2`, treat `m=8,16`, or close L1.
