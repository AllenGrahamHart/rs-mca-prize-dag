# Budget-three antipodal pure Euler ramification router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`,
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`

Retain the centered pure-quartic boundary

```text
d=4r+4,
D(U^4+e_4V^4)=Y^d-1,
deg D=4,       deg U=r,       deg V=r-1,       e_4!=0, (PER1)
```

where `D,U` are monic, `U,V` are squarefree and coprime, and the
characteristic is zero or exceeds `d`. Define

```text
T=dDU-Y(D'U+4DU'),
C=4YD V'+V(YD'-dD).                                  (PER2)
```

Then

```text
deg T=r,       deg C=r+3,
T U^3+d=e_4 V^3 C,
gcd(TU,VC)=1.                                         (PER3)
```

Conversely, with the degree and monicity conditions in `(PER1)`, the cubic
identity in `(PER3)` implies the pure norm equation in `(PER1)`.

Put

```text
W=T'U+3TU',       Z=3V'C+VC'.                         (PER4)
```

There is one nonzero linear polynomial `L` such that

```text
W=V^2L,       e_4Z=U^2L,
(TU^3)'=U^2V^2L.                                     (PER5)
```

Thus the degree-`4r=d-4` polynomial

```text
Phi=TU^3
```

has at most three finite critical values:

```text
0,       -d,       Phi(ell),                          (PER6)
```

where `ell` is the root of `L`. Roots of `U` map to zero and roots of
`V` map to `-d`. Every repeated root of `T` or `C`, and every root
common to `T,U` or to `C,V`, is `ell`; no such defect can occur at a
second point.

This replaces the second-derivative Wronskian by an exact low-critical-value
polynomial router. It does not classify the resulting ramification data,
exclude the harmonic matched Fermat decomposition, or close budget three.
