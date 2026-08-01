# KoalaBear m2 r4 coordinate negative zero-loop 433 BC-singleton finite classifier

- **status:** PROVED
- **scope:** common matching cells `[12],[13],[14]` in every root-sign row
  over the deployed base field
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

All three cells have singleton `BC+`.  In cell `12`, the first product row
splits into

```text
(-b+c r^2)(b r^2-c)=0,
c=b r^2                 or                 c=b/r^2. (KBZ433B-1)
```

Each branch has exactly two guarded packets in every sign row.  Thus cell
`12` has 16 packets.  In cells `13,14`, the product branches are

```text
cell 13: c=b((r-1)/(r+1))^2 or b((r+1)/(r-1))^2,
cell 14: c=-b((r-1)/(r+1))^2 or -b((r+1)/(r-1))^2. (KBZ433B-2)
```

Their opposite-sign q row forces `r=+/-i`, violating label injectivity.
Each same-sign row has two packets per branch.  Therefore the exact census is

```text
cell       (+,+)  (+,-)  (-,+)  (-,-)  total
12            4      4      4       4     16
13            4      0      0       4      8
14            4      0      0       4      8.       (KBZ433B-3)
```

Every admitted tuple passes the original four common equations and full
guard.  All solve losses are empty, guarded, or false on a prior linear row.
Together with the proved four-cell classifier and two four-cell exclusions,
the complete zero-loop 433 common atlas has exactly 64 packets: 32 in
`[2,5,6,9]`, 32 in `[12,13,14]`, and none in the other eight cells.

This theorem does not impose outside edge products on the 32 new packets,
delete a live common packet, close the coordinate orientation, close a Prize
row, or prove either Prize result.

## Falsifier

A guarded packet omitted by `(KBZ433B-3)`, failure of an admitted tuple in
an original equation, a valid opposite-sign cell-13/14 packet, or a valid
lost-branch packet.
