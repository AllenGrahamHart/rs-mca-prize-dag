# Proof

The pole-absorption theorem makes `s_FG/H` regular. Multiplying by two more
copies of the contact section preserves regularity. The resulting line
bundle has first coordinate

```text
3(-rho-1)+(N-s)=rho-s-3=d-3,                           (1)
```

and second coordinate

```text
3(e+1)-T=ell-e+3-beta.                                 (2)
```

The product is nonzero. The contact section is nonzero on at least one
component, and the rational function `G/H` is nonzero at that component's
generic point because every component is mixed.

Suppose `ell-e+3-beta<0`. The restriction sequence for the bidegree-`(d,e)`
curve is

```text
0 -> O(-3,ell-2e+3-beta)
  -> O(d-3,ell-e+3-beta)
  -> O_C(d-3,ell-e+3-beta) -> 0.                       (3)
```

The middle surface bundle has no sections because its second coordinate is
negative. Both coordinates of the left bundle are negative, so Kunneth
gives zero `H^1`. Thus the curve bundle in `(3)` has no sections,
contradicting the nonzero product. This proves `(DTC2)`.

For `s=0`, `beta=0` and the slope ledger gives

```text
ell<=4e-rho-2.                                         (4)
```

Compatibility with `ell>=e-3` requires `3e>=rho-1`. For `s=1`, `beta=1`
and

```text
ell<=4e-rho-1,
ell>=e-2,                                              (5)
```

which gives the same necessary inequality `3e>=rho-1`. Hence both branches
are empty below `(DTC4)`.

For the official `rho`, one has `3e_0=rho+1`. Substitution into `(4),(5)`
gives the three slacks printed for each core. Finally
`T=4e+beta-ell` maps both slack triples to
`{rho+4,rho+3,rho+2}`, proving `(DTC5)`. QED.
