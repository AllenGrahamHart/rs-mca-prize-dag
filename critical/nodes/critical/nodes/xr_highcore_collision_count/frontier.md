# Frontier

## Paid

- post-strip cross-slope cores are at most `k`;
- fixed-core pencil populations obey the moving-root/sunflower bound;
- the exact W-collision pair moment and codeword-pair regrouping are proved;
- every generic fixed union chart `|U|=R+d` obeys the field-independent GRK
  ray bound. Exact candidate arithmetic pays `d<=3` at all RowC rates and
  `d<=11,10,9` at the prize rates `1/4,1/8,1/16` respectively.
- the canonical component-union atlas partitions the high-core slope set,
  chooses one witness ray per slope, and applies GRK once per disjoint slope
  component. This resolves deduplication across collision cores and union
  charts exactly.
- the all-LineRay affine-core theorem pays the slope target whenever any
  one-per-slope selector has affine error rank `sigma<=3`, directly by
  `C(sigma+r,sigma)<=8n^3`. It separately counts the complete pair family at
  its full affine rank. Exact arithmetic rejects `sigma=4` at all six rows.
- the collision-line basis ledger proves `sum_ell b_ell<=C(n,s-1)` and the
  exact line cap `floor((n-k)/(A-k))`. A line with only `b` bases puts the
  whole selector in a chart of excess at most `b+s-2`; a minimum-basis line
  also self-localizes the basis injection to that chart. Uniform core matroids
  are paid through ranks `13,9,7,60,40,30` on the six rows.
- the affine-core cogirth ray bound proves
  `#slopes C(h+s-1,s-1)<=C(N,s-1)(N-s+1)`. It pays full-domain ranks through
  `4,4,3,11,11,10` and, on the self-localized line charts, closes selector rank
  four on all six high-core rows.
- every high-direction-distance fixed chart obeys the field-independent DDR
  bound `<=|U|^2`; the exact complementary branch has a sparse lift of the
  received direction. For an MDS chart direction at the prize rows, DDR pays
  residual excess through `d=45,210,182`, `38,693,399`, and `8,985,287` at
  rates `1/4`, `1/8`, and `1/16`. At RowC scale the MDS-direction excess
  threshold is zero.
- every uniform flat-nullity cell `u=v=0` at arbitrary selector rank
  `s=a+1` has a coherent `GRS_a` split-pencil compiler. Any over-budget family
  contains a bounded Maxwell core with an anomalous dual-product-code trade.
  Trade rank one is absent, while trade rank two uses at most `2a` active
  coordinates and a degree-at-most-`a-1` polynomial pencil.
- at the minimum rank-two union `a+2`, every trade is either an exact regular
  Plucker face syzygy or a common `k+2` near-tangent interpolation core. Mixed
  denominator collapse is impossible. Quotienting the regular local spaces
  moves the rank-two frontier to union at least `a+3`, apart from the explicit
  tangent deficit `h-2`.

## Open

Prove the aggregate distinct-slope count `<=8n^3` by controlling the explicit
canonical ledger

```text
sum_C floor(C(R+d_C,d_C) R / C(d_C+h,d_C)).
```

Every selector of the open family must have affine error rank at least five
at RowC `1/4,1/8`, and at least `12,12,11` at the prize rates `1/4,1/8,1/16`,
respectively. At RowC `1/16` the open family requires rank at least five OR
rank four with a line-free/line-uncovered min-rank selector hull (catch #158
-- CLB3/CLB4 coverage is not automatic for selected members).
Within the component route, the open quantities are the number of collision
components and their union excesses `d_C`; chart deduplication itself is paid.
The P9 profile records giant connected toy components with `d_C=k`, canonical
selector rank `k+1`, and no selector of rank at most three after the tangent
deletion. Thus neither a general small-excess claim nor a universal low-
transversal-rank claim is supported. The collision moment still cannot
replace the distinct-slope target. On the DDR complement, use the sparse-
direction normal form rather than treating low direction distance as an
unnamed exception.

The arbitrary-rank uniform compiler is structural rather than a payment. Its
open output is the actual count/classification of primitive trade rank at
least three and of the bounded rank-two pencil charts. The nonuniform
flat-nullity cells `u+v>0` remain outside that compiler. A continuation must
either pay those two outputs or connect them to the canonical
component-excess ledger; merely extracting another rank defect does not
improve the target.

The minimum-face theorem makes the near-tangent branch a named output rather
than an anonymous rank-two exception. It is paid automatically only for
`h<=2`; no current P-A row meets that condition. The exact deficits are
`3,3,1` on RowC `1/4,1/8,1/16` and `2^33-1,2^33-1,2^32-1` on the corresponding
prize rows. No statement here treats `k+2` as full tangent agreement when
`h>2`.
