# Budget-three antipodal generic secondary-gap reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_fourth_root_gap_reduction`

Retain the reversed centered norm identity

```text
E(B^4+e_2z^(2h)B^2C^2+e_3z^(3h)BC^3+e_4z^(4h)C^4)
 =1-z^d,                                                (SGR1)
```

where `B=z^rU(z^-1)`, `C=z^vV(z^-1)`, and `B(0)=1`,
`C(0)!=0`. On the maximal official generic boundary,

```text
e_2!=0,       s=2^37,       r=s-1,
v=s/2-2,      h=s/2+1,      v=h-3.                     (SGR2)
```

The dependency makes `B` the canonical truncation of `E^(-1/4)`. Define the
formal series

```text
R=E^(-1)(1-z^d)-B^4,
J=z^(-2h)R/B^2,       j_0=J(0),
P=(J/j_0)^(1/2),      P(0)=1.                          (SGR3)
```

Then `j_0=e_2C(0)^2!=0`, and

```text
P=C/C(0) mod z^h.                                      (SGR4)
```

Consequently the lower-degree direction is determined up to scale by `E`
and the canonical `B`, and it must satisfy the secondary gap

```text
[z^(h-2)]P=[z^(h-1)]P=0,                              (SGR5)
```

at the official indices `h-2=2^36-1` and `h-1=2^36`.

Thus a generic floor-boundary solution must satisfy both the primary
fourth-root gap at indices `2^37,2^37+1` and the secondary square-root gap in
`(SGR5)`. These necessary gaps do not prove nonexistence, determine the outer
coefficients `e_3,e_4`, or address generic solutions above the floor.
