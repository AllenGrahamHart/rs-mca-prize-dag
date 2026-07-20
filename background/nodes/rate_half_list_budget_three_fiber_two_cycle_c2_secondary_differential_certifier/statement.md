# Budget-three fiber-two c=2 secondary differential certifier

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_two_window_square_reduction`

Retain the generic primary-gap notation

```text
E=sum_(j=0)^4 E_jz^j,       E_0=1,
A=E^(-1/4)=sum_(n>=0)a_nz^n,
B=sum_(n=0)^(2H-3)a_nz^n,
a_(2H-2)=a_(2H-1)=0,       c=a_(2H)!=0,             (SDC1)
b=a_(2H-3),       kappa=E_4b/c.
```

The linear differential residual from the two-window theorem is exactly

```text
E'B+4EB'
 =-8Hc z^(2H-1)+8(H-1)E_4b z^(2H).                 (SDC2)
```

Assume the characteristic is zero or greater than `8H-8`, as on the official
row. Then the secondary two-window condition is equivalent to the existence
of a polynomial `C` satisfying

```text
C(0)=1,       deg C<=H-3,                            (SDC3)
```

and the single differential divisibility

```text
z^H divides
  zE'C^2+4HEC^2+4zECC'
    -(4H-4(H-1)kappa z)B.                           (SDC4)
```

Every polynomial in `(SDC4)` has degree at most `2H-2`, so the quotient has
degree at most `H-2`. This criterion eliminates the entire high window
`a_(2H),...,a_(3H-1)` except for its first scalar `c`; it is equivalent to,
not merely necessary for,

```text
LT=cC^2 mod z^H.                                    (SDC5)
```

The theorem does not force parity, impose root torsion, or solve the official
divisibility. In particular, the proved gap-only counterexample passes this
certifier. Its value is an exact lower-degree interface in which official
torsion can now be used essentially.
