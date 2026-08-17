# Rank-eleven rich-flat residual mass compiler

- **status:** PROVED
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **input:** PR `#1173`'s anchored `42452`-transverse payment

Every unsafe line has at least

```text
B_*+1=274980728111395088
```

bad slopes. PR `#1173` pays near, high-margin, anchor, and all transverse
rank-one/rank-two groups by

```text
274978720888758363.
```

Therefore the union of nontransverse groups contains at least

```text
E_rich=2007222636725                                      (RM1)
```

selected slopes.

Each original row-space group has at most `R_2=247628052` records, so there
are at least `8106` distinct represented nontransverse row spaces.

For every such rank-`r` row space, canonically promote its rich annihilator
flat to a dimension-`r+1` direction space. Merge all groups receiving the
same promoted space. If `B_2,B_3` are the resulting numbers of distinct
dimension-two and dimension-three containers, then

```text
247628052 B_2 + 3953204973 B_3 >= 2007222636725,          (RM2)
B_2+B_3 >= 508.                                          (RM3)
```

Every container vanishes on at least `42453` common actual coordinates in
the anchor-good set. All pair types assigned to it agree with the received
pair there, so the common-core adapter gives an exact group-local
shortening.

## Nonclaim

The `508` locators need not coincide, and their shortened buckets cannot be
summed without a cross-bucket first-match or chronology theorem.
