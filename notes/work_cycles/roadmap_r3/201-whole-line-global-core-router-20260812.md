# Cycle 201: whole-line global-core router (2026-08-12)

Cycle 200 proves that a critical record's local core is not a slope invariant.
There is nevertheless one exact repair: intersect the declared selected
maximal supports over the entire residual slope set on one received line and
cancel that core once.

For any finite selected slope set with at least two slopes, either all
selected explanations lie on one global codeword line, or its global core
`C_*` has size below `k`. In the latter case the imported common-core theorem
applies simultaneously to every selected slope:

```text
(n,k,m) -> (n-c_*,k-c_*,m-c_*).
```

The slope map is literally the identity, has exact fiber one, and preserves
`m-k`, `n-k`, `n-m`, maximal supports, and actual same-support
noncontainment. There is one global family, so no local-core count or
add-back occurs.

At the imported KoalaBear walls this gives a total paid/residual router:

```text
global affine                                  paid by the global block
s<=2                                           paid fixed-core family
3<=s<=13 plus direction separation             paid affine-span family
3<=s<=13 without direction separation          explicit direction residual
s>=14                                          explicit global-core residual
```

The `GF(11)` collision control has `C_*={10}` and shortens `(10,5,7)` to
`(9,4,6)`, preserving all seven slopes. The shortened direction has maximum
degree-`<4` agreement six, exactly `m'`; the router therefore emits the
direction-list residual at `s=4` and does not manufacture a payment.

The primary checker verifies cancellation, exact supports, noncontainment,
the direction gate, all official staircase walls, and 4/4 mutations. The
independent audit exhausts `7*11^4=102,487` shortened codewords and 3/3
controls.

```text
start:                   83eefd94f
result:                  PROVED whole-line identity-fiber core router
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none
upstream terminal delta: local-core ownership repaired without a forest;
                         direction and large-global-dimension bins remain
delta-star movement:     none
compute:                 tiny exact GF(11) replay; no Modal spend
next route action:       attack the direction-list residual first, since the
                         exact control shows it occurs before s=14
```
