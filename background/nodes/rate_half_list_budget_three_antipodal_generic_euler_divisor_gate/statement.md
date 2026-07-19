# Budget-three antipodal generic Euler divisor gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_canonical_span_criterion`

Retain the maximal official generic floor and its canonical original-coordinate
directions:

```text
d=2^39,       r=2^37-1,       v=2^36-2,
F=(Y^d-1)/D=product_i(U+c_iV),
e_2!=0,       deg U=r,         deg V=v.               (GED1)
```

The primary and secondary gap theorems determine the monic `U,V` from the
four deleted roots. Let

```text
T=dDU-Y(D'U+4DU'),       deg T=1,
P=TU^3+d.                                             (GED2)
```

Writing

```text
K=e_2U^2+e_3UV+e_4V^2,
S=DV^2K,                                              (GED3)
```

every valid generic floor solution satisfies

```text
P=YS'-dS,
V | P,
gcd(V,TU)=1.                                         (GED4)
```

Equivalently, the canonical data must pass the exact modular-remainder gate

```text
(TU^3+d) mod V=0.                                    (GED5)
```

This condition contains no outer coefficient `e_2,e_3,e_4`, no unknown
polynomial direction, and no split/Mobius parameter. Its exact ambient
degrees are

```text
deg P=3r+1=6*2^36-2,
deg(P/V)=5*2^36.                                     (GED6)
```

A nonzero remainder rejects the complete canonical generic candidate before
the full span and split/Mobius tests. This theorem does not prove that the
remainder is uniformly nonzero over the official deleted-root family or
exclude generic solutions above the floor.
