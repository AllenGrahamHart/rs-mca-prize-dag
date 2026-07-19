# Budget-three antipodal intermediate low-band exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_residual_square_gcd_gate`

Retain the maximal official row

```text
r=2^37-1,       d=4r+4=2^39,
e_2=0,          e_3!=0,       v=deg V.               (ILB1)
```

Put `h=r-v` and let `T` be the nonzero differential residual. Its exact
degree is

```text
t=deg T=r+4-3h=3v-2r+4.                              (ILB2)
```

Retain

```text
P=TU^3+d,                  W=T'U+3TU',
A=4YDT'+3T(dD-YD'),       J=dA^3+27T^7.              (ILB3)
```

The dependency proves

```text
V | gcd(P,W) | J.                                    (ILB4)
```

At the floor `v=(2^38-4)/3`, one has `t=2` and `deg J=18`, so that case is
empty. Above the floor, `t>=5` and

```text
deg A=t+4,       deg J=7t.                           (ILB5)
```

Consequently every surviving higher intermediate degree must satisfy

```text
v<=7t=7(3v-2r+4),
10v>=7r-14,
v>=ceil((7r-14)/10)=96,207,267,429.                  (ILB6)
```

Therefore the complete interval

```text
91,625,968,980 <= v <= 96,207,267,428                (ILB7)
```

is empty. This removes `4,581,298,449` consecutive intermediate degrees,
including the maximal floor boundary. It does not exclude intermediate
degrees at or above `96,207,267,429`, or any generic, pure, non-antipodal, or
other fiber-four branch.
