# Budget-three antipodal generic two-window square reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction`

Retain the maximal generic floor and write its parameters as

```text
d=8h-8,       r=2h-3,
A=E^(-1/4)=sum_(m>=0)a_mz^m,
B=sum_(m=0)^r a_mz^m.                                 (TWS1)
```

Assume the primary gap

```text
a_(2h-2)=a_(2h-1)=0,       c:=a_(2h)!=0.              (TWS2)
```

Define the two length-`h` coefficient windows

```text
L=sum_(m=0)^(h-1)a_mz^m,
T=sum_(m=0)^(h-1)a_(2h+m)z^m.                         (TWS3)
```

For the normalized secondary series `P` of the dependency,

```text
P^2 = L T/c mod z^h.                                  (TWS4)
```

Consequently the two secondary zero coefficients are equivalent to the
existence of a unique polynomial `C` with

```text
C(0)=1,       deg C<=h-3,       L T=c C^2 mod z^h.    (TWS5)
```

There is also an exact differential form. Put
`A-B=z^(2h)T_hat`. Then

```text
E'B+4EB'
 =-z^(2h-1)((zE'+8hE)T_hat+4zE T_hat'),               (TWS6)
```

and the expression in parentheses is a polynomial of degree at most one.
Thus the simultaneous primary and secondary gate is a two-window square
problem with linear differential forcing; it contains no free coefficients
of either official-degree pencil direction.

This theorem does not exclude `(TWS5)`, prove the canonical span identity, or
address the intermediate and above-floor strata.
