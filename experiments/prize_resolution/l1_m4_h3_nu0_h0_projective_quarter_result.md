# Nu=0, b!=0, h=0 projective quarter certificate

- **status:** complete exact projected certificate
- **script:** `l1_m4_h3_nu0_h0_projective_quarter_check.py`
- **scope:** the surviving constant-eliminant endpoint on all four official
  `m=4,h=3` characteristics
- **resources:** bounded symbolic resultants and degree-at-most-four quotient
  arithmetic; no field-scale enumeration

For each quarter pair `(epsilon,eta)`, the script intersects the projective
fiber-product equation with its Frobenius transform, computes the exact
univariate resultant, and proves the complete gcd with
`U^(p+1)-epsilon`. It then resolves every surviving constant or quadratic
packet and checks the `v` power, nondegeneracy, and normalized outer
parameters.

```text
p=8191:        (A,B)=(6,20)
p=131071:      (A,B)=(6,20)
p=524287:      (A,B)=(6,20)
p=2147483647:  (A,B)=(6,20) or
                (844833809,2002167159)
```

Here `A=a/R(0)^2` and `B=b/R(0)^3`. The universal packet has shifted
fiber-product polynomial

```text
X^3+3X^2+9X+27=(X+3)(X^2+9).
```

The certificate is a necessary projective classification. It does not prove
that either packet lifts to a degree-`p` inner polynomial or split pencil.
