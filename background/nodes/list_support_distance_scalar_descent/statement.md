# Support-distance scalar descent for Reed-Solomon lists

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **upstream source:** `przchojecki/rs-mca@57e39fba`,
  `experimental/notes/thresholds/m31_scalar_descent_equivalence.md`

Let `F=F_q`, let `E/F` be a finite extension of degree `r>=1`, and let the
evaluation domain `D` be contained in `F`, with `|D|=n`. For

```text
C_K=RS_K(D,k),                 K in {F,E},
B_K(a)=max_y #{c in C_K: agr(c,y)>=a},
t=n-a,                         g=a-k+1,
N_r=(q^r-1)/(q-1),             H_r=(q^(r-1)-1)/(q-1),
```

fix an integer `L>=1`. If

```text
L t H_r < g N_r,                                      (SD1)
```

then

```text
B_E(a)>=L  if and only if  B_F(a)>=L.                 (SD2)
```

Equivalently, under `(SD1)`, the extension-field upper predicate
`B_E(a)<=L-1` is exactly the base-field upper predicate `B_F(a)<=L-1`.
The easy-to-check stronger hypothesis

```text
L t < q g                                             (SD3)
```

implies `(SD1)`.

At the upstream deployed Mersenne-31 list row

```text
q=2^31-1, r=4, n=2^21, k=2^20, a=1116023, L=2^24,
```

condition `(SD1)` holds with exact margin

```text
592061458020761914489814638395392.                    (SD4)
```

Since `floor(q^4/2^100)=2^24-1`, this proves equivalence of the open
quartic- and prime-field upper predicates at that upstream row. It does not
prove either predicate. The specialization uses target `2^-100`, not the
`2^-128` target of the local grand-prize statement.
