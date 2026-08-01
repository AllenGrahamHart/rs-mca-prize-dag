# KoalaBear m2 r4 coordinate negative zero-loop 433 aligned doubled-pair finite classifier

- **status:** PROVED
- **scope:** common matching cells `[2,5,6,9]` in every root-sign row over
  the deployed field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

In cell `2`, `AB+` is the singleton and the source antipodal pairs are
`AB-:BC+` and `AC+:AC-`.  Normalize

```text
roles=(AB+,AB-,AC+,AC-,BC+),
roots=(t,1,r,epsilon_2 i r,epsilon_1 i),
x=t^2, y=r^2.                                    (KBZ433F-1)
```

Exact ratio-preserving product and quadratic-q elimination gives the common
packet census

```text
(epsilon_1,epsilon_2)   basis  deg E_b  base b roots  packets
(+,+)                     8       18          8          4
(+,-)                     4        4          2          0
(-,+)                     4        4          2          0
(-,-)                     8       18          8          4. (KBZ433F-2)
```

The eight representative packets `(b,c,r,t)` are

```text
(+,+):
(2122238824,2130706431,374290000,583634934),
(1069587021,1065353216,374290000,583634934),
(1061119412,1065353216,1722993073,1547071505),
(8467609,2130706431,1722993073,1547071505);

(-,-):
(2122238824,2130706431,1764884040,1547071505),
(1069587021,1065353216,1764884040,1547071505),
(1061119412,1065353216,399245749,583634934),
(8467609,2130706431,399245749,583634934).          (KBZ433F-3)
```

Every tuple passes the original two product and two q determinants and the
full guard.  All other base-field projections and every lost branch are
guarded or false.  Target sign/exchange transports cell `2` through
`[2,5,6,9]`, giving exactly `4*8=32` common packets in this orbit.

This theorem does not impose the seven outside fibers, prove that any of the
32 packets completes, delete the four-cell orbit, classify cells
`[12,13,14]`, close the coordinate orientation, close a Prize row, or prove
either Prize result.

## Falsifier

A ninth guarded packet in cell `2`, failure of a listed tuple in an original
equation or guard, a valid lost-branch packet, or a failed target transport.
