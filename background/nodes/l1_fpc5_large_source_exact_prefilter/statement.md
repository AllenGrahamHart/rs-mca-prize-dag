# L1 FPC5 large-source exact prefilter

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one maximal FPC5 source chart with

```text
N=k-1,       |B|=b<ell,
```

one touched set of `t` full petals, and one defect degree `d`. Put

```text
h=t ell,
r=2d-h,
u=d+ell-h=d-(t-1)ell.                                (PF1)
```

For the exact contributor cell at these parameters:

1. if `u>b`, the cell is empty;
2. if `r<0` or

   ```text
   2d>N+(t-2)ell+b,                                  (PF2)
   ```

   the cell has at most one contributor; and
3. if `b>0`, `0<=u<=b`, `r>=0`, and

   ```text
   J_bg=b d^2+N u^2-N b r>0,                         (PF3)
   ```

   then its contributor count `m` satisfies

   ```text
   m<=N b ell/J_bg<=n^3.                             (PF4)
   ```

The ordinary fixed-support Johnson payment also applies when

```text
d^2-Nr>0.                                             (PF5)
```

Consequently every nonempty, nonsingleton, unpaid fixed cell in the
large-source target must satisfy all of

```text
r>=0,
u<=b,
2d<=N+(t-2)ell+b,
d^2<=Nr,
u<0 or b=0 or J_bg<=0.                               (PF6)
```

Before the two Johnson tests are imposed, the exact integer upper endpoint
of this residual is at most

```text
U_prefilter=min {
  min(ell(M-2)-1,N),
  (t-1)ell+b,
  floor((N+(t-2)ell+b)/2)
}.                                                    (PF7)
```

Thus the `u>b` EMPTY charge and the background-overlap singleton charge are
theorem-level filters for every official `ell`, not percentages inferred
from the earlier three-point `ell` sample. The remaining target is the
disjoint aggregate payment of the cells satisfying `(PF6)`.

## Scope

The theorem is per fixed source chart, touched-petal set, and defect degree.
It does not sum touched sets, source layouts, petal polarities, or the
nonpositive-Johnson residual. In particular, it does not promote the sampled
`71.38%` EMPTY figure to a full-grid density statement.
