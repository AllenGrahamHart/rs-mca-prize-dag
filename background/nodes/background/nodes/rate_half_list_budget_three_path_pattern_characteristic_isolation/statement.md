# Budget-three path-pattern characteristic isolation

- **status:** PROVED
- **closure:** exact cyclotomic determinant
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_path_power_two_witness`

Write an order-sixteen domain as

```text
D_16={zeta^e:0<=e<16},       zeta primitive.             (PCI1)
```

Under the discrete logarithm `3^e mod 17`, the four agreement supports of the
known `F_17` path witness become

```text
S_0={2,3,4,5,6,7,10,11,12,13,15},
S_1={0,1,3,4,6,7,8,10,11,14,15},
S_2={0,1,2,3,5,7,8,12,13,14,15},
S_3={0,1,4,5,6,9,10,11,12,13,14}.                      (PCI2)
```

Form the `28 x 24` four-codeword intersection matrix over
`Z[zeta_16]` from these four fixed exponent supports. Order its rows by
increasing exponent, and within one exponent equate the least indexed present
word to every other present word, using word zero as base whenever it is
present. The rows with zero-based indices

```text
0,2,5,7,11,13,15,16,9,4,1,14,
6,3,18,20,10,17,8,19,12,21,22,23                      (PCI3)
```

give a `24 x 24` minor with determinant

```text
alpha=2^21(6 zeta^5-7 zeta^4+14 zeta^3-7 zeta^2+6 zeta),
|Norm_{Q(zeta_16)/Q}(alpha)|=2^170 17^4.               (PCI4)
```

Consequently this fixed exponent-support pattern has full intersection-matrix
column rank over every odd-characteristic field except possibly
characteristic `17`. The printed `F_17` realization has rank `23`, so it is a
genuine characteristic-`17` accident rather than a characteristic-free
order-sixteen identity.

Characteristic `17` cannot occur on the prize-max order-`2^41` domain under
the official `q<2^256` cap. Indeed

```text
2^41 | 17^e-1  =>  2^37 | e,
```

by the two-adic lifting-the-exponent formula, whereas `17^(2^37)>2^256`.
Thus the known path pattern cannot be transported to the prize-max budget-three
row by preserving its exponent supports. This theorem does not exclude a
different path assignment, a different incidence chamber, or a witness that
does not descend from `(PCI2)`.
