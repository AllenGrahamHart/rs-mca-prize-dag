# Proof

Apply
`rate_half_mca_rank11_anchor_exchange_split_pencil_synchronization` to the
fixed dense anchor. If one of its base or one-swap packets has the
high-complexity output, the desired router conclusion already holds.

Otherwise all those packets are rational and one fixed coprime pencil
contains the exception locators of all 5524 anchor records. The normal form
proves that these locators have pairwise-disjoint nonempty root sets.

Assume the base rational pencil is in the normalized nonzero
affine-reflection class `(AR2)`. Every rational one-swap pencil is the same
two-dimensional polynomial subspace, so its new locator is another fiber of
that same normalized pencil. Thus the fixed reflection must support at least
5524 nonfixed two-cycles in the official domain.

At least one split fiber exists, with roots `x,y in H subset F_p`. Its fixed
sum gives

```text
c=x+y in F_p.
```

The branch assumption gives `c!=0`. The exact official cyclotomic census in
`rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap`
therefore applies and bounds the number of nonfixed fibers by `1154`. Since

```text
5524>1154,
```

the all-rational alternative is impossible. Hence some packet has
`chi>=2299571`. QED.

No estimate on the number of packet certificates is summed. The contradiction
uses one synchronized pencil and its pairwise-disjoint anchor fibers.
