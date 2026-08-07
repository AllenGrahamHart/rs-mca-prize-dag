# WCL `(1,6)` parity-adapted Heron descent

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_ell1_weight6_pair_heron_norm_router`
- **consumer:** `dli_wcl_slot_1_6_emptiness`

Write the six squared roots as `y_i=zeta_256^(x_i)` and choose
`r_i=zeta_512^(x_i)`. The product sector is the parity of `sum_i x_i`.

## Even-product sector

If `sum_i x_i` is even, pair odd exponents among themselves and even
exponents among themselves. Every pair product

```text
t_j=r_a r_b=zeta_512^(x_a+x_b)
```

then lies in `K_0=Q(zeta_256)`. Consequently all eight Heron factors of the
pair router already lie in `K_0`; no auxiliary quadratic extension remains.

## Odd-product sector

If `sum_i x_i` is odd, pair all but one odd exponent and all but one even
exponent within parity, then pair the two leftovers. Exactly one pair product
`t` lies in `K=Q(zeta_512)\K_0`; the other two lie in `K_0`. For fixed signs
on the two same-parity pairs, write their squared sums as `V,W`, and for the
mixed pair put

```text
s=y_a+y_b,       d=y_a y_b,       t^2=d,
C=s^2+4d-2s(V+W)+(V-W)^2,
D=4(s-V-W).                                             (PAD1)
```

Then the two mixed-pair Heron conjugates have product

```text
H(s+2t,V,W) H(s-2t,V,W)=C^2-dD^2.                     (PAD2)
```

Thus the odd-sector sign product is the product of four explicit quadratic
norms `(PAD2)` in `K_0`, while the even-sector product is eight explicit
Heron factors in `K_0`.

The parity pairing can be made deterministic on a canonical exponent
representative by pairing consecutive exponents within each parity class and,
in the odd sector, pairing the two final leftovers. This is a field-descent
theorem only; no resulting `K_0` factor is excluded at the official gate.
