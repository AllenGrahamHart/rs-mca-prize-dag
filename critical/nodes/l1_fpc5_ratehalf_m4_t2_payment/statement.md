# Rate-half FPC5 `M=4,t=2` payment

- **status:** TARGET
- **consumer:** `l1_fpc5_m4_t2_payment`

Fix one admissible maximal rate-half source with `M=4`. Count all non-planted
FPC5 contributors touching exactly two full petals. For a cell

```text
d=ell+s,       0<=s<ell,
```

the proved petal-equation envelope has dimension `2s+2`; the exact cell also
imposes its background roots and exact nonagreements. The formal locator
codimension is at least two. At equality, official arithmetic forces

```text
5ell=k+4,       b=r=s=ell-3,       d=2ell-3,
```

and the full-background guard cuts the pair and locator dimensions to
`ell-1`.

Prove one disjoint aggregate payment of the remaining split-on-core locators
over the six touched pairs and all defect/background cells in this fixed
source. Internal tangent, quotient, and contributor-dependent recharts must
have explicit first owners. No sum over maximal source layouts is needed:
`l1_general_first_layout_domination` makes the fixed-layout payment global
after adding at most four anchors.
