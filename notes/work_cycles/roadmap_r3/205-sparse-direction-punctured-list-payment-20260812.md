# Cycle 205: sparse-direction punctured-list payment (2026-08-12)

Cycle 204 expands the low-defect side of the shortened global-core family.
The opposite, extremely high-defect side has a separate ordinary-list
reduction.

Suppose the shortened direction is

```text
r_1=b+q,       b in C,       E=supp(q),       |E|=e<d.
```

For every selected slope, subtract `gamma b` from its codeword explanation.
Outside `E` this produces a codeword agreeing with the base received word on
at least `d+s-e` coordinates.  Puncturing `E` and applying the complete-code
affine-span list theorem gives at most

```text
floor(C(R-e+s,s)/C(d-e+s,s))
```

distinct base explanations.  Pair noncontainment forces every witness to
meet `E`; for a fixed explanation and coordinate `x in E`, the equality
`a(x)-r_0(x)=gamma q(x)` determines at most one slope.  Hence

```text
|Z| <= e*floor(C(R-e+s,s)/C(d-e+s,s)).
```

At the first dimensions not paid uniformly in the direction, exact integer
evaluation gives

```text
KoalaBear, s=14: e=5 gives 239567470186217925 <= B*;
                  e=6 gives 287536780021025682 > B*.
Mersenne, s=6:   e=1 gives 14115447 <= B*;
                  e=2 gives 28233244 > B*.
```

Thus the first residual dimension also pays the high-defect tails
`j=R-e>=1048571` and `j>=1048575`, respectively.  The middle defect interval
and all out-of-gate dimensions remain open.

The primary checker scans all 134,918 legal support sizes using exact
binomials.  The independent checker reconstructs the ratios as cancelled
integer products and preserves the theorem's `e*floor(...)` order.  Four
mutations and three controls are rejected.

```text
start:                   3dec7412c
result:                  PROVED sparse-direction punctured-list payment
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none
upstream terminal delta: extreme high-defect tails paid at the first
                         residual dimension
delta-star movement:     none
compute:                 tiny integer arithmetic under RAMguard;
                         no Modal spend
next route action:       attack the middle direction-defect interval
```
