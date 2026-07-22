# Upstream finite row-sharp Q shortcut route cuts

- **status:** PROVED
- **closure:** proof
- **upstream:** `przchojecki/rs-mca@32a41660`, Grande Finale v4 source
- **role:** roadmap N4 negative-library import

Fix one deployed adjacent row, let `w=a_+-K`, let `B` be the generated base
field, and let `Delta_Q` be the available row-sharp Q margin.

## 1. Moment-order floor

If a pruned residual has full-slice mass `tau in (0,1]`, any proof using only
the upstream ordinary moment criterion must satisfy

```text
r(Delta_Q-log2(tau)) >= w log2|B|.                  (RC1)
```

For `tau=1`, the four minimum orders are

```text
KB MCA 94196,  KB list 94991,
M31 MCA 641593, M31 list 680397.                    (RC2)
```

Thus every fixed low-order full-mass moment route is incapable of proving a
deployed finite Q atom. The numbers in `(RC2)` must not be applied unchanged
after first-match pruning unless `tau=1`; the residual mass must be carried.

## 2. Packing gap

The proved Johnson/anticode Q ceiling permits normalized overheads of
approximately `2^1660789` on KoalaBear and `2^1660926` on Mersenne-31, while
the respective spare margins are only `22.1969`, `22.0109`, `3.2589`, and
`3.0730` bits. This theorem is valid but cannot imply any adjacent row.

## 3. BC is not boundary Q

At the four rows, the boundary-Q affine divisor slice has dimensions

```text
913633, 913634, 913681, 913682.                     (RC3)
```

The moving-root theorem pays one genuine projective locator pencil. It does
not pay `(RC3)` without an additional exhaustive pencil decomposition and a
bound on the number of relevant pencils.

These are route cuts, not Q upper bounds and not evidence that Q is false.
