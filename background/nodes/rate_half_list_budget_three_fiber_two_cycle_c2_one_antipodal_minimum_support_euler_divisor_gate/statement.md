# Budget-three fiber-two c=2 one-antipodal minimum-support Euler divisor gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_secondary_differential_certifier`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler`

Retain a complete canonical one-antipodal candidate and put

```text
N=8H-8,       r=2H-3,
V=z^H C,
T=NEB-z(E'B+4EB'),
P=TB^3-N.                                             (EDG1)
```

Write `c_0=a_(2H)`, `b_0=a_(2H-3)`, and let `E_4` be the leading
coefficient of `E`.  The proved two-term differential residual gives

```text
T=8T_0,
T_0=(H-1)EB+Hc_0z^(2H)-(H-1)E_4b_0z^(2H+1),
P=8P_0^raw,
P_0^raw=T_0B^3-(H-1).                                (EDG1')
```

Then every complete canonical packet satisfies

```text
V divides P,       gcd(V,TB)=1.                       (EDG2)
```

The primary double gap gives the stronger automatic valuation

```text
z^(2H) divides P.                                     (EDG3)
```

Consequently

```text
P_0=z^(-2H)P_0^raw is a polynomial,
C divides P_0,       gcd(C,T_0B)=1.                   (EDG4)
```

This is a deterministic outer-coefficient-free remainder gate on the
canonical outputs `E,B,C`.

If the barycentric mismatch has minimum support `3H+1`, then the full degree
of the support compiler forces

```text
deg C=H-3=2^37-2.                                    (EDG5)
```

Let `c_m` be the leading coefficient of `C` and put
`C_sharp=c_m^(-1)C`, the monic polynomial with the same roots.  Then
`(EDG4)` gives

```text
Res(C_sharp,T_0) Res(C_sharp,B)^3=(H-1)^(H-3).       (EDG6)
```

All factors are nonzero.  Since `3` divides `H-3`, every minimum-support
candidate therefore satisfies the scalar gate

```text
Res(C_sharp,T_0) is a nonzero cube in the base field. (EDG7)
```

The theorem applies before choosing the one-pair `L/Q` completion branch and
contains no outer coefficient or selected-pair variable.  It does not prove
the remainder nonzero, make its official-degree evaluation cheap, or address
larger barycentric support.
