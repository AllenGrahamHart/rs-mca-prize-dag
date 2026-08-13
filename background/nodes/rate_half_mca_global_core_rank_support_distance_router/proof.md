# Proof

The whole-line global-core router produces one shortened selected family,
with identity slope projection, in the row `(R+s,s,d+s)`.  Choose a minimum
lift `q=r_1-b` of the shortened direction.  The gauge theorem preserves every
selected slope, exact witness support, and same-support pair noncontainment,
while replacing the explanations by `c_gamma-gamma b`.  Thus all three
supplier theorems below apply to the same slope set.

Let `r` be the transformed affine rank.  The gauge-rank theorem supplies its
two-endpoint bound.  On the displayed dimension ranges this pays `r<=13` on
KoalaBear and `r<=5` on Mersenne-31.

Put `e=|supp(q)|`.  Since the lift is minimum, the direction-defect notation
of the recursive theorem gives

```text
e=d_U(y_1)=R-j.                                      (1)
```

The common-zero theorem gives

```text
|Z| <= floor(max_(x=R+r..R+s)
  ((x)_(fall r+1)-(x-e)_(fall r+1))
  /((x-R+d)d_(rise r))).                             (2)
```

Exact integer maximization of `(2)` for every `x` in the displayed
dimension range gives the low-support walls in the statement.  The bound is
increasing in `e`, so each last-paid/first-unpaid adjacent pair certifies the
whole prefix.  Taking the maximum through the last displayed dimension makes
each wall uniform in `s`.

Independently, the recursive direction theorem pays every `0<=j<=J_rec(s)`.
By `(1)` this is exactly the high-support suffix

```text
e>=R-J_rec(s).                                       (3)
```

For each support wall, rank legality first begins at `s=r`.  Substituting the
corresponding `J_rec(r)`, then removing the paid low prefix and high suffix,
gives the printed surviving intervals.  This also enforces `r<=s` rather than
attaching impossible higher ranks to the first residual dimension.  The
three alternatives are upper bounds on one family, so their union is a valid
router without summing any charges.
