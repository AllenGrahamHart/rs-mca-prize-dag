# `A=1` distance-three large Pade class has static denominator

- **status:** PROVED
- **closure:** proof plus exact threshold certificate
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_relation_class_reduction`

Let `H_[A:B]` be a Pade relation class of tail order `t`. If

```text
|H_[A:B]|>4t(t+1)+t,                                (QPSD1)
```

then the primitive relation can be represented in the form

```text
B=B(Z),
A=A_2(Z)U^2+A_1(Z)U+A_0(Z),
deg A_j,deg B<=t.                                   (QPSD2)
```

Consequently its class polynomial `P_H` divides all three static residuals

```text
F_2=I A_2+M_0B,
F_1=I A_1-2M_1B,
F_0=I A_0+M_2B.                                    (QPSD3)
```

The official relation-class lower bounds are far above `(QPSD1)`:

```text
t=6:  172410>174,
t=8:    2128>296.                                  (QPSD4)
```

Therefore every official degree-two survivor supplies polynomials
`A_0,A_1,A_2,B`, with `B` nonzero, of degree at most six or eight for which

```text
deg gcd(P_Z,F_0,F_1,F_2)>=172410       (antipodal),
deg gcd(P_Z,F_0,F_1,F_2)>=  2128       (constant product). (QPSD5)
```

Proving the strict complementary external-factor gcd bounds closes the
degree-two support branch. The remaining object is a four-input simultaneous
univariate Pade problem modulo the split external locator `P_Z`; no
orbit-coordinate or circuit enumeration remains.
