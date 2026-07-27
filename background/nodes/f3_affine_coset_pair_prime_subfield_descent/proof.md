# Proof

Suppose `x in F_q` and `L_1(x) in K`. Since `K<=F_p^*` and both
coefficients of `L_1` lie in `F_p`,

```text
x=a_1^(-1)(L_1(x)-b_1) in F_p.                    (1)
```

This proves that the left side of `(PSD1)` is contained in the right side;
the reverse inclusion is immediate. The count is therefore literally the
prime-field count, not an extension of Mattarei's theorem. Applying the
proved affine coset-pair transport over `F_p` proves `(PSD2)`.

For KoalaBear,

```text
p-1=2^24*127,       n=2^21,       d=(p-1)/n=8*127=1016.
```

Thus `n` divides `p-1`, so the unique order-`n` subgroup lies in `F_p^*`.
Also

```text
d^3=1048772096>8388608=4n,       d>=4.             (2)
```

Since `p=2 mod 3`, cubing is an automorphism of `F_p^*`; in particular
`{x:x^3 in H}=H`. The DSP8 affine forms use subgroup elements and the field
operations `+,-,*,/`, so all of their coefficients remain in `F_p`. Equation
`(1)` now proves the asserted KoalaBear descent for both the cube-preimage and
quotient-line factors.

Finally, for `p_M=2^31-1`,

```text
p_M-1=2(2^30-1),       v_2(p_M-1)=1.               (3)
```

Therefore `2^21` does not divide `p_M-1`, and an order-`2^21` subgroup of
the quartic ambient field cannot lie in its prime subfield. The premise of
`(PSD1)` fails, so no inference from Mattarei is licensed there. QED.
