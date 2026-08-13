# Proof

Let `N` be the near-rational first-match set and `E` the residual exception
set.  The proved two-anchor theorem gives

```text
|N|<=2w,
```

while the active order-32 conditional assembly assumes `|E|<=31`.  Since
`2w` is `134,944` on KoalaBear and `134,896` on Mersenne-31, `N` cannot be
silently included in `E`.  Remove the two disjoint sets in chronology order
and put

```text
R=2w+31.
```

In a rational atom with owner size `g>2m-K`, the existing localization splits
the residual into at most `n-g` crossing slopes plus the owner-contained
slopes.  Therefore the exact target required of the latter is

```text
B* - R - (n-g).
```

If that target holds, the four terms satisfy the identity

```text
2w + 31 + (n-g) + [B*-(2w+31)-(n-g)] = B*.
```

This proves the large-owner branch of the revised conditional assembly.

The other coherent branches remain arithmetically harmless.  A global affine
line or a rational atom with `g<m` contributes at most `n-m+1` residual
slopes, so the total is at most `R+n-m+1`.  For `m<=g<=2m-K`, the residual
contributes at most `n`, so the total is at most `R+n`.  The verifier checks
both totals are strictly below `B*` on both rows.  A residual set of at most
31 slopes is even smaller, and a spread input is assumed to pay the whole
line exactly as in the source conditional theorem.

At `g_min=2m-K+1`, substitution gives the first table target; at `g=n` it
gives `B*-R`.  Relative to the printed source target `B*-31-(n-g)`, every
revised target is lower by exactly `2w`.

Finally, the proved full-owner average ceilings are `57,198,030,366` and
`1,752,700`.  Exact Euclidean division gives

```text
274980728111260112 = 4807520*57198030366 + 53166107792,
          16642288 =       9*1752700     + 867988.
```

Hence the revised targets remain above the stated integer multiples of the
average ceilings.  This is arithmetic viability only; it does not prove a
maximum-fiber theorem at either factor.
