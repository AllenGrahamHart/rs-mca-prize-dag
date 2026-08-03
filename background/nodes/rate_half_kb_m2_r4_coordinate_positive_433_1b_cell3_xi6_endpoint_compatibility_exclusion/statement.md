# Statement

## Claim (KBP1B3-XI6-ENDPOINT-1)

On the guarded positive deployed 433-1b role-cell-3 branch, every atlas case
with missing record `xi=6` (the `sigma_c cf` record), any canonical matching,
any source sign `epsilon in {+-1}^2`, and any target lane
`sigma in {+-1}^2` is empty.

For each source point put `m=sigma_c cf`, `g=sigma_c f`, and
`s=c^2+f^2+2 sigma_c cf=(c+g)^2`. Since `m=cg` and guarded points have
`c!=0`, every target necessarily satisfies

```text
(c^2+m)^2-s c^2 = 0.
```

An exact four-row source census over the global quadratic quotient proves
that no guarded source point satisfies this necessary compatibility. The cut
does not use a matching or target sign, so the four rows pay all
`15*4*4=240` raw `xi=6` cases.

The same census finds six compatible source points in each `xi=5` source-sign
row. Those 24 points are retained as frontier, not asserted to be target
witnesses. No `xi in {4,5}`, complete cell-3, K3, LIST, MCA, or Prize result
is claimed.
