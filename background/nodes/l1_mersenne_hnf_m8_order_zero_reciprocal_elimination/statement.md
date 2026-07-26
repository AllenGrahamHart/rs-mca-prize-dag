# L1 Mersenne HNF m=8 order-zero reciprocal elimination

- **status:** PROVED
- **closure:** proof
- **dependencies:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`,
  `l1_mersenne_hnf_frobenius_reciprocal_gate`
- **consumer:** `l1_mixed_petal_amplification`

On each of the four official rows

```text
(n,p,m,h) in {
  (65536,       8191,       8,7),
  (1048576,     131071,     8,7),
  (4194304,     524287,     8,7),
  (17179869184, 2147483647, 8,7)
},
```

there is no `s notin F_p` for which

```text
P_s(W)=sum_(r=0)^7 binom(s+r-1,r)W^(7-r)
```

divides `W^n-1`. Equivalently, the complete `m=8,h=7`, `ord_0(T)=0`
outer HNF chamber is empty on all four official rows.

The proof uses only the first three coefficient equations of the bounded
Frobenius reciprocal gate. It therefore covers every colored-interpolant
degree at once; cubic and higher degrees need not be classified separately
on `m=8`.

This theorem does not treat the `m=16,h=15` order-zero chamber, the order-one
HNF chamber, other checkpoint widths, or the aggregate L1 exact shell. It
does not close a critical node or adjacent prize row.
