# C36' rich-fiber norm cutoff

- **status:** PROVED
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_shifted_product_sidon`

Let `n=2^s` with `s>=2`, let `p=1 mod n` be prime, let `H` be the
order-`n` subgroup of `F_p^*`, and put `A=(1-H)\{0}`. For

```text
P(t)=#{(a,b) in A^2:ab=t},
```

one has

```text
P(t)>=19  =>  p<=6^(n/4).                       (RFNC)
```

Consequently, if `p>6^(n/4)`, the C36' rich locus is empty and

```text
X_18=0.
```

Thus the open range of `f3_h3_mobius_excess_half` is reduced from all
`p>=n^2` to

```text
n^2<=p<=6^(n/4).
```
