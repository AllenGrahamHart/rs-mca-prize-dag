# Budget-three antipodal generic Euler coupled-norm gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_euler_cubic_norm_gate`

Retain the canonical generic floor and put

```text
Q_0=(Y^d-1)/D,
N_T=Res(V,T),       N_Q=Res(V,Q_0),       N_U=Res(V,U), (GNC1)
```

using the monic-first resultant convention of `(GCN1)`. Then all three
scalars are nonzero and

```text
N_Q=N_U^4,
N_T N_U^3=(-d)^v.                                    (GNC2)
```

Consequently every generic floor candidate satisfies both scalar gates

```text
N_Q in (F^*)^4,
N_T^4 N_Q^3=d^(4v).                                  (GNC3)
```

The second identity contains no `N_U`; it couples two resultants computable
directly from the canonical `D,U,V,T`. Over a finite base field of order `q`,
put `g_4=gcd(4,q-1)`. The fourth-power condition is equivalently

```text
N_Q^((q-1)/g_4)=1.                                   (GNC4)
```

This gate complements the cubic character of `N_T`. Passing both character
tests is not sufficient: the exact coupling in `(GNC3)` and then the full
Euler remainder must still hold. This theorem does not prove uniform scalar
rejection or exclude the generic floor.
