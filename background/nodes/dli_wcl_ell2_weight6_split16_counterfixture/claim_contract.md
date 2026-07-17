# Claim contract - DLI ell-two weight-six split-16 counterfixture

## Proven

1. A genuine reduced order-1024 weight-six solution exists in `GF(65537)`.
2. It satisfies both moments and every router guard.
3. The field has `v_2(q-1)=16`.
4. Order-1024 splitting alone cannot close the official slot.

## Still open

Exclude all guarded solutions in characteristics below `2^256` with
`v_2(q-1)>=41`, or find an actual characteristic in that range.

## Consumer effect

Use this node as route-cut evidence for `dli_wcl_zone_coverage`. It is not a
logical requirement and changes no critical status.
