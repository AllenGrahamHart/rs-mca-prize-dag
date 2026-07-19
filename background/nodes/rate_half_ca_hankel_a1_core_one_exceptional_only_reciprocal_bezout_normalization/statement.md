# `A=1` core-one exceptional-only reciprocal Bezout normalization

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_resultant_descent`

Retain `(RRD1)--(RRD5)` and define the next corrected-complement
coefficient

```text
a_minus=[X^(D_0-r-1)]A_1.                           (RBN1)
```

Then the first reciprocal coefficient satisfies the exact Bezout identity

```text
P_cl Delta_inf+E q_bar a_minus=1.                   (RBN2)
```

Consequently

```text
gcd(P_cl,E q_bar)=1,       gcd(Delta_inf,E q_bar)=1, (RBN3)

Delta_inf(tau)=P_cl(tau)^(-1)
                  for every root tau of E q_bar.    (RBN4)
```

Thus `Delta_inf` is not a free coefficient in the reciprocal classifier: it
is a specified inverse of the clean-slope locator modulo the complete
leading form `[X^r]Q=E q_bar`, with `a_minus` as the printed Bezout
coefficient. This normalization is necessary, but it does not determine the
lower reciprocal coefficients or exclude the corrected square.
