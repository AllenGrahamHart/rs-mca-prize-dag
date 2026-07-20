# Budget-three antipodal pure Euler spectral reconstruction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_pure_ramification_passport`

Let `d=4r+4`, `N=d-4`, and let the characteristic be zero or greater than
`d`. For a degree-`N` polynomial

```text
Phi=sum_(m=0)^N phi_m Y^m
```

define its low-degree Euler spectral lift

```text
S_Phi=1+sum_(m=0)^N (phi_m/(d-m))Y^m,       H=Y^d-1. (ESR1)
```

Every denominator in `(ESR1)` is nonzero. Put

```text
D_Phi=monic gcd(S_Phi,H).                              (ESR2)
```

Then `Phi` comes from a normalized pure-quartic norm packet

```text
H=D(U^4+e_4V^4),
deg D=4,       U monic of degree r,
V monic of degree r-1,       e_4!=0,
gcd(U,V)=1,
Phi=dDU^4-Y(DU^4)'                                      (ESR3)
```

if and only if the following deterministic tests hold:

```text
deg D_Phi=4,
(H+S_Phi)/D_Phi=U^4                    with U monic,
-S_Phi/D_Phi=e_4V^4                    with V monic.    (ESR4)
```

The quotients in `(ESR4)` are exact, and their degrees are `4r` and
`4r-4`. The data `D_Phi,U,V,e_4` are unique under the printed monic
normalization. The full centered base-field pencil additionally requires

```text
X^4+e_4 splits into four distinct linear factors over F. (ESR5)
```

When `(ESR5)` holds, its roots give the four pairwise-coprime factors
`U+c_iV`. Upgrading this norm packet to the original pure antipodal packet
still requires the harmonic matching between these `c_i` and square-root
lifts of the four roots of `D_Phi`.

The reconstruction is compatible with the Euler router. Defining `T,C` from
`D_Phi,U,V` as in `(PER2)` gives

```text
Phi=TU^3,       Phi+d=e_4V^3C.                         (ESR6)
```

Thus each of the five ramification passports now has one exact intrinsic
acceptance gate: one Euler spectral lift, one gcd with `Y^d-1`, and two
fourth-power tests. This is a structural equivalence, not authorization to
materialize degree-`d` coefficient arrays at official scale.
