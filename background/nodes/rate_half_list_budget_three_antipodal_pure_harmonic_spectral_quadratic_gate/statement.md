# Budget-three antipodal pure harmonic spectral quadratic gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_pure_euler_spectral_reconstruction`,
  `rate_half_list_budget_three_antipodal_pure_harmonic_binary_quartic_norm_gate`

Retain an official pure spectral candidate `Phi` and form

```text
S_Phi=1+sum_m phi_m/(d-m) Y^m,
D_Phi=monic gcd(S_Phi,Y^d-1).                            (HSQ1)
```

Assume the exact spectral tests hold: `deg D_Phi=4`, the two quotients are
the required fourth powers, `X^4+e_4` splits, and the four roots of `D_Phi`
are distinct and have square-root lifts in the official field.

For each of the three unordered quadratic splittings write

```text
D_Phi=(Y^2-SY+q)(Y^2-TY+u).                             (HSQ2)
```

Define

```text
A=4q+4u-ST,
C_0=A^2+4T^2q-4uS^2-16uq,
C_1=-4AT+16uS,
P(D_1,D_2)=C_0^2-qC_1^2.                               (HSQ3)
```

Then the deleted support has a harmonic square-root lift if and only if

```text
P(D_1,D_2)=0                                            (HSQ4)
```

for at least one of the three splittings. Consequently `(HSQ1)--(HSQ4)`,
the two fourth-power quotient tests, and base-field splitting form one exact
acceptance gate for a harmonic-matched pure norm packet.

The test uses only the coefficients of two quadratic factors of the spectral
gcd. It does not choose square roots, enumerate eight sign classes, expand a
degree-24 symmetric polynomial, classify the five passports, or assert that
the official gate is empty.
