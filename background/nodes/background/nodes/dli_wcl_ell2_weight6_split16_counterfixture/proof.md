# Proof - DLI ell-two weight-six split-16 counterfixture

The verifier first checks the Pocklington certificate

```text
3^(q-1)=1 mod q,
gcd(3^((q-1)/2)-1,q)=1,
q-1=2^16>sqrt(q),
```

so `q=65537` is prime and `3` has order `2^16`. Therefore `omega=3^64` has
exact order `2^10=1024`.

The six exponents are distinct. No pair differs by `512` modulo `1024`, so
the root set contains no antipodal pair. Their differences generate the full
cyclic group, so the configuration does not descend to a proper root-of-unity
subgroup.

Direct modular exponentiation verifies both equations in (S16). This is
exactly the simultaneous first- and third-moment condition in the
weight-six triple-cubic router. The compact certificate also records its
router discovery coordinates

```text
(x,y,d)=(zeta^116,zeta^377,zeta^334),
odd dilation=849.
```

Replaying the cubic router recovers the displayed six-set and all distinct,
disjoint, and antipodal guards. Finally, `q-1=2^16` gives the printed
valuation, which is insufficient for the official `2^41` ambient split.
