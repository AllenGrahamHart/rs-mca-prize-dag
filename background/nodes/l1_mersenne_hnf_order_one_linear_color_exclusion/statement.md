# L1 Mersenne HNF order-one linear-color exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` rows and the official
  `(m,h)=(16,15)` row

Remove the automatic order-one root and write

```text
L_(rho,c)(W)=P_(rho,c)(W)/(W+1/(c-1)),
H=deg L=h-1=m-2.                                    (OLC1)
```

For the roots `x` of `L`, let `E` be the unique degree-less-than-`H`
interpolant satisfying

```text
E(x)=x^(p+1).                                        (OLC2)
```

Then `E` cannot have degree one. Equivalently, every order-one survivor has

```text
deg E=0       or       deg E>=2.                     (OLC3)
```

Together with `l1_mersenne_hnf_m8_order_one_constant_color_exclusion`, this
shows that every live `m=8,h=7` order-one packet has `deg E>=2`.

The theorem does not exclude a constant color at `m=16,h=15`, any degree at
least two, the cyclotomic converse, an inner lift, or the remaining L1
chambers.
