# Proof

The low-difference Johnson theorem applies to the larger family of records
with difference degree at most `d`.  Hence, when `Delta_(e,d)>0`, its exact
degree-`d` subfamily satisfies

```text
D_(e,d)(S0)<=floor(N(e-d)/Delta_(e,d)).                 (1)
```

Split the positive cells into two classes.

If `Delta_(e,d)>=N`, equation `(1)` gives

```text
D_(e,d)(S0)<=e-d<=N/2.
```

There are fewer than

```text
sum_(e=1)^(N/2)(e-1)<N^2/8
```

possible pairs `(e,d)`, so all such cells contribute less than `N^3/16`.

Now suppose `0<Delta_(e,d)<N`.  For fixed `e`, increasing `d` by one
decreases `Delta_(e,d)` by exactly `N`.  Therefore at most one integer `d`
for each `e` lies in this boundary interval.  There are at most `N/2` such
cells, and equation `(1)` gives the crude bound

```text
D_(e,d)(S0)<=N(e-d)<=N^2/2.
```

Their total is at most `N^3/4`.  Adding the two classes proves `(JW-1)`.

The exact `(e,d)` strata are disjoint.  Thus every unpaid nonconstant record
has `Delta_(e,d)<=0`; the difference-degree partition independently gives
`e>=t_XR+d+1`, proving `(JW-2)`.  Finally

```text
16N^3-1-5N^3/16=(251/16)N^3-1,
```

which proves the sufficient residual allowance. QED.
