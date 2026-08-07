# L1 FPC5 rate-half `M=4,t=3` split-slice payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

At rate `1/2`, after the projective Johnson-positive cells are paid, the
three-touched-petal tail has

```text
N=4ell+b-2,       d=2ell-a,
b>=7,              1<=a<=floor((b-3)/4),
J=ell(4a-b+2)+a^2+2ab-4a<=0.
```

For one first-owned source, touched triple, defect, and normalized source
cross-ratio `lambda`, the fixed cell is exactly

```text
{D monic : D|L_C, deg D=2ell-a,
            deg rem_(L_2L_3)(D Etilde)<=ell-a,
            gcd(D,rem_(L_2L_3)(D Etilde))=1}.       (LS6)
```

The target is a disjoint polynomial/profile allocation after summing these
exact atoms over every first-owned source, triple, defect, and `lambda`.
Bounding the dimension of the ambient linear slice is not the conclusion.
