# XR rank-two Maxwell properness

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependencies:** `xr_split_pencil_trade_rank_two_support_atlas`,
  `xr_split_pencil_maxwell_core_extraction`

Let `G` be one of the official uniform-block Maxwell cores. Thus every block
has size `m=4+c`, with

```text
P-A:          (m,c) in {(9,5),(7,3)},
P-B one-loop: (m,c) in {(10,6),(8,4)}.
```

Suppose a nonzero left-kernel relation has trade-matrix rank two, and let
`J` be its set of active blocks. Put `t=|J|` and
`v_J=|union_(A in J) A|`. Number the five support profiles from the preceding
atlas in its displayed order. Then

```text
                  profile 1  2  3  4  5
(m,c)=(7,3):          8     2  4  9 10
(m,c)=(8,4):         12     6  8 14 16
(m,c)=(9,5):         16    10 12 19 22
(m,c)=(10,6):        20    14 16 24 28
```

are exact set-system lower bounds for the Maxwell deficit

```text
Delta_J=2v_J-8-ct.                                    (MP1)
```

In particular,

```text
Delta_J>=2.                                           (MP2)
```

The full Maxwell core instead has

```text
c|G|=2|union G|-8+e,       e>=0,
```

so its full-family deficit is `-e<=0`. Consequently `J` is always a proper
subfamily of `G`. Equivalently, if a Maxwell anomaly is a block circuit in
the sense that every nonzero left relation activates every block, then its
trade-matrix rank is at least three.

The minimum two and every table entry are sharp for abstract block set
systems satisfying the five support profiles and pair cap four. Therefore
this theorem separates a proper local-circuit branch from the primitive
full-core rank-at-least-three branch; it does not exclude the local branch,
count its embeddings, or promote either consumer.
