# H3 low-distance norm-class pilot

- **status:** EXPERIMENTAL route evidence; no theorem promotion.
- **Modal app:** `ap-nFVftE3yG19HwOwPvjIehP`.
- **resources:** two sequential functions, one physical CPU, 1 GiB RAM, and a
  120-second hard timeout each.
- **observed function time:** `0.355` seconds at `n=32` and `7.719` seconds at
  `n=64`.
- **campaign cost cap:** `$0.10`; published-rate requested-resource cost for
  the completed function time is below `$0.001`.
- **result hash:**
  `61f30dd669202102d8360ceb2b013d6fa8106a38e3a7647e8bdbc23b209e69ca`.

The complete squared-norm-at-most-three edge census separates normalized
collision norms by squared distance:

```text
order  distance  edge orbits  distinct norms  odd factors  relevant factors
32     2         154          3               0            0
32     4         1,701        34              17           4
32     6         2,967        210             120          103
64     2         393          4               0            0
64     4         9,619        163             102          67
64     6         41,527       3,735           2,212        2,127
```

Distance two is exactly 2-primary on both complete orders, agreeing with the
proved theorem. Distance four is not: at `n=32` one normalized norm is
`1282=2*641`, and odd factors persist at `n=64`. Thus distance four cannot be
deleted from the official candidate generator.

The route split is nevertheless useful. Distance four has far fewer norm
templates and relevant factors than distance six. It is a bounded four-term
obstruction lane; distance six remains the dominant generic lane. A larger
raw census is not selected.

Replay the pinned summary checks with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/h3_low_distance_norm_class_pilot_check.py
```
