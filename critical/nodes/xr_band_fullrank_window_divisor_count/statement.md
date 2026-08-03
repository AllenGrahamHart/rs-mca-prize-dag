# XR full-rank maximal window-divisor count

- **status:** TARGET
- **parent:** `xr_band_maximal_window_divisor_count`

In the setup of SL-2-RES, assume the stacked window matrix has full row
rank:

```text
rank J_d(u,v)=2d.
```

Then the maximal, selected, post-strip locator set satisfies

```text
25 |R_d(u,v)| <= 17 n^2.
```

All four filters in the parent statement remain load-bearing. This is
a split-divisor anti-concentration statement in a genuinely
codimension-`2d` affine window, not a raw affine-point count.

## Falsifier

One official row and high depth with full stacked rank and more than
`17n^2/25` locators passing maximality, selection, and every prior strip.
