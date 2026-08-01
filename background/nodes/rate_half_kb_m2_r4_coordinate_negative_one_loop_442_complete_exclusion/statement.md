# KoalaBear m2 r4 coordinate negative one-loop 442 complete exclusion

- **status:** PROVED
- **scope:** every negative one-loop `(4,4,2)` common matching cell, every
  source root-sign row, and every complete outside skeleton
- **dependencies:** the six terminal orbit deletions listed below
- **consumer:** `rate_half_band_closure`

The fifteen common matching cells split disjointly as

```text
[0]              aligned loop singleton,
[1,2]            crossed loop singleton,
[3,6]            AB nonloop singleton,
[4,5,7,8]        mixed-pair nonloop singleton,
[9,10,12,13]     AC-sextic nonloop singleton,
[11,14]          opposite-pair nonloop singleton.       (KB41C-1)
```

The aligned loop-q exclusion deletes `[0]`; the crossed and opposite-pair
common exclusions delete `[1,2]` and `[11,14]`; the AB `S1` terminal close
deletes every product cell over `[3,6]`; the mixed-pair common exclusion
deletes `[4,5,7,8]`; and the terminal `S0` guarded product exclusion,
together with its required `S1/S2` chain, deletes all eighty product cells
over `[9,10,12,13]`.

These six PROVED results cover every cell in `(KB41C-1)` and every sign and
outside-skeleton class retained by its cell.  Therefore no complete
negative one-loop `(4,4,2)` packet exists.

This theorem does not treat negative one-loop `(4,3,3)`, zero-loop,
two-loop, positive parity, another coordinate orientation, a whole Prize
row, or either Prize result.

## Falsifier

A fifteenth-cell partition defect, a sign or outside skeleton not covered
by its terminal parent, or an admissible complete negative one-loop 442
packet surviving all six terminal deletions.
