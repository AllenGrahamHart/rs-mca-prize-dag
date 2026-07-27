# E1 N=256 square-mass-16 variance-68 endpoint exclusion

- **status:** PROVED
- **closure:** proof synthesis

No pair-feasible folded-profile `(3,4,0)` collision at `N=256`, square mass
16, has autocorrelation variance `V=68` (`E=34`).

The complete chain is:

```text
24 integer profiles
 -> (6,7), (9,4,1), (12,1,2)
 -> (6,7)
 -> quarter / nonquarter diameter / progression / generic
 -> empty.
```

All transitions and all four terminal exclusions are proved. Consequently the
live positive even variance range in this profile sharpens from `V<=68` to
`V<=66`.

This theorem does not exclude any lower variance or the separate `(4,2,0)`
first-band profile.
