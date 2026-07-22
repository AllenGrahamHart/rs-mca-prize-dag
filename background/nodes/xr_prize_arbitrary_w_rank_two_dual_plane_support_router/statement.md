# XR prize arbitrary-`W` rank-two dual-plane support router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_arbitrary_w_trade_circuit_segre_router`,
  `xr_prize_rank_one_trade_flat_basis_owner`

Let a genuine rank-two four/five-block circuit have row-space basis `F,G`,
coefficient directions `beta_i=[c_i:d_i]`, row supports `S_i`, and

```text
X=union_i S_i.
```

Then

```text
L=<F,G> subset (W|X)^perp,                            (DP1)
```

`F,G` have no common zero on `X`, and the supports are determined by one
projective fiber map:

```text
phi:X->P^1,       phi(x)=[F(x):G(x)],
S_i=X\Z_i,        Z_i={x:c_iF(x)+d_iG(x)=0}.          (DP2)
```

Fibers belonging to distinct coefficient directions are disjoint. In a
four-block circuit all `beta_i` are distinct. In a five-block circuit every
coefficient direction has multiplicity at most two.

If two five-block rows have the same coefficient direction, their trade rows
are proportional and have the same support `S`. Their two distinct selected
slopes force

```text
b|S in W|S,       q|S in W|S.                         (DP3)
```

Hence the repeated pair receives the same canonical spanning-basis or proper-
flat owner as in `xr_prize_rank_one_trade_flat_basis_owner`; the spanning
basis population is at most `floor((R-v)/h)`.

Every row also has an exact arbitrary-`W` locator certificate. For
`s_i=|S_i|`, there is a unique polynomial `Q_i` of degree below `s_i`, nonzero
on `S_i`, such that

```text
lambda_i(x)=Q_i(x)/Lambda'_(S_i)(x),
sum_(x in S_i) Q_i(x)f(x)/Lambda'_(S_i)(x)=0
                                      for every f in W. (DP4)
```

Conversely, a dual plane, a certified four/five Segre circuit, and selected
blocks containing the supports in `(DP2)` reconstruct the trade. Thus the
arbitrary-`W` support tuple is one dual plane plus its projective fibers, not
four/five independent subsets.

This theorem does not count dual planes/fibers or deduplicate them across
Maxwell cores.
