# Proof

Put

```text
r_i = s_i omega^e_i,
p_j = sum_i r_i^j,
```

and write `a_j` for the `j`th elementary symmetric function of the four
`r_i`. Since `s_i^3=s_i`, the two `ell=2` odd-power equations say
`p_1=p_3=0`. Newton's identities give

```text
a_1 = p_1 = 0,
p_3 - a_1 p_2 + a_2 p_1 - 3a_3 = 0.
```

The official production prime satisfies `q=1 mod 2^41`, so its
characteristic is neither 2 nor 3. Hence `a_3=0`. The monic polynomial of the
four roots is therefore

```text
prod_i (T-r_i)
  = T^4 - a_1 T^3 + a_2 T^2 - a_3 T + a_4
  = T^4 + a_2 T^2 + a_4.
```

This polynomial is even. Thus `-r_i` is a root whenever `r_i` is. The roots
are nonzero and distinct, so they split into two antipodal pairs.

To compare this conclusion with reduced signed supports, encode `s_i=-1` by
the full exponent `e_i+512` and `s_i=+1` by `e_i`. Since
`-1=omega^512`, an antipodal pair has full exponents differing by 512 modulo
1024. Their reductions modulo 512 are then equal, contradicting the required
distinctness of the `e_i`. Therefore the two odd-power equations have no
reduced signed weight-4 solution.
