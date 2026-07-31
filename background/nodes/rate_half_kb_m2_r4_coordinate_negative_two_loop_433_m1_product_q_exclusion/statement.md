# KoalaBear m2 r4 coordinate negative two-loop 433 M1 product-q exclusion

- **status:** PROVED
- **scope:** cell `M1` in the residual `(4,3,3)` two-loop frontier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld` and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut`
- **consumer:** `rate_half_band_closure`

In cell `M1`, normalize the labels and products as

```text
(k_A,k_C,k_+,k_-,k_BC)=(R,M,1,-1,-R),       M^2+1=0,
(p_A,p_C,p_+,p_-,p_BC)=(-1,-c^2,b,-b,bc).       (KBM1-1)
```

Split first on the Mobius-chart denominator `b+R`.

On the boundary `b+R=0`, the five raw product minors and the actual-packet
guards force

```text
b=-R,     M=R^3,     c=MR^2.                       (KBM1-2)
```

Consequently `R^6+1=0`, while the second squared q weld reduces to
`-2(R^5-R+2)=0`.  Their exact resultant in `R` is `4`, so this boundary is
empty in odd characteristic.

On the interior `b+R!=0`, the unique affine Mobius chart through the first
three product values leaves exactly

```text
E1=bcR^2+bc+2bR+2cR+R^2+1,
E2=-b^2M+b^2R+bc^2MR-bc^2-bMR+b+c^2M-c^2R,
Q =(1-R)^2(c^2+b)^2+4c^2R(1+b)^2.                 (KBM1-3)
```

Let `I=<M^2+1,E1,E2,Q>`.  Exact integral lexicographic elimination gives

```text
(b+1)(R-1)^3(R+1)^3(R^2+1)^2 T in I,
T=MR+3M+5R^2+3R+4.                               (KBM1-4)
```

Every prefactor in `(KBM1-4)` is nonzero for an actual packet, so `T=0`.
The augmented ideal satisfies

```text
b^2(b+1)^2 in I+<T>.                              (KBM1-5)
```

But `b!=0,-1`: `B` is nonzero and its signed pair is distinct from the
normalized `A` pair.  This contradiction proves

```text
M1 is empty.                                      (KBM1-6)
```

The common-`K` cells still requiring classification are now only `M2,M3`;
the compiled `X2,N1,L1` rows remain for complete-packet assembly.

This theorem does not delete those cells, use the other seven fibers,
close the `(4,3,3)` skeleton or coordinate orientation, move an
owner/payment, close a row, or prove either Prize result.

## Falsifier

An actual `M1` packet, failure of either interior ideal-membership
certificate, failure of the boundary resultant certificate, or a
guard-compatible solution of `(KBM1-1)` with all product minors and weld
zero.
