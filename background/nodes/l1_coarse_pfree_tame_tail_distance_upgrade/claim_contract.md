# Claim contract - L1 coarse p-free tame-tail distance upgrade

## Inputs

- disjoint squarefree tail locators of common degree `t`;
- the coarse p-free Wronskian upper degree from the supplier;
- the official `p>n/24` bound only for the final row specialization.

## Output

When `t<p`, the Wronskian has degree at least `t-1`. Every coarse p-free
depth-`d` collision therefore has width at least `tau_p` in `(TTD3)`, giving
the improved packing cap `(TTD6)` and the official checkpoint floor
`t>=p>n/24`.

## Falsifier

A disjoint pair with `t<p` and `deg W<t-1`, or a coarse depth-`d` collision
with tail width below `tau_p`.

## Nonclaims

No exclusion at `t=p`, no exchange-subset count above `tau_p`, no finite
row-sharp flatness, and no L1 status change.
