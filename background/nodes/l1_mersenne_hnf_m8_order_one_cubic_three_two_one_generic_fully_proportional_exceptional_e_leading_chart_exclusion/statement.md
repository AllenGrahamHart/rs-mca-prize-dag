# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E leading-chart exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the fixed `a_2=0` chart (FEQ8) of the fully proportional
  official `h=7` cubic `3+2+1` residue

Let

```text
P_off={8191,131071,524287,2147483647}.               (FEL1)
```

On (FEQ8), put `z=b^2`. Then

```text
z=1575/247,
q=-10(z+27)/231.                                    (FEL2)
```

The exceptional equation is affine in `b` after `b^2=z`:

```text
E_G=C_b b+C_0,
C_b=-720q^2-1902q-40(z+27),
C_0=240zq+240z-630q.                                (FEL3)
```

Substitution of (FEL2) gives

```text
C_b=-8244*3950060/(61009*5929),
C_0=3233714400/(61009*231).                          (FEL4)
```

Every denominator in (FEL2)--(FEL4) is a unit in every characteristic in
`P_off`, and `C_b` is also a unit there. Hence `E_G=0` forces

```text
b=115275930/45228187.                                (FEL5)
```

Combining (FEL5) with `b^2=1575/247` would force

```text
W:=247*115275930^2-1575*45228187^2
  =60466872820654125=0.                              (FEL6)
```

But the official residues are

```text
W mod 8191       =       6740,
W mod 131071     =     100974,
W mod 524287     =     284891,
W mod 2147483647 = 1825899718.                       (FEL7)
```

All four are nonzero. Therefore the fixed exceptional leading chart (FEQ8)
is empty in every official characteristic. This closes only `a_2=0` inside
the exceptional `E_G=0` coefficient chart; it makes no claim about the
generic exceptional endpoint, `S_1=S_0=0`, `J_*=0`, the ordinary
coefficient chart, or any other `h=7` residue.
