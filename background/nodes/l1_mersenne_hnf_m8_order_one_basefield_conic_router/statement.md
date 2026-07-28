# L1 Mersenne HNF m=8 order-one base-field conic router

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_conic_reduction`,
  `l1_mersenne_next_to_maximal_belyi_shifted_value_gate`
- **consumer:** `l1_mixed_petal_amplification`

Use the conic coordinates and put

```text
theta=rho(c-1)=2A_HNF/c.                             (BCR1)
```

The two conic points with `z=-1` are not order-one survivors.

On the remaining affine chart, suppose its line parameter `t` lies in the
prime field. Then every survivor satisfies

```text
z=3,             zeta=-1,
c^2-3c+1=0,      c^p=c^(-1)=3-c,
7w^2=5308,       theta=(w-38)/5,
rho^p=-c*rho.                                          (BCR2)
```

This branch is empty on the rows with

```text
p=8191, 131071.                                       (BCR3)
```

On each of the rows with

```text
p=524287, 2147483647,                                 (BCR4)
```

it is reduced to at most the two signs of `w` in (BCR2). Equivalently,
`t=(w-6)/4`. A sign is only an outer candidate and must still pass the full
trace, cyclotomic, and inner equations.

The branch `t notin F_p` remains open. This theorem does not assert that the
two displayed larger-row packets exist or survive any later gate.
