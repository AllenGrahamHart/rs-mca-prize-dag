# KoalaBear m2 r4 coordinate negative one-loop product-to-q weld

- **status:** PROVED
- **scope:** both negative-parity one-loop skeletons retained by `(KBNL-2)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler`
- **consumer:** `rate_half_band_closure`

Let `h in K` be the unique loop label.  Write the nonconstant product map as

```text
p_s=N(s)/D(s),       N,D linear,       D(s)!=0 on K.       (KBN1W-1)
```

For each of the four nonloop labels put

```text
w_s=q_s/(p_h-p_s).                                      (KBN1W-2)
```

The four rows

```text
[1,s,w_s]                                                (KBN1W-3)
```

have rank at most two.  Equivalently, for distinct nonloops `i,j,k`, the
denominator-free weld

```text
q_i d_j d_k(k-j)+q_j d_i d_k(i-k)+q_k d_i d_j(j-i)=0,
d_s=p_h-p_s,                                             (KBN1W-4)
```

holds.  Fixing any two nonloop labels, the two instances with each remaining
label are necessary and sufficient for the complete five-row common-`K` sum
system.  Thus every signed candidate needs only the product rank/support gate
and two scalar welds.

This theorem does not classify or delete either one-loop skeleton, impose the
other seven source fibers, handle zero-loop or positive parity, close the
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An actual one-loop packet violating `(KBN1W-3)--(KBN1W-4)`, or a candidate
passing the product gate and two welds but not reconstructing the one-loop
common-`K` sum system.
