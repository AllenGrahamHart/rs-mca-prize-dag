# Proof

Fix one of the 23 endpoint rows. Let

```text
F=-13661092+2953K'                                  (1)
```

be the proved number of full 218-owner coordinates. At each such coordinate,
the owner plane is an endpoint 218-point plane. Its internal direction-bank
theorem supplies at least 210 distinct projective directions represented by
saturated 15-point affine lines in that plane.

For a projective direction `eta`, choose its nonzero residual direction
polynomial `T_eta`. Whenever a full coordinate contributes `eta`, evaluation
vanishes on that direction, so `T_eta` vanishes there. Since
`deg T_eta<K'`, one direction occurs at no more than `K'-1` residual
coordinates. Counting direction-root incidences gives

```text
210F<=sum_eta |Z_D(T_eta)|<=R(K'-1).                (2)
```

Therefore

```text
R>=ceil(210F/(K'-1)).                               (3)
```

Exact evaluation over `K'=4960..4982` makes the right side increase from
41,746 to 44,301. This proves the lower bound in `(DS1)`.

Every represented direction contains one saturated 15-point affine line.
Its 105 unordered selected-point pairs all have that projective direction,
and pair sets belonging to distinct directions are disjoint. Hence

```text
105R<=C(3170,2),
R<=floor(C(3170,2)/105)=47836.                      (4)
```

The parent saturated-line theorem gives each represented line a residual
common core of size at least `K'-2609`. This core lies in the zero set of
`T_eta`, proving `(DS2)`.

Finally define the aggregate unused degree capacity

```text
Delta_dir=R(K'-1)-sum_eta |Z_D(T_eta)|.
```

Using `(2)` and `(4)` gives

```text
Delta_dir<=47836(K'-1)-210F.                        (5)
```

The right side decreases across the endpoint interval and equals 30,203,244
at `K'=4960`. At that row the root-incidence lower bound divided by the
largest possible degree capacity is

```text
210*985788/(47836*4959)
 =207015480/237218724
 =5750430/6589409
 >0.8726.
```

This is the uniform aggregate saturation floor. QED.
