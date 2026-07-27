# E1 first-band variance route boundary

- **status:** PROVED
- **closure:** exact rational, tool-relative route cut
- **scope:** `N=256`, folded profile `(3,4,0)`, square mass `16`

For the fixed cubic-Hermite majorant whose moment inputs are

```text
m_1 = 16,  m_2 = 256 + V,  m_3 = 4096 + 48V + M_3,
```

the tested logarithmic margin is affine in `(V,M_3)` and strictly decreasing
in `M_3`.  Its exact integer thresholds are

```text
V:       68    66    64    62    60    50
M_3*:  1947  1732  1517  1302  1087    13
```

with every printed threshold pinned by positive certified margin at `M_3*`
and negative certified margin at `M_3*+1`.  The affine boundary has slope
strictly between `107` and `108`.  For every even `V` in `2..48`, the
optimistic margin is already negative at `M_3=0`; therefore this fixed
majorant cannot exclude any chamber whose third-moment maximum is
nonnegative.  The route cut is sharp on even levels because `V=50` still has
threshold `13`.

This statement decides no variance level and proves no collision exclusion.
It rules out only continued use of this fixed cubic-Hermite majorant as a
closure mechanism below `V=50`.
