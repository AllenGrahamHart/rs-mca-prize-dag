# M31 adjacent quotient-rotation product spectrum

- **status:** PROVED
- **dependency:** `rate_half_cyclic_rotated_prefix_floor`
- **consumer:** `rate_half_list_adjacent_crossing`
- **upstream workboard:** Lane M, direct ordinary-list stress row

Let

```text
p=2^31-1,       F=F_(p^4),       n=2^21,
k=2^20,         C=RS[F,D,k],
```

where `D` is any multiplicative coset of size `n`. At the adjacent M31 list
agreement

```text
a_+=1116023=k+67447,          B_*=16777215,           (MQR1)
```

specialize the cyclic quotient-rotation construction with

```text
c=2^16,       N=n/c=32,       d=1,       m=N/2+d=17,
s=1911.                                               (MQR2)
```

Fix the `s` partial roots above one quotient point `b_0`. Normalize the other
31 quotient points as the nonidentity elements of `C_32`. For a 17-subset
`A`, write

```text
product(A)=zeta^r,            r in Z/32Z.
```

The 32 quotient-rotation prefix classes have the exact sizes

| normalized product residue | number of residues | class size |
|---|---:|---:|
| `r` odd | 16 | 8,287,155 |
| `r=2 mod 4` | 8 | 8,286,755 |
| `v_2(r)=2` or `r=16` | 5 | 8,286,751 |
| `v_2(r)=3` or `r=0` | 3 | 8,286,750 |

Their sum is

```text
binom(31,17)=265182525.                               (MQR3)
```

For fixed partial roots, the high locator prefix determines and is determined
by the product class. Therefore the maximum contribution of this exact
quotient-rotation family to one received-word list is

```text
M_QR=8287155.                                        (MQR4)
```

Every member agrees in exactly

```text
k+dc+s=2^20+2^16+1911=1116023                       (MQR5)
```

positions. Hence

```text
B^list_C(1116023)>=8287155.                          (MQR6)
```

This sharpens the average product-fiber floor
`ceil(binom(31,17)/32)=8286954` by 201. It does not falsify the adjacent row:

```text
B_*-M_QR=8490060,
B_*-2M_QR=202905>0.                                  (MQR7)
```

Thus one product class from the zero-remainder quotient-rotation construction
cannot by itself decide Lane M. The theorem is an exact structured lower
floor and a route calibration, not an upper bound on the full list, a
deployed `U_Q`, an MCA statement, or a prize close.
