# Cycle 435: rank-eleven low-span and product-cover exclusion

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: bd851028c
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
crosswalk: PASS, 103 rows, pinned 052061e85/93fba1be
```

The crosswalk's canonical pin predates the current Fable head but validates at
its declared scope. No source tree was modified.

## Action

Attack PR `#1173`'s heavy-rich-flat terminal by asking whether all
nontransverse row-space groups can be charged together when their collective
correction span is small. Keep the arithmetic payment separate from the
factor-product algebra.

## Result: NARROWED

Two PROVED background nodes were added.

1. `rate_half_mca_rank11_low_span_residual_payment` proves that every unsafe
   survivor has collective nontransverse span at least seven. At
   `(tau,h)=(1549,42451)`, the transverse envelope plus one dimension-six
   interleaved affine-container charge is
   `274963410460662890`, below `B*=274980728111395087` by
   `17317650732197`. The adjacent `h=42452` formula is over by
   `1804196591101`.
2. `rate_half_mca_rank11_common_factor_product_cover_exclusion` proves that a
   complete common `2 x 3` factor-product cover has span at most six and is
   therefore absent from an unsafe survivor. Under exact-product distinct-
   pencil hypotheses, its fixed locus has at least `42325` actual
   coordinates.

The lower threshold strengthens the survivor population to

```text
nontransverse mass >= 33226847021583
represented row spaces >= 134181
promoted rich containers >= 8406
common zeros per container >= 42452
collective row-space span >= 7.
```

## Burn-down

```text
node/workboard item: KoalaBear rank-eleven anchored rich-flat terminal
result: NARROWED
DAG delta: +2 PROVED background nodes, +7 edges; critical open count remains 28
upstream delta: exact continuation of open PR #1173 prepared; not exported while live
delta-star movement: none
new assumptions: none in the survivor theorem; product-cover hypotheses are a paid subclass
live compute requests: none
Modal spend: zero
next action: classify or pay collective correction-span dimensions 7..10,
             using the 8406-container population inside the fixed ten-space C'
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_low_span_residual_payment/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_low_span_residual_payment/verify_audit.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_common_factor_product_cover_exclusion/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_common_factor_product_cover_exclusion/verify_audit.py
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
