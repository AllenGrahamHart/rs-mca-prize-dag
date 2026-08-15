# Rank-nine exact petal-partition capacity cut

- **status:** PROVED
- **newly closed interval:** `15529<=K'<=15634`
- **remaining rank-nine interval:** `10<=K'<=15528`

In the residual-petal rank-nine chart, put

```text
a=m'-j-1,             67472<=a<=67462+K'.
```

The petal sizes satisfy `0<=s_p<=a` and
`sum_p s_p<=981105+a`. Exact convex packing, rather than the relaxed
per-petal estimate, gives

```text
sum_p [s_p(j-9)+C(s_p,2)]
 <= r q(a)+q(b),
r=1+floor(981105/a),  b=981105 mod a.
```

For `10<=K'<=15634`, this exact expression is largest at `a=67472`, or
equivalently `j=K'-1`. There are fifteen full petals and one remainder of
size `36497`, and the marked component cap is

```text
W_B <= 981105*(1048577*K'+34798536326).
```

The weighted selector demand first exceeds this cap at `K'=15529`:

```text
K'=15528: demand=50114371326035640,
           cap   =50115667510540110;

K'=15529: demand=50120589875892136,
           cap   =50116696274677695.
```

The unrounded demand/cap ratio is strictly increasing after the crossing.
Thus this node closes `15529..15634`; together with the preceding residual
and high-row cuts, rank nine remains possible only on `10..15528`.

## Nonclaim

No rank-eight alternative, chronology assignment, active-v4 movement, or
rank-eleven closure is proved. The interval `10<=K'<=15528` remains open.

## Falsifier

A feasible petal partition above the exact packed value; an admissible
`a>67472` with larger capacity; a failed adjacent-row sign; or a later
reversal of the unrounded demand/cap ratio refutes the claim.
