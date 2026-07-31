# KoalaBear m2 r4 coordinate negative zero-loop product-to-q weld

- **status:** PROVED
- **scope:** the negative-parity zero-loop `(4,3,3)` skeleton
  `(0,0,0;2,2,1)` retained by `(KBNL-2)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler`
- **consumer:** `rate_half_band_closure`

The five product rows reconstruct the nonconstant Mobius map

```text
p_s=N(s)/D(s),       N,D linear,       D(s)!=0 on K.       (KBN0W-1)
```

Put `v_s=q_sD(s)`.  The five rows

```text
[1,s,s^2,v_s]                                             (KBN0W-2)
```

have rank at most three.  Fix any three common-`K` labels.  The two `4 x 4`
determinants obtained by adjoining each remaining label are necessary and
sufficient for the complete five-row common-`K` sum system.  Thus the
zero-loop signed atlas, like either one-loop atlas, has only two scalar q
welds after product reconstruction.

This theorem does not classify or delete the zero-loop skeleton, impose the
other seven source fibers, handle one-loop or positive parity, close the
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An actual zero-loop packet violating `(KBN0W-2)`, or a candidate passing the
product gate and two determinants but not reconstructing all five common-`K`
sum equations.
