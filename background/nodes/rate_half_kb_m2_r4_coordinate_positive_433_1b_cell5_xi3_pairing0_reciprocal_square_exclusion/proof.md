# Proof

After deleting the outside record, matching `0` pairs the residual products
as

```text
(de,de), (-de,sigma_o ef), (bf,sigma_c cf).
```

For `L_i(q)=B_i-qA_i`, direct expansion gives

```text
paired(q,q)=4 L_0(q)L_1(q)^2L_2(q).              (P0-1)
```

The characteristic is odd, so every finite solution lies on one of the
three branches `q=B_i/A_i`; zero denominators are retained in the candidate
union. Let `m=df`, `S=(d+f)^2`, and `y=1/d^2`. The missing Vieta equation is

```text
1+(2m-S)y+m^2y^2=0,             ef=qmy.           (P0-2)
```

On each branch, the compiler takes the quadratic resultant in `y` of
`(P0-2)` and `paired(-q,sigma_o qmy)=0`, then norms it through the exact
cell-5 row-6 four-basis algebra. The 24 rows cover four source signs, three
branches, and two `sigma_o` signs; each row checks both `sigma_c` lanes.

The exact census is 132 target roots, 324 candidate roots, 120 `r`-guard
records, 96 `t`-guard records, 104 nonsquare no-`b` lifts, and 416 guarded
source routes. Their finite terminal partition is 48 missing-impossible, 48
zero-product, 24 empty-branch, and 296 checked points. No leading boundary
is exported.

Independent Frobenius reconstruction finds 392 roots in 93 polynomial
profiles, with maximum degree 548. A separate replay reconstructs every
candidate union and source relation. It obtains 80 common `y` roots, all 160
`d/e/f` lifts, and 320 final lanes. Every final paired cut is nonzero. Thus
label `(3,0)` is empty, and the exact outside-role orbit theorem transports
the conclusion to `(4,0)`. QED.
