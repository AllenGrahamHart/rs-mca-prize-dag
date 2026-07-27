# L1 Mersenne HNF order-zero linear-color exclusion

- **status:** PROVED
- **closure:** proof
- **dependency:** `l1_mersenne_next_to_maximal_hypergeometric_normal_form`
- **consumer:** `l1_mixed_petal_amplification`

Consider either official next-to-maximal order-zero row

```text
n=m(p+1),       (m,h) in {(8,7),(16,15)},
P_s(W)=sum_(r=0)^h binom(s+r-1,r)W^(h-r),
P_s | W^n-1,    s notin F_p.                         (LCE1)
```

For the roots `a` of `P_s`, let `E_s` be the unique polynomial of degree
less than `h` satisfying

```text
E_s(a)=a^(p+1).                                      (LCE2)
```

Then

```text
deg E_s >= 2.                                       (LCE3)
```

Thus the colored Frobenius classification of the order-zero endpoint has
neither a constant- nor a linear-color stratum on any of the four
`m=8,h=7` rows or the one `m=16,h=15` row. Its first possible color degree
is two.

This theorem does not exclude degree at least two, close the order-zero
chamber, treat the order-one chamber, prove cyclotomic divisibility from the
bounded equations, or supply an inner lift.
