# All-admissible-row O1 mass bound - refuted

The refuted proposition is that at every official admissible `n=2^41` row,
the full-group F2 window satisfies

```text
E_(c in K1)[T_W(c)] <= 2^(m+o(n)).                              (O1)
```

It fails on the admissible row

```text
p=3*2^41+1=6,597,069,766,657,  q=p^6,
ord_n(p)=1<6=[F_q:F_p].
```

The governing nested-window lower bound exceeds `(O1)` by `2^(5n/12)`.
