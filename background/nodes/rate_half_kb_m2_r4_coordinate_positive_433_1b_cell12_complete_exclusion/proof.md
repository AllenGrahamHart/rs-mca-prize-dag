# Proof

The 105 labels are pairs `(xi,j)` with `0 <= xi <= 6` and
`0 <= j <= 14`. Seventeen proved suppliers form a disjoint partition:

- endpoint roles `xi=5,6`: 30 labels;
- first pairings `j=0,1,2` for `xi=0,1,2`: 9 labels;
- the seven remaining parallel-`DE` orbit packets: 36 labels;
- the eight reciprocal outside-role packets for `xi=3,4`: 30 labels.

The assembly verifier writes each supplier's exact label set, proves the sets
are disjoint, and proves their union is the full 105-label rectangle. Every
supplier is `PROVED`. The rational-boundary theorem pays every leading chart
excluded from the four-basis computations. Therefore cell 12 is empty.
